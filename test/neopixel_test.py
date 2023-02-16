import argparse
from openpibo.device import Device

def run():
  dev = Device()
  dev.send_raw(f"#23:{args.color}!")

# Main loop
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--color', help='255,255,255,255,255,255', default='255,255,255,255,255,255')
  args = parser.parse_args()

  run()