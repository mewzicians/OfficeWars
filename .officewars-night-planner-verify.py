import json
import os
import sys
from pathlib import Path


temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
GAME_URL = (ROOT / "officewarsautobattler.html").as_uri()

# Interface captures are browsable reference material, so they land in the
# private vault section when that section exists and in a gitignored local
# folder otherwise. A public clone has no Wiki/ and takes the fallback. Names
# carry no leading dot, because Obsidian hides dotfiles and a hidden reference
# image cannot be browsed.
CAPTURES = ROOT / "Wiki/Projects/OfficeWars/Visual Reference"
if not CAPTURES.is_dir():
    CAPTURES = ROOT / "artifacts/visual-reference"
CAPTURES.mkdir(parents=True, exist_ok=True)
READY = "document.documentElement.dataset.officewarsReady === 'true'"
META_COMPLETE = json.dumps(
    {
        "schema": 6,
        "tutorial": {
            "completed": True,
            "nextStep": 0,
            "skipped": False,
            "replayRequested": False,
        },
        "guidedIntern": {
            "required": True,
            "completed": True,
            "replayRequested": False,
            "version": 1,
        },
        "settings": {"volume": 70},
    }
)


def load(page):
    page.goto(GAME_URL, wait_until="load", timeout=30_000)
    page.wait_for_function(READY, timeout=15_000)
    page.evaluate("localStorage.clear()")
    page.evaluate(
        "(meta) => localStorage.setItem(OW_META_KEY, meta)", META_COMPLETE
    )
    page.reload(wait_until="load", timeout=30_000)
    page.wait_for_function(READY, timeout=15_000)


def start_night(page, seed=87001):
    page.evaluate(
        """(seed) => {
          startRun({seed});
          R.today = {additionalNightPurchases:0,log:[]};
          R.stress = 38;
          R.cash = 750;
          R.expenseCredit = 100;
          R.nightViewPreference = 'planner';
          nightPhase({animate:false});
        }""",
        seed,
    )
    page.wait_for_selector(".night-planner-shell")


def planner_state(page):
    return page.evaluate(
        """() => {
          const panel = document.getElementById('overlay-panel');
          const shell = document.querySelector('.night-planner-shell');
          const screen = document.querySelector('.night-planner-screen');
          const rect = shell?.getBoundingClientRect();
          const tabsRect = document.querySelector(
            '.night-planner-tabs'
          )?.getBoundingClientRect();
          const footerRect = document.querySelector(
            '.night-footer'
          )?.getBoundingClientRect();
          const pickerRect = document.querySelector(
            '.night-home-desk .card-row,.night-deals-desk .card-row'
          )?.getBoundingClientRect();
          const homeGrid = document.querySelector('.night-home-card-grid');
          const homeCards = [...document.querySelectorAll(
            '.night-home-card-grid .card'
          )];
          const homeCardRects = homeCards.map(card => card.getBoundingClientRect());
          const homeCardSpan = homeCardRects.length
            ? Math.max(...homeCardRects.map(rect => rect.right)) -
              Math.min(...homeCardRects.map(rect => rect.left))
            : 0;
          const homeGridRect = homeGrid?.getBoundingClientRect();
          const homeActionsRect = document.querySelector(
            '.night-home-desk .night-purchase-actions'
          )?.getBoundingClientRect();
          const homeColumns = homeGrid
            ? getComputedStyle(homeGrid).gridTemplateColumns
                .split(' ').filter(Boolean).length
            : 0;
          const usableCenter = tabsRect && footerRect
            ? (tabsRect.bottom + footerRect.top) / 2
            : null;
          const usableHeight = tabsRect && footerRect
            ? Math.max(1, footerRect.top - tabsRect.bottom)
            : null;
          const pickerCenterDelta = pickerRect && usableCenter !== null
            ? Math.abs((pickerRect.top + pickerRect.bottom) / 2 - usableCenter)
            : null;
          return {
            phase:R.phase,
            panelOpen:nightState.panelOpen,
            panelMode:nightState.panelMode,
            tab:nightState.tab,
            overlay:document.getElementById('overlay').classList.contains('active'),
            panelClass:panel.classList.contains('night-planner-panel'),
            shell:!!shell,
            tabs:document.querySelectorAll('.night-planner-tab').length,
            dealTab:!!document.querySelector(
              '.night-planner-tab[data-night-tab="deals"]'
            ),
            pickerCentered:pickerCenterDelta !== null &&
              pickerCenterDelta <= Math.max(32, usableHeight * .3),
            pickerCenterDelta,
            usableHeight,
            homeLayout:homeGridRect ? {
              cards:homeCards.length,
              columns:homeColumns,
              fillRatio:homeGridRect.width
                ? homeCardSpan / homeGridRect.width
                : 0,
              overflow:Math.max(0,homeGrid.scrollWidth-homeGrid.clientWidth),
              minimumCardWidth:homeCardRects.length
                ? Math.min(...homeCardRects.map(rect => rect.width))
                : 0,
              visibleAboveFooter:footerRect
                ? homeCardRects.every(rect => rect.bottom <= footerRect.top + 1)
                : false,
              actionsVisible:footerRect && homeActionsRect
                ? homeActionsRect.bottom <= footerRect.top + 1
                : false
            } : null,
            pickerRect:pickerRect ? {
              top:pickerRect.top,
              bottom:pickerRect.bottom,
              height:pickerRect.height
            } : null,
            usableRect:tabsRect && footerRect ? {
              top:tabsRect.bottom,
              bottom:footerRect.top
            } : null,
            footer:!!document.querySelector('.night-footer'),
            hide:!!document.querySelector('.night-planner-hide'),
            finalize:!!document.querySelector('.night-finalize'),
            cash:document.querySelector('.night-cash')?.textContent,
            credit:document.querySelector('.night-credit')?.textContent,
            shellRect:rect ? {
              left:rect.left, top:rect.top, right:rect.right,
              bottom:rect.bottom, width:rect.width, height:rect.height
            } : null,
            screenScroll:screen ? {
              client:screen.clientHeight,
              scroll:screen.scrollHeight
            } : null,
            viewport:[innerWidth,innerHeight],
            bodyOverflow:[
              Math.max(0,document.body.scrollWidth-innerWidth),
              Math.max(0,document.body.scrollHeight-innerHeight)
            ]
          };
        }"""
    )


def main():
    failures = []
    evidence = {}

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
            for name, viewport in [
                ("desktop", {"width": 1440, "height": 900}),
                ("landscape", {"width": 844, "height": 390}),
            ]:
                context = browser.new_context(viewport=viewport)
                page = context.new_page()
                page_errors = []
                console_errors = []
                page.on("pageerror", lambda error: page_errors.append(str(error)))
                page.on(
                    "console",
                    lambda message: console_errors.append(message.text)
                    if message.type == "error"
                    else None,
                )
                load(page)
                start_night(page)

                overview = page.evaluate(
                    """() => ({
                      overview:!!document.querySelector('.home-overview-grid'),
                      subtabs:[...document.querySelectorAll('.home-subtab')]
                        .map(button => button.textContent.trim()),
                      active:document.querySelector('.home-subtab.active')
                        ?.textContent.trim()
                    })"""
                )
                if overview != {
                    "overview": True,
                    "subtabs": ["OVERVIEW", "SHOP", "INVENTORY & SETS"],
                    "active": "OVERVIEW",
                }:
                    failures.append(f"{name}:home-overview:{overview}")
                page.click(".home-subtab:has-text('SHOP')")
                planner = planner_state(page)
                rect = planner["shellRect"]
                within_viewport = bool(
                    rect
                    and rect["left"] >= 0
                    and rect["top"] >= 0
                    and rect["right"] <= viewport["width"] + 1
                    and rect["bottom"] <= viewport["height"] + 1
                )
                if not (
                    planner["phase"] == "night"
                    and planner["panelOpen"]
                    and planner["panelMode"] == "planner"
                    and planner["tab"] == "home"
                    and planner["overlay"]
                    and planner["panelClass"]
                    and planner["shell"]
                    and planner["tabs"] == 3
                    and not planner["dealTab"]
                    and planner["pickerCentered"]
                    and planner["homeLayout"]["cards"] == 3
                    and planner["homeLayout"]["columns"] == 3
                    and planner["homeLayout"]["fillRatio"] >= 0.95
                    and planner["homeLayout"]["overflow"] == 0
                    and planner["homeLayout"]["visibleAboveFooter"]
                    and planner["homeLayout"]["actionsVisible"]
                    and planner["footer"]
                    and planner["hide"]
                    and planner["finalize"]
                    and "750" in (planner["cash"] or "")
                    and "100" in (planner["credit"] or "")
                    and within_viewport
                    and planner["bodyOverflow"] == [0, 0]
                ):
                    failures.append(f"{name}:planner:{planner}")

                page.screenshot(
                    path=CAPTURES / f"visual-night-planner-{name}.png",
                    animations="disabled",
                )

                page.evaluate(
                    """() => {
                      const shown = new Set(R.nightCards
                        .filter(card => card.upgrade)
                        .map(card => card.upgrade.id));
                      const extra = UPGRADES.find(item => !shown.has(item.id));
                      if(extra)R.nightCards.push({upgrade:extra});
                      renderNightUI();
                    }"""
                )
                four_offer = planner_state(page)
                if not (
                    four_offer["homeLayout"]["cards"] == 4
                    and four_offer["homeLayout"]["columns"] == 4
                    and four_offer["homeLayout"]["fillRatio"] >= 0.95
                    and four_offer["homeLayout"]["overflow"] == 0
                    and four_offer["homeLayout"]["minimumCardWidth"] >= 150
                    and four_offer["homeLayout"]["visibleAboveFooter"]
                    and four_offer["homeLayout"]["actionsVisible"]
                    and four_offer["bodyOverflow"] == [0, 0]
                ):
                    failures.append(f"{name}:four-home-offers:{four_offer}")
                page.screenshot(
                    path=CAPTURES / f"visual-night-home-four-{name}.png",
                    animations="disabled",
                )

                page.evaluate(
                    """() => {
                      R.nightCards = R.nightCards.slice(0, 3);
                      renderNightUI();
                    }"""
                )

                page.click(".night-planner-hide")
                room = page.evaluate(
                    """() => ({
                      panelOpen:nightState.panelOpen,
                      overlay:document.getElementById('overlay').classList.contains('active'),
                      homeMode:document.body.classList.contains('home-mode'),
                      tablet:document.querySelector(
                        '.home-hotspot-tablet .home-hotspot-label'
                      )?.textContent,
                      door:document.querySelector(
                        '.home-hotspot-outings .home-hotspot-label'
                      )?.textContent
                    })"""
                )
                if not (
                    not room["panelOpen"]
                    and not room["overlay"]
                    and room["homeMode"]
                    and room["tablet"] == "NIGHT PLANNER"
                    and room["door"] == "SOCIAL"
                ):
                    failures.append(f"{name}:room:{room}")

                page.click(".home-hotspot-shop")
                section = page.evaluate(
                    """() => ({
                      mode:nightState.panelMode,
                      tab:nightState.tab,
                      title:document.querySelector(
                        '.night-panel-header h2'
                      )?.textContent,
                      shop:!!document.querySelector('.night-home-desk'),
                      planner:!!document.querySelector('.night-planner-shell'),
                      tabs:document.querySelectorAll('.night-planner-tab').length,
                      footer:!!document.querySelector('.night-footer')
                    })"""
                )
                if not (
                    section["mode"] == "section"
                    and section["tab"] == "home"
                    and section["title"] == "Home Shop"
                    and section["shop"]
                    and not section["planner"]
                    and section["tabs"] == 0
                    and not section["footer"]
                ):
                    failures.append(f"{name}:section:{section}")
                page.click(".night-panel-header .btn")

                page.click(".home-hotspot-outings")
                social = page.evaluate(
                    """() => ({
                      mode:nightState.panelMode,
                      tab:nightState.tab,
                      title:document.querySelector(
                        '.night-panel-header h2'
                      )?.textContent,
                      tabs:[...document.querySelectorAll(
                        '.night-planner-tab strong'
                      )].map(node => node.textContent),
                      outings:!!document.querySelector('.night-outings-desk'),
                      footer:!!document.querySelector('.night-footer')
                    })"""
                )
                if not (
                    social["mode"] == "social"
                    and social["tab"] == "outings"
                    and social["title"] == "Social"
                    and social["tabs"] == ["OUTINGS", "RELATIONSHIPS"]
                    and social["outings"]
                    and not social["footer"]
                ):
                    failures.append(f"{name}:social:{social}")
                page.click(
                    ".night-planner-tab:has-text('RELATIONSHIPS')"
                )
                social_relationships = page.evaluate(
                    """() => ({
                      tab:nightState.tab,
                      relationships:!!document.querySelector(
                        '.night-relationships-desk'
                      ),
                      tabs:document.querySelectorAll(
                        '.night-planner-tab'
                      ).length
                    })"""
                )
                if not (
                    social_relationships["tab"] == "relationships"
                    and social_relationships["relationships"]
                    and social_relationships["tabs"] == 2
                ):
                    failures.append(
                        f"{name}:social-relationships:{social_relationships}"
                    )
                page.screenshot(
                    path=CAPTURES / f"visual-night-social-{name}.png",
                    animations="disabled",
                )
                page.click(".night-panel-header .btn")

                page.click(".home-hotspot-tablet")
                reopened = planner_state(page)
                if not (
                    reopened["panelMode"] == "planner"
                    and reopened["tab"] == "home"
                    and reopened["tabs"] == 3
                    and not reopened["dealTab"]
                    and reopened["pickerCentered"]
                ):
                    failures.append(f"{name}:reopened:{reopened}")

                page.evaluate(
                    """() => {
                      R.paths.Sales = 'negotiation';
                      R.milestones.Sales = 3;
                      R.today = {additionalNightPurchases:0,log:[]};
                      nightPhase({animate:false});
                    }"""
                )
                unlocked = planner_state(page)
                if not (
                    unlocked["tabs"] == 4
                    and unlocked["dealTab"]
                    and page.locator(".home-overview-grid").count() == 1
                ):
                    failures.append(f"{name}:unlocked:{unlocked}")
                page.click('.night-planner-tab[data-night-tab="deals"]')
                deal_picker = planner_state(page)
                if not (
                    deal_picker["tab"] == "deals"
                    and deal_picker["tabs"] == 4
                    and deal_picker["dealTab"]
                    and deal_picker["pickerCentered"]
                ):
                    failures.append(f"{name}:deal-picker:{deal_picker}")

                if page_errors or console_errors:
                    failures.append(
                        f"{name}:browser-errors:{page_errors}:{console_errors}"
                    )
                evidence[name] = {
                    "overview": overview,
                    "planner": planner,
                    "fourOffer": four_offer,
                    "room": room,
                    "section": section,
                    "social": social,
                    "socialRelationships": social_relationships,
                    "reopened": reopened,
                    "unlocked": unlocked,
                    "dealPicker": deal_picker,
                }
                context.close()

            context = browser.new_context(viewport={"width": 1440, "height": 900})
            page = context.new_page()
            load(page)
            start_night(page, 87002)
            preference = page.evaluate(
                """async () => {
                  const advance = owAdvanceAfterNight;
                  owAdvanceAfterNight = () => { R.phase = 'afterNightTest'; };
                  nightState.outingUsed = true;
                  nightState.homeUsed = nightState.homeLimit;
                  nightState.dealUsed = nightState.dealLimit;
                  R.expenseCredit = 0;
                  await owFinalizeNightUnlocked({animate:false,source:'planner'});
                  const planner = R.nightViewPreference;
                  R.today = {additionalNightPurchases:0,log:[]};
                  nightPhase({animate:false});
                  const plannerReopens = nightState.panelOpen &&
                    nightState.panelMode === 'planner';
                  nightState.outingUsed = true;
                  nightState.homeUsed = nightState.homeLimit;
                  nightState.dealUsed = nightState.dealLimit;
                  R.expenseCredit = 0;
                  await owFinalizeNightUnlocked({animate:false,source:'room'});
                  const room = R.nightViewPreference;
                  R.today = {additionalNightPurchases:0,log:[]};
                  nightPhase({animate:false});
                  const roomReopens = !nightState.panelOpen &&
                    !document.getElementById('overlay').classList.contains('active');
                  owAdvanceAfterNight = advance;
                  return {planner,plannerReopens,room,roomReopens};
                }"""
            )
            if preference != {
                "planner": "planner",
                "plannerReopens": True,
                "room": "room",
                "roomReopens": True,
            }:
                failures.append(f"preference:{preference}")
            evidence["preference"] = preference
            context.close()

            context = browser.new_context(viewport={"width": 1440, "height": 900})
            page = context.new_page()
            load(page)
            guided_compatibility = page.evaluate(
                """() => {
                  const legacyIncomplete = owMigrateMeta({
                    schema:3,
                    tutorial:{
                      completed:false,nextStep:7,
                      skipped:false,replayRequested:false
                    },
                    settings:{volume:70}
                  });
                  const legacyComplete = owMigrateMeta({
                    schema:4,
                    tutorial:{
                      completed:true,nextStep:10,
                      skipped:false,replayRequested:false
                    },
                    settings:{volume:70}
                  });
                  return {
                    incomplete:{
                      legacy:legacyIncomplete.tutorial,
                      guided:legacyIncomplete.guidedIntern
                    },
                    complete:{
                      legacy:legacyComplete.tutorial,
                      guided:legacyComplete.guidedIntern
                    },
                    lessons:OfficeWarsTest.guidedInternLessons().map(
                      lesson=>lesson.id
                    ),
                    oldUi:{
                      callout:!!document.getElementById('tutorial-callout'),
                      backdrop:!!document.getElementById('tutorial-backdrop'),
                      focusRing:!!document.getElementById('tutorial-focus-ring')
                    }
                  };
                }"""
            )
            if not (
                guided_compatibility["incomplete"]["legacy"]["nextStep"] == 5
                and not guided_compatibility["incomplete"]["legacy"]["completed"]
                and guided_compatibility["incomplete"]["guided"]["required"]
                and not guided_compatibility["incomplete"]["guided"]["completed"]
                and guided_compatibility["complete"]["legacy"]["nextStep"] == 13
                and guided_compatibility["complete"]["legacy"]["completed"]
                and guided_compatibility["complete"]["guided"]["required"]
                and not guided_compatibility["complete"]["guided"]["completed"]
                and len(guided_compatibility["lessons"]) == 18
                and len(set(guided_compatibility["lessons"])) == 18
                and not any(guided_compatibility["oldUi"].values())
            ):
                failures.append(
                    f"guided-compatibility:{guided_compatibility}"
                )
            evidence["guidedCompatibility"] = guided_compatibility
            context.close()
        finally:
            browser.close()

    print(json.dumps(evidence, separators=(",", ":")))
    if failures:
        print("FAIL:" + json.dumps(failures))
        return 1
    print("PASS:NIGHT_PLANNER")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
