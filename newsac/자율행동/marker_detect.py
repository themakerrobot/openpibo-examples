from openpibo.vision import Camera
from openpibo.vision import Detect

MARKER_LENGTH = 5.5
camera = Camera()
detect = Detect()

RANGE = 50

def check_pos(x, y):
  if x > 420:
    dirX = "Right"  
  elif x < 220:
    dirX = "Left"
  else:
    dirX = "Center"

  if y > 340:
    dirY = "Bottom"
  elif y < 140:
    dirY = "Top"  
  else:
    dirY = "Center"
  return dirX, dirY

while True:
  image = camera.read()
  items = detect.detect_marker(image, MARKER_LENGTH)

  camera.rectangle(image, (220, 140), (420, 340), (255,255,255), 2)
  
  for item in items['data']:
    _id = item['id']
    cx, cy = item['center']
    distance = item['distance']
    print(_id, check_pos(cx, cy), distance)

  camera.imshow_to_ide(items['img'])