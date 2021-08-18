from openpibo.motion import Motion

import time

m = Motion()

def move(n, degree, speed, accel):
  m.set_speed(n, speed)
  m.set_acceleration(n, accel)
  m.set_motor(n, degree)

def test():
  while True:
    move(2, 30, 100, 10)
    move(8, 30,  10, 10)
    time.sleep(1)

    move(2, -30, 100, 10)
    move(8, -30,  10, 10)
    time.sleep(1)

if __name__ == "__main__":
  test()
