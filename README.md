# openpibo-guide

Pibo / piBrain 예제와 버전별 문서입니다.

- **문서**: <https://themakerrobot.github.io/openpibo-guide/>
- **예제**: 이 저장소의 `기기/OS 버전/` 폴더

내 기기의 OS 버전과 같은 버전의 예제·문서를 쓰세요. 버전이 다르면 import 경로나 블록 이름이 달라 동작하지 않을 수 있습니다.

| 기기 | OS 버전 | 예제 | 문서 |
|---|---|---|---|
| Pibo | `260624v1` | [python · block · project · 교안](pibo/260624v1/README.md) | [문서](https://themakerrobot.github.io/openpibo-guide/pibo/260624v1/index.html) |
| piBrain | `260624v1` | [block · project](pibrain/260624v1/README.md) | [문서](https://themakerrobot.github.io/openpibo-guide/pibrain/260624v1/index.html) |

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
└── assets/         # 버전 공통 자원 (ArUco 마커, 모델, 대화 데이터)
```

## 사용법

1. 기기 IDE에서 해당 버전 폴더의 `.py` 또는 블록 `.json` 파일을 열어 실행합니다.
2. 모델·이미지·대화 데이터가 필요한 예제는 버전 폴더 README의 **준비** 항목대로 파일을 먼저 복사합니다.
3. 블록 예제는 모두 시작 깃발(`flag_event`) 블록 아래에 있습니다. 260624v1 IDE는 시작 깃발 밖의 블록을 실행하지 않습니다.
