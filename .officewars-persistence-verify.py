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
        "schema": 1,
        "tutorial": {
            "completed": True,
            "nextStep": 6,
            "skipped": False,
            "replayRequested": False,
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
                  hidden: document.getElementById('menu-continue').hidden
                })"""
            )
            expect(
                "corrupt-save-discarded",
                corrupt["removed"] and corrupt["hidden"],
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
                  hidden: document.getElementById('menu-continue').hidden
                })"""
            )
            expect(
                "incompatible-save-discarded",
                incompatible["removed"] and incompatible["hidden"],
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
                page.evaluate(
                    "(raw) => localStorage.setItem(OW_SAVE_KEY, raw)", prepared_raw
                )
                page.reload(wait_until="load", timeout=30_000)
                page.wait_for_function(READY, timeout=15_000)
                page.evaluate("owContinueRun()")
                wait_phase(page, "clockOut")
                return page.evaluate(
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

            first_restore = restore_prepared()
            second_restore = restore_prepared()
            expect(
                "prepared-workday-deterministic-restore",
                first_restore == second_restore,
                {"first": first_restore, "second": second_restore},
            )
            expect(
                "task-reward-not-duplicated",
                first_restore["codingXp"] == 1 and first_restore["plays"] == 1,
                first_restore,
            )

            page.evaluate("afterDayResults()")
            wait_phase(page, "night")
            page.evaluate(
                """() => {
                  owToggleLightsOut(true);
                  nightSwitchTab('relationships');
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
                  overlay: document.getElementById('overlay').classList.contains('active')
                })"""
            )
            expect(
                "night-state-restore",
                night_restore["lightsOut"]
                and night_restore["tab"] == "relationships"
                and night_restore["overlay"],
                night_restore,
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

            tutorial_context = browser.new_context(
                viewport={"width": 1440, "height": 900}
            )
            tutorial_page = tutorial_context.new_page()
            tutorial_errors = []
            tutorial_page.on(
                "pageerror", lambda error: tutorial_errors.append(str(error))
            )
            load(tutorial_page, clear=True, tutorial_complete=False)
            tutorial_page.evaluate("owRequestNewRun()")
            tutorial_page.wait_for_function(
                "document.getElementById('tutorial-callout').classList.contains('active')"
            )
            tutorial_page.screenshot(
                path=ROOT / ".visual-tutorial-desktop.png", full_page=True
            )
            titles = [
                tutorial_page.text_content("#tutorial-title"),
            ]
            tutorial_page.click("#tutorial-next")
            tutorial_page.set_viewport_size({"width": 844, "height": 390})
            tutorial_page.evaluate("owClockIn()")
            wait_phase(tutorial_page, "morning")
            tutorial_page.wait_for_function(
                "document.getElementById('tutorial-callout').classList.contains('active')"
            )
            tutorial_page.screenshot(
                path=ROOT / ".visual-tutorial-landscape.png", full_page=True
            )
            titles.append(tutorial_page.text_content("#tutorial-title"))
            tutorial_page.click("#tutorial-next")
            tutorial_page.wait_for_function(
                "document.getElementById('tutorial-callout').classList.contains('active')"
            )
            titles.append(tutorial_page.text_content("#tutorial-title"))
            tutorial_page.click("#tutorial-next")
            tutorial_page.evaluate(
                """() => {
                  const task = TASK_BY_ID.get('regressionTests');
                  R.morningCards = [{
                    task,
                    rarity: task.rarity,
                    source: 'offer',
                    modifiers: {}
                  }];
                  renderMorningUI();
                  selectMorning(0, 'offer');
                  void confirmMorning();
                }"""
            )
            tutorial_page.wait_for_function(
                "document.getElementById('tutorial-title').textContent === 'LET THE OFFICE WORK'",
                timeout=30_000,
            )
            titles.append(tutorial_page.text_content("#tutorial-title"))
            tutorial_page.click("#tutorial-next")
            wait_phase(tutorial_page, "workday")
            tutorial_page.evaluate("skipWorkDay()")
            tutorial_page.wait_for_function(
                "document.getElementById('tutorial-title').textContent === 'REVIEW CLOCK OUT'",
                timeout=30_000,
            )
            titles.append(tutorial_page.text_content("#tutorial-title"))
            tutorial_page.click("#tutorial-next")
            tutorial_page.evaluate("afterDayResults()")
            wait_phase(tutorial_page, "night")
            tutorial_page.wait_for_function(
                "document.getElementById('tutorial-title').textContent === 'PLAN THE NIGHT'",
                timeout=30_000,
            )
            titles.append(tutorial_page.text_content("#tutorial-title"))
            tutorial_page.click("#tutorial-next")
            tutorial_meta = tutorial_page.evaluate("OfficeWarsTest.meta()")
            expected_titles = [
                "THE PROJECT RACE",
                "CHOOSE TODAY'S TASK",
                "BUILD YOUR RESUME",
                "LET THE OFFICE WORK",
                "REVIEW CLOCK OUT",
                "PLAN THE NIGHT",
            ]
            expect(
                "six-step-orientation",
                titles == expected_titles
                and tutorial_meta["tutorial"]["completed"]
                and tutorial_meta["tutorial"]["nextStep"] == 6,
                {"titles": titles, "meta": tutorial_meta},
            )

            tutorial_page.evaluate(
                """() => {
                  localStorage.removeItem(OW_SAVE_KEY);
                  localStorage.removeItem(OW_META_KEY);
                  owReturnToMainMenu();
                  owRequestNewRun();
                }"""
            )
            tutorial_page.wait_for_function(
                "document.getElementById('tutorial-callout').classList.contains('active')"
            )
            tutorial_page.click(
                "#tutorial-callout button",
                position={"x": 10, "y": 10},
            )
            skipped_meta = tutorial_page.evaluate("OfficeWarsTest.meta()")
            expect(
                "orientation-skip-persists",
                skipped_meta["tutorial"]["completed"]
                and skipped_meta["tutorial"]["skipped"],
                skipped_meta,
            )
            replay_meta = tutorial_page.evaluate(
                """() => {
                  owRequestOrientationReplay();
                  return OfficeWarsTest.meta();
                }"""
            )
            expect(
                "orientation-replay-reset",
                not replay_meta["tutorial"]["completed"]
                and replay_meta["tutorial"]["nextStep"] == 0
                and replay_meta["tutorial"]["replayRequested"],
                replay_meta,
            )
            expect(
                "tutorial-no-page-errors", not tutorial_errors, tutorial_errors
            )
            tutorial_context.close()
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
