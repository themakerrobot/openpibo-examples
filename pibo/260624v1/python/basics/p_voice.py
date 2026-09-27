from openpibo.speech import Dialog
from openpibo.speech import Speech
from openpibo.audio import Audio

dialog = Dialog()
speech = Speech()
audio = Audio()

print('## 내장 대화')
print(dialog.get_dialog('반가워'))

print('## 나만의 대화')
dialog.load('/home/pi/code/mychat.csv')
print(dialog.get_dialog('안녕'))
print(dialog.get_dialog('반가워'))

speech.tts(string='안녕하세요', filename='/home/pi/code/voice.mp3', voice='main')
audio.play('/home/pi/code/voice.mp3', 30)