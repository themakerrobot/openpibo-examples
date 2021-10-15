import time

import openpibo
from openpibo.oled import Oled

# 화면에 clear.png 이미지 5초간 표시
def run():
  o = Oled()
  o.draw_image(openpibo.config['DATA_PATH']+"/image/clear.png")  # clear.png 그리기
  o.show()   # 화면에 표시
  time.sleep(5) # 5초동안 프로세스 정지
  o.clear()  # 화면 지우기
  o.show()

if __name__ == "__main__":
  run()
