import time
from openpibo.edu_v1 import Pibo

def run():
  while True:
    pibo.motor(2, 30, 100, 10)
    pibo.motor(8, 30, accel=10)
    time.sleep(1)

    pibo.motor(2, -30, 100, 10)
    pibo.motor(8, -30, speed=70)
    time.sleep(1)

if __name__ == '__main__':
  pibo = Pibo()

  run()
