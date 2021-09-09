from openpibo.motion import PyMotion

import time

m = PyMotion()

def move(n, speed, accel, degree):
  m.set_speed(n, speed)
  m.set_acceleration(n, accel)
  m.set_motor(n, degree)

# 2초 간격으로 move() 실행 무한 반복
def test():
  while True:
    move(2, 50, 0, 30)
    time.sleep(2)
  
    move(2, 50, 10, -30)
    time.sleep(2)

# Init 출력 -> move() -> 1초  휴식 -> Start 출력 -> test()
if __name__ == "__main__":
  print("Init")
  move(2, 20, 0, 0)
  time.sleep(1)

  print("Start")
  test()
