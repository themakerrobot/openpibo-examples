import time
from openpibo.edu_v1 import Pibo


def motors_test():
    pibo = Pibo()
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