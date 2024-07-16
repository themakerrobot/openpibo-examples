from openpibo.audio import Audio
from openpibo.speech import Speech
from openpibo.motion import Motion
from threading import Timer
import random

audio = Audio()
speech = Speech()
motion = Motion()

# voice mp3 미리 생성
filename = 'voice.mp3'
speech.tts(string='안녕하세요, 파이보입니다.', filename='voice.mp3', voice='main')

# mp3 재생 반복할 함수
# 안에서 mp3가 계속 재생됩니다.
def voice_loop(filename):
  while True:
    print("오디오 재생")
    # background=False는 음악 재생이 완료되어야 다음으로 넘어갑니다. (set_motion과 동일)
    # 기존 구현/블록에서는 음악 재생 완료와 상관없이 다음으로 넘어가서 sleep을 추가했습니다. 
    audio.play(filename, 60, background=False)

# voice_loop 함수 실행(비동기)
timer = Timer(0, voice_loop, args=(filename,)) # Timer( 실행주기-초, 실행할 함수, 매개변수 )
timer.daemon = True
timer.start()

# main loop
while True:
  # 만들어진 모션 중 1개씩 선택해서 반복합니다.
  motion_name = random.choice(motion.get_motion())
  print(motion_name)
  motion.set_motion(motion_name)