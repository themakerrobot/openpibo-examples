import openpibo
from openpibo.oled import Oled

import time

def oled_f():
  oObj = Oled()
  oObj.draw_image(openpibo.config['DATA_PATH']+"images/clear.png")
  oObj.show()
  time.sleep(5)
  oObj.clear()
  oObj.show()

if __name__ == "__main__":
  oled_f()
