# -*- coding: utf-8 -*-
"""Parse SEP article HTML into structured JSON."""
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path

HTML_PATH = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学\ethics-ai-raw.html")
html = HTML_PATH.read_text(encoding="utf-8", errors="replace")

# Locate main content
m = re.search(r'<div id="au-content">(.*?)<div id="bibliography">', html, re.S)
# SEP structure may differ; inspect markers first
markers = ["au-content", "bibliography", "academic-tools", "toc", "article-copyright", "other-internet-resources", "related-entries"]
for mk in markers:
    print(mk, [x.start() for x in re.finditer(f'id="{mk}"', html)][:5])
print("total len", len(html))
