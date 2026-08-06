import json
import os
import sys
from pathlib import Path


temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
GAME_PATH = (
    Path(sys.argv[1]).resolve()
    if len(sys.argv) > 1
    else ROOT / "officewarsautobattler.html"
)
GAME_URL = GAME_PATH.as_uri()


ADVANCED_AUDIT = r"""
async () => {
  const groups = {};
  const failures = [];

  const record = async (name, run) => {
    try {
      const result = await run();
      groups[name] = result;
      Object.entries(result.checks || {}).forEach(([check, passed]) => {
        if (!passed) failures.push({group: name, check});
      });
    } catch (error) {
      groups[name] = {
        checks: {completed_without_exception: false},
        evidence: {
          error: error.name + ': ' + error.message,
          stack: String(error.stack || '').slice(0, 1500)
        }
      };
      failures.push({group: name, check: 'completed_without_exception'});
    } finally {
      owAutomatedChoiceResolver = null;
      owResolutionLock = false;
      owChoiceState = null;
      pendingMorning = null;
      OW_currentEntry = null;
      hideOverlay();
    }
  };

  const card = (id, extra) => {
    const task = TASK_BY_ID.get(id);
    if (!task) throw new Error('Missing task fixture: ' + id);
    return Object.assign({
      task,
      rarity: task.rarity,
      source: 'verification',
      modifiers: {}
    }, extra || {});
  };

  const resetToday = (seed, options) => {
    const opts = options || {};
    startRun({seed});
    R.phase = opts.phase || 'morningResolution';
    R.floor = opts.floor || 1;
    R.stats.days = opts.day || 1;
    R.day = opts.floorDay || 1;
    R.daysLeft = opts.daysLeft || 20;
    R.project = {
      name: 'Advanced Verification',
      size: opts.projectSize || 100000,
      progress: opts.projectProgress || 0
    };
    R.rival.progress = opts.rivalProgress || 0;
    R.rival.today = {gain: opts.rivalGain || 0, workSlots: 1};
    R.manager = MANAGERS.find(manager => manager.id === (opts.manager || 'penny')) ||
      MANAGERS[0];
    R.stress = opts.stress || 0;
    R.cash = opts.cash === undefined ? 5000 : opts.cash;
    R.todayCard = null;
    R.today = {
      pts: 0,
      stressGain: 0,
      stressRelief: 0,
      pay: 0,
      log: [],
      lunchGood: null,
      startProjectProgress: R.project.progress,
      taskPlays: [],
      cardFlags: {},
      actionHistory: [],
      positiveActionTypes: [],
      backupQueue: [],
      standardBonusUsed: {
        karen: false,
        dave: false,
        bob: false,
        janet: false,
        raj: false,
        priya: false
      },
      activatedCoworkers: [],
      deadlineShift: 0,
      meetingsToday: 0,
      meetingTopicsUsed: [],
      meetingBonusAwarded: false,
      currentMeetingSummary: null,
      dailyInteractionDone: false,
      rivalLines: 0,
      dayProgress: [],
      activeProgressIndex: -1,
      previewActive: false,
      naturalSlots: (opts.naturalSlots || [
        'work', 'meeting', 'lunch', 'cooler', 'slump'
      ]).slice()
    };
    R.focusSpentToday = 0;
    R.delegateWorkIndex = 0;
    R.sabotageToday = false;
    R.sabotageStruck = false;
    hideOverlay();
    return R.today;
  };

  const firstLegal = request => request.options
    .map((option, index) => ({option, index}))
    .filter(item => !item.option.disabled)
    .slice(0, request.min)
    .map(item => item.index);

  const chooseLabel = (request, wanted, fallback) => {
    const terms = Array.isArray(wanted) ? wanted : [wanted];
    const found = request.options.findIndex(option =>
      !option.disabled &&
      terms.some(term => option.label.toLowerCase().includes(term.toLowerCase()))
    );
    if (found >= 0) return [found];
    if (fallback !== undefined) return [fallback];
    return firstLegal(request);
  };

  const nearly = (actual, expected, tolerance) =>
    Math.abs(actual - expected) <= (tolerance === undefined ? 0.0001 : tolerance);

  await record('schedule_conflicts_and_ordering', async () => {
    const configure = seed => {
      const hostile = 'hostile:' + HOSTILE_ACTIONS[0].id;
      resetToday(seed, {
        naturalSlots: ['slump', 'cooler', 'lunch', 'mad', hostile],
        projectSize: 100000
      });
      R.paths.Management = 'leadership';
      R.milestones.Management = 10;
      R.paths.Operations = 'efficiency';
      R.milestones.Operations = 10;
      R.standardProcedures = ['work', 'meeting', 'work'];
      R.capstone = {family: 'Operations', path: 'efficiency', status: 'active'};
      R.closingRewards = ['executiveAirCover'];
      R.today.cardFlags = {
        scheduleAdjustments: [0],
        meetingPrep: 1,
        executiveReviews: ['meeting', 'work'],
        crossFunctionalSyncs: [['karen', 'dave', 'bob']],
        warRooms: ['work', 'meeting'],
        campaignOperationsGuarantee: 1,
        capacityPlanning: 1,
        campaignManagementScheduleMultipliers: [2],
        perfectExecution: 1,
        perfectExecutionWorkBonus: 2
      };
      addEffect('productivityLicense', {
        nextWorkday: true,
        workBonus: 6,
        expiresDay: R.stats.days
      });
      addEffect('shiftHandoffAction', {
        nextWorkday: true,
        kind: 'cooler',
        expiresDay: R.stats.days
      });
      addEffect('workingCapitalActions', {
        nextWorkday: true,
        count: 2,
        expiresDay: R.stats.days
      });
      addEffect('launchSupport', {workdays: 2});
      addEffect('contractorSupport', {
        nextWorkday: true,
        count: 4,
        expiresDay: R.stats.days
      });
      addEffect('facilitatedWorkshop', {
        nextWorkday: true,
        count: 2,
        expiresDay: R.stats.days
      });
      addEffect('clientCall', {
        nextWorkday: true,
        progress: 20,
        expiresDay: R.stats.days
      });
    };

    owAutomatedChoiceResolver = request => {
      if (request.title.startsWith('Leadership:')) {
        return chooseLabel(request, 'Replace');
      }
      return firstLegal(request);
    };

    configure(71001);
    const entries = owPrepareSchedule(R.today.naturalSlots);
    await owApplyLeadership(entries);
    const beforeCapacity = R.project.progress;
    owApplyCapacityPlanning(entries);
    const capacityGain = R.project.progress - beforeCapacity;
    const scheduledResolutions = entries.reduce(
      (sum, entry) => sum + 1 + entry.repeats,
      0
    );
    const sources = entries.map(entry => entry.source);
    const firstCore = entries.findIndex(entry =>
      ['natural', 'replacement'].includes(entry.origin)
    );
    const lastOpening = Math.max(...entries
      .map((entry, index) => entry.origin === 'opening' ? index : -1));
    const firstOrdinaryBonus = entries.findIndex(entry =>
      entry.origin === 'bonus' && entry.source !== 'Team Briefing'
    );
    const lastCore = Math.max(...entries
      .map((entry, index) =>
        ['natural', 'replacement'].includes(entry.origin) ? index : -1
      ));
    const procedureStart = entries.findIndex(entry =>
      entry.origin === 'standardProcedure'
    );
    const procedures = entries.filter(entry =>
      entry.origin === 'standardProcedure'
    );
    const shape = {
      entryCount: entries.length,
      scheduledResolutions,
      sources,
      kinds: entries.map(entry => entry.kind),
      repeats: entries.map(entry => ({
        kind: entry.kind,
        origin: entry.origin,
        source: entry.source,
        repeats: entry.repeats
      })),
      capacityGain
    };

    const orderingShape =
      lastOpening >= 0 &&
      firstCore > lastOpening &&
      firstOrdinaryBonus > lastCore &&
      procedureStart > firstOrdinaryBonus &&
      entries.slice(procedureStart).every(entry =>
        entry.origin === 'standardProcedure'
      );
    const guaranteesHold =
      entries.some(entry => entry.kind === 'work') &&
      entries.some(entry => entry.kind === 'meeting') &&
      entries.filter(entry => entry.kind === 'lunch').length === 1;
    const briefingTarget = entries.find(entry =>
      entry.id === entries.find(item => item.kind === 'briefing').briefingTargetId
    );
    const repeatSemantics =
      entries.filter(entry => entry.source === 'War Room')
        .every(entry => entry.repeats === 1) &&
      !!briefingTarget &&
      briefingTarget.origin === 'natural' &&
      briefingTarget.repeats === 6 &&
      entries.filter(entry => entry.kind.startsWith('hostile:'))
        .every(entry => entry.repeats === 0) &&
      procedures.length === 3 &&
      procedures.every(entry => entry.repeats === 1);
    const capacityUsesEntries = nearly(
      capacityGain,
      4 + entries.length * 2
    );

    configure(71002);
    await owRunWorkDayHeadless({label: 'maximal-schedule'});
    const history = R.today.actionHistory.slice();
    const scheduledHistory = history.filter(item => item.origin !== 'triggered');
    const positiveNonWork = scheduledHistory.filter(item =>
      item.positive && item.kind !== 'work'
    ).length;
    const triggered = history.filter(item =>
      item.origin === 'triggered' && item.kind === 'work'
    ).length;
    const runtimeResolutions = R.today.scheduleEntries.reduce(
      (sum, entry) => sum + 1 + entry.repeats,
      0
    );
    const runtimeOrdering =
      R.phase === 'clockOut' &&
      scheduledHistory.length === runtimeResolutions &&
      scheduledHistory.slice(0, 4).every(item => item.origin === 'opening') &&
      scheduledHistory.slice(-6).every(item =>
        item.source === 'Standard Procedure'
      ) &&
      !scheduledHistory.some(item => item.kind.startsWith('hostile:'));
    const triggeredFinite =
      triggered === positiveNonWork &&
      history.length === scheduledHistory.length + triggered &&
      history.length < 200;

    return {
      checks: {
        maximal_schedule_order: orderingShape,
        guarantees_survive_conflicts: guaranteesHold,
        repeat_and_procedure_semantics: repeatSemantics,
        schedule_counts_use_entries: capacityUsesEntries,
        runtime_order_and_air_cover: runtimeOrdering,
        triggered_actions_are_finite: triggeredFinite
      },
      evidence: {
        shape,
        runtime: {
          phase: R.phase,
          scheduleEntries: R.today.scheduleEntries.length,
          runtimeResolutions,
          actionHistory: history.length,
          triggeredWorks: triggered,
          positiveNonWork,
          firstSources: scheduledHistory.slice(0, 8),
          lastSources: scheduledHistory.slice(-8)
        }
      }
    };
  });

  await record('clock_out_economy_and_debt', async () => {
    resetToday(72001, {
      floor: 3,
      manager: 'bean',
      stress: 60,
      cash: 250,
      projectProgress: 60,
      projectSize: 1000,
      rivalGain: 20
    });
    R.paths.Sales = 'negotiation';
    R.milestones.Sales = 10;
    R.paths.Operations = 'compoundInterest';
    R.milestones.Operations = 10;
    R.house = ['houseplant', 'savings'];
    R.closingRewards = ['burnoutInsurance', 'jointVenture'];
    R.focus = 5;
    R.today.pts = 20;
    R.today.stressGain = 4;
    R.today.stressRelief = 2;
    R.today.pay = 125;
    R.today.positiveActionTypes = ['work', 'meeting', 'cooler', 'mad'];
    R.today.activatedCoworkers = ['karen', 'dave', 'bob'];
    R.today.lastNaturalPositive = 'cooler';
    R.today.cardFlags = {
      campaignDesignClockOutRecovery: 10,
      campaignSalesCash: 300,
      referralFee: 1,
      salesQuota: 1,
      processAudit: 1,
      shiftHandoff: 1,
      workingCapitalCaps: [{cap: 500, sequence: 1}],
      overnightReserves: [{profit: 100, sequence: 2}]
    };
    R.effects = [];
    addEffect('creativeBreakthrough', {workdays: 2, rate: 1});
    addEffect('creativeBreakthrough', {workdays: 2, rate: 1});
    addEffect('whiteSpace', {clockOut: true, threshold: 80, progress: 3});
    addEffect('successFee', {
      nextWorkday: true,
      projectFloor: R.floor,
      payout: 1500
    });
    addEffect('commissionAdvance', {
      dueDay: R.stats.days,
      projectFloor: R.floor
    });
    R.workingCapital = [
      {amount: 500, matureDay: R.stats.days},
      {amount: 700, matureDay: R.stats.days + 1}
    ];
    R.today.accountedCash = 5000;
    R.today.interestPrincipal = 4500;
    const expectedInterest = owInterestAtClockOut();
    const expectedPerformance = 300 + 75 + 100;
    const expectedPay = dailyPay() + 125 + expectedPerformance;
    const expectedBeforeDebt =
      250 + 500 + expectedPay + expectedInterest;
    const debtTotal = expectedBeforeDebt - 600;
    R.debts = [
      {source: 'Net 30 A', amount: Math.floor(debtTotal / 2), dueDay: R.stats.days},
      {
        source: 'Net 30 B',
        amount: debtTotal - Math.floor(debtTotal / 2),
        dueDay: R.stats.days
      },
      {source: 'Future Debt', amount: 999, dueDay: R.stats.days + 1}
    ];

    dayResults();
    const progressExpected = 173;
    const economyEvidence = {
      expectedInterest,
      expectedPay,
      expectedBeforeDebt,
      debtTotal,
      cash: R.cash,
      stress: R.stress,
      focus: R.focus,
      projectProgress: R.project.progress,
      workingCapital: R.workingCapital,
      overnightReserves: R.overnightReserves,
      debts: R.debts,
      effects: R.effects.map(effect => ({
        type: effect.type,
        workdays: effect.workdays,
        nextWorkday: effect.nextWorkday
      }))
    };
    const orderedEconomy =
      expectedInterest === 2025 &&
      nearly(R.project.progress, progressExpected) &&
      R.cash === 100 &&
      R.workingCapital.some(item =>
        item.amount === 700 && item.matureDay === R.stats.days + 1
      ) &&
      R.workingCapital.some(item =>
        item.amount === 500 && item.matureDay === R.stats.days + 1
      ) &&
      R.overnightReserves.length === 0 &&
      R.debts.length === 1 &&
      R.debts[0].source === 'Future Debt';
    const timingAndExpiry =
      effectsOf('whiteSpace').length === 0 &&
      effectsOf('successFee').length === 0 &&
      effectsOf('commissionAdvance').length === 0 &&
      effectsOf('creativeBreakthrough').length === 2 &&
      effectsOf('creativeBreakthrough').every(effect => effect.workdays === 1) &&
      effectsOf('shiftHandoffAction').length === 1 &&
      R.daysLeft === 19;
    const focusAndFlatStress = nearly(R.stress, 42.6) && nearly(R.focus, 0);

    resetToday(72002, {
      floor: 1,
      stress: 80,
      cash: 0,
      projectSize: 1000
    });
    R.guardianAngel = 1;
    R.today.interestPrincipal = 0;
    R.rival.today = {gain: 0};
    const cashBeforeObligations = dailyPay();
    R.debts = [
      {source: 'Debt A', amount: cashBeforeObligations + 125, dueDay: R.stats.days},
      {source: 'Debt B', amount: 125, dueDay: R.stats.days}
    ];
    addEffect('commissionAdvance', {
      dueDay: R.stats.days,
      projectFloor: R.floor
    });
    dayResults();
    const guardianEvidence = {
      cashBeforeObligations,
      cash: R.cash,
      stress: R.stress,
      guardianAngel: R.guardianAngel,
      debts: R.debts.length,
      phase: R.phase
    };
    const aggregateGuardian =
      R.phase === 'clockOut' &&
      R.stress === 75 &&
      R.guardianAngel === 0 &&
      R.debts.length === 0 &&
      effectsOf('commissionAdvance').length === 0;

    return {
      checks: {
        maximal_clock_out_order: orderedEconomy,
        effect_expiry_and_carryover: timingAndExpiry,
        flat_stress_uses_focus: focusAndFlatStress,
        aggregate_debt_guardian_priority: aggregateGuardian
      },
      evidence: {
        maximal: economyEvidence,
        guardian: guardianEvidence
      }
    };
  });

  await record('coworker_standard_and_forced_ordering', async () => {
    resetToday(73001);
    R.rel.karen = 40;
    R.today.cardFlags.oneOnOne = 1;
    const standardFirst = owActivateCoworker('karen', {forced: false});
    const forcedAfter = owActivateCoworker('karen', {forced: true});
    const blockedAfter = owActivateCoworker('karen', {forced: false});
    const orderA = {
      standardUsed: R.today.standardBonusUsed.karen,
      activated: R.today.activatedCoworkers.slice(),
      pts: R.today.pts,
      stressRelief: R.today.stressRelief,
      standardFirst,
      forcedAfter,
      blockedAfter
    };
    const standardThenForced =
      R.today.standardBonusUsed.karen &&
      R.today.activatedCoworkers.filter(pid => pid === 'karen').length === 1 &&
      R.today.cardFlags.oneOnOneSpent === true &&
      blockedAfter.good === false &&
      blockedAfter.text.includes('already used') &&
      R.today.stressRelief === 8 &&
      R.today.pts === 2;

    resetToday(73002);
    R.rel.dave = 40;
    const forcedFirst = owActivateCoworker('dave', {forced: true});
    const standardAfter = owActivateCoworker('dave', {forced: false});
    const orderB = {
      standardUsed: R.today.standardBonusUsed.dave,
      pts: R.today.pts,
      forcedFirst,
      standardAfter
    };
    const forcedThenStandard =
      R.today.standardBonusUsed.dave &&
      R.today.pts === 8 &&
      forcedFirst.good &&
      standardAfter.good;

    resetToday(73003);
    R.rel.karen = 40;
    R.rel.dave = 40;
    R.rel.priya = 40;
    addEffect('referralNetwork', {
      nextWorkday: true,
      expiresDay: R.stats.days,
      coworkers: ['karen', 'dave', 'priya']
    });
    addEffect('referralNetwork', {
      nextWorkday: true,
      expiresDay: R.stats.days,
      coworkers: ['bob', 'janet', 'raj']
    });
    const networkResult = owActivateCoworker('karen', {forced: false});
    const afterNetworkDave = owActivateCoworker('dave', {forced: false});
    const networkEvidence = {
      result: networkResult,
      blockedDave: afterNetworkDave,
      standardBonusUsed: Object.assign({}, R.today.standardBonusUsed),
      remainingNetworks: effectsOf('referralNetwork').map(effect =>
        effect.coworkers.join(',')
      ),
      activated: R.today.activatedCoworkers.slice(),
      pay: R.today.pay,
      pts: R.today.pts,
      stressGain: R.today.stressGain,
      stressRelief: R.today.stressRelief
    };
    const referralReplacement =
      effectsOf('referralNetwork').length === 1 &&
      effectsOf('referralNetwork')[0].coworkers[0] === 'bob' &&
      ['karen', 'dave', 'priya'].every(pid => R.today.standardBonusUsed[pid]) &&
      afterNetworkDave.good === false &&
      R.today.activatedCoworkers.includes('karen') &&
      R.today.activatedCoworkers.includes('dave') &&
      R.today.activatedCoworkers.includes('priya');

    resetToday(73004);
    R.paths.Management = 'delegation';
    R.milestones.Management = 10;
    R.capstone = {family: 'Management', path: 'delegation', status: 'active'};
    R.delegates = ['karen', 'dave'];
    R.rel.karen = 40;
    R.rel.dave = 40;
    R.today.cardFlags.staffCheckIns = ['priya', 'raj'];
    addEffect('executiveSponsor', {
      workdays: 2,
      coworker: 'bob',
      chain: 3
    });
    addEffect('executiveSponsor', {
      workdays: 2,
      coworker: 'janet',
      chain: 4
    });
    owRunOpeningEvents();
    const openingNames = R.today.log
      .filter(line =>
        ['All Hands', 'Executive Sponsor', 'Staff Check-In'].includes(line.n)
      )
      .map(line => line.n + ':' + line.t);
    const openingOrder =
      openingNames.length === 5 &&
      openingNames[0].startsWith('All Hands:') &&
      openingNames[1].includes('Bob') &&
      openingNames[2].includes('Janet') &&
      openingNames[3].includes('Priya') &&
      openingNames[4].includes('Raj') &&
      Object.values(R.today.standardBonusUsed).every(value => value === false);

    return {
      checks: {
        standard_then_forced: standardThenForced,
        forced_then_standard: forcedThenStandard,
        referral_network_replaces_one_standard: referralReplacement,
        opening_events_use_locked_order: openingOrder
      },
      evidence: {
        standardThenForced: orderA,
        forcedThenStandard: orderB,
        referralNetwork: networkEvidence,
        openingOrder: openingNames
      }
    };
  });

  await record('repeated_meetings_and_strength', async () => {
    resetToday(74001);
    R.paths.Management = 'delegation';
    R.milestones.Management = 10;
    R.delegates = ['priya'];
    R.rel.priya = 0;
    R.rel.dave = 0;
    R.rel.karen = 0;
    const entry = owScheduleEntry(
      'meeting',
      'natural',
      'Repeated Meeting Fixture',
      {
        repeats: 1,
        participants: ['priya', 'dave', 'karen'],
        forceFavorable: true
      }
    );
    const summaries = [];
    for (let resolution = 0; resolution < 2; resolution++) {
      R.today.currentMeetingSummary = null;
      OW_currentEntry = entry;
      const line = actionDef('meeting').resolve();
      summaries.push({
        line,
        participants: R.today.currentMeetingSummary.participants.map(person => ({
          pid: person.pid,
          bonus: person.bonus
        }))
      });
    }
    const repeatedEvidence = {
      participants: entry.participants.slice(),
      summaries,
      pay: R.today.pay,
      pts: R.today.pts,
      stressGain: R.today.stressGain,
      stressRelief: R.today.stressRelief,
      standardBonusUsed: Object.assign({}, R.today.standardBonusUsed),
      meetingsToday: R.today.meetingsToday
    };
    const repeatedMeetings =
      summaries.every(summary =>
        summary.participants.map(person => person.pid).join(',') ===
          'priya,dave,karen'
      ) &&
      R.today.pay === 300 &&
      R.today.pts === 2 &&
      R.today.stressGain === 8 &&
      R.today.stressRelief === 12 &&
      R.today.standardBonusUsed.priya === false &&
      R.today.standardBonusUsed.dave === true &&
      R.today.standardBonusUsed.karen === true &&
      R.today.meetingsToday === 2;

    resetToday(74002, {floor: 7, stress: 0});
    R.rel.priya = 0;
    const before = owAccumulatorSnapshot();
    const multiplied = owActivateCoworker('priya', {
      forced: true,
      strength: 4
    });
    const raw = {
      pay: R.today.pay,
      stressGain: R.today.stressGain,
      activated: R.today.activatedCoworkers.slice(),
      result: multiplied
    };
    const survived = owSettleAccumulatorDelta(before, 'Strength Fixture');
    const strengthEvidence = {
      raw,
      finalStress: R.stress,
      cashPending: R.today.pay,
      survived
    };
    const strengthIncludesDrawback =
      raw.pay === 300 &&
      raw.stressGain === 8 &&
      raw.activated.filter(pid => pid === 'priya').length === 1 &&
      nearly(R.stress, 17.6) &&
      survived;

    return {
      checks: {
        repeated_meeting_activation_counts: repeatedMeetings,
        strength_multiplies_complete_package: strengthIncludesDrawback
      },
      evidence: {
        repeated: repeatedEvidence,
        strength: strengthEvidence
      }
    };
  });

  await record('promotion_batches_and_capstones', async () => {
    resetToday(75001, {phase: 'promotionReview'});
    R.familyXP = {
      Coding: 10,
      Management: 10,
      Design: 10,
      Sales: 10,
      Operations: 10
    };
    const pathChoices = {
      Coding: 'Clean Code',
      Management: 'Agile',
      Design: 'Moodboard',
      Sales: 'Negotiation',
      Operations: 'Compound Interest'
    };
    owAutomatedChoiceResolver = request => {
      if (request.title.startsWith('Promotion Review:')) {
        const family = request.title.split(':').pop().trim();
        return chooseLabel(request, pathChoices[family]);
      }
      if (request.title === 'Capstone Decision') {
        return chooseLabel(request, 'Flow State');
      }
      return firstLegal(request);
    };
    const stage = owClonePromotionState();
    await owStagePathChoices(stage);
    await owStageMilestones(stage);
    await owStageCapstone(stage);
    const beforeApply = {
      paths: Object.assign({}, R.paths),
      milestones: Object.assign({}, R.milestones),
      capstone: R.capstone
    };
    const staged = {
      paths: Object.assign({}, stage.paths),
      milestones: Object.assign({}, stage.milestones),
      capstone: Object.assign({}, stage.capstone),
      changes: stage.changes.slice()
    };
    const transactionIsStaged =
      Object.keys(beforeApply.paths).length === 0 &&
      Object.keys(beforeApply.milestones).length === 0 &&
      beforeApply.capstone === null &&
      Object.keys(stage.paths).length === 5 &&
      Object.values(stage.milestones).every(level => level === 10) &&
      stage.capstone.path === 'moodboard' &&
      stage.capstone.status === 'active';
    owApplyPromotionStage(stage);
    const appliedSnapshot = {
      paths: Object.assign({}, R.paths),
      milestones: Object.assign({}, R.milestones),
      capstone: Object.assign({}, R.capstone)
    };
    const appliedOnce =
      Object.keys(R.paths).length === 5 &&
      Object.values(R.milestones).every(level => level === 10) &&
      R.capstone.path === 'moodboard' &&
      R.capstone.status === 'active';

    resetToday(75002);
    R.paths.Coding = 'cleanCode';
    R.paths.Design = 'moodboard';
    R.familyXP.Coding = 9;
    R.familyXP.Design = 9;
    R.capstoneBatch = [];
    owGrantFamilyXP('Coding', 1, 'Atomic Fixture');
    owGrantFamilyXP('Design', 1, 'Atomic Fixture');
    owAutomatedChoiceResolver = request =>
      request.title === 'Capstone Decision'
        ? chooseLabel(request, 'Flow State')
        : firstLegal(request);
    await owResolveCapstoneBatch();
    const atomicEvidence = {
      familyXP: Object.assign({}, R.familyXP),
      capstone: Object.assign({}, R.capstone)
    };
    const atomicComparison =
      R.familyXP.Coding === 10 &&
      R.familyXP.Design === 10 &&
      R.capstone.path === 'moodboard' &&
      R.capstone.status === 'reserved';

    resetToday(75003);
    R.brandStrategyUnlocked = true;
    R.brandStrategy = {
      active: true,
      blocked: false,
      finalRewardActive: false,
      campaignsCompleted: 3,
      campaignIndex: 3,
      step: 5,
      dailyRerolls: 1,
      stepRewardsUnlocked: true
    };
    R.paths.Sales = 'negotiation';
    R.milestones.Sales = 6;
    R.familyXP.Sales = 9;
    owAutomatedChoiceResolver = request => {
      if (request.title === 'Capstone Decision') {
        return chooseLabel(request, 'Global Brand');
      }
      if (request.title === 'Campaign Partnership') return [0];
      return firstLegal(request);
    };
    const finalCampaignCard = {
      task: TASK_BY_ID.get('campaignPartnerLaunch'),
      rarity: 'campaign',
      source: 'campaign',
      campaignProtected: true,
      modifiers: {}
    };
    await owCompletePlay(finalCampaignCard, {
      primary: true,
      selection: true,
      setup: {},
      sourceAncestors: [finalCampaignCard.task.id]
    });
    const brandTieEvidence = {
      salesXP: R.familyXP.Sales,
      salesMilestone: R.milestones.Sales,
      capstone: Object.assign({}, R.capstone),
      brand: Object.assign({}, R.brandStrategy)
    };
    const brandTie =
      R.familyXP.Sales === 10 &&
      R.milestones.Sales === 6 &&
      R.capstone.path === 'brandStrategy' &&
      R.capstone.status === 'active' &&
      R.brandStrategy.finalRewardActive;

    return {
      checks: {
        promotion_choices_are_staged: transactionIsStaged,
        promotion_batch_applies_once: appliedOnce,
        atomic_candidates_compare_without_family_order: atomicComparison,
        brand_and_ordinary_capstones_compare_atomically: brandTie
      },
      evidence: {
        beforeApply,
        staged,
        applied: appliedSnapshot,
        atomic: atomicEvidence,
        brandTie: brandTieEvidence
      }
    };
  });

  await record('all_trait_path_timing', async () => {
    const pathChecks = {};
    const evidence = {};

    resetToday(76001);
    R.paths.Coding = 'cleanCode';
    R.milestones.Coding = 3;
    R.codebase = 4;
    const cleanCommon = owCardPreview(card('readmeUpdate'), {primary: true});
    const cleanRare = owCardPreview(card('parallelProcessing'), {primary: true});
    R.capstone = {family: 'Coding', path: 'cleanCode', status: 'active'};
    R.milestones.Coding = 10;
    const cleanCap = owCardPreview(card('readmeUpdate'), {primary: true});
    pathChecks.cleanCode =
      cleanCommon.progress === 14 &&
      cleanCommon.rawStress === 12 &&
      cleanRare.progress === 8 &&
      cleanRare.rawStress === 10 &&
      cleanCap.progress === 26 &&
      cleanCap.rawStress === 9;
    evidence.cleanCode = {cleanCommon, cleanRare, cleanCap};

    resetToday(76002);
    R.paths.Coding = 'automation';
    R.milestones.Coding = 3;
    owStartDayTraits();
    const commonCoding = card('readmeUpdate');
    const uncommonCoding = card('versionControl');
    pathChecks.automation =
      R.dailyTaskRerolls === 1 &&
      owIsAutomationStarter(commonCoding) &&
      !owIsAutomationStarter(uncommonCoding) &&
      R.today.automationNextAdditionalCost === 100;
    evidence.automation = {
      rerolls: R.dailyTaskRerolls,
      commonStarts: owIsAutomationStarter(commonCoding),
      uncommonStarts: owIsAutomationStarter(uncommonCoding),
      cost: R.today.automationNextAdditionalCost
    };

    resetToday(76003);
    R.paths.Coding = 'debugging';
    R.milestones.Coding = 6;
    R.yesterdayPrimaryFamily = 'Coding';
    const debugCard = card('actionPlan');
    await owCompletePlay(debugCard, {
      primary: true,
      selection: true,
      setup: {},
      sourceAncestors: [debugCard.task.id]
    });
    const xpAtSix = R.familyXP.Management;
    R.milestones.Coding = 10;
    R.familyXP = {
      Coding: 10,
      Management: 3,
      Design: 4,
      Sales: 5,
      Operations: 6
    };
    const debugBefore = R.project.progress;
    owStartDayTraits();
    pathChecks.debugging =
      xpAtSix === 3 &&
      nearly(R.project.progress - debugBefore, 14);
    evidence.debugging = {
      xpAtSix,
      startProgress: R.project.progress - debugBefore
    };

    resetToday(76004);
    R.paths.Management = 'delegation';
    R.milestones.Management = 6;
    R.delegates = ['karen', 'dave'];
    R.rel.karen = 10;
    const relationshipGain = owGainRelationship('karen', 5);
    R.today.standardBonusUsed.karen = true;
    R.today.standardBonusUsed.dave = false;
    const visitor = owChooseDailyVisitor(OW_COWORKER_PIDS);
    pathChecks.delegation =
      relationshipGain === 10 &&
      R.rel.karen === 20 &&
      visitor === 'dave';
    evidence.delegation = {relationshipGain, visitor, rel: R.rel.karen};

    resetToday(76005);
    R.paths.Management = 'agile';
    R.milestones.Management = 3;
    const chance3 = owMeetingFavorableChance();
    R.milestones.Management = 6;
    const chance6 = owMeetingFavorableChance();
    const standupEntries = owPrepareSchedule(R.today.naturalSlots);
    R.milestones.Management = 10;
    const chance10 = owMeetingFavorableChance();
    R.capstone = {family: 'Management', path: 'agile', status: 'active'};
    const chanceCap = owMeetingFavorableChance();
    pathChecks.agile =
      nearly(chance3, .575) &&
      nearly(chance6, .65) &&
      nearly(chance10, .725) &&
      nearly(chanceCap, .8) &&
      standupEntries[0].source === 'Daily Stand-Up';
    evidence.agile = {
      chance3,
      chance6,
      chance10,
      chanceCap,
      firstEntry: standupEntries[0]
    };

    resetToday(76006);
    R.paths.Management = 'leadership';
    R.milestones.Management = 10;
    owAutomatedChoiceResolver = request =>
      request.title.startsWith('Leadership:')
        ? chooseLabel(request, 'Replace')
        : firstLegal(request);
    const leadershipEntries = owPrepareSchedule(R.today.naturalSlots);
    await owApplyLeadership(leadershipEntries);
    const briefingEntries = leadershipEntries.filter(entry =>
      entry.kind === 'briefing'
    );
    pathChecks.leadership =
      briefingEntries.length === 2 &&
      briefingEntries.every(entry => !!entry.briefingTargetId) &&
      leadershipEntries.some(entry => entry.repeats >= 2);
    evidence.leadership = leadershipEntries.map(entry => ({
      kind: entry.kind,
      source: entry.source,
      repeats: entry.repeats,
      target: entry.briefingTargetId || null
    }));

    resetToday(76007);
    R.paths.Design = 'eyeForDetail';
    R.polish.iterationPass = 4;
    R.milestones.Design = 3;
    const eye3 = owPolishProfile(card('iterationPass'));
    R.milestones.Design = 6;
    const eye6 = owPolishProfile(card('iterationPass'));
    R.milestones.Design = 10;
    R.capstone = {family: 'Design', path: 'eyeForDetail', status: 'active'};
    R.masterpieceTaskId = 'iterationPass';
    const eyeCap = owPolishProfile(card('iterationPass'));
    pathChecks.eyeForDetail =
      eye3.baseBonus === 4 &&
      eye3.effectMultiplier === 1 &&
      eye6.baseBonus === 6 &&
      nearly(eye6.effectMultiplier, 1.2) &&
      eyeCap.baseBonus === 16 &&
      nearly(eyeCap.effectMultiplier, 1.8);
    evidence.eyeForDetail = {eye3, eye6, eyeCap};

    resetToday(76008, {stress: 20});
    R.paths.Design = 'moodboard';
    R.milestones.Design = 3;
    owGrantRecovery(15, 'Moodboard 3', false);
    const focus3 = R.focus;
    R.stress = 20;
    R.focus = 20;
    R.milestones.Design = 6;
    const moodProgress = R.project.progress;
    owApplyStressPackage(10, 0, {flat: true, source: 'Moodboard 6'});
    const spentProgress = R.project.progress - moodProgress;
    R.milestones.Design = 10;
    const focusCap10 = owFocusCap();
    R.capstone = {family: 'Design', path: 'moodboard', status: 'active'};
    R.phase = 'workday';
    R.focus = 5;
    R.focusRefreshNext = 0;
    owApplyStressPackage(3, 0, {flat: true, source: 'Moodboard cap'});
    const refresh = R.focusRefreshNext;
    pathChecks.moodboard =
      focus3 === 10 &&
      spentProgress === 10 &&
      focusCap10 === Number.POSITIVE_INFINITY &&
      refresh === 3;
    evidence.moodboard = {focus3, spentProgress, focusCap10, refresh};

    resetToday(76009, {cash: 5000});
    R.paths.Sales = 'negotiation';
    R.milestones.Sales = 3;
    const pay3 = dailyPay();
    R.milestones.Sales = 6;
    const pay6 = dailyPay();
    R.today.interestPrincipal = 1000;
    const interest6 = owInterestAtClockOut();
    R.milestones.Sales = 10;
    const pay10 = dailyPay();
    const interest10 = owInterestAtClockOut();
    R.capstone = {family: 'Sales', path: 'negotiation', status: 'active'};
    R.phase = 'night';
    nightPhase();
    pathChecks.negotiation =
      pay6 - pay3 === 100 &&
      pay10 - pay6 === 100 &&
      interest6 === 180 &&
      interest10 === 225 &&
      nightState.dealLimit === 2 &&
      nightState.dealRerollAvailable === true;
    evidence.negotiation = {
      pay3,
      pay6,
      pay10,
      interest6,
      interest10,
      dealLimit: nightState.dealLimit
    };

    resetToday(76010);
    R.paths.Sales = 'schmoozing';
    R.milestones.Sales = 3;
    const slots3 = owContactSlotCount();
    R.milestones.Sales = 6;
    const slots6 = owContactSlotCount();
    R.milestones.Sales = 10;
    const slots10 = owContactSlotCount();
    pathChecks.schmoozing =
      slots3 === 1 && slots6 === 2 && slots10 === 3 &&
      owSchmoozingAssistCap() === Number.POSITIVE_INFINITY;
    evidence.schmoozing = {
      slots3,
      slots6,
      slots10,
      cap: owSchmoozingAssistCap()
    };

    resetToday(76011);
    R.paths.Sales = 'closing';
    R.milestones.Sales = 3;
    R.familyXP.Sales = 3;
    R.morningCards = [
      card('salesQuota'),
      card('actionPlan'),
      card('processAudit')
    ];
    owMarkHotLead();
    const hotLeads = R.morningCards.filter(item => item.hotLead);
    pathChecks.closing =
      hotLeads.length === 1 &&
      owReachedTraitLevel('Sales', 'closing') === 3;
    evidence.closing = {
      hotLead: hotLeads.map(item => item.task.id),
      level: owReachedTraitLevel('Sales', 'closing')
    };

    resetToday(76012);
    R.paths.Operations = 'efficiency';
    R.milestones.Operations = 10;
    R.standardProcedures = ['work', 'meeting', 'work'];
    R.capstone = {family: 'Operations', path: 'efficiency', status: 'active'};
    const efficiencyEntries = owPrepareSchedule(R.today.naturalSlots);
    const procedureEntries = efficiencyEntries.filter(entry =>
      entry.origin === 'standardProcedure'
    );
    pathChecks.efficiency =
      procedureEntries.length === 3 &&
      procedureEntries.every(entry => entry.repeats === 1 && entry.protected);
    evidence.efficiency = procedureEntries;

    resetToday(76013);
    R.paths.Operations = 'logistics';
    R.milestones.Operations = 3;
    R.storedTask = {taskId: 'readmeUpdate', modifiers: {}, turnsHeld: 4};
    const storedCard = Object.assign(card('readmeUpdate'), {
      stored: true,
      source: 'stored'
    });
    const storedPreview = owCardPreview(storedCard, {primary: true});
    R.milestones.Operations = 6;
    const canDeliver6 = R.storedTask.turnsHeld >= 3;
    R.milestones.Operations = 10;
    const extra10 = Math.floor(R.storedTask.turnsHeld / 5);
    pathChecks.logistics =
      storedPreview.progress === 13 &&
      canDeliver6 &&
      extra10 === 0;
    evidence.logistics = {storedPreview, canDeliver6, extra10};

    resetToday(76014, {stress: 20});
    R.paths.Operations = 'compoundInterest';
    R.today.accountedCash = 5000;
    R.milestones.Operations = 3;
    const reserve3Before = R.project.progress;
    owApplyReserveLevels();
    const reserve3 = R.project.progress - reserve3Before;
    R.project.progress = 0;
    R.stress = 20;
    R.milestones.Operations = 6;
    owApplyReserveLevels();
    const reserve6 = {progress: R.project.progress, stress: R.stress};
    R.project.progress = 0;
    R.stress = 20;
    R.milestones.Operations = 10;
    owApplyReserveLevels();
    const reserve10 = {progress: R.project.progress, stress: R.stress};
    pathChecks.compoundInterest =
      reserve3 === 6 &&
      reserve6.progress === 10 &&
      reserve6.stress === 15 &&
      reserve10.progress === 24 &&
      reserve10.stress === 12;
    evidence.compoundInterest = {reserve3, reserve6, reserve10};

    const allPaths = [
      'cleanCode', 'automation', 'debugging',
      'delegation', 'agile', 'leadership',
      'eyeForDetail', 'moodboard',
      'negotiation', 'schmoozing', 'closing',
      'efficiency', 'logistics', 'compoundInterest'
    ];
    return {
      checks: Object.assign({
        every_ordinary_path_executed:
          allPaths.every(path => Object.prototype.hasOwnProperty.call(pathChecks, path))
      }, pathChecks),
      evidence
    };
  });

  await record('advanced_system_lifecycles', async () => {
    const originalResolveSelectedWorkday = owResolveSelectedWorkday;
    owResolveSelectedWorkday = async () => true;
    resetToday(77001, {stress: 0, rivalProgress: 40});
    R.paths.Sales = 'closing';
    R.milestones.Sales = 3;
    const hotLead = card('salesQuota');
    owStartSalesCycle(hotLead);
    const cycleStress = [];
    owAutomatedChoiceResolver = firstLegal;
    for (let chain = 1; chain <= 8; chain++) {
      R.phase = 'morning';
      R.morningCards = owGenerateSalesCycleOffer();
      const beforeStress = R.stress;
      await owSelectCycleCardUnlocked(0, {headless: true});
      cycleStress.push(R.stress - beforeStress);
    }
    const cycleBeforeClose = JSON.parse(JSON.stringify(R.salesCycle));
    const originalRandom = random;
    random = () => 0;
    R.phase = 'morning';
    await owResolveClose({headless: true});
    random = originalRandom;
    const closingEvidence = {
      cycleBeforeClose,
      cycleStress,
      rewards: R.closingRewards.slice(),
      projectProgress: R.project.progress,
      closeState: Object.assign({}, R.today.closeState),
      salesCycle: R.salesCycle
    };
    const closingLifecycle =
      cycleBeforeClose.actualChain === 8 &&
      cycleStress.join(',') === '2,3,4,5,6,7,8,9' &&
      R.salesCycle === null &&
      R.closingRewards.includes('jointVenture') &&
      R.today.closeState.actualChain === 8 &&
      R.todayCard === null;
    owResolveSelectedWorkday = originalResolveSelectedWorkday;

    resetToday(77002);
    R.brandStrategyUnlocked = true;
    R.brandStrategy = {
      active: true,
      blocked: false,
      finalRewardActive: false,
      campaignsCompleted: 0,
      campaignIndex: 0,
      step: 0,
      dailyRerolls: 0,
      stepRewardsUnlocked: false
    };
    owAutomatedChoiceResolver = request => {
      if (request.title === 'Department Coordination') {
        return chooseLabel(request, 'Coding');
      }
      return firstLegal(request);
    };
    const brandMilestones = [];
    for (let campaignIndex = 0; campaignIndex < BRAND_CAMPAIGNS.length; campaignIndex++) {
      const campaign = BRAND_CAMPAIGNS[campaignIndex];
      for (let step = 0; step < campaign.steps.length; step++) {
        if (campaignIndex === 3 && step === campaign.steps.length - 1) {
          R.capstoneBatch = [];
        }
        const required = campaign.steps[step];
        await owAdvanceBrandCampaign({
          task: required,
          rarity: 'campaign',
          modifiers: {}
        });
      }
      if (campaignIndex === 3) await owResolveCapstoneBatch();
      brandMilestones.push({
        completed: R.brandStrategy.campaignsCompleted,
        index: R.brandStrategy.campaignIndex,
        step: R.brandStrategy.step,
        dailyRerolls: R.brandStrategy.dailyRerolls,
        stepRewardsUnlocked: R.brandStrategy.stepRewardsUnlocked,
        finalRewardActive: R.brandStrategy.finalRewardActive,
        progress: R.project.progress,
        cash: R.cash
      });
    }
    const brandLifecycle =
      brandMilestones.length === 4 &&
      brandMilestones[0].dailyRerolls === 1 &&
      brandMilestones[1].cash === 7000 &&
      brandMilestones[2].stepRewardsUnlocked &&
      R.capstone.path === 'brandStrategy' &&
      R.capstone.status === 'active' &&
      R.brandStrategy.finalRewardActive;

    resetToday(77003, {phase: 'night', cash: 5000});
    R.paths.Sales = 'negotiation';
    R.milestones.Sales = 10;
    R.capstone = {family: 'Sales', path: 'negotiation', status: 'active'};
    nightPhase();
    R.dealCards = [
      OW_DEAL_BY_ID.get('productivityLicense'),
      OW_DEAL_BY_ID.get('contractorSupport'),
      OW_DEAL_BY_ID.get('wellnessStipend')
    ];
    await owPurchaseDeal(OW_DEAL_BY_ID.get('productivityLicense'), 1);
    await owPurchaseDeal(OW_DEAL_BY_ID.get('contractorSupport'), 1);
    const deniedThird = await owPurchaseDeal(
      OW_DEAL_BY_ID.get('wellnessStipend'),
      1
    );
    const dealsEvidence = {
      dealUsed: nightState.dealUsed,
      purchased: [...nightState.purchasedDealIds],
      deniedThird,
      effects: R.effects.map(effect => ({
        type: effect.type,
        workBonus: effect.workBonus,
        count: effect.count,
        progress: effect.progress
      }))
    };
    const dealLifecycle =
      nightState.dealUsed === 2 &&
      deniedThird === false &&
      effectsOf('productivityLicense').some(effect =>
        effect.nextWorkday && effect.workBonus === 6
      ) &&
      effectsOf('contractorSupport').some(effect =>
        effect.nextWorkday && effect.count === 4
      ) &&
      effectsOf('clientCall').length === 2;

    resetToday(77004);
    R.paths.Sales = 'schmoozing';
    R.milestones.Sales = 10;
    R.capstone = {family: 'Sales', path: 'schmoozing', status: 'active'};
    R.contactTeam = ['karen', 'dave', 'priya'];
    R.rel.karen = 50;
    R.rel.dave = 50;
    R.rel.priya = 50;
    const assistPrimary = card('readmeUpdate');
    const assistTargets = [card('regressionTests'), card('expenseAllowance')];
    const assistBefore = R.project.progress;
    owResolveSchmoozingAssists({
      setup: {assistTargets, rajAssistBoost: false}
    }, assistPrimary);
    const assistsEvidence = {
      progress: R.project.progress - assistBefore,
      familyXP: Object.assign({}, R.familyXP),
      taskPlays: R.today.taskPlays.length,
      contacts: R.contactTeam.slice()
    };
    const schmoozingLifecycle =
      nearly(R.project.progress - assistBefore, 38) &&
      R.familyXP.Coding === 1 &&
      R.familyXP.Sales === 1 &&
      R.today.taskPlays.length === 0 &&
      R.contactTeam.join(',') === 'karen,dave,priya';

    resetToday(77005);
    R.paths.Operations = 'logistics';
    R.milestones.Operations = 10;
    R.storedTask = {
      taskId: 'expenseAllowance',
      modifiers: {},
      turnsHeld: 10
    };
    const noCapStart = R.project.progress;
    await owDeliverStored({
      primary: false,
      selection: false,
      additional: true,
      setup: {},
      sourceAncestors: ['expenseAllowance']
    });
    const bulkEvidence = {
      progress: R.project.progress - noCapStart,
      credit: R.expenseCredit,
      salesXP: R.familyXP.Sales,
      plays: R.today.taskPlays.length
    };
    const bulkFulfillment =
      nearly(bulkEvidence.progress, 15) &&
      bulkEvidence.credit === 300 &&
      bulkEvidence.salesXP === 1 &&
      bulkEvidence.plays === 1;

    resetToday(77006);
    R.paths.Operations = 'logistics';
    R.milestones.Operations = 10;
    R.capstone = {family: 'Operations', path: 'logistics', status: 'active'};
    R.storedTask = {
      taskId: 'expenseAllowance',
      modifiers: {},
      turnsHeld: 10
    };
    const capStart = R.project.progress;
    await owDeliverStored({
      primary: false,
      selection: false,
      additional: true,
      setup: {},
      sourceAncestors: ['expenseAllowance']
    });
    const distributionEvidence = {
      progress: R.project.progress - capStart,
      credit: R.expenseCredit,
      salesXP: R.familyXP.Sales,
      plays: R.today.taskPlays.length
    };
    const globalDistribution =
      nearly(distributionEvidence.progress, 33) &&
      distributionEvidence.credit === 300 &&
      distributionEvidence.salesXP === 3 &&
      distributionEvidence.plays === 3;

    return {
      checks: {
        closing_full_cycle_and_cashout: closingLifecycle,
        brand_strategy_full_questline: brandLifecycle,
        deal_purchase_and_carryover: dealLifecycle,
        schmoozing_assists_are_not_plays: schmoozingLifecycle,
        logistics_bulk_fulfillment: bulkFulfillment,
        logistics_global_distribution: globalDistribution
      },
      evidence: {
        closing: closingEvidence,
        brand: brandMilestones,
        deals: dealsEvidence,
        schmoozing: assistsEvidence,
        bulk: bulkEvidence,
        globalDistribution: distributionEvidence
      }
    };
  });

  await record('worst_case_resolution_chains', async () => {
    resetToday(78001, {phase: 'morning', projectSize: 100000});
    R.paths.Coding = 'debugging';
    R.milestones.Coding = 10;
    R.capstone = {family: 'Coding', path: 'debugging', status: 'active'};
    R.yesterdayPrimaryFamily = 'Coding';
    R.focus = 200;
    R.morningCards = [
      card('rapidPrototype', {source: 'offer'}),
      card('parallelProcessing', {source: 'offer'}),
      card('hackathon', {source: 'offer'})
    ];
    pendingMorning = {index: 0, source: 'offer'};
    addEffect('pilotApproved', {nextOrdinaryPrimary: true});
    addEffect('pilotApproved', {nextOrdinaryPrimary: true});
    owAutomatedChoiceResolver = request => {
      if (request.title === 'Rapid Prototype') {
        return chooseLabel(request, 'Parallel Processing');
      }
      if (request.title === 'Parallel Processing') {
        return chooseLabel(request, 'Hackathon');
      }
      if (request.title === 'Hackathon') {
        const preferred = ['Management', 'Sales']
          .map(family => request.options.findIndex(option =>
            !option.disabled &&
            option.detail &&
            option.detail.startsWith(family + ' ')
          ))
          .filter(index => index >= 0);
        if (preferred.length >= request.min) {
          return preferred.slice(0, request.min);
        }
      }
      return firstLegal(request);
    };
    const originalResolveSelectedWorkday = owResolveSelectedWorkday;
    owResolveSelectedWorkday = async () => true;
    await owConfirmMorning({headless: true});
    owResolveSelectedWorkday = originalResolveSelectedWorkday;
    const replayEvidence = {
      plays: R.today.taskPlays.map(play => ({
        taskId: play.taskId,
        kind: play.kind,
        stress: play.stress
      })),
      familyXP: Object.assign({}, R.familyXP),
      focus: R.focus,
      stress: R.stress,
      pilotRemaining: effectsOf('pilotApproved').length
    };
    const hostPlays = R.today.taskPlays.filter(play =>
      play.taskId === 'rapidPrototype'
    );
    const hackathonPlays = R.today.taskPlays.filter(play =>
      play.taskId === 'hackathon'
    );
    const replayStorm =
      hostPlays.length === 4 &&
      hackathonPlays.length === 4 &&
      R.today.taskPlays.length === 16 &&
      effectsOf('pilotApproved').length === 0 &&
      R.phase !== 'gameOver';

    resetToday(78002, {projectSize: 100000});
    R.paths.Operations = 'logistics';
    R.milestones.Operations = 10;
    R.capstone = {family: 'Operations', path: 'logistics', status: 'active'};
    R.focus = 500;
    R.morningCards = [
      card('readmeUpdate'),
      card('actionPlan'),
      card('processAudit')
    ];
    R.storedTask = {
      taskId: 'hackathon',
      modifiers: {},
      turnsHeld: 20
    };
    owAutomatedChoiceResolver = request => {
      if (request.title === 'Hackathon') {
        const preferred = ['Management', 'Sales']
          .map(family => request.options.findIndex(option =>
            !option.disabled &&
            option.detail &&
            option.detail.startsWith(family + ' ')
          ))
          .filter(index => index >= 0);
        if (preferred.length >= request.min) {
          return preferred.slice(0, request.min);
        }
      }
      return firstLegal(request);
    };
    await owDeliverStored();
    const storedEvidence = {
      plays: R.today.taskPlays.length,
      hackathons: R.today.taskPlays.filter(play =>
        play.taskId === 'hackathon'
      ).length,
      xp: Object.values(R.familyXP).reduce((sum, value) => sum + value, 0),
      stress: R.stress,
      focus: R.focus
    };
    const storedStorm =
      storedEvidence.hackathons === 5 &&
      storedEvidence.plays === 15 &&
      storedEvidence.xp === 15 &&
      R.phase !== 'gameOver';

    resetToday(78003, {
      projectSize: 100000,
      naturalSlots: ['meeting', 'cooler', 'lunch', 'mad', 'meeting']
    });
    R.paths.Management = 'agile';
    R.milestones.Management = 10;
    R.capstone = {family: 'Management', path: 'agile', status: 'active'};
    R.paths.Operations = 'efficiency';
    R.milestones.Operations = 10;
    R.standardProcedures = ['meeting', 'cooler', 'meeting'];
    R.focus = 500;
    R.today.cardFlags = {
      warRooms: ['meeting', 'cooler', 'mad'],
      perfectExecution: 3,
      perfectExecutionWorkBonus: 6
    };
    await owRunWorkDayHeadless({label: 'worst-action-chain'});
    const actionHistory = R.today.actionHistory;
    const scheduled = actionHistory.filter(item => item.origin !== 'triggered');
    const triggered = actionHistory.filter(item => item.origin === 'triggered');
    const positiveNonWork = scheduled.filter(item =>
      item.positive && item.kind !== 'work'
    ).length;
    const positiveMeetings = scheduled.filter(item =>
      item.positive && item.kind === 'meeting'
    ).length;
    const expectedTriggered = positiveNonWork * 3 + positiveMeetings;
    const actionEvidence = {
      phase: R.phase,
      scheduleEntries: R.today.scheduleEntries.length,
      scheduledResolutions: scheduled.length,
      positiveNonWork,
      positiveMeetings,
      expectedTriggered,
      triggered: triggered.length,
      total: actionHistory.length,
      progress: R.project.progress,
      stress: R.stress
    };
    const actionStorm =
      R.phase === 'clockOut' &&
      triggered.length === expectedTriggered &&
      actionHistory.length === scheduled.length + triggered.length &&
      actionHistory.length < 400;

    resetToday(78004);
    R.morningCards = [
      card('rapidPrototype'),
      card('designSystem'),
      card('actionPlan')
    ];
    const source = card('rapidPrototype');
    const host = card('designSystem');
    const copyChoices = [];
    owAutomatedChoiceResolver = request => {
      if (request.title === 'Rapid Prototype') {
        copyChoices.push(request.options.map(option => option.label));
        return chooseLabel(request, 'Action Plan');
      }
      return firstLegal(request);
    };
    const nested = await owPrepareCopiedEffectContext(
      source,
      host,
      ['designSystem', 'rapidPrototype']
    );
    const beforeFlags = Object.keys(R.today.cardFlags).length;
    const nestedPlays = await owResolvePrintedEffect(
      source.task,
      host,
      nested,
      ['designSystem', 'rapidPrototype']
    );
    const copyEvidence = {
      choices: copyChoices,
      copySource: nested.setup.copySource &&
        nested.setup.copySource.task.id,
      queuedPlays: nestedPlays.length,
      flags: Object.assign({}, R.today.cardFlags),
      flagDelta: Object.keys(R.today.cardFlags).length - beforeFlags
    };
    const ancestryBounded =
      nested.setup.copySource.task.id === 'actionPlan' &&
      copyChoices.every(labels =>
        !labels.includes('Rapid Prototype') &&
        !labels.includes('Design System')
      ) &&
      nestedPlays.length === 0 &&
      R.today.cardFlags.actionPlan === 1;

    return {
      checks: {
        additive_replays_with_child_plays: replayStorm,
        stored_legendary_chain_terminates: storedStorm,
        maximal_action_chain_terminates: actionStorm,
        copy_ancestry_prevents_recursion: ancestryBounded
      },
      evidence: {
        replayStorm: replayEvidence,
        storedStorm: storedEvidence,
        actionStorm: actionEvidence,
        copyAncestry: copyEvidence
      }
    };
  });

  return {
    gameHashSource: location.href,
    groups,
    failures,
    passed: failures.length === 0
  };
}
"""


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
    requests = []
    try:
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.on(
            "console",
            lambda message: console_errors.append(message.text)
            if message.type == "error"
            else None,
        )
        page.on("request", lambda request: requests.append(request.url))
        page.goto(GAME_URL, wait_until="load", timeout=30_000)
        page.wait_for_function(
            "document.documentElement.dataset.officewarsReady === 'true'",
            timeout=15_000,
        )
        page.set_default_timeout(300_000)
        result = page.evaluate(ADVANCED_AUDIT)
        result["browser"] = {
            "pageErrors": page_errors,
            "consoleErrors": console_errors,
            "externalRequests": [
                request for request in requests if not request.startswith("file:")
            ],
        }
        if page_errors:
            result["failures"].append(
                {"group": "browser", "check": "no_page_errors"}
            )
        if console_errors:
            result["failures"].append(
                {"group": "browser", "check": "no_console_errors"}
            )
        if result["browser"]["externalRequests"]:
            result["failures"].append(
                {"group": "browser", "check": "no_external_requests"}
            )
        result["passed"] = not result["failures"]
        print("ADVANCED_JSON=" + json.dumps(result, separators=(",", ":")))
        sys.exit(0 if result["passed"] else 1)
    finally:
        browser.close()
