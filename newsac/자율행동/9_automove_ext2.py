from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.vision import TeachableMachine
from openpibo.motion import Motion
import time

MARKER_LENGTH = 8.5
# 인식할 마커 번호 목록
MARKER_LIST = [1,2,3,4]
index = 0

STATE = '직진'

camera = Camera()
detect = Detect()
motion = Motion()
tm = TeachableMachine()

# 티쳐블머신 모델 불러오기
tm.load('/home/pi/mymodel/model_unquant.tflite', '/home/pi/mymodel/labels.txt')

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
  
  if STATE == '회전':
    motion.set_motion('left')
    motion.set_motion('stop')
  else:
    motion.set_motion('stop')

  time.sleep(2)
  image = camera.read()
  
  # 티쳐블머신 활용 카드 분류
  cardname, scores = tm.predict(image)
  score = int(max(scores)*100)
  if score > 90:
    # 카드 인식이 높은 확률(90%)로 되었을 때,
    print(f'[카드인식]: {cardname} {int(max(scores)*100)}%') 

  items = detect.detect_marker(image, MARKER_LENGTH)
  camera.imshow_to_ide(items['img'], 1)
  
  dX, distance = engine(items['data'], MARKER_LIST[index])
  if dX == None or distance == None:
    if STATE != '회전':
      # 마커가 없을 때, 좌우측 머리를 돌려서 마커가 있는지 2차 확인 기능 추가
      motion.set_motor(4, -30) # 목 오른쪽 이동
      time.sleep(1)
      image = camera.read()
      items = detect.detect_marker(image, MARKER_LENGTH)
      camera.imshow_to_ide(items['img'], 1)
      dX, distance = engine(items['data'], MARKER_LIST[index])

      if dX != None and distance != None:
        motion.set_motion('right') # 머리를 우측으로 돌린 상황에서 마커가 인식되었으므로 오른쪽 회전
      else:
        motion.set_motor(4, 30) # 목 왼쪽 이동
        time.sleep(1)
        image = camera.read()
        items = detect.detect_marker(image, MARKER_LENGTH)
        camera.imshow_to_ide(items['img'], 1)
        dX, distance = engine(items['data'], MARKER_LIST[index])

        if dX != None and distance != None:
          motion.set_motion('left') # 머리를 좌측으로 돌린 상황에서 마커가 인식되었으므로 왼쪽 회전
        else:
          # 좌우측 머리를 이동해도 마커를 못 찾을 때, 경로 이탈
          print(f'[마커인식불가]: {MARKER_LIST[index]} - 로봇 재배치 필요')
  else:
    print(f'[마커인식]: {MARKER_LIST[index]} / {dX} / {distance}cm')
     
    if distance < 30:
      if len(MARKER_LIST) == index+1:
        print("[완료] 완주했습니다.")
        break

      print(f'[마커번호 변경]: ({MARKER_LIST[index]} > {MARKER_LIST[index+1]})')
      STATE = '회전'
      index += 1
    else:
      STATE = '직진'
    
    if dX == '오른쪽':
      motion.set_motion('right')
    elif dX == '왼쪽':
      motion.set_motion('left')
    elif dX == '가운데':
      motion.set_motion('forward1')