# -*- coding: utf-8 -*-

import uvicorn
import argparse
import cv2
import json
import logging
import os
import time
import numpy as np
from contextlib import asynccontextmanager
from typing import List, Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- openpibo 라이브러리 임포트 ---
from openpibo.vision_camera import Camera
from openpibo.audio import Audio
from openpibo.speech import Speech
from openpibo.motion import Motion
from openpibo.device import Device

# --- 로깅 설정 ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# --- Pibo 클래스 ---
class Pibo:
    def __init__(self):
        logging.info('Pibo Class INITIALIZING...')
        self.dev = Device()
        self.mot = Motion()
        self.aud = Audio()
        self.speech = Speech()
        self.cam = Camera()
        logging.info('Pibo Class INITIALIZED COMPLETE')

    def get_frame(self):
        try:
            return self.cam.read()
        except Exception as e:
            logging.error(f"[get_frame] Error: {e}")
            return np.zeros((240, 320, 3), dtype=np.uint8)

    def send_message(self, code, data=""):
        """명령을 로봇 하드웨어로 직접 전송합니다."""
        try:
            msg = f'#{code}:{data}!'
            response = self.dev.send_raw(msg)
            logging.info(f"Sent: {msg}, Received: {response}")
        except Exception as e:
            logging.error(f"Failed to send message {msg}: {e}")

# --- FastAPI 애플리케이션 설정 ---
pibo = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pibo
    pibo = Pibo()
    logging.info("Pibo instance created via lifespan.")
    yield
    logging.info("Application shutting down...")
    if pibo:
        pibo.device_stop()

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 데이터 모델 (Pydantic) ---
class NeoPixelRequest(BaseModel):
    colors: List[int]

class TTSRequest(BaseModel):
    text: str
    voice_type: Optional[str] = "gtts"
    volume: Optional[int] = -1

class MotionRunRequest(BaseModel):
    name: str
    cycle: Optional[int] = 1

class SetMotorRequest(BaseModel):
    n: int
    pos: int

# --- API Endpoints ---
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("index.html")

def frame_generator():
    while True:
        if pibo:
            frame = pibo.get_frame()
            if frame is not None:
                _, buffer = cv2.imencode('.jpg', frame)
                
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.2)

@app.get("/vision/stream")
def video_feed():
    return StreamingResponse(frame_generator(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.post("/device/neopixel")
def set_neopixel(request: NeoPixelRequest):
    if len(request.colors) == 6:
        color_str = ','.join(map(str, request.colors))
        pibo.send_message("23", color_str)
        return JSONResponse(content={'status': 'success', 'colors': request.colors})
    return JSONResponse(content={'status': 'error', 'message': 'Color list must contain 6 integer values.'}, status_code=400)

@app.post("/speech/tts")
def text_to_speech(request: TTSRequest):
    filename = "/home/pi/tts_output.mp3"
    try:
        pibo.speech.tts(text=request.text, filename=filename, voice=request.voice_type)
        pibo.aud.play(filename, volume=request.volume, background=False)
        return JSONResponse(content={'status': 'success', 'text': request.text})
    except Exception as e:
        return JSONResponse(content={'status': 'error', 'message': str(e)}, status_code=500)

@app.post("/motion/move")
def run_motion(request: MotionRunRequest):
    try:
        pibo.mot.set_motion(request.name, request.cycle)
        if request.name == "stop":
            pibo.mot.stop()

        return JSONResponse(content={'status': 'success', 'motion': request.name})
    except Exception as e:
        return JSONResponse(content={'status': 'error', 'message': f"Motion '{request.name}' not found: {e}"}, status_code=404)

@app.post("/motion/set_motor")
def set_motor(request: SetMotorRequest):
    """지정된 번호의 모터를 지정된 위치로 이동시킵니다."""
    try:
        pibo.mot.set_motor(request.n, request.pos)
        return JSONResponse(content={'status': 'success', 'motor': request.n, 'position': request.pos})
    except Exception as e:
        return JSONResponse(content={'status': 'error', 'message': str(e)}, status_code=500)

# --- 서버 실행 ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # [수정됨] 포트 번호 51111로 변경
    parser.add_argument('--port', help='set port number', default=51111, type=int)
    args = parser.parse_args()
    
    # [수정됨] reload=False로 변경
    uvicorn.run("main:app", host="0.0.0.0", port=args.port, reload=False)
