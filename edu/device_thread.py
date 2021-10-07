import time
from openpibo.edu_v1 import Pibo

def msg_device(msg):
    print(msg)
    if "touch" in msg:
      pibo.eye_on("red")
    else:
      pibo.eye_off()


def device_thread_test():
    ret=pibo.start_devices(msg_device)
    print(ret)
    time.sleep(12)
    pibo.stop_devices()

if __name__ == "__main__":
    pibo = Pibo()
    device_thread_test()
