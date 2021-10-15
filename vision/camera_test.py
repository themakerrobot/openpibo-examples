from openpibo.vision import Camera

def run(gui=False):
  o = Camera()

  # Capture / Read file
  # 이미지 촬영
  img = o.read()
  #img = cam.imread("/home/pi/test.jpg")

  # Write(test.jpg라는 이름을 촬영한 이미지 저장)
  o.imwrite("test.jpg", img)

  if gui:
    # display (only GUI): 3초동안 'TITLE' 이름의 윈도우 창에서 이미지 보여줌
    o.imshow(img, "TITLE")
    o.waitKey(3000) # 단위: ms

if __name__ == "__main__":
  run(gui=False)
