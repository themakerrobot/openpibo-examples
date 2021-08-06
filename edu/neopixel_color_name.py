import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def color_name_test():
    pibo = Edu_Pibo()
    ret=pibo.eye_on('aqua', 'purple')
    print(ret)
    time.sleep(1)
    
    ret2=pibo.eye_on('pink')
    print(ret2)
    time.sleep(1)
    pibo.eye_off()

if __name__ == "__main__":
    color_name_test()