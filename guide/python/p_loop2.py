print('1) 반복 / 중단')
num = 1
while True:
  print(num)
  if num > 3:
    print('반복을 중단합니다.')
    break
  num = num + 1

print('2) 목록 조회')
for item in ['사과', '배', '바나나']:
  print(item)