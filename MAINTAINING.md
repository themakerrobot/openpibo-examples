# 관리 문서

사용자용 안내는 `README.md`와 문서 사이트에 둡니다. 이 파일은 저장소를 관리하는 사람을 위한 내용입니다.

## 버전 현황

| 기기 | OS 버전 | 정적 검사 | 실기기 확인 |
|---|---|---|---|
| Pibo | `260624v1` | 188/188 ([COMPAT](pibo/260624v1/COMPAT.md)) | 진행 전 |
| piBrain | `260624v1` | 25/25 ([COMPAT](pibrain/260624v1/COMPAT.md)) | 진행 전 |

## 새 버전 추가

공식 OS 버전이 발행되면 다음 순서로 폴더를 추가합니다. 이전 버전 폴더는 수정하지 않습니다.

1. 직전 버전 폴더를 `pibo/<새버전>/`, `pibrain/<새버전>/`으로 복사합니다.
2. 새 버전의 openpibo-os 태그를 받아 호환성 검사를 돌립니다. openpibo 라이브러리와 IDE 블록은 openpibo-os 저장소 안의 것이 기준입니다.

   ```bash
   git clone --depth 1 --branch <새버전> https://github.com/themakerrobot/openpibo-os.pibo /tmp/os-pibo
   python3 tools/compat/check_compat.py --os /tmp/os-pibo --examples pibo/<새버전> --report pibo/<새버전>/COMPAT.md
   ```

3. 실패 항목을 고치고, 바뀐 점을 `<새버전>/MIGRATION.md`에 적습니다.
4. `docs/versions.json`의 `status`를 `released`로 바꾸거나 태그를 추가합니다(문서 사이트).
5. `README.md`의 버전 표와 위 **버전 현황**에 한 줄씩 추가하고, 태그 `pibo-<버전>`, `pibrain-<버전>`을 찍습니다.

두 버전 이상에서 같이 쓰는 파일(모델, 마커 이미지 등)은 `assets/`에 한 벌만 둡니다.

## 문서 사이트 (버전별)

GitHub Pages 설정: Settings → Pages → Source = **GitHub Actions**.

각 OS 태그 안의 문서(`docs/build/html`)를 모아 기기·버전별로 GitHub Pages(<https://themakerrobot.github.io/openpibo-guide/>)에 올립니다. 문서 원본은 OS 저장소 태그가 기준이며, 각 OS 저장소의 기존 Pages는 그대로 둡니다.

- 올릴 버전 목록: `docs/versions.json` (`status`: `released` 배포 / `testing` 테스트 중 / `legacy` 구버전)
- 버전에 `repo`를 적으면 기기 기본 저장소 대신 그 저장소의 태그에서 문서를 가져옵니다. Pibo 구버전 `v0.9.2.73`은 `openpibo-python` 태그를 씁니다(piBrain 구버전은 없음).
- 디자인: OS 웹 화면 v2와 같은 Pibo UI Kit(`openpibo-os.pibo`의 `design/`)을 빌드할 때 가져옵니다(`versions.json`의 `ui`). 키트는 OS 저장소에서만 고칩니다.
- 사이트 문구는 사용자용으로만 씁니다. 관리 정보는 이 파일에 둡니다.
- 예제 링크: 이 저장소에 `<기기>/<태그>/` 폴더가 있는 버전에만 첫 화면과 상단 바에 `예제` 버튼이 붙습니다(GitHub 폴더로 연결, `versions.json`의 `examples`). 예제 폴더를 추가하면 다음 배포 때 자동으로 연결됩니다.
- 테스트 중 버전은 모든 페이지 상단에 경고 띠가 붙습니다. 공식 배포되면 `status`를 `released`로 바꿉니다.
- `main`에서 `docs/`, `tools/docs/`가 바뀌거나 Actions에서 수동 실행하면 `.github/workflows/docs.yml`이 사이트를 다시 만들어 배포합니다.
- 영문 문서: 태그(브랜치)에 `docs/build/en`이 있으면 `<기기>/<태그>/en/`으로 함께 올리고, 상단 바에 한국어/English 전환과 첫 화면에 `Docs`(영문) 버튼이 붙습니다. 없는 버전은 한국어만 올립니다.
- 테스트 중 버전은 `"track": "latest-tag"`로 적어 두면 각 OS 저장소의 마지막 태그로 정해집니다(`tools/docs/latest_tag.py`). 태그 이름은 `YYMMDDvN`만 보고, 접미사가 붙은 태그(`-ph`, `-gl` 등)는 뺍니다. 마지막 태그가 이미 목록에 있는 태그(배포 버전)면 따로 올리지 않습니다.
- 매시간 예약 실행이 돌아 마지막 태그(이름과 가리키는 커밋)가 지난 배포(`_nav/latest.json`)와 다를 때만 다시 배포합니다. 태그를 지우면 그 전 태그로, 같은 이름으로 다시 찍으면 새 커밋으로 바뀝니다(태그를 찍고 늦어도 약 1시간 안에 반영). 바로 올리려면 Actions에서 docs 워크플로를 수동 실행합니다.
- 로컬 미리보기: `python3 tools/docs/build_site.py --out _site` 후 `_site`를 웹 서버로 엽니다.

## tools/compat

| 파일 | 용도 |
|---|---|
| `check_compat.py` | 예제를 openpibo-os 배포본의 openpibo 라이브러리·IDE 블록 정의와 대조하는 정적 검사 |
| `extract_blocks.js` | IDE의 `customblock.js`에서 블록 타입·필드·입력을 뽑음 (`check_compat.py`가 사용) |
| `migrate_blocks_260624v1.py` | 구 IDE 블록 JSON을 260624v1 블록으로 변환 |

Python 3와 node가 필요합니다. 정적 검사는 import, 메서드, 인자 개수, 블록 정의, 빈 입력, 시작 깃발 밖의 블록만 확인합니다. 반환값의 의미가 바뀐 것이나 하드웨어 동작은 실기기에서 확인해야 합니다.
