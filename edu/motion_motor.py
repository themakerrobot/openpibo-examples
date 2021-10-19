import time
from openpibo.edu_v1 import Pibo

def run():
  while True:
    ret = pibo.motor(2, 30, 100, 10)
    print('first motor()  : {}'.format(ret))
    
    ret = pibo.motor(8, 30, accel=10)
    print('second motor() : {}'.format(ret))

    time.sleep(1)

    ret = pibo.motor(2, -30, 100, 10)
    print('third motor()  : {}'.format(ret))

    ret = pibo.motor(8, -30, speed=70)
    print('fourth motor()  : {}'.format(ret))
    time.sleep(1)

if __name__ == '__main__':
  pibo = Pibo()

  run()
