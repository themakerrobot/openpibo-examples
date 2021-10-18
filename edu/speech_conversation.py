from openpibo.edu_v1 import Pibo

def run():
  print('대화를 시작합니다. (q: 종료)')
  while True:
    user_input = input('나: ')
    if user_input == 'q':
      break

    result = pibo.conversation(user_input)
    print('파이보 : {}'.format(result['data']))

if __name__ == "__main__":
  pibo = Pibo()

  run()
