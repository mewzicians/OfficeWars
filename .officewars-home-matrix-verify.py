#!/usr/bin/env python3
from __future__ import annotations

import json
import hashlib
import os
import sys
from pathlib import Path

temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / ".officewars-python"))

from playwright.sync_api import sync_playwright

GAME = ROOT / "officewarsautobattler.html"
GAME_HASH = hashlib.sha256(GAME.read_bytes()).hexdigest().upper()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        args=["--allow-file-access-from-files", "--disable-extensions"],
    )
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page_errors: list[str] = []
    console_errors: list[str] = []
    page.on("pageerror", lambda error: page_errors.append(str(error)))
    page.on(
        "console",
        lambda message: console_errors.append(message.text)
        if message.type == "error"
        else None,
    )
    page.goto(GAME.as_uri(), wait_until="load", timeout=30_000)
    page.wait_for_function(
        "document.documentElement.dataset.officewarsReady === 'true'",
        timeout=20_000,
    )
    matrix = page.evaluate(
        """async () => {
          const rows=[];
          const add=(kind,id,name,ok,evidence)=>rows.push({
            kind,id,name,verdict:ok?'Pass':'Fail',evidence:cloneForTest(evidence)
          });
          const firstLegal=request=>request.options
            .map((option,index)=>({option,index}))
            .filter(item=>!item.option.disabled)
            .slice(0,request.min)
            .map(item=>item.index);
          const card=id=>{
            const task=TASK_BY_ID.get(id);
            return{task,rarity:task.rarity,source:'generated',modifiers:{}};
          };
          const reset=(seed=992000)=>{
            startRun({seed});
            hideOverlay();
            R.floor=1;R.day=1;R.daysLeft=3;R.stats.days=1;
            R.phase='morningResolution';R.cash=10000;R.stress=0;
            R.homeState=owCreateHomeState();
            owInstallHomeCompatibilityAliases(R);
            R.homeState.levelId='penthouse';
            R.overdelivery.active=false;
            R.manager=MANAGERS.find(item=>item.id==='penny');
            R.today={
              pts:0,stressGain:0,stressRelief:0,pay:0,log:[],
              startStress:0,startProjectProgress:R.project.progress,
              taskPlays:[],cardFlags:{warRooms:[]},actionHistory:[],
              positiveActionTypes:[],scheduleEntries:[],
              naturalSlots:['work','meeting','lunch','mad','slump'],
              homePlans:[]
            };
            owHomeResetFloorState();owHomeResetDailyState();
            nightState=null;OW_currentEntry=null;
            owAutomatedChoiceResolver=null;owResolutionLock=false;
          };
          const acquire=(...ids)=>ids.map(id=>owAcquireHomeItem(
            id,{price:1000,cashPaid:1000,creditPaid:0,financed:false},
            'Matrix'
          ));
          const setupNight=()=>{
            R.phase='night';
            owHomePrepareNight();
            nightState={
              tab:'home',homePanel:'shop',bought:new Set(),
              purchasedDealIds:new Set(),recPicked:false,outingUsed:false,
              outingPid:null,homeUsed:0,homeBlockingPurchases:0,dealUsed:0,
              homeLimit:1+(owHomeSetCompleted('appliance')?1:0),
              dealLimit:0,extraPurchaseCredits:0,
              dealRerollAvailable:false,financeMode:false,panelOpen:false,
              panelMode:'planner',startCash:R.cash,startCredit:0
            };
            R.nightCards=genNightCards();
          };
          const roster=()=>owCurrentRosterIds();

          reset();acquire('coffeeMaker');R.stress=60;
          await owHomePrepareCoffee();
          add('item','coffeeMaker','Questionably Acquired Coffee Maker',
            R.today.homeCoffeeStressReduction===2&&
            owHomeMastery('coffeeMaker').brew===1,
            {reduction:R.today.homeCoffeeStressReduction,mastery:owHomeMastery('coffeeMaker')});

          reset();R.homeState.levelId='apartment';acquire('blackoutCurtains');
          add('item','blackoutCurtains','Blackout Curtains',
            autoSleepAmt()===1,{automaticRecovery:autoSleepAmt()});

          reset();acquire('neglectedHouseplant');
          const plantId=roster()[0];
          owHomeProcessSuccessfulSocial({coworkerId:plantId,success:true},'support');
          add('item','neglectedHouseplant','Neglected Houseplant',
            owHomeMastery('neglectedHouseplant').growth===1&&
            owHomeSalePrice(owHomeDefinition('neglectedHouseplant'))===300,
            {mastery:owHomeMastery('neglectedHouseplant'),
             sale:owHomeSalePrice(owHomeDefinition('neglectedHouseplant'))});

          reset();R.homeState.levelId='apartment';acquire('standingDesk');
          add('item','standingDesk','Standing Desk',
            homeEffectTotal('workProgress')===1,
            {workProgress:homeEffectTotal('workProgress')});

          reset();acquire('emergencySnacks');
          const snack=owResolveOutcome('lunch',false,()=>true);
          add('item','emergencySnacks','Emergency Snack Drawer',
            snack.favorable&&snack.source==='Emergency Snack Drawer'&&
            owHomeCurrentGeneration('emergencySnacks').charges===2,
            {snack,charges:owHomeCurrentGeneration('emergencySnacks').charges});

          reset();R.homeState.levelId='apartment';acquire('router');setupNight();
          R.rerollsNight=1;const routerBefore=R.nightCards.length;
          owHomeReroll();const routerAfter=R.nightCards.length;
          add('item','router','Router With One Good Antenna',
            routerBefore===3&&routerAfter===4,{routerBefore,routerAfter});

          reset();acquire('receiptsShoebox');
          R.today.managerDirective=OW_DIRECTIVE_BY_ID.get('DIR-COST-01');
          R.today.managerPackageAssignments={'offer:0':'negotiate'};
          R.today.managerPackageOrder=['offer:0'];
          const receiptCard=card('readmeUpdate');
          const receiptPkg=owManagerPackageFor(receiptCard,0,'offer');
          add('item','receiptsShoebox','Receipts Shoebox',
            receiptPkg.cost===25,{cost:receiptPkg.cost});

          reset();acquire('stickyNotes');R.phase='morning';
          R.morningCards=[card('readmeUpdate'),card('meetingMinutes'),card('iterationPass')];
          const stickyBefore=R.morningCards[0].task.id;
          const stickyRequests=[];
          owAutomatedChoiceResolver=request=>{
            stickyRequests.push({
              title:request.title,
              options:request.options.map(option=>option.label)
            });
            return firstLegal(request);
          };
          const stickyLockBefore=owResolutionLock;
          const stickyEligible=R.morningCards.filter(item=>
            item.source==='generated'&&!['special','campaign'].includes(item.rarity)
          ).map(item=>item.task.id);
          const stickyResult=await owUseStickyNotes();
          owAutomatedChoiceResolver=null;
          add('item','stickyNotes','Wall of Sticky Notes',
            stickyResult&&R.morningCards[0].task.id!==stickyBefore&&
            owHomeCurrentGeneration('stickyNotes').charges===2,
            {stickyResult,stickyLockBefore,stickyEligible,stickyRequests,
             phase:R.phase,before:stickyBefore,after:R.morningCards[0].task.id,
             charges:owHomeCurrentGeneration('stickyNotes').charges});

          reset();const outingId=roster()[0];
          const baseOuting=owPhase4InvitationPrice(outingId);
          acquire('foldingTable');owHomeResetFloorState();
          const discountedOuting=owPhase4InvitationPrice(outingId);
          add('item','foldingTable','Folding Dining Table',
            baseOuting-discountedOuting===25,
            {baseOuting,discountedOuting});

          reset();acquire('notWorkNotebook');R.today.startStress=0;R.stress=15;
          const journal=[owHomeRecordJournal(),owHomeRecordJournal(),owHomeRecordJournal()];
          add('item','notWorkNotebook','Notebook Marked "NOT WORK"',
            journal[2].ranks===1&&journal[2].entries===0,
            {journal,mastery:owHomeMastery('notWorkNotebook')});

          reset();acquire('comfyMattress');setupNight();R.stress=0;
          nightState.recPicked=true;owApplyNightResolution();
          add('item','comfyMattress','Comfy Mattress',
            R.homeState.wellRestedNext>=5,
            {wellRestedNext:R.homeState.wellRestedNext});

          reset();acquire('ergonomicChair');
          await owCompletePlay(card('actionPlan'),{
            primary:true,selection:true,sourceAncestors:['actionPlan'],setup:{}
          });
          add('item','ergonomicChair','Ergonomic Chair',
            R.stress===7&&R.homeState.daily.ergonomicUsed,
            {stress:R.stress,used:R.homeState.daily.ergonomicUsed});

          reset();R.homeState.levelId='apartment';acquire('savingsAccount');
          setupNight();const depositResult=owHomeDeposit(200);
          add('item','savingsAccount','Savings Account',
            depositResult&&R.homeState.depositCarry.amount===200,
            {carry:R.homeState.depositCarry});

          reset();acquire('gameConsole');setupNight();R.rerollsNight=1;
          owHomeReroll();
          add('item','gameConsole','Game Console',
            R.rerollsNight===1&&R.homeState.daily.consoleRefundUsed,
            {rerolls:R.rerollsNight,used:R.homeState.daily.consoleRefundUsed});

          reset();acquire('robotVacuum');setupNight();R.stress=20;
          R.nightCards=[{offerId:'matrix-buy',upgrade:owHomeDefinition('standingDesk'),purchased:false}];
          R.homeState.catalog={offers:[{offerId:'matrix-buy',itemId:'standingDesk',purchased:false}],rerolls:0};
          const robotBought=await owPurchaseHomeCard(R.nightCards[0],0,1);
          add('item','robotVacuum','Robot Vacuum',
            robotBought&&R.stress===16,{robotBought,stress:R.stress});

          reset();acquire('guestTowels');const towelId=roster()[0];
          const towelBefore=owCoworkerState(towelId).relationship;
          owHomeProcessSuccessfulSocial({coworkerId:towelId,success:true},'rapport');
          const towelAfter=owCoworkerState(towelId).relationship;
          owHomeProcessSuccessfulSocial({coworkerId:towelId,success:true},'rapport');
          add('item','guestTowels','Guest Towels',
            towelAfter-towelBefore===1&&
            owCoworkerState(towelId).relationship===towelAfter,
            {before:towelBefore,after:towelAfter,final:owCoworkerState(towelId).relationship});

          reset();acquire('conferenceBadge');const badgeId=roster()[0];
          const badgeTarget=owHomeLowestStanding(badgeId);
          const badgeBefore=badgeTarget?owCoworkerState(badgeTarget).playerStanding:null;
          owHomeProcessSuccessfulSocial({coworkerId:badgeId,success:true},'support');
          const badgeAfter=badgeTarget?owCoworkerState(badgeTarget).playerStanding:null;
          add('item','conferenceBadge','Framed Conference Badge',
            badgeTarget&&badgeAfter-badgeBefore===2,
            {badgeTarget,badgeBefore,badgeAfter});

          reset();acquire('secondMonitor');
          R.homeState.secondMonitor={day:1,bonus:5,taskName:'Fixture'};
          const monitorBase=owHomeBaseCardPreview(card('actionPlan'),{primary:true});
          const monitorPreview=owCardPreview(card('actionPlan'),{primary:true});
          add('item','secondMonitor','Second Monitor',
            monitorPreview.progress-monitorBase.progress===5,
            {base:monitorBase.progress,withMonitor:monitorPreview.progress});

          reset();acquire('cloudWorkstation');
          const cloudCard=card('readmeUpdate');
          cloudCard.modifiers.homeCloudMarked=true;
          const cloudBase=owHomeBaseCardPreview(cloudCard,{primary:true});
          const cloudPreview=owCardPreview(cloudCard,{primary:true});
          await owCompletePlay(cloudCard,{
            primary:true,selection:true,sourceAncestors:['readmeUpdate'],setup:{}
          });
          add('item','cloudWorkstation','Cloud Workstation',
            cloudPreview.progress-cloudBase.progress===5&&R.familyXP.Coding===2,
            {bonus:cloudPreview.progress-cloudBase.progress,xp:R.familyXP.Coding});

          reset();acquire('library');
          owHomeMastery('library').catalog=[
            'readmeUpdate','meetingMinutes','iterationPass','expenseAllowance','processAudit'
          ];
          owAutomatedChoiceResolver=firstLegal;const libraryBefore={...R.familyXP};
          await owHomeUseLibrary();owAutomatedChoiceResolver=null;
          const libraryGain=Object.keys(R.familyXP).reduce(
            (sum,key)=>sum+(R.familyXP[key]-libraryBefore[key]),0
          );
          add('item','library','Library',
            libraryGain===3&&owHomeMastery('library').catalog.length===0,
            {libraryGain,catalog:owHomeMastery('library').catalog});

          reset();acquire('homeGym');R.stress=55;
          owApplyStressPackage(5,0,{source:'Matrix'});
          add('item','homeGym','Home Gym',
            R.stress===50&&R.homeState.daily.gymUsed&&
            owHomeCurrentGeneration('homeGym').counters.threshold===65,
            {stress:R.stress,generation:owHomeCurrentGeneration('homeGym')});

          reset();acquire('jacuzzi');const jacuzziIds=roster().slice(0,3);
          jacuzziIds.forEach(id=>owHomeProcessSuccessfulSocial(
            {coworkerId:id,success:true},'support'
          ));
          OW_currentEntry={homePartyCrew:true};
          const jacuzziOutcome=owResolveOutcome('meeting',false,()=>false);
          add('item','jacuzzi','Jacuzzi',
            R.homeState.floor.partyCrew.length===3&&jacuzziOutcome.favorable,
            {crew:R.homeState.floor.partyCrew,outcome:jacuzziOutcome});

          reset();acquire('corkboard');const corkSource=roster()[0];
          owHomeProcessSuccessfulSocial({coworkerId:corkSource,success:true},'support');
          const corkTarget=R.homeState.floor.corkboardLinks[corkSource];
          const corkBefore=corkTarget?owCoworkerState(corkTarget).relationship:null;
          owGainRelationship(corkSource,2,'Matrix');
          const corkAfter=corkTarget?owCoworkerState(corkTarget).relationship:null;
          add('item','corkboard','Business Card Corkboard',
            corkTarget&&corkAfter-corkBefore===1,
            {corkSource,corkTarget,corkBefore,corkAfter});

          reset();acquire('homeOffice');
          R.homeState.remoteTask={
            day:1,taskId:'actionPlan',taskName:'Action Plan',
            card:card('actionPlan'),context:{},settled:false
          };
          const remoteBefore=R.project.progress;
          await owHomeResolveRemoteTask();
          add('item','homeOffice','Home Office',
            R.homeState.remoteTask.settled&&
            R.project.progress-remoteBefore===TASK_BY_ID.get('actionPlan').progress&&
            R.familyXP.Management===0,
            {gain:R.project.progress-remoteBefore,xp:R.familyXP.Management});

          reset();acquire('personalAssistant');R.phase='night';
          owAutomatedChoiceResolver=firstLegal;
          await owHomeChooseAssistantPrep();owAutomatedChoiceResolver=null;
          R.morningCards=[card('readmeUpdate'),card('meetingMinutes'),card('iterationPass')];
          const assistantFamily=R.homeState.assistantPrep.family;
          owHomeApplyAssistantFamily();
          add('item','personalAssistant','Personal Assistant',
            R.homeState.assistantPrep.consumed&&
            R.morningCards.some(item=>item.task.family===assistantFamily),
            {prep:R.homeState.assistantPrep,cards:R.morningCards.map(item=>item.task.family)});

          reset();acquire('espressoMachine');
          const espressoEntry={repeats:0};
          owAfterAction('work',{g:true},espressoEntry);
          const espressoSecond={repeats:0};
          owAfterAction('work',{g:true},espressoSecond);
          add('item','espressoMachine','Espresso Machine',
            espressoEntry.repeats===1&&espressoSecond.repeats===0,
            {first:espressoEntry,second:espressoSecond,used:R.homeState.daily.espressoUsed});

          reset();acquire('guestSuite');const suiteId=roster()[0];
          const suiteBefore=owCoworkerState(suiteId).relationship;
          owHomeProcessSuccessfulSocial({coworkerId:suiteId,success:true},'support');
          add('item','guestSuite','Guest Suite',
            owCoworkerState(suiteId).relationship-suiteBefore===1&&
            owCoworkerState(suiteId).blockNextChadGain&&
            R.homeState.guestPass.coworkerId===suiteId,
            {before:suiteBefore,after:owCoworkerState(suiteId),
             pass:R.homeState.guestPass});

          reset();acquire('smartHomeHub');let hubCount=0;
          owHomeTriggerNumeric('robotVacuum',()=>hubCount++);
          owHomeTriggerNumeric('robotVacuum',()=>hubCount++);
          add('item','smartHomeHub','Smart Home Hub',
            hubCount===3&&R.homeState.daily.smartHubUsed===1,
            {hubCount,used:R.homeState.daily.smartHubUsed});

          reset();acquire('coffeeMaker','blackoutCurtains');
          add('set','energy','Energy',
            owHomeSetCompleted('energy')&&homeEffectTotal('extraScheduleEntries')===1,
            {profile:owHomeSetProfile().find(item=>item.id==='energy'),
             entries:homeEffectTotal('extraScheduleEntries')});

          reset();R.homeState.levelId='house';
          acquire('receiptsShoebox','savingsAccount');
          R.today.interestEarned=100;R.homeState.equity=0;owHomePrepareNight();
          const finBase=R.homeState.equity;
          reset();R.homeState.levelId='house';
          acquire('receiptsShoebox','savingsAccount',
            'router','gameConsole','cloudWorkstation');
          R.today.interestEarned=100;R.homeState.equity=0;owHomePrepareNight();
          const finConnected=R.homeState.equity;
          add('set','financial','Financial Foundation',
            finBase===50&&finConnected===75,{finBase,finConnected});

          reset();acquire('coffeeMaker','gameConsole','robotVacuum');setupNight();
          add('set','appliance','Appliance Suite',
            owHomeSetCompleted('appliance')&&nightState.homeLimit===2,
            {profile:owHomeSetProfile().find(item=>item.id==='appliance'),
             homeLimit:nightState.homeLimit});

          reset();R.homeState.levelId='penthouse';
          acquire('blackoutCurtains','neglectedHouseplant','emergencySnacks');
          setupNight();R.stress=0;nightState.recPicked=false;owApplyNightResolution();
          const wellnessBase=R.homeState.wellRestedNext;
          reset();R.homeState.levelId='penthouse';
          acquire('blackoutCurtains','neglectedHouseplant','emergencySnacks',
            'router','gameConsole','cloudWorkstation');
          setupNight();R.stress=0;nightState.recPicked=false;owApplyNightResolution();
          const wellnessConnected=R.homeState.wellRestedNext;
          add('set','wellness','Wellness',
            wellnessBase===5&&wellnessConnected===7,
            {wellnessBase,wellnessConnected});

          reset();acquire('foldingTable','guestTowels','jacuzzi');
          const hospitalityPool=owHomeGatheringGuests();
          acquire('router','gameConsole','cloudWorkstation');
          const hospitalityConnected=owHomeGatheringGuests();
          add('set','hospitality','Hospitality',
            owHomeSetCompleted('hospitality')&&
            hospitalityPool.length<=3&&
            hospitalityConnected.length===roster().length,
            {hospitalityPool,hospitalityConnected});

          reset();acquire('conferenceBadge','corkboard','guestSuite');
          const networkId=roster()[0];
          owCoworkerState(networkId).playerStanding=50;
          owCoworkerState(networkId).chadStanding=50;
          owAutomatedChoiceResolver=firstLegal;
          await owHomeMaybeNetworkingFollowUp({coworkerId:networkId});
          owAutomatedChoiceResolver=null;
          const networkBase=owCoworkerState(networkId).playerStanding;
          reset();acquire('conferenceBadge','corkboard','guestSuite',
            'router','gameConsole','cloudWorkstation');
          const networkConnectedId=roster()[0];
          owCoworkerState(networkConnectedId).playerStanding=50;
          owCoworkerState(networkConnectedId).chadStanding=50;
          owAutomatedChoiceResolver=firstLegal;
          await owHomeMaybeNetworkingFollowUp({coworkerId:networkConnectedId});
          owAutomatedChoiceResolver=null;
          const networkConnected=owCoworkerState(networkConnectedId).playerStanding;
          add('set','networking','Networking',
            networkBase===55&&networkConnected===58,
            {networkBase,networkConnected});

          reset();acquire('router','gameConsole','cloudWorkstation');
          const connectedProfile=owHomeSetProfile();
          add('set','connected','Connected Home',
            owHomeConnectedActive()&&
            connectedProfile.find(item=>item.id==='connected').complete,
            {connectedProfile});

          reset();acquire('standingDesk','ergonomicChair','secondMonitor','cloudWorkstation');
          const workspaceCard=card('actionPlan');
          const workspaceBase=owHomeBaseCardPreview(workspaceCard,{primary:true});
          const workspacePreview=owCardPreview(workspaceCard,{primary:true});
          reset();acquire('standingDesk','ergonomicChair','secondMonitor','cloudWorkstation',
            'router','gameConsole','espressoMachine');
          const workspaceConnectedBase=owHomeBaseCardPreview(workspaceCard,{primary:true});
          const workspaceConnected=owCardPreview(workspaceCard,{primary:true});
          add('set','workspace','Workspace',
            workspacePreview.progress-workspaceBase.progress===3&&
            workspacePreview.rawStress===workspaceBase.rawStress-1&&
            workspaceConnected.progress-workspaceConnectedBase.progress===3&&
            workspaceConnected.rawStress===workspaceConnectedBase.rawStress-2,
            {base:workspaceBase,workspace:workspacePreview,
             connectedBase:workspaceConnectedBase,connected:workspaceConnected});

          reset();acquire('receiptsShoebox','stickyNotes','notWorkNotebook','library');
          R.phase='night';owAutomatedChoiceResolver=request=>{
            if(request.title.includes('Plans')){
              request.matrixOptionCount=request.options.length;
            }
            return firstLegal(request);
          };
          let planningOptionCount=0;
          owAutomatedChoiceResolver=request=>{
            if(request.title.includes('Plans'))planningOptionCount=request.options.length;
            return firstLegal(request);
          };
          await owHomeChoosePlans();owAutomatedChoiceResolver=null;
          const planningBase={options:planningOptionCount,plans:R.homeState.plans.length};
          reset();acquire('receiptsShoebox','stickyNotes','notWorkNotebook','library',
            'router','gameConsole','cloudWorkstation','personalAssistant');
          R.phase='night';let planningSuperOptions=0;
          owAutomatedChoiceResolver=request=>{
            if(request.title.includes('Plans')){
              planningSuperOptions=request.options.length;
              return[0,2];
            }
            return firstLegal(request);
          };
          await owHomeChoosePlans();owAutomatedChoiceResolver=null;
          const planningSuper={options:planningSuperOptions,plans:R.homeState.plans.length};
          add('set','planning','Planning',
            planningBase.options===2&&planningBase.plans===1&&
            planningSuper.options===6&&planningSuper.plans===2,
            {planningBase,planningSuper});

          reset();R.homeState.levelId='apartment';
          const first=owAcquireHomeItem('standingDesk',
            {price:400,cashPaid:400,creditPaid:0,financed:false},'Matrix');
          acquire('blackoutCurtains','neglectedHouseplant');
          const held=owAcquireHomeItem('ergonomicChair',
            {price:600,cashPaid:600,creditPaid:0,financed:false},'Matrix',{held:true});
          const sold=window.doSellUpgrade('standingDesk');
          add('lifecycle','held-activation','Held item activation',
            first&&held.status==='active'&&sold.activated?.itemId==='ergonomicChair',
            {first,held,sold});

          reset();acquire('notWorkNotebook');
          owHomeMastery('notWorkNotebook').ranks=2;
          window.doSellUpgrade('notWorkNotebook');
          owAcquireHomeItem('notWorkNotebook',
            {price:500,cashPaid:500,creditPaid:0,financed:false},'Reacquire');
          add('lifecycle','mastery-reacquisition','Mastery survives reacquisition',
            owHomeMastery('notWorkNotebook').ranks===2,
            {mastery:owHomeMastery('notWorkNotebook')});

          return{
            rows,
            counts:{
              items:rows.filter(row=>row.kind==='item').length,
              sets:rows.filter(row=>row.kind==='set').length,
              lifecycle:rows.filter(row=>row.kind==='lifecycle').length
            }
          };
        }"""
    )
    browser.close()

failed = [row for row in matrix["rows"] if row["verdict"] != "Pass"]
result = {
    "hash": GAME_HASH,
    "counts": matrix["counts"],
    "passed": len(matrix["rows"]) - len(failed),
    "failed": len(failed),
    "rows": matrix["rows"],
    "pageErrors": page_errors,
    "consoleErrors": console_errors,
}
print("HOME_MATRIX_JSON=" + json.dumps(result, separators=(",", ":")))
if failed or page_errors or console_errors:
    print("FAILED=" + ",".join(row["id"] for row in failed))
    raise SystemExit(1)
print(
    f"PASS:HOME_MATRIX items={matrix['counts']['items']} "
    f"sets={matrix['counts']['sets']} lifecycle={matrix['counts']['lifecycle']}"
)
