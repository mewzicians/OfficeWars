import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))

from playwright.sync_api import sync_playwright


GAME = ROOT / "officewarsautobattler.html"
GAME_URL = GAME.as_uri()
READY = "document.documentElement.dataset.officewarsReady === 'true'"


def main():
    source = GAME.read_text(encoding="utf-8")
    static = {
        "fixed_rank_curve": all(
            token in source
            for token in (
                "deadline:3, size:45",
                "deadline:5, size:80",
                "deadline:5, size:115",
                "deadline:5, size:155",
                "deadline:5, size:205",
                "deadline:5, size:265",
                "deadline:5, size:330",
            )
        ),
        "old_chad_ai_removed": "RIVAL_AI" not in source
        and "Current stacks" not in source
        and "Accumulated upgrades" not in source,
        "save_schema_9": "const OW_SAVE_SCHEMA=9;" in source,
        "payout_checkpoint": "'overdeliveryPayout'" in source,
        "weekday_hud": 'id="sp-weekday"' in source
        and 'id="sp-overtime"' in source,
    }

    page_errors = []
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
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.on("pageerror", lambda error: page_errors.append(str(error)))
            page.goto(GAME_URL, wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            runtime = page.evaluate(
                """async () => {
                  localStorage.clear();
                  const checks = {};
                  const evidence = {};
                  const expect = (name, value, detail) => {
                    checks[name] = !!value;
                    evidence[name] = detail;
                  };
                  const near = (a, b) => Math.abs(a - b) < 1e-7;

                  expect(
                    'rank_curve',
                    JSON.stringify(RANKS.map(r => [r.deadline, r.size, r.chadTargetDay])) ===
                      JSON.stringify([
                        [3,45,3],[5,80,4],[5,115,4],[5,155,4],
                        [5,205,4],[5,265,4],[5,330,4]
                      ]),
                    RANKS.map(r => ({
                      deadline:r.deadline,size:r.size,chadTargetDay:r.chadTargetDay
                    }))
                  );

                  startRun({seed: 910001});
                  expect(
                    'intern_calendar',
                    R.floor === 1 && R.project.size === 45 &&
                      R.daysLeft === 3 && dayName() === 'WED',
                    OfficeWarsTest.phase1State()
                  );
                  let pace = owChadPaceBreakdown();
                  expect(
                    'intern_chad_friday',
                    near(pace.base, 15) && near(pace.gain, 15) &&
                      owChadExpectedFinish() === 'FRI',
                    {pace, finish:owChadExpectedFinish()}
                  );

                  R.project.completionPending = false;
                  R.project.locked = false;
                  R.overtimeBank = 0;
                  R.daysLeft = 3;
                  const overtime = [
                    owAddOvertimeDay('Fixture A'),
                    owAddOvertimeDay('Fixture B'),
                    owAddOvertimeDay('Fixture C')
                  ];
                  expect(
                    'overtime_cap',
                    JSON.stringify(overtime) === JSON.stringify([true,true,false]) &&
                      R.overtimeBank === 2 && owFloorTotalDays() === 5,
                    {overtime,bank:R.overtimeBank,total:owFloorTotalDays()}
                  );

                  const setRace = (player, chad, day, overtimeBank=0) => {
                    R.floor = 1;
                    R.day = day;
                    R.overtimeBank = overtimeBank;
                    R.stress = 0;
                    R.project = {
                      name:'Fixture',baseSize:45,size:45,completionTarget:45,
                      progress:player,completionPending:player >= 45,
                      locked:false,completionDay:player >= 45 ? day : null,
                      lockDay:null
                    };
                    R.overdelivery = {
                      active:player >= 45,activationPending:false,target:45,
                      tiers:0,paid:false,payoutChoice:null
                    };
                    R.rival.progress = chad;
                    owRefreshDaysLeft();
                    return owClockOutVerdict();
                  };
                  expect(
                    'same_day_player_tie',
                    setRace(45,45,3) === 'promotion' && R.project.locked,
                    {verdict:R.project.locked, state:OfficeWarsTest.phase1State()}
                  );
                  expect(
                    'chad_first_defeat',
                    setRace(44,45,2) === 'rival',
                    {player:R.project.progress,chad:R.rival.progress}
                  );
                  expect(
                    'early_lock_continues',
                    setRace(45,0,1) === 'locked' && R.project.lockDay === 1,
                    OfficeWarsTest.phase1State()
                  );
                  expect(
                    'sunday_failure',
                    setRace(44,0,5,2) === 'fired',
                    OfficeWarsTest.phase1State()
                  );

                  R.floor = 1;
                  R.day = 1;
                  R.project = {
                    name:'Chain',baseSize:100,size:100,completionTarget:100,
                    progress:95,completionPending:false,locked:false
                  };
                  R.overdelivery = {
                    active:false,activationPending:false,target:100,
                    tiers:0,paid:false,payoutChoice:null
                  };
                  owProjectResolutionDepth = 0;
                  owBeginProjectResolution();
                  const crossing = owAddProjectProgress(10,{base:true,source:'Fixture'});
                  const deferred = R.project.completionPending &&
                    !R.overdelivery.active && R.overdelivery.activationPending;
                  owEndProjectResolution('Fixture');
                  const scaled = owAddProjectProgress(10,{base:true,source:'Fixture after'});
                  expect(
                    'chain_activation_and_base_scaling',
                    near(crossing,10) && deferred && R.overdelivery.active &&
                      near(scaled,2) && near(R.project.progress,107),
                    {crossing,deferred,scaled,progress:R.project.progress,over:R.overdelivery}
                  );

                  R.commit = 0;
                  R.codebase = 0;
                  R.polish = {};
                  R.cardCompletions = {};
                  R.house = [];
                  R.home = 'apartment';
                  const readme = {
                    task:TASK_BY_ID.get('readmeUpdate'),
                    rarity:'common',
                    modifiers:{}
                  };
                  const preview = owCardPreview(readme,{primary:true});
                  expect(
                    'task_base_scaling',
                    near(preview.progress,2) && near(preview.rawStress,1.8),
                    preview
                  );
                  expect(
                    'ordinary_action_base_scaling',
                    near(workActionPts(),1) && near(owOrdinaryBaseStress(10),2),
                    {work:workActionPts(),stress:owOrdinaryBaseStress(10)}
                  );

                  R.project.progress = 150;
                  R.overdelivery.target = 100;
                  R.overdelivery.active = true;
                  const totals = owOverdeliveryRewardTotals();
                  expect(
                    'tier_formula',
                    totals.tiers === 5 && totals.cash === 1500 &&
                      totals.recovery === 40,
                    totals
                  );
                  R.phase = 'clockOut';
                  R.floorCompleted = true;
                  R.cash = 100;
                  R.stats.cashEarned = 0;
                  const priorResolver = owAutomatedChoiceResolver;
                  owAutomatedChoiceResolver = () => 0;
                  await owResolveOverdeliveryPayout();
                  const firstPayout = {
                    cash:R.cash,
                    cashEarned:R.stats.cashEarned,
                    paid:R.overdelivery.paid,
                    choice:R.overdelivery.payoutChoice,
                    expectation:Object.assign({},R.expectationNext),
                    save:OfficeWarsTest.readSave()
                  };
                  await owResolveOverdeliveryPayout();
                  const secondCash = R.cash;
                  await owContinueRun();
                  const restoredPayout = {
                    phase:R.phase,
                    cash:R.cash,
                    paid:!!(R.overdelivery&&R.overdelivery.paid),
                    choice:R.overdelivery&&R.overdelivery.payoutChoice
                  };
                  owAutomatedChoiceResolver = priorResolver;
                  expect(
                    'payout_exactly_once',
                    firstPayout.cash === 1600 &&
                      firstPayout.cashEarned === 1500 &&
                      firstPayout.paid &&
                      firstPayout.choice === 'cash' &&
                      near(firstPayout.expectation.sizePct,.5) &&
                      near(firstPayout.expectation.chadPct,.5) &&
                      firstPayout.save &&
                      firstPayout.save.checkpoint === 'overdeliveryPayout' &&
                      firstPayout.save.run.overdelivery.paid &&
                      secondCash === 1600 &&
                      restoredPayout.phase === 'night' &&
                      restoredPayout.cash === 1600 &&
                      restoredPayout.paid &&
                      restoredPayout.choice === 'cash',
                    {firstPayout,secondCash,restoredPayout}
                  );

                  R.rival.progress = 20;
                  R.rival.directSubtraction = 0;
                  const removed = owSubtractChadProgress(7,'Fixture');
                  expect(
                    'chad_subtraction',
                    removed === 7 && R.rival.progress === 13 &&
                      R.rival.directSubtraction === 7,
                    {removed,progress:R.rival.progress,total:R.rival.directSubtraction}
                  );

                  R.floor = 1;
                  R.expectationNext = {sizePct:.2,chadPct:.2};
                  R.closingRewards = [];
                  nextFloor();
                  R.day = 1;
                  updateHUD();
                  pace = owChadPaceBreakdown();
                  expect(
                    'expectation_order_and_chad_pace',
                    R.floor === 2 && R.project.size === 96 &&
                      near(pace.base,24) && near(pace.gain,28.8),
                    {floor:R.floor,size:R.project.size,pace}
                  );
                  expect(
                    'weekday_and_hud',
                    dayName() === 'MON' &&
                      document.getElementById('sp-weekday').textContent === 'MON' &&
                      document.getElementById('sp-overtime').textContent === 'OT 0/2',
                    {
                      dayName:dayName(),
                      weekday:document.getElementById('sp-weekday').textContent,
                      overtime:document.getElementById('sp-overtime').textContent
                    }
                  );
                  expect(
                    'transparent_chad_state',
                    !('stacks' in R.rival) && !('upgrades' in R.rival) &&
                      !('upgBonus' in R.rival),
                    R.rival
                  );
                  expect(
                    'save_contract',
                    OW_SAVE_SCHEMA === 9 &&
                      OW_STABLE_CHECKPOINTS.has('overdeliveryPayout') &&
                      OW_STABLE_CHECKPOINTS.has('workdayPoliticalChoice') &&
                      OW_STABLE_CHECKPOINTS.has('homeTransaction') &&
                      OW_STABLE_CHECKPOINTS.has('homeSetup') &&
                      OW_STABLE_CHECKPOINTS.has('homePrepareTomorrow') &&
                      OW_STABLE_CHECKPOINTS.has('workdayPoliticalQueue') &&
                      OW_STABLE_CHECKPOINTS.has('politicsResultsReel') &&
                      !owValidateSave({
                        schema:1,checkpoint:'morning',
                        run:{floor:1,project:{},stats:{}}
                      }),
                    {schema:OW_SAVE_SCHEMA,checkpoints:[...OW_STABLE_CHECKPOINTS]}
                  );
                  R.floorCompleted = false;
                  const noWeekend = !weekendDue();
                  R.floorCompleted = true;
                  const floorWeekend = weekendDue();
                  expect(
                    'floor_weekend_routing',
                    noWeekend && floorWeekend,
                    {noWeekend,floorWeekend}
                  );

                  return {checks,evidence};
                }"""
            )
        finally:
            browser.close()

    checks = {**static, **runtime["checks"], "no_page_errors": not page_errors}
    detail = {
        "static": static,
        "runtime": runtime["evidence"],
        "page_errors": page_errors,
    }
    failed = [name for name, passed in checks.items() if not passed]
    print(json.dumps({"checks": checks, "detail": detail}, indent=2))
    if failed:
        print("FAILED=" + ",".join(failed))
        raise SystemExit(1)
    print(f"PASS phase1 {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
