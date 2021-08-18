from openpibo.vision import Camera
from openpibo.vision import Face

def test_f():
  # instance
  cam = Camera()
  faceObj = Face()

  # Capture / Read file
  img = cam.read()
  #img = cam.imread("/home/pi/test.jpg")
 
  disp = img.copy()

  # detect faces
  faceList = faceObj.detect(img)

  if len(faceList) < 1:
    print("No face")
    return 
 
  # get ageGender
  ret = faceObj.get_ageGender(img, faceList[0])
  age = ret["age"]
  gender = ret["gender"]

  # draw rectangle
  x,y,w,h = faceList[0]  
  cam.rectangle(disp, (x,y), (x+w, y+h))

  # recognize using facedb
  ret = faceObj.recognize(img, faceList[0])
  name = "Guest" if ret == False else ret["name"]

  cam.putText(disp, "{}/ {} {}".format(name,gender,age), (x-10, y-10), size=0.5)

  # display (only GUI)
  cam.imshow(disp, "VIEW")
  cam.waitKey(3000)

  # Write
  cam.imwrite("test.jpg", disp)

if __name__ == "__main__":
  test_f()
