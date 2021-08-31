import time
from openpibo.edu_v1 import Pibo

def capture_test():
    pibo = Pibo()

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