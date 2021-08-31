import time

from openpibo.edu_v1 import Pibo

def figure_test():
    pibo = Pibo()
    pibo.draw_figure((10,10,30,30), "rectangle", True)
    pibo.draw_figure((70,40,90,60), "circle", False)
    pibo.draw_figure((15,15,80,50), "line")
    pibo.show_display()
    time.sleep(1.5)

    pibo.invert()
    pibo.show_display()
    time.sleep(1.5)
    pibo.clear_display()

if __name__ == "__main__":
    figure_test()