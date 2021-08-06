import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo


def movetime_test():
    pibo = Edu_Pibo()
    while True:
        pibo.motors_movetime(positions=[0,0,30,20, 30,0, 0,0,30,20], movetime=1000)
        time.sleep(1)
        pibo.motors_movetime(positions=[0,0,-30,-20, -30,0, 0,0,-30,-20])
        time.sleep(1)

if __name__ == "__main__":
    movetime_test()