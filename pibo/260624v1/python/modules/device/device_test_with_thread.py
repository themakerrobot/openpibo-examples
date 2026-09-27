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
import time
from threading import Thread
from queue import Queue
from openpibo.device import Device

def main_loop():
  # 현재 timestamp 얻기
  system_time = time.time()
  battery_time = time.time()

  while True:
    # queue에 메시지가 존재하면 하나씩 실행
    if queue.qsize() > 0:
      data = device.send_raw(queue.get())
      print("Message:", data)

    if time.time() - system_time > 1:  # 시스템 메시지 1초 간격 전송
      data = device.send_raw('#40:!')
      print("System:", data)
      system_time = time.time()

    if time.time() - battery_time > 10: # 배터리 메시지 10초 간격 전송
      data = device.send_raw('#15:!')
      print("Battery:", data)
      battery_time = time.time()

    time.sleep(0.01)


device = Device()
queue = Queue()

t = Thread(target=main_loop, args=())
t.daemon = True # main thread 종료시 update 메서드 종료
t.start()			  # update 메서드 실행

# main thread  
# 사용자가 q를 입력할 때까지 무한 반복, que에 pkt 삽입
while True:
  message = input("메시지를 입력하세요 > ")
  if message == '그만':
    break

  queue.put(message)
