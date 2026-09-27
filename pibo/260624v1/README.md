# Pibo — 260624v1

> 구 openpibo(0.9.2.x, `openpibo.vision`) 기준 예제를 260624v1(openpibo-os.pibo 태그 `260624v1`, openpibo `0.9.3.3.1`)에 맞게 옮겼습니다.
> 정적 검사 결과는 [COMPAT.md](COMPAT.md)에 있습니다. **실기기 동작 확인은 아직 하지 않았습니다.**

## 260624v1에서 바뀐 점 (예제 수정 내역)

**Python**

| 구버전 | 260624v1 |
|---|---|
| `from openpibo.vision import Camera / Detect / Face / TeachableMachine` | `openpibo.vision_camera` / `vision_detect` / `vision_face` / `vision_classify` |
| `speech.tts(string=...)` | `speech.tts(text=...)` |
| `face.detect_face()` → `(x, y, w, h)` | `(x1, y1, x2, y2)` (docstring은 아직 `x, y, w, h`로 적혀 있음) |
| `detect.detect_qr()` → 딕셔너리 1개, `position` | 리스트, `box` |
| `detect.detect_object()` 항목의 `position` | `box` |
| `detect.detect_marker()` → `{"data", "img"}` | 리스트. 그리기는 `detect_marker_vis(img, items)` |
| `detect.detect_pose()` → `{"data", "img"}` | 리스트. 그리기는 `detect_pose_vis(img, items)` |
| `face.get_ageGender()` | `face.analyze_face()` → `{"age", "gender", "emotion", "box"}` |
| `detect.classify_image()` | 없음 (`p_vision1.py`에서 제거) |
| `Dialog.mecab_pos / morphs / nouns` | 없음 (`chatbot_test.py`는 단어 포함 여부로 판단, `mecab_test.py` 삭제) |

**Block** (`tools/compat/migrate_blocks_260624v1.py`로 변환)

| 구버전 블록 | 260624v1 |
|---|---|
| `vision_imshow_to_ide_img` | `vision_imshow_to_ide` |
| `vision_face` | `vision_face_detect` (박스의 3·4번째 값은 x2, y2 → 너비·높이 계산을 `x2-x1`, `y2-y1`로 바꿈) |
| `vision_face_age` / `vision_face_gender` | `vision_face_analyze` 결과에서 `age` / `gender` |
| `vision_classification` | `vision_object` (이미지 분류 → 사물 인식 이름 목록) |
| `device_eye_off` | `device_eye_on(0,0,0,0,0,0)` |
| `device_eye_fade` | `device_eye_colour_on` (서서히 켜기 없음) |
| `vision_analyze_pose` 입력 `val` | `v` |
| `vision_marker_detect` / `vision_pose` / `vision_face_landmark` 결과의 `data` / `img` | 결과 리스트 그대로 / `*_vis` 블록으로 원본 이미지에 그림 |
| `vision_face_landmark(img)` | `vision_face_landmark(img, 첫 번째 얼굴 박스)` — 얼굴이 없으면 실행 중 에러 |
| `vision_load_tm` / `vision_predict_tm` | **260624v1에 없음** — 아래 "미해결" 참고 |

## 미해결

- Teachable Machine 블록 예제 6개 (`block/automove/5_predict_tm.json`, `block/basics/p_vision3.json`, `block/botcard/bc_tm.json`, `block/examples/ex_project.json`, `block/examples/ex_tm.json`, `block/sign-language/result.json`)
  - 260624v1 IDE에서 `vision_load_tm`/`vision_predict_tm`이 주석 처리되어 IDE에서 열리지 않습니다.
  - 대체 블록 `vision_load_cf`/`vision_predict_cf`는 기기 내장 Classifier에서 만든 `model.keras` 전용이라 TM `.tflite` 모델(`assets/botcard`, `assets/models/tm-sample`)은 쓸 수 없습니다.
  - Python의 `TeachableMachine`(`openpibo.vision_classify`)은 260624v1에도 있어 `python/automove/5_predict_tm.py` 등은 그대로 동작합니다.

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


## 자원 파일 경로

예제 코드는 아래 경로를 전제로 합니다. `assets/`에서 복사해 두세요.

| 예제에서 쓰는 경로 | 복사할 파일 |
|---|---|
| `/home/pi/mymodel/model_unquant.tflite`, `labels.txt` | `assets/models/tm-sample/` (봇카드 예제는 `assets/botcard/`) |
| `/home/pi/code/mychat.csv` | `assets/dialog/mychat.csv` |

## lectures/

봇카드, 블록코딩, 비서로봇, 자율주행로봇, 파이썬 교안 PDF (examples-for-pibo `lectures/`).
