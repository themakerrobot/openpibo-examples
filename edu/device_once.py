import os, sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def device_once_test():
    pibo = Edu_Pibo()
    print('확인할 device를 입력하세요.(system, battery) (q: 종료)')

    while True:
        cmd = input("")
        if cmd == "q":
            break
        ret = pibo.check_device(cmd)
        print(ret) 

if __name__ == "__main__":
    device_once_test()