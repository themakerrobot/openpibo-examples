# piBrain — 260624v1

> 이 폴더의 예제는 260624v1 이전 IDE에서 작성된 것을 옮겨온 것입니다.
> 260624v1(openpibo-os.pibrain 태그 `260624v1`, openpibo `0.9.3.3.1`) 기준 정적 검사 결과는 [COMPAT.md](COMPAT.md)에 있습니다.
> **실기기 동작 확인은 아직 하지 않았습니다.**
> 버튼 블록 `device_hat_button`은 260624v1에서 `device_pibrain_button`으로 바뀌었습니다.

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
