# o_detect
import time
from openpibo.vision import Camera
from openpibo.vision import Detect

image = None
result = None

camera = Camera()
detect = Detect()

while True:
  image = camera.read()
  #result = [ item['name'] for item in detect.detect_object(image)]
  items = detect.detect_object(image)
  print(items)
  for item in items:
    x1,y1,x2,y2 = item['position']
    camera.rectangle(image, (x1,y1), (x2, y2), (255,255,255), 2)
  
  camera.imshow_to_ide(image)