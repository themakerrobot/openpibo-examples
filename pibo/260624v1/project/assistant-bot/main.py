# -*- coding: utf-8 -*-
# 필요한 openpibo 라이브러리 및 표준 라이브러리를 임포트합니다.
from openpibo.vision import Camera, Detect, Face  # 카메라, 객체 감지(QR코드), 얼굴 감지
from openpibo.speech import Speech, Dialog       # 음성 합성(TTS), 대화 처리
from openpibo.audio import Audio                 # 오디오 재생
from openpibo.oled import Oled                   # OLED 디스플레이 제어
from openpibo.motion import Motion               # 로봇 모션 제어
from openpibo.collect import Weather, News       # 날씨, 뉴스 정보 수집
from openpibo.device import Device               # 로봇 장치 제어 (예: 눈 LED)
import time                                      # 시간 관련 기능 사용

# 각 라이브러리의 클래스 인스턴스를 생성합니다.
camera = Camera()       # 카메라 객체 생성
detect = Detect()       # 객체 감지 객체 생성 (QR코드 감지에 사용)
face = Face()           # 얼굴 감지 객체 생성
speech = Speech()       # 음성 합성 객체 생성
dialog = Dialog()       # 대화 객체 생성
audio = Audio()         # 오디오 재생 객체 생성
oled = Oled()           # OLED 디스플레이 객체 생성
motion = Motion()       # 모션 제어 객체 생성
weather = Weather()     # 날씨 정보 객체 생성
news = News()           # 뉴스 정보 객체 생성
device = Device()       # 장치 제어 객체 생성

# 파일 경로 및 설정값을 정의합니다.
IMAGE_DIR = '/home/pi/openpibo-files/image/'  # 이미지 파일이 저장된 기본 디렉토리 경로
AUDIO_DIR = '/home/pi/openpibo-files/audio/'  # 오디오 파일이 저장된 기본 디렉토리 경로
VOLUME = 50                                   # 오디오 재생 볼륨 설정 (0~100)
min_text = '-1'                               # 분 단위 알람 기능에서 이전 분을 저장하기 위한 변수 초기화

# 초기 설정을 수행합니다.
oled.set_font(size=30)                        # OLED 디스플레이의 폰트 크기를 30으로 설정
# "사진 찍을게요." 라는 안내 음성을 미리 생성하여 'photo.mp3' 파일로 저장 (효율성 증대)
speech.tts(string='사진 찍을게요.', filename='photo.mp3', voice='main')

# 메인 루프를 시작합니다. 프로그램은 이 루프를 계속 반복 실행합니다.
while True:
  # 현재 시간을 년, 월, 일, 시, 분, 초 단위로 나누어 리스트에 저장합니다.
  # 예: 2024년 7월 15일 10시 10분 5초 -> ['2024', '07', '15', '10', '10', '5']
  time_list = time.strftime('%Y,%m,%d,%H,%M,%S').split(',')
  print(time_list) # 현재 시간 리스트를 콘솔에 출력 (디버깅 목적)

  # 카메라로부터 현재 이미지를 읽어옵니다.
  image = camera.read()
  # 이미지에서 QR 코드를 감지합니다. 결과는 딕셔너리 형태로 반환됩니다.
  result = detect.detect_qr(image)
  # 이미지에서 얼굴을 감지합니다. 결과는 감지된 얼굴들의 좌표 리스트로 반환됩니다.
  items = face.detect_face(image)

  # 분 단위 알람 기능: 현재 분(time_list[4])이 이전에 저장된 분(min_text)과 다를 경우 실행
  if time_list[4] != min_text:
    oled.draw_image(IMAGE_DIR + 'machine/clock.jpg') # OLED에 시계 이미지를 표시
    oled.show()                                     # OLED 화면 업데이트
    # 현재 시와 분을 음성으로 안내하는 TTS 파일을 생성 ('voice.mp3')
    speech.tts(string=f'{time_list[3]}시 {time_list[4]}분 입니다.', filename='voice.mp3', voice='main')
    audio.play('voice.mp3', VOLUME)                 # 생성된 시간 안내 음성 파일을 재생
    min_text = time_list[4]                         # 현재 분을 min_text에 저장하여 다음 비교에 사용

  # 얼굴 감지 시 처리: 감지된 얼굴 리스트(items)의 길이가 0보다 크면 (얼굴이 감지되면) 실행
  if len(items) > 0:
    device.eye_on(0, 255, 255)                     # 로봇 눈 LED를 청록색(Cyan)으로 켭니다.
    x, y, w, h = items[0]                          # 첫 번째로 감지된 얼굴의 좌표와 크기를 가져옵니다.
    # 감지된 얼굴 주위에 흰색 사각형을 그립니다 (카메라 미리보기용).
    image = camera.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 3)
    oled.draw_image(IMAGE_DIR + 'expression/smile.jpg') # OLED에 웃는 표정 이미지를 표시
    oled.show()                                     # OLED 화면 업데이트
    # "안녕하세요." 인사말 TTS 파일을 생성 ('voice.mp3')
    speech.tts(string='안녕하세요.', filename='voice.mp3', voice='main')
    audio.play('voice.mp3', VOLUME)                 # 생성된 인사말 음성 파일을 재생
    motion.set_motion('greeting')                   # 'greeting' 모션을 실행 (인사 동작)
  # 얼굴이 감지되지 않았을 경우 실행
  else:
    device.eye_off()                               # 로봇 눈 LED를 끕니다.

  # 봇카드(QR 코드) 인식 시 기능 구현: 감지된 QR코드의 타입이 'CARD'일 경우 실행
  if result['type'] == 'CARD':
    print('봇카드를 인식했습니다.')                   # 콘솔에 봇카드 인식 메시지 출력

    # 봇카드 데이터에 따른 기능 분기
    if result['data'] == '날씨':                    # 카드 데이터가 '날씨'일 경우
      comment = weather.search('서울')['forecast']   # 서울 지역의 날씨 예보를 가져옵니다.
      oled.draw_image(IMAGE_DIR + 'weather/cloud.jpg') # OLED에 구름 이미지를 표시
      oled.show()                                   # OLED 화면 업데이트
      # 날씨 예보 안내 TTS 파일을 생성 ('voice.mp3')
      speech.tts(string='날씨를 알려드리겠습니다. ' + comment, filename='voice.mp3', voice='main')
      audio.play('voice.mp3', VOLUME)               # 생성된 날씨 안내 음성 파일을 재생
      motion.set_motion('speak1')                   # 'speak1' 모션을 실행 (말하는 동작)
    elif result['data'] == '뉴스':                  # 카드 데이터가 '뉴스'일 경우
      comment = news.search('뉴스랭킹')[0]['description'] # 뉴스 랭킹 첫 번째 기사의 설명을 가져옵니다.
      oled.draw_image(IMAGE_DIR + 'etc/star.jpg')     # OLED에 별 이미지를 표시
      oled.show()                                   # OLED 화면 업데이트
      # 뉴스 요약 안내 TTS 파일을 생성 ('voice.mp3')
      speech.tts(string='뉴스를 알려드리겠습니다. ' + comment, filename='voice.mp3', voice='main')
      audio.play('voice.mp3', VOLUME)               # 생성된 뉴스 안내 음성 파일을 재생
      motion.set_motion('speak1')                   # 'speak1' 모션을 실행 (말하는 동작)
    elif result['data'] == '체조':                  # 카드 데이터가 '체조'일 경우
      oled.draw_image(IMAGE_DIR + 'etc/person.jpg')   # OLED에 사람 이미지를 표시
      oled.show()                                   # OLED 화면 업데이트
      audio.play(AUDIO_DIR + 'music/exercise.mp3', VOLUME) # 미리 준비된 체조 음악 파일을 재생
      motion.set_motion('dance4')                   # 'dance4' 모션을 실행 (체조/춤 동작)
      audio.stop()                                  # 모션 종료 후 음악 재생 중지
    elif result['data'] == '대화':                  # 카드 데이터가 '대화'일 경우
      oled.draw_image(IMAGE_DIR + 'expression/joke.jpg') # OLED에 농담/대화 표정 이미지를 표시
      oled.show()                                   # OLED 화면 업데이트
      # 콘솔(터미널)에서 사용자 입력을 받아 질문(Q>)으로 사용하고, Dialog 객체로 답변을 생성합니다.
      # 주의: 이 부분은 로봇 자체에서 사용자 입력을 받는 방식이 아니라,
      # 코드를 실행하는 컴퓨터의 터미널에서 입력을 받아야 합니다.
      comment = dialog.get_dialog(input("Q>"))
      # 답변 내용을 TTS 파일로 생성 ('voice.mp3')
      speech.tts(string='답변드리겠습니다. ' + comment, filename='voice.mp3', voice='main')
      audio.play('voice.mp3', VOLUME)               # 생성된 답변 음성 파일을 재생
      motion.set_motion('speak1')                   # 'speak1' 모션을 실행 (말하는 동작)
    elif result['data'] == '카메라':                # 카드 데이터가 '카메라'일 경우
      oled.draw_image(IMAGE_DIR + 'game/scissors.jpg') # OLED에 가위 이미지를 표시 (카메라 관련 아이콘으로 사용된 듯)
      oled.show()                                   # OLED 화면 업데이트
      audio.play('photo.mp3', VOLUME)               # 미리 생성된 "사진 찍을게요." 음성 파일을 재생
      time.sleep(3)                                 # 3초간 대기
      # 사진 촬영 카운트다운을 OLED에 표시합니다.
      for n in ['- 3 -', '- 2 -', '- 1 -', '찰칵!']:
        oled.clear()                                # OLED 화면 내용을 지웁니다.
        oled.draw_text((30, 20), n)                 # 카운트다운 텍스트를 (30, 20) 위치에 표시
        oled.show()                                 # OLED 화면 업데이트
        time.sleep(1)                               # 각 단계마다 1초씩 대기
      # 새로운 이미지를 카메라에서 읽어 'photo.jpg' 파일로 저장합니다.
      camera.imwrite('photo.jpg', camera.read())
    else:                                           # 인식된 카드 데이터가 위 경우들에 해당하지 않으면
      pass                                          # 아무 작업도 수행하지 않습니다.

  # 현재 진행 중인 모션이 있다면 정지시킵니다 (다음 루프 시작 전 상태 초기화 목적일 수 있음).
  motion.set_motion('stop')
  # 현재 카메라 뷰(얼굴 감지 시 사각형 포함)를 IDE(통합개발환경)의 미리보기 창으로 전송합니다.
  camera.imshow_to_ide(image)

# while True 루프는 사용자가 프로그램을 강제 종료하지 않는 한 계속 실행됩니다.