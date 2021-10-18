import time
from openpibo.edu_v1 import Pibo

def run():
  pibo.start_thread_camera()
  time.sleep(3)
  face = pibo.search_face()
  print(face)
  pibo.stop_thread_camera()

if __name__ == '__main__':
  pibo = Pibo()

  run()
