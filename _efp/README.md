# OpenPibo Robot Programming Repository

## 소개 (Introduction)

이 저장소는 Pibo 로봇을 활용한 다양한 파이썬 프로그래밍 예제와 프로젝트를 포함하고 있습니다. 기초적인 기능 학습부터 인공지능 기술(컴퓨터 비전, 음성 등)을 접목한 서비스 구현까지 단계별 실습 자료를 제공하는 것을 목표로 합니다.


## 저장소 구조 (Repository Structure)

* **/examples**: `openpibo` 라이브러리의 개별 기능(모션, LED, 센서 등)을 테스트하고 이해하기 위한 간단한 파이썬 예제 코드들이 포함되어 있습니다. 블록 코딩 예제와 유사한 수준의 기본적인 스크립트들입니다.
* **/projects**: Pibo의 여러 기능을 복합적으로 사용하고, 인공지능 기술과 연동하여 좀 더 완성도 있는 서비스를 구현하는 프로젝트 코드들이 포함되어 있습니다. 주석 작업이 진행된 코드들이 이 디렉토리에 해당합니다.
* **/lectures**: Pibo 프로그래밍 관련 강의나 워크숍 진행을 위한 교안, 슬라이드 등의 자료가 포함될 수 있습니다.

## 프로젝트 개요 (/project Directory Overview)

`/project` 디렉토리에는 다음과 같은 주제의 응용 프로젝트 예시들이 포함되어 있습니다:

* **얼굴 인식 기반 상호작용 (Face Interaction)**:
    * 실시간 얼굴 감지 및 화면 중앙 추적 (얼굴 트래킹).
    * 특정 인물 얼굴 데이터 학습 및 저장.
    * 학습된 얼굴 데이터 기반 사용자 인증 및 구별.
* **비전 기반 자율 주행 (Vision-Based Navigation)**:
    * ArUco 마커를 이용한 경로 인식 및 순차 주행.
    * 마커 탐색 로직 (정면 실패 시 고개 돌려 탐색).
    * 주행 중 Teachable Machine 모델을 활용한 객체 분류 기능 통합.
* **웹 연동 서비스 (Web Integration)**:
    * FastAPI를 이용한 웹 서버 구축.
    * 웹 인터페이스를 통한 로봇 제어 (질문-답변, 모션/음성 출력).
    * 실시간 로봇 상태 피드백 (예: 볼륨 조절).
* **음성 처리 (Speech Processing)**:
    * 텍스트 목록을 음성 파일(MP3)로 일괄 변환 (TTS 활용).

## 시작하기 (Getting Started)

### 사전 요구 사항 (Prerequisites)

* Pibo 로봇
* Python 3.x
* `openpibo` 라이브러리:

### 사용 방법 (Usage)

1.  **프로젝트 선택 및 이동 (Select and Navigate to Project)**:
    ```bash
    # 예: 얼굴 인식 프로젝트로 이동
    cd project/face_recognition
    ```
3.  **의존성 설치 (Install Dependencies)**: 각 프로젝트 폴더의 요구사항에 따라 필요한 라이브러리를 설치합니다. (위 `Prerequisites` 참고)
4.  **환경 설정 (Setup Environment)**:
    * **모델/데이터베이스**: 얼굴 인식, Teachable Machine 프로젝트의 경우, 학습된 모델 파일(`.tflite`)이나 얼굴 데이터베이스(`facedb`) 파일을 스크립트 내 지정된 경로에 배치해야 할 수 있습니다.
    * **미디어 파일**: 웹 연동 Q&A, TTS 프로젝트의 경우, 미리 생성된 음성 파일(`mp3`)을 저장할 디렉토리가 필요할 수 있습니다.
    * **마커 배치**: 마커 기반 주행 프로젝트의 경우, 실제 환경에 스크립트(`MARKER_LIST`)에 정의된 ID의 마커를 경로에 맞게 배치해야 합니다.
5.  **스크립트 실행 (Run Script)**:
    ```bash
    python3 <script_name>.py
    ```

## 기여하기 (Contributing)

프로젝트 개선을 위한 기여(버그 수정, 기능 추가, 새로운 프로젝트 제안 등)는 언제나 환영입니다. 이슈를 생성하거나 Pull Request를 보내주세요.
