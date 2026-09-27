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

device = Device()

# q를 입력할 때까지 계속해서 명령어 입력 가능
while True:
  pkt = input("메시지를 입력하세요 > ")

  if pkt == '그만':
    break
  result = device.send_raw(pkt)
  print(result)
