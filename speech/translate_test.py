from openpibo.speech import Speech

# "즐거운 하루 보내세요."를 영어로 번역 후 출력
def run():
  o = Speech()
  string = "즐거운 하루 보내세요."
 
  print(f'입력 > {string}')

  result = o.translate(string, to="en")
  print(f' ko->en > {result}')
  result = o.translate(string, to="ko")
  print(f' en->ko > {result}')

if __name__ == "__main__":
  run()
