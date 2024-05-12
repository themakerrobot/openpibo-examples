from openpibo.audio import Audio
from openpibo.speech import Speech
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.collect import Wikipedia, Weather, News

audio = Audio()
speech = Speech()
motion = Motion()
device = Device()

device.eye_on(0,255,255, 0,255,255)

# wikipedia = Wikipedia()
# result = wikipedia.search_s('로봇') # 키워드 검색 결과 리스트
# print(result)
# ment = result[0]

# weather = Weather()
# result = weather.search_s('서울')
# print(result)
# ment = result

news = News()
result = news.search_s('속보')
print(result)
ment = result[0]

speech.tts(ment, 'tts.mp3', 'main')
audio.play('tts.mp3', 50)
#print(motion.get_motion())
motion.set_motion('speak1')
motion.set_motion('stop')

device.eye_off()