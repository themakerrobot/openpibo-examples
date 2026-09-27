from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import asyncio
from openpibo.device import Device
from openpibo.motion import Motion
from openpibo.audio import Audio
from threading import Timer
import os, random, asyncio

audio = Audio()
motion = Motion()
device = Device()
VOLUME = 100

theme = "default" # default, dark, mint, retro, pastel
topic = "로봇은 무엇일까요?"
qlist = [
    "로봇은 어떻게 움직이고 사람처럼 거리도 스스로 이동하나요?",
    "로봇이 사람처럼 생각하고 느낄 수 있는 인공지능 기술이 있나요?",
    "로봇은 어떤 재료로 만들어져서 오랫동안 튼튼하게 사용할 수 있나요?",
    "로봇은 공장뿐 아니라 병원이나 학교에서도 실제로 쓰이고 있나요?",
    "로봇은 스스로 판단하여 복잡한 문제를 해결할 수 있을까요?",
    "로봇은 전기 외에도 다른 에너지원으로 움직일 수 있나요?",
    "로봇은 음악을 듣고 춤을 추거나 그림을 그리는 것도 가능한가요?",
    "로봇이 사람을 돕는 직업을 갖게 되면 어떤 도움을 줄 수 있을까요?",
    "로봇은 스스로 배우고 성장하여 사람처럼 똑똑해질 수도 있나요?",
    "로봇은 명령을 어떤 방식으로 받아서 움직이는지 궁금해요, 알려주세요.",
    "만약 로봇이 고장나면 어떻게 수리하고 다시 쓸 수 있을까요?",
    "우리 주변에서 로봇을 가장 쉽게 찾아볼 수 있는 곳은 어디인가요?",
    "로봇이 인간보다 힘이 세거나 더 빨리 움직이는 것도 가능한가요?",
    "로봇이 미래에는 어떤 새로운 기능을 갖추게 될지 궁금해요.",
    "로봇이 발전하면 사람의 일을 빼앗을까 걱정되는데, 어떻게 생각하나요?"
]

alist = [
    "로봇은 바퀴나 다리, 센서 등의 기계 부품으로 명령에 따라 움직여요.",
    "네, 인공지능 기술로 로봇이 단순한 상황에서 간단히 판단해요.",
    "주로 금속, 플라스틱, 특수 합금으로 만들어 오래 쓰기 좋아요.",
    "네, 병원에서 수술 도와주고 학교에서 교육용으로 쓰이고 있어요.",
    "지금은 단순한 작업만 가능하지만, 점차 똑똑해지고 있어 더 어려운 일도 할 거예요.",
    "주로 전기를 쓰지만 일부는 태양광이나 배터리 에너지로도 움직여요.",
    "특정 프로그램으로 음악에 맞춰 움직이거나 간단한 그림을 그릴 수도 있어요.",
    "장애인 도우미, 노인 돌봄, 위험한 현장 작업 등 다양한 분야에서 사람을 도울 거예요.",
    "인공지능 발전 덕분에 로봇은 과거 데이터에서 배우며 점점 똑똑해지고 있어요.",
    "로봇은 컴퓨터 프로그램이나 센서 입력을 통해 전달받은 명령대로 움직여요.",
    "전문가가 부품을 교체하거나 소프트웨어를 재설치해 고친 뒤 다시 사용할 수 있어요.",
    "가장 흔한 곳은 공장 자동화 라인이고, 가끔 청소 로봇도 집에서 볼 수 있어요.",
    "특수한 기계 구조와 빠른 모터 덕분에 일부 로봇은 사람보다 더 강하고 빨라요.",
    "더 자연스러운 대화나 정교한 손동작, 복잡한 문제 해결 능력 등 여러 기능이 생길 거예요.",
    "일부 직업은 변화하지만, 새로운 직업이 생기고 로봇과 사람이 협력해 일하게 될 거예요."
]

os.makedirs('mp3', exist_ok=True)
   
async def talk(string, filepath, actions):
    #speech.tts(string=string, filename=filepath, voice='gtts', lang='ko')
    device.eye_on(random.randint(100,255),random.randint(100,255),random.randint(100,255))
    if actions != None:
        motion_timer = Timer(0, motion.set_motion, args=(random.choice(actions),))
        motion_timer.start()
    audio.play(filepath, VOLUME, background=False)
    motion.set_motion('stop')
    device.eye_off()
    await asyncio.sleep(0.5)

app = FastAPI()

# HTML 템플릿을 위한 경로 설정
templates = Jinja2Templates(directory="templates")

# 메인 페이지 렌더링
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"theme":theme, "request": request, "qlist": qlist, "alist": alist, "initial_volume": VOLUME, "topic":topic}, )

# 버튼 클릭 시 호출되는 엔드포인트
class Question(BaseModel):
    index: int

class VolumeControl(BaseModel):
    volume: int

@app.post("/set_volume/")
async def set_volume(volume_control: VolumeControl):
    global VOLUME
    VOLUME = volume_control.volume
    print(f"Volume set to: {VOLUME}")  # 디버깅용 출력
    return {"message": f"Volume updated to {VOLUME}"}
    
@app.post("/get_answer/")
async def get_answer(question: Question):
    # talk 함수를 비동기 태스크로 실행하여 대기하지 않고 즉시 반환
    asyncio.create_task(talk(alist[question.index], f'mp3/answer_{question.index}.mp3', ["clapping1", "clapping2", "speak_r1","speak_r2", "speak_l1","speak_l2","hand1","hand2", "hand3","hand4"]))
    
    # 즉시 응답 반환
    return {"answer": alist[question.index]}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run('main:app', host='0.0.0.0', port=10001, access_log=False)
