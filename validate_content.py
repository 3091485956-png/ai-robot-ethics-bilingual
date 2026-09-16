# -*- coding: utf-8 -*-
"""Validate content/shard-*.json against article.json ground truth.
Usage: python validate_content.py [--merge]
With --merge, also merge valid shards into content/content.json (assembly input).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
ground = json.loads((ROOT / "article.json").read_text(encoding="utf-8"))

def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()

# ground-truth ordered list of blocks (preamble + body)
truth = []
for b in ground["preamble"]:
    truth.append(("p", b["pid"]))
for b in ground["blocks"]:
    if b["kind"] == "heading":
        truth.append(("h", b["id"] or "sec-" + b.get("num","").replace(".","-")))
    else:
        truth.append((b["kind"], b["pid"]))

truth_map = {}
for b in ground["preamble"]:
    truth_map[b["pid"]] = b
for b in ground["blocks"]:
    key = b["pid"] if b["kind"] in ("p", "quote") else b["id"]
    truth_map[key] = b

errors, warnings = [], []
merged = []
seen = set()

for shard in "abcd":
    fp = ROOT / "content" / f"shard-{shard}.json"
    if not fp.exists():
        errors.append(f"[shard {shard}] missing file {fp}")
        continue
    try:
        d = json.loads(fp.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"[shard {shard}] invalid JSON: {e}")
        continue
    src_fp = ROOT / "content-source" / f"shard-{shard}.source.json"
    src = json.loads(src_fp.read_text(encoding="utf-8"))
    src_blocks = src["blocks"]
    out_blocks = d.get("blocks", [])
    if len(src_blocks) != len(out_blocks):
        errors.append(f"[shard {shard}] block count {len(out_blocks)} != source {len(src_blocks)}")
    for i, (s, o) in enumerate(zip(src_blocks, out_blocks)):
        if s["kind"] != o.get("kind"):
            errors.append(f"[shard {shard}] block {i} kind mismatch")
            continue
        if s["kind"] == "heading":
            key = s["id"]
            if s.get("num") and not s["id"]:
                key = "sec-" + s["num"].replace(".", "-")
            tz = (o.get("title_zh") or "").strip()
            if not tz:
                errors.append(f"[shard {shard}] heading {s.get('num')} missing title_zh")
            if key in seen:
                errors.append(f"[shard {shard}] duplicate heading {key}")
            seen.add(key)
        else:
            pid = s["pid"]
            if o.get("pid") != pid:
                errors.append(f"[shard {shard}] block {i} pid mismatch: {o.get('pid')} != {pid}")
            if pid in seen:
                errors.append(f"[shard {shard}] duplicate pid {pid}")
            seen.add(pid)
            zh = (o.get("zh") or "").strip()
            if not zh:
                errors.append(f"[{pid}] missing zh")
            else:
                en_words = len(norm(s["text_en"]).split())
                zh_chars = len(re.sub(r"\s", "", zh))
                if zh_chars < max(20, en_words * 0.9):
                    warnings.append(f"[{pid}] zh suspiciously short: {zh_chars} chars vs {en_words} en words")
                # check every english sentence has some coverage: flag if zh has no CJK at all
                if not re.search(r"[一-鿿]", zh):
                    errors.append(f"[{pid}] zh contains no Chinese characters")
            logic = o.get("logic", [])
            if not (2 <= len(logic) <= 5):
                warnings.append(f"[{pid}] logic count = {len(logic)} (expect 2-4)")
            elif not all(isinstance(x, str) and len(x) > 8 for x in logic):
                errors.append(f"[{pid}] malformed logic items")
            terms = o.get("terms", [])
            for t in terms:
                if not all(t.get(k) for k in ("en", "zh", "def")):
                    errors.append(f"[{pid}] term missing fields: {t.get('en')}")
            bg = o.get("background", [])
            for t in bg:
                if not all(t.get(k) for k in ("title", "body")):
                    errors.append(f"[{pid}] background missing fields: {t.get('title')}")
            vocab = o.get("vocab", [])
            if len(vocab) < 2:
                warnings.append(f"[{pid}] vocab count = {len(vocab)} (expect 4-8)")
            en_norm = norm(s["text_en"])
            for v in vocab:
                if not all(v.get(k) for k in ("en", "pos", "zh", "ex")):
                    errors.append(f"[{pid}] vocab missing fields: {v.get('en')}")
                    continue
                ex = norm(v["ex"])
                # verbatim check: every word of ex (stripped of punctuation) must appear in order
                ex_words = re.findall(r"[A-Za-z][A-Za-z\-’']*", ex)
                en_words_list = re.findall(r"[A-Za-z][A-Za-z\-’']*", en_norm)
                # subsequence match
                j = 0
                for w in en_words_list:
                    if j < len(ex_words) and w.strip(".,;:’'\"()–-").lower() == ex_words[j].strip(".,;:’'\"()–-").lower():
                        j += 1
                if j < len(ex_words):
                    errors.append(f"[{pid}] vocab ex not verbatim from paragraph: '{v['en']}' -> '{ex[:60]}'")
        merged.append(o)

# coverage of all truth blocks
missing = [k for kind, k in truth if k not in seen]
if missing:
    errors.append(f"missing {len(missing)} blocks from output, e.g. {missing[:8]}")

print(f"truth blocks: {len(truth)} | covered: {len(seen)}")
if warnings:
    print(f"\nWARNINGS ({len(warnings)}):")
    for w in warnings[:60]:
        print("  ~", w)
if errors:
    print(f"\nERRORS ({len(errors)}):")
    for e in errors[:80]:
        print("  X", e)
    sys.exit(1)

if "--merge" in sys.argv:
    # order merged output by ground-truth order
    order = {k: i for i, (kind, k) in enumerate(truth)}
    def keyfn(o):
        if o["kind"] == "heading":
            k = o.get("id") or ("sec-" + o.get("num","").replace(".","-"))
        else:
            k = o["pid"]
        return order[k]
    merged.sort(key=keyfn)
    out = {"meta": ground["meta"], "toc": ground["toc"],
           "preamble": [o for o in merged if o.get("pid") in {b["pid"] for b in ground["preamble"]}],
           "blocks": [o for o in merged if not (o.get("pid") in {b["pid"] for b in ground["preamble"]})],
           "bibliography": ground["bibliography"]}
    (ROOT / "content" / "content.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\nmerged -> content/content.json with", len(merged), "blocks +",
          len(out["bibliography"]), "bibliography entries")
print("\nVALIDATION PASSED")
