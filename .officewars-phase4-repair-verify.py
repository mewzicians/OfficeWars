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
READY = "document.documentElement.dataset.officewarsReady === 'true'"


def main():
    source = GAME.read_text(encoding="utf-8")
    checks = {
        "retired_text_absent": all(
            text not in source
            for text in (
                "Penny-pincher",
                "Frozen modifiers:",
                "first coworker bonus triggered today",
            )
        ),
        "schema_9_active": "const OW_SAVE_SCHEMA=9;" in source,
        "contact_overrides_present": all(
            text in source
            for text in (
                "owContactSlotCount=function(){return 0;}",
                "owContactBookMarkup=function(){return'';}",
                "owResolveSchmoozingAssists=function(){return 0;}",
            )
        ),
    }
    evidence = {}
    page_errors = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            args=["--allow-file-access-from-files", "--disable-extensions", "--no-first-run"],
        )
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.on("pageerror", lambda error: page_errors.append(str(error)))
            page.goto(GAME.as_uri(), wait_until="load", timeout=30_000)
            page.wait_for_function(READY, timeout=15_000)
            runtime = page.evaluate(
                """async () => {
                  localStorage.clear();
                  const checks = {};
                  const evidence = {};
                  const expect = (name,value,detail) => {
                    checks[name]=!!value;
                    evidence[name]=detail;
                  };

                  startRun({seed:946001});
                  R.roleVoteState={id:'old',floor:1,settled:true};
                  R.alumni.floorFlags={
                    floor:1,approvalLossPrevented:true,
                    dilemmaRerollUsed:true,relationshipLossPrevented:true,
                    quietHelpUsed:true,stretchGoalUsed:true
                  };
                  R.effects.push({
                    type:'referralNetwork',
                    targetLifetime:'archetype',
                    coworkers:['INT-GAT'],
                    coworkerArchetypes:['Gatekeeper'],
                    nextWorkday:true
                  });
                  R.floorCompleted=true;
                  nextFloor();
                  const retarget=R.effects.find(
                    effect=>effect.type==='referralNetwork'
                  );
                  expect(
                    'floor_lifecycle_reset',
                    R.floor===2 &&
                      R.roleVoteState===null &&
                      R.alumni.floorFlags.floor===2 &&
                      !R.alumni.floorFlags.approvalLossPrevented &&
                      retarget.coworkers[0]==='ASC-GAT',
                    {
                      floor:R.floor,
                      vote:R.roleVoteState,
                      flags:R.alumni.floorFlags,
                      retarget
                    }
                  );

                  R.paths.Sales='schmoozing';
                  R.milestones.Sales=10;
                  R.phase='night';
                  nightState={
                    outingUsed:false,panelOpen:true,panelMode:'planner',
                    tab:'outings',startCash:R.cash,startCredit:0,
                    homeUsed:0,homeLimit:1,dealUsed:0,dealLimit:0,
                    extraPurchaseCredits:0,bought:new Set(),
                    purchasedDealIds:new Set()
                  };
                  R.nightInvitations=null;
                  renderNightTabs();
                  const nightText=document.getElementById('overlay-panel').innerText;
                  const picker=owCoworkerOption('ASC-GAT');
                  expect(
                    'contact_model_removed',
                    owContactSlotCount()===0 &&
                      owContactBookMarkup()==='' &&
                      !nightText.includes('Contacts') &&
                      picker.detail.includes('/10') &&
                      picker.detail.includes('Standing'),
                    {nightText:nightText.slice(0,240),picker}
                  );

                  R.today={
                    pts:0,stressGain:0,stressRelief:0,log:[],
                    cardFlags:{},activatedCoworkers:[],
                    standardBonusUsed:{},politicalEvents:[],
                    cinematicResults:[]
                  };
                  const before=Object.fromEntries(
                    owCurrentRosterIds().map(id=>[
                      id,
                      {
                        relationship:owCoworkerState(id).relationship,
                        standing:owCoworkerState(id).playerStanding
                      }
                    ])
                  );
                  const originalPick=pick;
                  pick=items=>items.includes('seniorSponsor')
                    ?'seniorSponsor'
                    :originalPick(items);
                  const senior=owExecutiveSupportOutcomeLine();
                  pick=originalPick;
                  const changed=owCurrentRosterIds().filter(id=>{
                    const state=owCoworkerState(id);
                    return state.relationship===before[id].relationship+1 &&
                      state.playerStanding===before[id].standing+3;
                  });
                  expect(
                    'senior_sponsor',
                    changed.length===2,
                    {changed,senior}
                  );

                  const gate='ASC-GAT';
                  const gateState=owCoworkerState(gate);
                  gateState.blockNextChadGain=true;
                  const gateBefore=gateState.playerStanding;
                  const blocked=owShiftStanding(gate,'chad',5,'Fixture');
                  expect(
                    'gatekeeper_block',
                    blocked===0 &&
                      gateState.playerStanding===gateBefore &&
                      !gateState.blockNextChadGain,
                    gateState
                  );

                  const networker=owCurrentRosterIds().find(id=>
                    owCoworkerIdentity(id).archetype==='Networker'
                  );
                  const targets=owCurrentRosterIds().filter(id=>id!==networker);
                  owCoworkerState(networker).relationship=10;
                  const primary=targets[0],secondary=targets[1];
                  const p0=owCoworkerState(primary).playerStanding;
                  const s0=owCoworkerState(secondary).playerStanding;
                  R.pendingDelegateCampaigns=[{
                    id:'network-fixture',delegateId:networker,
                    targetId:primary,secondaryTargetId:secondary,
                    odds:80,roll:0,success:null,settled:false
                  }];
                  owPhase4ResolvePendingCampaigns();
                  expect(
                    'networker_campaign',
                    owCoworkerState(primary).playerStanding===p0+5 &&
                      owCoworkerState(secondary).playerStanding===s0+3,
                    {
                      primary:owCoworkerState(primary),
                      secondary:owCoworkerState(secondary)
                    }
                  );

                  R.favors=[];
                  R.sponsorFavors=[];
                  R.rewardFavors=[];
                  R.paths.Sales=null;
                  R.milestones.Sales=0;
                  const brunch=owPhase4AwardFavor(
                    'receipts','networkingBrunch'
                  );
                  expect(
                    'brunch_reward_favor',
                    !!brunch && brunch.reward &&
                      R.rewardFavors.length===1 &&
                      R.favors.length===0,
                    {brunch,rewardFavors:R.rewardFavors}
                  );

                  R.paths.Sales='schmoozing';
                  R.milestones.Sales=10;
                  R.nightInvitations=null;
                  const invitations=owPhase4PrepareInvitations();
                  const guarantees=invitations.entries
                    .filter(item=>
                      item.reason!=='Relationship-weighted invitation'
                    )
                    .map(item=>item.coworkerId).join('|');
                  owRerollNightInvitations();
                  const guaranteesAfter=R.nightInvitations.entries
                    .filter(item=>
                      item.reason!=='Relationship-weighted invitation'
                    )
                    .map(item=>item.coworkerId).join('|');
                  expect(
                    'invitation_reroll',
                    R.nightInvitations.rerolled &&
                      guarantees===guaranteesAfter,
                    R.nightInvitations
                  );

                  R.favors=[];
                  R.sponsorFavors=[];
                  R.rewardFavors=[];
                  const quiet=owPhase4AwardFavor('quietFix','fixture');
                  const raise=owPhase4AwardFavor('raiseBar','fixture');
                  R.today.managerDirective=
                    OW_DIRECTIVE_BY_ID.get('DIR-OUT-01');
                  R.today.managerPackageAssignments={'offer:2':'negotiate'};
                  R.today.managerPackageOrder=['offer:0','offer:1','offer:2'];
                  R.today.pendingManagerFavorIds=[quiet.id,raise.id];
                  const cashBefore=R.cash;
                  const card={
                    task:TASK_BY_ID.get('bugTriage'),
                    rarity:'common',
                    source:'offer',
                    modifiers:{}
                  };
                  const pkg=owCommitManagerPackage(card,2,'offer');
                  const pp=pkg.successEffects.find(
                    effect=>effect.type==='project'
                  );
                  expect(
                    'manager_favors',
                    pkg.cost===0 &&
                      R.cash===cashBefore &&
                      pp.amount===14 &&
                      R.favors.length===0 &&
                      pkg.favorIds.length===2,
                    {pkg,cashBefore,cashAfter:R.cash}
                  );

                  R.today={
                    pts:0,stressGain:0,stressRelief:0,log:[],
                    cardFlags:{oneOnOne:1},politicalEvents:[],
                    cinematicResults:[],phase4ShiftedTowardPlayer:[]
                  };
                  const oneTarget=owCurrentRosterIds()[0];
                  const event={
                    id:'one-on-one-fixture',type:'relationship',
                    page:{
                      targetIds:[oneTarget],
                      options:[{
                        id:'safe',label:'Safe',
                        successEffects:[],failureEffects:[],
                        cost:{cash:0}
                      }]
                    },
                    choice:{optionId:'safe'},rolledSuccess:true,
                    finalOdds:100,reservedCash:0,
                    participants:owCurrentRosterIds().slice(0,3),
                    applied:false,discarded:false,order:0,
                    exactlyOnce:{}
                  };
                  R.today.politicalEvents=[event];
                  owApplyCinematicPoliticalEvent(event);
                  expect(
                    'one_on_one_targets',
                    R.project.progress>=2 &&
                      R.today.cardFlags.phase4OneOnOneSpent,
                    {progress:R.project.progress,event}
                  );

                  startRun({seed:946002});
                  R.day=1;
                  R.stats.days=1;
                  R.today={
                    pts:0,stressGain:0,stressRelief:0,log:[],
                    cardFlags:{},naturalSlots:['work','mad','lunch'],
                    politicalEvents:[],cinematicResults:[]
                  };
                  const entries=[
                    owScheduleEntry('work','natural','Work'),
                    owScheduleEntry('mad','natural','Chat'),
                    owScheduleEntry('lunch','natural','Lunch')
                  ];
                  const standingBefore=R.floorRoster.stakeholderIds.map(
                    id=>owCoworkerState(id).playerStanding
                  );
                  owPreparePoliticalEvents(entries);
                  const chadEvent=R.today.politicalEvents.find(
                    item=>item.type==='chadConversation'
                  );
                  const standingPrepared=R.floorRoster.stakeholderIds.map(
                    id=>owCoworkerState(id).playerStanding
                  );
                  R.workdayPresentation={
                    skipRequested:true,currentEventId:null
                  };
                  R.phase='workday';
                  await owResolveCinematicPoliticalEvents(
                    entries.find(item=>item.id===chadEvent.entryId),
                    chadEvent.triggerPhase,
                    {headless:true,policy:'baseline'}
                  );
                  expect(
                    'chad_chronology',
                    JSON.stringify(standingBefore)===
                      JSON.stringify(standingPrepared) &&
                      chadEvent.applied,
                    {standingBefore,standingPrepared,chadEvent}
                  );

                  document.documentElement.style.fontSize='32px';
                  openOfficePoliticsBoard();
                  const dialog=document.querySelector(
                    '#office-politics-board .hud-modal-dialog'
                  );
                  expect(
                    'text_200_percent',
                    dialog.scrollWidth<=dialog.clientWidth+2 &&
                      document.querySelectorAll(
                        '#office-politics-board .office-politics-card'
                      ).length===6,
                    {
                      scrollWidth:dialog.scrollWidth,
                      clientWidth:dialog.clientWidth
                    }
                  );
                  return {checks,evidence};
                }"""
            )
            checks.update(runtime["checks"])
            evidence.update(runtime["evidence"])
        finally:
            browser.close()

    checks["no_page_errors"] = not page_errors
    evidence["page_errors"] = page_errors
    print(json.dumps({"checks": checks, "evidence": evidence}, indent=2))
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        print("FAILED=" + ",".join(failed))
        raise SystemExit(1)
    print("PASS:PHASE4_DEPENDENCY_REPAIR")


if __name__ == "__main__":
    main()
