from openpibo.edu_v1 import Pibo

def run():
  result = pibo.check_device()
  print(result)

if __name__ == '__main__':
  pibo = Pibo()

  run()
