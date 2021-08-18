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
'''
from openpibo.device import Device

if __name__ == "__main__":
  obj = Device()
  data = obj.send_cmd(obj.code['PIR'], "on")

  while True:
    pkt = input("")
    
    if pkt == 'q':
      break
    ret = obj.send_raw(pkt)
    print(ret)
