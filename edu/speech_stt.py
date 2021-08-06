import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def stt_test():
    pibo = Edu_Pibo()

    ret = pibo.stt()
    print(ret)

if __name__ == "__main__":
    stt_test()