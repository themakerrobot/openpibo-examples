from openpibo.device import Device
from openpibo.oled import Oled
from openpibo.speech import Speech
from openpibo.audio import Audio

device = Device()
oled = Oled()
speech = Speech()
audio = Audio()

# 눈 색상 표시하기
device.eye_on(0,255,255)

# 디스플레이에 이름(별명) 표시하기
oled.set_font(size=20)
oled.draw_image('/home/pi/openpibo-files/image/expression/smile.jpg')
#oled.draw_text((0,0), '안녕하세요')
oled.show()

# 음성으로 내 소개하기
speech.tts(string='안녕하세요, 파이보입니다.', filename='voice.mp3', voice='main')
audio.play('voice.mp3', 80)