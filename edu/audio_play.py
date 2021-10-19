import time
import openpibo
from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.play_audio(filename=openpibo.config['DATA_PATH']+'/audio/test.mp3', out='local', volume=-2000)
  print('play_audio() : ', ret)
  time.sleep(3)

  ret = pibo.stop_audio()
  print('stop_audio() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
