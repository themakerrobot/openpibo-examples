import time

import openpibo
from openpibo.edu_v1 import Pibo

def run():
  filename = openpibo.config['DATA_PATH']+"/audio/tts.mp3"
  ret = pibo.tts(string="안녕, 나는 파이보야", voice_type='WOMAN_READ_CALM', break_time=500, filename=filename)
  print(ret)
  pibo.play_audio(filename, out='local', volume=-1500)
  time.sleep(2)

if __name__ == "__main__":
  pibo = Pibo()

  run()
