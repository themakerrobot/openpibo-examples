import os
data_path = os.path.dirname(os.path.abspath(__file__))+'/../data/'
from openpibo.oled import Oled

import time

def oled_f():
  oObj = Oled()
  oObj.draw_image(data_path+"image/clear.png")
  oObj.show()
  time.sleep(5)
  oObj.clear()
  oObj.show()

if __name__ == "__main__":
  oled_f()
