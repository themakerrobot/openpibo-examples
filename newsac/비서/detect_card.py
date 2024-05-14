from openpibo.vision import Camera
from openpibo.vision import Detect

camera = Camera()
detect = Detect()

while True:
  image = camera.read()
  print("QR Detect:", detect.detect_qr(image))
  camera.imshow_to_ide(image)