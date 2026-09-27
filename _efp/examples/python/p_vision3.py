from openpibo.vision import TeachableMachine
from openpibo.vision import Camera

tm = TeachableMachine()
camera = Camera()

tm.load('/home/pi/mymodel/model_unquant.tflite', '/home/pi/mymodel/labels.txt')
img = camera.read()

result = tm.predict(img)
print(result[0])