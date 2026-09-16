# -*- coding: utf-8 -*-
"""Generate truncated, layer-expanded temp builds ONLY for screenshot QA."""
import json
from pathlib import Path
ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
tpl = (ROOT/"web"/"index.html").read_text(encoding="utf-8")
d = json.loads((ROOT/"content"/"content.json").read_text(encoding="utf-8"))

# 截取：导言 + 前 46 个正文块（覆盖到 2.5 护理机器人附近）
d2 = dict(d)
d2["blocks"] = d["blocks"][:46]
d2["bibliography"] = d["bibliography"][:14]

shot_css = """
<style id="shot-override">
.reveal{opacity:1!important;transform:none!important}
.hero h1 .bt,.hero-title-zh,.hero-sub,.hero-meta,.hero-cta,.colophon{opacity:1!important;animation:none!important;filter:none!important;transform:none!important}
.dock-wrap{grid-template-rows:1fr!important}
.dock-btn[aria-expanded="false"]{color:#fff!important;border-color:transparent!important}
.dock-btn[data-k="logic"]{background:var(--c-logic)!important}
.dock-btn[data-k="term"]{background:var(--c-term)!important}
.dock-btn[data-k="background"]{background:var(--c-bg)!important}
.dock-btn[data-k="vocab"]{background:var(--c-vocab)!important}
.dock-btn .n{color:rgba(255,255,255,.85)!important}
.p-meta{opacity:1!important}
html{scroll-behavior:auto!important}
</style>
</head>"""
tpl2 = tpl.replace("</head>", shot_css, 1).replace("<body>", '<body data-view="bi" data-highlight="on">', 1)
tpl2 = tpl2.replace("/*__DATA__*/null", json.dumps(d2, ensure_ascii=False), 1)
(ROOT/"web"/"_shot_full.html").write_text(tpl2, encoding="utf-8")

# 仅封面（真实完整数据，用于首屏截图）
tpl3 = tpl.replace("</head>", shot_css, 1)
tpl3 = tpl3.replace("/*__DATA__*/null", json.dumps(d, ensure_ascii=False), 1)
(ROOT/"web"/"_shot_hero.html").write_text(tpl3, encoding="utf-8")

# 深色首屏：强制深色，阻止内联初始化脚本读 localStorage 覆盖
tpl4 = tpl.replace("</head>", shot_css, 1)
tpl4 = tpl4.replace("localStorage.getItem('eai.theme')", "'dark'")
tpl4 = tpl4.replace('data-theme="light"', 'data-theme="dark"', 1)
tpl4 = tpl4.replace("/*__DATA__*/null", json.dumps(d, ensure_ascii=False), 1)
(ROOT/"web"/"_shot_dark.html").write_text(tpl4, encoding="utf-8")

# 引文段 p072 截断页：从最近的上级标题开始，保留到引文段后一块
blocks = d["blocks"]
qi = next(i for i, b in enumerate(blocks) if b.get("pid") == "p072")
start = qi
while start > 0 and blocks[start].get("kind") != "heading":
    start -= 1
dq = dict(d)
dq["blocks"] = blocks[start:qi+2]
dq["preamble"] = []
dq["bibliography"] = []
quote_css = """
<style id="shot-override">
.hero{display:none!important}
.bib-chapter{display:none!important}
.article > .chapter{display:none!important}
.pblock:not(#p072){display:none!important}
.reader{padding-top:calc(var(--topbar-h) + 24px)}
.reveal{opacity:1!important;transform:none!important}
.p-meta{opacity:1!important}
html{scroll-behavior:auto!important}
</style>
</head>"""
tplq = tpl.replace("</head>", quote_css, 1)
tplq = tplq.replace("/*__DATA__*/null", json.dumps(dq, ensure_ascii=False), 1)
(ROOT/"web"/"_shot_quote.html").write_text(tplq, encoding="utf-8")

# 文献置顶页：隐藏封面与正文，仅显示文献章
bib_css = """
<style id="shot-override">
.hero{display:none!important}
.article > *:not(.bib-chapter){display:none!important}
.bib-chapter{padding-top:calc(var(--topbar-h) + 28px)}
.reveal{opacity:1!important;transform:none!important}
html{scroll-behavior:auto!important}
</style>
</head>"""
tplb = tpl.replace("</head>", bib_css, 1)
tplb = tplb.replace("/*__DATA__*/null", json.dumps(d, ensure_ascii=False), 1)
(ROOT/"web"/"_shot_bib.html").write_text(tplb, encoding="utf-8")

# 浮层静态页：加载后自动点击首个 term-hot，并把浮层钉在首屏可见位置
pop_css = """
<style id="shot-override">
.reveal{opacity:1!important;transform:none!important}
.hero h1 .bt,.hero-title-zh,.hero-sub,.hero-meta,.hero-cta,.colophon{opacity:1!important;animation:none!important;filter:none!important;transform:none!important}
#pop{position:fixed!important;left:50%!important;top:600px!important;transform:translateX(-50%)!important;right:auto!important;bottom:auto!important;opacity:1!important;visibility:visible!important;pointer-events:auto!important}
html{scroll-behavior:auto!important}
</style>
</head>"""
pop_js = """<script>window.addEventListener('load',function(){setTimeout(function(){var h=document.querySelector('.term-hot');if(h)h.click();},400);});</script>
</body>"""
tplp = tpl.replace("</head>", pop_css, 1).replace("</body>", pop_js, 1)
tplp = tplp.replace("/*__DATA__*/null", json.dumps(d, ensure_ascii=False), 1)
(ROOT/"web"/"_shot_pop.html").write_text(tplp, encoding="utf-8")
print("ok")
