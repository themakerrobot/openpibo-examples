#!/usr/bin/env python3
"""
기기마다 OS 저장소의 마지막 태그를 찾는다 (versions.json 에서 "track": "latest-tag" 인 버전).

태그 이름은 YYMMDDvN 형식만 본다. 접미사가 붙은 태그(260915v1-ph, 260930v8-gl 등)는 뺀다.
날짜(YYMMDD)가 큰 것, 같은 날이면 N 이 큰 것이 마지막 태그다.

  python3 tools/docs/latest_tag.py                     기기별 마지막 태그를 JSON 으로 출력
  python3 tools/docs/latest_tag.py --compare <URL>     배포된 사이트의 _nav/latest.json 과 비교해
                                                       changed=true|false 를 출력 (GitHub Actions 출력용)
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TAG_RE = re.compile(r"^(\d{6})v(\d+)$")


def latest_tag(repo_url):
    out = subprocess.run(["git", "ls-remote", "--tags", "--refs", repo_url],
                         check=True, capture_output=True, text=True).stdout
    tags = [line.rsplit("/", 1)[-1] for line in out.splitlines()]
    tags = [t for t in tags if TAG_RE.match(t)]
    if not tags:
        raise SystemExit(f"{repo_url}: YYMMDDvN 형식 태그가 없습니다")
    return max(tags, key=lambda t: tuple(int(x) for x in TAG_RE.match(t).groups()))


def state(cfg):
    """{"<기기>": "<마지막 태그>"} — "track": "latest-tag" 버전이 있는 기기만."""
    out = {}
    for dev in cfg["devices"]:
        for v in dev["versions"]:
            if v.get("track") == "latest-tag":
                out[dev["id"]] = latest_tag(v.get("repo", dev["repo"]))
    return out


def load_cfg():
    with open(os.path.join(ROOT, "docs", "versions.json"), encoding="utf-8") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--compare", metavar="URL", help="배포된 _nav/latest.json 주소")
    args = ap.parse_args()

    cur = state(load_cfg())
    if not args.compare:
        print(json.dumps(cur, ensure_ascii=False, indent=2))
        return
    try:
        req = urllib.request.Request(args.compare, headers={"User-Agent": "openpibo-guide-docs"})
        with urllib.request.urlopen(req, timeout=30) as r:
            prev = json.load(r)
    except (urllib.error.URLError, ValueError) as e:  # 첫 배포이거나 사이트가 없으면 배포한다
        print(f"배포된 상태 없음: {e}", file=sys.stderr)
        prev = None
    for k, t in cur.items():
        print(f"{k}: {t} (배포본 {(prev or {}).get(k)})", file=sys.stderr)
    print(f"changed={'false' if cur == prev else 'true'}")


if __name__ == "__main__":
    main()
