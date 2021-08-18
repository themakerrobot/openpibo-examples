from openpibo.edu_v1 import Pibo

def translate_test():
    pibo = Pibo()

    print('한->영: 번역할 문장을 입력하세요. (q: 종료)')
    while True:
        string = input('입력: ')
        if string == "q":
            break
        ret = pibo.translate(string, to="en")
        print("번역:", ret["data"])

if __name__ == "__main__":
    translate_test()