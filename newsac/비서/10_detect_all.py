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

# IDE에 표시
camera.imshow_to_ide(image, 1)