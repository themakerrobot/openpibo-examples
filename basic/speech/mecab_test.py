from openpibo.speech import Dialog

# mode(pos, morphs, nouns)에 따른 문장 분석
def run():
  o = Dialog()
  string = "아버지 가방에 들어가신다"
  
  print("입력: ", string)
  
  result = o.mecab_pos(string)
  print(f' pos: {result}')
  result = o.mecab_morphs(string)
  print(f' morphs: {result}')
  result = o.mecab_nouns(string)
  print(f' nouns: {result}')

if __name__ == "__main__":
  run()


