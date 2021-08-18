from openpibo.edu_v1 import Pibo

def stt_test():
    pibo = Pibo()

    ret = pibo.stt()
    print(ret)

if __name__ == "__main__":
    stt_test()