import time
import openpibo
from openpibo.edu_v1 import Pibo

def run():
  pibo.draw_image(openpibo.config['DATA_PATH']+'/image/clear.png')
  pibo.show_display()
  time.sleep(2)

  pibo.clear_display()

if __name__ == '__main__':
  pibo = Pibo()

  run()
