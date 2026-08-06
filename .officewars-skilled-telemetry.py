import json
import os
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
GAME_URL = (ROOT / "officewarsautobattler.html").as_uri()
RUNS = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
START_SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 1110000


TELEMETRY_AUDIT = r"""
async ({runs, startSeed}) => {
  const output = [];
  let current = null;

  const stateSnapshot = () => ({
    phase: R.phase,
    floor: R.floor,
    floorDay: R.day,
    runDay: R.stats.days,
    stress: R.stress,
    cash: R.cash,
    cashEarned: R.stats.cashEarned,
    progress: R.project.progress,
    projectSize: R.project.size,
    rivalProgress: R.rival.progress,
    daysLeft: R.daysLeft,
    manager: R.manager && R.manager.id,
    taskId: R.todayCard && R.todayCard.task && R.todayCard.task.id,
    familyXP: Object.assign({}, R.familyXP),
    paths: Object.assign({}, R.paths)
  });

  const recordBurnout = detail => {
    if (!current || current.burnout) return;
    current.burnout = Object.assign(stateSnapshot(), detail || {});
  };

  const originalStressPackage = owApplyStressPackage;
  owApplyStressPackage = function(rawGain, recovery, options) {
    const opts = Object.assign(
      {flat: false, source: 'Stress', check: true},
      options || {}
    );
    const pending = {
      source: opts.source,
      rawGain: Number(rawGain) || 0,
      recovery: Number(recovery) || 0,
      flat: !!opts.flat,
      check: opts.check !== false,
      beforeStress: R.stress,
      phaseBefore: R.phase
    };
    if (current) current.pendingStress = pending;
    const result = originalStressPackage.apply(this, arguments);
    if (current) {
      current.lastStress = Object.assign({}, pending, {
        afterStress: R.stress,
        scaledGain: result.gain,
        actualRecovery: result.actualRecovery,
        focusSpent: result.focusSpent,
        net: result.net,
        burnedOut: result.burnedOut
      });
      current.pendingStress = null;
    }
    return result;
  };

  const originalCheckBurnout = owCheckBurnout;
  owCheckBurnout = function(source) {
    if (current) {
      current.pendingBurnout = Object.assign(
        {},
        current.pendingStress || current.lastStress || {},
        current.pendingCard || {},
        {source: source || 'Unknown stress', stage: 'stress-check'}
      );
    }
    const result = originalCheckBurnout.apply(this, arguments);
    if (result && current) recordBurnout(current.pendingBurnout);
    if (current) current.pendingBurnout = null;
    return result;
  };

  const originalCompletePlay = resolveCompletePlay;
  resolveCompletePlay = function(card, context) {
    if (current) {
      current.pendingCard = {
        taskId: card.task.id,
        taskName: card.task.name,
        family: card.task.family,
        rarity: card.rarity,
        playKind: context && context.primary
          ? 'primary'
          : (context && context.replay ? 'replay' : 'additional')
      };
    }
    const result = originalCompletePlay.apply(this, arguments);
    if (result === false && R.gameResult === 'burnout' && current) {
      recordBurnout(Object.assign(
        {},
        current.lastStress || {},
        current.pendingCard || {},
        {
          source: current.pendingCard
            ? current.pendingCard.taskName
            : 'Task play',
          stage: 'task-play'
        }
      ));
    }
    if (current) current.pendingCard = null;
    return result;
  };

  const originalDefeat = defeat;
  defeat = function(type) {
    if (type === 'burnout' && current && !current.burnout) {
      const fallback = current.pendingBurnout ||
        (current.pendingCard
          ? Object.assign({}, current.lastStress || {}, current.pendingCard, {
              source: current.pendingCard.taskName,
              stage: 'task-play'
            })
          : Object.assign({}, current.lastStress || {}, {
              source: (current.lastStress && current.lastStress.source) ||
                'Unattributed burnout',
              stage: 'fallback'
            }));
      recordBurnout(fallback);
    }
    return originalDefeat.apply(this, arguments);
  };

  const originalStartDay = startDay;
  startDay = async function() {
    const result = await originalStartDay.apply(this, arguments);
    if (current && R.phase === 'morning') {
      current.mornings.push(stateSnapshot());
    }
    return result;
  };

  const originalDayResults = dayResults;
  dayResults = function() {
    const before = stateSnapshot();
    before.startProgress = R.today.startProjectProgress;
    before.pendingProgress = R.today.pts || 0;
    before.pendingRawStress = R.today.stressGain || 0;
    before.pendingRecovery = R.today.stressRelief || 0;
    const result = originalDayResults.apply(this, arguments);
    if (current) {
      const after = stateSnapshot();
      const morning = [...current.mornings].reverse().find(item =>
        item.runDay === after.runDay
      );
      current.clockOuts.push({
        floor: after.floor,
        floorDay: after.floorDay,
        runDay: after.runDay,
        taskId: before.taskId,
        manager: after.manager,
        startProgress: before.startProgress,
        progress: after.progress,
        progressGain: after.progress - before.startProgress,
        projectSize: after.projectSize,
        rivalProgress: after.rivalProgress,
        stressMorning: morning ? morning.stress : null,
        stressBeforeClockOut: before.stress,
        stress: after.stress,
        cashMorning: morning ? morning.cash : null,
        cash: after.cash,
        cashEarned: morning
          ? after.cashEarned - morning.cashEarned
          : null,
        cashNetBeforeNight: morning ? after.cash - morning.cash : null,
        daysLeft: after.daysLeft,
        verdict: owClockOutVerdict(),
        gameResult: R.gameResult || null
      });
    }
    return result;
  };

  const originalResolveNight = owSimulationResolveNight;
  owSimulationResolveNight = async function(policy) {
    const before = stateSnapshot();
    const result = await originalResolveNight.apply(this, arguments);
    if (current) {
      const after = stateSnapshot();
      current.nights.push({
        floor: before.floor,
        floorDay: before.floorDay,
        runDay: before.runDay,
        cashBefore: before.cash,
        cashAfter: after.cash,
        cashChange: after.cash - before.cash,
        stressBefore: before.stress,
        stressAfter: after.stress
      });
    }
    return result;
  };

  const originalResolveWeekend = owSimulationResolveWeekend;
  owSimulationResolveWeekend = async function(policy, nextAction, report) {
    const before = stateSnapshot();
    const result = await originalResolveWeekend.apply(this, arguments);
    if (current) {
      const after = stateSnapshot();
      current.weekends.push({
        floor: before.floor,
        runDay: before.runDay,
        cashBefore: before.cash,
        cashAfter: after.cash,
        stressBefore: before.stress,
        stressAfter: after.stress,
        gameResult: R.gameResult || null
      });
    }
    return result;
  };

  for (let index = 0; index < runs; index++) {
    current = {
      seed: startSeed + index,
      mornings: [],
      clockOuts: [],
      nights: [],
      weekends: [],
      burnout: null,
      lastStress: null,
      pendingStress: null,
      pendingBurnout: null,
      pendingCard: null
    };
    const report = await OfficeWarsTest.simulateRun({
      seed: current.seed,
      policy: 'skilled',
      maxDays: 100
    });
    current.result = report.result;
    current.daysWorked = report.daysWorked;
    current.floorReached = report.floorReached;
    current.finalStress = report.finalStress;
    current.finalCash = report.finalCash;
    current.finalProgress = report.projectProgress;
    current.finalProjectSize = report.projectSize;
    current.finalRivalProgress = report.rivalProgress;
    current.familyXP = report.familyXP;
    current.paths = report.paths;
    current.milestones = report.milestones;
    current.capstone = report.capstone;
    current.familySelections = report.familySelections;
    current.raritySelections = report.raritySelections;
    current.offers = report.offers;
    current.home = R.home;
    current.house = R.house.slice();
    current.closingRewards = R.closingRewards.slice();
    current.closingBestChain = R.closingBestChain;
    current.seasonedStacks = R.seasonedStacks;
    current.codebase = R.codebase;
    current.printedCommonCompleted = R.printedCommonCompleted;
    current.commit = R.commit;
    current.history = report.history;
    output.push(current);
  }

  return {
    gameHashSource: location.href,
    policy: 'skilled',
    startSeed,
    runs,
    output
  };
}
"""

CHAIN_NINE_AUDIT = r"""
async ({runs, startSeed}) => {
  let completedChainNine = 0;
  let chainNineVictories = 0;

  const policy = {
    name: 'skilled',
    chooseSalesCycle({cards, cycle, state}) {
      if (cycle.actualChain >= 9) return {close: true};
      const index = cards
        .map((card, cardIndex) => ({
          index: cardIndex,
          score: (state.familyXP[card.task.family] || 0) +
            (cycle.representedFamilies.includes(card.task.family) ? 0 : 2)
        }))
        .sort((a, b) => b.score - a.score || a.index - b.index)[0].index;
      return {close: false, index};
    }
  };

  for (let index = 0; index < runs; index++) {
    const report = await OfficeWarsTest.simulateRun({
      seed: startSeed + index,
      policy,
      maxDays: 100
    });
    if ((R.closingBestChain || 0) >= 9) {
      completedChainNine++;
      if (report.result === 'victory') chainNineVictories++;
    }
  }

  return {
    runs,
    completedChainNine,
    chainNineVictories,
    chainNineWinRate: completedChainNine
      ? chainNineVictories / completedChainNine
      : null
  };
}
"""


def percentile(values, fraction):
    clean = sorted(value for value in values if value is not None)
    if not clean:
        return None
    if len(clean) == 1:
        return clean[0]
    position = (len(clean) - 1) * fraction
    lower = int(position)
    upper = min(len(clean) - 1, lower + 1)
    weight = position - lower
    return clean[lower] * (1 - weight) + clean[upper] * weight


def rounded(value, digits=1):
    return None if value is None else round(value, digits)


def summary(values):
    clean = [value for value in values if value is not None]
    return {
        "median": rounded(percentile(clean, 0.5)),
        "p25": rounded(percentile(clean, 0.25)),
        "p75": rounded(percentile(clean, 0.75)),
        "mean": rounded(statistics.fmean(clean) if clean else None),
    }


def burnout_category(item, task_names):
    source = item.get("source") or "Unattributed"
    phase = item.get("phaseBefore") or item.get("phase") or ""
    if "Sales Cycle" in source or item.get("rarity") == "cycle":
        return "Sales Cycle"
    if (
        item.get("stage") == "task-play"
        or item.get("taskName")
        or source in task_names
        or phase == "morningResolution"
    ):
        return "Task play or card effect"
    if source == "Clock Out obligations":
        return "Clock Out obligations"
    if source == "Clock Out workday stress":
        return "Clock Out passive stress"
    if source == "Weekend event" or phase.startswith("weekend"):
        return "Weekend event"
    if phase == "workday" or source in {
        "Work on Task",
        "Lunch",
        "Water Cooler",
        "Office Chat",
        "Slumped at Desk",
        "Team Meeting",
        "Sabotage",
        "Desk Visit",
        "Delegation",
        "All Hands",
        "Executive Sponsor",
        "Staff Check-In",
        "Perfect Execution",
    }:
        return "Workday action or event"
    return "Other"


def build_signature(paths):
    if not paths:
        return "No path"
    return " + ".join(
        f"{family}:{path}" for family, path in sorted(paths.items())
    )


def result_summary(runs):
    counts = Counter(run["result"] for run in runs)
    return {
        "n": len(runs),
        "winRate": rounded(counts["victory"] / len(runs), 4)
        if runs
        else None,
        "results": dict(counts),
    }


def build_analysis(runs):
    checkpoint_builds = {}
    for floor in (3, 4, 5):
        grouped = defaultdict(list)
        for run in runs:
            morning = next(
                (
                    item
                    for item in run["mornings"]
                    if item["floor"] == floor
                ),
                None,
            )
            if morning:
                grouped[build_signature(morning.get("paths") or {})].append(
                    run
                )
        rows = []
        for signature, group in grouped.items():
            row = {"signature": signature, **result_summary(group)}
            rows.append(row)
        checkpoint_builds[str(floor)] = sorted(
            rows, key=lambda row: (-row["n"], row["signature"])
        )

    first_cohorts = defaultdict(list)
    individual_paths = defaultdict(list)
    for run in runs:
        first_seen = {}
        for morning in run["mornings"]:
            for family, path in (morning.get("paths") or {}).items():
                key = f"{family}:{path}"
                if key not in first_seen:
                    first_seen[key] = {
                        "floor": morning["floor"],
                        "runDay": morning["runDay"],
                    }
        if first_seen:
            first_day = min(item["runDay"] for item in first_seen.values())
            cohort = {
                key.split(":", 1)[0]: key.split(":", 1)[1]
                for key, item in first_seen.items()
                if item["runDay"] == first_day
            }
            first_cohorts[build_signature(cohort)].append(run)
        for key, acquisition in first_seen.items():
            individual_paths[key].append((run, acquisition))

    path_rows = []
    for path, items in individual_paths.items():
        group = [run for run, _ in items]
        row = {"path": path, **result_summary(group)}
        row["acquisitionFloor"] = summary(
            [item["floor"] for _, item in items]
        )
        row["acquisitionRunDay"] = summary(
            [item["runDay"] for _, item in items]
        )
        path_rows.append(row)

    first_rows = [
        {"signature": signature, **result_summary(group)}
        for signature, group in first_cohorts.items()
    ]

    family_mix = {}
    for result in sorted({run["result"] for run in runs}):
        result_runs = [run for run in runs if run["result"] == result]
        counts = Counter()
        for run in result_runs:
            counts.update(run.get("familySelections") or {})
        total = sum(counts.values())
        family_mix[result] = {
            family: rounded(counts[family] / total, 4) if total else None
            for family in (
                "Coding",
                "Management",
                "Design",
                "Sales",
                "Operations",
            )
        }

    card_runs = defaultdict(list)
    card_picks = defaultdict(Counter)
    card_offer_appearances = Counter()
    card_offer_selections = Counter()
    card_offer_by_result = defaultdict(Counter)
    card_appearance_by_result = defaultdict(Counter)
    for run in runs:
        selected_ids = {
            row["taskId"] for row in run["history"] if row.get("taskId")
        }
        for task_id in selected_ids:
            card_runs[task_id].append(run)
        for row in run["history"]:
            if row.get("taskId"):
                card_picks[row["taskId"]][run["result"]] += 1
        for offer in run.get("offers") or []:
            for card in offer.get("cards") or []:
                task_id = card["id"]
                card_offer_appearances[task_id] += 1
                card_appearance_by_result[task_id][run["result"]] += 1
            selected = offer.get("selected")
            if selected and selected.get("source") == "offer":
                task_id = selected["id"]
                card_offer_selections[task_id] += 1
                card_offer_by_result[task_id][run["result"]] += 1

    card_rows = []
    for task_id, group in card_runs.items():
        row = {"taskId": task_id, **result_summary(group)}
        row["totalPicks"] = sum(card_picks[task_id].values())
        row["picksByResult"] = dict(card_picks[task_id])
        appearances = card_offer_appearances[task_id]
        row["offerAppearances"] = appearances
        row["offerPickRate"] = rounded(
            card_offer_selections[task_id] / appearances, 4
        ) if appearances else None
        row["offerPickRateByResult"] = {}
        for result, result_appearances in card_appearance_by_result[
            task_id
        ].items():
            row["offerPickRateByResult"][result] = rounded(
                card_offer_by_result[task_id][result] / result_appearances,
                4,
            )
        card_rows.append(row)

    upgrade_runs = defaultdict(list)
    for run in runs:
        for upgrade in set(run.get("house") or []):
            upgrade_runs[upgrade].append(run)
    upgrade_rows = [
        {"upgrade": upgrade, **result_summary(group)}
        for upgrade, group in upgrade_runs.items()
    ]

    return {
        "checkpointBuilds": checkpoint_builds,
        "firstPathCohorts": sorted(
            first_rows, key=lambda row: (-row["n"], row["signature"])
        ),
        "individualPaths": sorted(
            path_rows, key=lambda row: (-row["n"], row["path"])
        ),
        "familySelectionMix": family_mix,
        "cards": sorted(
            card_rows, key=lambda row: (-row["totalPicks"], row["taskId"])
        ),
        "homeUpgrades": sorted(
            upgrade_rows, key=lambda row: (-row["n"], row["upgrade"])
        ),
    }


def aggregate(data):
    runs = data["output"]
    result_counts = Counter(run["result"] for run in runs)
    result_by_floor = defaultdict(Counter)
    floor_reach = Counter()
    for run in runs:
        result_by_floor[run["result"]][run["floorReached"]] += 1
        for morning in run["mornings"]:
            if morning["floorDay"] == 1:
                floor_reach[morning["floor"]] += 1
    winners = [run for run in runs if run["result"] == "victory"]
    burnouts = [run for run in runs if run["result"] == "burnout"]
    task_names = {
        play.get("taskName")
        for run in burnouts
        for play in [run.get("burnout") or {}]
        if play.get("stage") == "task-play"
    }

    cause_categories = Counter()
    cause_sources = Counter()
    burnout_floors = Counter()
    burnout_floor_rows = defaultdict(list)
    burnout_progress = []
    completed_despite_burnout = 0
    leading_chad = 0
    for run in burnouts:
        event = run.get("burnout") or {}
        category = burnout_category(event, task_names)
        source = event.get("source") or "Unattributed"
        cause_categories[category] += 1
        cause_sources[source] += 1
        floor = int(event.get("floor") or run["floorReached"])
        burnout_floors[floor] += 1
        size = event.get("projectSize") or run["finalProjectSize"]
        progress = event.get("progress")
        if progress is None:
            progress = run["finalProgress"]
        rival = event.get("rivalProgress")
        if rival is None:
            rival = run["finalRivalProgress"]
        player_pct = 100 * progress / size if size else 0
        rival_pct = 100 * rival / size if size else 0
        burnout_progress.append(player_pct)
        if progress >= size:
            completed_despite_burnout += 1
        if progress > rival:
            leading_chad += 1
        burnout_floor_rows[floor].append(
            {
                "floorDay": event.get("floorDay"),
                "beforeStress": event.get("beforeStress"),
                "playerPct": player_pct,
                "rivalPct": rival_pct,
                "daysLeft": event.get("daysLeft"),
            }
        )

    burnout_by_floor = {}
    for floor in range(1, 8):
        rows = burnout_floor_rows[floor]
        burnout_by_floor[str(floor)] = {
            "count": len(rows),
            "shareOfBurnouts": rounded(len(rows) / len(burnouts), 3)
            if burnouts
            else 0,
            "rateAmongFloorReach": rounded(
                len(rows) / floor_reach[floor], 3
            )
            if floor_reach[floor]
            else 0,
            "floorDay": summary([row["floorDay"] for row in rows]),
            "preHitStress": summary([row["beforeStress"] for row in rows]),
            "playerCompletionPct": summary([row["playerPct"] for row in rows]),
            "chadCompletionPct": summary([row["rivalPct"] for row in rows]),
            "daysLeft": summary([row["daysLeft"] for row in rows]),
        }

    curve_rows = defaultdict(list)
    for run in runs:
        for row in run["clockOuts"]:
            curve_rows[(row["floor"], row["floorDay"])].append(row)
    pressure_curve = {}
    for floor in range(1, 8):
        floor_curve = {}
        for (row_floor, floor_day), rows in sorted(curve_rows.items()):
            if row_floor != floor:
                continue
            player_pct = [
                100 * row["progress"] / row["projectSize"]
                for row in rows
                if row["projectSize"]
            ]
            chad_pct = [
                100 * row["rivalProgress"] / row["projectSize"]
                for row in rows
                if row["projectSize"]
            ]
            floor_curve[str(floor_day)] = {
                "n": len(rows),
                "stress": summary([row["stress"] for row in rows]),
                "playerPct": summary(player_pct),
                "chadPct": summary(chad_pct),
                "daysLeft": summary([row["daysLeft"] for row in rows]),
                "progressPerTurn": summary(
                    [row["progressGain"] for row in rows]
                ),
                "cash": summary([row["cash"] for row in rows]),
            }
        pressure_curve[str(floor)] = floor_curve

    winner_floors = {}
    for floor in range(1, 8):
        floor_records = []
        for run in winners:
            rows = [row for row in run["clockOuts"] if row["floor"] == floor]
            pass_rows = [
                row
                for row in rows
                if row["verdict"] in {"promotion", "victory"}
            ]
            mornings = [
                row for row in run["mornings"] if row["floor"] == floor
            ]
            nights = [row for row in run["nights"] if row["floor"] == floor]
            if not rows or not pass_rows or not mornings:
                continue
            passed = pass_rows[-1]
            entry = mornings[0]
            progress_gains = [row["progressGain"] for row in rows]
            gross_cash = sum(
                row["cashEarned"] or 0 for row in rows
            )
            night_cash_change = sum(
                row["cashChange"] or 0 for row in nights
            )
            effective_budget = passed["floorDay"] + passed["daysLeft"]
            floor_records.append(
                {
                    "daysUsed": passed["floorDay"],
                    "daysLeft": passed["daysLeft"],
                    "effectiveBudget": effective_budget,
                    "clearFraction": passed["floorDay"] / effective_budget
                    if effective_budget
                    else None,
                    "progressPerTurnMean": statistics.fmean(progress_gains),
                    "progressPerTurnMedian": statistics.median(progress_gains),
                    "entryCash": entry["cash"],
                    "clearCash": passed["cash"],
                    "grossCashEarned": gross_cash,
                    "nightCashChange": night_cash_change,
                    "entryStress": entry["stress"],
                    "clearStress": passed["stress"],
                    "chadPctAtClear": 100
                    * passed["rivalProgress"]
                    / passed["projectSize"],
                    "overshoot": passed["progress"] - passed["projectSize"],
                }
            )
        winner_floors[str(floor)] = {
            "n": len(floor_records),
            "daysUsed": summary([row["daysUsed"] for row in floor_records]),
            "daysLeft": summary([row["daysLeft"] for row in floor_records]),
            "effectiveBudget": summary(
                [row["effectiveBudget"] for row in floor_records]
            ),
            "clearFraction": summary(
                [100 * row["clearFraction"] for row in floor_records]
            ),
            "progressPerTurn": summary(
                [row["progressPerTurnMean"] for row in floor_records]
            ),
            "entryCash": summary([row["entryCash"] for row in floor_records]),
            "clearCash": summary([row["clearCash"] for row in floor_records]),
            "grossCashEarned": summary(
                [row["grossCashEarned"] for row in floor_records]
            ),
            "nightCashChange": summary(
                [row["nightCashChange"] for row in floor_records]
            ),
            "entryStress": summary(
                [row["entryStress"] for row in floor_records]
            ),
            "clearStress": summary(
                [row["clearStress"] for row in floor_records]
            ),
            "chadPctAtClear": summary(
                [row["chadPctAtClear"] for row in floor_records]
            ),
            "overshoot": summary([row["overshoot"] for row in floor_records]),
        }

    return {
        "runs": len(runs),
        "seedRange": [data["startSeed"], data["startSeed"] + len(runs) - 1],
        "results": dict(result_counts),
        "resultsByFloor": {
            result: {
                str(floor): counts[floor] for floor in range(1, 8)
            }
            for result, counts in result_by_floor.items()
        },
        "floorReach": {
            str(floor): floor_reach[floor] for floor in range(1, 8)
        },
        "winRate": rounded(
            result_counts["victory"] / len(runs) if runs else None, 4
        ),
        "burnout": {
            "count": len(burnouts),
            "categoryCounts": dict(cause_categories.most_common()),
            "sourceCounts": dict(cause_sources.most_common()),
            "floorCounts": {
                str(floor): burnout_floors[floor] for floor in range(1, 8)
            },
            "byFloor": burnout_by_floor,
            "projectCompletionPct": summary(burnout_progress),
            "atLeast75Pct": sum(value >= 75 for value in burnout_progress),
            "atLeast90Pct": sum(value >= 90 for value in burnout_progress),
            "projectAlreadyComplete": completed_despite_burnout,
            "leadingChad": leading_chad,
        },
        "winnerFloors": winner_floors,
        "pressureCurve": pressure_curve,
        "buildAnalysis": build_analysis(runs),
    }


def compact_build_output(result):
    build = result["buildAnalysis"]
    checkpoints = {}
    for floor, rows in build["checkpointBuilds"].items():
        stable = [row for row in rows if row["n"] >= 15]
        checkpoints[floor] = {
            "sampledRuns": sum(row["n"] for row in rows),
            "stableGroups": sorted(
                stable,
                key=lambda row: (-row["winRate"], -row["n"], row["signature"]),
            ),
        }

    stable_cards = [row for row in build["cards"] if row["n"] >= 100]
    stable_upgrades = [
        row for row in build["homeUpgrades"] if row["n"] >= 100
    ]
    return {
        "runs": result["runs"],
        "results": result["results"],
        "winRate": result["winRate"],
        "checkpoints": checkpoints,
        "firstPathCohorts": build["firstPathCohorts"],
        "individualPaths": build["individualPaths"],
        "familySelectionMix": build["familySelectionMix"],
        "topCardsByConditionalWinRate": sorted(
            stable_cards,
            key=lambda row: (-row["winRate"], -row["n"], row["taskId"]),
        )[:12],
        "bottomCardsByConditionalWinRate": sorted(
            stable_cards,
            key=lambda row: (row["winRate"], -row["n"], row["taskId"]),
        )[:12],
        "mostSelectedCards": build["cards"][:15],
        "homeUpgradesByConditionalWinRate": sorted(
            stable_upgrades,
            key=lambda row: (-row["winRate"], -row["n"], row["upgrade"]),
        ),
    }


def compact_closing_output(result):
    runs = result["buildAnalysis"]["_runs"]
    closing_runs = [
        run
        for run in runs
        if (run.get("paths") or {}).get("Sales") == "closing"
    ]

    def closing_group_summary(group):
        row = result_summary(group)
        row["averageFloorReached"] = rounded(
            statistics.fmean(run["floorReached"] for run in group)
            if group
            else None,
            2,
        )
        return row

    exact = {}
    for chain in range(10):
        group = [
            run
            for run in closing_runs
            if int(run.get("closingBestChain") or 0) == chain
        ]
        exact[str(chain)] = closing_group_summary(group)

    thresholds = {}
    for label, minimum in (
        ("Chain 1+", 1),
        ("Chain 4+", 4),
        ("Chain 5+ Presenting", 5),
        ("Chain 6+", 6),
        ("Chain 8+ Enterprise", 8),
        ("Chain 9 Capstone", 9),
    ):
        group = [
            run
            for run in closing_runs
            if int(run.get("closingBestChain") or 0) >= minimum
        ]
        thresholds[label] = closing_group_summary(group)

    reward_runs = defaultdict(list)
    for run in closing_runs:
        for reward in set(run.get("closingRewards") or []):
            reward_runs[reward].append(run)

    return {
        "runs": result["runs"],
        "overallResults": result["results"],
        "closingPath": closing_group_summary(closing_runs),
        "exactBestCompletedChain": exact,
        "cumulativeThresholds": thresholds,
        "persistentRewards": sorted(
            (
                {"reward": reward, **closing_group_summary(group)}
                for reward, group in reward_runs.items()
            ),
            key=lambda row: (-row["n"], row["reward"]),
        ),
        "closingCapstoneOwners": closing_group_summary(
            [
                run
                for run in closing_runs
                if (run.get("capstone") or {}).get("path") == "closing"
            ]
        ),
    }


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        args=[
            "--allow-file-access-from-files",
            "--disable-extensions",
            "--no-first-run",
        ],
    )
    page_errors = []
    console_errors = []
    try:
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.on(
            "console",
            lambda message: console_errors.append(message.text)
            if message.type == "error"
            else None,
        )
        page.goto(GAME_URL, wait_until="load", timeout=30_000)
        page.wait_for_function(
            "document.documentElement.dataset.officewarsReady === 'true'",
            timeout=15_000,
        )
        page.set_default_timeout(600_000)
        mode = sys.argv[3] if len(sys.argv) > 3 else ""
        if mode == "chain9":
            chain_nine = page.evaluate(
                CHAIN_NINE_AUDIT,
                {"runs": RUNS, "startSeed": START_SEED},
            )
            print(
                "SKILLED_CHAIN9_JSON="
                + json.dumps(chain_nine, separators=(",", ":"))
            )
            sys.exit(0 if not page_errors and not console_errors else 1)
        telemetry = page.evaluate(
            TELEMETRY_AUDIT,
            {"runs": RUNS, "startSeed": START_SEED},
        )
        result = aggregate(telemetry)
        result["browser"] = {
            "pageErrors": page_errors,
            "consoleErrors": console_errors,
        }
        if mode == "closing":
            result["buildAnalysis"]["_runs"] = telemetry["output"]
            print(
                "SKILLED_CLOSING_JSON="
                + json.dumps(compact_closing_output(result), separators=(",", ":"))
            )
        elif mode == "build":
            print(
                "SKILLED_BUILD_JSON="
                + json.dumps(compact_build_output(result), separators=(",", ":"))
            )
        else:
            print(
                "SKILLED_TELEMETRY_JSON="
                + json.dumps(result, separators=(",", ":"))
            )
        sys.exit(0 if not page_errors and not console_errors else 1)
    finally:
        browser.close()
