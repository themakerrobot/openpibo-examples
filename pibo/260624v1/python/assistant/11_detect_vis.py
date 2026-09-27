from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.vision import Face

camera = Camera()
detect = Detect()
face = Face()

# 이미지 촬영
image = camera.read()

result_face = face.detect_face(image)
result_object = detect.detect_object(image)
result_qr = detect.detect_qr(image)

print('얼굴인식:', result_face)
print('사물인식:', result_object)
print('QR코드인식:', result_qr)

# visualize
if len(result_face):
  x,y,w,h = result_face[0]
  image = camera.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

if len(result_object):
  for item in result_object:
    x1,y1,x2,y2 = item['position']
    name = item['name']
    image = camera.putTextPIL(image, name, (x1-10, y1-10), 20, (255, 255, 255))
    image = camera.rectangle(image, (x1,y1), (x2,y2), (255,255,0), 2)
  
if result_qr['data'] != '':
  print(result_qr['data'])
  x1,y1,x2,y2 = result_qr['position']
  image = camera.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 2)


# IDE에 표시
camera.imshow_to_ide(image, 1)

