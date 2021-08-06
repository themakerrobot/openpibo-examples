import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def translate_test():
    pibo = Edu_Pibo()

    print('한->영: 번역할 문장을 입력하세요. (q: 종료)')
    while True:
        string = input('입력: ')
        if string == "q":
            break
        ret = pibo.translate(string, to="en")
        print("번역:", ret["data"])

if __name__ == "__main__":
    translate_test()