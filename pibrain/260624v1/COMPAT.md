# 호환성 검사 — `pibrain/260624v1`

- 기준: openpibo-os 태그 `260624v1`, openpibo `0.9.3.3.1`
- 방법: 정적 검사 (`tools/compat/check_compat.py`). **실기기 동작 확인은 별도.**
- 결과: 25개 중 OK 10 / FAIL 15

| 파일 | 종류 | 결과 | 문제 |
|---|---|---|---|
| `block/face-id/10_detect_face.json` | block | FAIL | 블록 `vision_face` 정의 없음 |
| `block/face-id/11_analyze_face.json` | block | FAIL | 블록 `vision_face_age` 정의 없음<br>블록 `vision_face_gender` 정의 없음<br>블록 `vision_face` 정의 없음 |
| `block/face-id/12_train_face.json` | block | FAIL | 블록 `vision_face` 정의 없음 |
| `block/face-id/13_attedance.json` | block | FAIL | 블록 `vision_face` 정의 없음 |
| `block/face-id/14_face_game.json` | block | FAIL | 블록 `vision_face` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/face-id/1_print.json` | block | OK |  |
| `block/face-id/2_lcd1.json` | block | OK |  |
| `block/face-id/2_lcd2.json` | block | OK |  |
| `block/face-id/2_lcd3.json` | block | OK |  |
| `block/face-id/3_pixel.json` | block | OK |  |
| `block/face-id/4_button.json` | block | FAIL | 블록 `device_hat_button` 정의 없음 |
| `block/face-id/5_loop.json` | block | OK |  |
| `block/face-id/6_logic.json` | block | OK |  |
| `block/face-id/7_camera1.json` | block | OK |  |
| `block/face-id/7_camera2.json` | block | FAIL | 블록 `device_hat_button` 정의 없음 ×3 |
| `block/face-id/8_dictionary.json` | block | OK |  |
| `block/face-id/9_landmark.json` | block | OK |  |
| `block/personal-trainer/ex_analyze_pose.json` | block | FAIL | 블록 `vision_analyze_pose` 입력 `val` 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/personal-trainer/ex_camera.json` | block | FAIL | 블록 `device_hat_button` 정의 없음 ×3<br>블록 `vision_flip` 정의 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/personal-trainer/ex_custom_pose.json` | block | FAIL | 블록 `vision_analyze_pose` 입력 `val` 없음 |
| `block/personal-trainer/ex_detect_pose.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/personal-trainer/ex_draw_pose.json` | block | FAIL | 블록 `vision_analyze_pose` 입력 `val` 없음<br>블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/personal-trainer/ex_image.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
| `block/personal-trainer/final.json` | block | FAIL | 블록 `vision_analyze_pose` 입력 `val` 없음 ×3 |
| `block/personal-trainer/print.json` | block | FAIL | 블록 `vision_imshow_to_ide_img` 정의 없음 |
