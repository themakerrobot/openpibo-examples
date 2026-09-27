from openpibo.vision_camera import Camera
from openpibo.vision_face import Face

camera = Camera()
face = Face()

# First, execute face_train.py
face.load_db("facedb")

# Capture / Read file
image = camera.read()
#image = camera.imread("/home/pi/test.jpg")

# detect faces: [(x1, y1, x2, y2), ...]
faceList = face.detect_face(image)

if len(faceList) > 0:
  # 나이·성별·감정 추정: {"age", "gender", "emotion", "box"}
  result = face.analyze_face(image, faceList[0])
  age = result["age"]
  gender = result["gender"]

  x1,y1,x2,y2 = faceList[0]
  # recognize using facedb(동일인이라 판정되면 이름, 아니면 Guest)
  ret = face.recognize(image, faceList[0])
  name = "Guest" if ret == False else ret["name"]

  print(f'{name}/ {gender} {age}')
  image = camera.rectangle(image, (x1,y1), (x2,y2))
  image = camera.putTextPIL(image, f'{name}/ {gender} {age}', (x1-10, y1-10), 30, (255, 255, 255))

camera.imshow_to_ide(image)
