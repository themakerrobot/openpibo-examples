from openpibo.vision import Camera

camera = Camera()

# 이미지 촬영 / 파일 불러오기
image = camera.read()
#image = cam.imread("/home/pi/test.jpg")

  # Draw rectangle, Text
image = camera.rectangle(image, (100,100), (300,300))    # 화면의 (100,100), (300,300) 위치에 사각형 그리기
image = camera.putTextPIL(image, '안녕하세요.', (15, 10), 30, (255, 255, 255)) # 화면의 (50,50) Hello Camera 쓰기

# 저장(test.jpg라는 이름을 촬영한 이미지 저장)
camera.imwrite("test.jpg", image)

# IDE에 표시
camera.imshow_to_ide(image)