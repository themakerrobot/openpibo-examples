import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def get_code():
    pibo = Edu_Pibo()

    time.sleep(0.5)
    print('조회하고 싶은 errcode를 입력하세요.(숫자) (q: 종료)')
    while True:
        user_input = input()
        
        if user_input == 'q':
            return
        print(pibo.get_codeMean(int(user_input)))

if __name__ == "__main__":
    get_code()