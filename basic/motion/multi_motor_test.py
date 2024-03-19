import time

from openpibo.motion import Motion

# 'set_motors() 실행 -> 1.1초 휴식 -> set_motors() 실행 -> 1.1초 휴식'을 무한 반복
def run():
  o = Motion()

  while True:
    o.set_motors(positions=[0,0,30,20, 30,0, 0,0,30,20], movetime=1000)
    time.sleep(1.1)
    o.set_motors(positions=[0,0,-30,-20, -30,0, 0,0,-30,-20], movetime=1000)
    time.sleep(1.1)

if __name__ == "__main__":
  run()
