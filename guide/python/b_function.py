def func1():
  print('Hello')

def func2(name):
  print('Hello', name)

def func3():
  return 'Hi'

def func4(name):
  return f'Hi {name}'

func1()
func2('pibo')

result3 = func3()
result4 = func4('pibo')
print(result3)
print(result4)
