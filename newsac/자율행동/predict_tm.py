from openpibo.vision import TeachableMachine
from openpibo.vision import Camera

tm = TeachableMachine()
camera = Camera()

MODEL_DIR = '/home/pi/mymodel/'
tm.load(MODEL_DIR+'model_unquant.tflite', MODEL_DIR+'labels.txt')
img = camera.read()

result = tm.predict(img)
print(result[0])