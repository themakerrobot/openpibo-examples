from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.motion import Motion
import time

camera = Camera()
detect = Detect()
motion = Motion()

def move(l, r, intv):
  data = [
    [10,     0, -70, -25,   0,   0,  20,    0,  70,  25],
    [999,  999, -80, 999, 999, 999, 999, -1*l,  60, 999],
    [999, -1*r, 999, 999, 999, 999, 999,  999, 999, 999],
    [999,  999, 999, 999, 999, 999,   0,  999, 999, 999],
    [-20,  999, 999, 999, 999, 999, -10,  999, 999, 999],
    [999,    r, -60, 999, 999, 999, 999,  999,  80, 999],
    [999,  999, 999, 999, 999, 999, 999,   l,  999, 999],
    [0,    999, 999, 999, 999, 999,   0,  999, 999, 999]
  ]

  for m in data:
    motion.set_motors(m, intv)
    time.sleep(intv/1000)
    
motion.set_motors([0, 0, 999, 999, 999, 999, 0, 0, 999, 999], 1000)

for i in range(10):
  move(35, 35, 300)
  motion.set_motors([0, 0, 999, 999, 999, 999, 0, 0, 999, 999], 500)
  image = camera.read()
  res = detect.marker_detect(image, 5.5)
  camera.imwrite(f'image-{i}.jpg', res['img'])
