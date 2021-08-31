from openpibo.vision import Camera
from openpibo.vision import Detect

def test_func():
  # instance
  cam = Camera()
  det = Detect()

  # Capture / Read file
  img = cam.read()
  #img = cam.imread("image.jpg")

  print("Object Detect: ", det.detect_object(img))
  print("Qr Detect:", det.detect_qr(img))
  print("Text Detect:", det.detect_text(img))

if __name__ == "__main__":
  test_func()
