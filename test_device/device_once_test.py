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
from openpibo.device import Device

import argparse

def main(args):
  obj = Device()
  print('Send:', args.command)
  data = obj.send_raw(args.command)
  print('Receive:', data)
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--command', help='check specific decvice', required=True) #default=0
  args = parser.parse_args()
  main(args)
