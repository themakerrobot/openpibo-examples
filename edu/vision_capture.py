import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def capture_test():
    pibo = Edu_Pibo()

    # Version 1. Camera on
    pibo.start_camera()
    time.sleep(1)
    pibo.capture()
    time.sleep(3)
    pibo.stop_camera()

    # Version 2. Camera off
    pibo.capture("capture_cameraoff.png")
    
if __name__ == "__main__":
    capture_test()