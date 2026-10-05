import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))

from playwright.sync_api import sync_playwright


GAME = ROOT / "officewarsautobattler.html"
READY = "document.documentElement.dataset.officewarsReady === 'true'"

EXPECTED_CARDS = {
    "readmeUpdate": ("Coding", "README Update", "common", 10, 9),
    "regressionTests": ("Coding", "Regression Tests", "common", 10, 10),
    "bugTriage": ("Coding", "Bug Triage", "common", 10, 10),
    "productionHotfix": ("Coding", "Production Hotfix", "common", 10, 12),
    "versionControl": ("Coding", "Version Control", "uncommon", 10, 10),
    "buildScript": ("Coding", "Build Script", "uncommon", 10, 10),
    "apiIntegration": ("Coding", "API Integration", "uncommon", 10, 10),
    "repositoryFork": ("Coding", "Repository Fork", "rare", 10, 12),
    "parallelProcessing": ("Coding", "Parallel Processing", "rare", 8, 10),
    "hackathon": ("Coding", "Hackathon", "legendary", 8, 8),
    "oneOnOne": ("Management", "One-on-One", "common", 10, 10),
    "meetingMinutes": ("Management", "Meeting Minutes", "common", 10, 10),
    "actionPlan": ("Management", "Action Plan", "common", 10, 10),
    "capacityPlanning": ("Management", "Capacity Planning", "common", 9, 10),
    "meetingPrep": ("Management", "Meeting Prep", "uncommon", 10, 10),
    "staffCheckIn": ("Management", "Staff Check-In", "uncommon", 9, 10),
    "scheduleAdjustment": ("Management", "Schedule Adjustment", "uncommon", 10, 10),
    "crossFunctionalSync": ("Management", "Cross-Functional Sync", "rare", 8, 12),
    "executiveReview": ("Management", "Executive Review", "rare", 9, 11),
    "warRoom": ("Management", "War Room", "legendary", 8, 10),
    "iterationPass": ("Design", "Iteration Pass", "common", 10, 10),
    "referenceStudy": ("Design", "Reference Study", "common", 10, 10),
    "accessibilityReview": ("Design", "Accessibility Review", "common", 9, 10),
    "whiteSpace": ("Design", "White Space", "common", 10, 10),
    "prototypeTest": ("Design", "Prototype Test", "uncommon", 10, 10),
    "conceptSelection": ("Design", "Concept Selection", "uncommon", 9, 10),
    "userTesting": ("Design", "User Testing", "uncommon", 10, 10),
    "creativeBreakthrough": ("Design", "Creative Breakthrough", "rare", 9, 11),
    "rapidPrototype": ("Design", "Rapid Prototype", "rare", 8, 12),
    "designSystem": ("Design", "Design System", "legendary", 8, 12),
    "expenseAllowance": ("Sales", "Expense Allowance", "common", 9, 10),
    "referralFee": ("Sales", "Referral Fee", "common", 10, 10),
    "salesQuota": ("Sales", "Sales Quota", "common", 10, 10),
    "crossSell": ("Sales", "Cross-Sell", "common", 10, 10),
    "clientEntertainment": ("Sales", "Client Entertainment", "uncommon", 9, 10),
    "comparisonShopping": ("Sales", "Comparison Shopping", "uncommon", 9, 10),
    "commissionAdvance": ("Sales", "Commission Advance", "uncommon", 9, 11),
    "corporateExpenseAccount": ("Sales", "Corporate Expense Account", "rare", 8, 12),
    "referralNetwork": ("Sales", "Referral Network", "rare", 9, 11),
    "net30Contract": ("Sales", "Net 30 Contract", "legendary", 8, 8),
    "processAudit": ("Operations", "Process Audit", "common", 9, 10),
    "preventiveMaintenance": ("Operations", "Preventive Maintenance", "common", 8, 11),
    "priorityRequisition": ("Operations", "Priority Requisition", "common", 9, 10),
    "overnightReserve": ("Operations", "Overnight Reserve", "common", 10, 9),
    "contingencyPlan": ("Operations", "Contingency Plan", "uncommon", 9, 10),
    "shiftHandoff": ("Operations", "Shift Handoff", "uncommon", 8, 11),
    "accrualAccounting": ("Operations", "Accrual Accounting", "uncommon", 9, 10),
    "workingCapital": ("Operations", "Working Capital", "rare", 9, 11),
    "failoverProtocol": ("Operations", "Failover Protocol", "rare", 8, 12),
    "perfectExecution": ("Operations", "Perfect Execution", "legendary", 8, 12),
}


def main():
    source = GAME.read_text(encoding="utf-8")
    task_pattern = re.compile(
        r"task\('([^']+)','([^']+)','([^']+)','([^']+)',(\d+),(\d+),"
    )
    parsed = {
        card_id: (family, name, rarity, int(progress), int(stress))
        for card_id, family, name, rarity, progress, stress in task_pattern.findall(source)
    }
    ordinary = {card_id: parsed.get(card_id) for card_id in EXPECTED_CARDS}
    rarity_counts = {}
    for value in ordinary.values():
        if value:
            rarity_counts[value[2]] = rarity_counts.get(value[2], 0) + 1

    retired = (
        "Penny-pincher",
        "Frozen modifiers:",
        "first coworker bonus triggered today",
        "Each task package carries one fixed response",
        "Base odds after frozen modifiers",
    )
    static = {
        "schema_9": "const OW_SAVE_SCHEMA=9;" in source,
        "path_authority": all(
            marker in source
            for marker in (
                "const OW_PATH_PROGRESSION=Object.freeze({",
                "cleanCode:{kind:'xp',milestones:[3,10,20]}",
                "closing:{kind:'salesCycle',milestones:[3],capstone:{kind:'chain',value:9}}",
                "brandStrategy:{kind:'campaign',milestones:[],capstone:{kind:'campaign',value:4}}",
            )
        ),
        "no_raw_old_trait_checks": not re.search(
            r"owTraitLevel\('[^']+'\)\s*(?:>=|<=|<|>)\s*(?:6|10|20)",
            source,
        ),
        "resume_rail_and_book_surfaces": all(
            marker in source
            for marker in (
                "--ow-rail-width: clamp(180px, 13vw, 230px)",
                "const OW_RESUME_RAIL_MARKERS={",
                "function owResumeRailPresentation(family)",
                'class="resume-rail-footer"',
                "Array.from({length:20}",
                "20+ XP",
            )
        ),
        "card_inventory": ordinary == EXPECTED_CARDS,
        "card_rarity_curve": rarity_counts == {
            "common": 20,
            "uncommon": 15,
            "rare": 10,
            "legendary": 5,
        },
        "referral_copy_picker": "const count=sourceCard.task.id==='referralNetwork'?2:3;" in source,
        "referral_context_text": (
            "fill non-Chad invitation slots" in source
            and "shifts every invited coworker 3 standing toward you" in source
        ),
        "conference_pass_text": (
            "Choose one coworker: +1 Relationship and +5 player standing." in source
        ),
        "retired_text_absent": all(text not in source for text in retired),
    }

    page_errors = []
    responsive = {}
    presentation = {}
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
                """async expectedIds => {
                  localStorage.clear();
                  const checks = {};
                  const evidence = {};
                  const expect = (name,value,detail) => {
                    checks[name]=!!value;
                    evidence[name]=detail;
                  };
                  const firstLegal = request => request.options
                    .map((option,index)=>({option,index}))
                    .filter(item=>!item.option.disabled)
                    .slice(0,request.min)
                    .map(item=>item.index);
                  const taskCard = id => {
                    const task=TASK_BY_ID.get(id);
                    if(!task)throw new Error('Missing task '+id);
                    return{task,rarity:task.rarity,source:'phase5Fixture',modifiers:{}};
                  };
                  const reset = seed => {
                    localStorage.clear();
                    startRun({seed});
                    R.phase='morningResolution';
                    R.floor=1;
                    R.day=1;
                    R.stats.days=1;
                    R.daysLeft=3;
                    R.project={
                      name:'Phase 5 Verification',
                      baseSize:100000,
                      size:100000,
                      completionTarget:100000,
                      progress:0,
                      completionPending:false,
                      completionSource:null,
                      completionDay:null,
                      locked:false,
                      lockDay:null
                    };
                    R.overdelivery={
                      active:false,activationPending:false,target:100000,
                      tiers:0,paid:false,payoutChoice:null,
                      rewardTierPenalty:0,expectationTierReduction:0
                    };
                    R.rival.progress=0;
                    R.rival.today={gain:0,workSlots:1};
                    R.stress=0;
                    R.cash=10000;
                    R.expenseCredit=0;
                    R.familyXP={Coding:0,Management:0,Design:0,Sales:0,Operations:0};
                    R.paths={};
                    R.milestones={};
                    R.capstone=null;
                    R.capstoneBatch=null;
                    R.effects=[];
                    R.pins=[];
                    R.storedTask=null;
                    R.completedTaskIds=[
                      'readmeUpdate','meetingMinutes','referenceStudy',
                      'expenseAllowance','processAudit'
                    ];
                    R.cardCompletions={};
                    R.polish={};
                    R.codebase=0;
                    R.printedCommonCompleted=0;
                    R.rerollsNight=1;
                    R.rerollsMorning=2;
                    R.dailyTaskRerolls=0;
                    R.todayCard=null;
                    R.today={
                      pts:0,stressGain:0,stressRelief:0,pay:0,log:[],
                      lunchGood:null,startProjectProgress:0,taskPlays:[],
                      cardFlags:{},actionHistory:[],positiveActionTypes:[],
                      backupQueue:[],standardBonusUsed:{},activatedCoworkers:[],
                      deadlineShift:0,meetingsToday:0,meetingTopicsUsed:[],
                      meetingBonusAwarded:false,currentMeetingSummary:null,
                      dailyInteractionDone:false,rivalLines:0,dayProgress:[],
                      activeProgressIndex:-1,previewActive:false,
                      naturalSlots:['work','meeting','lunch','cooler','mad'],
                      scheduleEntries:[],politicalEvents:[],cinematicResults:[],
                      phase4ShiftedTowardPlayer:[]
                    };
                    R.morningCards=[
                      taskCard('readmeUpdate'),
                      taskCard('meetingMinutes'),
                      taskCard('referenceStudy'),
                      taskCard('expenseAllowance'),
                      taskCard('processAudit')
                    ];
                    owAutomatedChoiceResolver=firstLegal;
                    hideOverlay();
                  };

                  reset(950001);
                  const ordinaryPaths=[
                    'cleanCode','automation','debugging','delegation','agile',
                    'leadership','eyeForDetail','moodboard','negotiation',
                    'schmoozing','efficiency','logistics','compoundInterest'
                  ];
                  const progression=Object.fromEntries(ordinaryPaths.map(path=>[
                    path,
                    [2,3,9,10,19,20,21].map(value=>
                      owPathTierForLevel(path,value)
                    )
                  ]));
                  expect(
                    'progression_boundaries',
                    Object.values(progression).every(values=>
                      values.join('|')==='0|1|1|2|2|3|3'
                    ),
                    progression
                  );
                  expect(
                    'exceptional_progression',
                    owMilestoneLevelsForPath('closing').join('|')==='3' &&
                      owPathProgressionSpec('closing').capstone.value===9 &&
                      owMilestoneLevelsForPath('brandStrategy').length===0 &&
                      owPathProgressionSpec('brandStrategy').kind==='campaign',
                    {
                      closing:owPathProgressionSpec('closing'),
                      brand:owPathProgressionSpec('brandStrategy')
                    }
                  );

                  R.paths.Coding='cleanCode';
                  R.milestones.Coding=10;
                  R.familyXP.Coding=19;
                  owGrantFamilyXP('Coding',1,'Boundary fixture');
                  expect(
                    'capstone_at_twenty',
                    R.familyXP.Coding===20 &&
                      R.capstone && R.capstone.path==='cleanCode' &&
                      R.capstone.status==='reserved',
                    {xp:R.familyXP.Coding,capstone:R.capstone}
                  );
                  const stage={
                    paths:{Coding:'cleanCode',Design:'eyeForDetail'},
                    milestones:{Coding:20,Design:20},
                    capstone:null
                  };
                  R.capstone=null;
                  R.milestones={Coding:10,Design:10};
                  expect(
                    'simultaneous_capstones',
                    owPromotionCapstoneCandidates(stage).length===2,
                    owPromotionCapstoneCandidates(stage)
                  );

                  const cardResults={};
                  for(let index=0;index<expectedIds.length;index++){
                    const id=expectedIds[index];
                    try{
                      reset(951000+index);
                      const primary=taskCard(id);
                      R.morningCards=[
                        primary,
                        taskCard('readmeUpdate'),
                        taskCard('meetingMinutes'),
                        taskCard('referenceStudy'),
                        taskCard('expenseAllowance'),
                        taskCard('processAudit')
                      ];
                      const context=await owPrepareCardContext(primary,{
                        primarySource:'offer'
                      });
                      const survived=await owCompletePlay(primary,context);
                      cardResults[id]={
                        pass:survived!==false &&
                          (R.cardCompletions[id]||0)>=1 &&
                          R.today.taskPlays.some(play=>play.taskId===id),
                        taskPlays:R.today.taskPlays.map(play=>play.taskId),
                        effects:(R.effects||[]).map(effect=>effect.type)
                      };
                    }catch(error){
                      cardResults[id]={
                        pass:false,
                        error:error.name+': '+error.message,
                        stack:String(error.stack||'').slice(0,800)
                      };
                    }finally{
                      owAutomatedChoiceResolver=null;
                      owResolutionLock=false;
                      owChoiceState=null;
                      pendingMorning=null;
                      hideOverlay();
                    }
                  }
                  expect(
                    'all_fifty_cards_execute',
                    Object.values(cardResults).every(result=>result.pass),
                    cardResults
                  );

                  reset(952001);
                  let referralRequest=null;
                  owAutomatedChoiceResolver=request=>{
                    if(request.title==='Referral Network')referralRequest={
                      min:request.min,max:request.max,
                      labels:request.options.map(option=>option.label)
                    };
                    return firstLegal(request);
                  };
                  const copied=await owPrepareCopiedEffectContext(
                    taskCard('referralNetwork'),
                    taskCard('rapidPrototype'),
                    ['referralNetwork']
                  );
                  const coworkerIds=owCurrentRosterIds().slice(0,2);
                  const detail=owEffectDetail({
                    type:'referralNetwork',
                    nextWorkday:true,
                    coworkers:coworkerIds
                  });
                  expect(
                    'referral_network_repair',
                    referralRequest && referralRequest.min===2 &&
                      referralRequest.max===2 &&
                      copied.setup.coworkers.length===2 &&
                      detail.includes('non-Chad invitation slots') &&
                      detail.includes('3 standing toward you') &&
                      !detail.includes('bonus') &&
                      !detail.includes('doubled'),
                    {referralRequest,copied,detail}
                  );

                  const meta=owDefaultMeta();
                  meta.guidedIntern.completed=true;
                  meta.settings.volume=33;
                  owWriteMeta(meta);
                  owStorageSet(OW_SAVE_KEY,JSON.stringify({
                    schema:7,
                    checkpoint:'morning',
                    run:{floor:1,project:{},stats:{}}
                  }));
                  const restored=owReadActiveSave();
                  const notice=owStorageGet(OW_SAVE_NOTICE_KEY)||'';
                  const preserved=owReadMeta();
                  expect(
                    'schema_7_invalidation',
                    restored===null &&
                      notice.includes('retired Home system') &&
                      preserved.guidedIntern.completed===true &&
                      preserved.settings.volume===33,
                    {restored,notice,preserved}
                  );

                  reset(952002);
                  R.paths.Coding='cleanCode';
                  R.milestones.Coding=20;
                  R.familyXP.Coding=21;
                  owRenderResumeRail();
                  openResumeBook('Coding');
                  expect(
                    'resume_compact_footer_and_detailed_book',
                    document.querySelectorAll(
                      '.resume-family .resume-xp-segment'
                    ).length===0 &&
                      document.querySelectorAll(
                        '.resume-family .resume-rail-footer'
                      ).length===5 &&
                      document.querySelectorAll(
                        '.resume-family .resume-rail-bar'
                      ).length===5 &&
                      document.querySelector(
                        '.resume-family[data-family="Coding"]'
                      ).classList.contains('is-complete') &&
                      !document.querySelector(
                        '.resume-family[data-family="Coding"] .resume-rail-marker'
                      ) &&
                      document.querySelector(
                        '.resume-family[data-family="Coding"] .resume-rail-current'
                      ).textContent.replace(/\\s+/g,' ').trim()==='21 XP' &&
                      document.querySelectorAll(
                        '#resume-book .resume-book-track .resume-xp-segment'
                      ).length===20 &&
                      !!document.querySelector(
                        '#resume-book .resume-xp-segment.overflow'
                      ) &&
                      document.getElementById('resume-book-content')
                        .innerText.includes('21 XP'),
                    {
                      rail:document.querySelectorAll(
                        '.resume-family .resume-xp-segment'
                      ).length,
                      footers:document.querySelectorAll(
                        '.resume-family .resume-rail-footer'
                      ).length,
                      book:document.querySelectorAll(
                        '#resume-book .resume-book-track .resume-xp-segment'
                      ).length,
                      text:document.getElementById('resume-book-content')
                        .innerText.slice(0,200)
                    }
                  );

                  closeHudModal('resume-book');
                  reset(952003);
                  const renderModel=(family,configure)=>{
                    configure();
                    owRenderResumeRail();
                    const model=owResumeRailPresentation(family);
                    const row=document.querySelector(
                      `.resume-family[data-family="${family}"]`
                    );
                    return{
                      current:model.current,
                      unit:model.unit,
                      final:model.final,
                      next:model.next,
                      secondary:model.secondary,
                      fill:Math.round(model.fillPercentage*100)/100,
                      marker:model.markerPercentage===null
                        ?null
                        :Math.round(model.markerPercentage*100)/100,
                      pathReady:model.pathReady,
                      complete:model.complete,
                      activeCapstone:model.activeCapstone,
                      text:row.querySelector(
                        '.resume-rail-current'
                      )?.textContent.replace(/\\s+/g,' ').trim(),
                      secondaryText:row.querySelector(
                        '.resume-rail-next'
                      )?.textContent.trim()||'',
                      hasMarker:!!row.querySelector('.resume-rail-marker'),
                      classes:row.className,
                      badge:!!row.querySelector('.resume-capstone-badge')
                    };
                  };
                  const railStates={};
                  railStates.noPath=renderModel('Coding',()=>{
                    R.paths={};
                    R.familyXP.Coding=0;
                  });
                  railStates.pathReady=renderModel('Coding',()=>{
                    R.paths={};
                    R.familyXP.Coding=3;
                  });
                  railStates.intermediate=renderModel('Coding',()=>{
                    R.paths.Coding='automation';
                    R.familyXP.Coding=6;
                  });
                  railStates.final=renderModel('Coding',()=>{
                    R.paths.Coding='automation';
                    R.familyXP.Coding=20;
                  });
                  railStates.uncapped=renderModel('Coding',()=>{
                    R.paths.Coding='automation';
                    R.familyXP.Coding=27;
                  });
                  railStates.accelerated=renderModel('Management',()=>{
                    R.cashJarRewards={
                      flags:{acceleratedDevelopment:true}
                    };
                    R.paths.Management='delegation';
                    R.familyXP.Management=8;
                  });
                  railStates.closing=renderModel('Sales',()=>{
                    R.paths.Sales='closing';
                    R.familyXP.Sales=12;
                    R.closingBestChain=4;
                  });
                  railStates.capstone=renderModel('Coding',()=>{
                    R.cashJarRewards={flags:{}};
                    R.paths.Coding='automation';
                    R.familyXP.Coding=20;
                    R.capstone={
                      family:'Coding',
                      path:'automation',
                      status:'active'
                    };
                  });
                  expect(
                    'resume_rail_presentation_states',
                    railStates.noPath.secondary==='PATH 3' &&
                    railStates.noPath.final===3 &&
                    railStates.noPath.hasMarker &&
                    railStates.pathReady.secondary==='PATH READY' &&
                    railStates.pathReady.pathReady &&
                    railStates.intermediate.secondary==='NEXT 10' &&
                    railStates.intermediate.final===20 &&
                    railStates.intermediate.hasMarker &&
                    railStates.final.complete &&
                    railStates.final.secondaryText==='' &&
                    !railStates.final.hasMarker &&
                    railStates.uncapped.text==='27 XP' &&
                    railStates.accelerated.final===18 &&
                    railStates.accelerated.next===18 &&
                    railStates.accelerated.secondary==='NEXT 18' &&
                    railStates.closing.current===4 &&
                    railStates.closing.unit==='CHAIN' &&
                    railStates.closing.final===9 &&
                    railStates.closing.secondary==='NEXT 5' &&
                    railStates.capstone.activeCapstone &&
                    railStates.capstone.badge &&
                    railStates.capstone.classes.includes(
                      'has-active-capstone'
                    ),
                    railStates
                  );

                  const bodyText=document.body.innerText;
                  expect(
                    'fresh_load_retired_text_absent',
                    ![
                      'Frozen modifiers:',
                      'first coworker bonus triggered today',
                      'Each task package carries one fixed response',
                      'Base odds after frozen modifiers'
                    ].some(text=>bodyText.includes(text)),
                    bodyText.slice(0,600)
                  );
                  return{checks,evidence};
                }""",
                list(EXPECTED_CARDS.keys()),
            )

            for name, viewport in (
                ("desktop", {"width": 1440, "height": 900}),
                ("compact", {"width": 900, "height": 700}),
                ("short_landscape", {"width": 900, "height": 520}),
            ):
                page.set_viewport_size(viewport)
                responsive[name] = page.evaluate(
                    """() => {
                      if(!R)startRun({seed:953000});
                      R.paths.Coding='cleanCode';
                      R.milestones.Coding=20;
                      R.familyXP.Coding=21;
                      R.paths.Management=undefined;
                      R.familyXP.Management=0;
                      owRenderResumeRail();
                      openResumeBook('Coding');
                      const track=document.querySelector(
                        '#resume-book .resume-book-track'
                      );
                      const row=document.querySelector(
                        '.resume-family[data-family="Coding"]'
                      );
                      const rail=row.querySelector('.resume-rail-bar');
                      const footer=row.querySelector('.resume-rail-footer');
                      const pending=document.querySelector(
                        '.resume-family[data-family="Management"]'
                      );
                      const marker=pending.querySelector(
                        '.resume-rail-marker'
                      );
                      const markerTrack=pending.querySelector(
                        '.resume-rail-bar-wrap'
                      );
                      const style=getComputedStyle(track);
                      const rowRect=row.getBoundingClientRect();
                      const footerRect=footer.getBoundingClientRect();
                      const markerRect=marker.getBoundingClientRect();
                      const markerTrackRect=markerTrack.getBoundingClientRect();
                      return{
                        bookSegments:track.children.length,
                        railSegments:document.querySelectorAll(
                          '.resume-family .resume-xp-segment'
                        ).length,
                        columns:style.gridTemplateColumns.split(' ').length,
                        bookHeight:track.getBoundingClientRect().height,
                        railHeight:rail.getBoundingClientRect().height,
                        overflow:!!track.querySelector('.overflow'),
                        footerContained:
                          footerRect.left>=rowRect.left-1&&
                          footerRect.right<=rowRect.right+1&&
                          footerRect.top>=rowRect.top-1&&
                          footerRect.bottom<=rowRect.bottom+1,
                        markerContained:
                          markerRect.left>=markerTrackRect.left-1&&
                          markerRect.right<=markerTrackRect.right+1,
                        railWidth:document.getElementById(
                          'side-panel'
                        ).getBoundingClientRect().width
                      };
                    }"""
                )
            for motion in ("no-preference", "reduce"):
                context = browser.new_context(
                    viewport={"width": 1440, "height": 900},
                    reduced_motion=motion,
                )
                motion_page = context.new_page()
                motion_page.on(
                    "pageerror",
                    lambda error: page_errors.append(str(error)),
                )
                motion_page.goto(
                    GAME.as_uri(), wait_until="load", timeout=30_000
                )
                motion_page.wait_for_function(READY, timeout=15_000)
                presentation[motion] = motion_page.evaluate(
                    """async motion => {
                      localStorage.clear();
                      startRun({seed:954000});
                      R.phase='morning';
                      Object.keys(FAMILIES).forEach((family,index)=>{
                        delete R.paths[family];
                        R.familyXP[family]=index;
                      });
                      R.capstone=null;
                      owRenderResumeRail();
                      const familyMarkers=[...document.querySelectorAll(
                        '.resume-family .resume-rail-marker'
                      )];
                      const markerContained=familyMarkers.every(marker=>{
                        const markerRect=marker.getBoundingClientRect();
                        const trackRect=marker.parentElement
                          .getBoundingClientRect();
                        return markerRect.left>=trackRect.left-1&&
                          markerRect.right<=trackRect.right+1;
                      });
                      const markerIcons=familyMarkers.map(marker=>
                        marker.innerHTML.replace(/\\s+/g,' ').trim()
                      );
                      R.paths.Coding='automation';
                      R.familyXP.Coding=20;
                      R.milestones.Coding=20;
                      R.capstone={
                        family:'Coding',
                        path:'automation',
                        status:'active'
                      };
                      const stateBefore=JSON.stringify({
                        familyXP:R.familyXP,
                        paths:R.paths,
                        capstone:R.capstone,
                        cash:R.cash,
                        rng:RNG.gameplayState
                      });
                      owQueueResumeRailCapstoneShimmer(R.capstone);
                      if(motion==='no-preference'){
                        await new Promise(resolve=>setTimeout(resolve,1050));
                      }
                      owRenderResumeRail();
                      const coding=document.querySelector(
                        '.resume-family[data-family="Coding"]'
                      );
                      const stateAfter=JSON.stringify({
                        familyXP:R.familyXP,
                        paths:R.paths,
                        capstone:R.capstone,
                        cash:R.cash,
                        rng:RNG.gameplayState
                      });
                      const first={
                        shimmer:coding.classList.contains(
                          'capstone-shimmer'
                        ),
                        animation:getComputedStyle(
                          coding,'::before'
                        ).animationName,
                        markers:familyMarkers.length,
                        markerIcons:new Set(markerIcons).size,
                        markerContained,
                        stateInert:stateBefore===stateAfter
                      };
                      await new Promise(resolve=>setTimeout(resolve,1050));
                      const afterTimeout=coding.classList.contains(
                        'capstone-shimmer'
                      );
                      owRenderResumeRail();
                      const afterRerender=document.querySelector(
                        '.resume-family[data-family="Coding"]'
                      ).classList.contains('capstone-shimmer');
                      owPersistCheckpoint('morning');
                      return{
                        motion,
                        first,
                        afterTimeout,
                        afterRerender,
                        rng:RNG.gameplayState
                      };
                    }""",
                    motion,
                )
                if motion == "no-preference":
                    before_reload = presentation[motion]["rng"]
                    motion_page.reload(wait_until="load", timeout=30_000)
                    motion_page.wait_for_function(READY, timeout=15_000)
                    motion_page.evaluate("void owContinueRun()")
                    motion_page.wait_for_function(
                        "() => !!R && document.querySelector('.resume-family')",
                        timeout=15_000,
                    )
                    presentation[motion]["reload"] = motion_page.evaluate(
                        """before => ({
                          shimmer:document.querySelector(
                            '.resume-family[data-family="Coding"]'
                          ).classList.contains('capstone-shimmer'),
                          capstone:R.capstone,
                          rng:RNG.gameplayState,
                          rngPreserved:RNG.gameplayState===before
                        })""",
                        before_reload,
                    )
                context.close()
        finally:
            browser.close()

    checks = dict(static)
    checks.update(runtime["checks"])
    checks["no_page_errors"] = not page_errors
    checks["responsive_xp_rail"] = (
        responsive["desktop"]["columns"] == 20
        and responsive["compact"]["columns"] == 10
        and responsive["short_landscape"]["columns"] == 20
        and all(
            item["bookSegments"] == 20
            and item["railSegments"] == 0
            and item["overflow"]
            and item["footerContained"]
            and item["markerContained"]
            and item["railHeight"] <= 10
            and item["railWidth"] <= 230.5
            for item in responsive.values()
        )
    )
    checks["resume_presentation_is_inert"] = all(
        item["first"]["stateInert"]
        for item in presentation.values()
    )
    checks["resume_family_markers"] = all(
        item["first"]["markers"] == 5
        and item["first"]["markerIcons"] == 5
        and item["first"]["markerContained"]
        for item in presentation.values()
    )
    checks["capstone_shimmer_once"] = (
        presentation["no-preference"]["first"]["shimmer"]
        and presentation["no-preference"]["first"]["animation"]
        == "resume-capstone-acquired"
        and not presentation["no-preference"]["afterTimeout"]
        and not presentation["no-preference"]["afterRerender"]
        and not presentation["no-preference"]["reload"]["shimmer"]
        and presentation["no-preference"]["reload"]["rngPreserved"]
    )
    checks["capstone_reduced_motion_static"] = (
        not presentation["reduce"]["first"]["shimmer"]
        and presentation["reduce"]["first"]["animation"] == "none"
    )
    detail = {
        "static": static,
        "parsed_cards": ordinary,
        "rarity_counts": rarity_counts,
        "runtime": runtime["evidence"],
        "responsive": responsive,
        "presentation": presentation,
        "page_errors": page_errors,
    }
    print(json.dumps({"checks": checks, "detail": detail}, indent=2))
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        print("FAILED=" + ",".join(failed))
        raise SystemExit(1)
    print("PASS:OFFICEWARS_PHASE5")


if __name__ == "__main__":
    main()
