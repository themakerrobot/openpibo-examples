import time
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.start_thread_camera()
  print('start_thread_camera() : ', ret)
  time.sleep(3)
  
  face = pibo.search_face()
  print('search_face() : \n', face)
  
  ret = pibo.stop_thread_camera()
  print('stop_thread_camera() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
