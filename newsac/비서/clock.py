import time  
from openpibo.speech import Speech
from openpibo.audio import Audio
from openpibo.oled import Oled
from openpibo.device import Device

speech = Speech()
audio = Audio()
oled = Oled()
device = Device()

oled.set_font(size=15)

while True:
  device.eye_off()
  time_list = time.strftime('%Y,%m,%d,%H,%M,%S').split(',')

  if time_list[5] == '00': # 0초 일 때만 체크 > 분 단위
    device.eye_on(255, 0, 0, 255, 0, 0)
    speech.tts(string=f'{time_list[3]}시 {time_list[4]}분 입니다.', filename='voice.mp3', voice='main')
    audio.play('voice.mp3', 50)

  oled.draw_line((20, 25, 100, 25))
  oled.set_font(size=15)
  # 연-월-일
  oled.draw_text((20, 5), f'{time_list[0]}-{time_list[1]}-{time_list[2]}')
  oled.set_font(size=30)
  # 시-분-초
  oled.draw_text((0, 30), f'{time_list[3]}:{time_list[4]}:{time_list[5]}')
  oled.show()
  
  time.sleep(1)
  oled.clear(show=False)