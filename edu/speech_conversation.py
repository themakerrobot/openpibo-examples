import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def talk_test():
    pibo = Edu_Pibo()

    print('대화를 시작합니다. (q: 종료)')
    while True:
        question = input('나: ')
        if question == 'q':
            break

        ans = pibo.conversation(question)
        print('파이보: ', ans["data"])

if __name__ == "__main__":
    talk_test()