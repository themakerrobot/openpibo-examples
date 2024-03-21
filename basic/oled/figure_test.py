from openpibo.oled import Oled

oled = Oled()
oled.clear()                              # 화면 지우기
oled.draw_rectangle((10,10,30,30), True)  # 길이가 20인 채워진 사각형 그리기
oled.draw_ellipse((70,40,90,60), False)   # 지름이 20인 빈 원 그리기
oled.draw_line((15,15,80,50))             # 선 그리기
oled.show()                               # 화면에 표시