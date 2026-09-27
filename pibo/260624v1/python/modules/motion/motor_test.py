import time
from openpibo.motion import Motion

motion = Motion()

def move(n, p, s, a):
  motion.set_speed(n, s)         # n번 모터의 속도를 s로 변경
  motion.set_acceleration(n, a)  # n번 모터의 가속도를 a로 변경
  motion.set_motor(n, p)        # n번 모터의 위치를 p로 이동

# 'move() 실행 -> 3초 휴식 -> move() 실행 -> 3초 휴식'을 무한 반복
while True:
  move(2, 30, 100, 10)
  move(8, 30,  10, 10)
  time.sleep(3) # 단위: 초(sec)

  move(2, -30, 100, 10)
  move(8, -30,  10, 10)
  time.sleep(3)