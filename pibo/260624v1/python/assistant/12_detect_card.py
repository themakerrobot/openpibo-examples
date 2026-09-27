from openpibo.vision import Camera
from openpibo.vision import Detect

camera = Camera()
detect = Detect()

image = camera.read()
result_qr = detect.detect_qr(image)

print("카드 인식:",result_qr)
camera.imshow_to_ide(image, 1)