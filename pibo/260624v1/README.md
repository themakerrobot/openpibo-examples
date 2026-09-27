# Pibo — 260624v1

- 기준: openpibo-os.pibo 태그 `260624v1`, openpibo `0.9.3.3.1`
- 정적 검사: [COMPAT.md](COMPAT.md) (188/188 통과)
- 실기기 확인: **진행 전**
- 이전 버전 대비 바뀐 점: [MIGRATION.md](MIGRATION.md)

## python/

| 폴더 | 내용 |
|---|---|
| `basics/` | `b_*`: 파이썬 문법 기초, `p_*`: openpibo 기능별 예제 |
| `modules/` | 모듈별 단위 테스트 (audio, collect, device, ext, motion, oled, speech, vision) |
| `assistant/` | 비서 로봇 단계별 예제 |
| `automove/` | 자율행동(ArUco 마커 주행) 단계별 예제 |

## block/

| 폴더 | 내용 |
|---|---|
| `basics/` | 블록코딩 기초 |
| `examples/` | 기능별·응용 블록 예제 |
| `botcard/` | 봇카드(QR) 인식, Classifier 분류 |
| `assistant/` | 비서 로봇 블록 버전 |
| `automove/` | 자율행동 블록 버전 |
| `sign-language/` | 수화 |
| `history-performance/` | 역사문화공연 |

## project/

| 폴더 | 내용 |
|---|---|
| `assistant-bot/` | 봇카드로 날씨·뉴스·대화 기능을 고르는 비서 |
| `automove-bot/` | ArUco 마커 경로 주행 + Teachable Machine 분류 |
| `face-recognition-bot/` | 얼굴 학습/인식 |
| `face-recognition-simple/` | 얼굴 학습/인식 최소 예제 |
| `face-tracking-bot/` | 얼굴 추적 (`face_tracking.json`은 블록 버전) |
| `guide-bot/` | FastAPI 웹 Q&A 안내 로봇 |
| `pose-avatar/` | 포즈 따라하기 (블록) |
| `web-controller/` | FastAPI 웹 컨트롤러 |

## lectures/

봇카드, 블록코딩, 비서로봇, 자율주행로봇, 파이썬 교안 PDF.

## 준비

예제 코드는 아래 경로를 전제로 합니다.

| 예제에서 쓰는 경로 | 준비 방법 | 사용하는 예제 |
|---|---|---|
| `/home/pi/mymodel/model.keras`, `labels.txt` | IDE의 **Image Classifier**로 모델을 변환하면 이 경로에 저장됩니다 | 블록의 `vision_load_cf` (`p_vision3`, `bc_tm`, `ex_tm`, `ex_project`, `automove/5_predict_tm`, `sign-language/result`) |
| `/home/pi/mymodel/model_unquant.tflite`, `labels.txt` | `assets/models/tm-sample/`을 복사하거나 Teachable Machine에서 TFLite로 내보내기 | Python의 `TeachableMachine` (`p_vision3.py`, `automove/5_predict_tm.py` 등) |
| `/home/pi/code/mychat.csv` | `assets/dialog/mychat.csv` 복사 | `p_voice` |
| ArUco `DICT_4X4_50` 마커 (한 변 8.5cm) | `assets/aruco/4x4_50/` 인쇄 | `automove` 예제·프로젝트 |

- 클래스 이름으로 동작을 나누는 예제는 예제에 적힌 클래스 이름과 같은 이름으로 모델을 학습해야 합니다.
- Teachable Machine `.tflite` 모델은 260624v1 블록에서 쓸 수 없고, Python `TeachableMachine`에서만 쓸 수 있습니다.
- Image Classifier와 Python TM 예제가 모두 `/home/pi/mymodel/labels.txt`를 씁니다. Image Classifier로 변환하면 이 파일이 덮어써지므로, 둘을 번갈아 쓸 때는 라벨 파일을 다시 복사하세요.

## 주의

- 랜드마크 블록 예제(`history-performance/vision.json`)는 화면에 얼굴이 없으면 실행 중 에러가 납니다.
- `face.detect_face()`의 반환값은 `(x1, y1, x2, y2)`입니다. openpibo 0.9.3.3.1 docstring에는 아직 `(x, y, w, h)`로 적혀 있습니다.
