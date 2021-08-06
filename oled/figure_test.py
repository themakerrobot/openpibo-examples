import os
import sys

# 상위 디렉토리 추가 (for utils.config)
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

# openpibo 라이브러리 경로 추가
sys.path.append(cfg.OPENPIBO_PATH + '/lib')
from oled.oledlib import cOled

import time

def oled_f():
  oObj = cOled(conf=cfg)
  oObj.clear()
  oObj.draw_rectangle((10,10,30,30) ,True)
  oObj.draw_ellipse((70,40,90,60) ,False)
  oObj.draw_line((15,15,80,50))
  oObj.show()

if __name__ == "__main__":
  oled_f()
