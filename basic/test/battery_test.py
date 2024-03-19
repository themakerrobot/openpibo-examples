from openpibo.device import Device

def run():
  dev = Device()
  print(dev.send_raw(f"#15:!").split(":")[1])

# Main loop
if __name__ == "__main__":
  run()