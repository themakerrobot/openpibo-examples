from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.motion import Motion
import time

camera = Camera()
detect = Detect()
motion = Motion()

def move(l, r, intv):
  data = [
    [10,     0, -70, -25,   0,  10,  20,    0,  70,  25],
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
         
def get_dirX(x):
  if x > 420:
    dirX = "Right"  
  elif x < 220:
    dirX = "Left"
  else:
    dirX = "Center"
  return dirX

def engine(data):
  distance, dX = None, None
  for item in items['data']:
    _id = item['id']
    if _id == mark:
      distance = item['distance']
      dX = get_dirX(item['center'][0])
      break
  return dX, distance

motion.set_motion('stop')
time.sleep(2)

mark = 29

while True:
  print('center')
  time.sleep(2)
  image = camera.read()
  items = detect.detect_marker(image, 5.5)
  camera.imshow_to_ide(items['img'])

  if len(items['data']) == 0:
    print('right')
    motion.set_motor(4, -30)
    time.sleep(2)
    image = camera.read()
    items = detect.detect_marker(image, 5.5)
    camera.imshow_to_ide(items['img'])
    
    if len(items['data']) == 0:
      print('left')
      motion.set_motor(4, 30)
      time.sleep(2)
      image = camera.read()
      items = detect.detect_marker(image, 5.5)
      camera.imshow_to_ide(items['img'])
      if len(items['data']) == 0:
        print("lost")
      else: # left
        print('move left')
        move(30, 15, 250)
        motion.set_motion('stop')
    else: # right
      print('move right')
      move(15, 30, 250)
      motion.set_motion('stop')
  else: # center 
    dX, distance = engine(items['data'])
    print(f'[{mark}]: {dX} {distance}cm')

    if dX == "Right":
      move(15, 30, 250)
    elif dX == "Left":
      move(30, 15, 250)
    else:
      move(35, 35, 250)

    motion.set_motion('stop')