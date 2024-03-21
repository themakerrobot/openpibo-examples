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

device = Device()

command = '#20:255,0,0!'

print('Send:', command)        		# 실행한 명령어 출력
result = device.send_raw(command)   # Device에 메시지 전송하고 응답받음
print('Receive:', result)      		# Device로부터 받은 응답 출력