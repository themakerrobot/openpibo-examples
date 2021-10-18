from openpibo.edu_v1 import Pibo

def run():
  ret = pibo.set_motion('dance1', 2)
  print(ret)

if __name__ == '__main__':
  pibo = Pibo()

  run()
