import time, pprint
from openpibo.edu_v1 import Pibo

def run():
  print('=== Motion list ===\n', pibo.get_motion()['data'])

  while True:
    user_input = input('\n 모션 이름을 입력하세요. (q: 종료) ')
    if user_input == 'q':
      break

    result = pibo.get_motion(user_input)
    result = result['data'] if type(result['data']) is dict else f'{user_input} is not support'
    pprint.pprint(result)

if __name__ == '__main__':
  pibo = Pibo()

  run()
