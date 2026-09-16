# -*- coding: utf-8 -*-
import json, random, re
from pathlib import Path
ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
d = json.loads((ROOT/"content"/"content.json").read_text(encoding="utf-8"))
blocks = d["preamble"] + d["blocks"]
paras = [b for b in blocks if b.get("kind") in ("p","quote")]
random.seed(7)
sample = random.sample(paras, 4)
for b in sample:
    print("="*100)
    print("PID", b["pid"])
    print("EN:", b["text_en"][:600])
    print("-"*60)
    print("ZH:", b.get("zh","")[:700])
    print("LOGIC:", *b.get("logic",[]), sep="\n  - ")
    print("TERMS:", [(t.get("en"),t.get("zh")) for t in b.get("terms",[])])
    print("BG:", [t.get("title") for t in b.get("background",[])])
    print("VOCAB:", [(v.get("en"),v.get("zh")) for v in b.get("vocab",[])])
    # ex verbatim check
    for v in b.get("vocab",[]):
        ex = re.sub(r"\s+"," ",v.get("ex","")).strip()
        en = re.sub(r"\s+"," ",b["text_en"]).strip()
        if ex not in en:
            # word-level check
            print("  !! EX NOT EXACT:", ex[:80])
    print()
# heading translations
print("#"*100)
for b in blocks:
    if b.get("kind")=="heading":
        print(b.get("num"), "|", b.get("title_en"), "=>", b.get("title_zh"))
