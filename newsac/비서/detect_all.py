from openpibo.vision import Camera
from openpibo.vision import Detect
from openpibo.vision import Face

camera = Camera()
detect = Detect()
face = Face()

# 이미지 촬영
image = camera.read()

print("Face Detect:", face.detect_face(image)) # 얼굴 인식 
print("Object Detect:", detect.detect_object(image))  # 객체 인식
print("QR Detect:", detect.detect_qr(image))           # QR코드 인식

# IDE에 표시
camera.imshow_to_ide(image)