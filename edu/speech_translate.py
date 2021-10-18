from openpibo.edu_v1 import Pibo

def check(string):
  return ('en', 'ko') if string.upper() != string.lower() else ('ko', 'en')

def run():
  print('한<->영: 번역할 문장을 입력하세요. (q: 종료)')
  while True:
    user_input = input('입력: ')
    if user_input == 'q':
      break

    lang_from, lang_to = check(user_input)
    result = pibo.translate(user_input, to=lang_to)
    print('번역 : {} ({}) --> {} ({})'.format(user_input, lang_from, result['data'], lang_to))

if __name__ == '__main__':
  pibo = Pibo()

  run()
