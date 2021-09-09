import openpibo
from openpibo.speech import Speech
from openpibo.audio import Audio

# tts.mp3 파일의 문자 데이터를 음성 언어로 변환 후, 파이보 스피커에 출력
def tts_f():
  tObj = Speech()
  filename = openpibo.config['DATA_PATH']+"audio/tts.mp3"
  tObj.tts("<speak>\
              <voice name='MAN_READ_CALM'>안녕하세요. 반갑습니다.<break time='500ms'/></voice>\
            </speak>"\
          , filename)
  print(filename)
  aObj = Audio()
  aObj.play(filename, out='local', volume=-1500)  # 파이보 스피커로 filename 출력

if __name__ == "__main__":
  tts_f()
