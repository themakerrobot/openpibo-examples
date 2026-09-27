#!/usr/bin/env python3
"""
예제가 특정 openpibo-os 배포본(예: 260624v1)의 openpibo 라이브러리·IDE 블록과 맞는지 정적으로 검사한다.

기기 없이 확인할 수 있는 것만 본다.
  - python: openpibo 모듈/클래스/함수 import, 생성자·메서드 존재 여부, 위치 인자 개수
  - block : 블록 타입 정의 여부, 파이썬 생성기 유무, 필드 이름, 고정 드롭다운 값, 입력 이름, 빈 입력
실행 결과(카메라·서보·음성 동작)는 실기기에서 따로 확인해야 한다.

사용:
  git clone --branch 260624v1 https://github.com/themakerrobot/openpibo-os.pibo /tmp/os-pibo
  python3 tools/compat/check_compat.py --os /tmp/os-pibo --examples pibo/260624v1 \
      --report pibo/260624v1/COMPAT.md
"""
import argparse
import ast
import json
import os
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- library index
class Sig:
    def __init__(self, fn, drop_self):
        a = fn.args
        pos = [x.arg for x in a.posonlyargs + a.args]
        if drop_self and pos:
            pos = pos[1:]
        self.min = len(pos) - len(a.defaults)
        self.max = None if a.vararg else len(pos)
        self.names = set(pos) | {x.arg for x in a.kwonlyargs}
        self.varkw = a.kwarg is not None

    def check(self, call):
        n = len(call.args)
        if any(isinstance(x, ast.Starred) for x in call.args) or any(k.arg is None for k in call.keywords):
            return None
        kw = {k.arg for k in call.keywords}
        bad = [k for k in kw if k not in self.names] if not self.varkw else []
        if bad:
            return f"알 수 없는 키워드 인자 {bad}"
        if self.max is not None and n > self.max:
            return f"위치 인자 {n}개 (최대 {self.max})"
        if n + len(kw) < self.min:
            return f"인자 {n + len(kw)}개 (최소 {self.min})"
        return None


def index_library(pkg_dir):
    """{module: {"classes": {name: {method: Sig}}, "funcs": {name: Sig}, "names": set}}"""
    lib = {}
    for fn in sorted(os.listdir(pkg_dir)):
        if not fn.endswith(".py"):
            continue
        mod = fn[:-3]
        tree = ast.parse(open(os.path.join(pkg_dir, fn), encoding="utf-8").read())
        classes, funcs, names, bases = {}, {}, set(), {}
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                meths = {}
                for b in node.body:
                    if isinstance(b, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        static = any(isinstance(d, ast.Name) and d.id == "staticmethod" for d in b.decorator_list)
                        meths[b.name] = Sig(b, drop_self=not static)
                classes[node.name] = meths
                bases[node.name] = [b.id for b in node.bases if isinstance(b, ast.Name)]
                names.add(node.name)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                funcs[node.name] = Sig(node, drop_self=False)
                names.add(node.name)
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                for t in (node.targets if isinstance(node, ast.Assign) else [node.target]):
                    if isinstance(t, ast.Name):
                        names.add(t.id)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                for a in node.names:
                    names.add((a.asname or a.name).split(".")[0])
        # 같은 모듈 안 상속만 펼친다 (외부 기반 클래스는 메서드 검사 생략)
        opaque = set()
        for c in classes:
            seen, stack = set(), list(bases[c])
            while stack:
                b = stack.pop()
                if b in seen:
                    continue
                seen.add(b)
                if b in classes:
                    for m, s in classes[b].items():
                        classes[c].setdefault(m, s)
                    stack += bases[b]
                elif b != "object":
                    opaque.add(c)
        lib[mod] = {"classes": classes, "funcs": funcs, "names": names, "opaque": opaque}
    return lib


# ---------------------------------------------------------------- python check
def check_python(path, lib):
    issues = []
    try:
        tree = ast.parse(open(path, encoding="utf-8").read())
    except SyntaxError as e:
        return [f"L{e.lineno}: 문법 오류 (Python 3) — {e.msg}"]

    imported = {}   # local name -> (module, name)
    modalias = {}   # local name -> module
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and node.module.split(".")[0] == "openpibo":
            parts = node.module.split(".")
            if len(parts) == 1:
                for a in node.names:
                    if a.name in lib:
                        modalias[a.asname or a.name] = a.name
                    elif a.name not in lib.get("__init__", {}).get("names", set()):
                        issues.append(f"L{node.lineno}: `openpibo.{a.name}` 없음")
                continue
            mod = parts[1]
            if mod not in lib:
                for a in node.names:
                    # 이름이 다른 모듈로 옮겨졌으면 그 위치를 알려주고, 메서드 검사는 계속한다
                    moved = [m for m in lib if a.name in lib[m]["classes"] or a.name in lib[m]["funcs"]]
                    hint = f" → `from openpibo.{moved[0]} import {a.name}`" if moved else ""
                    issues.append(f"L{node.lineno}: 모듈 `openpibo.{mod}` 없음{hint}")
                    if moved:
                        imported[a.asname or a.name] = (moved[0], a.name)
                continue
            for a in node.names:
                if a.name == "*":
                    continue
                if a.name not in lib[mod]["names"]:
                    issues.append(f"L{node.lineno}: `openpibo.{mod}` 에 `{a.name}` 없음")
                else:
                    imported[a.asname or a.name] = (mod, a.name)
        elif isinstance(node, ast.Import):
            for a in node.names:
                p = a.name.split(".")
                if p[0] == "openpibo" and len(p) > 1:
                    if p[1] not in lib:
                        issues.append(f"L{node.lineno}: 모듈 `{a.name}` 없음")
                    elif a.asname:
                        modalias[a.asname] = p[1]

    # 인스턴스 추적: x = Cls(...) / self.x = Cls(...)
    inst = {}

    def target_key(t):
        if isinstance(t, ast.Name):
            return t.id
        if isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name):
            return f"{t.value.id}.{t.attr}"
        return None

    def cls_of_call(call):
        f = call.func
        if isinstance(f, ast.Name) and f.id in imported:
            return imported[f.id]
        if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id in modalias:
            return (modalias[f.value.id], f.attr)
        return None

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            c = cls_of_call(node.value)
            if c and c[1] in lib[c[0]]["classes"]:
                for t in node.targets:
                    k = target_key(t)
                    if k:
                        inst[k] = c

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        c = cls_of_call(node)
        if c:
            mod, name = c
            if name in lib[mod]["classes"]:
                init = lib[mod]["classes"][name].get("__init__")
                if init and (err := init.check(node)):
                    issues.append(f"L{node.lineno}: `{name}()` {err}")
            elif name in lib[mod]["funcs"]:
                if err := lib[mod]["funcs"][name].check(node):
                    issues.append(f"L{node.lineno}: `{name}()` {err}")
            elif isinstance(f, ast.Attribute) and name not in lib[mod]["names"]:
                issues.append(f"L{node.lineno}: `openpibo.{mod}` 에 `{name}` 없음")
            continue
        if isinstance(f, ast.Attribute):
            k = target_key(f.value)
            if k in inst:
                mod, cls = inst[k]
                meths = lib[mod]["classes"][cls]
                if f.attr not in meths:
                    if cls not in lib[mod]["opaque"]:
                        issues.append(f"L{node.lineno}: `{cls}.{f.attr}()` 메서드 없음")
                elif err := meths[f.attr].check(node):
                    issues.append(f"L{node.lineno}: `{cls}.{f.attr}()` {err}")
    return sorted(set(issues), key=lambda s: int(s[1:].split(":")[0]) if s[1:].split(":")[0].isdigit() else 0)


# ---------------------------------------------------------------- block check
def walk_blocks(b, out):
    if not isinstance(b, dict):
        return
    out.append(b)
    for v in (b.get("inputs") or {}).values():
        walk_blocks(v.get("block"), out)
        walk_blocks(v.get("shadow"), out)
    if b.get("next"):
        walk_blocks(b["next"].get("block"), out)


def check_block(path, defs):
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return None, [f"JSON 파싱 실패 — {e}"]
    if not (isinstance(data, dict) and isinstance(data.get("blocks"), dict)):
        return None, None  # 블록 파일 아님 (모션 DB 등)
    blocks = []
    for b in data["blocks"].get("blocks", []):
        walk_blocks(b, blocks)
    issues = defaultdict(int)
    for b in blocks:
        t = b.get("type")
        d = defs.get(t)
        if d is None:
            issues[f"블록 `{t}` 정의 없음"] += 1
            continue
        if d.get("core"):
            continue
        if not d.get("generator"):
            issues[f"블록 `{t}` 파이썬 생성기 없음"] += 1
        for fname, val in (b.get("fields") or {}).items():
            if fname not in d["fields"]:
                issues[f"블록 `{t}` 필드 `{fname}` 없음"] += 1
            elif d["fields"][fname] is not None and val not in d["fields"][fname]:
                issues[f"블록 `{t}` 필드 `{fname}` 값 `{val}` 허용 목록에 없음"] += 1
        for iname in (b.get("inputs") or {}):
            if iname not in d["inputs"]:
                issues[f"블록 `{t}` 입력 `{iname}` 없음"] += 1
        # 비어 있는 입력은 생성기에서 None 이 되어 실행 중 에러가 난다
        for iname in d["inputs"]:
            slot = (b.get("inputs") or {}).get(iname) or {}
            if not (slot.get("block") or slot.get("shadow")):
                issues[f"블록 `{t}` 입력 `{iname}` 비어 있음"] += 1
    return len(blocks), [f"{k}" + (f" ×{n}" if n > 1 else "") for k, n in sorted(issues.items())]


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--os", required=True, help="openpibo-os.<기기> 체크아웃 경로 (배포 태그)")
    ap.add_argument("--examples", required=True, help="검사할 예제 폴더 (예: pibo/260624v1)")
    ap.add_argument("--report", help="마크다운 보고서 출력 경로")
    args = ap.parse_args()

    lib = index_library(os.path.join(args.os, "openpibo"))
    defs = json.loads(subprocess.check_output(
        ["node", os.path.join(HERE, "extract_blocks.js"), os.path.join(args.os, "ide", "static")]))
    ver = next((l.split("=")[1].strip().strip("'\"") for l in open(os.path.join(args.os, "openpibo", "__init__.py"))
                if l.startswith("__version__")), "?")
    tag = subprocess.run(["git", "-C", args.os, "describe", "--tags", "--exact-match"],
                         capture_output=True, text=True).stdout.strip() or "?"

    rows = []
    for root, _, files in os.walk(args.examples):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, args.examples)
            if fn.endswith(".py"):
                iss = check_python(p, lib)
                rows.append((rel, "python", "FAIL" if iss else "OK", iss))
            elif fn.endswith(".json"):
                n, iss = check_block(p, defs)
                if iss is None:
                    continue
                rows.append((rel, "block", "FAIL" if iss else "OK", iss))
    rows.sort()

    ok = sum(r[2] == "OK" for r in rows)
    lines = [
        f"# 호환성 검사 — `{args.examples}`",
        "",
        f"- 기준: openpibo-os 태그 `{tag}`, openpibo `{ver}`",
        f"- 방법: 정적 검사 (`tools/compat/check_compat.py`). **실기기 동작 확인은 별도.**",
        f"- 결과: {len(rows)}개 중 OK {ok} / FAIL {len(rows) - ok}",
        "",
        "| 파일 | 종류 | 결과 | 문제 |",
        "|---|---|---|---|",
    ]
    for rel, kind, st, iss in rows:
        detail = "<br>".join(i.replace("|", "\\|") for i in iss[:8]) + (f"<br>… 외 {len(iss) - 8}건" if len(iss) > 8 else "")
        lines.append(f"| `{rel}` | {kind} | {st} | {detail} |")
    text = "\n".join(lines) + "\n"
    if args.report:
        open(args.report, "w", encoding="utf-8").write(text)
    print(f"{args.examples}: {len(rows)} files, OK {ok}, FAIL {len(rows) - ok}", file=sys.stderr)
    if not args.report:
        print(text)


if __name__ == "__main__":
    main()
