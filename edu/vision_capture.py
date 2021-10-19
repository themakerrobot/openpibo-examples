import time
from openpibo.edu_v1 import Pibo

def run():
  # Version 1. Camera on
  ret = pibo.start_thread_camera()
  print('start_thread_camera() : ', ret)
  time.sleep(1)

  ret = pibo.capture()
  print('first capture() : ', ret)
  time.sleep(3)

  ret = pibo.stop_thread_camera()
  print('stop_thread_camera() : ', ret)

  # Version 2. Camera off
  ret = pibo.capture('capture_cameraoff.png')
  print('second captutre() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
