import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def face_test():
    pibo = Edu_Pibo()

    pibo.start_camera()
    time.sleep(3)
    face = pibo.search_face()
    print(face)
    pibo.stop_camera()
    
if __name__ == "__main__":
    face_test()