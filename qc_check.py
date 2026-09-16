# -*- coding: utf-8 -*-
"""Organizer QC on merged content/content.json:
1) cross-shard glossary consistency of terms entries
2) suspicious substitute renderings in zh text
3) random sample dump for manual eyeball
"""
import json, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = r"C:\Users\loong\Desktop\人工智能与机器人伦理学"
d = json.load(open(ROOT + r"\content\content.json", encoding="utf-8"))

# glossary en-key -> required zh substring (must appear in terms.zh)
GLOSS = {
    "moral status": "道德地位",
    "existential risk": "存在性风险",
    "superintelligence": "超级智能",
    "singularity": "奇点",
    "intelligence explosion": "智能爆炸",
    "value alignment": "价值对齐",
    "responsibility gap": "责任缺口",
    "black box": "黑箱",
    "explainability": "可解释",
    "nudging": "助推",
    "surveillance capitalism": "监控资本主义",
    "machine ethics": "机器伦理",
    "artificial moral agent": "人工道德能动者",
    "algorithm": None,
}
# 'agency' handled separately (two allowed renderings)
AGENCY_OK = ("能动作用", "能动性")

print("== terms-entry glossary check ==")
issues = 0
for b in d["blocks"] + d["preamble"]:
    for t in b.get("terms", []):
        en = (t.get("en") or "").lower()
        zh = t.get("zh") or ""
        for key, want in GLOSS.items():
            if want is None:
                continue
            if key in en and want not in zh:
                print(f"  X [{b.get('pid', b.get('id'))}] term '{t['en']}' -> zh '{zh}' (should contain '{want}')")
                issues += 1
        if "agency" in en:
            if not any(w in zh for w in AGENCY_OK):
                print(f"  X [{b.get('pid', b.get('id'))}] term '{t['en']}' -> zh '{zh}' (should be 能动作用/能动性)")
                issues += 1
print(f"terms issues: {issues}")

print("\n== suspicious substitute renderings in zh text ==")
suspects = {
    "道德身份": "moral status 应为'道德地位'；personhood 才是'人格'",
    "存在风险": "existential risk 应为'存在性风险'，此处疑似漏'性'",
    "代理": "agency 语境应为'能动者/能动性'，'代理'可疑",
    "人工智能伦理": "词条定名应为'人工智能与机器人伦理学'",
}
for pat, why in suspects.items():
    hits = [b.get("pid", b.get("id")) for b in d["blocks"] + d["preamble"] if pat in (b.get("zh") or "")]
    if hits:
        print(f"  ~ '{pat}' hits in {len(hits)} blocks: {hits[:12]}  -> {why}")
    else:
        print(f"  ok  '{pat}' 0 hits")

print("\n== per-shard sample blocks for eyeball ==")
# shard boundaries by pid ranges: a=p001-p029(+preamble), b=p030-p057, c=p058-p087, d=p088-p116
def shard_of(pid):
    n = int(re.sub(r"\D", "", pid))
    if n <= 29: return "a"
    if n <= 57: return "b"
    if n <= 87: return "c"
    return "d"

ps = [b for b in d["blocks"] + d["preamble"] if b["kind"] in ("p", "quote")]
by_shard = {"a": [], "b": [], "c": [], "d": []}
for b in ps:
    by_shard[shard_of(b["pid"])].append(b)

for s in "abcd":
    arr = by_shard[s]
    picks = [arr[len(arr)//4], arr[len(arr)//2], arr[3*len(arr)//4]]
    for b in picks:
        en = re.sub(r"\s+", " ", b["text_en"]).strip()
        print(f"\n----- shard {s} | {b['pid']} | en_words={len(en.split())} zh_chars={len(re.sub(r"\s","",b["zh"]))} logic={len(b.get('logic',[]))} terms={len(b.get('terms',[]))} vocab={len(b.get('vocab',[]))}")
        print("EN:", en[:500])
        print("ZH:", (b["zh"])[:600])
