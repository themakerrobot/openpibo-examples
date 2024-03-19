import openpibo
from openpibo.speech import Speech
from openpibo.audio import Audio

# tts.mp3 파일의 문자 데이터를 음성 언어로 변환 후, 파이보 스피커에 출력
def run():
  o_speech = Speech()
  o_audio = Audio()

  filename = openpibo.datapath + "/audio/tts.mp3"
  o_speech.tts("<speak>\
              <voice name='MAN_READ_CALM'>안녕하세요. 반갑습니다.<break time='500ms'/></voice>\
            </speak>"\
          , filename)
  o_audio.play(filename, volume=80)  # 파이보 스피커로 filename 출력

if __name__ == "__main__":
  run()
