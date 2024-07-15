from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.motion import Motion
import time

MARKER_LENGTH = 8.5
# 인식할 마커 번호 목록
MARKER_LIST = [1, 9, 28, 29]
index = 0

# 상태> '직진' or '회전'
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

  for item in data:
    if item['id'] == _id:
      distance = item['distance']
      dX = get_dirX(item['center'][0])
      break
  return dX, distance

while True:
  print(f'[진행상태]: {STATE}')
  
  # '회전' 상태: 다음 마커를 찾기 위에 회전하는 상태
  if STATE == '회전':
    motion.set_motion('left')
    motion.set_motion('stop')

  time.sleep(2)
  image = camera.read()
  items = detect.detect_marker(image, MARKER_LENGTH)
  camera.imshow_to_ide(items['img'])
  dX, distance = engine(items['data'], MARKER_LIST[index])

  if dX == None or distance == None:
    if STATE != '회전':
      # '회전' 상태가 아닌데, 마커를 찾지 못했으면, 경로 이탈
      print(f'[인식불가]: 마커({MARKER_LIST[index]}) 인식 불가, 로봇 재배치 필요!')
  else:
    print(f'[마커인식]: {MARKER_LIST[index]} / {dX} / {distance}cm')
     
    if distance < 30:
      if len(MARKER_LIST) == index+1:
        print("[완료] 완주했습니다.")
        break      
      # 마커와의 거리가 30cm 이내이면, 다음 마커로 변경하고, 상태를 '회전'으로 변경
      # 다음 마커를 찾을 때까지 회전
      print(f'[마커번호 변경]: ({MARKER_LIST[index]} > {MARKER_LIST[index+1]})')
      STATE = '회전'
      index += 1
    else:
      # 마커 위치에 따라 우측/좌측/전진하여 마커가 중앙에 위치하도록 조정 (직진)
      # 마커와의 거리가 30cm 이상이기 때문에, 직진해야 함
      STATE = '직진'
      # right, left 동작의 _half는 좀 더 적은 회전
      if dX == '오른쪽':
        motion.set_motion('right_half')
      elif dX == '왼쪽':
        motion.set_motion('left_half')
      elif dX == '가운데':
        motion.set_motion('forward1')

      motion.set_motion('stop')