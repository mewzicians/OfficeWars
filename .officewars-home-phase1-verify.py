#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / ".officewars-python"))

from playwright.sync_api import sync_playwright


GAME_URL = (ROOT / "officewarsautobattler.html").as_uri()
checks: list[tuple[str, bool, object]] = []


def check(name: str, condition: bool, evidence: object) -> None:
    checks.append((name, bool(condition), evidence))


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(GAME_URL, wait_until="load")
    page.wait_for_function(
        "document.documentElement.dataset.officewarsReady === 'true'",
        timeout=20_000,
    )
    page.evaluate(
        """() => {
          const meta={
            schema:6,
            tutorial:{completed:true,nextStep:0,skipped:false,replayRequested:false},
            guidedIntern:{
              required:true,completed:true,replayRequested:false,version:1
            },
            settings:{volume:70}
          };
          localStorage.setItem('officewars.meta.v1',JSON.stringify(meta));
          startRun({seed:991001});
        }"""
    )
    page.wait_for_timeout(100)
    state = page.evaluate("OfficeWarsTest.homePhase1State()")

    check("schema-9", state["schema"] == 9, state["schema"])
    check(
        "seven-homes",
        [(item["id"], item["slots"], item["recovery"]) for item in state["levels"]]
        == [
            ("apartment", 3, 0),
            ("condo", 5, 1),
            ("townhouse", 7, 2),
            ("duplex", 9, 3),
            ("house", 11, 4),
            ("estate", 13, 5),
            ("penthouse", 15, 6),
        ],
        state["levels"],
    )
    rarity_counts: dict[str, int] = {}
    for item in state["items"]:
        rarity_counts[item["rarity"]] = rarity_counts.get(item["rarity"], 0) + 1
    check(
        "item-inventory",
        len(state["items"]) == 29
        and rarity_counts == {
            "common": 11,
            "uncommon": 7,
            "rare": 6,
            "legendary": 5,
        },
        {"total": len(state["items"]), "rarities": rarity_counts},
    )
    cash_jar = next(item for item in state["items"] if item["id"] == "cashJar")
    check(
        "cash-jar-gated",
        cash_jar["gated"] and cash_jar["nonSellable"],
        cash_jar,
    )
    check("nine-sets", len(state["sets"]) == 9, state["sets"])
    check("new-run-home-state", state["home"]["levelId"] == "apartment", state["home"])
    check("initial-capacity", state["capacity"] == 3, state["capacity"])

    acquired = page.evaluate(
        """() => {
          OfficeWarsTest.acquireHomeItem('standingDesk');
          OfficeWarsTest.acquireHomeItem('ergonomicChair');
          OfficeWarsTest.acquireHomeItem('secondMonitor');
          return OfficeWarsTest.homePhase1State();
        }"""
    )
    check(
        "capacity-filled",
        acquired["activeItems"]
        == ["standingDesk", "ergonomicChair", "secondMonitor"],
        acquired["activeItems"],
    )
    held = page.evaluate(
        """() => {
          return OfficeWarsTest.acquireHomeItem('cloudWorkstation',{held:true});
        }"""
    )
    check("holding-slot", held and held["status"] == "held", held)
    profile = page.evaluate("OfficeWarsTest.homeSetProfile()")
    workspace = next(item for item in profile if item["id"] == "workspace")
    check("workspace-incomplete", workspace["count"] == 3 and not workspace["complete"], workspace)

    page.evaluate(
        """() => {
          R.phase='night';
          R.cash=1000;
          owHomePrepareNight();
          nightState={
            tab:'home',homePanel:'overview',bought:new Set(),purchasedDealIds:new Set(),
            recPicked:false,outingUsed:false,homeUsed:0,homeBlockingPurchases:0,
            dealUsed:0,homeLimit:1,dealLimit:0,extraPurchaseCredits:0,
            panelOpen:true,panelMode:'planner',startCash:R.cash,startCredit:0
          };
          R.nightCards=genNightCards();
          renderNightUI();
        }"""
    )
    overview_text = page.locator("#overlay-panel").inner_text()
    check(
        "home-overview-ui",
        "OVERVIEW" in overview_text
        and "SHOP" in overview_text
        and "INVENTORY & SETS" in overview_text,
        overview_text[:500],
    )
    page.evaluate(
        """() => {
          nightState.homePanel='shop';
          R.nightCards=[
            {offerId:'verify-coffee',upgrade:owHomeDefinition('coffeeMaker'),purchased:false},
            {offerId:'verify-mattress',upgrade:owHomeDefinition('comfyMattress'),purchased:false},
            {offerId:'verify-snacks',upgrade:owHomeDefinition('emergencySnacks'),purchased:false}
          ];
          renderNightUI();
        }"""
    )
    keyword = page.locator(".night-home-card-grid .ow-keyword").first
    keyword_info = {
        "text": keyword.inner_text(),
        "tabindex": keyword.get_attribute("tabindex"),
        "tip": keyword.get_attribute("data-tip"),
    }
    keyword.focus()
    page.wait_for_function(
        "document.getElementById('global-tip').style.display === 'block'"
    )
    focus_tip = page.locator("#global-tip").inner_text()
    page.keyboard.press("Escape")
    escape_hidden = not page.locator("#global-tip").is_visible()
    keyword.dispatch_event(
        "pointerdown",
        {"pointerType": "touch", "bubbles": True, "cancelable": True},
    )
    touch_visible = page.locator("#global-tip").is_visible()
    check(
        "home-keyword-tooltip",
        keyword_info["tabindex"] == "0"
        and bool(keyword_info["tip"])
        and bool(focus_tip)
        and escape_hidden
        and touch_visible,
        {
            "keyword": keyword_info,
            "focusTip": focus_tip,
            "escapeHidden": escape_hidden,
            "touchVisible": touch_visible,
        },
    )
    buffs = page.evaluate("OfficeWarsTest.openBuffs()")
    check(
        "active-buffs-page",
        all(label in buffs for label in ["ACTIVE BUFFS", "TODAY", "NEXT WORKDAY", "HOME & SETS", "ECONOMY"]),
        buffs[:800],
    )
    page.evaluate("document.documentElement.style.fontSize='200%'")
    buff_layout = page.evaluate(
        """() => {
          const modal=document.getElementById('resume-book');
          const dialog=modal.querySelector('.hud-modal-dialog');
          const content=document.getElementById('resume-book-content');
          const rect=dialog.getBoundingClientRect();
          return{
            open:modal.classList.contains('open'),
            categories:document.querySelectorAll('.active-buff-group').length,
            dialogOverflow:Math.max(0,dialog.scrollWidth-dialog.clientWidth),
            contentOverflow:Math.max(0,content.scrollWidth-content.clientWidth),
            withinViewport:
              rect.left>=0&&rect.top>=0&&rect.right<=innerWidth+1&&rect.bottom<=innerHeight+1
          };
        }"""
    )
    check(
        "active-buffs-200-percent",
        buff_layout["open"]
        and buff_layout["categories"] == 5
        and buff_layout["dialogOverflow"] == 0
        and buff_layout["contentOverflow"] == 0
        and buff_layout["withinViewport"],
        buff_layout,
    )
    check("no-page-errors", not errors, errors)
    browser.close()

passed = sum(1 for _, ok, _ in checks if ok)
failed = len(checks) - passed
for name, ok, evidence in checks:
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        print(json.dumps(evidence, ensure_ascii=False, default=str, indent=2))
print(f"SUMMARY passed={passed} failed={failed}")
raise SystemExit(1 if failed else 0)
