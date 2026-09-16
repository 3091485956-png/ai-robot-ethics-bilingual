# -*- coding: utf-8 -*-
"""Build final standalone HTML by merging article.json (English truth) and
content/shard-*.json (Chinese annotations) into web/index.html.

Usage:
  python build.py            # production build (requires all shards)
  python build.py --dev      # dev build with placeholder translations
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEV = "--dev" in sys.argv

ground = json.loads((ROOT / "article.json").read_text(encoding="utf-8"))

# ---- collect annotations ----
ann = {}
for shard in "abcd":
    fp = ROOT / "content" / f"shard-{shard}.json"
    if fp.exists():
        d = json.loads(fp.read_text(encoding="utf-8"))
        for b in d.get("blocks", []):
            if b["kind"] == "heading":
                key = b.get("id") or ("sec-" + b.get("num", "").replace(".", "-"))
            else:
                key = b["pid"]
            ann[key] = b
    elif not DEV:
        print(f"MISSING {fp}"); sys.exit(1)

FIELDS = ["zh", "logic", "terms", "background", "vocab"]
def dev_block(b):
    if b["kind"] in ("p", "quote"):
        b["zh"] = "【开发预览占位译文】该段中文译文、逻辑拆解、名词解释、背景知识与词汇标注正在并行生产中，正式版将逐句完整呈现。"
        b["logic"] = ["开发预览：逻辑拆解条目示例。", "开发预览：第二条论证动作示例。"]
        b["terms"] = [{"en": "example term", "zh": "示例术语", "def": "开发预览占位：术语解释将在正式版中给出。"}]
        b["background"] = [{"title": "示例人物（Example Person）", "body": "开发预览占位：背景知识将在正式版中给出。"}]
        b["vocab"] = [{"en": "substantial", "pos": "adj.", "zh": "实质性的；重大的", "ex": "substantial impact on the world"}]
    else:
        b["title_zh"] = "开发预览标题"
    return b

def merge(src):
    out = []
    for b in src:
        if b["kind"] == "heading":
            key = b.get("id") or ("sec-" + b.get("num", "").replace(".", "-"))
            a = ann.get(key)
            nb = dict(b)
            nb["title_zh"] = (a or {}).get("title_zh", "")
            if not nb["title_zh"] and DEV: nb = dev_block(nb)
            out.append(nb)
        else:
            nb = dict(b)
            a = ann.get(b["pid"])
            if a:
                for f in FIELDS:
                    nb[f] = a.get(f)
            elif DEV:
                nb = dev_block(nb)
            out.append(nb)
    return out

merged_blocks = merge(ground["blocks"])
heading_zh = {b.get("id"): b.get("title_zh", "") for b in merged_blocks if b["kind"] == "heading"}
toc = []
for t in ground["toc"]:
    tt = dict(t)
    tt["title_zh"] = heading_zh.get(t.get("id"), "")
    toc.append(tt)

payload = {
    "meta": ground["meta"],
    "toc": toc,
    "preamble": merge(ground["preamble"]),
    "blocks": merged_blocks,
    "bibliography": ground["bibliography"],
}

# coverage report
missing = [b["pid"] for b in payload["preamble"] + payload["blocks"]
           if b["kind"] in ("p", "quote") and not b.get("zh")]
miss_h = [b.get("num") for b in payload["blocks"] if b["kind"] == "heading" and not b.get("title_zh")]
print(f"paragraphs missing zh: {len(missing)} {missing[:5]}")
print(f"headings missing title_zh: {len(miss_h)} {miss_h[:5]}")

tpl = (ROOT / "web" / "index.html").read_text(encoding="utf-8")
marker = "/*__DATA__*/null"
assert marker in tpl, "template marker not found"
data_js = json.dumps(payload, ensure_ascii=False)
html_out = tpl.replace(marker, data_js, 1)

name = "AI伦理论文精读_dev预览.html" if DEV else "人工智能与机器人伦理学·中英精读.html"
out_fp = ROOT / name
out_fp.write_text(html_out, encoding="utf-8")
print(f"built: {out_fp.name}  ({out_fp.stat().st_size/1024:.0f} KB)")

# GitHub Pages 发布副本（main 分支 /docs 目录）
if not DEV:
    docs_fp = ROOT / "docs" / "index.html"
    docs_fp.parent.mkdir(exist_ok=True)
    docs_fp.write_text(html_out, encoding="utf-8")
    print(f"pages copy: docs/index.html  ({docs_fp.stat().st_size/1024:.0f} KB)")
