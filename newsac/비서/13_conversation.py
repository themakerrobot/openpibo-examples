from openpibo.speech import Dialog
from openpibo.audio import Audio

dialog = Dialog()
audio = Audio()

# 대화 파일 교체
#dialog.load('mydialog.csv')

print('대화를 시작합니다 >>')
while True:
  question = input('')
  
  if question == '그만':
    print('즐거운 하루 보내세요.')
    break

  answer = dialog.get_dialog(question)

  print('Q:', question, 'A:', answer)
