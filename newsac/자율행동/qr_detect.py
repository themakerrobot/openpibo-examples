# qr
from openpibo.vision import Camera
from openpibo.vision import Detect

image = None
result = None

camera = Camera()
detect = Detect()

while True:
  image = camera.read()
  result = detect.detect_qr(image)
  print(result)
  if result['position'] != None:
    x1,y1,x2,y2 = result['position']
    camera.rectangle(image, (x1,y1), (x2, y2), (255,255,255), 2)
  camera.imshow_to_ide(image)
