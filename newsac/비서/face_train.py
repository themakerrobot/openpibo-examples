from openpibo.vision import Camera, Face

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

x,y,w,h = face

c.rectangle(img, (x,y), (x+w, y+h), (255, 255, 255), 2)
c.imshow_to_ide(img)