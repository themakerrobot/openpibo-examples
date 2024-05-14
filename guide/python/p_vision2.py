from openpibo.vision import Camera
from openpibo.vision import Detect

camera = Camera()
detect = Detect()

img = camera.read()
result = detect.detect_pose(img)

print([[_i.coordinate.x, _i.coordinate.y] for _i in result['data'][0][0]])
print(detect.analyze_pose(result))