from openpibo.vision import Camera
from openpibo.vision import Detect

def run():
  o_cam = Camera()
  o_det = Detect()

  # Capture / Read file
  img = o_cam.read()
  #img = cam.imread("image.jpg")

  print("Object Detect: ", o_det.detect_object(img))  # 객체 인식
  print("QR Detect:", o_det.detect_qr(img))           # QR코드 인식

if __name__ == "__main__":
  run()
