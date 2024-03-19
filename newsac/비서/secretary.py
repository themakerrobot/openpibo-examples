from openpibo.collect import Weather
from openpibo.collect import News
from openpibo.collect import Wikipedia
from openpibo.speech import Dialog
from openpibo.motion import Motion
from threading import Timer
import time

keyword = None
x = None
q = None
command = None

weather = Weather()
news = News()
wikipedia = Wikipedia()
dialog = Dialog()
motion = Motion()
prior_time = None

def run_weather():
  global keyword, x, q, command
  log(weather.search_s('서울', 'forecast'))

def run_news():
  global keyword, x, q, command
  log(news.search_s('속보', 'title'))

def run_time():
  global keyword, x, q, command
  log(time.strftime('%Y-%m-%d %H:%M:%S'))

def run_wiki(keyword):
  global x, q, command
  log(wikipedia.search_s(keyword))

def run_dialog(q):
  global keyword, x, command
  log(dialog.get_dialog(q))

def log(x):
  global keyword, q, command
  print('[LOG]: ' + str(x))

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

def run_event():
  global prior_time
  current_time = time.strftime('%H:%M:%S').split(':')
  
  if prior_time == None or prior_time[1] != current_time[1]:
    print(f"\n{time.strftime('%H시 %M분')} 입니다.\n")
  prior_time = current_time
    
  t = Timer(1, run_event)
  t.daemon = True
  t.start()

run_event()

while True:
  command = text_prompt('무엇을 할까요? > ')
  if '날씨' in command:
    run_weather()
  elif '뉴스' in command:
    run_news()
  elif '시간' in command:
    run_time()
  elif '위키' in command:
    run_wiki(text_prompt('무엇을 검색할까요? > '))
  elif '댄스' in command:
    log('motion')
    motion.set_motion('foot1', 1)
  elif '체조' in command:
    log('exercise')
    motion.set_motion('greeting', 1)
  else:
    run_dialog(command)