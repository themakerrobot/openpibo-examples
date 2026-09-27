# assets

두 버전 이상에서 같이 쓰는 자원입니다. 예제가 쓰는 기기 안 경로로 복사해서 사용합니다.

| 경로 | 내용 | 복사할 위치 | 사용하는 예제 |
|---|---|---|---|
| `aruco/4x4_50/` | ArUco `DICT_4X4_50` 마커 이미지 (ID 0~49) | 인쇄 (예제 기준 한 변 8.5cm) | `automove` 예제·프로젝트 |
| `models/tm-sample/` | Teachable Machine 샘플 모델 (`model_unquant.tflite`, `labels.txt`) | `/home/pi/mymodel/` | Python `TeachableMachine` 예제 (`p_vision3.py`, `automove/5_predict_tm.py` 등) |
| `botcard/` | 봇카드 Teachable Machine 모델 (`model_unquant.tflite`, `labels.txt`) | `/home/pi/mymodel/` | Python `TeachableMachine` 전용. 260624v1 블록(`vision_load_cf`)에서는 쓸 수 없습니다 |
| `dialog/mychat.csv` | 대화 예제용 질문-답변 데이터 | `/home/pi/code/` | `p_voice` |
| `tools/pibo-maker.html` | 파이보 메이커 접속 페이지 | — | — |
