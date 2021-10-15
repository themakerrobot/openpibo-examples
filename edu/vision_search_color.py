import time

from openpibo.edu_v1 import Pibo

def run():
  pibo.start_thread_camera()
  time.sleep(2)
  color = pibo.search_color()
  print("Search Color: ", color)
  pibo.stop_thread_camera()

if __name__ == "__main__":
  pibo = Pibo()

  run()

