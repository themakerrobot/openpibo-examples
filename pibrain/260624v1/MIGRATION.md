# piBrain 260624v1 — 이전 버전 대비 바뀐 점

구버전 IDE 기준 블록 예제를 260624v1에 맞게 고친 내역입니다.
블록 변환은 `tools/compat/migrate_blocks_260624v1.py`로 했습니다.

## Block

| 구버전 블록 | 260624v1 |
|---|---|
| `device_hat_button(num=4/17/27)` (BCM 번호, 내부 풀다운, HIGH = `on`) | `device_pibrain_button(num=1/2/3)` (SW 번호, 라이브러리가 내부 풀업, LOW = `on`) |
| `vision_face` | `vision_face_detect` (박스 (x1,y1,x2,y2) → 너비·높이 계산 보정) |
| `vision_face_age` / `vision_face_gender` | `vision_face_analyze` 결과에서 `age` / `gender` |
| `vision_imshow_to_ide_img` | `vision_imshow_to_ide` |
| `vision_analyze_pose` 입력 `val` | `v` |
| `vision_face_landmark(img)` 결과의 `data`/`img` | `vision_face_landmark(img, 첫 번째 얼굴 박스)` + `vision_face_landmark_vis` |
| `vision_flip` | 없음 → 원본 이미지 사용 (`personal-trainer/ex_camera.json`, 좌우반전 화면이 아님) |
| 최상위에 놓인 블록 (시작 블록 없음) | `flag_event`(시작 깃발) 하나 아래로 연결. 260624v1 IDE는 시작 블록 밖의 블록을 실행하지 않음 (`openpibo-os.pibrain/examples`와 같은 구조) |
