import openpibo
from openpibo.speech import Speech
from openpibo.audio import Audio

def tts_f():
  tObj = Speech()
  filename = openpibo.data_path+"/tts.mp3"
  tObj.tts("<speak>\
              <voice name='MAN_READ_CALM'>안녕하세요. 반갑습니다.<break time='500ms'/></voice>\
            </speak>"\
          , filename)
  print(filename)
  aObj = Audio()
  aObj.play(filename, out='local', volume=-1500)

if __name__ == "__main__":
  tts_f()
