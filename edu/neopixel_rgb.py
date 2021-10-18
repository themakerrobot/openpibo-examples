import time
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.eye_on(0,255,0)
  print(ret)
  time.sleep(1.5)

  ret = pibo.eye_on(0,0,255,255,0,0)
  print(ret)
  time.sleep(1.5)

  pibo.eye_off()

if __name__ == '__main__':
  pibo = Pibo()

  run()
