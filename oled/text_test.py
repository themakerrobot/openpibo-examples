from openpibo.oled import Oled

def oled_f():
  oObj = Oled()
  oObj.set_font(size=15)
  
  oObj.draw_text((0, 0), "안녕? 난 파이보야 ")
  oObj.draw_text((0,20), "☆  ★ ")
  oObj.show()

'''
  for count in range(5):
    oObj.clear()
    oObj.draw_text((10,10), "Hello World:{}".format(count))
    oObj.show()
    time.sleep(1)

  oObj.clear()
'''

if __name__ == "__main__":
  oled_f()
