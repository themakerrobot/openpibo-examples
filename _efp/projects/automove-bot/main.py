# 필요한 openpibo 라이브러리 및 표준 라이브러리를 임포트합니다.
from openpibo.vision import Camera           # 카메라 제어
from openpibo.vision import Detect           # 객체 감지 (마커 감지에 사용)
from openpibo.vision import TeachableMachine # 티처블 머신 모델 사용
from openpibo.motion import Motion           # 로봇 모션 제어
import time                                  # 시간 관련 함수 사용 (예: sleep)

# 마커의 실제 길이(cm)를 정의합니다. 거리 계산에 사용됩니다.
MARKER_LENGTH = 8.5
# 로봇이 순서대로 찾아야 할 마커의 ID 목록입니다.
MARKER_LIST = [10, 20, 21, 23]
# 현재 찾아야 할 마커의 인덱스를 저장하는 변수입니다. MARKER_LIST의 인덱스입니다.
index = 0

# 로봇의 현재 상태를 나타내는 변수입니다. '직진' 또는 '회전' 상태를 가집니다.
STATE = '직진'

# 각 라이브러리의 클래스 인스턴스를 생성합니다.
camera = Camera()         # 카메라 객체 생성
detect = Detect()         # 객체 감지 객체 생성 (마커 감지용)
motion = Motion()         # 모션 제어 객체 생성
tm = TeachableMachine() # 티처블 머신 객체 생성

# 학습된 티처블 머신 모델 파일과 라벨 파일을 로드합니다.
# 모델 파일 경로는 실제 파일 위치에 맞게 수정해야 할 수 있습니다.
tm.load('/home/pi/mymodel/model_unquant.tflite', '/home/pi/mymodel/labels.txt')

# 마커의 x 좌표를 입력받아 로봇 시야 기준 '왼쪽', '가운데', '오른쪽' 중 어디에 있는지 반환하는 함수입니다.
def get_dirX(x):
  # 이미지 너비가 640이라고 가정할 때의 기준값입니다. (카메라 해상도에 따라 조절 필요)
  if x > 420:
    dirX = "오른쪽" # right
  elif x < 220:
    dirX = "왼쪽" # left
  else:
    dirX = "가운데" # center
  return dirX

# 감지된 마커 데이터(data)와 찾아야 할 마커 ID(_id)를 입력받아,
# 해당 ID의 마커가 감지되었으면 그 마커의 x축 방향(dX)과 거리(distance)를 반환하는 함수입니다.
# 마커가 없으면 None, None을 반환합니다.
def engine(data, _id):
  distance, dX = None, None # 거리와 방향 초기화
  # 감지된 모든 마커(item)에 대해 반복
  for item in data:
    # 현재 마커의 ID가 찾고 있는 ID(_id)와 일치하는지 확인
    if item['id'] == _id:
      distance = item['distance']         # 일치하면 거리 정보 저장
      dX = get_dirX(item['center'][0])  # 일치하면 x 좌표로 방향 계산 후 저장
      break                             # 해당 ID 마커를 찾았으므로 반복 중단
  return dX, distance                   # 계산된 방향과 거리 반환 (못 찾았으면 None, None)

# 메인 루프 시작: 로봇이 마커를 따라 이동하는 로직을 반복 실행합니다.
while True:
  # 현재 로봇의 진행 상태를 콘솔에 출력합니다.
  print(f'[진행상태]: {STATE}')

  # 로봇 상태가 '회전'일 경우, 제자리에서 왼쪽으로 회전하는 모션을 실행합니다.
  if STATE == '회전':
    motion.set_motion('left') # 왼쪽으로 회전 (다음 마커를 찾기 위함)

  # 일단 정지합니다. (이미지 처리 및 판단 시간 확보)
  motion.set_motion('stop')
  time.sleep(2) # 2초 대기 (로봇 안정화 및 카메라 준비)

  # 카메라로부터 현재 이미지를 읽어옵니다.
  image = camera.read()

  # ---- 티처블 머신 활용 부분 ----
  # 현재 이미지에서 티처블 머신으로 학습된 카드(객체)를 분류합니다.
  cardname, scores = tm.predict(image)
  # 가장 높은 확률 값을 정수로 변환합니다.
  score = int(max(scores) * 100)
  # 인식 확률이 90%를 넘으면, 인식된 카드 이름과 확률을 출력합니다.
  if score > 90:
    print(f'[카드인식]: {cardname} {score}%')
  # ---- 티처블 머신 활용 부분 끝 ----

  # 현재 이미지에서 마커를 감지합니다. MARKER_LENGTH는 거리 계산에 사용됩니다.
  # items 딕셔너리에는 감지 결과 이미지('img')와 감지된 마커 정보 리스트('data')가 포함됩니다.
  items = detect.detect_marker(image, MARKER_LENGTH)
  # 감지 결과 이미지를 IDE 미리보기 창에 표시합니다. (1ms 동안 표시)
  camera.imshow_to_ide(items['img'], 1)

  # engine 함수를 호출하여 현재 찾아야 할 마커(MARKER_LIST[index])의 방향(dX)과 거리(distance)를 얻습니다.
  dX, distance = engine(items['data'], MARKER_LIST[index])

  # 마커를 찾지 못했을 경우 (dX나 distance가 None일 경우)
  if dX == None or distance == None:
    # 현재 상태가 '회전'이 아닐 때만 (직진 중 마커를 놓쳤을 때만) 2차 탐색 시도
    if STATE != '회전':
      print(f'[마커 탐색]: {MARKER_LIST[index]} - 정면에서 찾지 못함. 좌우 탐색 시작.')
      # --- 오른쪽 탐색 ---
      motion.set_motor(4, -20) # 목(모터 4번)을 오른쪽으로 약간 돌립니다. 각도 조절 필요.
      time.sleep(2)           # 목 움직임 대기
      image = camera.read()     # 목을 돌린 상태에서 이미지 다시 촬영
      items = detect.detect_marker(image, MARKER_LENGTH) # 마커 재탐색
      camera.imshow_to_ide(items['img'], 1)             # 결과 이미지 표시
      dX, distance = engine(items['data'], MARKER_LIST[index]) # 재탐색 결과 분석

      # 오른쪽에서 마커를 찾았을 경우
      if dX != None and distance != None:
        print(f'[마커 탐색]: {MARKER_LIST[index]} - 오른쪽에서 발견. 오른쪽으로 회전.')
        motion.set_motion('right') # 몸 전체를 오른쪽으로 회전
      # 오른쪽에서도 못 찾았을 경우
      else:
        # --- 왼쪽 탐색 ---
        motion.set_motor(4, 20) # 목(모터 4번)을 왼쪽으로 돌립니다. (중앙 위치를 지나 왼쪽으로)
        time.sleep(2)          # 목 움직임 대기 (오른쪽 -> 중앙 -> 왼쪽 이동 시간 고려)
        image = camera.read()    # 목을 돌린 상태에서 이미지 다시 촬영
        items = detect.detect_marker(image, MARKER_LENGTH) # 마커 재탐색
        camera.imshow_to_ide(items['img'], 1)            # 결과 이미지 표시
        dX, distance = engine(items['data'], MARKER_LIST[index]) # 재탐색 결과 분석

        # 왼쪽에서 마커를 찾았을 경우
        if dX != None and distance != None:
          print(f'[마커 탐색]: {MARKER_LIST[index]} - 왼쪽에서 발견. 왼쪽으로 회전.')
          motion.set_motion('left') # 몸 전체를 왼쪽으로 회전
        # 왼쪽에서도 못 찾았을 경우 (최종적으로 못 찾음)
        else:
          # 로봇의 목을 다시 중앙으로 되돌리는 동작 추가 (선택 사항)
          motion.set_motor(4, 0)
          print(f'[마커 인식 불가]: {MARKER_LIST[index]} - 좌우 탐색 실패. 로봇 재배치 필요.')
          # 여기서 프로그램을 종료하거나, 다른 예외 처리 로직을 넣을 수 있습니다.
          # 예: break 또는 특정 위치로 이동 등
  # 마커를 성공적으로 찾았을 경우
  else:
    # 찾은 마커의 ID, 방향, 거리를 출력합니다.
    print(f'[마커 인식]: {MARKER_LIST[index]} / {dX} / {distance}cm')

    # 마커와의 거리가 30cm 미만으로 가까워졌을 경우
    if distance < 30:
      # 현재 마커가 마지막 마커인지 확인합니다.
      if len(MARKER_LIST) == index + 1:
        print("[완료] 모든 마커를 통과했습니다.")
        motion.set_motion('stop') # 최종 정지
        break # 메인 루프를 종료합니다.

      # 마지막 마커가 아니라면, 다음 마커를 찾아야 함을 알리고 상태를 '회전'으로 변경합니다.
      print(f'[마커 번호 변경]: ({MARKER_LIST[index]} -> {MARKER_LIST[index+1]})')
      STATE = '회전' # 다음 마커를 찾기 위해 회전 상태로 변경
      index += 1   # 다음 마커 인덱스로 업데이트
    # 마커와의 거리가 아직 30cm 이상일 경우
    else:
      STATE = '직진' # 계속 현재 마커를 향해 직진 상태 유지

    # 마커의 방향(dX)에 따라 로봇의 움직임을 결정합니다.
    if dX == '오른쪽':
      motion.set_motion('right_half') # 오른쪽으로 조금 회전하며 전진 (또는 제자리 회전)
    elif dX == '왼쪽':
      motion.set_motion('left_half')  # 왼쪽으로 조금 회전하며 전진 (또는 제자리 회전)
    elif dX == '가운데':
      motion.set_motion('forward1')   # 마커가 중앙에 있으므로 직진

# 루프 종료 후 (모든 마커 통과 시) 추가 정리 코드 (필요시)