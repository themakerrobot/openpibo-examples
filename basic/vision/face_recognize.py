from openpibo.vision import Camera
from openpibo.vision import Face

camera = Camera()
face = Face()

# First, execute face_train.py
face.load_db("facedb")

# Capture / Read file
image = camera.read()
#image = camera.imread("/home/pi/test.jpg")

# detect faces
faceList = face.detect_face(image)

if len(faceList) > 0:
  # get ageGender
  result = face.get_ageGender(image, faceList[0])
  age = result["age"]
  gender = result["gender"]

  x,y,w,h = faceList[0]
  # recognize using facedb(동일인이라 판정되면 이름, 아니면 Guest)
  ret = face.recognize(image, faceList[0])
  name = "Guest" if ret == False else ret["name"]

  print(f'{name}/ {gender} {age}')
  image = camera.rectangle(image, (x,y), (x+w, y+h))
  image = camera.putTextPIL(image, f'{name}/ {gender} {age}', (x-10, y-10), 30, (255, 255, 255)) # 화면의 (50,50) Hello Camera 쓰기

camera.imshow_to_ide(image)