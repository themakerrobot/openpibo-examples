# 마커 인식 기본 코드
from openpibo.vision import Camera
from openpibo.vision import Detect

# 마커의 실제 길이 (cm) - 마커 카드의 길이 8.5cm
MARKER_LENGTH = 8.5
camera = Camera()
detect = Detect()

image = camera.read()
items = detect.detect_marker(image, MARKER_LENGTH)

# _id: 마커 번호
# cx, cy: 마커의 중심 좌표
# 마커와 카메라와의 실제 거리(cm)
for item in items['data']:
  _id = item['id']
  cx, cy = item['center']
  distance = item['distance']
  print(_id, (cx,cy), distance)

camera.imshow_to_ide(items['img'])