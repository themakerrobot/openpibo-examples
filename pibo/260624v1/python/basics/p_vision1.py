from openpibo.vision_camera import Camera
from openpibo.vision_detect import Detect

camera = Camera()
detect = Detect()

image = camera.read()
camera.imwrite('/home/pi/code/image.jpg', image)
camera.imshow_to_ide(image)

cartoon = camera.stylization(image)
camera.imwrite('/home/pi/code/cartoon.jpg', cartoon)

# 사물 인식: [{"name": 이름, "score": 정확도, "box": (x1, y1, x2, y2)}, ...]
items = detect.detect_object(image)
print([ item['name'] for item in items])
print(items)

# QR/바코드 인식: 인식한 코드 전부를 리스트로 반환합니다.
# [{"data": 내용, "type": 종류, "box": (x1, y1, x2, y2)}, ...]
items = detect.detect_qr(image)
print([ item['data'] for item in items])
