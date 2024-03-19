from openpibo.vision import Camera

# 모니터에 3초간 이미지 스트리밍
def run(gui=False):
  o = Camera()

  if gui:
    # For streaming (only GUI)
    o.streaming(timeout=3)
  else:
    print("No GUI")

if __name__ == "__main__":
  run(gui=False)
