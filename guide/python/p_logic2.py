print('1) 참 and 참')
if True and True:
  print('맞아요.')
else:
  print('틀려요.')

print('2) 참 and 거짓')
if True and False:
  print('맞아요.')
else:
  print('틀려요.')

print('3) 거짓 or 참')
if False or True:
  print('맞아요.')
else:
  print('틀려요.')

print('4) 거짓 or 거짓')
if False or False:
  print('맞아요.')
else:
  print('틀려요.')

print('5) 한줄 - 참')
print('맞아요.' if True else '틀려요.')