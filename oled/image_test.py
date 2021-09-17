import openpibo
from openpibo.oled import Oled

import time

# 화면에 clear.png 이미지 5초간 표시
def oled_f():
  oObj = Oled()
  oObj.draw_image(openpibo.config['DATA_PATH']+"/image/clear.png")  # clear.png 그리기
  oObj.show()   # 화면에 표시
  time.sleep(5) # 5초동안 프로세스 정지
  oObj.clear()  # 화면 지우기
  oObj.show()

if __name__ == "__main__":
  oled_f()
