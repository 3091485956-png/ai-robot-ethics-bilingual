# -*- coding: utf-8 -*-
"""Playwright QA screenshots (accurate viewports, bypasses headless min-width)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
OUT = Path(r"C:\TempEai")
WEB = ROOT / "web"

def url(name):
    return (WEB / name).resolve().as_uri()

jobs = [
    # (output, file, width, height, prepare_fn_name)
    ("08-hero-mobile.png", "_shot_hero.html", 390, 844, "hero"),
    ("09-bib-mobile.png", "_shot_bib.html", 390, 844, "bibtop"),
    ("10-mobile-layers.png", "_shot_hero.html", 390, 844, "layers"),
    ("11-mobile-panel.png", "_shot_hero.html", 390, 844, "panel"),
]

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--disable-gpu"])
    for name, f, w, h, mode in jobs:
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        pg.goto(url(f), wait_until="networkidle")
        pg.wait_for_timeout(1400)
        if mode == "bibtop":
            pg.locator("#bib").scroll_into_view_if_needed()
            pg.wait_for_timeout(600)
        elif mode == "layers":
            pg.locator('.ml-btn[data-layer="logic"]').click()
            pg.wait_for_timeout(500)
        elif mode == "panel":
            # 展开 p001 的名词面板并滚动到该段
            pg.locator('#p001 .dock-btn[data-k="term"]').click()
            pg.wait_for_timeout(400)
            pg.locator("#p001").scroll_into_view_if_needed()
            pg.wait_for_timeout(500)
        pg.screenshot(path=str(OUT / name))
        print("OK", name)
        pg.close()
    b.close()
print("done")
