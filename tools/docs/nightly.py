#!/usr/bin/env python3
"""
nightly 버전(status "nightly", 예: 브랜치 main)의 문서가 바뀌었는지 확인한다.

각 nightly 버전마다 OS 저장소에서 docs/build(한국어 html·영문 en)를 마지막으로 바꾼 커밋을 GitHub API 로 찾는다.
코드만 바뀐 푸시는 무시되고, 빌드한 문서를 커밋했을 때만 값이 바뀐다.

  python3 tools/docs/nightly.py                      현재 상태를 JSON 으로 출력
  python3 tools/docs/nightly.py --compare <URL>      배포된 사이트의 _nav/nightly.json 과 비교해
                                                     changed=true|false 를 출력 (GitHub Actions 출력용)

GITHUB_TOKEN 또는 GH_TOKEN 이 있으면 API 호출에 쓴다(없어도 공개 저장소는 동작).
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_PATH = "docs/build"  # 한국어(html)·영문(en) 빌드 결과


def _get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "openpibo-guide-docs"})
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def last_docs_commit(repo_url, ref):
    """ref(브랜치)에서 docs/build 를 마지막으로 바꾼 커밋 {sha, date}."""
    owner, name = repo_url.rstrip("/").split("/")[-2:]
    data = _get(f"https://api.github.com/repos/{owner}/{name}/commits?sha={ref}&path={DOCS_PATH}&per_page=1")
    if not data:
        raise SystemExit(f"{owner}/{name}@{ref}: {DOCS_PATH} 커밋이 없습니다")
    c = data[0]
    return {"sha": c["sha"], "date": c["commit"]["committer"]["date"][:10]}


def state(cfg):
    """{"<기기>/<태그>": {sha, date}} — nightly 버전만."""
    out = {}
    for dev in cfg["devices"]:
        for v in dev["versions"]:
            if v["status"] == "nightly":
                out[f'{dev["id"]}/{v["tag"]}'] = last_docs_commit(v.get("repo", dev["repo"]), v["tag"])
    return out


def load_cfg():
    with open(os.path.join(ROOT, "docs", "versions.json"), encoding="utf-8") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--compare", metavar="URL", help="배포된 _nav/nightly.json 주소")
    args = ap.parse_args()

    cur = state(load_cfg())
    if not args.compare:
        print(json.dumps(cur, ensure_ascii=False, indent=2))
        return
    try:
        prev = _get(args.compare)
    except (urllib.error.URLError, ValueError) as e:  # 첫 배포이거나 사이트가 없으면 배포한다
        print(f"배포된 상태 없음: {e}", file=sys.stderr)
        prev = None
    same = {k: v["sha"] for k, v in cur.items()} == {k: v.get("sha") for k, v in (prev or {}).items()}
    for k, v in cur.items():
        print(f"{k}: {v['sha'][:7]} ({v['date']})", file=sys.stderr)
    print(f"changed={'false' if same else 'true'}")


if __name__ == "__main__":
    main()
