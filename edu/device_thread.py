import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def msg_device(msg):
    print(msg)

def device_thread_test():
    pibo = Edu_Pibo()
    ret=pibo.start_devices(msg_device)
    print(ret)
    time.sleep(12)
    pibo.stop_devices()

if __name__ == "__main__":
    device_thread_test()