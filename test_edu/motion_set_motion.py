from openpibo.edu_v1 import Pibo


def motion_test():
    pibo = Pibo()
    ret=pibo.set_motion("dance1", 2)
    print(ret)

if __name__ == "__main__":
    motion_test()