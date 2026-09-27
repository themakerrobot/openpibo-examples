from openpibo.vision_camera import Camera
from openpibo.vision_face import Face

c = Camera()
f = Face()

name = "iu"

img = c.read()
faces = f.detect_face(img)

if len(faces) == 0:
  print("no face")

face = faces[0]
f.train_face(img, face, name)
f.save_db('facedata')

x1,y1,x2,y2 = face

c.rectangle(img, (x1,y1), (x2,y2), (255, 255, 255), 2)
c.imshow_to_ide(img)