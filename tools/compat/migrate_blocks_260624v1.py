#!/usr/bin/env python3
"""
구 IDE(openpibo-os 2024, openpibo.vision 시절) 블록 JSON 을 260624v1 IDE 블록으로 옮긴다.

규칙 (260624v1 customblock.js / customblock_callback.js 와 구 openpibo-os 생성기를 대조해 정함):
  vision_imshow_to_ide_img(img)          -> vision_imshow_to_ide(img)            같은 코드 생성
  vision_face(img)                       -> vision_face_detect(img)
  device_eye_off()                       -> device_eye_on(0,0,0,0,0,0)
  device_eye_fade(left,right,time)       -> device_eye_colour_on(left,right)     서서히 켜기(time)는 없어짐
  vision_face_age(img,v)                 -> utils_dict_get(vision_face_analyze(img,v), 'age')
  vision_face_gender(img,v)              -> utils_dict_get(vision_face_analyze(img,v), 'gender')
  vision_classification(img)             -> vision_object(img)                   이름 리스트 반환은 같음
  vision_analyze_pose 입력 val           -> v
  device_hat_button(num=BCM)             -> device_pibrain_button(num=SW번호)    BCM4/17/27 -> 1/2/3
  vision_flip(img, flags)                -> img 그대로                            좌우반전 블록 없음
  얼굴 박스 (x,y,w,h) -> (x1,y1,x2,y2):  얼굴 박스 변수의 3·4번째 값을 (x2-x1), (y2-y1) 로 바꿔 기존 w/h 계산을 유지
  결과 딕셔너리 {"data", "img"} 를 돌려주던 블록 (vision_marker_detect, vision_pose, vision_face_landmark):
    X = 블록(img=이미지) 뒤에 *_vis(이미지, X) 를 넣고, get(X,'data') -> X, get(X,'img') -> 이미지
  vision_face_landmark(img)              -> vision_face_landmark(img, 첫 번째 얼굴 박스)   얼굴이 없으면 실행 중 에러

바꾸지 않는 것: vision_load_tm / vision_predict_tm (260624v1 에 대응 블록 없음. 파일 목록만 출력)

사용: python3 tools/compat/migrate_blocks_260624v1.py <json 파일 또는 폴더>...
"""
import json
import os
import random
import string
import sys

HAT_TO_SW = {"4": "1", "17": "2", "27": "3"}
UNSUPPORTED = {"vision_load_tm", "vision_predict_tm"}
_ID_CHARS = string.ascii_letters + string.digits + "!#$%()*+,-./:;=?@[]^_`{|}~"


def new_id():
    return "".join(random.choice(_ID_CHARS) for _ in range(20))


def num(n):
    return {"shadow": {"type": "math_number", "id": new_id(), "fields": {"NUM": n}}}


def text(s):
    return {"shadow": {"type": "text", "id": new_id(), "fields": {"TEXT": s}}}


def inp(b, name):
    """입력 슬롯에 연결된 블록 (block 이 없으면 shadow)"""
    slot = (b.get("inputs") or {}).get(name) or {}
    return slot.get("block") or slot.get("shadow") or {}


def children(b):
    for v in (b.get("inputs") or {}).values():
        for k in ("block", "shadow"):
            if isinstance(v.get(k), dict):
                yield v, k
    if b.get("next") and isinstance(b["next"].get("block"), dict):
        yield b["next"], "block"


def all_blocks(b):
    stack = [b]
    while stack:
        x = stack.pop()
        yield x
        stack += [slot[k] for slot, k in children(x)]


def face_box_vars(roots):
    """vision_face(_detect) 결과 리스트 변수, 그 원소(얼굴 박스) 변수의 id 집합"""
    lists, boxes = set(), set()
    blocks = [x for r in roots for x in all_blocks(r)]
    for x in blocks:
        if x.get("type") == "variables_set":
            v = inp(x, "VALUE")
            if v.get("type") in ("vision_face", "vision_face_detect"):
                lists.add(x["fields"]["VAR"]["id"])
    for x in blocks:
        if x.get("type") == "variables_set":
            v = inp(x, "VALUE")
            if v.get("type") == "lists_getIndex":
                src = inp(v, "VALUE")
                if src.get("type") == "variables_get" and src["fields"]["VAR"]["id"] in lists:
                    boxes.add(x["fields"]["VAR"]["id"])
    return boxes


def get_index_at(b):
    at = (b.get("inputs") or {}).get("AT", {})
    blk = at.get("block") or at.get("shadow") or {}
    return str(blk.get("fields", {}).get("NUM")) if blk.get("type") == "math_number" else None


def minus(a, b):
    return {"type": "math_arithmetic", "id": new_id(), "fields": {"OP": "MINUS"},
            "inputs": {"A": {"shadow": num(1)["shadow"], "block": a},
                       "B": {"shadow": num(1)["shadow"], "block": b}}}


def box_index(var_field, at):
    return {"type": "lists_getIndex", "id": new_id(),
            "extraState": {"isStatement": False},
            "fields": {"MODE": "GET", "WHERE": "FROM_START"},
            "inputs": {"VALUE": {"block": {"type": "variables_get", "id": new_id(), "fields": {"VAR": dict(var_field)}}},
                       "AT": num(at)}}


def already_fixed(b, boxes):
    """(box[3] - box[1]) / (box[4] - box[2]) 형태로 이미 바뀐 블록인지"""
    if b.get("type") != "math_arithmetic" or b.get("fields", {}).get("OP") != "MINUS":
        return None
    ins = b.get("inputs") or {}
    a, c = inp(b, "A"), inp(b, "B")
    if a.get("type") == c.get("type") == "lists_getIndex":
        va = inp(a, "VALUE")
        vc = inp(c, "VALUE")
        if (va.get("type") == vc.get("type") == "variables_get" and va["fields"]["VAR"]["id"] in boxes
                and va["fields"]["VAR"]["id"] == vc["fields"]["VAR"]["id"]
                and (get_index_at(a), get_index_at(c)) in (("3", "1"), ("4", "2"))):
            return a.get("id")
    return None


def convert(b, boxes, notes, skip=frozenset()):
    """블록 b 를 바꾼 결과를 돌려준다 (다른 블록으로 대체될 수 있음)."""
    fixed = already_fixed(b, boxes)
    if fixed:
        skip = skip | {fixed}
    for slot, k in list(children(b)):
        slot[k] = convert(slot[k], boxes, notes, skip)

    t = b.get("type")
    ins = b.get("inputs") or {}

    if t == "vision_imshow_to_ide_img":
        b["type"] = "vision_imshow_to_ide"
    elif t == "vision_face":
        b["type"] = "vision_face_detect"
    elif t == "vision_classification":
        b["type"] = "vision_object"
    elif t == "device_eye_off":
        b["type"] = "device_eye_on"
        b["inputs"] = {f"val{i}": num(0) for i in range(6)}
    elif t == "device_eye_fade":
        b["type"] = "device_eye_colour_on"
        b["inputs"] = {k: v for k, v in ins.items() if k in ("left", "right")}
        notes.add("device_eye_fade -> device_eye_colour_on (서서히 켜기 시간 없어짐)")
    elif t in ("vision_face_age", "vision_face_gender"):
        key = "age" if t.endswith("age") else "gender"
        analyze = {"type": "vision_face_analyze", "id": new_id(),
                   "inputs": {k: v for k, v in ins.items() if k in ("img", "v")}}
        b = {"type": "utils_dict_get", "id": b.get("id", new_id()),
             "inputs": {"dictionary": {"block": analyze}, "keyname": text(key)}}
    elif t == "vision_analyze_pose" and "val" in ins:
        ins["v"] = ins.pop("val")
    elif t == "device_hat_button":
        b["type"] = "device_pibrain_button"
        bcm = str(b.get("fields", {}).get("num"))
        if bcm not in HAT_TO_SW:
            raise ValueError(f"device_hat_button num={bcm}: 대응 SW 없음")
        b["fields"]["num"] = HAT_TO_SW[bcm]
    elif t == "vision_flip":
        img = ins.get("img", {})
        inner = img.get("block") or img.get("shadow")
        notes.add("vision_flip 제거 (260624v1 에 좌우반전 블록 없음, 원본 이미지 사용)")
        if inner:
            return inner
    elif t == "lists_getIndex":
        src = inp(b, "VALUE")
        at = get_index_at(b)
        if (src.get("type") == "variables_get" and src["fields"]["VAR"]["id"] in boxes and at in ("3", "4")
                and b.get("id") not in skip):
            base = "1" if at == "3" else "2"
            notes.add("얼굴 박스 3·4번째 값 -> (x2-x1), (y2-y1)")
            b = minus(b, box_index(src["fields"]["VAR"], base))
    return b


RESULT_VIS = {"vision_marker_detect": "vision_marker_detect_vis",
              "vision_pose": "vision_pose_vis",
              "vision_face_landmark": "vision_face_landmark_vis"}


def var_get(var_field):
    return {"type": "variables_get", "id": new_id(), "fields": {"VAR": dict(var_field)}}


def clone(b):
    c = json.loads(json.dumps(b))
    for x in all_blocks(c):
        x["id"] = new_id()
    return c


def dict_get_target(b):
    """utils_dict_get(variables_get X, 'key') 이면 (X id, key)"""
    if b.get("type") != "utils_dict_get":
        return None
    ins = b.get("inputs") or {}
    d = inp(b, "dictionary")
    k = inp(b, "keyname")
    if d.get("type") == "variables_get" and k.get("type") == "text":
        return d["fields"]["VAR"]["id"], k["fields"]["TEXT"]
    return None


def fix_results(roots, notes):
    """결과 딕셔너리({'data','img'})를 쓰던 블록을 260624v1 방식으로 바꾼다."""
    blocks = [x for r in roots for x in all_blocks(r)]
    producers = {}  # var id -> (variables_set 블록, 생산 블록)
    for x in blocks:
        if x.get("type") == "variables_set":
            v = inp(x, "VALUE")
            if v.get("type") in RESULT_VIS:
                producers[x["fields"]["VAR"]["id"]] = (x, v)
    if not producers:
        return roots

    for x in blocks:
        if x.get("type") == "vision_face_landmark" and "v" not in (x.get("inputs") or {}):
            img = inp(x, "img")
            if img:
                detect = {"type": "vision_face_detect", "id": new_id(), "inputs": {"img": {"block": clone(img)}}}
                x["inputs"]["v"] = {"block": {"type": "lists_getIndex", "id": new_id(),
                                              "extraState": {"isStatement": False},
                                              "fields": {"MODE": "GET", "WHERE": "FIRST"},
                                              "inputs": {"VALUE": {"block": detect}}}}
                notes.add("vision_face_landmark 에 첫 번째 얼굴 박스 입력 추가 (얼굴 없으면 에러)")

    used_img = set()

    def repl(b):
        for slot, k in list(children(b)):
            slot[k] = repl(slot[k])
        t = dict_get_target(b)
        if t and t[0] in producers:
            vid, key = t
            vset, prod = producers[vid]
            if key == "data":
                notes.add("결과 get(.., 'data') -> 결과 리스트 그대로")
                return var_get(vset["fields"]["VAR"])
            if key == "img":
                img = inp(prod, "img")
                if img and img.get("type") == "variables_get":
                    used_img.add(vid)
                    notes.add("결과 get(.., 'img') -> *_vis 로 그린 원본 이미지")
                    return clone(img)
                notes.add(f"확인 필요: {prod['type']} 의 'img' 를 대체할 이미지 변수가 없음")
        return b

    roots = [repl(r) for r in roots]
    for vid in used_img:
        vset, prod = producers[vid]
        img = inp(prod, "img")
        vis = {"type": RESULT_VIS[prod["type"]], "id": new_id(),
               "inputs": {"img": {"block": clone(img)}, "v": {"block": var_get(vset["fields"]["VAR"])}}}
        if vset.get("next"):
            vis["next"] = vset["next"]
        vset["next"] = {"block": vis}
    return roots


def migrate(path):
    data = json.load(open(path, encoding="utf-8"))
    if not (isinstance(data, dict) and isinstance(data.get("blocks"), dict)):
        return None
    roots = data["blocks"].get("blocks", [])
    types = {x.get("type") for r in roots for x in all_blocks(r)}
    unsupported = sorted(types & UNSUPPORTED)
    boxes = face_box_vars(roots)
    notes = set()
    before = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    roots = [convert(r, boxes, notes) for r in roots]
    data["blocks"]["blocks"] = fix_results(roots, notes)
    after = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if after != before:
        open(path, "w", encoding="utf-8").write(after)
    return after != before, sorted(notes), unsupported


def main():
    random.seed(260624)
    files = []
    for a in sys.argv[1:]:
        if os.path.isdir(a):
            files += [os.path.join(r, f) for r, _, fs in os.walk(a) for f in fs if f.endswith(".json")]
        else:
            files.append(a)
    for p in sorted(files):
        res = migrate(p)
        if not res:
            continue
        changed, notes, unsupported = res
        if changed or unsupported:
            msg = "변경" if changed else "그대로"
            extra = "; ".join(notes + ([f"미지원 블록 남음: {', '.join(unsupported)}"] if unsupported else []))
            print(f"{msg}: {p}" + (f"  ({extra})" if extra else ""))


if __name__ == "__main__":
    main()
