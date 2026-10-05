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
        "seven_project_briefs": "const OW_PROJECT_BRIEFS=[" in source,
        "twenty_one_directives": "const OW_DIRECTIVE_TEMPLATES=[" in source,
        "fifteen_boss_schemes": "const OW_BOSS_SCHEMES=[" in source,
        "approval_states": all(
            label in source
            for label in (
                "Vindictive Rage",
                "Petty Scrutiny",
                "Professionally Neutral",
                "Suspiciously Pleased",
                "Shameless Favorite",
            )
        ),
        "generic_hostile_injection_removed": "slots[hostileIdx()]" not in source,
        "review_results_surface": "OFFICE POLITICS · RESULTS" in source
        and 'id="review-results-continue"' in source,
    }

    page_errors = []
    responsive = {}
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

                  const briefShape = OW_PROJECT_BRIEFS.map(item => ({
                    id:item.id,
                    dilemmas:item.dilemmaTitles.length,
                    stakeholders:item.stakeholders.length,
                    favored:item.favored,
                    adversarial:item.adversarial
                  }));
                  expect(
                    'project_brief_inventory',
                    OW_PROJECT_BRIEFS.length === 7 &&
                      OW_PROJECT_BRIEFS.every(item =>
                        item.dilemmaTitles.length === 5 &&
                        item.stakeholders.length === 2 &&
                        item.favored !== item.adversarial
                      ) &&
                      OW_OVERDELIVERY_SCENES.length === 5,
                    {
                      briefs:briefShape,
                      overdeliveryScenes:OW_OVERDELIVERY_SCENES.map(
                        item=>item.id
                      )
                    }
                  );

                  const categoryCounts = {};
                  OW_DIRECTIVE_TEMPLATES.forEach(item => {
                    categoryCounts[item.category] =
                      (categoryCounts[item.category] || 0) + 1;
                  });
                  expect(
                    'directive_inventory',
                    OW_DIRECTIVE_TEMPLATES.length === 21 &&
                      Object.keys(categoryCounts).length === 7 &&
                      Object.values(categoryCounts).every(value=>value === 3) &&
                      new Set(
                        OW_DIRECTIVE_TEMPLATES.map(item=>item.id)
                      ).size === 21,
                    categoryCounts
                  );

                  const bossCounts = {};
                  OW_BOSS_SCHEMES.forEach(item => {
                    bossCounts[item.floor] =
                      (bossCounts[item.floor] || 0) + 1;
                  });
                  expect(
                    'boss_inventory',
                    OW_BOSS_SCHEMES.length === 15 &&
                      bossCounts[3] === 5 &&
                      bossCounts[5] === 5 &&
                      bossCounts[7] === 5 &&
                      new Set(OW_BOSS_SCHEMES.map(item=>item.id)).size === 15,
                    bossCounts
                  );

                  startRun({seed:930001});
                  await startDay();
                  const initial = OfficeWarsTest.phase3State();
                  expect(
                    'floor_start_state',
                    initial.approval.value === 2 &&
                      initial.approval.label ===
                        'Professionally Neutral' &&
                      initial.projectPolitics.stakeholders.length === 2 &&
                      initial.projectPolitics.stakeholders[0].player === 60 &&
                      initial.projectPolitics.stakeholders[1].chad === 60 &&
                      !!initial.directive &&
                      !initial.manager.never.includes(
                        initial.directive.category
                      ),
                    initial
                  );

                  const originalManager = R.manager;
                  const passive = {};
                  R.manager = MANAGERS.find(item=>item.id === 'micro');
                  R.managerApproval = 0;
                  passive.microVindictive = owManagerGeneratedCardCount(3);
                  R.managerApproval = 2;
                  passive.microNeutral = owManagerGeneratedCardCount(3);
                  R.managerApproval = 4;
                  passive.microFavorite = owManagerGeneratedCardCount(3);

                  R.manager = MANAGERS.find(item=>item.id === 'slave');
                  R.managerApproval = 0;
                  passive.slaveVindictive = owManagerDailyStress();
                  R.managerApproval = 2;
                  passive.slaveNeutral = owManagerDailyStress();
                  R.managerApproval = 4;
                  passive.slaveFavorite = owManagerDailyStress();

                  R.manager = MANAGERS.find(item=>item.id === 'penny');
                  R.managerApproval = 0;
                  passive.pennyVindictive = owManagerPayAdjustment();
                  R.managerApproval = 2;
                  passive.pennyNeutral = owManagerPayAdjustment();
                  R.managerApproval = 4;
                  passive.pennyFavorite = owManagerPayAdjustment();

                  R.manager = MANAGERS.find(item=>item.id === 'absent');
                  R.managerApproval = 0;
                  passive.absentVindictive = owManagerPayAdjustment();
                  R.managerApproval = 2;
                  passive.absentNeutral = owManagerPayAdjustment();
                  R.managerApproval = 4;
                  passive.absentFavorite = owManagerPayAdjustment();

                  R.manager = MANAGERS.find(item=>item.id === 'toxic');
                  R.managerApproval = 0;
                  passive.toxicVindictive = owManagerRelationshipLoss(1);
                  R.managerApproval = 2;
                  passive.toxicNeutral = owManagerRelationshipLoss(1);
                  R.managerApproval = 4;
                  passive.toxicFavorite = owManagerRelationshipLoss(1);
                  R.manager = originalManager;
                  R.managerApproval = 2;
                  expect(
                    'manager_extreme_riders',
                    JSON.stringify(passive) === JSON.stringify({
                      microVindictive:1,
                      microNeutral:2,
                      microFavorite:3,
                      slaveVindictive:2,
                      slaveNeutral:1,
                      slaveFavorite:0,
                      pennyVindictive:-100,
                      pennyNeutral:-50,
                      pennyFavorite:0,
                      absentVindictive:-50,
                      absentNeutral:0,
                      absentFavorite:50,
                      toxicVindictive:3,
                      toxicNeutral:2,
                      toxicFavorite:1
                    }),
                    passive
                  );

                  const approvalBeforeAir = R.managerApproval;
                  R.closingRewards = ['executiveAirCover'];
                  const airBefore = owApprovalValue();
                  const blockedLoss = owAdjustManagerApproval(
                    -1,
                    'Air Cover fixture'
                  );
                  expect(
                    'executive_air_cover',
                    airBefore === 4 &&
                      blockedLoss === 0 &&
                      owApprovalValue() === 4 &&
                      R.managerApproval === approvalBeforeAir,
                    {
                      airBefore,
                      blockedLoss,
                      storedApproval:R.managerApproval
                    }
                  );
                  R.closingRewards = [];

                  R.projectPolitics = owCreateProjectPolitics();
                  R.today.primaryPoliticsApplied = false;
                  R.today.primaryPolitics = null;
                  const favoredTask = TASKS.find(
                    item=>item.family === R.projectPolitics.favored
                  );
                  owApplyPrimaryProjectPolitics({
                    task:favoredTask,
                    rarity:favoredTask.rarity,
                    modifiers:{}
                  });
                  const favored = cloneForTest(R.today.primaryPolitics);

                  R.today.primaryPoliticsApplied = false;
                  R.today.primaryPolitics = null;
                  R.managerApproval = 2;
                  R.projectPolitics = owCreateProjectPolitics();
                  const adversarialTask = TASKS.find(
                    item=>item.family === R.projectPolitics.adversarial
                  );
                  owApplyPrimaryProjectPolitics({
                    task:adversarialTask,
                    rarity:adversarialTask.rarity,
                    modifiers:{}
                  });
                  const adversarial = {
                    politics:cloneForTest(R.today.primaryPolitics),
                    approval:R.managerApproval,
                    stakeholders:cloneForTest(
                      R.projectPolitics.stakeholders
                    )
                  };
                  expect(
                    'favored_and_adversarial_primary',
                    favored.favored &&
                      !favored.adversarial &&
                      adversarial.politics.adversarial &&
                      adversarial.approval === 1 &&
                      adversarial.stakeholders[0].chad === 45 &&
                      adversarial.stakeholders[1].chad === 65,
                    {favored,adversarial}
                  );

                  R.managerApproval = 4;
                  R.today.primaryPolitics = {
                    family:R.projectPolitics.favored,
                    favored:true,
                    adversarial:false
                  };
                  R.today.primaryPoliticsApplied = true;
                  R.today.managerDirective =
                    OW_DIRECTIVE_BY_ID.get('DIR-OUT-01');
                  R.today.managerQuota = 0;
                  R.today.actionHistory = [
                    {kind:'work',positive:true},
                    {kind:'work',positive:true}
                  ];
                  R.today.positiveActionTypes = ['work','meeting','mad'];
                  R.today.pts = 20;
                  R.project.progress =
                    R.today.startProjectProgress + 20;
                  R.floorRoster.coworkers['INT-WIL'].sceneQueue = ['ordinary'];
                  const review = owCreatePoliticsReview(
                    owBuildPoliticsReviewPages(),
                    {id:'phase3-review'}
                  );
                  R.phase = 'politicsReview';
                  owRebuildReviewReservations(review);
                  const reviewShape = {
                    pages:review.pages.map(item=>({
                      id:item.id,
                      type:item.type,
                      options:item.options.length
                    })),
                    invalid:review.invalidPages.slice(),
                    managerPresent:review.pages.some(
                      item=>item.type === 'manager'
                    ),
                    projectOdds:owReviewOptionOdds(
                      review.pages.find(item=>item.type === 'project'),
                      review.pages.find(
                        item=>item.type === 'project'
                      ).options[0]
                    )
                  };
                  expect(
                    'review_page_contract',
                    review.pages.length === 2 &&
                      review.pages.map(item=>item.type).join(',') ===
                        'project,relationship' &&
                      review.pages.every(item =>
                        item.options.length >= 3 &&
                        item.options.some(option =>
                          Number(option.cost.cash || 0) === 0
                        )
                      ) &&
                      !reviewShape.managerPresent &&
                      reviewShape.projectOdds === 100,
                    reviewShape
                  );

                  const projectPage = review.pages.find(
                    item=>item.type === 'project'
                  );
                  const relationshipPage = review.pages.find(
                    item=>item.type === 'relationship'
                  );
                  owStagePoliticsReviewChoice(
                    projectPage.id,
                    projectPage.options.find(
                      item=>item.label.includes('Solution')
                    ).id
                  );
                  owStagePoliticsReviewChoice(
                    relationshipPage.id,
                    relationshipPage.options[0].id
                  );
                  const originalDayResults = dayResults;
                  dayResults = () => { R.phase = 'clockOut'; };
                  await owConfirmPoliticsReviewUnlocked({headless:false});
                  const settledReview = cloneForTest(R.politicsReview);
                  const phaseAfterConfirm = R.phase;
                  const resultsText =
                    document.getElementById('overlay-panel').textContent;
                  const projectAfterFirst = R.project.progress;
                  owSettlePoliticsReview({headless:false});
                  const projectAfterRepeat = R.project.progress;
                  owContinueFromPoliticsReviewUnlocked();
                  const phaseAfterContinue = R.phase;
                  dayResults = originalDayResults;
                  expect(
                    'review_freeze_results_and_exactly_once',
                    settledReview.confirmed &&
                      settledReview.settled &&
                      !!settledReview.frozen.odds &&
                      settledReview.results.map(
                        item=>item.pageId
                      ).join(',') ===
                        'review-project,review-relationship' &&
                      phaseAfterConfirm === 'politicsReviewSettled' &&
                      resultsText.includes('OFFICE POLITICS · RESULTS') &&
                      projectAfterFirst === projectAfterRepeat &&
                      phaseAfterContinue === 'clockOut',
                    {
                      settledReview,
                      phaseAfterConfirm,
                      projectAfterFirst,
                      projectAfterRepeat,
                      phaseAfterContinue
                    }
                  );

                  startRun({seed:930002});
                  await startDay();
                  R.today.managerDirective =
                    OW_DIRECTIVE_BY_ID.get('DIR-COLL-03');
                  R.today.managerPackageAssignments = {'offer:0':'comply'};
                  const nightCard = R.morningCards[0];
                  const committedNightPackage = owCommitManagerPackage(
                    nightCard,
                    0,
                    'offer'
                  );
                  const pending = cloneForTest(R.pendingNightDirective);
                  nightState = {
                    outingUsed:true,
                    recPicked:false,
                    homeUsed:0,
                    dealUsed:0,
                    startCash:R.cash,
                    startCredit:R.expenseCredit || 0
                  };
                  R.phase = 'night';
                  R.managerApproval = 3;
                  R.stress = 10;
                  const approvalBeforeNight = owApprovalValue();
                  const firstNight = owSettlePendingNightDirective();
                  const approvalAfterFirst = owApprovalValue();
                  const stressAfterFirst = R.stress;
                  const secondNight = owSettlePendingNightDirective();
                  dayResults = originalDayResults;
                  expect(
                    'night_directive_exactly_once',
                    pending &&
                      committedNightPackage &&
                      pending.directiveId === 'DIR-COLL-03' &&
                      firstNight.met &&
                      firstNight.objectiveStatus === 'complete' &&
                      firstNight.success &&
                      !('finalOdds' in firstNight) &&
                      approvalAfterFirst ===
                        Math.min(4,approvalBeforeNight + 1) &&
                      stressAfterFirst === 7 &&
                      secondNight === null &&
                      R.pendingNightDirective === null &&
                      Object.values(R.settlementLedger).some(
                        item=>item.id.startsWith('manager-night:') &&
                          item.settled
                      ),
                    {
                      pending,
                      firstNight,
                      secondNight,
                      approvalBeforeNight,
                      approvalAfterFirst,
                      stressAfterFirst,
                      ledger:R.settlementLedger
                    }
                  );

                  const bossEvidence = {};
                  for(const floor of [3,5,7]){
                    R.floor = floor;
                    R.bossState = owCreateBossState();
                    const draws = [];
                    for(let index=0;index<6;index++){
                      draws.push(owDrawBossScheme().id);
                    }
                    bossEvidence[floor] = draws;
                  }
                  R.floor = 5;
                  R.projectPolitics = {
                    stakeholders:[
                      {player:40,chad:60},
                      {player:60,chad:40}
                    ]
                  };
                  const managerScheme =
                    OW_BOSS_SCHEMES.find(item=>item.floor === 5);
                  const fullClient = owBossAbsorbEffects(
                    managerScheme,
                    false,
                    false
                  );
                  const halfClient = owBossAbsorbEffects(
                    managerScheme,
                    false,
                    true
                  );
                  expect(
                    'boss_draws_and_mechanics',
                    [3,5,7].every(floor =>
                      new Set(bossEvidence[floor].slice(0,5)).size === 5 &&
                      bossEvidence[floor][5] !==
                        bossEvidence[floor][4]
                    ) &&
                      fullClient[0].amount === .05 &&
                      halfClient[0].amount === .025,
                    {
                      draws:bossEvidence,
                      fullClient,
                      halfClient
                    }
                  );

                  R.floor = 1;
                  R.manager = MANAGERS.find(item=>item.id === 'hawk');
                  R.managerApproval = 2;
                  R.managerNextChadPct = 0;
                  R.today.managerQuota = 25;
                  R.today.managerQuotaSettled = false;
                  R.today.startProjectProgress = 0;
                  R.project.progress = 10;
                  R.today.pts = 0;
                  const firstQuota = owSettleHawkQuota();
                  const secondQuota = owSettleHawkQuota();
                  expect(
                    'deadline_hawk_quota_once',
                    R.managerApproval === 1 &&
                      R.managerNextChadPct === .10 &&
                      firstQuota.includes('missed') &&
                      secondQuota === null,
                    {
                      approval:R.managerApproval,
                      nextPct:R.managerNextChadPct,
                      firstQuota,
                      secondQuota
                    }
                  );

                  return {checks,evidence};
                }"""
            )
            for name, width, height in (
                ("desktop", 1440, 900),
                ("landscape", 844, 390),
            ):
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    reduced_motion="reduce",
                )
                review_page = context.new_page()
                review_page.goto(GAME_URL, wait_until="load", timeout=30_000)
                review_page.wait_for_function(READY, timeout=15_000)
                review_page.evaluate(
                    """async () => {
                      localStorage.clear();
                      startRun({seed:930100});
                      await startDay();
                      R.floorRoster.coworkers['INT-WIL'].sceneQueue =
                        ['ordinary'];
                      R.todayCard = R.morningCards[0];
                      R.rival.today = {gain:0,workSlots:1};
                      await owEnterPoliticsReview({replace:true});
                    }"""
                )
                responsive[name] = review_page.evaluate(
                    """() => {
                      const panel = document.getElementById('overlay-panel');
                      const pages = [...document.querySelectorAll(
                        '.politics-review-page'
                      )];
                      const options = [...document.querySelectorAll(
                        '.politics-review-option'
                      )];
                      const rect = panel.getBoundingClientRect();
                      return {
                        viewport:[innerWidth,innerHeight],
                        pages:pages.length,
                        navPages:document.querySelectorAll(
                          '.politics-review-nav button'
                        ).length,
                        options:options.length,
                        horizontalOverflow:
                          panel.scrollWidth - panel.clientWidth,
                        panel:{
                          top:rect.top,bottom:rect.bottom,
                          height:rect.height,
                          overflowY:getComputedStyle(panel).overflowY
                        },
                        confirmVisible:document.getElementById(
                          'review-confirm'
                        ).getBoundingClientRect().height > 0,
                        named:options.every(button =>
                          button.textContent.trim().length > 0
                        )
                      };
                    }"""
                )
                context.close()
        finally:
            browser.close()

    responsive_pass = all(
        value["pages"] == 1
        and value["navPages"] == 2
        and value["options"] >= 3
        and value["horizontalOverflow"] <= 2
        and value["confirmVisible"]
        and value["named"]
        and value["panel"]["top"] >= 0
        and value["panel"]["bottom"] <= value["viewport"][1] + 1
        for value in responsive.values()
    )
    checks = {
        **static,
        **runtime["checks"],
        "review_responsive": responsive_pass,
        "no_page_errors": not page_errors,
    }
    detail = {
        "static": static,
        "runtime": runtime["evidence"],
        "responsive": responsive,
        "page_errors": page_errors,
    }
    failed = [name for name, passed in checks.items() if not passed]
    print(json.dumps({"checks": checks, "detail": detail}, indent=2))
    if failed:
        print("FAILED=" + ",".join(failed))
        raise SystemExit(1)
    print(f"PASS phase3 {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
