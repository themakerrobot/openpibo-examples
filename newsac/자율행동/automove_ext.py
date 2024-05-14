from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.motion import Motion
import time

MARKER_LENGTH = 5.5
MARKER_LIST = [1, 9, 28, 29]
index = 0
STATE = '직진'
camera = Camera()
detect = Detect()
motion = Motion()

motion.set_motion('stop')

def get_dirX(x):
  if x > 420:
    dirX = "오른쪽" # right 
  elif x < 220:
    dirX = "왼쪽" # left
  else:
    dirX = "가운데" # center
  return dirX

def engine(data, _id):
  distance, dX = None, None
  for item in items['data']:
    if item['id'] == _id:
      distance = item['distance']
      dX = get_dirX(item['center'][0])
      break
  return dX, distance

while True:
  print(f'[진행상태]: {STATE}')
  if STATE == '회전':
    motion.set_motion('left')
    motion.set_motion('stop')

  time.sleep(2)
  image = camera.read()
  items = detect.detect_marker(image, MARKER_LENGTH)
  camera.imshow_to_ide(items['img'])

  if len(items['data']) == 0:
    if STATE != '회전':
      print("[마커인식불가]: 로봇 재배치 필요!")
  else:
    dX, distance = engine(items['data'], MARKER_LIST[index])

    if dX == None or distance == None:
      print(f'[마커인식불가]: {MARKER_LIST[index]} 마커 준비 필요!')
    else:
      print(f'[마커인식]: {MARKER_LIST[index]} / {dX} / {distance}cm')
      
      if distance < 30:
        print(f'[마커번호 변경]: ({MARKER_LIST[index]} > {MARKER_LIST[index+1]})')
        STATE = '회전'
        index += 1
      else:
        STATE = '직진'
      
      if dX == '오른쪽':
        motion.set_motion('right_half')
      elif dX == '왼쪽':
        motion.set_motion('left_half')
      elif dX == '가운데':
        motion.set_motion('forward1')

      motion.set_motion('stop')