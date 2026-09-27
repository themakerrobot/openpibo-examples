import time
from openpibo.oled import Oled

IMG_PATH = '/home/pi/openpibo-files/image'

# 화면에 sun.jpg 이미지 5초간 표시
oled = Oled()
oled.draw_image(IMG_PATH + "/weather/sun.jpg") # sun.jpg 그리기
oled.show()   # 화면에 표시
time.sleep(5) # 5초동안 프로세스 정지
oled.clear()  # 화면 지우기
oled.show()