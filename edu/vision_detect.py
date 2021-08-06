import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def detect_test():
    pibo = Edu_Pibo()

    pibo.start_camera()
    time.sleep(2)
    obj = pibo.search_object()
    qr = pibo.search_qr()
    text = pibo.search_text()
    print("Search Object: ", obj)
    print("Search QR: ", qr)
    print("Search Text: ", text)
    pibo.stop_camera()
    
if __name__ == "__main__":
    detect_test()