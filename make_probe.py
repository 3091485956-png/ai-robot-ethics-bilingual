# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
h = (ROOT / "_final-check.html").read_text(encoding="utf-8")
probe = """<script>
window.__errs=[];
window.addEventListener('error',function(e){window.__errs.push(String(e.message))});
window.addEventListener('unhandledrejection',function(e){window.__errs.push('P:'+String(e.reason))});
window.addEventListener('load',function(){setTimeout(function(){
  var ok={
    pblocks:document.querySelectorAll('.pblock').length,
    headings:document.querySelectorAll('#article .h2,#article .h3,#article .h4').length,
    bib:document.querySelectorAll('#bibList .bib-item').length,
    hotTerm:document.querySelectorAll('.term-hot').length,
    hotVocab:document.querySelectorAll('.vocab-hot').length,
    tocLinks:document.querySelectorAll('#tocTree a').length,
    zhParas:document.querySelectorAll('.p-zh').length
  };
  var d=document.createElement('div');d.id='probe';
  d.textContent='PROBE '+JSON.stringify(ok)+' ERRORS='+JSON.stringify(window.__errs);
  document.body.appendChild(d);
},1500);});
</script>
</head>"""
(ROOT / "_final-probe.html").write_text(h.replace("</head>", probe, 1), encoding="utf-8")
print("ok")
