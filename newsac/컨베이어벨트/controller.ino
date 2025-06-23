/*******************************************

사용법
#모터:각도!

모터
 - m1: 롤러용 서보 모터 (360도 연속 회전) / 0 ~+ (정방향)
       값의 범위는 일반적으로 -90 ~ +90 사이로 입력하여 속도와 방향을 제어합니다.
       90은 정지, 90보다 크면 정방향, 90보다 작으면 역방향으로 해석될 수 있으나,
       본 코드에서는 입력값을 상대적인 속도/방향 값으로 사용합니다.
       (예: 10은 정방향 속도, -10은 역방향 속도, 0은 정지 시도)
       실제 write 값은 (입력값 + DEFAULT_SERVO_ANGLE) 입니다.
 - m2: 분류용 서보 모터 (0도 ~ 180도 회전)
       값의 범위는 -90 ~ +90 사이로 입력하여 절대적인 각도를 나타냅니다.
       (예: 0은 중앙(90도), 30은 중앙에서 30도 더 간 위치(120도), -30은 중앙에서 30도 덜 간 위치(60도))
       실제 write 값은 (입력값 + DEFAULT_SERVO_ANGLE) 입니다.

예시
 - #m1:10!  > 롤러를 정방향으로 약한 속도로 회전 (실제 write: 100)
 - #m1:-10! > 롤러를 역방향으로 약한 속도로 회전 (실제 write: 80)
 - #m1:0!   > 롤러를 정지 시도 (실제 write: 90)
 - #m2:30!  > 분류용 서보 모터를 (90+30) = 120도 위치로 이동
 - #m2:-30! > 분류용 서보 모터를 (90-30) = 60도 위치로 이동
 - #m2:0!   > 분류용 서보 모터를 90도 (중앙) 위치로 이동


*******************************************/

#include <Servo.h>

// --- 상수 정의 ---
const int ROLLER_MOTOR_PIN = 5;
const int SORTING_MOTOR_PIN = 6;
const int DEFAULT_SERVO_ANGLE = 90; // 서보 모터 중간 각도 (연속 회전 서보의 경우 정지 각도)
const long SERIAL_BAUD_RATE = 9600;
const char PACKET_START_CHAR = '#';
const char PACKET_END_CHAR = '!';
const char PACKET_DELIMITER = ':';

// --- 서보 모터 객체 ---
Servo roller_motor;
Servo sorting_motor;

// --- 모터 현재 각도/값 저장 변수 ---
// 초기값을 DEFAULT_SERVO_ANGLE로 설정하여 실제 모터 위치와 일치시킴
int roller_motor_value = DEFAULT_SERVO_ANGLE;
int sorting_motor_value = DEFAULT_SERVO_ANGLE;

void setup() {
  Serial.begin(SERIAL_BAUD_RATE);

  roller_motor.attach(ROLLER_MOTOR_PIN);
  roller_motor.write(DEFAULT_SERVO_ANGLE); // 초기 위치 설정 (연속 회전 서보는 정지)
  //roller_motor.write(110);
  sorting_motor.attach(SORTING_MOTOR_PIN);
  sorting_motor.write(DEFAULT_SERVO_ANGLE); // 초기 위치 설정 (일반 서보는 중간 각도)

  Serial.println("** Conveyor Belt for piBrain (Improved with Usage Guide) **");
  Serial.println((String) "Initial roller_motor_value (represents written value): " + roller_motor_value);
  Serial.println((String) "Initial sorting_motor_value (represents written value): " + sorting_motor_value);
}

/**
 * @brief 롤러 모터(연속 회전 서보)를 지정된 상대 속도/방향으로 이동시킵니다.
 * @param v 이동할 상대 속도/방향 (-90 ~ +90). 0은 정지 시도.
 * 양수는 정방향, 음수는 역방향으로 해석됩니다.
 * 값이 클수록 속도가 빠릅니다. (실제 서보의 반응은 다를 수 있음)
 */
void move_roller_motor(int v) {
  // 입력값 v는 상대적인 속도/방향 값이므로, -90 ~ +90 범위를 가짐
  // 연속 회전 서보의 경우, write 값은 일반적으로 다음과 같이 해석됨:
  //   - 90: 정지
  //   - 0~89: 역방향 회전 (값이 작을수록 빠름)
  //   - 91~180: 정방향 회전 (값이 클수록 빠름)
  // 따라서, 입력값 v를 90을 기준으로 하는 값으로 변환합니다.
  int target_speed_value = v + DEFAULT_SERVO_ANGLE;
  
  // 서보 모터의 유효 입력 범위(0-180)로 제한
  target_speed_value = constrain(target_speed_value, 0, 180);
  
  roller_motor.write(target_speed_value);
  roller_motor_value = target_speed_value; // 현재 모터에 기록된 값 업데이트
  Serial.println((String)"Roller motor command value: " + v + ", written value: " + roller_motor_value); // 디버깅용
}

/**
 * @brief 분류 모터(일반 서보)를 지정된 상대 각도로 부드럽게 이동시킵니다.
 * @param v 이동할 상대 각도 (-90 ~ +90). 0은 DEFAULT_SERVO_ANGLE (중앙) 위치.
 */
void move_sorting_motor(int v) {
  // 입력값 v는 DEFAULT_SERVO_ANGLE(90도)을 기준으로 하는 상대 각도.
  // 서보 모터는 0 ~ 180 범위의 절대 각도를 사용하므로, DEFAULT_SERVO_ANGLE을 더해줌
  int target_angle = v + DEFAULT_SERVO_ANGLE;

  // 서보 모터의 유효 각도 범위(0-180)로 제한
  target_angle = constrain(target_angle, 0, 180);

  Serial.println((String)"Sorting motor command value: " + v + ", target angle: " + target_angle + ", current angle: " + sorting_motor_value); // 디버깅용

  if (target_angle > sorting_motor_value) {
    for (int current_angle_step = sorting_motor_value; current_angle_step <= target_angle; current_angle_step++) {
      sorting_motor.write(current_angle_step);
      delay(15); // 부드러운 움직임을 위한 지연 (값을 조절하여 속도 변경 가능)
    }
  } else if (target_angle < sorting_motor_value) {
    for (int current_angle_step = sorting_motor_value; current_angle_step >= target_angle; current_angle_step--) {
      sorting_motor.write(current_angle_step);
      delay(15); // 부드러운 움직임을 위한 지연
    }
  }
  // 목표 각도와 현재 각도가 같으면 아무것도 하지 않음 (이미 위에서 처리됨)
  // sorting_motor.write(target_angle); // 최종 위치 보정 (for 루프에서 이미 도달)
  sorting_motor_value = target_angle; // 현재 모터 각도 최종 업데이트
  Serial.println((String)"Sorting motor moved to angle: " + sorting_motor_value); // 디버깅용
}

void loop() {
  if (Serial.available()) {
    // 1) PACKET_END_CHAR('!')까지 읽고 공백 제거
    String pkt = Serial.readStringUntil(PACKET_END_CHAR);
    pkt.trim();

    // 패킷이 비어있는 경우 무시
    if (pkt.length() == 0) {
      return;
    }

    // 2) PACKET_START_CHAR('#')이 없으면 에러
    if (pkt.charAt(0) != PACKET_START_CHAR) { // Use charAt(0) for robust single character check
      Serial.println("Error: Invalid packet start. Expected '#'. Received: " + pkt);
    } else {
      // '#' 제거
      pkt.remove(0, 1); // 첫 번째 문자 '#' 제거

      // 첫 번째 콜론을 찾음
      int idx = pkt.indexOf(PACKET_DELIMITER);
      if (idx == -1) {
        // 콜론이 하나도 없으면 에러 처리
        Serial.println("Error: No delimiter '" + String(PACKET_DELIMITER) + "' found in packet => " + pkt);
        return;
      }

      // 콜론 앞은 opcode, 콜론 뒤는 data
      String opcode = pkt.substring(0, idx);
      String data_str = pkt.substring(idx + 1);

      // 데이터 문자열이 비어있는지 확인
      if (data_str.length() == 0) {
        Serial.println("Error: Data is empty for opcode: " + opcode);
        return;
      }
      
      // 데이터가 유효한 숫자인지 검사 (음수 부호, 숫자만 허용)
      bool isValidNumber = true;
      for (unsigned int i = 0; i < data_str.length(); i++) {
        if (i == 0 && data_str.charAt(i) == '-') continue; // 음수 부호 허용
        if (!isDigit(data_str.charAt(i))) {
          isValidNumber = false;
          break;
        }
      }
      
      if (!isValidNumber) {
        Serial.println("Error: Data is not a valid integer for opcode: " + opcode + ", data: " + data_str);
        return;
      }
      
      int data_val = data_str.toInt();

      // opcode 판별 후 처리
      if (opcode == "m1") {
        move_roller_motor(data_val);
      } else if (opcode == "m2") {
        move_sorting_motor(data_val);
      } else {
        Serial.println("Unknown opcode: " + opcode);
      }
    }
  }
}
