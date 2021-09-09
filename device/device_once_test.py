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
  print('Send:', args.command)        # 실행한 명령어 출력
  data = obj.send_raw(args.command)   # Device에 메시지 전송하고 응답받음
  print('Receive:', data)             # Device로부터 받은 응답 출력
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser()  # 인자값을 받을 수 있는 인스턴스 생성
  parser.add_argument('--command', help='check specific decvice', required=True) #default=0, 입력받고자 하는 인자의 조건 설정
  args = parser.parse_args()          # 명령창(터미널)에 주어진 인자를 파싱하여 args에 저장
  main(args)                          # 입력받은 인자값을 인수로 main 함수 실행
