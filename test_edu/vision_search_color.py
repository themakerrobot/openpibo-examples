import time
from openpibo.edu_v1 import Pibo

def color_test():
    pibo = Pibo()
    pibo.start_camera()
    time.sleep(2)
    color = pibo.search_color()
    print("Search Color: ", color)
    pibo.stop_camera()
    
if __name__ == "__main__":
    color_test()

    