from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.vision import Face

camera = Camera()
detect = Detect()
face = Face()

# 이미지 촬영
image = camera.read()

res_face = face.detect_face(image) # 얼굴 인식 
res_object = detect.detect_object(image) # 객체 인식
res_qr = detect.detect_qr(image)          # QR코드 인식
print(res_face)
print(res_object)
print(res_qr)

# visualize
if len(res_face):
  x,y,w,h = res_face[0]
  image = camera.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

if len(res_object):
  for item in res_object:
    x1,y1,x2,y2 = item['position']
    name = item['name']
    image = camera.putTextPIL(image, name, (x1-10, y1-10), 20, (255, 255, 255))
    image = camera.rectangle(image, (x1,y1), (x2,y2), (255,255,0), 2)
  
if res_qr['data'] != '':
  print(res_qr['data'])
  x1,y1,x2,y2 = res_qr['position']
  image = camera.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 2)

# IDE에 표시
camera.imshow_to_ide(image, 1)