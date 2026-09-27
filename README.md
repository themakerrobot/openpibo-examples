# openpibo-examples

Pibo / piBrain 예제 저장소. **기기 → 버전 → 종류(python / block / project)** 순서로 정리합니다.

```
openpibo-examples/
├── pibo/
│   └── 260624v1/
│       ├── python/     # 파이썬 예제 (basics, modules, 주제별)
│       ├── block/      # 블록코딩 JSON (basics, examples, botcard, 주제별)
│       ├── project/    # 여러 기능을 묶은 응용 프로젝트
│       └── lectures/   # 교안 PDF
├── pibrain/
│   └── 260624v1/
│       ├── block/
│       └── project/
└── assets/             # 기기·버전 공통 자원 (AR 마커, 봇카드 모델, TM 샘플 모델 등)
```

## 버전 관리 규칙

- 버전 폴더 이름은 기기 이미지 버전을 그대로 사용합니다 (예: `260624v1`).
- 공식 버전이 발행되면 `pibo/<새버전>/`, `pibrain/<새버전>/` 폴더를 추가합니다. 이전 버전 폴더는 수정하지 않고 유지합니다.
- 버전 폴더를 추가할 때 git 태그 `pibo-<버전>`, `pibrain-<버전>`을 함께 찍습니다.
- 두 버전 이상에서 공통으로 쓰는 파일(모델, 마커 이미지 등)은 `assets/`에 한 벌만 둡니다.

## 호환성 검사

새 버전 폴더를 만들 때 그 버전의 openpibo-os 태그를 받아 정적 검사를 돌리고, 결과를 `COMPAT.md`로 남깁니다.
openpibo 라이브러리는 openpibo-os 저장소 안의 것을 기준으로 합니다. 구 `openpibo-python` 저장소는 쓰지 않습니다.

```bash
git clone --depth 1 --branch 260624v1 https://github.com/themakerrobot/openpibo-os.pibo /tmp/os-pibo
python3 tools/compat/check_compat.py --os /tmp/os-pibo --examples pibo/260624v1 --report pibo/260624v1/COMPAT.md
```

정적 검사는 import, 메서드, 인자 개수, 블록 정의만 확인합니다. 반환값 형식이 바뀐 것이나 실제 하드웨어 동작은 실기기에서 확인해야 합니다. Python 3와 node가 필요합니다.

## 기기별 README

- [pibo/260624v1](pibo/260624v1/README.md)
- [pibrain/260624v1](pibrain/260624v1/README.md)
- [assets](assets/README.md)

## 이력

- 구 `themakerrobot/examples-for-pibo` 저장소는 이 저장소에 병합되었습니다 (git 이력 보존).
- 기존 `basic/`, `guide/`, `project/`, `newsac/`, `app/`, `data/` 폴더는 위 구조로 재배치되었습니다. 이전 경로는 git 이력에서 확인할 수 있습니다.
