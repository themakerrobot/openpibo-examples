import argparse, os, serial

def run():
  print("Send: ", args.message)
  ser = serial.Serial(port=f"{args.device}", baudrate=9600)

  ser.write(f"#{args.message}!".encode('utf-8'))
  data = ""
  while True:
    ch = ser.read().decode()
    if ch == '#' or ch == '\r' or ch == '\n':
      continue
    if ch == '!':
      break
    data += ch
  print("Receive:", data)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--device', help='tty device name', default='/dev/ttyS0')
  parser.add_argument('--message', help="message to send", default='hello')
  args = parser.parse_args()
  run()