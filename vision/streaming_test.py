from openpibo.vision import Camera

# 모니터에 3초간 이미지 스트리밍
def test_func():
  # instance
  cam = Camera()

  # For streaming (only GUI)
  cam.streaming(timeout=3)

if __name__ == "__main__":
  test_func()
