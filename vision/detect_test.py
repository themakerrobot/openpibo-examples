import os
import sys

# 상위 디렉토리 추가 (for utils.config)
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

# openpibo 라이브러리 경로 추가
sys.path.append(cfg.OPENPIBO_PATH + '/lib')
from vision.visionlib import cCamera
from vision.visionlib import cDetect

def test_func():
  # instance
  cam = cCamera()
  det = cDetect(conf=cfg)

  # Capture / Read file
  img = cam.read()
  #img = cam.imread("image.jpg")

  print("Object Detect: ", det.detect_object(img))
  print("Qr Detect:", det.detect_qr(img))
  print("Text Detect:", det.detect_text(img))

if __name__ == "__main__":
  test_func()
