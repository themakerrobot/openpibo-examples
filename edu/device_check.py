from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.check_device()
  print('check_device() : ', ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
