# Pibo — 260624v1

> 이 폴더의 예제는 openpibo 0.9.2.x(2024~2025) 기준으로 작성된 것을 옮겨온 것입니다.
> **260624v1 이미지 실기기 검증은 아직 완료되지 않았습니다.** 검증한 항목은 아래 표에 표시합니다.

## python/

| 폴더 | 내용 | 원래 위치 |
|---|---|---|
| `basics/` | `b_*`: 파이썬 문법 기초, `p_*`: openpibo 기능별 예제 | `guide/python`, examples-for-pibo `examples/python` (동일 파일) |
| `modules/` | 모듈별 단위 테스트 (audio, collect, device, ext, motion, oled, speech, vision) | `basic/` |
| `assistant/` | 비서 로봇 단계별 예제 | `newsac/비서` |
| `automove/` | 자율행동(마커 주행) 단계별 예제 | `newsac/자율행동` |

## block/

| 폴더 | 내용 | 원래 위치 |
|---|---|---|
| `basics/` | 블록코딩 기초 (`version`: 240402) | `guide/block-coding`, examples-for-pibo `examples/block` |
| `examples/` | 기능별·응용 블록 예제 | `basic/block` (`newsac/휴머노이드AISW`의 상위 집합이라 그쪽은 제거) |
| `botcard/` | 봇카드 블록 예제 (`version`: 2403) | `guide/botcard` |
| `assistant/` | 비서 로봇 블록 버전 | `newsac/easy/비서` |
| `automove/` | 자율행동 블록 버전 | `newsac/easy/자율행동` |
| `sign-language/` | 수화 | `newsac/수화` |
| `history-performance/` | 역사문화공연 | `newsac/역사문화공연` |

## project/

| 폴더 | 내용 | 원래 위치 |
|---|---|---|
| `assistant-bot/` | 날씨·뉴스·대화 비서 | examples-for-pibo |
| `automove-bot/` | ArUco 마커 경로 주행 + TM 분류 | examples-for-pibo |
| `face-recognition-bot/` | 얼굴 학습/인식 | examples-for-pibo |
| `face-recognition-simple/` | 얼굴 학습/인식 최소 예제 | `project/` |
| `face-tracking-bot/` | 얼굴 추적 (`face_tracking.json`은 블록 버전) | examples-for-pibo, `project/` |
| `guide-bot/` | FastAPI 웹 Q&A 안내 로봇 | examples-for-pibo |
| `pose-avatar/` | 포즈 따라하기 (블록) | `project/` |
| `web-controller/` | FastAPI 웹 컨트롤러 | `app/controller` |

> `web-controller/main.py`는 `openpibo.vision_camera`를 import합니다. 공개된 openpibo-python(0.9.2.74)에는 이 모듈이 없습니다.
> 260624v1 이미지의 openpibo에 이 모듈이 포함되어 있는지 **확인 필요**합니다.

## 자원 파일 경로

예제 코드는 아래 경로를 전제로 합니다. `assets/`에서 복사해 두세요.

| 예제에서 쓰는 경로 | 복사할 파일 |
|---|---|
| `/home/pi/mymodel/model_unquant.tflite`, `labels.txt` | `assets/models/tm-sample/` (봇카드 예제는 `assets/botcard/`) |
| `/home/pi/code/mychat.csv` | `assets/dialog/mychat.csv` |

## lectures/

봇카드, 블록코딩, 비서로봇, 자율주행로봇, 파이썬 교안 PDF (examples-for-pibo `lectures/`).
