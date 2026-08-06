import json
import os
import sys
from pathlib import Path


temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
GAME_URL = (ROOT / "officewarsautobattler.html").as_uri()
RUNS_PER_POLICY = int(sys.argv[1]) if len(sys.argv) > 1 else 250


CORE_AUDIT = r"""
() => {
  const checks = {};
  const detail = {};
  const expect = (name, value, evidence) => {
    checks[name] = !!value;
    detail[name] = evidence;
  };

  expect('core-values',
    CONFIG.STRESS_FLOOR_SCALE === .20 &&
    CONFIG.AUTO_SLEEP === 4 &&
    CONFIG.REC_SLEEP === 5 &&
    CONFIG.PROMOTION_STRESS_RECOVERY === 25 &&
    CONFIG.INTEREST_RATE === .15 &&
    CONFIG.ACTIONS_PER_DAY === 5,
    {
      stressScale: CONFIG.STRESS_FLOOR_SCALE,
      autoSleep: CONFIG.AUTO_SLEEP,
      lightsOut: CONFIG.REC_SLEEP,
      promotionRecovery: CONFIG.PROMOTION_STRESS_RECOVERY,
      interest: CONFIG.INTEREST_RATE,
      actions: CONFIG.ACTIONS_PER_DAY
    }
  );

  const rankPairs = RANKS.map(rank => [rank.size, rank.deadline]);
  expect('rank-curve',
    JSON.stringify(rankPairs) === JSON.stringify([
      [110, 10], [130, 8], [165, 7], [210, 6],
      [250, 6], [285, 6], [300, 5]
    ]),
    rankPairs
  );

  const counts = {};
  TASKS.forEach(card => {
    counts[card.family] ||= {common: 0, uncommon: 0, rare: 0, legendary: 0};
    counts[card.family][card.rarity]++;
  });
  expect('roster-shape',
    TASKS.length === 50 &&
    Object.keys(FAMILIES).every(family =>
      JSON.stringify(counts[family]) ===
      JSON.stringify({common: 4, uncommon: 3, rare: 2, legendary: 1})
    ),
    {total: TASKS.length, counts}
  );

  const ids = TASKS.map(card => card.id);
  expect('roster-identities', new Set(ids).size === 50, {
    total: ids.length,
    unique: new Set(ids).size
  });
  expect('common-micro-effects',
    TASKS.filter(card => card.rarity === 'common')
      .every(card => typeof card.effect === 'string' && card.effect.trim().length > 0),
    TASKS.filter(card => card.rarity === 'common').map(card => card.id)
  );
  expect('special-roster',
    SPECIAL_TASKS.length === 1 &&
    SPECIAL_TASKS[0].id === 'rebrandInitiative' &&
    SPECIAL_TASKS[0].progress === 10 &&
    SPECIAL_TASKS[0].stress === 10,
    SPECIAL_TASKS
  );
  expect('campaign-shape',
    JSON.stringify(BRAND_CAMPAIGNS.map(campaign => campaign.steps.length)) ===
      JSON.stringify([3, 4, 5, 6]) &&
    CAMPAIGN_TASKS.every(card => card.progress === 10 && card.stress === 10),
    BRAND_CAMPAIGNS.map(campaign => ({
      id: campaign.id,
      steps: campaign.steps.map(card => card.id)
    }))
  );
  expect('sales-cycle-shape',
    SALES_CYCLE_TASKS.length === 5 &&
    SALES_CYCLE_TASKS.every(card =>
      card.progress === 10 && card.stress === 0 && card.rarity === 'cycle'
    ),
    SALES_CYCLE_TASKS.map(card => ({
      id: card.id,
      family: card.family,
      progress: card.progress,
      stress: card.stress
    }))
  );

  expect('home-registry',
    UPGRADES.length === 15 &&
    Object.keys(HOME_EFFECTS).length === 15 &&
    UPGRADES.every(upgrade =>
      JSON.stringify(upgrade.effects) ===
      JSON.stringify(HOME_EFFECTS[upgrade.id] || {})
    ),
    {
      upgrades: UPGRADES.length,
      registryEntries: Object.keys(HOME_EFFECTS).length
    }
  );
  expect('home-sets-inert',
    Object.keys(HOME_SETS).length === 0 &&
    UPGRADES.every(upgrade => upgrade.setId === null),
    {
      activeSets: Object.keys(HOME_SETS),
      taggedUpgrades: UPGRADES.filter(upgrade => upgrade.setId).map(upgrade => upgrade.id)
    }
  );

  startRun({seed: 88001});
  R.house = ['mattress'];
  expect('mattress-total', autoSleepAmt() === 6, autoSleepAmt());
  R.floor = 7;
  R.stress = 50;
  owGrantRecovery(5, 'verification', false);
  expect('recovery-unscaled', R.stress === 45, R.stress);
  expect('stress-scaled',
    scaledStress(10) === 22,
    {floor: R.floor, base: 10, scaled: scaledStress(10)}
  );

  const managerRuns = [];
  let managerUnique = true;
  for (let seed = 88100; seed < 88200; seed++) {
    startRun({seed});
    const order = R.managerOrder.map(manager => manager.id);
    managerRuns.push(order);
    if (order.length !== 8 ||
        new Set(order).size !== 8 ||
        new Set(order.slice(0, 7)).size !== 7) {
      managerUnique = false;
    }
  }
  expect('manager-without-replacement', managerUnique, {
    sampledRuns: managerRuns.length,
    first: managerRuns[0]
  });

  const chad = CONFIG.RIVAL_AI;
  expect('chad-baseline',
    chad.STACK_RATE === .5 &&
    chad.UPG_EVERY === 3 &&
    chad.UPG_BONUS === 1.2 &&
    chad.BOSS_MULT === 1.15 &&
    JSON.stringify(chad.WORKSLOT_FLOORS) === JSON.stringify([1, 1, 2, 2, 2, 3, 3]),
    chad
  );

  startRun({seed: 88300});
  for (let day = 0; day < 60; day++) simulateRivalDay();
  updateHUD();
  expect('chad-upgrade-cap',
    R.rival.upgrades === 10 &&
    TIP_TEXTS['sp-rival-tip'].includes('Accumulated upgrades: 10/10'),
    {
      upgrades: R.rival.upgrades,
      stacks: R.rival.stacks,
      tooltip: TIP_TEXTS['sp-rival-tip']
    }
  );

  const liveIds = [...document.querySelectorAll('[id]')].map(node => node.id);
  expect('runtime-ids-unique', liveIds.length === new Set(liveIds).size, {
    count: liveIds.length,
    unique: new Set(liveIds).size
  });
  expect('office-fixtures',
    document.querySelectorAll('[data-cubicle]').length === 8 &&
    document.querySelectorAll('.water-station').length === 1,
    {
      cubicles: document.querySelectorAll('[data-cubicle]').length,
      waterCoolers: document.querySelectorAll('.water-station').length
    }
  );

  expect('trait-family-shape',
    Object.keys(OW_TRAITS).length === 5 &&
    Object.values(OW_TRAITS).reduce((sum, paths) => sum + Object.keys(paths).length, 0) === 14,
    Object.fromEntries(
      Object.entries(OW_TRAITS).map(([family, paths]) => [family, Object.keys(paths)])
    )
  );
  expect('deals-shape',
    OW_DEALS.length === 8 &&
    new Set(OW_DEALS.map(deal => deal.id)).size === 8,
    OW_DEALS.map(deal => ({id: deal.id, price: deal.price, weight: deal.weight}))
  );
  expect('closing-reward-shape',
    Object.values(OW_CLOSE_REWARDS).flat().length === 21 &&
    new Set(Object.values(OW_CLOSE_REWARDS).flat().map(reward => reward.id)).size === 21,
    Object.fromEntries(
      ['nurturing', 'qualifying', 'presenting', 'enterprise'].map(tier => [
        tier,
        OW_CLOSE_REWARDS[tier].map(reward => reward.id)
      ])
    )
  );

  return {checks, detail};
}
"""


CARD_AUDIT = r"""
async () => {
  const previewFailures = [];
  const markupFailures = [];
  const playFailures = [];
  const playEvidence = [];
  const originalAutomated = owAutomatedChoiceResolver;
  const legalChoice = request => {
    const legal = request.options
      .map((option, index) => ({option, index}))
      .filter(item => !item.option.disabled)
      .map(item => item.index);
    return legal.slice(0, request.min);
  };
  owAutomatedChoiceResolver = legalChoice;

  const resetToday = () => {
    R.today = {
      log: [],
      cardFlags: {},
      taskPlays: [],
      backupQueue: [],
      standardBonusUsed: {},
      activatedCoworkers: [],
      positiveActionTypes: [],
      actionHistory: [],
      dayProgress: [],
      activeProgressIndex: -1,
      naturalSlots: ['work', 'meeting', 'lunch', 'cooler', 'slump'],
      pts: 0,
      pay: 0,
      stressGain: 0,
      stressRelief: 0,
      startProjectProgress: 0,
      previewActive: false
    };
  };

  for (let index = 0; index < TASKS.length; index++) {
    const task = TASKS[index];
    startRun({seed: 89000 + index});
    resetToday();
    R.phase = 'morningResolution';
    R.cash = 5000;
    R.stress = 55;
    R.daysLeft = 2;
    R.project.progress = 0;
    R.rival.progress = 50;
    R.completedTaskIds = TASKS
      .filter(candidate => candidate.family !== 'Coding')
      .map(candidate => candidate.id);
    OW_COWORKER_PIDS.forEach(pid => R.rel[pid] = 50);

    const card = {task, rarity: task.rarity, source: 'offer', modifiers: {}};
    const fillers = Object.keys(FAMILIES)
      .map(family => TASKS.find(candidate =>
        candidate.family === family && candidate.id !== task.id
      ))
      .filter(Boolean)
      .map(candidate => ({
        task: candidate,
        rarity: candidate.rarity,
        source: 'offer',
        modifiers: {}
      }));
    R.morningCards = [card, ...fillers];

    try {
      const preview = owCardPreview(card, {primary: true});
      if (![preview.progress, preview.rawStress, preview.recovery, preview.netStress]
          .every(Number.isFinite)) {
        previewFailures.push({id: task.id, preview});
      }
      const markup = owMorningCardMarkup(card, 0, 'offer');
      if (!markup.includes(task.name) ||
          !markup.includes(esc(task.effect)) ||
          !markup.includes('<button')) {
        markupFailures.push(task.id);
      }
      const context = await owPrepareCardContext(card, {});
      const resolved = await owCompletePlay(card, context);
      if (!resolved) {
        playFailures.push({id: task.id, error: 'resolution returned false'});
      } else {
        playEvidence.push({
          id: task.id,
          plays: R.today.taskPlays.length,
          xp: Object.values(R.familyXP).reduce((sum, value) => sum + value, 0),
          effects: R.effects.length,
          flags: Object.keys(R.today.cardFlags)
        });
      }
    } catch (error) {
      playFailures.push({
        id: task.id,
        error: error.name + ': ' + error.message
      });
    } finally {
      owResolutionLock = false;
      owChoiceState = null;
      hideOverlay();
    }
  }
  owAutomatedChoiceResolver = originalAutomated;

  return {
    checks: {
      'all-card-previews': previewFailures.length === 0,
      'all-card-markup': markupFailures.length === 0,
      'all-card-primary-resolution': playFailures.length === 0
    },
    detail: {
      previewFailures,
      markupFailures,
      playFailures,
      resolvedCards: playEvidence.length,
      playEvidence
    }
  };
}
"""


SURFACE_AUDIT = r"""
async () => {
  const checks = {};
  const detail = {};
  const expect = (name, value, evidence) => {
    checks[name] = !!value;
    detail[name] = evidence;
  };

  startRun({seed: 90001});
  owClockIn();
  const morningDeadline = performance.now() + 15000;
  while (R.phase !== 'morning' || !R.morningCards || !R.morningCards.length) {
    if (performance.now() > morningDeadline) {
      throw new Error('Morning surface did not become ready.');
    }
    await new Promise(resolve => setTimeout(resolve, 10));
  }
  await new Promise(resolve => setTimeout(resolve, 40));
  const morningButtons = [...document.querySelectorAll('#overlay-panel .card')];
  expect('morning-surface',
    R.phase === 'morning' &&
    morningButtons.length === R.morningCards.length &&
    morningButtons.every(button => button.tagName === 'BUTTON'),
    {
      phase: R.phase,
      cards: R.morningCards.length,
      buttons: morningButtons.length
    }
  );

  const allButtonsNamed = [...document.querySelectorAll('button')].every(button =>
    !!(button.getAttribute('aria-label') ||
       button.getAttribute('title') ||
       button.textContent.trim())
  );
  expect('buttons-named', allButtonsNamed, {
    buttonCount: document.querySelectorAll('button').length
  });

  hideOverlay();
  const inventoryTrigger = document.querySelector('[aria-label="Open Home inventory"]');
  inventoryTrigger.focus();
  openHomeInventory();
  await new Promise(resolve => setTimeout(resolve, 20));
  const inventory = document.getElementById('home-inventory');
  const inventoryEntry = inventory.contains(document.activeElement);
  const inventoryClose = inventory.querySelector('.hud-modal-close');
  inventoryClose.focus();
  const tab = new KeyboardEvent('keydown', {
    key: 'Tab',
    bubbles: true,
    cancelable: true
  });
  inventoryClose.dispatchEvent(tab);
  const inventoryTrap = tab.defaultPrevented && document.activeElement === inventoryClose;
  closeHomeInventory();
  const inventoryReturn = document.activeElement === inventoryTrigger;
  expect('inventory-focus',
    inventoryEntry && inventoryTrap && inventoryReturn,
    {inventoryEntry, inventoryTrap, inventoryReturn}
  );

  const manager = document.querySelector('.hud-info-button');
  manager.focus();
  const tip = document.getElementById('global-tip');
  expect('keyboard-tooltip',
    tip.style.display === 'block' && tip.textContent.trim().length > 0,
    tip.textContent
  );
  hideGlobalTooltip();

  const controls = ['day-speed-1', 'day-speed-2', 'day-speed-4', 'day-skip-button']
    .map(id => document.getElementById(id));
  expect('playback-controls-semantic',
    controls.every(control =>
      control &&
      control.tagName === 'BUTTON' &&
      control.getAttribute('aria-label')
    ),
    controls.map(control => control && ({
      id: control.id,
      label: control.getAttribute('aria-label')
    }))
  );

  const styleText = document.querySelector('style').textContent;
  expect('responsive-rules',
    styleText.includes('@media (orientation:portrait)') &&
    styleText.includes('.rotate-device') &&
    styleText.includes('@media (prefers-reduced-motion:reduce)'),
    {
      portrait: styleText.includes('@media (orientation:portrait)'),
      rotationGate: styleText.includes('.rotate-device'),
      reducedMotion: styleText.includes('@media (prefers-reduced-motion:reduce)')
    }
  );

  startRun({seed: 90002});
  R.paths.Sales = 'closing';
  R.milestones.Sales = 3;
  const lead = {
    task: TASK_BY_ID.get('salesQuota'),
    rarity: 'common',
    source: 'offer',
    modifiers: {}
  };
  owStartSalesCycle(lead);
  R.morningCards = owGenerateSalesCycleOffer();
  owRenderSalesCycleUI();
  expect('closing-surface',
    document.getElementById('overlay-panel').textContent.includes('CLOSE') &&
    R.morningCards.length === 2,
    {
      cards: R.morningCards.map(card => card.task.id),
      text: document.getElementById('overlay-panel').textContent.slice(0, 300)
    }
  );

  startRun({seed: 90003});
  R.today = {
    log: [],
    cardFlags: {},
    taskPlays: [],
    backupQueue: [],
    standardBonusUsed: {},
    activatedCoworkers: [],
    positiveActionTypes: [],
    actionHistory: [],
    dayProgress: [],
    activeProgressIndex: -1,
    pts: 0,
    pay: 0,
    stressGain: 0,
    stressRelief: 0,
    startProjectProgress: 0,
    previewActive: false
  };
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
  R.phase = 'morning';
  R.today.naturalSlots = ['work', 'meeting', 'lunch', 'cooler', 'slump'];
  R.morningCards = genMorningCards({allowSpecial: false});
  owApplyCampaignReplacement(R.morningCards);
  renderMorningUI();
  const campaignCard = R.morningCards.find(card => card.rarity === 'campaign');
  expect('campaign-surface',
    !!campaignCard &&
    document.getElementById('overlay-panel').textContent.includes('Brand Research'),
    {
      card: campaignCard && campaignCard.task.id,
      text: document.getElementById('overlay-panel').textContent.slice(0, 300)
    }
  );

  openResumeBook();
  await new Promise(resolve => setTimeout(resolve, 20));
  const resume = document.getElementById('resume-book');
  expect('resume-book',
    resume.classList.contains('open') &&
    resume.textContent.includes('Coding') &&
    resume.textContent.includes('Management') &&
    resume.textContent.includes('Design') &&
    resume.textContent.includes('Sales') &&
    resume.textContent.includes('Operations'),
    resume.textContent.slice(0, 500)
  );
  closeHudModal('resume-book');

  startRun({seed: 90004});
  R.effects = [
    {
      id: 'verify-commission',
      type: 'commissionAdvance',
      dueDay: R.stats.days + 1,
      projectFloor: R.floor
    }
  ];
  R.debts = [
    {
      source: 'Net 30 Contract',
      amount: 500,
      dueDay: R.stats.days + 1
    }
  ];
  R.overnightReserves = [
    {
      amount: 250,
      profit: 100,
      returnDay: R.stats.days + 1
    }
  ];
  R.workingCapital = [
    {
      amount: 500,
      matureDay: R.stats.days + 1
    }
  ];
  const commission = owActiveEffectEntries()
    .find(entry => entry.label === 'COMMISSION ADVANCE');
  const economy = owEconomyTooltip();
  expect('delayed-effect-exact-trace',
    !!commission &&
    commission.detail.includes('20') &&
    commission.detail.toLowerCase().includes('clock out') &&
    economy.toLowerCase().includes('due day') &&
    economy.toLowerCase().includes('return') &&
    economy.toLowerCase().includes('mature'),
    {
      commission,
      economy
    }
  );

  const requiredCardDisclosure = {
    repositoryFork: ['Coding XP'],
    crossFunctionalSync: ['already'],
    creativeBreakthrough: ['Excess'],
    designSystem: ['no rerolls'],
    clientEntertainment: ['instead'],
    comparisonShopping: ['same catalog'],
    corporateExpenseAccount: ['expires'],
    net30Contract: ['$25'],
    workingCapital: ["tomorrow's Clock Out", 'each $500']
  };
  const disclosureFailures = Object.entries(requiredCardDisclosure)
    .map(([id, tokens]) => {
      const effect = TASK_BY_ID.get(id).effect;
      return {
        id,
        effect,
        missing: tokens.filter(token =>
          !effect.toLowerCase().includes(token.toLowerCase())
        )
      };
    })
    .filter(item => item.missing.length);
  expect('material-card-disclosure',
    disclosureFailures.length === 0,
    disclosureFailures
  );

  const helpSource = showHowToPlay.toString();
  const glossaryTerms = [
    'Complete Play',
    'Replay',
    'Printed-Effect Resolution',
    'Assist',
    'Schedule Entry',
    'Workday Event'
  ];
  expect('help-resolution-glossary',
    glossaryTerms.every(term => helpSource.includes(term)),
    {
      required: glossaryTerms,
      present: glossaryTerms.filter(term => helpSource.includes(term))
    }
  );

  const actionLegend = document.getElementById('day-action-legend');
  expect('day-action-legend-keyboard',
    !!actionLegend &&
    actionLegend.tabIndex === 0 &&
    actionLegend.getAttribute('aria-labelledby') === 'day-action-legend-title',
    actionLegend && {
      tabIndex: actionLegend.tabIndex,
      labelledBy: actionLegend.getAttribute('aria-labelledby')
    }
  );

  return {checks, detail};
}
"""


SIMULATION_AUDIT = r"""
async ({runsPerPolicy}) => {
  const policies = ['baseline', 'random', 'skilled'];
  const output = {};
  for (let policyIndex = 0; policyIndex < policies.length; policyIndex++) {
    const policy = policies[policyIndex];
    const aggregate = {
      runs: runsPerPolicy,
      results: {},
      floors: {},
      totalDays: 0,
      totalStress: 0,
      stressValues: [],
      totalCash: 0,
      totalPlayerMargin: 0,
      totalRivalMargin: 0,
      cardSelections: {},
      familySelections: {},
      raritySelections: {},
      pathSelections: {},
      capstones: {},
      offerSlots: 0,
      legendaryOffers: 0,
      specialOffers: 0,
      errors: []
    };
    for (let runIndex = 0; runIndex < runsPerPolicy; runIndex++) {
      const seed = 910000 + policyIndex * 100000 + runIndex;
      try {
        const report = await OfficeWarsTest.simulateRun({
          seed,
          policy,
          maxDays: 100
        });
        aggregate.results[report.result] = (aggregate.results[report.result] || 0) + 1;
        aggregate.floors[report.floorReached] =
          (aggregate.floors[report.floorReached] || 0) + 1;
        aggregate.totalDays += report.daysWorked;
        aggregate.totalStress += report.finalStress;
        aggregate.stressValues.push(report.finalStress);
        aggregate.totalCash += report.finalCash;
        aggregate.totalPlayerMargin += report.projectProgress - report.projectSize;
        aggregate.totalRivalMargin += report.projectSize - report.rivalProgress;
        Object.entries(report.familySelections).forEach(([key, value]) => {
          aggregate.familySelections[key] =
            (aggregate.familySelections[key] || 0) + value;
        });
        Object.entries(report.raritySelections).forEach(([key, value]) => {
          aggregate.raritySelections[key] =
            (aggregate.raritySelections[key] || 0) + value;
        });
        report.history.forEach(day => {
          if (day.taskId) {
            aggregate.cardSelections[day.taskId] =
              (aggregate.cardSelections[day.taskId] || 0) + 1;
          }
        });
        Object.values(report.paths).filter(Boolean).forEach(path => {
          aggregate.pathSelections[path] = (aggregate.pathSelections[path] || 0) + 1;
        });
        if (report.capstone) {
          const path = report.capstone.path || 'unknown';
          aggregate.capstones[path] = (aggregate.capstones[path] || 0) + 1;
        }
        report.offers.forEach(offer => {
          offer.cards.forEach(card => {
            aggregate.offerSlots++;
            if (card.rarity === 'legendary') aggregate.legendaryOffers++;
            if (card.rarity === 'special') aggregate.specialOffers++;
          });
        });
      } catch (error) {
        aggregate.errors.push({
          seed,
          error: error.name + ': ' + error.message
        });
      }
    }
    aggregate.stressValues.sort((a, b) => a - b);
    const percentile = p => {
      if (!aggregate.stressValues.length) return null;
      const index = Math.min(
        aggregate.stressValues.length - 1,
        Math.floor((aggregate.stressValues.length - 1) * p)
      );
      return aggregate.stressValues[index];
    };
    const completed = runsPerPolicy - aggregate.errors.length;
    output[policy] = {
      runs: runsPerPolicy,
      completed,
      errors: aggregate.errors,
      results: aggregate.results,
      winRate: completed ? (aggregate.results.victory || 0) / completed : null,
      floors: aggregate.floors,
      averageDays: completed ? aggregate.totalDays / completed : null,
      averageFinalStress: completed ? aggregate.totalStress / completed : null,
      p50FinalStress: percentile(.5),
      p90FinalStress: percentile(.9),
      averageFinalCash: completed ? aggregate.totalCash / completed : null,
      averagePlayerMargin: completed ? aggregate.totalPlayerMargin / completed : null,
      averageRivalMargin: completed ? aggregate.totalRivalMargin / completed : null,
      familySelections: aggregate.familySelections,
      raritySelections: aggregate.raritySelections,
      pathSelections: aggregate.pathSelections,
      capstones: aggregate.capstones,
      offerSlots: aggregate.offerSlots,
      legendaryOffers: aggregate.legendaryOffers,
      legendaryOfferRate: aggregate.offerSlots
        ? aggregate.legendaryOffers / aggregate.offerSlots
        : null,
      specialOffers: aggregate.specialOffers,
      specialOfferRate: aggregate.offerSlots
        ? aggregate.specialOffers / aggregate.offerSlots
        : null,
      topCards: Object.entries(aggregate.cardSelections)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10),
      bottomCards: Object.entries(aggregate.cardSelections)
        .sort((a, b) => a[1] - b[1])
        .slice(0, 10)
    };
  }
  return output;
}
"""

LAYOUT_SETUP = r"""
async ({state}) => {
  startRun({seed: 93001});
  owClockIn();
  const waitFor = async predicate => {
    const deadline = performance.now() + 15000;
    while (!predicate()) {
      if (performance.now() > deadline) {
        throw new Error('Layout state timeout: ' + state);
      }
      await new Promise(resolve => setTimeout(resolve, 10));
    }
  };
  await waitFor(() =>
    R.phase === 'morning' &&
    R.morningCards &&
    R.morningCards.length > 0
  );
  if (state === 'workday') {
    OfficeWarsTest.setTimingScale(3);
    const common = R.morningCards.findIndex(card => card.rarity === 'common');
    selectMorning(common >= 0 ? common : 0, 'offer');
    await confirmMorning();
    await waitFor(() => R.phase === 'workday');
    await new Promise(resolve => setTimeout(resolve, 50));
  } else if (state === 'night') {
    nightPhase();
    await waitFor(() => R.phase === 'night');
    await new Promise(resolve => setTimeout(resolve, 50));
  }
  return R.phase;
}
"""

LAYOUT_INSPECT = r"""
() => {
  const visible = element => {
    if (!element) return false;
    const style = getComputedStyle(element);
    const rect = element.getBoundingClientRect();
    return style.display !== 'none' &&
      style.visibility !== 'hidden' &&
      rect.width > 0 &&
      rect.height > 0;
  };
  const rectOf = element => {
    const rect = element.getBoundingClientRect();
    return {
      left: Math.round(rect.left),
      top: Math.round(rect.top),
      right: Math.round(rect.right),
      bottom: Math.round(rect.bottom),
      width: Math.round(rect.width),
      height: Math.round(rect.height)
    };
  };
  const viewportOverflow = [...document.querySelectorAll(
    '#run-hud,#project-hud,#rival-hud,#player-hud,#side-panel,' +
    '#day-playback-controls,#day-ticker,#day-action-legend,#overlay-panel'
  )].filter(visible).filter(element => {
    const rect = element.getBoundingClientRect();
    return rect.left < -1 || rect.top < -1 ||
      rect.right > innerWidth + 1 || rect.bottom > innerHeight + 1;
  }).map(element => ({id: element.id, rect: rectOf(element)}));

  const clippedText = [...document.querySelectorAll(
    '#day-action-legend *,#overlay-panel .card *,#resume-book *,#home-inventory *'
  )].filter(element => {
    if (!visible(element) || !element.textContent.trim()) return false;
    const style = getComputedStyle(element);
    if (!['hidden', 'clip'].includes(style.overflow) &&
        !['hidden', 'clip'].includes(style.overflowX) &&
        !['hidden', 'clip'].includes(style.overflowY)) return false;
    return element.scrollWidth > element.clientWidth + 1 ||
      element.scrollHeight > element.clientHeight + 1;
  }).map(element => ({
    id: element.id,
    className: String(element.className || ''),
    text: element.textContent.trim().slice(0, 100),
    client: [element.clientWidth, element.clientHeight],
    scroll: [element.scrollWidth, element.scrollHeight]
  }));

  const legend = document.getElementById('day-action-legend');
  let legendReport = null;
  if (visible(legend)) {
    const legendRect = legend.getBoundingClientRect();
    const clippedChildren = [...legend.querySelectorAll('*')]
      .filter(element => {
        if (!visible(element) || !element.textContent.trim()) return false;
        const rect = element.getBoundingClientRect();
        return rect.bottom > legendRect.bottom + 1 ||
          rect.top < legendRect.top - 1;
      })
      .map(element => ({
        tag: element.tagName,
        className: String(element.className || ''),
        text: element.textContent.trim().slice(0, 100),
        rect: rectOf(element)
      }));
    legendReport = {
      rect: rectOf(legend),
      client: [legend.clientWidth, legend.clientHeight],
      scroll: [legend.scrollWidth, legend.scrollHeight],
      overflow: getComputedStyle(legend).overflow,
      tabIndex: legend.tabIndex,
      focusableDescendants: legend.querySelectorAll(
        'button,[href],input,select,textarea,[tabindex]:not([tabindex="-1"])'
      ).length,
      clippedChildren
    };
  }

  const overlay = document.getElementById('overlay-panel');
  const overlayReport = visible(overlay) ? {
    rect: rectOf(overlay),
    client: [overlay.clientWidth, overlay.clientHeight],
    scroll: [overlay.scrollWidth, overlay.scrollHeight],
    overflowY: getComputedStyle(overlay).overflowY
  } : null;

  return {
    viewport: [innerWidth, innerHeight],
    phase: R.phase,
    viewportOverflow,
    clippedText,
    legend: legendReport,
    overlay: overlayReport,
    body: {
      client: [document.documentElement.clientWidth, document.documentElement.clientHeight],
      scroll: [document.documentElement.scrollWidth, document.documentElement.scrollHeight]
    }
  };
}
"""


def merge_audit(target, audit):
    target["checks"].update(audit["checks"])
    target["detail"].update(audit["detail"])


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
        page.set_default_timeout(120_000)

        audit = {"checks": {}, "detail": {}}
        merge_audit(audit, page.evaluate(CORE_AUDIT))
        merge_audit(audit, page.evaluate(CARD_AUDIT))
        merge_audit(audit, page.evaluate(SURFACE_AUDIT))
        audit["checks"]["no-page-errors"] = not page_errors
        audit["detail"]["no-page-errors"] = page_errors
        audit["checks"]["no-console-errors"] = not console_errors
        audit["detail"]["no-console-errors"] = console_errors
        audit["checks"]["no-external-runtime-requests"] = all(
            request.startswith("file:") for request in requests
        )
        audit["detail"]["no-external-runtime-requests"] = requests

        print("AUDIT_JSON=" + json.dumps(audit, separators=(",", ":")))

        layout_cases = [
            ("desktop-morning", 1440, 900, "morning"),
            ("compact-morning", 1024, 768, "morning"),
            ("landscape-morning", 844, 390, "morning"),
            ("portrait-morning", 390, 844, "morning"),
            ("desktop-workday", 1440, 900, "workday"),
            ("compact-workday", 1024, 768, "workday"),
            ("landscape-workday", 844, 390, "workday"),
            ("desktop-night", 1440, 900, "night"),
            ("compact-night", 1024, 768, "night"),
            ("landscape-night", 844, 390, "night"),
        ]
        layout = {}
        for name, width, height, state in layout_cases:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                reduced_motion="reduce",
            )
            layout_page = context.new_page()
            layout_page.goto(GAME_URL, wait_until="load", timeout=30_000)
            layout_page.wait_for_function(
                "document.documentElement.dataset.officewarsReady === 'true'",
                timeout=15_000,
            )
            phase = layout_page.evaluate(LAYOUT_SETUP, {"state": state})
            layout[name] = {"requestedState": state, "phase": phase}
            layout[name].update(layout_page.evaluate(LAYOUT_INSPECT))
            legend = layout_page.locator("#day-action-legend")
            if state == "workday" and legend.is_visible():
                legend.focus()
                scroll_before = legend.evaluate("element => element.scrollTop")
                layout_page.keyboard.press("End")
                scroll_after = legend.evaluate("element => element.scrollTop")
                layout[name]["legendKeyboardScroll"] = {
                    "before": scroll_before,
                    "after": scroll_after,
                    "passed": scroll_after > scroll_before,
                }
            context.close()
        print("LAYOUT_JSON=" + json.dumps(layout, separators=(",", ":")))

        if RUNS_PER_POLICY > 0:
            page.set_default_timeout(900_000)
            simulation = page.evaluate(
                SIMULATION_AUDIT, {"runsPerPolicy": RUNS_PER_POLICY}
            )
            print("SIMULATION_JSON=" + json.dumps(simulation, separators=(",", ":")))
    finally:
        browser.close()
