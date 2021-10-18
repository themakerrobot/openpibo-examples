import time
from openpibo.edu_v1 import Pibo

def decode_message(msg):
  print(msg)
  if 'touch' in msg:
    pibo.eye_on(255,0,0)
  else:
    pibo.eye_off()

def run():
  ret = pibo.start_thread_device(decode_message)
  print(ret)
  time.sleep(12)
  pibo.stop_thread_device()

if __name__ == '__main__':
  pibo = Pibo()

  run()
