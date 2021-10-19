import time
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.eye_on(0,255,0)
  print('first eye_on() : ', ret)
  time.sleep(1.5)

  ret = pibo.eye_on(0,0,255,255,0,0)
  print('second eye_on() : ', ret)
  time.sleep(1.5)

  ret = pibo.eye_off()
  print('eye_off() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
