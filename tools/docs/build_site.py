#!/usr/bin/env python3
"""
openpibo-os.<기기> 태그 안에 커밋된 Sphinx 빌드 결과(docs/build/html)를 모아
기기·버전별 문서 사이트를 만든다. 버전 목록은 docs/versions.json.

  <out>/index.html                      기기·버전 목록 (첫 화면)
  <out>/<기기>/<태그>/...                 해당 태그의 docs/build/html
  <out>/_nav/                           모든 문서 페이지 상단의 버전 바 (JS/CSS)
  <out>/_nav/kit/                       Pibo UI Kit (openpibo-os.pibo design/, versions.json 의 ui)

문서 원본은 각 OS 저장소 태그가 기준이다. 버전에 "repo" 가 있으면 그 저장소의 태그를 쓴다
(예: Pibo 구버전 v0.9.2.73 은 openpibo-python). 디자인은 OS 웹 화면(v2)과 같은 Pibo UI Kit 을 쓴다.
이 스크립트는 복사와 버전 바 삽입만 한다.

사용:
  python3 tools/docs/build_site.py --out _site
  python3 tools/docs/build_site.py --out _site --cache /path/to/clones   # 로컬 클론 재사용
    (--cache 아래 openpibo-os.pibo, openpibo-os.pibrain 처럼 저장소 이름의 클론이 있으면 git archive 로 꺼낸다)
"""
import argparse
import html
import io
import json
import os
import shutil
import subprocess
import tarfile
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC_DIR = os.path.join(ROOT, "docs")
DOCS_PATH = "docs/build/html"
STATUS_LABEL = {"released": "배포", "testing": "테스트 중", "legacy": "구버전"}


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def fetch_docs(repo_url, tag, dest, cache, path=DOCS_PATH):
    """태그(또는 브랜치)의 path 를 dest 로 꺼낸다."""
    name = repo_url.rstrip("/").split("/")[-1]
    local = os.path.join(cache, name) if cache else None
    if local and os.path.isdir(os.path.join(local, ".git")):
        # 브랜치는 원격 쪽(origin/<이름>)을, 태그는 태그를 쓴다
        has = lambda r: subprocess.run(["git", "-C", local, "rev-parse", "-q", "--verify", r],
                                       capture_output=True).returncode == 0
        ref = f"origin/{tag}" if has(f"origin/{tag}") else tag
        data = run(["git", "-C", local, "archive", "--format=tar", ref, path], capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(data)) as tf:
            tmp = tempfile.mkdtemp()
            tf.extractall(tmp)
            shutil.copytree(os.path.join(tmp, path), dest)
            shutil.rmtree(tmp)
        return
    tmp = tempfile.mkdtemp()
    try:
        run(["git", "-c", "advice.detachedHead=false", "clone", "--quiet", "--depth", "1", "--branch", tag,
             "--filter=blob:none", "--sparse", repo_url, tmp])
        run(["git", "-C", tmp, "sparse-checkout", "set", path])
        shutil.copytree(os.path.join(tmp, path), dest)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def inject_nav(site_root, version_dir, device, tag):
    """버전 디렉터리의 모든 html 에 버전 바를 넣는다."""
    for base, _, files in os.walk(version_dir):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(base, fn)
            rel_root = os.path.relpath(site_root, base).replace(os.sep, "/") + "/"
            page = os.path.relpath(path, version_dir).replace(os.sep, "/")
            with open(path, encoding="utf-8") as f:
                s = f.read()
            if "_nav/version-bar.js" in s:
                continue
            head = f'<link rel="stylesheet" href="{rel_root}_nav/version-bar.css">\n'
            body = (f'<script src="{rel_root}_nav/versions.js"></script>\n'
                    f'<script src="{rel_root}_nav/version-bar.js" data-root="{rel_root}" '
                    f'data-device="{device}" data-tag="{tag}" data-page="{html.escape(page)}"></script>\n')
            s = s.replace("</head>", head + "</head>", 1) if "</head>" in s else head + s
            s = s.replace("</body>", body + "</body>", 1) if "</body>" in s else s + body
            with open(path, "w", encoding="utf-8") as f:
                f.write(s)


def add_example_links(cfg):
    """이 저장소에 <기기>/<태그>/ 예제 폴더가 있는 버전에 GitHub 폴더 주소를 넣는다."""
    ex = cfg.get("examples") or {}
    base = ex.get("repo", "").rstrip("/")
    for dev in cfg["devices"]:
        for v in dev["versions"]:
            if base and os.path.isdir(os.path.join(ROOT, dev["id"], v["tag"])):
                v["examples"] = f'{base}/tree/{ex.get("branch", "main")}/{dev["id"]}/{v["tag"]}'


def render_index(cfg):
    """첫 화면: 기기별 버전 목록 (정적 HTML)."""
    cards = []
    for dev in cfg["devices"]:
        rows = []
        latest = next((v["tag"] for v in dev["versions"] if v["status"] == "released"), None)
        for v in dev["versions"]:
            badges = f'<span class="pb-badge {v["status"]}">{STATUS_LABEL.get(v["status"], v["status"])}</span>'
            if v["tag"] == latest:
                badges = '<span class="pb-badge latest">최신</span>' + badges
            links = f'<a class="pb-btn pb-btn--sm" href="{dev["id"]}/{v["tag"]}/index.html">문서</a>'
            if v.get("examples"):
                links += (f'<a class="pb-btn pb-btn--sm" href="{html.escape(v["examples"])}" '
                          f'target="_blank" rel="noopener">예제</a>')
            rows.append(
                f'<li><a class="ver" href="{dev["id"]}/{v["tag"]}/index.html">'
                f'<span class="tag">{html.escape(v["tag"])}</span>'
                f'<span class="badges">{badges}</span></a>'
                f'<span class="links">{links}</span></li>')
        cards.append(f'<section class="card"><h2>{html.escape(dev["name"])}</h2><ul>{"".join(rows)}</ul></section>')
    with open(os.path.join(SRC_DIR, "site", "index.html"), encoding="utf-8") as f:
        tpl = f.read()
    return tpl.replace("<!--DEVICES-->", "\n".join(cards))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--cache", help="OS 저장소 클론이 있는 폴더 (없으면 GitHub 에서 받음)")
    args = ap.parse_args()

    with open(os.path.join(SRC_DIR, "versions.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    add_example_links(cfg)
    out = os.path.abspath(args.out)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)

    for dev in cfg["devices"]:
        for v in dev["versions"]:
            dest = os.path.join(out, dev["id"], v["tag"])
            repo = v.get("repo", dev["repo"])
            print(f"{dev['id']} {v['tag']} <- {repo}")
            fetch_docs(repo, v["tag"], dest, args.cache)
            inject_nav(out, dest, dev["id"], v["tag"])

    nav = os.path.join(out, "_nav")
    os.makedirs(nav)
    ui = cfg["ui"]
    print(f"ui kit {ui['ref']} <- {ui['repo']}")
    kit = os.path.join(nav, "kit")
    fetch_docs(ui["repo"], ui["ref"], kit, args.cache, path=ui["path"])
    # 사이트에 필요한 것만 남긴다: pibo-ui.css, fonts/ (글꼴 라이선스 포함)
    for fn in os.listdir(kit):
        if fn not in ("pibo-ui.css", "fonts"):
            p = os.path.join(kit, fn)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    for fn in ("version-bar.js", "version-bar.css"):
        shutil.copy(os.path.join(SRC_DIR, "site", fn), nav)
    with open(os.path.join(nav, "versions.js"), "w", encoding="utf-8") as f:
        f.write("window.DOCS_VERSIONS = " + json.dumps(cfg, ensure_ascii=False) + ";\n")
    # 파비콘: OS 웹·문서와 같은 파이보 아이콘(문서 _static/icon.png)을 첫 화면에도 쓴다
    for dev in cfg["devices"]:
        icon = os.path.join(out, dev["id"], dev["versions"][0]["tag"], "_static", "icon.png")
        if os.path.isfile(icon):
            shutil.copy(icon, os.path.join(out, "favicon.png"))
            break
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index(cfg))
    open(os.path.join(out, ".nojekyll"), "w").close()  # _static, _sources 폴더가 무시되지 않게
    print(f"done: {out}")


if __name__ == "__main__":
    main()
