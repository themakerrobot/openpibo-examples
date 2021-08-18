import time

import os
data_path = os.path.dirname(os.path.abspath(__file__))+'/../data/'
from openpibo.audio import Audio

def tts_f():
  obj = Audio()
  obj.play(filename=data_path+"audio/test.mp3", out='local', volume=-2000)
  time.sleep(5)
  obj.stop()

if __name__ == "__main__":
  tts_f()
