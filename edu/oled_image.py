import time
import openpibo
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.draw_image(openpibo.datapath + '/image/clear.png')
  print('draw_image() : ', ret)
  ret = pibo.show_display()
  print('show_display() : ', ret)
  time.sleep(2)

  ret =pibo.clear_display()
  print('clear_display() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
