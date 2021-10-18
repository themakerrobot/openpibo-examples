import time
from openpibo.edu_v1 import Pibo

def run():
  # Version 1. Camera on
  pibo.start_thread_camera()
  pibo.start_thread_camera()
  time.sleep(1)
  pibo.capture()
  time.sleep(3)
  pibo.stop_thread_camera()

  # Version 2. Camera off
  pibo.capture('capture_cameraoff.png')

if __name__ == '__main__':
  pibo = Pibo()

  run()
