from openpibo.vision import Camera
from openpibo.vision import Detect

camera = Camera()
detect = Detect()

image = camera.read()
camera.imwrite('/home/pi/code/image.jpg', image)
camera.imshow_to_ide(image)

cartoon = camera.stylization(image)
camera.imwrite('/home/pi/code/cartoon.jpg', cartoon)

items = detect.classify_image(image)
print([ item['name'] for item in items])
print(items)

items = detect.detect_object(image)
print([ item['name'] for item in items])
print(items)

print(detect.detect_qr(image)['data'])