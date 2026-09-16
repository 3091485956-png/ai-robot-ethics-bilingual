# -*- coding: utf-8 -*-
"""Functional smoke test on the FINAL deliverable."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(r"C:\Users\loong\Desktop\人工智能与机器人伦理学")
FINAL = ROOT / "人工智能与机器人伦理学·中英精读.html"
OUT = Path(r"C:\TempEai")

errors = []
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--disable-gpu"])
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errors.append("PAGEERROR: " + str(e)))
    pg.goto(FINAL.resolve().as_uri(), wait_until="networkidle")
    pg.wait_for_timeout(1800)

    n_pblock = pg.locator(".pblock").count()
    n_bib = pg.locator("#bibList li").count()
    n_toc = pg.locator(".toc-tree a").count()
    print("pblocks:", n_pblock, "| bib:", n_bib, "| toc links:", n_toc)

    # 视图切换
    pg.locator('[data-view-btn="en"]').click(); pg.wait_for_timeout(300)
    print("view en ->", pg.locator("body").get_attribute("data-view"))
    pg.locator('[data-view-btn="zh"]').click(); pg.wait_for_timeout(300)
    print("view zh ->", pg.locator("body").get_attribute("data-view"))
    pg.locator('[data-view-btn="bi"]').click(); pg.wait_for_timeout(300)

    # 全局标注层
    pg.locator('.icon-btn[data-layer="logic"]').click(); pg.wait_for_timeout(400)
    print("logic open wraps:", pg.locator(".dock-wrap.open").count())
    pg.locator('.icon-btn[data-layer="vocab"]').click(); pg.wait_for_timeout(400)
    print("highlight:", pg.locator("body").get_attribute("data-highlight"))
    pg.locator('.icon-btn[data-layer="logic"]').click()
    pg.locator('.icon-btn[data-layer="vocab"]').click()

    # 浮层
    pg.locator(".term-hot").first.click(); pg.wait_for_timeout(400)
    print("popover shown:", pg.locator("#pop.show").count())
    pg.screenshot(path=str(OUT / "12-final-pop.png"))
    pg.keyboard.press("Escape")

    # 文献检索
    pg.locator("#bibSearch").fill("Bostrom"); pg.wait_for_timeout(500)
    print("bib count text:", pg.locator("#bibCount").inner_text())
    pg.locator("#bibSearch").fill(""); pg.wait_for_timeout(300)

    # 深色
    pg.locator("#themeBtn").click(); pg.wait_for_timeout(500)
    print("theme:", pg.locator("html").get_attribute("data-theme"))
    pg.locator("#bib").scroll_into_view_if_needed()
    pg.wait_for_timeout(400)
    pg.screenshot(path=str(OUT / "13-final-dark-bib.png"))

    # 移动端
    pg2 = b.new_page(viewport={"width": 390, "height": 844})
    errs2 = []
    pg2.on("console", lambda m: errs2.append(m.text) if m.type == "error" else None)
    pg2.goto(FINAL.resolve().as_uri(), wait_until="networkidle")
    pg2.wait_for_timeout(1500)
    docw = pg2.evaluate("document.documentElement.scrollWidth")
    winw = pg2.evaluate("window.innerWidth")
    print("mobile docW/winW:", docw, winw, "overflow:", docw > winw)
    pg2.locator("#menuBtn").click(); pg2.wait_for_timeout(500)
    print("drawer open:", pg2.locator("#tocDrawer.show").count())
    pg2.screenshot(path=str(OUT / "14-final-drawer.png"))
    pg2.keyboard.press("Escape"); pg2.wait_for_timeout(300)
    b.close()

print("desktop console errors:", errors)
print("mobile console errors:", errs2)
print("SMOKE DONE")
