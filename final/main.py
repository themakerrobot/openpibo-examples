from bs4 import BeautifulSoup as bs
import requests
import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

weather_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&tqi=hvPRwsp0YiRssgy0vfVssssssMl-323245"

# Functions for Utils
def LOG_PRINT(*msg):
    print("[PIBO] {}".format(",".join(str(p) for p in msg)))


def play_tts(msg):
    filename = cfg.TESTDATA_PATH+"/tts.mp3"
    txt = "<speak><voice name='WOMAN_READ_CALM'> {} <break time='500ms'/></voice></speak>".format(msg)

    pibo.tts(txt, filename)
    pibo.play_audio(filename, out='local', volume=-1500, background=False)


# Functions for Bots
def bot_weather():
    LOG_PRINT('Enter the {}'.format(sys._getframe(0).f_code.co_name))

    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/weather_bot.png")
    pibo.show_display()

    res = requests.get(weather_url)

    soup = bs(res.text, 'html.parser')
    mdata = soup.find('div', {'class': 'main_info'})

    temp = mdata.find('span', {'class': 'todaytemp'}).text
    feel_temp = mdata.find('p', {'class':'cast_txt'}).text
    play_tts("오늘 기온은 {}°, {}.".format(temp, feel_temp))

    LOG_PRINT('Leave the {}'.format(sys._getframe(0).f_code.co_name))


def bot_picture():
    LOG_PRINT('Enter the {}'.format(sys._getframe(0).f_code.co_name))

    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/camera.png")
    pibo.show_display()
    time.sleep(1)

    pibo.start_camera()
    time.sleep(3)
    pibo.capture("/home/pi/openpibo-example/final/capture.png")
    pibo.stop_camera()

    LOG_PRINT('Leave the {}'.format(sys._getframe(0).f_code.co_name))


def bot_walk(msg):
    LOG_PRINT('Enter the {}'.format(sys._getframe(0).f_code.co_name))

    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/walk.png")
    pibo.show_display()

    motions_db = {
        "앞" : "forward1",
        "뒤" : "backward1",
        "왼쪽" : "left",
        "오른쪽" : "right"
    }

    go_motion = "stop"
    for motion in motions_db:
        if motion in msg:
            go_motion = motions_db[motion]

    pibo.set_motion(go_motion, 4)
    pibo.set_motion("stop", 1)

    LOG_PRINT('Leave the {}'.format(sys._getframe(0).f_code.co_name))


def decode(msg):
    matched = False
    bot_db ={
        '날씨' : bot_weather,
        '사진' : bot_picture,
        '이동' : bot_walk,
    }

    for item in bot_db:
        if item in msg:
            matched = True
            
            if item == '이동':
                bot_db[item](msg)
            else:
                bot_db[item]()

    LOG_PRINT('{}: {}'.format(sys._getframe(0).f_code.co_name, msg), matched)

    if matched == False:
        ans = pibo.conversation(msg)
        play_tts(ans)


def listen():
    pibo.stop_camera()
    pibo.set_motion("lookup", 1)

    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/mic.png")
    pibo.show_display()

    res = pibo.stt()['data']

    LOG_PRINT('{}: {}'.format(sys._getframe(0).f_code.co_name, res))

    if "no result" not in res:
        pibo.draw_image(cfg.TESTDATA_PATH + "/icon/check.png")
        pibo.show_display()
        decode(res)
        

def check_person():
    pibo.start_camera()
    time.sleep(1)

    faces = pibo.detect_face()['data']
    if faces == 'No Face':
        face_num = 0
    else:
        face_num = len(faces)

    LOG_PRINT('{}: Found {} faces'.format(sys._getframe(0).f_code.co_name, face_num))

    return face_num


def device(msg):
    LOG_PRINT('{}: {}'.format(sys._getframe(0).f_code.co_name, msg))
    
    if "person" in msg["PIR"]:
        if check_person() > 0:
            listen()


if __name__ == "__main__":
    LOG_PRINT("Start")
    pibo = Edu_Pibo()
    LOG_PRINT("Init ...")

    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/pibo_logo.png")
    pibo.show_display()

    play_tts("안녕! 난 파이보야.")
    pibo.set_motion("welcome", 1)
    pibo.set_motion("stop", 1)

    LOG_PRINT("Device Start ...")

    while True:
        res = pibo.check_device("system")
        device(res['data'])
        time.sleep(1)
