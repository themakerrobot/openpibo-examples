import time

from openpibo.motion import PyMotion

def move(n, p, s, a):
  o.set_speed(n, s)         # n번 모터의 속도를 s로 변경
  o.set_acceleration(n, a)  # n번 모터의 가속도를 a로 변경
  o.set_motor(n, p)        # n번 모터의 위치를 p로 이동

# 2초 간격으로 move() 실행 무한 반복
def run():
  while True:
    move(2, 30, 50,  0)
    move(8, 30, 50, 10)
    time.sleep(2)
  
    move(2,-30, 50,  0)
    move(8,-30, 50, 10)
    time.sleep(2)

if __name__ == "__main__":
  o = PyMotion()
  
  run()
