from openpibo.vision_camera import Camera
from openpibo.vision_detect import Detect

camera = Camera()
detect = Detect()

img = camera.read()
result = detect.detect_pose(img)  # 인식한 사람 리스트

if result:
  # 첫 번째 사람의 관절 좌표 17개
  print([[kp.coordinate.x, kp.coordinate.y] for kp in result[0].keypoints])
  print(detect.analyze_pose(result))  # ['left_hand_up', 'right_hand_up', 'clap'] 중 해당하는 것

  detect.detect_pose_vis(img, result)  # 관절 표시
camera.imshow_to_ide(img)
