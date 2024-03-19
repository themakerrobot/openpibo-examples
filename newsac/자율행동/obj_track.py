from openpibo.vision import Camera
from openpibo.vision import Detect
from threading import Thread

image = None
result = None
tracker = None
TRAIN = False

camera = Camera()
detect = Detect()

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

def check_cmd():
  global TRAIN
  while True:
    if text_prompt('> ') == '학습':
      print("train")
      TRAIN = True
    
Thread(name='test', target=check_cmd, daemon=True).start()

while True:
  image = camera.read()
  if TRAIN == True:
    tracker = detect.object_tracker_init(image, (0,0,200,200))
    TRAIN = False
    print('학습')
  
  if tracker != None:
    result = detect.object_track(tracker, image)
    x1,y1,x2,y2 = result['position']
    camera.rectangle(image, (x1,y1), (x2,y2), (255,0,0), 3)
  camera.rectangle(image, (0,0), (200,200), (30,30,30), 1)
  camera.imshow_to_ide(image)