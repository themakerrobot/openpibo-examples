from openpibo.vision_camera import Camera
from openpibo.vision_detect import Detect
from openpibo.vision_face import Face
from openpibo.speech import Speech, Dialog
from openpibo.audio import Audio
from openpibo.oled import Oled
from openpibo.motion import Motion
from openpibo.collect import Weather, News
from openpibo.device import Device
import time

camera = Camera()
detect = Detect()
face = Face()
speech = Speech()
dialog = Dialog()
audio = Audio()
oled = Oled()
motion = Motion()
weather = Weather()
news = News()
device = Device()

IMAGE_DIR = '/home/pi/openpibo-files/image/'
AUDIO_DIR = '/home/pi/openpibo-files/audio/'
VOLUME = 50
min_text = '-1'

oled.set_font(size=30)
speech.tts(text='사진 찍을게요.', filename='photo.mp3', voice='main')

while True:
  # 현재 시간 확인 2024년 7월 15일 10시 10분 5초 라면, 
  # time_list = ['2024','07','15','10','10','5']
  time_list = time.strftime('%Y,%m,%d,%H,%M,%S').split(',')
  print(time_list)
  
  image = camera.read()
  qr_items = detect.detect_qr(image)
  # 260624v1부터 detect_qr은 인식한 코드 전부를 리스트로 반환합니다. 첫 번째 것만 사용합니다.
  result = qr_items[0] if qr_items else {'data': '', 'type': '', 'box': None}
  items = face.detect_face(image)

  # 분 단위 알람 기능
  if time_list[4] != min_text:
    oled.draw_image(IMAGE_DIR + 'machine/clock.jpg')
    oled.show()
    speech.tts(text=f'{time_list[3]}시 {time_list[4]}분 입니다.', filename='voice.mp3', voice='main')
    audio.play('voice.mp3', VOLUME)
    min_text = time_list[4]

  # 얼굴을 찾았을 때, 인사
  if len(items) > 0:
    device.eye_on(0,255,255)
    x1,y1,x2,y2 = items[0]
    image = camera.rectangle(image, (x1,y1), (x2,y2), (255,255,255), 3)
    oled.draw_image(IMAGE_DIR + 'expression/smile.jpg')
    oled.show()
    speech.tts(text='안녕하세요.', filename='voice.mp3', voice='main')
    audio.play('voice.mp3', VOLUME)
    motion.set_motion('greeting')
  else:
    device.eye_off()
  
  # 봇카드 인식 시, 기능 구현
  if result['type'] == 'CARD':
    print('봇카드를 인식했습니다.')
    if result['data'] == '날씨':
      comment = weather.search('서울')['forecast']
      oled.draw_image(IMAGE_DIR + 'weather/cloud.jpg')
      oled.show()
      speech.tts(text='날씨를 알려드리겠습니다. '+comment, filename='voice.mp3', voice='main')
      audio.play('voice.mp3', VOLUME)
      motion.set_motion('speak1')
    elif result['data'] == '뉴스':
      comment = news.search('뉴스랭킹')[0]['description']
      oled.draw_image(IMAGE_DIR + 'etc/star.jpg')
      oled.show()
      speech.tts(text='뉴스를 알려드리겠습니다. '+comment, filename='voice.mp3', voice='main')
      audio.play('voice.mp3', VOLUME)
      motion.set_motion('speak1')      
    elif result['data'] == '체조':
      oled.draw_image(IMAGE_DIR + 'etc/person.jpg')
      oled.show()
      audio.play(AUDIO_DIR+'music/exercise.mp3', VOLUME)
      motion.set_motion('dance4')
      audio.stop()
    elif result['data'] == '대화':
      oled.draw_image(IMAGE_DIR + 'expression/joke.jpg')
      oled.show()
      comment = dialog.get_dialog(input("Q>"))
      speech.tts(text='답변드리겠습니다. ' + comment, filename='voice.mp3', voice='main')
      audio.play('voice.mp3', VOLUME)
      motion.set_motion('speak1')
    elif result['data'] == '카메라':
      oled.draw_image(IMAGE_DIR + 'game/scissors.jpg')
      oled.show()
      audio.play('photo.mp3', VOLUME)
      time.sleep(3)
      for n in ['- 3 -', '- 2 -', '- 1 -', '찰칵!']:
        oled.clear()
        oled.draw_text((30,20), n)
        oled.show()
        time.sleep(1)
      camera.imwrite('photo.jpg', camera.read())
    else:
      pass
  
  motion.set_motion('stop')
  camera.imshow_to_ide(image)