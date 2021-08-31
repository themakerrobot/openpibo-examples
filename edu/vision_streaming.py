import time
from openpibo.edu_v1 import Pibo

def streaming_test():
    pibo = Pibo()

    pibo.start_camera()
    time.sleep(3)
    pibo.stop_camera()
    
if __name__ == "__main__":
    streaming_test()