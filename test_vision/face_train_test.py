from openpibo.vision import Camera
from openpibo.vision import Face

def test_func():
  # instance
  cam = Camera()
  faceObj = Face()

  print("Start DB:", faceObj.get_db()[0])
  
  # Capture / Read file
  img = cam.read()
  #img = cam.imread("/home/pi/test.jpg")

  # Train face
  faces = faceObj.detect(img)
  if len(faces) < 1:
    print(" No face")
  else:
    print(" Train:", faceObj.train_face(img, faces[0], "yjlee"))
  print("After Train, DB:", faceObj.get_db()[0])

  img = cam.read()
  faces = faceObj.detect(img)
  if len(faces) < 1:
    print(" No face")
  else:
    print(" Recognize:", faceObj.recognize(img, faces[0]))

  # Save DB
  faceObj.save_db("./facedb")

  # Reset DB
  faceObj.init_db()
  print("After reset db, DB:", faceObj.get_db()[0])
  
  # Load DB
  faceObj.load_db("facedb")
  print("After Load db, DB:", faceObj.get_db()[0])

  # delete Face
  faceObj.delete_face("yjlee")
  print("After Delete face:", faceObj.get_db()[0])

if __name__ == "__main__":
  test_func()
