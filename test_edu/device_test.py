import random

from openpibo.edu_v1 import Pibo

def msg_device(msg):
    print(msg)

def device_test():
    ret=pibo.start_devices(msg_device)
    print(ret)


if __name__ == "__main__":
    pibo = Pibo()
    device_test()

    while True:
        cmd = [random.randint(0, 255) for i in range(6)]
        pibo.eye_on(*cmd)
