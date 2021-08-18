from openpibo.edu_v1 import Pibo

def device_once_test():
    pibo = Pibo()
    print('확인할 device를 입력하세요.(system, battery) (q: 종료)')

    while True:
        cmd = input("")
        if cmd == "q":
            break
        ret = pibo.check_device(cmd)
        print(ret) 

if __name__ == "__main__":
    device_once_test()