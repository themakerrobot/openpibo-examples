from openpibo.vision import Camera
from openpibo.vision import Detect

MARKER_LENGTH = 5.5
camera = Camera()
detect = Detect()

image = camera.read()
items = detect.detect_marker(image, MARKER_LENGTH)

for item in items['data']:
  _id = item['id']
  cx, cy = item['center']
  distance = item['distance']
  print(_id, (cx,cy), distance)

camera.imshow_to_ide(items['img'])