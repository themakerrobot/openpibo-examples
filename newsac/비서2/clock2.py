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
  time_text = time.strftime('%Y-%m-%d,%H:%M:%S').split(',')
  second_text = time_text[1].split(':')[2]

  if second_text == '00':
    device.eye_on(255, 0, 0, 255, 0, 0)
    audio.play('/home/pi/openpibo-files/audio/piano/do.mp3', 80)

  oled.draw_line((20, 25, 100, 25))
  oled.set_font(size=15)
  oled.draw_text((20, 5), time_text[0])
  oled.set_font(size=30)
  oled.draw_text((0, 30), time_text[1])
  oled.show()
  
  time.sleep(1)
  oled.clear(show=False)