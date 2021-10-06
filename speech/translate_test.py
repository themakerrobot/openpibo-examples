from openpibo.speech import Speech

# "안녕하세요"를 영어로 번역 후 출력
def translate_f():
  obj = Speech()
  string = "안녕하세요"
  ret = obj.translate(string, to="en")
  print("Input:", string)
  print("Output:", ret)

if __name__ == "__main__":
  translate_f()