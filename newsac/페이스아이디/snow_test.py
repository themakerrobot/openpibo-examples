from openpibo.vision import Camera
from openpibo.vision import Face
from openpibo.oled import OledbyILI9341 as Oled
import cv2

camera = Camera()
_face = Face()
oled = Oled()

ratio=0.6

mask = cv2.imread('/home/pi/code/mask.png', cv2.IMREAD_UNCHANGED)
_,_,_, alpha = cv2.split(mask)
mask_alpha = cv2.merge((alpha, alpha, alpha))

while True:
  image = camera.read()
  items = _face.detect_face(image)
  if len(items):
    x,y,w,h = items[0]
    
    x = max(0, int(x-ratio/2*x))
    y = max(0, int(y-ratio/2*y))
    w = min(int(x+ratio*w), 640-x)
    h = min(int(y+ratio*h), 480-y)

    # 얼굴 영역과 동일한 크기로 마스크 이미지 조정
    mask_alpha_resized = camera.resize(mask_alpha, w, h)
    mask_face = camera.resize(mask, w, h)

    # 얼굴 영역에 마스크 적용
    image[y:y+h, x:x+w] = mask_face[..., :3] + image[y:y+h, x:x+w] * (1 - mask_alpha_resized / 255)

  oled.draw_data(image)
  oled.show()
