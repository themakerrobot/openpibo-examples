'''
+ 메시지 구조
 - VERSION(10) ->  ex) #10:!
 - HALT(11) -> ex) #11:!
 - DC_CONN(14) -> ex) #14:!
 - BATTERY(15) -> ex) #15:!
 - NEOPIXEL(20) -> ex) #20:255,255,255!
 - NEOPIXEL_EACH(23) -> ex) #23:255,255,255,255,255,255!
 - PIR(30) -> ex) #30:!
 - TOUCH(31) -> ex) #31:!
 - SYSTEM(40) -> ex) #40:!
'''
import os
import sys

# 상위 디렉토리 추가 (for utils.config)
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

# openpibo 라이브러리 경로 추가
sys.path.append(cfg.OPENPIBO_PATH + '/lib')
from device.devicelib import cDevice

import argparse

def main(args):
  obj = cDevice()
  print('Send:', args.command)
  data = obj.send_raw(args.command)
  print('Receive:', data)
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--command', help='check specific decvice', required=True) #default=0
  args = parser.parse_args()
  main(args)
