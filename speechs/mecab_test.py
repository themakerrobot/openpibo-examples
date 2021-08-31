from openpibo.speech import Dialog

def mecab_f(string, mode):
  print("Input: ", string)
  obj = Dialog()
  
  if mode == "pos":
    data = obj.mecab_pos(string)
  elif mode == "morphs":
    data = obj.mecab_morphs(string)
  elif mode == "nouns":
    data = obj.mecab_nouns(string)
  print("Output: ", data)

if __name__ == "__main__":
  mecab_f("아버지 가방에 들어가신다", "nouns")


