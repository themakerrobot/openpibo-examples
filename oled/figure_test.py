from openpibo.oled import Oled

def oled_f():
  oObj = Oled()
  oObj.clear()                              # 화면 지우기
  oObj.draw_rectangle((10,10,30,30) ,True)  # 길이가 20인 채워진 사각형 그리기
  oObj.draw_ellipse((70,40,90,60) ,False)   # 지름이 20인 빈 원 그리기
  oObj.draw_line((15,15,80,50))             # 선 그리기
  oObj.show()                               # 화면에 표시

if __name__ == "__main__":
  oled_f()
