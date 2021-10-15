from openpibo.oled import Oled

# (0,0), (0,20)에 15 크기의 text 표시
def run():
  o = Oled()
  o.set_font(size=15)
  o.draw_text((0, 0), "안녕? 난 파이보야 ")  # (0,0)에 문자열 출력
  o.draw_text((0,20), "☆  ★ ") # (0,20)에 문자열 출력
  o.show() # 화면에 표시

"""
  for count in range(5):
    oObj.clear()
    oObj.draw_text((10,10), "Hello World:{}".format(count))
    oObj.show()
    time.sleep(1)

  oObj.clear()
"""

if __name__ == "__main__":
  run()
