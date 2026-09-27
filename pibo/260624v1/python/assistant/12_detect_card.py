from openpibo.vision_camera import Camera
from openpibo.vision_detect import Detect

camera = Camera()
detect = Detect()

image = camera.read()
result_qr = detect.detect_qr(image)

print("카드 인식:",result_qr)
camera.imshow_to_ide(image, 1)