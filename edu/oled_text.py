import time

from openpibo.edu_v1 import Pibo

def run():
  pibo.draw_text((10,10), '안녕하세요. Hello', 15)
  pibo.show_display()
  time.sleep(2)

  pibo.clear_display()

if __name__ == "__main__":
  pibo = Pibo()

  run()
