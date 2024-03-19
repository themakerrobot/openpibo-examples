from openpibo.oled import Oled

def run():
  oled = Oled()
  oled.set_font(size=15)
  oled.clear()
  
  string = "#가나다라마바사자#"
  for i in range(4):
    print(i)
    oled.draw_text((0,i*15), string)
  oled.show()

# Main loop
if __name__ == "__main__":
  run()