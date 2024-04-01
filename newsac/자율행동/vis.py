from openpibo.vision import Camera

camera = Camera()

image = camera.read()

camera.line(image, (0, 0), (640, 480), '#ff0000', 4)
camera.line(image, (640, 0), (0, 480), '#ff0000', 4)

camera.imshow_to_ide(image)