from openpibo.vision import Camera

camera = Camera()

# 이미지 촬영 / 파일 불러오기
image = camera.read()
#image = cam.imread("/home/pi/test.jpg")

# 저장(test.jpg라는 이름을 촬영한 이미지 저장)
camera.imwrite("test.jpg", image)

# IDE에 표시
camera.imshow_to_ide(image)