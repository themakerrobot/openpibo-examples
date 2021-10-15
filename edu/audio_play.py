import time

import openpibo
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.play_audio(filename=openpibo.config['DATA_PATH']+"/audio/test.mp3", out='local', volume=-2000)
  print(ret)
  time.sleep(3)
  pibo.stop_audio()

if __name__ == "__main__":
  pibo = Pibo()

  run()
