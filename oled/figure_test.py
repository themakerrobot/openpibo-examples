from openpibo.oled import Oled

def oled_f():
  oObj = Oled()
  oObj.clear()
  oObj.draw_rectangle((10,10,30,30) ,True)
  oObj.draw_ellipse((70,40,90,60) ,False)
  oObj.draw_line((15,15,80,50))
  oObj.show()

if __name__ == "__main__":
  oled_f()
