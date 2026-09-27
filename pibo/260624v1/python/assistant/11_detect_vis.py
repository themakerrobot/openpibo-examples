from openpibo.vision_camera import Camera
from openpibo.vision_detect import Detect
from openpibo.vision_face import Face

camera = Camera()
detect = Detect()
face = Face()

# 이미지 촬영
image = camera.read()

result_face = face.detect_face(image)      # [(x1, y1, x2, y2), ...]
result_object = detect.detect_object(image) # [{"name", "score", "box"}, ...]
result_qr = detect.detect_qr(image)         # [{"data", "type", "box"}, ...]

print('얼굴인식:', result_face)
print('사물인식:', result_object)
print('QR코드인식:', result_qr)

# visualize
if len(result_face):
  x1,y1,x2,y2 = result_face[0]
  image = camera.rectangle(image, (x1,y1), (x2,y2), (0,0,255), 2)

if len(result_object):
  for item in result_object:
    x1,y1,x2,y2 = item['box']
    name = item['name']
    image = camera.putTextPIL(image, name, (x1-10, y1-10), 20, (255, 255, 255))
    image = camera.rectangle(image, (x1,y1), (x2,y2), (255,255,0), 2)

for item in result_qr:
  print(item['data'])
  x1,y1,x2,y2 = item['box']
  image = camera.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 2)


# IDE에 표시
camera.imshow_to_ide(image, 1)
