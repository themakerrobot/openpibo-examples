from threading import Timer


def print_test(n):
  print(n + 10)
  timer = Timer(1, print_test, args=(5,)) # Timer( 실행주기-초, 실행할 함수, 매개변수 )
  timer.daemon = True
  timer.start()

print_test(5)

while True:
  pass