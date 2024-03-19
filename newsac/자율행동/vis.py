from openpibo.vision import Camera

cam = Camera()

image = cam.read()

cam.line(image, (0, 0), (640, 480), '#ff0000', 4)

cam.imshow_to_ide(image)