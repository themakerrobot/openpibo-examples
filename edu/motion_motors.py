import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo


def motors_test():
    pibo = Edu_Pibo()
    while True:
        pibo.motors(
            positions=[0,0,0,10,0,10,0,0,0,20], 
            speed=[0,0,0,15,0,10,0,0,0,10], 
            accel=[0,0,10,5,0,0,0,0,5,10]
        )
        time.sleep(1)

        pibo.motors(
            positions=[0,0,0,-10,0,-10,0,0,0,-20], 
            speed=[0,0,0,15,0,10,0,0,0,10],
        )
        time.sleep(1)

if __name__ == "__main__":
    motors_test()