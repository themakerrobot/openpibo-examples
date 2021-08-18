import time
import os
data_path = os.path.dirname(os.path.abspath(__file__))+'/../data/'
from openpibo.edu_v1 import Pibo

def image_test():
    pibo = Pibo()

    ret=pibo.draw_image(data_path+"image/clear.png")
    print(ret)
    pibo.show_display()
    time.sleep(2)
    pibo.clear_display()

if __name__ == "__main__":
    image_test()