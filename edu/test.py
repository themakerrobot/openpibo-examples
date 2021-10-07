import time
from openpibo.edu_v1 import Pibo
from threading import Thread

def move():
    print("[move]", "start")
    pibo.set_motion("wave1")
    print("[move]", "end")

def run():
    print("[run]", "start")
    
    while True:
        result = pibo.check_device('SYSTEM')
        print(" [run]: msg-", result)
        if result['data']['TOUCH'] == 'touch':
            print(" [run]:", "TOUCH")
            pibo.eye_on("yellow")
            Thread(target=move, args=(), daemon=True).start()
            time.sleep(10)            
        pibo.eye_on("aqua")
        time.sleep(1)

if __name__ == "__main__":
    pibo = Pibo()
    Thread(target=run, args=(), daemon=True).start()

    while True:
        pass
