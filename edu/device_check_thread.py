import time
from openpibo.edu_v1 import Pibo

def decode_message(msg):
  print('message from firmware : ', msg)
  
  if 'touch' in msg:
    ret = pibo.eye_on(255,0,0)
    print('eye_on() : ', ret)
  else:
    ret = pibo.eye_off()
    print('eye_off() : ', ret)

def run():
  ret = pibo.start_thread_device(decode_message)
  print('start_thread_device() : ', ret)

  time.sleep(12)
  
  ret = pibo.stop_thread_device()
  print('stop_thread_device() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
