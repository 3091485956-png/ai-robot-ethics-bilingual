# -*- coding: utf-8 -*-
"""Slice article.json into 4 balanced shard source files for parallel annotation."""
import json, re
from pathlib import Path

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
data = json.loads((ROOT / "article.json").read_text(encoding="utf-8"))
out_dir = ROOT / "content-source"
out_dir.mkdir(exist_ok=True)

SHARDS = {
    "a": ("Preamble + 1.1 + 1.2 + 2.1 + 2.2", lambda n: n == "" or n.startswith(("1.", "2.1", "2.2")) and not n.startswith(("2.10",))),
    "b": ("2.3 + 2.4 + 2.5 + 2.6", lambda n: n.startswith(("2.3", "2.4", "2.5", "2.6"))),
    "c": ("2.7 + 2.8", lambda n: n.startswith(("2.7", "2.8"))),
    "d": ("2.9 + 2.10 + 3", lambda n: n.startswith(("2.9", "2.10")) or n == "3"),
}

def shard_of(num):
    if num == "":
        return "a"
    if num.startswith(("1.", "2.1.", "2.2")) and not num.startswith("2.10"):
        return "a"
    if num in ("2.1", "2.2"):
        return "a"
    if num.startswith(("2.3", "2.4", "2.5", "2.6")):
        return "b"
    if num.startswith(("2.7", "2.8")):
        return "c"
    if num.startswith(("2.9", "2.10")) or num == "3":
        return "d"
    # h2 parents "1" and "2" themselves
    if num == "1" or num == "2":
        return "a"
    raise ValueError(num)

buckets = {k: [] for k in SHARDS}
cur = ""
# preamble first -> shard a
for b in data["preamble"]:
    buckets["a"].append(b)
for b in data["blocks"]:
    if b["kind"] == "heading":
        cur = b.get("num", "")
        k = shard_of(cur)
    else:
        k = shard_of(cur)
    buckets[k].append(b)

for k, items in buckets.items():
    pcount = sum(1 for b in items if b["kind"] in ("p", "quote"))
    hcount = sum(1 for b in items if b["kind"] == "heading")
    payload = {
        "shard": k,
        "scope": SHARDS[k][0],
        "meta": data["meta"],
        "blocks": items,
        "stats": {"paragraphs": pcount, "headings": hcount},
    }
    (out_dir / f"shard-{k}.source.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"shard {k}: {pcount} paragraphs, {hcount} headings -> shard-{k}.source.json")
