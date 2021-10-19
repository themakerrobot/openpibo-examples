import time
from openpibo.edu_v1 import Pibo

def run():
  while True:
    ret = pibo.motors(
      positions=[0,0,0,10,0,10,0,0,0,20],
      speeds=[0,0,0,15,0,10,0,0,0,10], 
      accels=[0,0,10,5,0,0,0,0,5,10]
    )
    print('first motors() : ', ret)
    time.sleep(1)

    pibo.motors(
      positions=[0,0,0,-10,0,-10,0,0,0,-20],
      speeds=[0,0,0,15,0,10,0,0,0,10],
    )
    print('second motores() : ', ret)
    time.sleep(1)

if __name__ == '__main__':
  pibo = Pibo()

  run()
