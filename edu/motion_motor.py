import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo


def motor_test():
    pibo = Edu_Pibo()
    while True:
        pibo.motor(2, 30, 100, 10)
        pibo.motor(8, 30, accel=10)
        time.sleep(1)

        pibo.motor(2, -30, 100, 10)
        pibo.motor(8, -30, speed=70)
        time.sleep(1)

if __name__ == "__main__":
    motor_test()