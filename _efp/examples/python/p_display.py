from openpibo.oled import Oled
import time

oled = Oled()

oled.set_font(size=20)
oled.draw_text((0, 0), '안녕하세요.')
oled.show()
time.sleep(1)

oled.clear()
oled.draw_image('/home/pi/openpibo-files/image/weather/cloud.jpg')
oled.show()
time.sleep(1)

oled.clear()
oled.draw_rectangle((0, 0, 30, 30), False)
oled.draw_ellipse((31, 31, 60, 60), True)
oled.draw_line((0, 0, 30, 30))
oled.show()
