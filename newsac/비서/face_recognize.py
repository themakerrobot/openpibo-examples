from openpibo.vision import Camera, Face

c = Camera()
f = Face()
f.load_db('facedata')

while True:
  img = c.read()
  faces = f.detect_face(img)

  if len(faces) == 0:
    print("no face")
  else:
    x,y,w,h = faces[0]
    res = f.recognize(img, faces[0])
    print(res)
    c.rectangle(img, (x,y), (x+w, y+h), (255, 255, 255), 2)
    c.putText(img, f"{res['name']} / {res['score']}", (50,50), 1, (255, 255, 255), 1)
  c.imshow_to_ide(img)