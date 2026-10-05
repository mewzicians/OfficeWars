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
        "save_schema_9": "const OW_SAVE_SCHEMA=9;" in source,
        "meta_schema_6": "const OW_META_SCHEMA=6;" in source,
        "review_checkpoints": all(
            checkpoint in source
            for checkpoint in (
                "'politicsReviewStaging'",
                "'politicsReviewConfirmed'",
                "'politicsReviewSettled'",
                "'roleVote'",
                "'pendingNightDirective'",
                "'floorBriefing'",
                "'tutorialLesson'",
            )
        ),
        "review_shell": 'id="review-confirm"' in source
        and "CONFIRM REVIEW" in source,
        "visible_save_notice": 'id="menu-save-notice"' in source
        and "Settings were preserved." in source,
        "prepared_restore_to_cinematic_queue": (
            "owRunCinematicWorkDay({" in source
            and "skipRequested:true" in source
            and "'workdayPoliticalQueue'" in source
        ),
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

                  localStorage.setItem(OW_META_KEY, JSON.stringify({
                    schema:5,
                    tutorial:{
                      completed:true,nextStep:13,skipped:false,
                      replayRequested:false
                    },
                    settings:{volume:33}
                  }));
                  const migratedMeta = owReadMeta();
                  expect(
                    'meta_migration',
                    migratedMeta.schema === 6 &&
                      migratedMeta.settings.volume === 33 &&
                      migratedMeta.tutorial.completed &&
                      migratedMeta.guidedIntern.required &&
                      !migratedMeta.guidedIntern.completed &&
                      migratedMeta.guidedIntern.version === 1,
                    migratedMeta
                  );

                  localStorage.setItem(OW_SAVE_KEY, JSON.stringify({
                    schema:2,
                    checkpoint:'morning',
                    run:{floor:1,project:{size:45},stats:{}}
                  }));
                  const incompatible = owReadActiveSave();
                  owRenderSaveNotice();
                  const saveNotice =
                    document.getElementById('menu-save-notice').textContent;
                  const metaAfterInvalidation = owReadMeta();
                  expect(
                    'active_save_invalidation',
                    incompatible === null &&
                      !localStorage.getItem(OW_SAVE_KEY) &&
                      saveNotice.includes('retired Home system') &&
                      saveNotice.includes(
                        'Settings and tutorial progress were preserved'
                      ) &&
                      metaAfterInvalidation.settings.volume === 33,
                    {saveNotice,metaAfterInvalidation}
                  );

                  startRun({seed:920002});
                  await startDay();
                  R.todayCard = R.morningCards[0];
                  R.rival.today = {gain:0,workSlots:1};
                  R.cash = 500;
                  R.favors = [{id:'receipts'},{id:'backup'}];
                  R.politicalCharges = {leverage:2};
                  const pages = [
                    {
                      id:'project',
                      type:'project',
                      source:'Project',
                      timelineIndex:0,
                      mandatory:true,
                      legalTargetIds:['bob'],
                      options:[
                        {
                          id:'project-conflict',
                          label:'Conflict',
                          cost:{
                            cash:450,
                            favors:['receipts'],
                            charges:{leverage:2}
                          },
                          targets:['bob']
                        },
                        {
                          id:'project-safe',
                          label:'Safe',
                          cost:{
                            cash:100,
                            favors:['backup'],
                            charges:{leverage:1}
                          },
                          targets:['bob']
                        }
                      ]
                    },
                    {
                      id:'manager',
                      type:'manager',
                      source:'Manager',
                      timelineIndex:5,
                      mandatory:true,
                      legalTargetIds:['alice'],
                      options:[{
                        id:'manager-comply',
                        label:'Comply',
                        cost:{
                          cash:100,
                          favors:['receipts'],
                          charges:{leverage:1}
                        },
                        targets:['alice']
                      }]
                    },
                    {
                      id:'relationship',
                      type:'relationship',
                      source:'Relationship',
                      timelineIndex:2,
                      mandatory:true,
                      options:[{
                        id:'relationship-noop',
                        label:'Take No Action',
                        cost:{cash:0,favors:[],charges:{}}
                      }]
                    }
                  ];
                  OfficeWarsTest.createPoliticsReview(pages,{
                    id:'phase2-transaction'
                  });
                  const emptyReview = OfficeWarsTest.phase2State();
                  expect(
                    'mandatory_pages_start_incomplete',
                    JSON.stringify(
                      R.politicsReview.invalidPages.slice().sort()
                    ) === JSON.stringify(
                      ['manager','project','relationship']
                    ) &&
                      emptyReview.review.status === 'staging',
                    emptyReview.review
                  );

                  OfficeWarsTest.stagePoliticsReviewChoice(
                    'project',
                    {optionId:'project-conflict',rerollSource:'favor:backup'}
                  );
                  OfficeWarsTest.stagePoliticsReviewChoice(
                    'manager',
                    {optionId:'manager-comply'}
                  );
                  OfficeWarsTest.stagePoliticsReviewChoice(
                    'relationship',
                    {optionId:'relationship-noop'}
                  );
                  const conflicted = OfficeWarsTest.phase2State();
                  const conflictedSave = OfficeWarsTest.readSave();
                  expect(
                    'resource_conflict_blocks_confirmation',
                    conflicted.review.invalidPages.includes('manager') &&
                      conflicted.review.reservations.cash === 550 &&
                      conflicted.review.reservations.favors.length === 1 &&
                      conflicted.review.reservations.charges.leverage === 3,
                    conflicted.review
                  );
                  expect(
                    'staging_checkpoint_serializes_edits',
                    conflictedSave.checkpoint === 'politicsReviewStaging' &&
                      conflictedSave.run.politicsReview.choices.project.optionId ===
                        'project-conflict' &&
                      conflictedSave.run.politicsReview.focus.pageId ===
                        'relationship' &&
                      conflictedSave.run.politicsReview.rerolls.project ===
                        'favor:backup',
                    conflictedSave.run.politicsReview
                  );

                  OfficeWarsTest.stagePoliticsReviewChoice(
                    'project',
                    {
                      optionId:'project-safe',
                      targetIds:['bob'],
                      rerollSource:'favor:backup'
                    }
                  );
                  const legal = OfficeWarsTest.phase2State();
                  expect(
                    'legal_reservations',
                    legal.review.invalidPages.length === 0 &&
                      legal.review.reservations.cash === 200 &&
                      JSON.stringify(
                        legal.review.reservations.favors.slice().sort()
                      ) === JSON.stringify(['backup','receipts']) &&
                      legal.review.reservations.charges.leverage === 2 &&
                      JSON.stringify(
                        legal.review.reservations.targets.slice().sort()
                      ) === JSON.stringify(['alice','bob']),
                    legal.review.reservations
                  );
                  OfficeWarsTest.renderPoliticsReview();
                  const shell = {
                    phase:R.phase,
                    pageCount:document.querySelector(
                      '.politics-review-count'
                    ).textContent,
                    confirmDisabled:document.getElementById(
                      'review-confirm'
                    ).disabled,
                    nextDisabled:document.getElementById(
                      'review-next-incomplete'
                    ).disabled
                  };
                  expect(
                    'review_shell_controls',
                    shell.phase === 'politicsReview' &&
                      shell.pageCount === '3 PAGES' &&
                      !shell.confirmDisabled &&
                      shell.nextDisabled,
                    shell
                  );

                  const originalDayResults = dayResults;
                  dayResults = () => { R.phase = 'clockOut'; };
                  await OfficeWarsTest.confirmPoliticsReview();
                  const settled = OfficeWarsTest.phase2State();
                  const frozenBefore = JSON.stringify(settled.review.frozen);
                  const cashBeforeRepeat = R.cash;
                  const favorsBeforeRepeat = JSON.stringify(R.favors);
                  const chargesBeforeRepeat =
                    JSON.stringify(R.politicalCharges);
                  const restageAfterConfirm =
                    OfficeWarsTest.stagePoliticsReviewChoice(
                      'project',
                      {optionId:'project-conflict'}
                    );
                  OfficeWarsTest.settlePoliticsReview();
                  dayResults = originalDayResults;
                  const frozenAfter = JSON.stringify(R.politicsReview.frozen);
                  const settlement =
                    R.settlementLedger[R.politicsReview.settlementId];
                  expect(
                    'confirmation_freezes_transaction',
                    settled.review.confirmed &&
                      settled.review.settled &&
                      frozenBefore === frozenAfter &&
                      restageAfterConfirm === false,
                    {
                      frozen:settled.review.frozen,
                      restageAfterConfirm
                    }
                  );
                  expect(
                    'manager_first_settlement_order',
                    JSON.stringify(
                      settled.review.results.map(result=>result.pageId)
                    ) === JSON.stringify(
                      ['manager','project','relationship']
                    ),
                    settled.review.results
                  );
                  expect(
                    'resources_settle_exactly_once',
                    settled.resources.cash === 300 &&
                      settled.resources.favors.length === 0 &&
                      settled.resources.politicalCharges.leverage === 0 &&
                      R.cash === cashBeforeRepeat &&
                      JSON.stringify(R.favors) === favorsBeforeRepeat &&
                      JSON.stringify(R.politicalCharges) ===
                        chargesBeforeRepeat &&
                      settlement.settled &&
                      settlement.applied,
                    {
                      resources:settled.resources,
                      repeat:{
                        cash:R.cash,
                        favors:R.favors,
                        charges:R.politicalCharges
                      },
                      settlement
                    }
                  );

                  startRun({seed:920003});
                  await startDay();
                  R.todayCard = R.morningCards[0];
                  R.rival.today = {gain:0,workSlots:1};
                  await owEnterPoliticsReview({replace:true});
                  const bridge = OfficeWarsTest.phase2State();
                  const bridgeText =
                    document.getElementById('overlay-panel').textContent;
                  expect(
                    'populated_review_bridge',
                    bridge.phase === 'politicsReview' &&
                      bridge.review.pages.length === 1 &&
                      Object.keys(bridge.review.choices).length === 0 &&
                      !bridge.review.confirmed &&
                      bridgeText.includes('PROJECT') &&
                      !bridgeText.includes('RELATIONSHIP') &&
                      document.getElementById('review-confirm').disabled,
                    {bridge:bridge.review,bridgeText}
                  );

                  R.pendingNightDirective = {
                    id:'night-directive-fixture',
                    status:'pending'
                  };
                  R.roleVoteState = {
                    id:'role-vote-fixture',
                    ballots:['a','b'],
                    settled:false
                  };
                  R.floorBriefingState = {
                    id:'briefing-fixture',
                    projectId:'fixture-project',
                    rosterIds:['a','b'],
                    delegateIds:['a']
                  };
                  R.tutorialLessonState = {
                    id:'tutorial-fixture',
                    lesson:'day-2',
                    targetId:'review-confirm',
                    dialogueId:'coordinator-7'
                  };
                  const deferred = {};
                  for(const checkpoint of [
                    'pendingNightDirective','roleVote',
                    'floorBriefing','tutorialLesson'
                  ]){
                    OfficeWarsTest.saveNow(checkpoint);
                    const saved = OfficeWarsTest.readSave();
                    deferred[checkpoint] = {
                      checkpoint:saved.checkpoint,
                      pendingNightDirective:
                        saved.run.pendingNightDirective,
                      roleVoteState:saved.run.roleVoteState,
                      floorBriefingState:saved.run.floorBriefingState,
                      tutorialLessonState:saved.run.tutorialLessonState
                    };
                  }
                  expect(
                    'deferred_boundaries_serialize',
                    Object.entries(deferred).every(
                      ([checkpoint,value]) =>
                        value.checkpoint === checkpoint &&
                        value.pendingNightDirective.id ===
                          'night-directive-fixture' &&
                        value.roleVoteState.id === 'role-vote-fixture' &&
                        value.floorBriefingState.id ===
                          'briefing-fixture' &&
                        value.tutorialLessonState.id ===
                          'tutorial-fixture'
                    ),
                    deferred
                  );

                  const contract = OfficeWarsTest.phase2State();
                  expect(
                    'phase2_contract',
                    contract.saveSchema === 9 &&
                      contract.metaSchema === 6 &&
                      [
                        'politicsReviewStaging',
                        'politicsReviewConfirmed',
                        'politicsReviewSettled',
                        'workdayPoliticalChoice',
                        'workdayPoliticalQueue',
                        'politicsResultsReel',
                        'roleVote',
                        'pendingNightDirective',
                        'floorBriefing',
                        'tutorialLesson'
                      ].every(id=>contract.checkpoints.includes(id)),
                    contract
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
    print(f"PASS phase2 {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
