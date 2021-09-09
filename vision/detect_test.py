from openpibo.vision import Camera
from openpibo.vision import Detect

def test_func():
  # instance
  cam = Camera()  # Camera 클래스에 대한 객체 생성
  det = Detect()

  # Capture / Read file
  img = cam.read()
  #img = cam.imread("image.jpg")

  print("Object Detect: ", det.detect_object(img))  # 객체 인식
  print("Qr Detect:", det.detect_qr(img))           # QR코드 인식
  print("Text Detect:", det.detect_text(img))       # 문자 인식

if __name__ == "__main__":
  test_func()
