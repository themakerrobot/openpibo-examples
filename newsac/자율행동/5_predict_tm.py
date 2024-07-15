from openpibo.vision import TeachableMachine
from openpibo.vision import Camera

tm = TeachableMachine()
camera = Camera()

MODEL_DIR = '/home/pi/mymodel/'

# 티쳐블머신 모델 불러오기
tm.load(MODEL_DIR+'model_unquant.tflite', MODEL_DIR+'labels.txt')

# 이미지 촬영
img = camera.read()

# 티쳐블머신 모델로 이미지 분류
result = tm.predict(img)
print(result[0])