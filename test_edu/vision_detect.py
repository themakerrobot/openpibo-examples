import time
from openpibo.edu_v1 import Pibo

def detect_test():
    pibo = Pibo()

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