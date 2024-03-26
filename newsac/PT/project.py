from openpibo.oled import OledbyILI9341 as Oled
from openpibo.vision import Camera, vision_api, Detect
import cv2
import time

oled = Oled()
camera = Camera()
detect = Detect()

actions = ["양팔올리기", "왼팔올리기", "오른팔올리기"]

NOSE, LEFT_EYE, RIGHT_EYE, LEFT_EAR, RIGHT_EAR = 0,1,2,3,4
LEFT_SHOULDER, RIGHT_SHOULDER, LEFT_ELBOW, RIGHT_ELBOW, LEFT_WRIST, RIGHT_WRIST = 5,6,7,8,9,10
LEFT_HIP, RIGHT_HIP, LEFT_KNEE, RIGHT_KNEE, LEFT_ANKLE, RIGHT_ANKLE = 11,12,13,14,15,16

print("[AI-PT] 초기화 완료")
t = 0
while True:
  oled.clear(show=False, fill=False)
  img = camera.read()
  
  print("[AI-PT] 사람 체크")
  objs = detect.detect_object(img)
  objs = [item['name'] for item in objs]
  
  print(objs)
  if "person" in objs:
    print(" 사람 인식")
    
    result = detect.detect_pose(img)
    data = result['data'][0].keypoints
    
    if data[LEFT_WRIST].coordinate.y < data[LEFT_ELBOW].coordinate.y:
      print("  - 왼손 위")
      left_hand = "↑"
    else:
      left_hand = "↓"
    if data[RIGHT_WRIST].coordinate.y < data[RIGHT_ELBOW].coordinate.y:
      print("  - 오른손 위")
      right_hand = "↑"
    else:
      right_hand= "↓"
   
    pose = detect.analyze_pose(result)
    
    
    pose = "양팔올리기"
    print(pose, t, "초")
    t = t+1
    
    if t == 6:
      print(" ", pose, "성공")
      break
    
    oled.draw_data(img)
    oled.set_font(size=10)
    oled.draw_text((5,5), f'오른손 {right_hand}, 왼손 {left_hand}', (0,0,0))
    oled.draw_text((5,15), f'행동: {pose}', (0,0,0))
    oled.draw_text((5,25), "시간: 5초 (성공)", (0,0,0))    
  oled.show()
  camera.imshow_to_ide(img)
