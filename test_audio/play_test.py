import time

import openpibo
from openpibo.audio import Audio

def tts_f():
  obj = Audio()
  obj.play(filename=openpibo.data_path+"audio/test.mp3", out='local', volume=-2000)
  time.sleep(5)
  obj.stop()

if __name__ == "__main__":
  tts_f()
