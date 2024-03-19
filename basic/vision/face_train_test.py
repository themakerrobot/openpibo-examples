from openpibo.vision import Camera
from openpibo.vision import Face

def run(gui=False):
  # instance
  o_cam = Camera()
  o_face = Face()

  print("Start DB:", o_face.get_db()[0])
  
  # Capture / Read file
  img = o_cam.read()
  #img = o_cam.imread("/home/pi/test.jpg")

  # Train face
  faces = o_face.detect(img)
  if len(faces) < 1:
    print(" No face")
  else:
    # 얼굴 학습(학습할  이미지 데이터, 얼굴 1개 위치, 학습할 얼굴 이름)
    print(" Train:", o_face.train_face(img, faces[0], "pibo"))
  print("After Train, DB:", o_face.get_db()[0])

  img = o_cam.read()
  faces = o_face.detect(img)
  if len(faces) < 1:
    print(" No face")
  else:
    print(" Recognize:", o_face.recognize(img, faces[0]))

  # Save DB
  o_face.save_db("./facedb")

  # Reset DB
  o_face.init_db()
  print("After reset db, DB:", o_face.get_db()[0])
  
  # Load DB
  o_face.load_db("facedb")
  print("After Load db, DB:", o_face.get_db()[0])

  # delete Face
  o_face.delete_face("yjlee")
  print("After Delete face:", o_face.get_db()[0])

if __name__ == "__main__":
  run(gui=False)
