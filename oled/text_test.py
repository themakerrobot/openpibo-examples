import os
import sys

# 상위 디렉토리 추가 (for utils.config)
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

# openpibo 라이브러리 경로 추가
sys.path.append(cfg.OPENPIBO_PATH + '/lib')
from oled.oledlib import cOled

def oled_f():
  oObj = cOled(conf=cfg)
  oObj.set_font(size=15)
  
  oObj.draw_text((0, 0), "안녕? 난 파이보야 ")
  oObj.draw_text((0,20), "☆  ★ ")
  oObj.show()

'''
  for count in range(5):
    oObj.clear()
    oObj.draw_text((10,10), "Hello World:{}".format(count))
    oObj.show()
    time.sleep(1)

  oObj.clear()
'''

if __name__ == "__main__":
  oled_f()
