from openpibo.speech import Speech

def run():
  o = Speech()
  # 음성 언어를 문자 데이터로 변환하여 출력
  result = o.stt()
  print(result)

if __name__ == "__main__":
  run()
