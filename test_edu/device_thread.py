import time

from openpibo.edu_v1 import Pibo

def msg_device(msg):
    print(msg)

def device_thread_test():
    pibo = Pibo()
    ret=pibo.start_devices(msg_device)
    print(ret)
    time.sleep(12)
    pibo.stop_devices()

if __name__ == "__main__":
    device_thread_test()