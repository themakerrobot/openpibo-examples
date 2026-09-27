from openpibo.vision_camera import Camera
from openpibo.vision_face import Face

c = Camera()
f = Face()
f.load_db('facedata')

while True:
  img = c.read()
  faces = f.detect_face(img)

  if len(faces) == 0:
    print("no face")
  else:
    x1,y1,x2,y2 = faces[0]
    res = f.recognize(img, faces[0])
    print(res)
    c.rectangle(img, (x1,y1), (x2,y2), (255, 255, 255), 2)
    c.putText(img, f"{res['name']} / {res['score']}", (50,50), 1, (255, 255, 255), 1)
  c.imshow_to_ide(img)