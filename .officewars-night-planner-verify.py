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
READY = "document.documentElement.dataset.officewarsReady === 'true'"
META_COMPLETE = json.dumps(
    {
        "schema": 4,
        "tutorial": {
            "completed": True,
            "nextStep": 10,
            "skipped": False,
            "replayRequested": False,
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
          return {
            phase:R.phase,
            panelOpen:nightState.panelOpen,
            panelMode:nightState.panelMode,
            tab:nightState.tab,
            overlay:document.getElementById('overlay').classList.contains('active'),
            panelClass:panel.classList.contains('night-planner-panel'),
            shell:!!shell,
            tabs:document.querySelectorAll('.night-planner-tab').length,
            disabledDeals:!!document.querySelector(
              '.night-planner-tab:disabled'
            ),
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
                    and planner["tabs"] == 4
                    and planner["disabledDeals"]
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
                    path=ROOT / f".visual-night-planner-{name}.png",
                    animations="disabled",
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
                    path=ROOT / f".visual-night-social-{name}.png",
                    animations="disabled",
                )
                page.click(".night-panel-header .btn")

                page.click(".home-hotspot-tablet")
                reopened = planner_state(page)
                if not (
                    reopened["panelMode"] == "planner"
                    and reopened["tab"] == "home"
                    and reopened["tabs"] == 4
                ):
                    failures.append(f"{name}:reopened:{reopened}")

                if page_errors or console_errors:
                    failures.append(
                        f"{name}:browser-errors:{page_errors}:{console_errors}"
                    )
                evidence[name] = {
                    "planner": planner,
                    "room": room,
                    "section": section,
                    "social": social,
                    "socialRelationships": social_relationships,
                    "reopened": reopened,
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
            migrations = page.evaluate(
                """() => {
                  const migrate = nextStep => owMigrateMeta({
                    schema:3,
                    tutorial:{
                      completed:false,
                      nextStep,
                      skipped:false,
                      replayRequested:false
                    },
                    settings:{volume:70}
                  }).tutorial.nextStep;
                  return {
                    beforeNight:migrate(4),
                    nightHome:migrate(5),
                    nightMiddle:migrate(7),
                    promotion:migrate(9),
                    capstone:migrate(12),
                    complete:owMigrateMeta({
                      schema:3,
                      tutorial:{completed:true,nextStep:13},
                      settings:{volume:70}
                    }).tutorial.nextStep,
                    total:OW_ORIENTATION_STEPS.length
                  };
                }"""
            )
            if migrations != {
                "beforeNight": 4,
                "nightHome": 5,
                "nightMiddle": 5,
                "promotion": 6,
                "capstone": 9,
                "complete": 10,
                "total": 10,
            }:
                failures.append(f"migration:{migrations}")

            page.evaluate(
                """() => {
                  const meta = owReadMeta();
                  meta.tutorial = {
                    completed:false,
                    nextStep:5,
                    skipped:false,
                    replayRequested:false
                  };
                  owWriteMeta(meta);
                  startRun({seed:87003});
                  R.today = {additionalNightPurchases:0,log:[]};
                  nightPhase({animate:false});
                  void owMaybeShowOrientationForPhase('night');
                }"""
            )
            page.wait_for_function(
                "document.getElementById('tutorial-callout').classList.contains('active')"
            )
            tutorial = page.evaluate(
                """() => ({
                  title:document.getElementById('tutorial-title').textContent,
                  copy:document.getElementById('tutorial-copy').textContent,
                  planner:!!document.querySelector('.night-planner-shell'),
                  focus:document.getElementById(
                    'tutorial-focus-ring'
                  ).classList.contains('active'),
                  step:owOrientationStepIndex
                })"""
            )
            if not (
                tutorial["title"] == "PLAN YOUR NIGHT"
                and "Hide Planner" in tutorial["copy"]
                and tutorial["planner"]
                and tutorial["focus"]
                and tutorial["step"] == 5
            ):
                failures.append(f"tutorial:{tutorial}")
            evidence["migration"] = migrations
            evidence["tutorial"] = tutorial
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
