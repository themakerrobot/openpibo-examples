from openpibo.vision import Camera
from openpibo.vision import Face

camera = Camera()
face = Face()

print("Start DB:", face.get_db()[0])
  
# Capture / Read file
img = camera.read()
#img = o_cam.imread("/home/pi/test.jpg")

# Train face
faces = face.detect_face(img)
if len(faces) < 1:
  print(" No face")
else:
  # 얼굴 학습(학습할  이미지 데이터, 얼굴 1개 위치, 학습할 얼굴 이름)
  print(" Train:", face.train_face(img, faces[0], "yjlee"))
print("After Train, DB:", face.get_db()[0])

img = camera.read()
items = face.detect_face(img)
if len(items) < 1:
  print(" No face")
else:
  print(" Recognize:", face.recognize(img, items[0]))

# Save DB
face.save_db("./facedb")

# Reset DB
face.init_db()
print("After reset db, DB:", face.get_db()[0])
  
# Load DB
face.load_db("facedb")
print("After Load db, DB:", face.get_db()[0])

# delete Face
face.delete_face("yjlee")
print("After Delete face:", face.get_db()[0])