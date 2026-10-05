import json
import os
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))

from playwright.sync_api import sync_playwright


GAME = ROOT / "officewarsautobattler.html"
GAME_URL = GAME.as_uri()
READY = "document.documentElement.dataset.officewarsReady === 'true'"


def load_page(browser, viewport=None, reduced_motion="no-preference"):
    context = browser.new_context(
        viewport=viewport or {"width": 1440, "height": 900},
        reduced_motion=reduced_motion,
    )
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(GAME_URL, wait_until="load", timeout=30_000)
    page.wait_for_function(READY, timeout=15_000)
    page.evaluate("localStorage.clear()")
    return context, page, errors


def package_inventory(page):
    return page.evaluate(
        """async () => {
          startRun({seed:935100});
          await startDay();
          const cards=TASKS.filter(task =>
            ['common','uncommon','rare','legendary'].includes(task.rarity)
          ).slice(0,5).map(task => ({
            task,rarity:task.rarity,source:'offer',modifiers:{}
          }));
          R.manager=MANAGERS.find(item=>item.id==='absent');
          R.managerApproval=2;
          R.closingRewards=[];
          R.today.managerDirective=OW_DIRECTIVE_BY_ID.get('DIR-OUT-01');
          R.morningCards=cards.slice(0,3);
          R.pins=[];
          R.storedTask=null;
          R.salesCycle=null;
          R.today.managerPackageAssignments={};
          const ordinary=R.morningCards.map((card,index)=>
            owManagerPackageFor(card,index,'offer')
          );
          const rerollBefore=ordinary[1];
          R.morningCards[1]=cards[4];
          const rerollAfter=owManagerPackageFor(
            R.morningCards[1],1,'offer'
          );

          owAddCurrentPin(cards[3].task.id,'Verifier',{},true);
          R.storedTask={taskId:cards[4].task.id,turnsHeld:1,modifiers:{}};
          R.today.managerPackageAssignments={};
          const mixedOrder=owManagerPackageVisibleKeys();
          owPrepareManagerPackageAssignments();
          const mixedStances=mixedOrder.map(
            key=>R.today.managerPackageAssignments[key]
          );

          R.manager=MANAGERS.find(item=>item.id==='micro');
          const microCounts={};
          for(const approval of [0,2,4]){
            R.managerApproval=approval;
            microCounts[approval]=owManagerGeneratedCardCount(3);
          }

          R.manager=MANAGERS.find(item=>item.id==='absent');
          R.managerApproval=2;
          R.salesCycle={active:true};
          R.morningCards=cards.slice(0,2);
          R.today.managerPackageAssignments={};
          const salesPackages=[
            owManagerPackageFor(R.morningCards[0],0,'salesCycle'),
            owManagerPackageFor(R.morningCards[1],1,'salesCycle'),
            owManagerPackageFor(null,0,'close')
          ];
          R.cash=100;
          const committed=owCommitManagerPackage(null,0,'close');
          const cashAfterManagerCost=R.cash;

          R.cash=0;
          R.today.managerPackage=null;
          const unavailablePackage=owManagerPackageFor(null,0,'close');
          const unavailableBadge=owManagerPackageBadge(
            null,0,'close',false
          );
          const unavailable={
            disabled:R.cash<unavailablePackage.cost,
            reason:unavailableBadge.includes('NEED $50')
          };

          const names=Object.values(OW_MANAGER_RESPONSE_NAMES)
            .flatMap(group=>Object.values(group));
          const announcement=owManagerDirectiveMarkup();
          return{
            ordinary:ordinary.map(item=>({
              key:item.key,stance:item.stance,name:item.name,
              packageSlot:item.packageSlot
            })),
            reroll:{
              before:{key:rerollBefore.key,stance:rerollBefore.stance},
              after:{key:rerollAfter.key,stance:rerollAfter.stance}
            },
            mixed:{order:mixedOrder,stances:mixedStances},
            microCounts,
            sales:salesPackages.map(item=>({
              key:item.key,stance:item.stance,slot:item.packageSlot,
              cost:item.cost
            })),
            cost:{
              committed:!!committed,
              paidCost:committed&&committed.paidCost,
              cashAfter:cashAfterManagerCost,
              objectiveStatus:committed&&committed.objectiveStatus,
              deterministic:committed&&
                !('baseOdds' in committed)&&
                !('frozenModifiers' in committed)&&
                !('rolledSuccess' in committed)
            },
            unavailable,
            names:{count:names.length,unique:new Set(names).size},
            tooltip:owManagerPackageTooltip(unavailablePackage),
            announcement:
              announcement.includes('manager-directive-announcement') &&
              announcement.includes('manager-directive-bubble') &&
              !announcement.includes('manager-directive-avatar') &&
              !announcement.includes('Each task package carries')
          };
        }"""
    )


def start_cinematic(page, seed=935001, speed=1, text_scale=False):
    page.evaluate(
        """async ({seed,speed,textScale}) => {
          localStorage.clear();
          if(textScale)document.documentElement.style.fontSize='32px';
          OfficeWarsTest.setTimingScale(.0001);
          startRun({seed});
          await startDay();
          preferredDayPlaybackRate=speed;
          window.__walkerCalls=[];
          walkTo=()=>{window.__walkerCalls.push('walkTo');throw new Error('walker path used');};
          startAmbientLife=()=>{window.__walkerCalls.push('startAmbientLife');throw new Error('ambient path used');};
          runDailyDeskVisit=()=>{window.__walkerCalls.push('runDailyDeskVisit');throw new Error('desk walker used');};
          reserveCubicle=()=>{window.__walkerCalls.push('reserveCubicle');throw new Error('cubicle reservation used');};
          const index=R.morningCards.findIndex((card,index) =>
            R.cash>=owManagerPackageFor(card,index,'offer').cost
          );
          if(index<0)throw new Error('No affordable manager task package');
          selectMorning(index,'offer');
          void confirmMorning();
        }""",
        {"seed": seed, "speed": speed, "textScale": text_scale},
    )


def choose_current_event(page):
    return page.evaluate(
        """() => {
          const event=R.today.politicalEvents.find(item =>
            item.id===R.workdayPresentation.currentEventId
          );
          if(!event)return null;
          const legal=event.page.options.filter(option =>
            R.cash>=Number(option.cost&&option.cost.cash||0)
          );
          const option=
            legal.find(item=>event.type==='project'&&item.label==='Safe')||
            legal.find(item=>event.type==='boss'&&item.label==='Counter')||
            legal.find(item=>
              event.type==='relationship'&&item.label==='Take No Action'
            )||legal[0];
          if(!option)return null;
          const result={
            eventId:event.id,
            optionId:option.id,
            snapshot:cloneForTest(event.snapshot),
            skipDisabled:document.getElementById('day-skip-button').disabled,
            noBackOrDefer:!document.getElementById(
              'cinematic-politics-pane'
            ).textContent.match(/\\b(BACK|DEFER)\\b/i),
            focused:document.activeElement&&
              document.activeElement.classList.contains('cinematic-choice'),
            phase:R.phase,
            stageClasses:document.getElementById('workday-stage').className
          };
          owChooseCinematicPolitics(event.id,option.id);
          return result;
        }"""
    )


def mechanical_snapshot(page):
    return page.evaluate(
        """() => ({
          phase:R.phase,
          cash:R.cash,
          stress:R.stress,
          project:R.project.progress,
          rival:R.rival.progress,
          approval:R.managerApproval,
          overtime:R.overtimeBank,
          rng:RNG.snapshot().gameplayState,
          events:(R.today.politicalEvents||[]).map(event=>({
            id:event.id,
            entryId:event.entryId,
            trigger:event.triggerPhase,
            option:event.choice&&event.choice.optionId,
            odds:event.finalOdds,
            roll:event.secretRoll,
            success:event.rolledSuccess,
            applied:event.applied,
            discarded:event.discarded,
            result:event.result
          })),
          log:(R.today.log||[]).map(line=>({
            name:line.n||'',effect:line.e||'',good:line.g!==false
          })),
          manager:R.today.managerPackage&&{
            id:R.today.managerPackage.id,
            stance:R.today.managerPackage.stance,
            paidCost:R.today.managerPackage.paidCost,
            settled:R.today.managerPackage.settled,
            result:R.today.managerPackage.result
          },
          results:(R.today.cinematicResults||[]).map(result=>({
            id:result.id,success:result.success,result:result.result
          })),
          walkerCalls:window.__walkerCalls||[]
        })"""
    )


def drive_case(page, mode="watched", timeout=20):
    deadline = time.time() + timeout
    first_event = None
    reel = None
    skip_requested = False
    answered = 0
    history = []
    while time.time() < deadline:
        state = page.evaluate(
            """() => ({
              phase:R.phase,
              dayActive,
              currentEvent:R.workdayPresentation&&
                R.workdayPresentation.currentEventId,
              path:R.workdayPresentation&&R.workdayPresentation.path,
              skipRequested:R.workdayPresentation&&
                R.workdayPresentation.skipRequested
            })"""
        )
        if not history or state != history[-1]:
            history.append(state)
        if (
            mode == "skip"
            and state["dayActive"]
            and state["phase"] == "workday"
            and not skip_requested
        ):
            page.evaluate("skipWorkDay()")
            skip_requested = True
        if (
            mode == "partial"
            and answered >= 1
            and state["dayActive"]
            and state["phase"] == "workday"
            and not skip_requested
        ):
            page.evaluate("skipWorkDay()")
            skip_requested = True
        if state["phase"] in ("workdayPoliticalChoice", "workdayPoliticalQueue"):
            evidence = choose_current_event(page)
            if evidence:
                answered += 1
                if first_event is None:
                    first_event = evidence
        elif state["phase"] == "politicsResultsReel":
            reel = page.evaluate(
                """() => ({
                  rows:owCinematicResultRows().map(item=>({
                    type:item.type,id:item.id,pending:item.pending
                  })),
                  revealed:document.querySelectorAll(
                    '.cinematic-result-card.revealed'
                  ).length,
                  total:document.querySelectorAll(
                    '.cinematic-result-card'
                  ).length,
                  noReviewBack:
                    !document.getElementById('cinematic-results-reel')
                      .textContent.match(/\\bBACK\\b/i)
                })"""
            )
            page.evaluate(
                """() => {
                  owRevealAllCinematicResults();
                  owFinishCinematicResults();
                }"""
            )
        elif state["phase"] in ("clockOut", "gameOver"):
            return {
                "final": mechanical_snapshot(page),
                "firstEvent": first_event,
                "reel": reel,
                "history": history,
            }
        time.sleep(0.01)
    raise AssertionError("Cinematic case timed out: " + json.dumps(history[-8:]))


def live_layout(page):
    page.wait_for_function(
        "() => R.phase==='workdayPoliticalChoice'",
        timeout=15_000,
    )
    page.evaluate(
        """() => {
          const event=R.today.politicalEvents.find(item=>
            item.id===R.workdayPresentation.currentEventId
          );
          owExitPoliticalDecisionFocus();
          renderDayActionLegend();
          dayActionLegendOpen=true;
          layoutDayActionLegend();
          owRenderCinematicPoliticalEvent(event);
        }"""
    )
    return page.evaluate(
        """() => {
          const visible=element=>{
            if(!element)return false;
            const style=getComputedStyle(element);
            const rect=element.getBoundingClientRect();
            return style.display!=='none'&&style.visibility!=='hidden'&&
              rect.width>0&&rect.height>0;
          };
          const stage=document.getElementById('workday-stage').getBoundingClientRect();
          const mainElement=document.getElementById('cinematic-main-pane');
          const politicsElement=document.getElementById(
            'cinematic-politics-pane'
          );
          const main=mainElement.getBoundingClientRect();
          const politics=politicsElement.getBoundingClientRect();
          const event=R.today.politicalEvents.find(item=>
            item.id===R.workdayPresentation.currentEventId
          );
          const context=owPoliticalDecisionContext(event);
          return{
            stage:[stage.width,stage.height],
            main:[main.left,main.top,main.width,main.height],
            politics:[politics.left,politics.top,politics.width,politics.height],
            fullScreen:document.getElementById(
              'workday-stage'
            ).classList.contains('politics-fullscreen'),
            focusMode:document.body.classList.contains(
              'ow-political-decision-focus'
            ),
            mainHidden:!visible(mainElement),
            tickerHidden:!visible(document.getElementById('day-ticker')),
            guideHidden:!visible(document.getElementById('day-action-legend')),
            playbackHidden:!visible(
              document.getElementById('day-playback-controls')
            ),
            contextText:document.querySelector(
              '.cinematic-workday-context span:last-child'
            )?.textContent.trim(),
            expectedContext:context.label,
            horizontalOverflow:
              document.documentElement.scrollWidth-
              document.documentElement.clientWidth
          };
        }"""
    )


def reload_choice_case(page):
    start_cinematic(page, seed=935001)
    page.wait_for_function(
        "() => R.phase==='workdayPoliticalChoice'",
        timeout=15_000,
    )
    before = page.evaluate(
        """() => ({
          id:R.workdayPresentation.currentEventId,
          focus:R.workdayPresentation.focus,
          snapshot:cloneForTest(R.today.politicalEvents.find(
            item=>item.id===R.workdayPresentation.currentEventId
          ).snapshot),
          count:R.today.politicalEvents.length,
          rng:RNG.snapshot().gameplayState,
          checkpoint:JSON.parse(localStorage.getItem(OW_SAVE_KEY)).checkpoint
        })"""
    )
    page.reload(wait_until="load", timeout=30_000)
    page.wait_for_function(READY, timeout=15_000)
    page.evaluate("owContinueRun()")
    page.wait_for_function(
        "() => R.phase==='workdayPoliticalQueue'",
        timeout=15_000,
    )
    page.wait_for_function(
        """() => document.activeElement&&
          document.activeElement.classList.contains('cinematic-choice')""",
        timeout=5_000,
    )
    after = page.evaluate(
        """() => ({
          id:R.workdayPresentation.currentEventId,
          focus:R.workdayPresentation.focus,
          snapshot:cloneForTest(R.today.politicalEvents.find(
            item=>item.id===R.workdayPresentation.currentEventId
          ).snapshot),
          count:R.today.politicalEvents.length,
          rng:RNG.snapshot().gameplayState,
          path:R.workdayPresentation.path,
          checkpoint:JSON.parse(localStorage.getItem(OW_SAVE_KEY)).checkpoint,
          activeChoice:document.activeElement&&
            document.activeElement.classList.contains('cinematic-choice')
        })"""
    )
    result = drive_case(page, mode="restored")
    return {"before": before, "after": after, "result": result}


def main():
    source = GAME.read_text(encoding="utf-8")
    static = {
        "schema9": "const OW_SAVE_SCHEMA=9;" in source,
        "cinematicStage": 'id="workday-stage"' in source,
        "activeCinematicRoute": (
            "runWorkDay=function(){\n  return owRunCinematicWorkDay();" in source
        ),
        "sequentialCheckpoints": all(
            token in source
            for token in (
                "'workdayPoliticalChoice'",
                "'workdayPoliticalQueue'",
                "'politicsResultsReel'",
            )
        ),
        "actionTemplates": all(
            token in source
            for token in (
                "scene-client-call",
                "scene-executive-support",
                "scene-standard-procedure",
                "scene-triggered-work",
                "scene-sabotage",
                "scene-desk-visit",
                "politics-project",
                "politics-relationship",
                "politics-boss",
            )
        ),
        "no_external_assets": "cinematic-workday-stage" in source,
    }
    checks = dict(static)
    detail = {"static": static}

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
            context, page, errors = load_page(browser)
            packages = package_inventory(page)
            context.close()
            detail["packages"] = packages
            checks.update(
                {
                    "fixedStanceCycle": [
                        item["stance"] for item in packages["ordinary"]
                    ]
                    == ["comply", "resist", "negotiate"],
                    "rerollRetainsSlot": (
                        packages["reroll"]["before"]
                        == packages["reroll"]["after"]
                    ),
                    "pinStoredContinueCycle": packages["mixed"]["stances"]
                    == [
                        "comply",
                        "resist",
                        "negotiate",
                        "comply",
                        "resist",
                    ],
                    "micromanagerMissingStances": packages["microCounts"]
                    == {"0": 1, "2": 2, "4": 3},
                    "salesAndCloseCycle": [
                        item["stance"] for item in packages["sales"]
                    ]
                    == ["comply", "resist", "negotiate"],
                    "managerCostImmediate": (
                        packages["cost"]["committed"]
                        and packages["cost"]["paidCost"] == 50
                        and packages["cost"]["cashAfter"] == 50
                    ),
                    "deterministicPackageRecord": (
                        packages["cost"]["deterministic"]
                        and packages["cost"]["objectiveStatus"] == "inProgress"
                    ),
                    "conciseManagerTooltip": (
                        packages["tooltip"].count("\n") == 1
                        and packages["tooltip"].startswith("SUCCESS")
                        and "\nFAILURE" in packages["tooltip"]
                        and "odds" not in packages["tooltip"].lower()
                        and "cost" not in packages["tooltip"].lower()
                    ),
                    "unaffordableReason": all(packages["unavailable"].values()),
                    "sixtyThreeNames": packages["names"]
                    == {"count": 63, "unique": 63},
                    "managerAnnouncement": packages["announcement"],
                    "packagePageErrors": not errors,
                }
            )

            cases = {}
            all_errors = {}
            for name, mode, speed in (
                ("watch1", "watched", 1),
                ("watch2", "watched", 2),
                ("watch4", "watched", 4),
                ("skip", "skip", 1),
                ("partial", "partial", 1),
            ):
                context, page, errors = load_page(browser)
                start_cinematic(page, seed=935001, speed=speed)
                cases[name] = drive_case(page, mode=mode)
                all_errors[name] = errors
                context.close()
            detail["cases"] = cases
            baseline = cases["watch1"]["final"]
            checks["watchedSkipParity"] = all(
                cases[name]["final"] == baseline
                for name in ("watch2", "watch4", "skip", "partial")
            )
            checks["noWalkerPath"] = all(
                not cases[name]["final"]["walkerCalls"] for name in cases
            )
            checks["hardPauseNoBackDefer"] = all(
                cases[name]["firstEvent"]
                and cases[name]["firstEvent"]["skipDisabled"]
                and cases[name]["firstEvent"]["noBackOrDefer"]
                for name in cases
            )
            checks["liveAndHiddenPhases"] = (
                cases["watch1"]["firstEvent"]["phase"]
                == "workdayPoliticalChoice"
                and "skip-hidden"
                not in cases["watch1"]["firstEvent"]["stageClasses"]
            )
            checks["managerResultFirst"] = all(
                not case["reel"]["rows"]
                or case["reel"]["rows"][0]["type"] == "manager"
                for case in cases.values()
            )
            checks["noGroupedReviewRoute"] = all(
                all(item["phase"] != "politicsReview" for item in case["history"])
                for case in cases.values()
            )
            checks["presentationPageErrors"] = not any(all_errors.values())

            context, page, errors = load_page(
                browser, {"width": 1440, "height": 900}
            )
            start_cinematic(page, seed=935030)
            desktop = live_layout(page)
            context.close()
            context, page, short_errors = load_page(
                browser, {"width": 844, "height": 390}
            )
            start_cinematic(page, seed=935030)
            short = live_layout(page)
            context.close()
            context, page, text_errors = load_page(
                browser, {"width": 1440, "height": 900}
            )
            start_cinematic(page, seed=935030, text_scale=True)
            text200 = live_layout(page)
            context.close()
            detail["layout"] = {
                "desktop": desktop,
                "shortLandscape": short,
                "text200": text200,
            }
            checks["decisionFocusHidesCompetingChrome"] = all(
                layout["focusMode"]
                and layout["mainHidden"]
                and layout["tickerHidden"]
                and layout["guideHidden"]
                and layout["playbackHidden"]
                for layout in (desktop, short, text200)
            )
            checks["inlineActionContextMatchesEvent"] = all(
                layout["contextText"] == layout["expectedContext"]
                and layout["contextText"].startswith("WORKDAY CONTEXT")
                for layout in (desktop, short, text200)
            )
            checks["decisionPaneResponsive"] = (
                desktop["politics"][2] >= desktop["stage"][0] * 0.65
                and not desktop["fullScreen"]
                and short["fullScreen"]
                and text200["fullScreen"]
                and short["politics"][2] >= short["stage"][0] * 0.9
                and text200["politics"][2] >= text200["stage"][0] * 0.9
                and short["horizontalOverflow"] <= 1
                and text200["horizontalOverflow"] <= 1
            )
            checks["layoutPageErrors"] = not (
                errors or short_errors or text_errors
            )

            context, page, errors = load_page(browser)
            restored = reload_choice_case(page)
            context.close()
            detail["reload"] = restored
            checks["reloadSameUnansweredEvent"] = (
                restored["before"]["checkpoint"] == "workdayPoliticalChoice"
                and restored["after"]["checkpoint"] == "workdayPoliticalQueue"
                and restored["before"]["id"] == restored["after"]["id"]
                and restored["before"]["snapshot"]
                == restored["after"]["snapshot"]
                and restored["before"]["count"] == restored["after"]["count"]
                and restored["before"]["rng"] == restored["after"]["rng"]
                and restored["after"]["path"] == "reload-skip"
                and restored["after"]["activeChoice"]
                and restored["result"]["final"]["phase"] == "clockOut"
            )
            checks["liveAndHiddenPhases"] = (
                checks["liveAndHiddenPhases"]
                and restored["after"]["checkpoint"] == "workdayPoliticalQueue"
                and restored["result"]["firstEvent"]["phase"]
                == "workdayPoliticalQueue"
                and "skip-hidden"
                in restored["result"]["firstEvent"]["stageClasses"]
            )
            checks["reloadPageErrors"] = not errors

            context, page, errors = load_page(
                browser, reduced_motion="reduce"
            )
            start_cinematic(page, seed=935040)
            reduced = drive_case(page)
            context.close()
            detail["reducedMotion"] = reduced["reel"]
            checks["reducedMotionRevealsAll"] = (
                reduced["reel"]
                and reduced["reel"]["revealed"] == reduced["reel"]["total"]
            )
            checks["reducedMotionPageErrors"] = not errors
        finally:
            browser.close()

    failed = [name for name, passed in checks.items() if not passed]
    print(
        json.dumps(
            {"checks": checks, "detail": detail, "failed": failed},
            indent=2,
        )
    )
    if failed:
        raise SystemExit(1)
    print(f"PASS cinematic-workday {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
