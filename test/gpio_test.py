import os, time

def run():
  os.system('gpio mode 22 in')
  while True:
    time.sleep(1)
    print(os.popen('gpio read 22').read().replace('\n',''))

if __name__ == "__main__":
  run()