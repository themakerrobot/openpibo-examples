import time
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.start_thread_camera()
  print('start_thread_camera()', ret)
  time.sleep(2)

  obj = pibo.search_object()
  qr = pibo.search_qr()
  print('Search Object: ', obj)
  print('Search QR: ', qr)
  
  ret = pibo.stop_thread_camera()
  print('stop_thread_camera() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
