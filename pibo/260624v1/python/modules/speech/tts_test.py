from openpibo.speech import Speech
from openpibo.audio import Audio

# tts.mp3 파일의 문자 데이터를 음성 언어로 변환 후, 파이보 스피커에 출력
speech = Speech()
audio = Audio()

filename = "tts.mp3"
speech.tts("안녕하세요. 반갑습니다.", voice='main', filename=filename)
audio.play(filename, volume=60)  # 파이보 스피커로 filename 출력