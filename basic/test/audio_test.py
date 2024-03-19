import argparse

import time, os
from openpibo.audio import Audio
from openpibo.device import Device

def mute(en):
  if args.board == "old":
    os.system(f"gpio write 7 {0 if en == True else 1}")
  else:
    dev.send_raw(f"#16:{'on' if en == True else 'off'}!")

def run():
  audio = Audio()
  device = Device()

  print("+ AUDIO-START")
  audio.play(args.filename, args.volume, background=True)
  time.sleep(5)
  mute(True)
  print("  - MUTE-ON")
  time.sleep(5)
  mute(False)
  print("  - MUTE-OFF")
  time.sleep(5)
  print("+ AUDIO-STOP")
  audio.stop()

# Main loop
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--filename', help='audio filepath (fullpath)', default='/home/pi/openpibo-files/audio/music/nature.mp3')
  parser.add_argument('--volume', help='volume 0 -100', default=80, type=int)
  parser.add_argument('--board', help='"new" or "old" > main board ', default='old')
  args = parser.parse_args()

  run()