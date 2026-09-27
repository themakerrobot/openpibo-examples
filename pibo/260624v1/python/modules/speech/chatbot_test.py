from openpibo.speech import Dialog

def weather(cmd):
  topic = None

  # 분석한 문장 중 "오늘", "내일"이 있다면 topic 으로 설정
  for item in ['오늘', '내일']:
    if item in cmd:
      topic = item

  answer = f'{topic} 날씨 알려줄게요' if topic else '오늘, 내일 날씨만 가능해요.'
  print(f'\n - 날씨: {answer}')

def music(cmd):
  topic = None

  # 분석한 문장 중 "발라드", "댄스", "락"이 있다면 topic 으로 설정
  for item in ['발라드', '댄스', '락']:
    if item in cmd:
      topic = item

  answer = f'{topic} 음악 들려줄게요' if topic else '발라드, 댄스, 락 음악만 가능해요.'
  print(f'\n - 음악: {answer}')

def news(cmd):
  topic = None

  # 분석한 문장 중 "경제", "스포츠", "문화"가 있다면 topic 으로 설정
  for item in ['경제', '스포츠', '문화']:
    if item in cmd:
      topic = item

  answer = f'{topic} 뉴스 들려줄게요' if topic else '경제, 스포츠, 문화 뉴스만 가능해요.'
  print(f'\n - 뉴스: {answer}')

func = {
  "날씨":weather,
  "음악":music, 
  "뉴스":news,
}

# 사용자가 입력한 문장에 대해 형태소 분석을 실시하여 파이보가 실행하는 함수가 달라짐

dialog = Dialog()
print("대화 시작합니다.")
while True:
  keyword = input("입력 > ")
  matched = False
  if keyword == "그만":
    break

  # 사용자가 입력한 질문에 대한 형태소 분석
  result = dialog.mecab_morphs(keyword)
  print("\n  - 형태소 분석: ", result)
  # 분석한 문장 중 "날씨", "음악", "뉴스"가 있다면 해당 key값의 함수 실행
  for key in func.keys():
    if key in result:
      func[key](result)
      matched = True

  # key 값이 없다면 대화봇 실행
  if matched == False:
    print(f'\n 대화: {dialog.get_dialog(keyword)}')