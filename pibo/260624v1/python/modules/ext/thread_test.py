from threading import Timer
import time

def a():
  print('thread-start')
  time.sleep(1)
  print('thread-1')
  time.sleep(1)
  print('thread-2')  
  time.sleep(1)
  print('thread-3')
  time.sleep(1)
  print('thread-4')
  time.sleep(1)
  print('thread-5')
  
  print('thread-end')
  
t = Timer(1, a)
t.daemon = True
t.start()

while True:
  print(time.time())
  time.sleep(0.1)