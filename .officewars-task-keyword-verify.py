import json
import os
import sys
from pathlib import Path


TEMP_ROOT = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if TEMP_ROOT:
    sys.path.insert(0, os.path.join(TEMP_ROOT, "officewars-python"))

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
URL = (ROOT / "officewarsautobattler.html").as_uri()
META = {
    "schema": 4,
    "tutorial": {
        "completed": True,
        "nextStep": 10,
        "skipped": False,
        "replayRequested": False,
    },
    "settings": {"volume": 70},
}


def load(page):
    page.goto(URL, wait_until="load", timeout=30_000)
    page.evaluate(
        "(meta) => localStorage.setItem('officewars.meta.v1', JSON.stringify(meta))",
        META,
    )
    page.reload(wait_until="load", timeout=30_000)
    page.wait_for_function(
        "document.documentElement.dataset.officewarsReady === 'true'",
        timeout=30_000,
    )


def setup_morning(page):
    page.evaluate(
        """() => {
          startRun({seed: 81126});
          hideOverlay();
          R.phase = 'morning';
          R.morningCards = [
            'versionControl',
            'meetingPrep',
            'accrualAccounting'
          ].map(id => owTaskCardFromTask(TASK_BY_ID.get(id), 'morning'));
          R.pins = [];
          renderMorningUI();
        }"""
    )
    page.wait_for_selector(".morning-window")


def check_card_markup(page):
    return page.evaluate(
        """() => {
          const samples = {};
          for (const task of TASKS) {
            const card = owTaskCardFromTask(task, 'morning');
            const host = document.createElement('div');
            host.innerHTML = owMorningCardMarkup(card, 0, 'offer');
            samples[task.id] = {
              expected: owKeywordEntries(task.effect).map(entry => entry.term),
              actual: [...new Set(
                [...host.querySelectorAll('.rules-keyword')]
                  .map(node => OW_RULE_KEYWORD_BY_ALIAS.get(
                    node.textContent.toLowerCase()
                  )?.term || node.textContent)
              )],
              parentTip: host.querySelector('.task-card')?.dataset.tip || ''
            };
          }
          return samples;
        }"""
    )


def sample_celestial_arcs(page):
    return page.evaluate(
        """async () => {
          const root = document.getElementById('phase-transition');
          const sun = root.querySelector('.transition-sun');
          const moon = root.querySelector('.transition-moon');
          const centerX = element => {
            const rect = element.getBoundingClientRect();
            return rect.left + rect.width / 2;
          };
          const sample = async phase => {
            root.className = `active ${phase}`;
            await new Promise(resolve => requestAnimationFrame(
              () => requestAnimationFrame(resolve)
            ));
            const sunAnimation = sun.getAnimations().find(animation =>
              animation.animationName === (
                phase === 'sunset' ? 'ow-arc-descend' : 'ow-arc-ascend'
              )
            );
            const moonAnimation = moon.getAnimations().find(animation =>
              animation.animationName === (
                phase === 'sunset' ? 'ow-arc-ascend' : 'ow-arc-descend'
              )
            );
            if (!sunAnimation || !moonAnimation) {
              return {error:'missing animation'};
            }
            sunAnimation.pause();
            moonAnimation.pause();
            const duration = Number(sunAnimation.effect.getTiming().duration);
            const points = [];
            for (const fraction of [0, .25, .5, .75, 1]) {
              sunAnimation.currentTime = duration * fraction;
              moonAnimation.currentTime = duration * fraction;
              await new Promise(resolve => requestAnimationFrame(resolve));
              points.push({
                fraction,
                sunX:centerX(sun),
                moonX:centerX(moon)
              });
            }
            root.className = '';
            return {duration,points};
          };
          return {
            width:innerWidth,
            sunset:await sample('sunset'),
            sunrise:await sample('sunrise')
          };
        }"""
    )


def main():
    failures = []
    evidence = {}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            args=["--allow-file-access-from-files", "--disable-extensions"],
        )
        try:
            for name, width, height, touch in [
                ("desktop", 1440, 900, False),
                ("landscape", 844, 390, True),
            ]:
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    has_touch=touch,
                )
                page = context.new_page()
                page_errors = []
                console_errors = []
                page.on("pageerror", lambda error: page_errors.append(str(error)))
                page.on(
                    "console",
                    lambda message: (
                        console_errors.append(message.text)
                        if message.type == "error"
                        else None
                    ),
                )
                load(page)
                setup_morning(page)

                markup = check_card_markup(page)
                mismatches = {
                    task_id: result
                    for task_id, result in markup.items()
                    if result["expected"] != result["actual"]
                    or (result["expected"] and not result["parentTip"])
                }
                if mismatches:
                    failures.append(f"{name}:card-markup:{mismatches}")

                required_terms = {
                    term
                    for result in markup.values()
                    for term in result["actual"]
                }
                expected_terms = {
                    "Pinned Task",
                    "Commit",
                    "Team Meeting",
                    "Natural",
                    "Ordinary Action",
                    "Reserve Level",
                    "Interest-Eligible Cash",
                    "Clock Out",
                    "Flat Stress",
                    "Expense Credit",
                    "Coworker Bonus",
                    "Task Reroll",
                    "Home Reroll",
                    "Positive Action",
                }
                missing_terms = sorted(expected_terms - required_terms)
                if missing_terms:
                    failures.append(f"{name}:keyword-coverage:{missing_terms}")

                page.evaluate(
                    """() => {
                      R.morningCards = [
                        'commissionAdvance',
                        'corporateExpenseAccount',
                        'priorityRequisition'
                      ].map(id => owTaskCardFromTask(TASK_BY_ID.get(id), 'morning'));
                      renderMorningUI();
                    }"""
                )
                first_card = page.locator(".morning-full-cards .task-card").first
                first_keyword = page.locator(
                    ".morning-full-cards .task-card .rules-keyword"
                ).first
                compact_keyword = page.locator(
                    ".morning-compact-detail .rules-keyword"
                ).first
                before = page.evaluate(
                    "() => ({phase:R.phase,todayCard:R.todayCard,days:R.stats.days})"
                )
                if touch:
                    compact_keyword.tap()
                else:
                    first_keyword.click()
                after = page.evaluate(
                    "() => ({phase:R.phase,todayCard:R.todayCard,days:R.stats.days})"
                )
                tooltip = page.locator("#global-tip")
                if before != after or not tooltip.is_visible():
                    failures.append(
                        f"{name}:keyword-click-safety:{before}:{after}:"
                        f"{tooltip.is_visible()}"
                    )

                if touch:
                    compact_keyword.focus()
                else:
                    first_card.focus()
                if not tooltip.is_visible() or not tooltip.inner_text().strip():
                    failures.append(f"{name}:keyword-focus-tooltip")

                page.evaluate(
                    """() => {
                      owChoiceState = {
                        title:'Task Card Keyword Check',
                        subtitle:'Choose one.',
                        options:[
                          owCardOption(
                            owTaskCardFromTask(
                              TASK_BY_ID.get('parallelProcessing'),
                              'choice'
                            ),
                            'full'
                          )
                        ],
                        min:1,
                        max:1,
                        selected:[],
                        resolve:() => {}
                      };
                      owRenderChoice();
                    }"""
                )
                choice = page.evaluate(
                    """() => {
                      const card = document.querySelector('.task-choice-card');
                      return {
                        keywords:[...card.querySelectorAll('.rules-keyword')]
                          .map(node => node.textContent),
                        tip:card.dataset.tip || ''
                      };
                    }"""
                )
                if (
                    "positive stress" not in {
                        value.lower() for value in choice["keywords"]
                    }
                    or "Positive Stress:" not in choice["tip"]
                ):
                    failures.append(f"{name}:choice-card:{choice}")
                if touch:
                    selected_before = page.evaluate(
                        "() => owChoiceState.selected.slice()"
                    )
                    page.locator(
                        ".task-choice-card .rules-keyword"
                    ).first.tap()
                    selected_after = page.evaluate(
                        "() => owChoiceState.selected.slice()"
                    )
                    if selected_before != selected_after:
                        failures.append(
                            f"{name}:choice-keyword-tap:"
                            f"{selected_before}:{selected_after}"
                        )
                hide_result = page.evaluate(
                    """() => {
                      hideOverlay();
                      R.phase = 'morning';
                      R.morningCards = [
                        owTaskCardFromTask(
                          TASK_BY_ID.get('versionControl'),
                          'morning'
                        )
                      ];
                      R.pins = [];
                      owAddCurrentPin(
                        'commissionAdvance',
                        'Verification',
                        {},
                        false
                      );
                      renderMorningUI();
                      owOpenPinnedTaskDetail(0);
                      const detail = document.querySelector(
                        '.pinned-task-detail-card'
                      );
                      return {
                        keywords:[...detail.querySelectorAll('.rules-keyword')]
                          .map(node => node.textContent),
                        focusable:[...detail.querySelectorAll('.rules-keyword')]
                          .every(node => node.tabIndex === 0)
                      };
                    }"""
                )
                if (
                    "flat stress" not in {
                        value.lower() for value in hide_result["keywords"]
                    }
                    or not hide_result["focusable"]
                ):
                    failures.append(f"{name}:pinned-detail:{hide_result}")
                page.evaluate("() => closeHudModal('pinned-task-detail')")

                arcs = sample_celestial_arcs(page)
                if "error" in arcs["sunset"] or "error" in arcs["sunrise"]:
                    failures.append(f"{name}:celestial-animation:{arcs}")
                else:
                    sunset = arcs["sunset"]["points"]
                    sunrise = arcs["sunrise"]["points"]
                    if not (
                        all(point["sunX"] < point["moonX"] for point in sunset)
                        and sunset[-1]["sunX"] < 0
                        and sunset[0]["moonX"] > width
                        and sunset[-1]["sunX"] < sunset[0]["sunX"]
                        and sunset[-1]["moonX"] < sunset[0]["moonX"]
                    ):
                        failures.append(f"{name}:sunset-direction:{sunset}")
                    if not (
                        all(point["moonX"] < point["sunX"] for point in sunrise)
                        and sunrise[-1]["moonX"] < 0
                        and sunrise[0]["sunX"] > width
                        and sunrise[-1]["sunX"] < sunrise[0]["sunX"]
                        and sunrise[-1]["moonX"] < sunrise[0]["moonX"]
                    ):
                        failures.append(f"{name}:sunrise-direction:{sunrise}")

                page.evaluate(
                    "() => { hideOverlay(); R.phase='morning'; renderMorningUI(); }"
                )
                page.screenshot(
                    path=ROOT / f".visual-{name}-task-keywords.png",
                    animations="disabled",
                )
                if page_errors or console_errors:
                    failures.append(
                        f"{name}:browser-errors:{page_errors}:{console_errors}"
                    )
                evidence[name] = {
                    "tasksWithKeywords": sum(
                        1 for result in markup.values() if result["actual"]
                    ),
                    "terms": sorted(required_terms),
                    "choice": choice,
                    "pinnedDetail": hide_result,
                    "arcs": arcs,
                }
                context.close()
        finally:
            browser.close()

    print(json.dumps(evidence, separators=(",", ":")))
    if failures:
        print("FAIL:" + json.dumps(failures))
        return 1
    print("PASS:TASK_KEYWORDS_CELESTIAL_DIRECTION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
