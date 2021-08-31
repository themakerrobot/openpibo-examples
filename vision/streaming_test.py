from openpibo.vision import Camera

def test_func():
  # instance
  cam = Camera()

  # For streaming (only GUI)
  cam.streaming(timeout=3)

if __name__ == "__main__":
  test_func()
