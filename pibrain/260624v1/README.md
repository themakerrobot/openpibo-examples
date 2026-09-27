# piBrain — 260624v1

> 이 폴더의 예제는 260624v1 이미지 이전에 작성된 것을 옮겨온 것입니다. **실기기 검증 필요.**
> 여기에 있는 블록 예제는 모두 `device_hat_button`(piBrain 버튼 SW1=BCM4, SW2=BCM17, SW3=BCM27, openpibo 블록 가이드 기준)을 사용하고, motion/audio/speech는 사용하지 않습니다.

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
