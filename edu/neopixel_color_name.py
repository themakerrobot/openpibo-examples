import time
from openpibo.edu_v1 import Pibo

def color_name_test():
    pibo = Pibo()
    ret=pibo.eye_on('aqua', 'purple')
    print(ret)
    time.sleep(1)
    
    ret2=pibo.eye_on('pink')
    print(ret2)
    time.sleep(1)
    pibo.eye_off()

if __name__ == "__main__":
    color_name_test()