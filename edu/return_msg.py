import time
from pprint import pprint
from openpibo.edu_v1 import Pibo

def run():
  pprint(pibo.return_msg_list)

if __name__ == '__main__':
  pibo = Pibo()

  run()
