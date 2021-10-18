import time
from openpibo.edu_v1 import Pibo

def run():
  while True:
    pibo.motors_movetime(positions=[0,0,30,20, 30,0, 0,0,30,20], movetime=1000)
    time.sleep(1)
    pibo.motors_movetime(positions=[0,0,-30,-20, -30,0, 0,0,-30,-20])
    time.sleep(1)

if __name__ == '__main__':
  pibo = Pibo()

  run()
