import time
from openpibo.audio import Audio

AUDIO_PATH = '/home/pi/openpibo-files/audio'

o = Audio()
o.play(filename=AUDIO_PATH + "/effect/opening.mp3", volume=60)
time.sleep(5) # 5초동안 프로세스 정지
o.stop()