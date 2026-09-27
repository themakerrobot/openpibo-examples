from openpibo.vision import Camera

camera = Camera()
image = camera.read() # 이미지 촬영하기

# 화면의 (100,100), (300,300) 위치에 (255,255,0) 색상, 두께 2의 사각형 그리기
image = camera.rectangle(image, (100,100), (300,300), (255,0,0), 2)

# 화면의 0, 0 위치에 글자크기 30인 “안녕하세요“ 문자 쓰기
image = camera.putTextPIL(image, '안녕하세요.', (0, 0), 30, (0, 0, 255))

# image 변수를 test.jpg 저장
camera.imwrite('test.jpg', image)

# IDE 뷰어에 표시
camera.imshow_to_ide(image, 1)