from openpibo.vision import Camera

def run(gui=False):
  o = Camera()

  # Capture / Read file
  img = o.read()
  #img = cam.imread("/home/pi/test.jpg")

  # Draw rectangle, Text
  o.rectangle(img, (100,100), (300,300))    # 화면의 (100,100), (300,300) 위치에 사각형 그리기
  o.putText(img, "Hello Camera", (50, 50))  # 화면의 (50,50) Hello Camera 쓰기

  # Write
  o.imwrite("test.jpg", img)  # test.jpg로 이미지 저장

  if gui:
    # display (only GUI): 3초동안 'TITLE'이라는 제목으로 이미지 보여줌
    o.imshow(img, "TITLE")
    o.waitKey(3000)

if __name__ == "__main__":
  run(gui=False)
