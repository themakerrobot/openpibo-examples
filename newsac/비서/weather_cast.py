from openpibo.collect import Weather
from openpibo.device import Device
from openpibo.oled import Oled
from openpibo.speech import Speech
from openpibo.audio import Audio
from openpibo.motion import Motion

device = Device()
oled = Oled()
speech = Speech()
audio = Audio()
weather = Weather()
motion = Motion()

# 서울 오늘 날씨
result = weather.search('서울')['today']
print(result)

# 눈 색상 표시하기
device.eye_on(0,255,255)

# 디스플레이에 최저/최고 기온 표시
oled.set_font(size=20)
oled.draw_text((0,0), '# 날씨')
oled.set_font(size=15)
oled.draw_text((0,25), result['minimum_temp'])
oled.draw_text((0,45), result['highst_temp'])
oled.show()

# 예보 음성 재생하기
speech.tts(string=result['weather'], filename='voice.mp3', voice='main')
audio.play('voice.mp3', 80)

# 동작 실행하기
motion.set_mymotion('weather')
motion.set_motion('stop')