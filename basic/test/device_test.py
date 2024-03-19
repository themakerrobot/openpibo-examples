from openpibo.device import Device
import time

KEYS = ['PIR', 'TOUCH', 'DC', 'BUTTON']

def run():
  dev = Device()

  while True:
    time.sleep(1)
    res = dev.send_raw("#40:!").split(":")[1].split("-")
    print([{KEYS[i]:item}for i, item in enumerate(res[:4])])

# Main loop
if __name__ == "__main__":
  run()