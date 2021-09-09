from openpibo.motion import Motion

# wave3 모션 10번 반복
if __name__ == "__main__":
  m = Motion()
  m.set_motion(name="wave3", cycle=10)
