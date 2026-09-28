# openpibo-guide

Pibo / piBrain 예제 모음입니다. **기기 → OS 버전 → 종류(python / block / project)** 순서로 정리되어 있습니다.

| 기기 | OS 버전 | openpibo | 예제 | 정적 검사 | 실기기 확인 |
|---|---|---|---|---|---|
| Pibo | [`260624v1`](pibo/260624v1/README.md) | 0.9.3.3.1 | python · block · project · 교안 | 188/188 ([COMPAT](pibo/260624v1/COMPAT.md)) | 진행 전 |
| piBrain | [`260624v1`](pibrain/260624v1/README.md) | 0.9.3.3.1 | block · project | 25/25 ([COMPAT](pibrain/260624v1/COMPAT.md)) | 진행 전 |

기기의 OS 버전과 같은 폴더의 예제를 쓰세요. 다른 버전 폴더의 예제는 import 경로나 블록 이름이 달라 동작하지 않을 수 있습니다.

## 구조

```
openpibo-guide/
├── pibo/<버전>/
│   ├── python/     # 파이썬 예제 (basics, modules, 주제별)
│   ├── block/      # 블록코딩 JSON (basics, examples, botcard, 주제별)
│   ├── project/    # 여러 기능을 묶은 응용 프로젝트
│   └── lectures/   # 교안 PDF
├── pibrain/<버전>/
│   ├── block/
│   └── project/
├── assets/         # 버전 공통 자원 (ArUco 마커, 모델, 대화 데이터)
└── tools/compat/   # 호환성 검사기, 블록 변환기
```

## 사용법

1. 기기 IDE에서 해당 버전 폴더의 `.py` 또는 블록 `.json` 파일을 열어 실행합니다.
2. 모델·이미지·대화 데이터가 필요한 예제는 버전 폴더 README의 **준비** 항목대로 파일을 먼저 복사합니다.
3. 블록 예제는 모두 `flag_event`(시작 깃발) 블록 아래에 있습니다. 260624v1 IDE는 시작 깃발 밖의 블록을 실행하지 않습니다.

## 새 버전 추가

공식 OS 버전이 발행되면 다음 순서로 폴더를 추가합니다. 이전 버전 폴더는 수정하지 않습니다.

1. 직전 버전 폴더를 `pibo/<새버전>/`, `pibrain/<새버전>/`으로 복사합니다.
2. 새 버전의 openpibo-os 태그를 받아 호환성 검사를 돌립니다. openpibo 라이브러리와 IDE 블록은 openpibo-os 저장소 안의 것이 기준입니다.

   ```bash
   git clone --depth 1 --branch <새버전> https://github.com/themakerrobot/openpibo-os.pibo /tmp/os-pibo
   python3 tools/compat/check_compat.py --os /tmp/os-pibo --examples pibo/<새버전> --report pibo/<새버전>/COMPAT.md
   ```

3. 실패 항목을 고치고, 바뀐 점을 `<새버전>/MIGRATION.md`에 적습니다.
4. 이 README의 버전 표에 한 줄을 추가하고, 태그 `pibo-<버전>`, `pibrain-<버전>`을 찍습니다.

두 버전 이상에서 같이 쓰는 파일(모델, 마커 이미지 등)은 `assets/`에 한 벌만 둡니다.

## 문서 사이트 (버전별)

각 OS 태그 안의 문서(`docs/build/html`)를 모아 기기·버전별로 GitHub Pages(<https://themakerrobot.github.io/openpibo-guide/>)에 올립니다. 문서 원본은 OS 저장소 태그가 기준이며, 각 OS 저장소의 기존 Pages는 그대로 둡니다.

- 올릴 버전 목록: `docs/versions.json` (`status`: `released` 배포 / `testing` 테스트 중)
- 테스트 중 버전은 모든 페이지 상단에 경고 띠가 붙습니다. 공식 배포되면 `status`를 `released`로 바꿉니다.
- `main`에서 `docs/`가 바뀌면 `.github/workflows/docs.yml`이 사이트를 다시 만들어 배포합니다.
- 로컬 미리보기: `python3 tools/docs/build_site.py --out _site` 후 `_site`를 웹 서버로 엽니다.

## tools/compat

| 파일 | 용도 |
|---|---|
| `check_compat.py` | 예제를 openpibo-os 배포본의 openpibo 라이브러리·IDE 블록 정의와 대조하는 정적 검사 |
| `extract_blocks.js` | IDE의 `customblock.js`에서 블록 타입·필드·입력을 뽑음 (`check_compat.py`가 사용) |
| `migrate_blocks_260624v1.py` | 구 IDE 블록 JSON을 260624v1 블록으로 변환 |

Python 3와 node가 필요합니다. 정적 검사는 import, 메서드, 인자 개수, 블록 정의, 빈 입력, 시작 깃발 밖의 블록만 확인합니다. 반환값의 의미가 바뀐 것이나 하드웨어 동작은 실기기에서 확인해야 합니다.
