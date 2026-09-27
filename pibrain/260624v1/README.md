# piBrain — 260624v1

- 기준: openpibo-os.pibrain 태그 `260624v1`, openpibo `0.9.3.3.1`
- 정적 검사: [COMPAT.md](COMPAT.md) (25/25 통과)
- 실기기 확인: **진행 전**
- 이전 버전 대비 바뀐 점: [MIGRATION.md](MIGRATION.md)

## block/

| 폴더 | 내용 |
|---|---|
| `face-id/` | OLED·버튼·카메라 기초 → 얼굴 감지/분석/학습 → 출석, 게임 |
| `personal-trainer/` | 포즈 인식 기반 퍼스널 트레이너 |

## project/

| 폴더 | 내용 |
|---|---|
| `conveyor-belt/` | Arduino 컨베이어 벨트 컨트롤러 (piBrain과 시리얼 통신). 배선 전 [README](project/conveyor-belt/README.md)의 확인 사항을 먼저 보세요 |

python 예제는 아직 없습니다.

## 버튼

`device_pibrain_button`의 SW1~SW3은 BCM 4 / 17 / 27입니다. 260624v1 `DeviceByPiBrain`은 내부 풀업을 걸고 LOW일 때 `on`을 돌려줍니다.

> **회로 확인 필요**: 구 블록(`device_hat_button`)은 내부 풀다운을 걸고 HIGH일 때 `on`으로 처리했습니다.
> 같은 보드에서 둘 다 맞을 수는 없으므로, 보드 회로도에서 SW1~SW3이 GND 쪽으로 닫히는지 확인해 주세요.

## 주의

- `face-id/9_landmark.json`은 화면에 얼굴이 없으면 실행 중 에러가 납니다.
- `personal-trainer/ex_camera.json`은 좌우반전 블록이 없어 반전되지 않은 화면이 나옵니다.
