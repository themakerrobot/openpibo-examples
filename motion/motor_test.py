from openpibo.motion import Motion

import time

m = Motion()

def move(n, degree, speed, accel):
  m.set_speed(n, speed)         # n번 모터의 속도를 speed로 변경
  m.set_acceleration(n, accel)  # n번 모터의 가속도를 accel로 변경
  m.set_motor(n, degree)        # n번 모터의 위치를 degree로 이동

# 'move() 실행 -> 1초 휴식 -> move() 실행 -> 1초 휴식'을 무한 반복
def test():
  while True:
    move(2, 30, 100, 10)
    move(8, 30,  10, 10)
    time.sleep(1)               # 단위: 초(sec)

    move(2, -30, 100, 10)
    move(8, -30,  10, 10)
    time.sleep(1)

if __name__ == "__main__":
  test()
