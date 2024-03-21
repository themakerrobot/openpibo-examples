import time
from openpibo.oled import Oled

# (0,0), (0,20)에 15 크기의 text 표시
oled = Oled()
oled.set_font(size=15)
oled.draw_text((0, 0), "안녕? 난 파이보야 ")  # (0,0)에 문자열 출력
oled.draw_text((0,20), "☆  ★ ") # (0,20)에 문자열 출력
oled.show() # 화면에 표시

"""
time.sleep(1)
for count in range(5):
  oled.clear()
  oled.draw_text((10,10), f"Hello World:{count}")
  oled.show()
  time.sleep(0.5)

oled.clear()
#"""