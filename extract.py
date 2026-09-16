# -*- coding: utf-8 -*-
"""Full extraction of SEP ethics-ai entry into article.json (verbatim)."""
import json, re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
html = (ROOT / "ethics-ai-raw.html").read_text(encoding="utf-8", errors="replace")

class Inline(HTMLParser):
    """Keep em/strong/i/b/a markup; absolutize SEP links; drop everything else."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.href_stack = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("em", "strong", "i", "b"):
            t = {"i": "em", "b": "strong"}.get(tag, tag)
            self.out.append(f"<{t}>")
        elif tag == "a":
            href = a.get("href", "")
            if href:
                if href.startswith("../"):
                    href = "https://plato.stanford.edu/archives/sum2026/entries/" + href[3:]
                elif href.startswith("/"):
                    href = "https://plato.stanford.edu" + href
            self.href_stack.append(href)
            self.out.append(f'<a href="{href}" data-ext="{1 if href.startswith("http") else 0}">')
        elif tag == "br":
            self.out.append(" ")
    def handle_endtag(self, tag):
        if tag in ("em", "strong", "i", "b"):
            t = {"i": "em", "b": "strong"}.get(tag, tag)
            self.out.append(f"</{t}>")
        elif tag == "a":
            self.out.append("</a>")
            if self.href_stack: self.href_stack.pop()
    def handle_data(self, d):
        self.out.append(d)

def inline(raw):
    p = Inline()
    p.feed(raw)
    s = "".join(p.out)
    s = s.replace("\n", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\s+([,.;:?!\u2019\u201d])", r"\1", s)
    return s.strip()

def plain(raw_html):
    s = re.sub(r"<[^>]+>", "", raw_html)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

class BlockParser(HTMLParser):
    def __init__(self, region):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.cur = None
        self.depth_skip = 0
        self.feed(region)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.cur is not None:
            if tag in ("em","strong","i","b","a","br","span","sup","sub"):
                if tag == "br": self.cur["raw"].append(" ")
                elif tag in ("em","strong","i","b","a"):
                    if tag in ("i","b"): tag = {"i":"em","b":"strong"}[tag]
                    if tag == "a":
                        href = a.get("href","")
                        if href.startswith("../"):
                            href = "https://plato.stanford.edu/archives/sum2026/entries/" + href[3:]
                        self.cur["raw"].append(f'<{tag} href="{href}">')
                    else:
                        self.cur["raw"].append(f"<{tag}>")
            return
        if tag in ("h2","h3","h4"):
            self.cur = {"kind": "heading", "level": int(tag[1]), "id": a.get("id",""), "raw": []}
        elif tag == "p":
            self.cur = {"kind": "p", "raw": []}
        elif tag == "blockquote":
            self.cur = {"kind": "quote", "raw": []}
    def handle_endtag(self, tag):
        if self.cur is None: return
        if self.cur["kind"] == "heading" and tag in ("h2","h3","h4"):
            self._finish()
        elif self.cur["kind"] == "p" and tag == "p":
            self._finish()
        elif self.cur["kind"] == "quote" and tag == "blockquote":
            self._finish()
        elif tag in ("em","strong","a") and self.cur is not None:
            self.cur["raw"].append(f"</{tag}>")
    def handle_data(self, d):
        if self.cur is not None:
            self.cur["raw"].append(d)
    def _finish(self):
        raw = "".join(self.cur["raw"])
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", raw)).strip()
        if text:
            b = {"kind": self.cur["kind"], "text_en": text}
            if self.cur["kind"] == "heading":
                b["level"] = self.cur["level"]; b["id"] = self.cur["id"]
                mm = re.match(r"^(\d+(?:\.\d+){0,2})\.?\s+(.*)$", text)
                b["num"] = mm.group(1) if mm else ""
                b["title_en"] = mm.group(2) if mm else text
            else:
                b["html_en"] = inline(raw)
            self.blocks.append(b)
        self.cur = None

def region(start_marker, end_marker):
    s = html.find(start_marker); e = html.find(end_marker, s)
    return html[s:e]

pre = region('<div id="preamble">', '<div id="main-text">')
main = region('<div id="main-text">', 'id="bibliography"')
bp = BlockParser(pre)
pre_blocks = [b for b in bp.blocks if b["kind"] == "p"]
bm = BlockParser(main)
blocks = bm.blocks

# assign stable ids
pidx = 0
for b in pre_blocks:
    pidx += 1; b["pid"] = f"p{pidx:03d}"
for b in blocks:
    if b["kind"] in ("p", "quote"):
        pidx += 1; b["pid"] = f"p{pidx:03d}"
all_body = pre_blocks + blocks

# h4 ids from number
for b in blocks:
    if b["kind"] == "heading" and not b["id"] and b.get("num"):
        b["id"] = "sec-" + b["num"].replace(".", "-")

# bibliography entries
bib_region = region('<h2 id="Bib">', 'id="Aca"')
entries = re.findall(r"<li>(.*?)</li>", bib_region, re.S)
bib = [inline(e) for e in entries]
bib = [b for b in bib if b]

# TOC
toc = [{"num": b["num"], "title_en": b["title_en"], "id": b["id"], "level": b["level"]}
       for b in blocks if b["kind"] == "heading"]

data = {
    "meta": {
        "title_en": "Ethics of Artificial Intelligence and Robotics",
        "author": "Vincent C. Müller",
        "pubinfo": "First published Thu Apr 30, 2020; substantive revision Fri Mar 27, 2026",
        "archive": "Summer 2026",
        "source_url": "https://plato.stanford.edu/archives/sum2026/entries/ethics-ai/",
        "publisher": "Stanford Encyclopedia of Philosophy (SEP)"
    },
    "preamble": pre_blocks,
    "toc": toc,
    "blocks": blocks,
    "bibliography": bib,
}
(ROOT / "article.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

# stats + per-leaf-section paragraph counts
from collections import OrderedDict
cur = "preamble"; counts = OrderedDict([(cur, 0)]); titles = {cur: "Preamble"}
for b in pre_blocks:
    if b["kind"] in ("p","quote"): counts[cur] += 1
for b in blocks:
    if b["kind"] == "heading":
        if b["level"] in (2,3):
            cur = b["num"] + " " + b["title_en"]
            counts[cur] = 0; titles[cur] = b["title_en"]
    elif b["kind"] in ("p","quote"):
        counts[cur] += 1
print("total body paras:", pidx, "| bib entries:", len(bib), "| headings:", len(toc))
for k,v in counts.items():
    print(f"{v:3d}  {k[:70]}")
