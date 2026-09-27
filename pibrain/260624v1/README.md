# piBrain — 260624v1

> 이 폴더의 예제는 260624v1 이전 IDE에서 작성된 것을 옮겨온 것입니다.
> 260624v1(openpibo-os.pibrain 태그 `260624v1`, openpibo `0.9.3.3.1`) 기준 정적 검사 결과는 [COMPAT.md](COMPAT.md)에 있습니다.
> **실기기 동작 확인은 아직 하지 않았습니다.**

## 260624v1에서 바뀐 점 (예제 수정 내역)

| 구버전 블록 | 260624v1 |
|---|---|
| `device_hat_button(num=4/17/27)` (BCM 번호, 내부 풀다운, HIGH = `on`) | `device_pibrain_button(num=1/2/3)` (SW 번호, 라이브러리가 내부 풀업, LOW = `on`) |
| `vision_face` | `vision_face_detect` (박스 (x1,y1,x2,y2) → 너비·높이 계산 보정) |
| `vision_face_age` / `vision_face_gender` | `vision_face_analyze` 결과에서 `age` / `gender` |
| `vision_imshow_to_ide_img` | `vision_imshow_to_ide` |
| `vision_analyze_pose` 입력 `val` | `v` |
| `vision_face_landmark(img)` 결과의 `data`/`img` | `vision_face_landmark(img, 첫 번째 얼굴 박스)` + `vision_face_landmark_vis` |
| `vision_flip` | 없음 → 원본 이미지 사용 (`personal-trainer/ex_camera.json`, 좌우반전 화면이 아님) |

> **버튼 회로 확인 필요**: 구 블록은 내부 풀다운 + HIGH일 때 눌림, 260624v1 `DeviceByPiBrain`은 내부 풀업 + LOW일 때 눌림으로 처리합니다.
> 같은 보드에서 둘 다 맞을 수는 없으므로, 현재 piBrain 보드의 SW1~SW3 회로(GND 쪽으로 눌리는지)를 회로도로 확인해 주세요.

## block/

| 폴더 | 내용 | 원래 위치 |
|---|---|---|
| `face-id/` | OLED·버튼·카메라 기초 → 얼굴 감지/분석/학습 → 출석, 게임 | `newsac/페이스아이디` |
| `personal-trainer/` | 포즈 인식 기반 퍼스널 트레이너 | `newsac/퍼스널트레이너` |

## project/

| 폴더 | 내용 | 원래 위치 |
|---|---|---|
| `conveyor-belt/` | Arduino 기반 컨베이어 벨트 컨트롤러 (piBrain과 시리얼 통신) | `newsac/컨베이어벨트` |

python 예제는 아직 없습니다.
