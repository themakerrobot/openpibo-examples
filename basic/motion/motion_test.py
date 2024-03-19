from openpibo.motion import Motion

# wave3 모션 10번 반복
def run():
  o = Motion()
  o.set_motion(name="wave3", cycle=10)

if __name__ == "__main__":
  run()
