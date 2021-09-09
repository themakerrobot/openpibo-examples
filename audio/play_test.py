import time

import openpibo
from openpibo.audio import Audio

# test.mp3 파일 5초 재생 후 정지
def tts_f():
  obj = Audio()
  obj.play(filename=openpibo.config['DATA_PATH']+"audio/test.mp3", out='local', volume=-2000)
  time.sleep(5) # 5초동안 프로세스 정지
  obj.stop()

if __name__ == "__main__":
  tts_f()
