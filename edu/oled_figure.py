import time
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.draw_figure((10,10,30,30), 'rectangle', True)
  print('first draw_figure() : ', ret)
  ret = pibo.draw_figure((70,40,90,60), 'circle', False)
  print('second draw_figure() : ', ret)
  ret = pibo.draw_figure((15,15,80,50), 'line')
  print('third draw_figure() : ', ret)
  ret = pibo.show_display()
  print('fist show_display() : ', ret)
  time.sleep(1.5)

  ret = pibo.invert()
  print('invert() : ', ret)
  ret = pibo.show_display()
  print('second show_display() : ', ret)
  time.sleep(1.5)

  ret = pibo.clear_display()
  print('clear_display() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
