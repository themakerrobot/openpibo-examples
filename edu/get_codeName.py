import time

from openpibo.edu_v1 import Pibo

def get_code():
    pibo = Pibo()

    time.sleep(0.5)
    print('조회하고 싶은 errcode를 입력하세요.(숫자) (q: 종료)')
    while True:
        user_input = input()
        
        if user_input == 'q':
            return
        
        result = pibo.get_codeMean(int(user_input))
        if result['result'] == True:
            print(result['data'])
        else:
            print(result['errmsg'])

if __name__ == "__main__":
    get_code()