from openpibo.motion import PyMotion

import time

m = PyMotion()

def move(n, speed, accel, degree):
  m.set_speed(n, speed)
  m.set_acceleration(n, accel)
  m.set_motor(n, degree)

def test():
  while True:
    move(2, 50, 0, 30)
    time.sleep(2)
  
    move(2, 50, 10, -30)
    time.sleep(2)

if __name__ == "__main__":
  print("Init")
  move(2, 20, 0, 0)
  time.sleep(1)

  print("Start")
  test()
