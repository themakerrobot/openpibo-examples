from openpibo.vision import Camera

def test_func():
  # instance
  cam = Camera()

  # Capture / Read file
  img = cam.read()
  #img = cam.imread("/home/pi/test.jpg")

  # Write
  cam.imwrite("test.jpg", img)

  # display (only GUI)
  cam.imshow(img, "TITLE")
  cam.waitKey(3000)

if __name__ == "__main__":
  test_func()
