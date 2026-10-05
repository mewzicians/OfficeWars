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
CAPTURE = ROOT / "Wiki/Projects/OfficeWars/Visual Reference/todays-directive-morning.png"
if not CAPTURE.parent.is_dir():
    CAPTURE = ROOT / "artifacts/visual-reference/todays-directive-morning.png"
CAPTURE.parent.mkdir(parents=True, exist_ok=True)


def main():
    page_errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            args=["--allow-file-access-from-files", "--disable-extensions"],
        )
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.on("pageerror", lambda error: page_errors.append(str(error)))
            page.goto(GAME.as_uri(), wait_until="load", timeout=30_000)
            page.wait_for_function(
                "document.documentElement.dataset.officewarsReady === 'true'",
                timeout=15_000,
            )
            evidence = page.evaluate(
                """async () => {
                  localStorage.clear();
                  const meta=owDefaultMeta();
                  meta.tutorial.completed=true;
                  meta.tutorial.nextStep=13;
                  owWriteMeta(meta);
                  const checks={};
                  const detail={};
                  const expect=(name,value,data)=>{
                    checks[name]=!!value;
                    detail[name]=data;
                  };
                  const cards=TASKS.filter(task =>
                    ['common','uncommon'].includes(task.rarity)
                  ).slice(0,3).map(task=>({
                    task,rarity:task.rarity,source:'offer',modifiers:{}
                  }));
                  const reset=(directiveId,cash=500,stance='comply')=>{
                    startRun({seed:936000});
                    R.floor=1;
                    R.day=1;
                    R.stats.days=1;
                    R.manager=MANAGERS.find(item=>item.id==='penny');
                    R.cash=cash;
                    R.today=Object.assign(R.today||{},{
                      startCash:cash,
                      startProjectProgress:R.project.progress,
                      startStress:R.stress,
                      actionHistory:[],
                      positiveActionTypes:[],
                      stressGain:0,
                      managerDirective:OW_DIRECTIVE_BY_ID.get(directiveId),
                      managerPackageAssignments:{'offer:0':stance},
                      managerPackageOrder:['offer:0'],
                      managerPackage:null,
                      cinematicResults:[],
                      log:[],
                      scheduleEntries:[]
                    });
                    R.morningCards=cards;
                    return owCommitManagerPackage(cards[0],0,'offer');
                  };

                  let pkg=reset('DIR-COST-01',100,'negotiate');
                  const holdCost={cash:R.cash,start:pkg.trackingStartCash};
                  const holdEarly=owMaybeSettleManagerPackage('task');
                  const holdComplete=owMaybeSettleManagerPackage('wrapUp');
                  expect('hold_line_excludes_package_cost',
                    holdCost.cash===50&&holdCost.start===50&&
                    holdEarly===null&&pkg.objectiveStatus==='complete'&&
                    !!holdComplete,
                    {holdCost,status:pkg.objectiveStatus,result:pkg.result}
                  );

                  pkg=reset('DIR-COST-01',100,'negotiate');
                  R.cash-=10;
                  owMaybeSettleManagerPackage('action');
                  expect('hold_line_fails_after_later_spend',
                    pkg.objectiveStatus==='failed',
                    cloneForTest(pkg)
                  );

                  pkg=reset('DIR-COST-02',550,'negotiate');
                  R.today.accountedCash=R.cash;
                  const reserveCashBeforeSettlement=R.cash;
                  owMaybeSettleManagerPackage('task');
                  expect('reserve_includes_package_cost',
                    reserveCashBeforeSettlement===500&&
                    R.today.accountedCash===500&&
                    pkg.objectiveStatus==='complete',
                    {
                      cashBeforeSettlement:reserveCashBeforeSettlement,
                      accountedCash:R.today.accountedCash,
                      cashAfterReward:R.cash,
                      status:pkg.objectiveStatus
                    }
                  );

                  pkg=reset('DIR-OUT-02',100,'comply');
                  R.today.actionHistory=[
                    {kind:'work',positive:true},
                    {kind:'work',positive:true}
                  ];
                  const rngBefore=RNG.snapshot().gameplayState;
                  owMaybeSettleManagerPackage('action');
                  const rngAfter=RNG.snapshot().gameplayState;
                  const approvalOnce=R.managerApproval;
                  owMaybeSettleManagerPackage('wrapUp');
                  expect('early_complete_no_rng_exactly_once',
                    pkg.objectiveStatus==='complete'&&
                    rngBefore===rngAfter&&
                    R.managerApproval===approvalOnce,
                    {rngBefore,rngAfter,approval:R.managerApproval,pkg}
                  );

                  pkg=reset('DIR-OUT-01',100,'comply');
                  R.project.progress=R.today.startProjectProgress+20;
                  R.today.pts=0;
                  const projectEarly=owMaybeSettleManagerPackage('action');
                  const projectFinal=owMaybeSettleManagerPackage('wrapUp');
                  expect('period_end_project_gain',
                    projectEarly===null&&!!projectFinal&&
                    pkg.objectiveStatus==='complete',
                    cloneForTest(pkg)
                  );

                  pkg=reset('DIR-COLL-03',100,'comply');
                  nightState={
                    outingUsed:true,recPicked:false,homeUsed:0,dealUsed:0,
                    startCash:R.cash,startCredit:0
                  };
                  R.phase='night';
                  const nightRngBefore=RNG.snapshot().gameplayState;
                  const nightResult=owMaybeSettleNightDirective('nightAction');
                  expect('night_early_complete_no_rng',
                    nightResult&&nightResult.success&&
                    nightResult.objectiveStatus==='complete'&&
                    nightRngBefore===RNG.snapshot().gameplayState&&
                    R.pendingNightDirective===null,
                    nightResult
                  );

                  pkg=reset('DIR-OUT-03',100,'comply');
                  nightState={
                    outingUsed:false,recPicked:false,homeUsed:0,dealUsed:0,
                    startCash:R.cash,startCredit:0
                  };
                  R.phase='night';
                  const nightFailure=owSettlePendingNightDirective();
                  expect('night_period_end_failure',
                    nightFailure&&!nightFailure.success&&
                    nightFailure.objectiveStatus==='failed',
                    nightFailure
                  );

                  pkg=reset('DIR-OUT-02',100,'comply');
                  R.projectPolitics.briefId='reorg';
                  R.projectPolitics.roleOwner='player';
                  R.managerApproval=1;
                  R.today.actionHistory=[
                    {kind:'work',positive:true},
                    {kind:'work',positive:true}
                  ];
                  owMaybeSettleManagerPackage('action');
                  const playerApproval=R.managerApproval;
                  pkg=reset('DIR-RISK-01',100,'resist');
                  R.projectPolitics.briefId='reorg';
                  R.projectPolitics.roleOwner='chad';
                  R.managerApproval=3;
                  R.today.actionHistory=[{kind:'slump',positive:false}];
                  owMaybeSettleManagerPackage('action');
                  expect('reorg_approval_leverage',
                    playerApproval===3&&R.managerApproval===1,
                    {playerApproval,chadFailureApproval:R.managerApproval}
                  );

                  startRun({seed:936090});
                  owShowDirectiveResultBanner({
                    success:false,
                    result:'PENALTY Â· +2 stress'
                  });
                  const bannerBefore=!!document.getElementById(
                    'directive-result-banner'
                  );
                  await startDay();
                  const bannerAfter=!!document.getElementById(
                    'directive-result-banner'
                  );
                  expect('night_banner_clears_before_morning',
                    bannerBefore&&!bannerAfter&&R.phase==='morning',
                    {bannerBefore,bannerAfter,phase:R.phase}
                  );

                  startRun({seed:936100});
                  await startDay();
                  R.manager=MANAGERS.find(item=>item.id==='penny');
                  R.today.managerDirective=OW_DIRECTIVE_BY_ID.get('DIR-COST-03');
                  R.today.managerPackageAssignments={
                    'offer:0':'comply','offer:1':'resist','offer:2':'negotiate'
                  };
                  renderMorningUI();
                  updateHUD();
                  const panel=document.getElementById('overlay-panel')
                    .getBoundingClientRect();
                  const announcement=document.querySelector(
                    '.manager-directive-announcement'
                  );
                  const rect=announcement.getBoundingClientRect();
                  const firstBadge=document.querySelector(
                    '.manager-package-badge'
                  );
                  showGlobalTooltip(firstBadge);
                  const tooltip=firstBadge.dataset.tip;
                  const copy=announcement.textContent
                    .replace(/\\s+/g,' ').trim();
                  expect('centered_three_line_announcement',
                    Math.abs(
                      (rect.left+rect.width/2)-(panel.left+panel.width/2)
                    )<2&&
                    copy.includes('The Penny Pincher')&&
                    copy.includes('Spend No Cash or Expense Credit Tonight')&&
                    copy.includes('“No Expense After Hours”')&&
                    !announcement.querySelector('.manager-directive-avatar'),
                    {panel,rect,copy}
                  );
                  expect('tooltip_success_failure_only',
                    tooltip.split('\\n').length===2&&
                    tooltip.startsWith('SUCCESS')&&
                    tooltip.includes('\\nFAILURE')&&
                    !/odds|cost|modifier|settles|objective/i.test(tooltip),
                    tooltip
                  );
                  expect('manager_names_standardized',
                    MANAGERS.find(item=>item.id==='penny').name===
                      'The Penny Pincher'&&
                    MANAGERS.find(item=>item.id==='slave').name===
                      'The Slave Driver',
                    MANAGERS.map(item=>item.name)
                  );
                  return{checks,detail};
                }"""
            )
            page.wait_for_timeout(250)
            page.evaluate(
                """() => {
                  const meta=owReadMeta();
                  meta.tutorial.completed=true;
                  meta.tutorial.nextStep=0;
                  meta.guidedIntern=Object.assign(
                    owDefaultMeta().guidedIntern,
                    meta.guidedIntern||{},
                    {
                      required:true,completed:true,
                      replayRequested:false,version:1
                    }
                  );
                  owWriteMeta(meta);
                  showGlobalTooltip(
                    document.querySelector('.manager-package-badge')
                  );
                }"""
            )
            page.wait_for_timeout(10)
            page.screenshot(path=str(CAPTURE))
            checks = dict(evidence["checks"])
            checks["no_page_errors"] = not page_errors
            failed = [name for name, passed in checks.items() if not passed]
            print(
                "DIRECTIVE_JSON="
                + json.dumps(
                    {
                        "checks": checks,
                        "detail": evidence["detail"],
                        "capture": str(CAPTURE),
                        "pageErrors": page_errors,
                    },
                    separators=(",", ":"),
                )
            )
            if failed:
                print("FAILED=" + ",".join(failed))
                return 1
            print(f"PASS:TODAYS_DIRECTIVE {len(checks)}/{len(checks)}")
            return 0
        finally:
            browser.close()


if __name__ == "__main__":
    raise SystemExit(main())
