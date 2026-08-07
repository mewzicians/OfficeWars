import os
import sys
from pathlib import Path


temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


URL = (Path(__file__).resolve().parent / ".officewars-smoke.html").as_uri()
DONE = """() =>
  document.title.startsWith('PASS:') ||
  document.title.startsWith('FAIL:') ||
  document.title.startsWith('ERROR:') ||
  document.title === 'NOT_READY'
"""


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        args=[
            "--allow-file-access-from-files",
            "--disable-extensions",
            "--no-first-run",
        ],
    )
    try:
        page = browser.new_page()
        page.on("pageerror", lambda error: print("PAGE_ERROR:", error))
        page.goto(URL, wait_until="load", timeout=30_000)
        try:
            page.wait_for_function(DONE, timeout=120_000)
        except PlaywrightTimeoutError:
            frame = page.frame(name="game")
            stage = frame.evaluate("window.__smokeStage || 'base'") if frame else "no-frame"
            difference = (
                frame.evaluate("window.__playbackDifference || ''") if frame else ""
            )
            print(f"TIMEOUT:{stage}:{page.title()}:{difference}")
            raise
        else:
            title = page.title()
            print(title)
            if not title.startswith("PASS:"):
                raise SystemExit(1)
    finally:
        browser.close()
