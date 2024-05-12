import time

while True:
  print(time.strftime('%Y-%m-%d %H:%M:%S'))
  s = time.strftime('%S')
  if s == '00':
    print(time.strftime('%H 시 %M 분 입니다.'))

  time.sleep(1)