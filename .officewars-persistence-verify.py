import json
import os
import sys
import time
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
    }
)


def load(page, clear=False, tutorial_complete=True):
    page.goto(GAME_URL, wait_until="load", timeout=30_000)
    page.wait_for_function(READY, timeout=15_000)
    if clear:
        page.evaluate("localStorage.clear()")
    if tutorial_complete:
        page.evaluate(
            "(meta) => localStorage.setItem(OW_META_KEY, meta)", META_COMPLETE
        )
    if clear or tutorial_complete:
        page.reload(wait_until="load", timeout=30_000)
        page.wait_for_function(READY, timeout=15_000)


def wait_phase(page, phase, timeout=30_000):
    try:
        page.wait_for_function(
            "(phase) => typeof R !== 'undefined' && R && R.phase === phase",
            arg=phase,
            timeout=timeout,
        )
    except Exception:
        print(
            "PHASE_TIMEOUT="
            + json.dumps(
                page.evaluate(
                    """() => ({
                      phase: typeof R !== 'undefined' && R && R.phase,
                      saveError: window.owLastSaveError,
                      pageErrors: document.title
                    })"""
                )
            )
        )
        raise


def wait_casino(page, predicate, timeout=30_000):
    try:
        page.wait_for_function(predicate, timeout=timeout)
    except Exception:
        print(
            "CASINO_TIMEOUT="
            + json.dumps(
                page.evaluate(
                    """() => ({
                      phase: typeof R !== 'undefined' && R && R.phase,
                      open: typeof casinoOpen !== 'undefined' && casinoOpen,
                      view: typeof owCasinoView !== 'undefined' && owCasinoView,
                      pending: typeof OW_SLOT_PENDING !== 'undefined'
                        ? OW_SLOT_PENDING
                        : 'unavailable',
                      chips: typeof CASINO !== 'undefined' && CASINO.chips,
                      save: localStorage.getItem(OW_SAVE_KEY),
                      saveError: window.owLastSaveError
                    })"""
                )
            )
        )
        raise


def main():
    checks = {}
    detail = {}

    def expect(name, value, evidence=None):
        checks[name] = bool(value)
        detail[name] = evidence

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
            context = browser.new_context(viewport={"width": 1440, "height": 900})
            page = context.new_page()
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            load(page, clear=True)

            round_trip = page.evaluate(
                """() => {
                  const value = {
                    set: new Set(['a', 'b']),
                    map: new Map([['x', 4]]),
                    positive: Infinity,
                    negative: -Infinity
                  };
                  const restored = OfficeWarsTest.saveRoundTrip(value);
                  return {
                    set: restored.set instanceof Set && restored.set.has('b'),
                    map: restored.map instanceof Map && restored.map.get('x') === 4,
                    positive: restored.positive === Infinity,
                    negative: restored.negative === -Infinity
                  };
                }"""
            )
            expect("serializer-round-trip", all(round_trip.values()), round_trip)

            page.evaluate(
                "localStorage.setItem(OW_SAVE_KEY, '{broken-json')"
            )
            page.reload(wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            corrupt = page.evaluate(
                """() => ({
                  removed: localStorage.getItem(OW_SAVE_KEY) === null,
                  hidden: document.getElementById('menu-continue').hidden,
                  notice: document.getElementById('menu-save-notice').textContent
                })"""
            )
            expect(
                "corrupt-save-discarded",
                corrupt["removed"]
                and corrupt["hidden"]
                and "could not be restored" in corrupt["notice"],
                corrupt,
            )
            page.evaluate(
                "localStorage.setItem(OW_SAVE_KEY, JSON.stringify({schema: 999}))"
            )
            page.reload(wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            incompatible = page.evaluate(
                """() => ({
                  removed: localStorage.getItem(OW_SAVE_KEY) === null,
                  hidden: document.getElementById('menu-continue').hidden,
                  notice: document.getElementById('menu-save-notice').textContent
                })"""
            )
            expect(
                "incompatible-save-discarded",
                incompatible["removed"]
                and incompatible["hidden"]
                and "retired Home system" in incompatible["notice"]
                and "Settings and tutorial progress were preserved"
                in incompatible["notice"],
                incompatible,
            )

            page.evaluate(
                """(meta) => {
                  localStorage.setItem(OW_META_KEY, meta);
                  startRun({seed: 44001});
                }""",
                META_COMPLETE,
            )
            wait_phase(page, "floorIntro")
            floor_save = page.evaluate(
                """() => {
                  const save = JSON.parse(localStorage.getItem(OW_SAVE_KEY));
                  return {
                    checkpoint: save.checkpoint,
                    floor: save.preview.floor,
                    continueVisible: !document.getElementById('menu-continue').hidden
                  };
                }"""
            )
            expect(
                "floor-intro-autosave",
                floor_save["checkpoint"] == "floorIntro"
                and floor_save["floor"] == 1,
                floor_save,
            )

            page.reload(wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            continue_menu = page.evaluate(
                """() => ({
                  visible: !document.getElementById('menu-continue').hidden,
                  preview: document.getElementById('menu-continue-detail').textContent
                })"""
            )
            page.evaluate("owContinueRun()")
            wait_phase(page, "floorIntro")
            restored_floor = page.evaluate(
                """() => ({
                  floor: R.floor,
                  overlay: document.getElementById('overlay').classList.contains('active'),
                  office: document.getElementById('office-scene').classList.contains('active')
                })"""
            )
            expect(
                "continue-menu-preview",
                continue_menu["visible"]
                and "Floor 1" in continue_menu["preview"],
                continue_menu,
            )
            expect(
                "floor-intro-restore",
                restored_floor["floor"] == 1
                and restored_floor["overlay"]
                and restored_floor["office"],
                restored_floor,
            )

            page.evaluate("owClockIn()")
            wait_phase(page, "morning")
            morning_before = page.evaluate(
                """() => ({
                  cards: R.morningCards.map(card => card.task.id),
                  rng: RNG.snapshot(),
                  checkpoint: JSON.parse(localStorage.getItem(OW_SAVE_KEY)).checkpoint
                })"""
            )
            page.reload(wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            page.evaluate("owContinueRun()")
            wait_phase(page, "morning")
            morning_after = page.evaluate(
                """() => ({
                  cards: R.morningCards.map(card => card.task.id),
                  rng: RNG.snapshot()
                })"""
            )
            expect(
                "morning-offer-restore",
                morning_before["checkpoint"] == "morning"
                and morning_before["cards"] == morning_after["cards"]
                and morning_before["rng"] == morning_after["rng"],
                {"before": morning_before, "after": morning_after},
            )

            page.evaluate(
                """() => {
                  const task = TASK_BY_ID.get('regressionTests');
                  R.morningCards = [{
                    task,
                    rarity: task.rarity,
                    source: 'offer',
                    modifiers: {}
                  }];
                  renderMorningUI();
                  owPersistCheckpoint('morning');
                  selectMorning(0, 'offer');
                  void confirmMorning();
                }"""
            )
            page.wait_for_function(
                """() => {
                  const raw = localStorage.getItem(OW_SAVE_KEY);
                  return raw && JSON.parse(raw).checkpoint === 'workdayPrepared';
                }""",
                timeout=30_000,
            )
            prepared_raw = page.evaluate("localStorage.getItem(OW_SAVE_KEY)")
            prepared_evidence = page.evaluate(
                """() => {
                  const save = JSON.parse(localStorage.getItem(OW_SAVE_KEY));
                  return {
                    phase: R.phase,
                    checkpoint: save.checkpoint,
                    codingXp: save.run.familyXP.Coding,
                    plays: save.run.today.taskPlays.length,
                    entries: save.run.today.scheduleEntries.length
                  };
                }"""
            )
            expect(
                "prepared-workday-checkpoint",
                prepared_evidence["checkpoint"] == "workdayPrepared"
                and prepared_evidence["codingXp"] == 1
                and prepared_evidence["plays"] == 1
                and prepared_evidence["entries"] >= 5,
                prepared_evidence,
            )

            def restore_prepared():
                page.reload(wait_until="load", timeout=30_000)
                page.wait_for_function(READY, timeout=15_000)
                page.evaluate(
                    "(raw) => localStorage.setItem(OW_SAVE_KEY, raw)", prepared_raw
                )
                continuation = page.evaluate(
                    """async () => {
                      const before = JSON.parse(
                        localStorage.getItem(OW_SAVE_KEY)
                      ).checkpoint;
                      await owContinueRun();
                      return {
                        before,
                        phase: R.phase,
                        checkpoint: JSON.parse(
                          localStorage.getItem(OW_SAVE_KEY)
                        ).checkpoint,
                        review: R.politicsReview &&
                          R.politicsReview.status,
                        headless: owHeadlessRunActive
                      };
                    }"""
                )
                if continuation["phase"] != "politicsReview":
                    raise AssertionError(
                        "Prepared restore bypassed Review: "
                        + json.dumps(continuation)
                    )
                wait_phase(page, "politicsReview")
                review = page.evaluate(
                    """() => {
                      const save = JSON.parse(localStorage.getItem(OW_SAVE_KEY));
                      return {
                        phase: R.phase,
                        checkpoint: save.checkpoint,
                        pages: R.politicsReview.pages.length,
                        pageTypes: R.politicsReview.pages.map(
                          page => page.type
                        ),
                        choices: Object.keys(R.politicsReview.choices).length,
                        confirmed: R.politicsReview.confirmed,
                        settled: R.politicsReview.settled,
                        codingXp: R.familyXP.Coding,
                        plays: R.today.taskPlays.length,
                        focusId: document.activeElement && document.activeElement.id
                      };
                    }"""
                )
                page.evaluate(
                    """async () => {
                      owAutoStagePoliticsReview(
                        R.politicsReview,
                        'skilled'
                      );
                      await owConfirmPoliticsReview();
                    }"""
                )
                wait_phase(page, "politicsReviewSettled")
                settled_raw = page.evaluate(
                    "localStorage.getItem(OW_SAVE_KEY)"
                )
                settled_before = page.evaluate(
                    """() => ({
                      phase:R.phase,
                      project:R.project.progress,
                      stress:R.stress,
                      cash:R.cash,
                      results:R.politicsReview.results.length,
                      checkpoint:JSON.parse(
                        localStorage.getItem(OW_SAVE_KEY)
                      ).checkpoint
                    })"""
                )
                page.reload(wait_until="load", timeout=30_000)
                page.wait_for_function(READY, timeout=15_000)
                page.evaluate(
                    "(raw) => localStorage.setItem(OW_SAVE_KEY, raw)",
                    settled_raw,
                )
                page.evaluate("owContinueRun()")
                wait_phase(page, "politicsReviewSettled")
                settled_after = page.evaluate(
                    """() => ({
                      phase:R.phase,
                      project:R.project.progress,
                      stress:R.stress,
                      cash:R.cash,
                      results:R.politicsReview.results.length,
                      checkpoint:JSON.parse(
                        localStorage.getItem(OW_SAVE_KEY)
                      ).checkpoint,
                      resultsVisible:document.getElementById(
                        'overlay-panel'
                      ).textContent.includes('OFFICE POLITICS · RESULTS')
                    })"""
                )
                page.evaluate("owContinueFromPoliticsReview()")
                wait_phase(page, "clockOut")
                clock_out = page.evaluate(
                    """() => ({
                      project: R.project.progress,
                      stress: R.stress,
                      cash: R.cash,
                      rival: R.rival.progress,
                      daysLeft: R.daysLeft,
                      codingXp: R.familyXP.Coding,
                      plays: R.today.taskPlays.length,
                      gameplayRng: RNG.snapshot().gameplayState
                    })"""
                )
                return {
                    "review": review,
                    "settledRestore": {
                        "before": settled_before,
                        "after": settled_after,
                    },
                    "clockOut": clock_out,
                }

            def restore_cinematic_prepared():
                page.reload(wait_until="load", timeout=30_000)
                page.wait_for_function(READY, timeout=15_000)
                page.evaluate(
                    "(raw) => localStorage.setItem(OW_SAVE_KEY, raw)",
                    prepared_raw,
                )
                page.evaluate("owContinueRun()")
                wait_phase(page, "workdayPoliticalQueue")
                page.wait_for_function(
                    """() => document.activeElement&&
                      document.activeElement.classList.contains(
                        'cinematic-choice'
                      )""",
                    timeout=5_000,
                )
                queue = page.evaluate(
                    """() => {
                      const save=JSON.parse(localStorage.getItem(OW_SAVE_KEY));
                      const current=R.today.politicalEvents.find(
                        event=>event.id===R.workdayPresentation.currentEventId
                      );
                      return{
                        phase:R.phase,
                        checkpoint:save.checkpoint,
                        currentEvent:current&&current.id,
                        snapshot:current&&current.snapshot,
                        eventCount:R.today.politicalEvents.length,
                        answered:R.today.politicalEvents.filter(
                          event=>!!event.choice
                        ).length,
                        path:R.workdayPresentation.path,
                        codingXp:R.familyXP.Coding,
                        plays:R.today.taskPlays.length,
                        focus:R.workdayPresentation.focus
                      };
                    }"""
                )

                deadline = time.time() + 20
                while time.time() < deadline:
                    phase = page.evaluate("R.phase")
                    if phase == "politicsResultsReel":
                        break
                    if phase in (
                        "workdayPoliticalChoice",
                        "workdayPoliticalQueue",
                    ):
                        page.evaluate(
                            """() => {
                              const event=R.today.politicalEvents.find(
                                item=>item.id===
                                  R.workdayPresentation.currentEventId
                              );
                              const option=event&&event.page.options.find(
                                item=>
                                  (event.type==='project'&&
                                    item.label==='Safe')||
                                  (event.type==='relationship'&&
                                    item.label==='Take No Action')||
                                  (event.type==='boss'&&
                                    item.label==='Counter')
                              )||event&&event.page.options.find(
                                item=>R.cash>=Number(
                                  item.cost&&item.cost.cash||0
                                )
                              );
                              if(event&&option){
                                owChooseCinematicPolitics(event.id,option.id);
                              }
                            }"""
                        )
                    time.sleep(0.01)
                if page.evaluate("R.phase") != "politicsResultsReel":
                    raise AssertionError(
                        "Cinematic restore did not reach results reel"
                    )

                page.evaluate("owRevealCinematicResult(0)")
                reel_raw = page.evaluate("localStorage.getItem(OW_SAVE_KEY)")
                reel_before = page.evaluate(
                    """() => ({
                      phase:R.phase,
                      project:R.project.progress,
                      stress:R.stress,
                      cash:R.cash,
                      results:owCinematicResultRows().length,
                      reelIndex:R.workdayPresentation.reelIndex,
                      revealed:document.querySelectorAll(
                        '.cinematic-result-card.revealed'
                      ).length,
                      checkpoint:JSON.parse(
                        localStorage.getItem(OW_SAVE_KEY)
                      ).checkpoint
                    })"""
                )
                page.reload(wait_until="load", timeout=30_000)
                page.wait_for_function(READY, timeout=15_000)
                page.evaluate(
                    "(raw) => localStorage.setItem(OW_SAVE_KEY, raw)",
                    reel_raw,
                )
                page.evaluate("owContinueRun()")
                wait_phase(page, "politicsResultsReel")
                reel_after = page.evaluate(
                    """() => ({
                      phase:R.phase,
                      project:R.project.progress,
                      stress:R.stress,
                      cash:R.cash,
                      results:owCinematicResultRows().length,
                      reelIndex:R.workdayPresentation.reelIndex,
                      revealed:document.querySelectorAll(
                        '.cinematic-result-card.revealed'
                      ).length,
                      checkpoint:JSON.parse(
                        localStorage.getItem(OW_SAVE_KEY)
                      ).checkpoint
                    })"""
                )
                page.evaluate(
                    """() => {
                      owRevealAllCinematicResults();
                      owFinishCinematicResults();
                    }"""
                )
                wait_phase(page, "clockOut")
                clock_out = page.evaluate(
                    """() => ({
                      project:R.project.progress,
                      stress:R.stress,
                      cash:R.cash,
                      rival:R.rival.progress,
                      daysLeft:R.daysLeft,
                      codingXp:R.familyXP.Coding,
                      plays:R.today.taskPlays.length,
                      gameplayRng:RNG.snapshot().gameplayState
                    })"""
                )
                return {
                    "queue": queue,
                    "reelRestore": {
                        "before": reel_before,
                        "after": reel_after,
                    },
                    "clockOut": clock_out,
                }

            first_restore = restore_cinematic_prepared()
            second_restore = restore_cinematic_prepared()
            expect(
                "prepared-workday-restores-hidden-queue",
                first_restore["queue"]["phase"] == "workdayPoliticalQueue"
                and first_restore["queue"]["checkpoint"]
                == "workdayPoliticalQueue"
                and first_restore["queue"]["eventCount"] >= 1
                and first_restore["queue"]["answered"] == 0
                and first_restore["queue"]["path"] == "reload-skip"
                and first_restore["queue"]["snapshot"] is not None,
                first_restore["queue"],
            )
            expect(
                "prepared-workday-deterministic-restore",
                first_restore == second_restore,
                {"first": first_restore, "second": second_restore},
            )
            expect(
                "results-reel-restores-once",
                first_restore["reelRestore"]["before"]["project"]
                == first_restore["reelRestore"]["after"]["project"]
                and first_restore["reelRestore"]["before"]["stress"]
                == first_restore["reelRestore"]["after"]["stress"]
                and first_restore["reelRestore"]["before"]["cash"]
                == first_restore["reelRestore"]["after"]["cash"]
                and first_restore["reelRestore"]["before"]["results"]
                == first_restore["reelRestore"]["after"]["results"]
                and first_restore["reelRestore"]["before"]["reelIndex"]
                == first_restore["reelRestore"]["after"]["reelIndex"]
                and first_restore["reelRestore"]["after"]["revealed"] >= 1
                and first_restore["reelRestore"]["after"]["checkpoint"]
                == "politicsResultsReel",
                first_restore["reelRestore"],
            )
            expect(
                "task-reward-not-duplicated",
                first_restore["queue"]["codingXp"] == 1
                and first_restore["queue"]["plays"] == 1
                and first_restore["clockOut"]["codingXp"] == 1
                and first_restore["clockOut"]["plays"] == 1,
                first_restore,
            )

            page.evaluate("afterDayResults()")
            page.evaluate(
                """() => {
                  if (R.phase === 'roleVote') {
                    owContinueRoleVote();
                  }
                }"""
            )
            wait_phase(page, "night")
            page.evaluate(
                """() => {
                  owToggleLightsOut(true);
                  owOpenNightPlanner('relationships');
                }"""
            )
            page.reload(wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            page.evaluate("owContinueRun()")
            wait_phase(page, "night")
            night_restore = page.evaluate(
                """() => ({
                  lightsOut: nightState.recPicked,
                  tab: nightState.tab,
                  panelOpen: nightState.panelOpen,
                  panelMode: nightState.panelMode,
                  planner: !!document.querySelector('.night-planner-shell'),
                  overlay: document.getElementById('overlay').classList.contains('active'),
                  homeMode: document.body.classList.contains('home-mode'),
                  homeScene: document.getElementById('home-scene').classList.contains('active')
                })"""
            )
            expect(
                "night-state-restore",
                night_restore["lightsOut"]
                and night_restore["tab"] == "relationships"
                and night_restore["panelOpen"]
                and night_restore["panelMode"] == "planner"
                and night_restore["planner"]
                and night_restore["overlay"]
                and night_restore["homeMode"]
                and night_restore["homeScene"],
                night_restore,
            )

            resolved_before_reload = page.evaluate(
                """() => {
                  hideOverlay();
                  nightState.panelOpen = false;
                  nightState.outingUsed = true;
                  nightState.homeUsed = nightState.homeLimit;
                  nightState.dealUsed = nightState.dealLimit;
                  R.expenseCredit = 0;
                  owPrepareNightRecoveryForFinalization();
                  const before = R.stress;
                  const recovery = owApplyNightResolution();
                  owPersistCheckpoint('nightResolved');
                  return {
                    before,
                    after: R.stress,
                    recovery,
                    checkpoint: JSON.parse(
                      localStorage.getItem(OW_SAVE_KEY)
                    ).checkpoint
                  };
                }"""
            )
            page.reload(wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            page.evaluate("owContinueRun()")
            page.wait_for_function(
                """() => R && !['night', 'nightResolution'].includes(R.phase)""",
                timeout=30_000,
            )
            resolved_after_reload = page.evaluate(
                """() => ({
                  phase: R.phase,
                  stress: R.stress,
                  homeMode: document.body.classList.contains('home-mode'),
                  homeScene: document.getElementById('home-scene')
                    .classList.contains('active')
                })"""
            )
            expect(
                "night-resolved-restores-once",
                resolved_before_reload["checkpoint"] == "nightResolved"
                and resolved_before_reload["recovery"] > 0
                and resolved_after_reload["stress"]
                == resolved_before_reload["after"]
                and resolved_after_reload["phase"] != "night"
                and not resolved_after_reload["homeMode"]
                and not resolved_after_reload["homeScene"],
                {
                    "before": resolved_before_reload,
                    "after": resolved_after_reload,
                },
            )

            page.evaluate(
                """() => {
                  R.phase = 'gameOver';
                  R.gameResult = 'burnout';
                  runSummary('burnout');
                }"""
            )
            page.reload(wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            page.evaluate("owContinueRun()")
            page.wait_for_function(
                "document.getElementById('screen-gameover').classList.contains('active')"
            )
            result_restore = page.evaluate(
                """() => ({
                  phase: R.phase,
                  result: R.gameResult,
                  title: document.getElementById('go-title').textContent
                })"""
            )
            expect(
                "result-survives-refresh",
                result_restore["phase"] == "gameOver"
                and result_restore["result"] == "burnout"
                and "BURNOUT" in result_restore["title"],
                result_restore,
            )

            page.evaluate("owRequestNewRun()")
            dialog_open = page.evaluate(
                "document.getElementById('menu-dialog').classList.contains('open')"
            )
            page.click("#menu-dialog-confirm")
            wait_phase(page, "floorIntro")
            replacement = page.evaluate(
                """() => ({
                  phase: R.phase,
                  result: R.gameResult,
                  rngSeeded: RNG.snapshot().seeded,
                  checkpoint: JSON.parse(localStorage.getItem(OW_SAVE_KEY)).checkpoint
                })"""
            )
            expect(
                "new-run-confirmation",
                dialog_open
                and replacement["phase"] == "floorIntro"
                and replacement["result"] is None
                and replacement["rngSeeded"]
                and replacement["checkpoint"] == "floorIntro",
                {"dialog": dialog_open, "replacement": replacement},
            )

            page.evaluate(
                """() => {
                  R.phase = 'gameOver';
                  R.gameResult = 'burnout';
                  runSummary('burnout');
                  owReturnToMainMenu();
                }"""
            )
            menu_return = page.evaluate(
                """() => ({
                  menu: !document.getElementById('screen-menu').classList.contains('hidden'),
                  result: document.getElementById('screen-gameover').classList.contains('active'),
                  save: localStorage.getItem(OW_SAVE_KEY)
                })"""
            )
            expect(
                "return-to-menu-clears-active-save",
                menu_return["menu"]
                and not menu_return["result"]
                and menu_return["save"] is None,
                menu_return,
            )
            expect("persistence-no-page-errors", not errors, errors)
            context.close()

            casino_context = browser.new_context(
                viewport={"width": 1440, "height": 900}
            )
            casino_page = casino_context.new_page()
            casino_errors = []
            casino_page.on(
                "pageerror", lambda error: casino_errors.append(str(error))
            )
            load(casino_page, clear=True)

            casino_page.evaluate(
                """() => {
                  startRun({seed: 45001});
                  R.phase = 'weekend';
                  casinoOpen = true;
                  Object.assign(CASINO, {
                    chips: 450,
                    buyIn: 0,
                    pokerHands: 0,
                    bjHands: 0
                  });
                  SLOT_BET = 50;
                  owCasinoView = 'slots';
                  OW_SLOT_PENDING = {
                    bet: 50,
                    result: [SLOT_SYMBOLS[0], SLOT_SYMBOLS[0], SLOT_SYMBOLS[0]]
                  };
                  CASINO.chips -= 50;
                  slotsRender(true);
                  owPersistCheckpoint('weekendCasino');
                }"""
            )
            casino_page.reload(wait_until="load", timeout=30_000)
            casino_page.wait_for_function(READY, timeout=15_000)
            casino_page.evaluate("owContinueRun()")
            wait_casino(
                casino_page,
                "OW_SLOT_PENDING === null && owCasinoView === 'slots'",
            )
            slot_restore = casino_page.evaluate(
                """() => ({
                  chips: CASINO.chips,
                  pending: OW_SLOT_PENDING,
                  message: document.getElementById('slot-msg')?.textContent,
                  checkpoint: JSON.parse(localStorage.getItem(OW_SAVE_KEY)).checkpoint
                })"""
            )
            casino_page.reload(wait_until="load", timeout=30_000)
            casino_page.wait_for_function(READY, timeout=15_000)
            casino_page.evaluate("owContinueRun()")
            wait_casino(
                casino_page,
                "OW_SLOT_PENDING === null && owCasinoView === 'slots'",
            )
            slot_second_restore = casino_page.evaluate(
                "() => ({chips: CASINO.chips, pending: OW_SLOT_PENDING})"
            )
            expect(
                "pending-slot-settles-once",
                slot_restore["chips"] == 550
                and slot_restore["pending"] is None
                and "WINNER" in slot_restore["message"]
                and slot_restore["checkpoint"] == "weekendCasino"
                and slot_second_restore["chips"] == 550
                and slot_second_restore["pending"] is None,
                {"first": slot_restore, "second": slot_second_restore},
            )

            casino_page.evaluate(
                """() => {
                  R.phase = 'weekend';
                  casinoOpen = true;
                  Object.assign(CASINO, {
                    chips: 400,
                    buyIn: 0,
                    pokerHands: 0,
                    bjHands: 1
                  });
                  BJ = {
                    deck: [{r: 2, s: 0}, {r: 3, s: 1}],
                    bet: 100,
                    phase: 'player',
                    player: [{r: 10, s: 0}, {r: 7, s: 1}],
                    dealer: [{r: 9, s: 2}, {r: 6, s: 3}]
                  };
                  owCasinoView = 'blackjack';
                  bjRender('Restore fixture.');
                  owPersistCheckpoint('weekendCasino');
                }"""
            )
            casino_page.reload(wait_until="load", timeout=30_000)
            casino_page.wait_for_function(READY, timeout=15_000)
            casino_page.evaluate("owContinueRun()")
            casino_page.wait_for_function(
                "owCasinoView === 'blackjack' && BJ && BJ.phase === 'player'"
            )
            blackjack_restore = casino_page.evaluate(
                """() => ({
                  chips: CASINO.chips,
                  hands: CASINO.bjHands,
                  value: bjValue(BJ.player),
                  phase: BJ.phase,
                  hit: [...document.querySelectorAll('#bj-actions button')]
                    .some(button => button.textContent.trim() === 'HIT'),
                  stand: [...document.querySelectorAll('#bj-actions button')]
                    .some(button => button.textContent.trim() === 'STAND')
                })"""
            )
            expect(
                "blackjack-hand-restores",
                blackjack_restore["chips"] == 400
                and blackjack_restore["hands"] == 1
                and blackjack_restore["value"] == 17
                and blackjack_restore["phase"] == "player"
                and blackjack_restore["hit"]
                and blackjack_restore["stand"],
                blackjack_restore,
            )

            casino_page.evaluate(
                """() => {
                  R.phase = 'weekend';
                  casinoOpen = true;
                  Object.assign(CASINO, {
                    chips: 380,
                    buyIn: 0,
                    pokerHands: 1,
                    bjHands: 1
                  });
                  PK = {
                    seats: [
                      {
                        pid: null, name: 'You', chips: 380, isYou: true,
                        committed: 20, eliminated: false, folded: false,
                        allin: false, bet: 20,
                        cards: [{r: 14, s: 0}, {r: 13, s: 0}]
                      },
                      {
                        pid: 'karen', name: 'Karen', chips: 780,
                        committed: 20, eliminated: false, folded: false,
                        allin: false, bet: 20, ai: {tight: .65, bluff: .05},
                        cards: [{r: 8, s: 1}, {r: 8, s: 2}]
                      },
                      {
                        pid: 'chad', name: 'CHAD', chips: 980,
                        committed: 20, eliminated: false, folded: false,
                        allin: false, bet: 20, ai: {tight: .3, bluff: .35},
                        cards: [{r: 10, s: 1}, {r: 9, s: 1}]
                      },
                      {
                        pid: 'janet', name: 'Janet', chips: 780,
                        committed: 20, eliminated: false, folded: false,
                        allin: false, bet: 20, ai: {tight: .55, bluff: .12},
                        cards: [{r: 4, s: 2}, {r: 3, s: 3}]
                      }
                    ],
                    deck: [{r: 2, s: 0}, {r: 5, s: 1}],
                    board: [{r: 2, s: 1}, {r: 7, s: 2}, {r: 11, s: 3}],
                    pot: 80,
                    stage: 1,
                    raiseAmt: 100,
                    dealerBtn: 3,
                    toCall: 20,
                    turn: 0,
                    lastAggressor: 3,
                    actedThisRound: new Set([1, 2, 3])
                  };
                  owCasinoView = 'poker';
                  pokerRender('Restore fixture.');
                  pokerActions();
                  owPersistCheckpoint('weekendCasino');
                }"""
            )
            casino_page.reload(wait_until="load", timeout=30_000)
            casino_page.wait_for_function(READY, timeout=15_000)
            casino_page.evaluate("owContinueRun()")
            casino_page.wait_for_function(
                "owCasinoView === 'poker' && PK && document.getElementById('pk-actions')"
            )
            poker_restore = casino_page.evaluate(
                """() => ({
                  chips: CASINO.chips,
                  hands: CASINO.pokerHands,
                  pot: PK.pot,
                  board: PK.board.length,
                  actedSet: PK.actedThisRound instanceof Set,
                  acted: [...PK.actedThisRound],
                  actions: [...document.querySelectorAll('#pk-actions button')]
                    .map(button => button.textContent.trim())
                })"""
            )
            expect(
                "poker-decision-restores",
                poker_restore["chips"] == 380
                and poker_restore["hands"] == 1
                and poker_restore["pot"] == 80
                and poker_restore["board"] == 3
                and poker_restore["actedSet"]
                and poker_restore["acted"] == [1, 2, 3]
                and "CHECK" in poker_restore["actions"],
                poker_restore,
            )
            expect("casino-restore-no-page-errors", not casino_errors, casino_errors)
            casino_context.close()

            guided_context = browser.new_context(
                viewport={"width": 1440, "height": 900},
                reduced_motion="reduce",
            )
            guided_page = guided_context.new_page()
            guided_errors = []
            guided_page.on(
                "pageerror", lambda error: guided_errors.append(str(error))
            )
            load(guided_page, clear=True, tutorial_complete=False)
            guided_page.evaluate("owRequestNewRun()")
            guided_page.wait_for_function(
                """() => R && R.phase === 'floorIntro' &&
                  R.runMode === 'guidedIntern' &&
                  document.querySelector('.guided-intro-briefing') &&
                  !document.getElementById('guided-coordinator')
                    .classList.contains('active')"""
            )
            opening = guided_page.evaluate(
                """() => ({
                  phase:R.phase,
                  floor:R.floor,
                  manager:R.manager.id,
                  runMode:R.runMode,
                  lesson:owGuidedState().lessonId,
                  openingStep:owGuidedState().openingStep,
                  visited:[...owGuidedState().visitedLessons],
                  checkpoint:owReadActiveSave().checkpoint,
                  lessons:OfficeWarsTest.guidedInternLessons().length,
                  copy:document.getElementById(
                    'guided-intro-instruction'
                  )?.textContent,
                  buttons:[...document.querySelectorAll(
                    '.guided-intro-actions button'
                  )].map(button=>button.textContent.trim()),
                  clockCount:[...document.querySelectorAll('button')]
                    .filter(button=>
                      button.textContent.trim()==='CLOCK IN'
                    ).length,
                  verticalOverflow:
                    document.getElementById('overlay-panel').scrollHeight-
                    document.getElementById('overlay-panel').clientHeight,
                  overflowY:getComputedStyle(
                    document.getElementById('overlay-panel')
                  ).overflowY,
                  dockActive:document.getElementById(
                    'guided-coordinator'
                  ).classList.contains('active'),
                  oldUi:[
                    'tutorial-callout',
                    'tutorial-backdrop',
                    'tutorial-focus-ring'
                  ].some(id=>document.getElementById(id))
                })"""
            )
            expect(
                "guided-first-profile-routing",
                opening == {
                    "phase": "floorIntro",
                    "floor": 1,
                    "manager": "guidedCoordinator",
                    "runMode": "guidedIntern",
                    "lesson": "GI-OPEN",
                    "openingStep": 0,
                    "visited": ["GI-OPEN"],
                    "checkpoint": "floorIntro",
                    "lessons": 18,
                    "copy": (
                        "This bar tracks Project Progress (PP) for the floor. "
                        "Each morning you choose a daily task; tasks and "
                        "Workday events add PP here."
                    ),
                    "buttons": ["BACK", "NEXT"],
                    "clockCount": 0,
                    "verticalOverflow": 0,
                    "overflowY": "hidden",
                    "dockActive": False,
                    "oldUi": False,
                },
                opening,
            )
            guided_page.screenshot(
                path=CAPTURES / "visual-guided-intern-desktop.png",
                full_page=True,
            )
            inert = guided_page.evaluate(
                """async () => {
                  const before={
                    project:R.project.progress,
                    cash:R.cash,
                    gameplay:RNG.gameplayState,
                    lesson:owGuidedState().lessonId
                  };
                  const moved=owGuidedOpeningMove(1);
                  await new Promise(resolve=>setTimeout(resolve,100));
                  const step=OfficeWarsTest.guidedInternOpeningSteps()[
                    owGuidedState().openingStep
                  ];
                  const target=document.querySelector(step.target);
                  return {
                    before,
                    after:{
                      project:R.project.progress,
                      cash:R.cash,
                      gameplay:RNG.gameplayState,
                      lesson:owGuidedState().lessonId
                    },
                    moved,
                    openingStep:owGuidedState().openingStep,
                    focused:document.activeElement?.id,
                    highlighted:target?.classList.contains('is-spotlight'),
                    buttons:[...document.querySelectorAll(
                      '.guided-intro-actions button'
                    )].map(button=>button.textContent.trim())
                  };
                }"""
            )
            expect(
                "guided-instruction-controls-are-inert",
                inert["before"] == inert["after"]
                and inert["moved"]
                and inert["openingStep"] == 1
                and inert["focused"] == "guided-intro-next"
                and inert["highlighted"]
                and inert["buttons"] == ["BACK", "NEXT"],
                inert,
            )
            guided_page.wait_for_timeout(250)
            expect(
                "guided-no-instructional-auto-advance",
                guided_page.evaluate(
                    """() => ({
                      lesson:owGuidedState().lessonId,
                      openingStep:owGuidedState().openingStep
                    })"""
                )
                == {"lesson": "GI-OPEN", "openingStep": 1},
                guided_page.evaluate("OfficeWarsTest.guidedInternState()"),
            )

            guided_page.reload(wait_until="load", timeout=30_000)
            guided_page.wait_for_function(READY, timeout=15_000)
            guided_page.evaluate("void owContinueRun()")
            guided_page.wait_for_function(
                """() => R && R.phase === 'floorIntro' &&
                  R.runMode === 'guidedIntern' &&
                  owGuidedState().lessonId === 'GI-OPEN' &&
                  document.querySelector('.guided-intro-briefing') &&
                  !document.getElementById('guided-coordinator')
                    .classList.contains('active')"""
            )
            restored = guided_page.evaluate(
                """() => ({
                  phase:R.phase,
                  runMode:R.runMode,
                  lesson:owGuidedState().lessonId,
                  openingStep:owGuidedState().openingStep,
                  visited:[...owGuidedState().visitedLessons],
                  checkpoint:owReadActiveSave().checkpoint
                })"""
            )
            expect(
                "guided-opening-reloads",
                restored == {
                    "phase": "floorIntro",
                    "runMode": "guidedIntern",
                    "lesson": "GI-OPEN",
                    "openingStep": 1,
                    "visited": ["GI-OPEN"],
                    "checkpoint": "floorIntro",
                },
                restored,
            )
            guided_page.set_viewport_size({"width": 844, "height": 390})
            guided_page.screenshot(
                path=CAPTURES / "visual-guided-intern-landscape.png",
                full_page=True,
            )
            landscape = guided_page.evaluate(
                """() => {
                  const panel=document.querySelector(
                    '.guided-intro-briefing'
                  );
                  const overlayPanel=document.getElementById(
                    'overlay-panel'
                  );
                  const step=OfficeWarsTest.guidedInternOpeningSteps()[
                    owGuidedState().openingStep
                  ];
                  const target=document.querySelector(step.target);
                  const rect=panel.getBoundingClientRect();
                  const targetRect=target.getBoundingClientRect();
                  return {
                    visible:!!panel&&rect.width>0&&rect.height>0,
                    left:rect.left,
                    right:rect.right,
                    top:rect.top,
                    bottom:rect.bottom,
                    width:innerWidth,
                    height:innerHeight,
                    highlighted:target.classList.contains('is-spotlight'),
                    overlap:!(
                      rect.right<=targetRect.left||
                      rect.left>=targetRect.right||
                      rect.bottom<=targetRect.top||
                      rect.top>=targetRect.bottom
                    ),
                    verticalOverflow:
                      overlayPanel.scrollHeight-
                      overlayPanel.clientHeight,
                    overflowY:getComputedStyle(
                      overlayPanel
                    ).overflowY
                  };
                }"""
            )
            expect(
                "guided-landscape-fits-viewport",
                landscape["visible"]
                and landscape["left"] >= -1
                and landscape["right"] <= landscape["width"] + 1
                and landscape["top"] >= -1
                and landscape["bottom"] <= landscape["height"] + 1
                and landscape["highlighted"]
                and not landscape["overlap"]
                and landscape["verticalOverflow"] == 0
                and landscape["overflowY"] == "hidden",
                landscape,
            )

            guided_page.evaluate(
                """() => {
                  const meta=owReadMeta();
                  meta.guidedIntern.completed=true;
                  meta.guidedIntern.replayRequested=false;
                  owWriteMeta(meta);
                  showOptions();
                }"""
            )
            guided_page.click("#options-guided-replay")
            guided_page.wait_for_function(
                """() => document.getElementById('menu-dialog')
                  .classList.contains('open')"""
            )
            replay_warning = guided_page.evaluate(
                """() => ({
                  replayRequested:owReadMeta().guidedIntern.replayRequested,
                  dialog:document.getElementById('menu-dialog-title').textContent,
                  confirm:document.getElementById('menu-dialog-confirm').textContent
                })"""
            )
            expect(
                "guided-replay-uses-replacement-warning",
                replay_warning["replayRequested"]
                and replay_warning["dialog"] == "REPLACE ACTIVE RUN?"
                and replay_warning["confirm"] == "START NEW RUN",
                replay_warning,
            )
            guided_page.click("#menu-dialog-confirm")
            guided_page.wait_for_function(
                """() => R && R.phase === 'floorIntro' &&
                  R.runMode === 'guidedIntern' &&
                  owGuidedState().lessonId === 'GI-OPEN' &&
                  document.querySelector('.guided-intro-briefing')"""
            )
            fresh_replay = guided_page.evaluate(
                """() => ({
                  runMode:R.runMode,
                  lesson:owGuidedState().lessonId,
                  openingStep:owGuidedState().openingStep,
                  visited:[...owGuidedState().visitedLessons],
                  replayRequested:owReadMeta().guidedIntern.replayRequested,
                  oldUi:!!document.getElementById('tutorial-callout')
                })"""
            )
            expect(
                "guided-replay-starts-fresh-real-run",
                fresh_replay == {
                    "runMode": "guidedIntern",
                    "lesson": "GI-OPEN",
                    "openingStep": 0,
                    "visited": ["GI-OPEN"],
                    "replayRequested": False,
                    "oldUi": False,
                },
                fresh_replay,
            )
            expect(
                "guided-persistence-no-page-errors",
                not guided_errors,
                guided_errors,
            )
            guided_context.close()
        finally:
            browser.close()

    print("PERSISTENCE_JSON=" + json.dumps({"checks": checks, "detail": detail}))
    failures = [name for name, passed in checks.items() if not passed]
    if failures:
        print("FAILED=" + ",".join(failures))
        return 1
    print("PASS:PERSISTENCE_AND_TUTORIAL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
