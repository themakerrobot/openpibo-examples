import time, pprint

from openpibo.edu_v1 import Pibo

def get_motion():
    pibo = Pibo()
    motion_list = pibo.get_motion()
    print(motion_list['data'])

    time.sleep(0.5)
    print('모션을 입력하면 해당 모션의 정보를 조회할 수 있습니다.(q: 종료)')
    while True:
        user_input = input('입력: ')
        
        if user_input == 'q':
            return
        info = pibo.get_motion(user_input)
        pprint.pprint(info['data'])

if __name__ == "__main__":
    get_motion()