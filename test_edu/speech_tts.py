import time
import os
data_path = os.path.dirname(os.path.abspath(__file__))+'/../data/'
from openpibo.edu_v1 import Pibo

def tts_test():
    pibo = Pibo()

    filename = data_path+"audio/tts.mp3"
    ret=pibo.tts("<speak><voice name='WOMAN_READ_CALM'>안녕. 나는 파이보야.<break time='500ms'/></voice></speak>", filename)
    print(ret)
    pibo.play_audio(filename, out='local', volume=-1500)
    time.sleep(2)
    
if __name__ == "__main__":
    tts_test()