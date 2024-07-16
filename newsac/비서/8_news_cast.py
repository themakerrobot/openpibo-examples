from openpibo.collect import News
from openpibo.device import Device
from openpibo.oled import Oled
from openpibo.speech import Speech
from openpibo.audio import Audio
from openpibo.motion import Motion

device = Device()
oled = Oled()
speech = Speech()
audio = Audio()
news = News()
motion = Motion()

# '경제' 뉴스 첫번째 항목 가져오기 
result = news.search('경제')[0]
print(result)

# 눈 색상 표시하기
device.eye_on(0,255,255)

# 디스플레이에 뉴스 업데이트 날짜 표시
oled.set_font(size=20)
oled.draw_text((0,0), '# 뉴스')
oled.set_font(size=15)
oled.draw_text((0,25), result['pubDate'])
oled.show()

# 뉴스 제목 음성 재생하기
speech.tts(string='뉴스입니다.' + result['title'], filename='voice.mp3', voice='main')
audio.play('voice.mp3', 80)

# 동작 실행하기
# motion.set_mymotion('news')
motion.set_motion('speak1')
motion.set_motion('stop')