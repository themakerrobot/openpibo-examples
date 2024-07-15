from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.motion import Motion
import time

# 마커의 실제 길이 (cm) - 마커 카드의 길이 8.5cm
MARKER_LENGTH = 8.5
# 마커 번호
MARKER_ID = 29

camera = Camera()
detect = Detect()
motion = Motion()

motion.set_motion('stop')

# 마커 위치 반환 함수(오른쪽/왼쪽/가운데)
def get_dirX(x):
  if x > 420:
    dirX = "오른쪽" # right 
  elif x < 220:
    dirX = "왼쪽" # left
  else:
    dirX = "가운데" # center
  return dirX

# 설정한 마커가 인식되었는지, 거리/마커위치(오른쪽/왼쪽/가운데) 반환하는 함수
def engine(data, _id):
  distance, dX = None, None
  
  # 설정한 마커(MARKER_ID)만 인식
  for item in data:
    if item['id'] == _id:
      distance = item['distance']
      dX = get_dirX(item['center'][0])
      break
  return dX, distance

while True:
  # 보행 중에 카메라(머리)가 흔들려서, 로봇이 완전히 정지하고 이미지 촬영 
  time.sleep(2)
  
  image = camera.read()
  
  # 마커 인식 함수
  # 입력: 이미지 / 실제 마커 길이
  # 반환: 딕셔너리{"data":마커 데이터, "img":마커가 표시된 이미지}
  #   - 마커 데이터: 딕셔너리{"id": 마커번호, "distance": 카메라와 마커의 실제거리, "center": 마커 중심 좌표}
  items = detect.detect_marker(image, MARKER_LENGTH)
  
  # 마커 표시된 이미지 IDE로 표시
  camera.imshow_to_ide(items['img'])

  # 인식된 마커가 있으면, engine함수를 통해 중심 x좌표, 거리를 가져옴
  dX, distance = engine(items['data'], MARKER_ID)

  if dX == None or distance == None:
    # 마커가 없거나, 다른 마커가 인식된 경우
    print(f'[인식불가]: 마커({MARKER_ID}) 인식 불가, 로봇 재배치 필요!')
  else:
    # 설정한 마커가 인식된 경우
    print(f'[마커인식]: {MARKER_ID} / {dX} / {distance}cm')

    # 마커 위치에 따라 좌우 회전/ 앞으로 이동하여, 직진할 수 있도록 함
    if dX == '오른쪽':
      motion.set_motion('right_half')
    elif dX == '왼쪽':
      motion.set_motion('left_half')
    elif dX == '가운데':
      motion.set_motion('forward1')
    motion.set_motion('stop')