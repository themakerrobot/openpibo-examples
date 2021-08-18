import time

import os
data_path = os.path.dirname(os.path.abspath(__file__))+'/../data/'
from openpibo.edu_v1 import Pibo

def audio_test():
    pibo = Pibo()
    ret=pibo.play_audio(filename=data_path+"audio/test.mp3", out='local', volume=-2000)
    print(ret)
    time.sleep(3)
    pibo.stop_audio()

if __name__ == "__main__":
    audio_test()