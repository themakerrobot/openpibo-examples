import time
from openpibo.edu_v1 import Pibo

def face_test():
    pibo = Pibo()

    pibo.start_camera()
    time.sleep(3)
    face = pibo.search_face()
    print(face)
    pibo.stop_camera()
    
if __name__ == "__main__":
    face_test()