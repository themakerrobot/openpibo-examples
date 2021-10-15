from openpibo.vision import Camera
from openpibo.vision import Face

def run(gui=False):
  # instance
  o_cam = Camera()
  o_face = Face()

  # Capture / Read file
  img = o_cam.read()
  #img = cam.imread("/home/pi/test.jpg")
 
  disp = img.copy()

  # detect faces
  faceList = o_face.detect(img)

  if len(faceList) < 1:
    print("No face")
    return 
 
  # get ageGender
  result= o_face.get_ageGender(img, faceList[0])
  age = result["age"]
  gender = result["gender"]

  # draw rectangle
  x,y,w,h = faceList[0]  
  o_cam.rectangle(disp, (x,y), (x+w, y+h))

  # recognize using facedb(동일인이라 판정되면 이름, 아니면 Guest)
  result = o_face.recognize(img, faceList[0])
  name = "Guest" if result == False else ret["name"]

  print(f'{name}/ {gender} {age}')
  o_cam.putText(disp, f'{name}/ {gender} {age}', (x-10, y-10), size=0.5)

  if gui:
    # display (only GUI): 모니터에서 3초간 VIEW라는 제목으로 이미지 확인
    o_cam.imshow(disp, "VIEW")
    o_cam.waitKey(3000)

  # Write: test.jpg로 이미지 저장
  o_cam.imwrite("test.jpg", disp)

if __name__ == "__main__":
  run(gui=False)
