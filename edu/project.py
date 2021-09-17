import time

import requests
from bs4 import BeautifulSoup as bs

import openpibo
from openpibo.edu_v1 import Pibo

"""
  make your own code
"""
pibo = Pibo()


def oled_display(_path):
  pibo.draw_image(_path)
  pibo.show_display()

def speak(_text):
  print("SPEAK:", _text)
  #pibo.tts("<speak><voice name='WOMAN_READ_CALM'>{}<break time='500ms'/></voice></speak>".format(_text))
  #pibo.play_audio(filename='tts.mp3', background=False)  

def walk():
  oled_display(openpibo.config['DATA_PATH']+"/icon/walk.png")
  pibo.motors_movetime(positions=[  10,   0, -70, -25,   0,   0,  20,   0,  70,  25 ], movetime=300)
  time.sleep(0.2)
  pibo.motors_movetime(positions=[  10,   0, -80, -25,  20,   0,  20, -30,  60,  25 ], movetime=300)
  time.sleep(0.2)
  pibo.motors_movetime(positions=[  10, -30, -80, -25,  20,   0,  20, -30,  60,  25 ], movetime=300)
  time.sleep(0.2)
  pibo.motors_movetime(positions=[  10, -30, -80, -25,  20,   0,   0, -30,  60,  25 ], movetime=300)
  time.sleep(0.2)
  pibo.motors_movetime(positions=[ -20, -30, -80, -25,  20,   0, -10, -30,  60,  25 ], movetime=300)
  time.sleep(0.2)
  pibo.motors_movetime(positions=[ -20,  30, -60, -25, -20,   0, -10, -30,  80,  25 ], movetime=300)
  time.sleep(0.2)
  pibo.motors_movetime(positions=[ -20,  30, -60, -25, -20,   0, -10,  30,  80,  25 ], movetime=300)
  time.sleep(0.2)
  pibo.motors_movetime(positions=[   0,  30, -60, -25, -20,   0, -10,  30,  80,  25 ], movetime=300)
  time.sleep(0.2)

def weather():
  oled_display(openpibo.config['DATA_PATH']+"/icon/weather.png")
  weather_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&tqi=hvPRwsp0YiRssgy0vfVssssssMl-323245"
  pibo.draw_image(openpibo.config['DATA_PATH']+"/image/icon/weather_bot.png")
  pibo.show_display()

  res = requests.get(weather_url)

  soup = bs(res.text, 'html.parser')
  mdata = soup.find('div', {'class': 'main_info'})

  temp = mdata.find('span', {'class': 'todaytemp'}).text
  feel_temp = mdata.find('p', {'class':'cast_txt'}).text
  speak("오늘 기온은 {}°, {}.".format(temp, feel_temp))

def dance():
  oled_display(openpibo.config['DATA_PATH']+"/icon/check.png")
  pibo.motors_movetime(positions=[   0,   0, -70,  25,   0,   0,  20,   0,  70,  25 ], movetime= 450)
  time.sleep(0.3)
  pibo.motors_movetime(positions=[ -20,   0, -70,  25,   0,   0,  20,   0,  70, -25 ], movetime= 450)
  time.sleep(0.3)
  pibo.motors_movetime(positions=[ -20,   0, -70, -25,  20,   0,   0,   0,  70, -25 ], movetime= 450)
  time.sleep(0.3)
  pibo.motors_movetime(positions=[   0,   0, -70, -25,  20,   0,   0,   0,  70,  25 ], movetime= 450)
  time.sleep(0.3)
  pibo.motors_movetime(positions=[ -20,   0, -70, -25,  20,   0,   0,   0,  70, -25 ], movetime= 450)
  time.sleep(0.3)
  pibo.motors_movetime(positions=[ -20,   0, -70,  25,  20,   0,  20,   0,  70, -25 ], movetime= 450)
  time.sleep(0.3)
  pibo.motors_movetime(positions=[   0,   0, -70,  25, -20,   0,  20,   0,  70,  25 ], movetime= 450)
  time.sleep(0.3)
  pibo.motors_movetime(positions=[   0,   0, -70, -25, -20,   0,   0,   0,  70,  25 ], movetime= 450)
  time.sleep(0.3)

def conversation(_text):
  print("대화:", _text)
  oled_display(openpibo.config['DATA_PATH']+"/icon/conversation.png")
  time.sleep(5)
  ans = pibo.conversation(_text)
  speak(ans['data'])


def decode(_text):
  if _text.find("전진") > -1:
    walk()
  elif _text.find("날씨") > -1:
    weather()
  elif _text.find("댄스") > -1:
    dance()
  else:
    conversation(_text)


if __name__ == "__main__":
  pibo.eye_on('aqua')
  oled_display(openpibo.config['DATA_PATH']+"/icon/pibo_logo.png")
  pibo.check_device("system")
  pibo.motors_movetime(positions=[   0,   0, -70, -25, 0,   0,   0,   0,  70,  25 ], movetime= 500)
  time.sleep(0.3)

  start = time.time()

  while True:
    if time.time() - start > 1:
      start = time.time()
      ret = pibo.check_device("system")

      if ret['data']['TOUCH'] == 'touch':
        oled_display(openpibo.config['DATA_PATH']+"/icon/mic.png")

        cmd = {"result":True, "data":""}
        cmd['data'] = input('명령어를 입력하세요: ')
        #cmd = pibo.stt()

        if (cmd['result'] == True) and (cmd['data'].find('no') == -1):
          pibo.eye_on('red')
          #oled_display(openpibo.config['DATA_PATH']+"/image/icon/check.png")
  
          # decode
          decode(cmd['data'])

          #speak(cmd['data'] + ".")

        pibo.eye_on('aqua') 
        oled_display(openpibo.config['DATA_PATH']+"/icon/pibo_logo.png")
        pibo.motors_movetime(positions=[   0,   0, -70, -25, 0,   0,   0,   0,  70,  25 ], movetime= 500)
    time.sleep(0.1)

