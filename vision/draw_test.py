from openpibo.vision import Camera

def test_func():
  # instance
  cam = Camera()

  # Capture / Read file
  img = cam.read()
  #img = cam.imread("/home/pi/test.jpg")

  # Draw rectangle, Text
  cam.rectangle(img, (100,100), (300,300))    # 화면의 (100,100), (300,300) 위치에 사각형 그리기
  cam.putText(img, "Hello Camera", (50, 50))  # 화면의 (50,50) Hello Camera 쓰기

  # Write
  cam.imwrite("test.jpg", img)  # test.jpg로 이미지 저장

  # display (only GUI): 3초동안 'TITLE'이라는 제목으로 이미지 보여줌
  cam.imshow(img, "TITLE")
  cam.waitKey(3000)

if __name__ == "__main__":
  test_func()
