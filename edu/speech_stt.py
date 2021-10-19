from openpibo.edu_v1 import Pibo

def run():
  result = pibo.stt()
  print('stt() : ', result)

if __name__ == '__main__':
  pibo = Pibo()

  run()
