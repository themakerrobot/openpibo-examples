import time
from openpibo.edu_v1 import Pibo

def run():
  while True:
    pibo.motors(
      positions=[0,0,0,10,0,10,0,0,0,20],
      speeds=[0,0,0,15,0,10,0,0,0,10], 
      accels=[0,0,10,5,0,0,0,0,5,10]
    )
    time.sleep(1)

    pibo.motors(
      positions=[0,0,0,-10,0,-10,0,0,0,-20],
      speeds=[0,0,0,15,0,10,0,0,0,10],
    )
    time.sleep(1)

if __name__ == '__main__':
  pibo = Pibo()

  run()
