import time
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.draw_text((10,10), '안녕하세요. Hello', 15)
  print('draw_text() : ', ret)
  ret = pibo.show_display()
  print('show_display() : ', ret)
  time.sleep(2)

  ret = pibo.clear_display()
  print('clear_display() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
