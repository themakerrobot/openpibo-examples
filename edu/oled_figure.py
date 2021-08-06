import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def figure_test():
    pibo = Edu_Pibo()
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