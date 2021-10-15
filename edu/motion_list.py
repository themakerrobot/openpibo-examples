import time, pprint

from openpibo.edu_v1 import Pibo

def run():
  print("=== Motion list ===\n", pibo.get_motion()['data'])

  while True:
    user_input = input('\n 입력> ')
    if user_input == 'q':
      break

    result = pibo.get_motion(user_input)
    result = result['data'] if type(result['data']) is dict else f'{user_input} not support'
    pprint.pprint(result)

if __name__ == "__main__":
  pibo = Pibo()

  run()
