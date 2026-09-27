# Pibo 260624v1 — 이전 버전 대비 바뀐 점

구 openpibo(0.9.2.x, `openpibo.vision`)와 구 IDE(openpibo-os 2024) 기준 예제를 260624v1(openpibo `0.9.3.3.1`)에 맞게 고친 내역입니다.
블록 변환은 `tools/compat/migrate_blocks_260624v1.py`로 했습니다.

## Python

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

## Block

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
| `vision_load_tm` / `vision_predict_tm` | `vision_load_cf('/home/pi/mymodel/', 'model.keras', 'labels.txt')` / `vision_predict_cf` |
| 최상위에 놓인 블록 (시작 블록 없음) | `flag_event`(시작 깃발) 하나 아래로 연결 |

- **`flag_event`**: 260624v1 IDE는 `flag_event`·함수 정의 밖의 최상위 블록을 비활성화해서 실행하지 않습니다(`disable-top-blocks.js`). `flag_event`는 작업공간에 하나만 둘 수 있어, 구 IDE 실행 순서대로 스택을 이어 붙였습니다. 260624v1 공식 예제(`openpibo-os.pibo/examples`)와 같은 구조입니다.
- **Teachable Machine → Classifier**: 260624v1 IDE는 TM 블록을 뺐습니다. 기기 내장 Classifier(Tools)가 만든 `/home/pi/mymodel/model.keras`, `labels.txt`를 씁니다. 블록 예제를 돌리기 전에 Classifier로 같은 클래스 이름의 모델을 만들어야 합니다. TM `.tflite` 모델(`assets/botcard`, `assets/models/tm-sample`)은 Python `TeachableMachine`(`openpibo.vision_classify`) 예제에서만 씁니다.
