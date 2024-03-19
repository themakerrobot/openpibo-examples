import time

import openpibo
from openpibo.audio import Audio

o = Audio()
o.play(filename=openpibo.datapath + "/audio/effect/opening.mp3", volume=30)
time.sleep(5) # 5초동안 프로세스 정지
o.stop()