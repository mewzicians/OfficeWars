import json
import os
import sys
from pathlib import Path


temp_root = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if temp_root:
    sys.path.insert(0, os.path.join(temp_root, "officewars-python"))
from playwright.sync_api import sync_playwright


ROOT = os.path.dirname(os.path.abspath(__file__))
GAME_URL = (Path(ROOT) / "officewarsautobattler.html").as_uri()
QUIET = "--quiet" in sys.argv
META_COMPLETE = json.dumps(
    {
        "schema": 3,
        "tutorial": {
            "completed": True,
            "nextStep": 13,
            "skipped": False,
            "replayRequested": False,
        },
    }
)


def complete_orientation(page):
    page.evaluate(
        "(meta) => localStorage.setItem(OW_META_KEY, meta)", META_COMPLETE
    )
    page.reload(wait_until="load", timeout=30000)
    page.wait_for_function(
        "document.documentElement.dataset.officewarsReady === 'true'",
        timeout=15000,
    )

CASES = [
    ("desktop-morning", 1440, 900, "morning"),
    ("compact-morning", 1024, 700, "morning"),
    ("landscape-morning", 844, 390, "morning"),
    ("desktop-context-pins", 1440, 900, "context-pins"),
    ("landscape-context-pins", 844, 390, "context-pins"),
    ("desktop-context-pins-zoom", 1440, 900, "context-pins-zoom"),
    ("desktop-pinned-detail", 1440, 900, "pinned-detail"),
    ("landscape-pinned-detail", 844, 390, "pinned-detail"),
    ("desktop-resume-tooltips", 1440, 900, "resume-tooltips"),
    ("landscape-resume-tooltips", 844, 390, "resume-tooltips"),
    ("desktop-trait-keywords", 1440, 900, "trait-keywords"),
    ("landscape-trait-keywords", 844, 390, "trait-keywords"),
    ("desktop-promotion-path", 1440, 900, "promotion-path"),
    ("landscape-promotion-path", 844, 390, "promotion-path"),
    ("desktop-promotion-milestone", 1440, 900, "promotion-milestone"),
    ("landscape-promotion-milestone", 844, 390, "promotion-milestone"),
    ("desktop-promotion-capstone", 1440, 900, "promotion-capstone"),
    ("landscape-promotion-capstone", 844, 390, "promotion-capstone"),
    ("desktop-automation-combo", 1440, 900, "automation-combo"),
    ("landscape-automation-combo", 844, 390, "automation-combo"),
    ("desktop-campaign", 1440, 900, "campaign"),
    ("landscape-campaign", 844, 390, "campaign"),
    ("portrait-rotate", 390, 844, "morning"),
    ("desktop-resume", 1440, 900, "resume"),
    ("landscape-resume", 844, 390, "resume"),
    ("desktop-workday", 1440, 900, "workday"),
    ("landscape-workday", 844, 390, "workday"),
    ("desktop-clockout", 1440, 900, "clockout"),
    ("landscape-clockout", 844, 390, "clockout"),
    ("desktop-night", 1440, 900, "night"),
    ("landscape-night", 844, 390, "night"),
    ("desktop-night-sale", 1440, 900, "night-sale"),
    ("landscape-night-sale", 844, 390, "night-sale"),
    ("desktop-night-lights", 1440, 900, "night-lights"),
    ("landscape-night-lights", 844, 390, "night-lights"),
    ("desktop-outing-lights", 1440, 900, "outing-lights"),
    ("landscape-outing-lights", 844, 390, "outing-lights"),
    ("desktop-text-zoom", 1440, 900, "text-zoom"),
]

SETUP = """
async ({state}) => {
  startRun({seed: 73001});
  owClockIn();
  const waitFor = async predicate => {
    const deadline = performance.now() + 15000;
    while (!predicate()) {
      if (performance.now() > deadline) throw new Error('State timeout: ' + state);
      await new Promise(resolve => setTimeout(resolve, 10));
    }
  };
  await waitFor(() =>
    R.phase === 'morning' &&
    R.morningCards &&
    R.morningCards.length > 0 &&
    document.getElementById('mc-name')
  );
  if (
    state === 'context-pins' ||
    state === 'context-pins-zoom' ||
    state === 'pinned-detail'
  ) {
    R.paths.Management = 'delegation';
    R.milestones.Management = 6;
    R.familyXP.Management = 6;
    R.delegates = ['karen', 'dave'];
    R.paths.Sales = 'schmoozing';
    R.milestones.Sales = 6;
    R.familyXP.Sales = 6;
    R.contactTeam = ['bob', 'priya'];
    addEffect('apiFollowup', {
      nextWorkday: true,
      family: 'Design',
      expiresDay: R.stats.days + 1
    });
    owAddCurrentPin('versionControl', 'Case Study', {}, false);
    owAddCurrentPin('corporateExpenseAccount', 'Masterpiece', {}, false);
    renderMorningUI();
    updateHUD();
    if (state === 'context-pins-zoom') {
      document.documentElement.style.fontSize = '36px';
    }
    if (state === 'pinned-detail') {
      owOpenPinnedTaskDetail(0);
      await waitFor(() =>
        document.getElementById('pinned-task-detail').classList.contains('open')
      );
    }
  } else if (state === 'resume-tooltips') {
    R.familyXP.Coding = 6;
    R.paths.Coding = 'automation';
    R.milestones.Coding = 3;
    R.familyXP.Management = 3;
    updateHUD();
    const chosen = document.querySelectorAll(
      '#sp-resume .resume-family'
    )[0].querySelectorAll('.resume-xp-segment.milestone')[1];
    chosen.focus();
    await waitFor(() =>
      document.getElementById('global-tip').style.display === 'block'
    );
  } else if (state === 'trait-keywords') {
    R.familyXP.Design = 10;
    R.paths.Design = 'eyeForDetail';
    R.milestones.Design = 10;
    updateHUD();
    openResumeBook('Design');
    await waitFor(() =>
      document.getElementById('resume-book').classList.contains('open')
    );
    await new Promise(resolve =>
      requestAnimationFrame(() => requestAnimationFrame(resolve))
    );
    const polish = [...document.querySelectorAll(
      '#resume-book-content .rules-keyword'
    )].find(element => element.textContent === 'Polish');
    if (!polish) throw new Error('Missing Polish glossary keyword.');
    polish.focus();
    await waitFor(() =>
      document.getElementById('global-tip').style.display === 'block'
    );
  } else if (state === 'promotion-path') {
    R.phase = 'promotionReview';
    R.familyXP.Coding = 3;
    void owRunPromotionReview();
    await waitFor(() =>
      owChoiceState &&
      owChoiceState.title === 'Promotion Review: Coding'
    );
  } else if (state === 'promotion-milestone') {
    R.phase = 'promotionReview';
    R.paths.Coding = 'automation';
    R.milestones.Coding = 0;
    R.familyXP.Coding = 6;
    void owRunPromotionReview();
    await waitFor(() =>
      owChoiceState &&
      owChoiceState.title === 'Promotion Review' &&
      document.querySelectorAll('.promotion-milestone-card').length === 2
    );
  } else if (state === 'promotion-capstone') {
    R.phase = 'promotionReview';
    R.paths.Coding = 'cleanCode';
    R.paths.Design = 'moodboard';
    R.milestones.Coding = 6;
    R.milestones.Design = 6;
    R.familyXP.Coding = 10;
    R.familyXP.Design = 10;
    R.capstone = {
      family: 'Coding',
      path: 'cleanCode',
      status: 'reserved'
    };
    void owRunPromotionReview();
    await waitFor(() =>
      owChoiceState &&
      owChoiceState.title === 'Capstone Decision'
    );
    const flowState = owChoiceState.options.findIndex(
      option => option.label === 'Flow State'
    );
    owToggleChoice(flowState);
    owConfirmChoice();
    await waitFor(() =>
      owChoiceState &&
      owChoiceState.title === 'Promotion Review'
    );
    const revise = owChoiceState.options.findIndex(
      option => option.label === 'Revise Choices'
    );
    owChooseImmediate(revise);
    await waitFor(() =>
      owChoiceState &&
      owChoiceState.title === 'Capstone Decision'
    );
    window.__owVisualCapstoneRevised = true;
    const zeroDebt = owChoiceState.options.findIndex(
      option => option.label === 'Zero Technical Debt'
    );
    owChooseImmediate(zeroDebt);
    await waitFor(() =>
      owChoiceState &&
      owChoiceState.title === 'Promotion Review' &&
      document.querySelector('.promotion-capstone-card')
    );
  } else if (state === 'automation-combo') {
    R.paths.Coding = 'automation';
    R.milestones.Coding = 6;
    R.cash = 1000;
    R.dailyTaskRerolls = 1;
    R.rerollsMorning = 2;
    R.today.automationCombo = 0;
    R.today.automationAdditionalPlayed = 0;
    R.today.automationNextAdditionalCost = 100;
    void owRunAutomationCombo({
      task: TASK_BY_ID.get('readmeUpdate'),
      rarity: 'common',
      source: 'visual',
      modifiers: {}
    });
    await waitFor(() =>
      owChoiceState &&
      owChoiceState.title === 'Automation Combo 1'
    );
  } else if (state === 'campaign') {
    R.brandStrategyUnlocked = true;
    R.brandStrategy = {
      active: true,
      blocked: false,
      finalRewardActive: false,
      campaignsCompleted: 0,
      campaignIndex: 0,
      step: 2,
      dailyRerolls: 0,
      stepRewardsUnlocked: false
    };
    R.morningCards[0] = {
      task: owCampaignRequiredTask(),
      rarity: 'campaign',
      source: 'campaign',
      modifiers: {},
      specialProtected: true
    };
    renderMorningUI();
  } else if (state === 'resume') {
    R.familyXP.Coding = 6;
    R.paths.Coding = 'automation';
    R.milestones.Coding = 3;
    updateHUD();
    openResumeBook('Coding');
    await waitFor(() => document.getElementById('resume-book').classList.contains('open'));
  } else if (state === 'workday' || state === 'clockout') {
    OfficeWarsTest.setTimingScale(state === 'workday' ? 0.25 : 0.02);
    const common = R.morningCards.findIndex(card => card.rarity === 'common');
    selectMorning(common >= 0 ? common : 0, 'offer');
    void confirmMorning();
    await waitFor(() => R.phase === 'workday');
    if (state === 'clockout') {
      skipWorkDay();
      await waitFor(() => R.phase === 'clockOut');
    } else {
      await waitFor(() =>
        document.getElementById('dt-result').textContent !==
        'Results appear as actions resolve.'
      );
    }
  } else if (
    state === 'night' ||
    state === 'night-sale' ||
    state === 'night-lights' ||
    state === 'outing-lights'
  ) {
    R.stress = 42;
    R.cash = 725;
    R.expenseCredit = 175;
    R.house = ['standingDesk'];
    hideOverlay();
    hideOverlayToggle();
    nightPhase();
    await waitFor(() => R.phase === 'night');
    if (state === 'night-sale') {
      owPromptHomeSale('standingDesk');
      await waitFor(() => document.getElementById('sell-popup'));
    } else if (state === 'night-lights') {
      owToggleLightsOut(true);
    } else if (state === 'outing-lights') {
      owOpenNightPanel('outings');
      pickOutingPid('karen');
      const freeOuting = OUTINGS.findIndex(outing => outing.cost === 0);
      nightState.outingCards = [freeOuting];
      nightState.pendingOuting = 0;
      confirmOuting();
      await waitFor(() =>
        document.getElementById('overlay-panel').textContent.includes('HEAD HOME')
      );
      owReturnFromOuting();
      await waitFor(() =>
        document.getElementById('home-scene').classList.contains('active') &&
        !document.getElementById('overlay').classList.contains('active')
      );
      owToggleLightsOut(true);
      await waitFor(() =>
        nightState.recPicked &&
        nightState.outingUsed &&
        nightState.outingPid === null
      );
    }
  } else if (state === 'text-zoom') {
    document.documentElement.style.fontSize = '36px';
  }
  return R.phase;
}
"""

LAYOUT_REPORT = """
() => {
  const ids = [
    'run-hud', 'project-hud', 'rival-hud', 'player-hud', 'side-panel',
    'day-playback-controls', 'day-ticker', 'day-action-legend', 'overlay-panel',
    'resume-book', 'home-scene'
  ];
  const visible = ids.map(id => {
    const element = document.getElementById(id);
    if (!element) return null;
    const style = getComputedStyle(element);
    const rect = element.getBoundingClientRect();
    if (style.display === 'none' || style.visibility === 'hidden' ||
        rect.width === 0 || rect.height === 0) return null;
    return {
      id,
      left: Math.round(rect.left),
      top: Math.round(rect.top),
      right: Math.round(rect.right),
      bottom: Math.round(rect.bottom),
      width: Math.round(rect.width),
      height: Math.round(rect.height)
    };
  }).filter(Boolean);
  const overflow = visible.filter(rect =>
    rect.left < -1 || rect.top < -1 ||
    rect.right > innerWidth + 1 || rect.bottom > innerHeight + 1
  ).map(rect => rect.id);
  const persistent = new Set([
    'run-hud', 'project-hud', 'rival-hud', 'player-hud', 'side-panel',
    'day-playback-controls', 'day-ticker', 'day-action-legend'
  ]);
  const overlaps = [];
  for (let a = 0; a < visible.length; a++) {
    if (!persistent.has(visible[a].id)) continue;
    for (let b = a + 1; b < visible.length; b++) {
      if (!persistent.has(visible[b].id)) continue;
      const one = visible[a];
      const two = visible[b];
      if (one.left < two.right && one.right > two.left &&
          one.top < two.bottom && one.bottom > two.top) {
        overlaps.push(one.id + ':' + two.id);
      }
    }
  }
  const rotate = document.querySelector('.rotate-device');
  return {
    viewport: [innerWidth, innerHeight],
    phase: R.phase,
    rotateVisible: rotate && getComputedStyle(rotate).display !== 'none',
    overflow,
    overlaps,
    visible
  };
}
"""

READABILITY_REPORT = """
({state}) => {
  const visible = element => {
    if (!element) return false;
    const style = getComputedStyle(element);
    const rect = element.getBoundingClientRect();
    return style.display !== 'none' && style.visibility !== 'hidden' &&
      rect.width > 0 && rect.height > 0;
  };
  const clippedText = [...document.querySelectorAll(
    '#project-hud *,#overlay-panel *,#resume-book *,#day-ticker *,#side-panel *,' +
    '#home-scene button *,#home-scene .home-night-status-item'
  )].filter(element => {
    if (!visible(element) || !element.textContent.trim()) return false;
    if (element.matches(
      '.home-visual, .resume-family, .morning-build-context-detail'
    )) return false;
    const style = getComputedStyle(element);
    if (!['hidden', 'clip'].includes(style.overflow) &&
        !['hidden', 'clip'].includes(style.overflowX) &&
        !['hidden', 'clip'].includes(style.overflowY)) return false;
    return element.scrollWidth > element.clientWidth + 1 ||
      element.scrollHeight > element.clientHeight + 1;
  }).map(element => ({
    id: element.id,
    className: String(element.className || ''),
    text: element.textContent.trim().slice(0, 80)
  }));
  const panel = document.getElementById('overlay-panel');
  const dialog = document.querySelector('#resume-book .hud-modal-dialog');
  const report = {
    state,
    clippedText,
    overlayHorizontalOverflow: visible(panel)
      ? panel.scrollWidth - panel.clientWidth
      : 0,
    modalHorizontalOverflow: visible(dialog)
      ? dialog.scrollWidth - dialog.clientWidth
      : 0,
    projectBar: {
      topFill: !!document.querySelector('#project-hud #sp-prog-fill'),
      topValue: document.querySelector('#project-hud #sp-prog-val')?.textContent.trim(),
      topName: document.querySelector('#project-hud #hud-project-name')?.textContent.trim(),
      scrim: !!document.querySelector('#project-hud .project-hud-scrim'),
      bottomProject: !!document.querySelector('#player-hud #sp-prog-fill'),
      bottomStress: !!document.querySelector('#player-hud #sp-str-fill')
    }
  };
  if (state === 'morning' || state === 'text-zoom' || state === 'campaign') {
    const railArt = [...document.querySelectorAll(
      '#sp-resume .resume-family-art'
    )];
    report.resumeRailArt = {
      count: railArt.length,
      decorative: railArt.every(art =>
        art.getAttribute('aria-hidden') === 'true' &&
        getComputedStyle(art).pointerEvents === 'none'
      ),
      foregrounded: [...document.querySelectorAll(
        '#sp-resume .resume-family-name'
      )].every(name =>
        Number(getComputedStyle(name).zIndex) >
        Number(getComputedStyle(name.closest('.resume-family')
          .querySelector('.resume-family-art')).zIndex)
      )
    };
    report.familyBanners = document.querySelectorAll(
      '.morning-full-cards .task-family-banner'
    ).length;
    report.routineXp = /\\+1\\s+(Coding|Management|Design|Sales|Operations)\\s+XP/.test(
      panel.innerText
    );
    if (state === 'campaign') {
      const campaign = document.querySelector('.campaign-status');
      report.campaign = {
        present: !!campaign,
        text: campaign?.innerText,
        step: campaign?.dataset.campaignStep,
        filled: campaign?.querySelectorAll(
          '.campaign-progress-segment.filled'
        ).length
      };
    }
  } else if (
    state === 'context-pins' ||
    state === 'context-pins-zoom'
  ) {
    const context = document.querySelector('.morning-build-context');
    const pins = [...document.querySelectorAll('.pinned-task-summary')];
    const railArt = [...document.querySelectorAll(
      '#sp-resume .resume-family-art'
    )];
    report.buildContext = {
      present: !!context,
      labels: [...document.querySelectorAll(
        '.morning-build-context-label'
      )].map(element => element.textContent.trim()),
      details: [...document.querySelectorAll(
        '.morning-build-context-detail'
      )].map(element => element.textContent.trim()),
      apiTip: [...document.querySelectorAll(
        '.morning-build-context-entry'
      )].find(element => element.textContent.includes('API FOLLOW-UP'))
        ?.dataset.tip,
      entries: document.querySelectorAll(
        '.morning-build-context-entry'
      ).length
    };
    report.pins = {
      count: pins.length,
      fullCards: document.querySelectorAll(
        '.pinned-task-section .task-card'
      ).length,
      rows: pins.map(pin => ({
        skill: pin.querySelector('.pinned-task-skill')?.textContent.trim(),
        name: pin.querySelector('.pinned-task-name')?.textContent.trim(),
        rarity: pin.querySelector('.pinned-task-rarity')?.textContent.trim(),
        height: Math.round(pin.getBoundingClientRect().height)
      })),
      sectionOverflow: (() => {
        const section = document.querySelector('.pinned-task-section');
        return section ? section.scrollHeight - section.clientHeight : 0;
      })()
    };
    report.resumeRailArt = {
      count: railArt.length,
      baseOpacity: railArt.map(art => Number(getComputedStyle(art).opacity)),
      decorative: railArt.every(art =>
        art.getAttribute('aria-hidden') === 'true' &&
        getComputedStyle(art).pointerEvents === 'none'
      )
    };
  } else if (state === 'pinned-detail') {
    const modal = document.getElementById('pinned-task-detail');
    const card = modal.querySelector('.pinned-task-detail-card');
    report.pinnedDetail = {
      open: modal.classList.contains('open') &&
        modal.getAttribute('aria-hidden') === 'false',
      title: card?.querySelector('.task-card-title')?.textContent.trim(),
      skill: card?.querySelector('.task-family-banner')?.textContent.trim(),
      metrics: card?.querySelectorAll('.task-metric').length,
      effect: card?.querySelector('.task-effect')?.textContent.trim(),
      actions: [...modal.querySelectorAll(
        '.pinned-task-detail-actions button'
      )].map(button => button.textContent.trim()),
      focusedClose: document.activeElement === modal.querySelector(
        '.hud-modal-close'
      )
    };
  } else if (state === 'resume-tooltips') {
    const families = [...document.querySelectorAll(
      '#sp-resume .resume-family'
    )];
    const coding = [...families[0].querySelectorAll(
      '.resume-xp-segment.milestone'
    )].map(element => element.dataset.tip);
    const management = [...families[1].querySelectorAll(
      '.resume-xp-segment.milestone'
    )].map(element => element.dataset.tip);
    report.milestoneTooltips = {
      coding,
      management,
      visible: document.getElementById('global-tip').textContent.trim(),
      focusable: [...document.querySelectorAll(
        '#sp-resume .resume-xp-segment.milestone'
      )].every(element => element.tabIndex === 0)
    };
  } else if (state === 'trait-keywords') {
    const terms = [...document.querySelectorAll(
      '#resume-book-content .rules-keyword'
    )];
    const polish = terms.find(element => element.textContent === 'Polish');
    report.keywordGlossary = {
      count: terms.length,
      terms: [...new Set(terms.map(element => element.textContent))],
      focusable: terms.every(element => element.tabIndex === 0),
      color: polish ? getComputedStyle(polish).color : '',
      visible: document.getElementById('global-tip').textContent.trim(),
      focusText: document.activeElement === polish
        ? polish.textContent
        : ''
    };
  } else if (state === 'promotion-path') {
    report.choiceTitle = owChoiceState?.title;
    report.choiceSubtitle = owChoiceState?.subtitle;
    report.choiceDetails = (owChoiceState?.options || [])
      .map(option => option.detail || '');
  } else if (state === 'promotion-milestone') {
    report.choiceTitle = owChoiceState?.title;
    report.promotion = {
      shell: !!document.querySelector('.promotion-review-shell'),
      cash: document.querySelector('.promotion-cash')?.textContent.trim(),
      stress: document.querySelector('.promotion-stress')?.innerText.trim(),
      tabs: document.querySelectorAll('.promotion-skill-tab').length,
      page: document.querySelector('.promotion-page-title')?.textContent.trim(),
      levels: [...document.querySelectorAll('.promotion-level')]
        .map(element => element.textContent.trim()),
      cards: [...document.querySelectorAll('.promotion-milestone-card')]
        .map(element => element.innerText.trim()),
      actions: [...document.querySelectorAll('.promotion-review-actions button')]
        .map(button => button.textContent.trim()),
      footerInPanel: (() => {
        const footer = document.querySelector('.promotion-review-footer');
        if (!footer || !panel) return false;
        const footerRect = footer.getBoundingClientRect();
        const panelRect = panel.getBoundingClientRect();
        return visible(footer) &&
          footerRect.top >= panelRect.top - 1 &&
          footerRect.bottom <= panelRect.bottom + 1;
      })(),
      genericConfirm: [...document.querySelectorAll('#overlay-panel button')]
        .some(button => button.textContent.trim() === 'CONFIRM')
    };
  } else if (state === 'promotion-capstone') {
    report.choiceTitle = owChoiceState?.title;
    report.promotion = {
      shell: !!document.querySelector('.promotion-review-shell'),
      tabs: document.querySelectorAll('.promotion-skill-tab').length,
      page: document.querySelector('.promotion-page-title')?.textContent.trim(),
      capstone: document.querySelector('.promotion-capstone-card')?.innerText.trim(),
      actions: [...document.querySelectorAll('.promotion-review-actions button')]
        .map(button => button.textContent.trim()),
      footerInPanel: (() => {
        const footer = document.querySelector('.promotion-review-footer');
        if (!footer || !panel) return false;
        const footerRect = footer.getBoundingClientRect();
        const panelRect = panel.getBoundingClientRect();
        return visible(footer) &&
          footerRect.top >= panelRect.top - 1 &&
          footerRect.bottom <= panelRect.bottom + 1;
      })(),
      geometry: (() => {
        const rect = selector => {
          const element = document.querySelector(selector);
          if (!element) return null;
          const box = element.getBoundingClientRect();
          return {top: box.top, bottom: box.bottom, height: box.height};
        };
        return {
          panel: rect('#overlay-panel'),
          shell: rect('.promotion-review-shell'),
          body: rect('.promotion-review-body'),
          page: rect('.promotion-page'),
          footer: rect('.promotion-review-footer')
        };
      })()
    };
    report.revised = window.__owVisualCapstoneRevised === true;
  } else if (state === 'automation-combo') {
    const commandRow = document.querySelector('.automation-command-row');
    const choiceRow = document.querySelector('.automation-choice-row');
    report.choiceTitle = owChoiceState?.title;
    report.choiceSubtitle = owChoiceState?.subtitle;
    report.taskCards = document.querySelectorAll(
      '.automation-choice-row .card'
    ).length;
    const taskRects = [...document.querySelectorAll(
      '.automation-choice-row .task-choice-card'
    )].map(card => {
      const bounds = card.getBoundingClientRect();
      return {left: bounds.left, top: bounds.top, right: bounds.right};
    });
    report.taskCardLayout = {
      display: getComputedStyle(choiceRow).display,
      columns: getComputedStyle(choiceRow).gridTemplateColumns,
      sameRow: taskRects.length > 0 &&
        Math.max(...taskRects.map(rect => rect.top)) -
          Math.min(...taskRects.map(rect => rect.top)) < 2,
      contained: taskRects.every(rect =>
        rect.left >= choiceRow.getBoundingClientRect().left - 1 &&
        rect.right <= choiceRow.getBoundingClientRect().right + 1
      ),
      rects: taskRects
    };
    report.commands = [...document.querySelectorAll(
      '.automation-command-row .btn'
    )].map(button => ({
      label: button.textContent.trim(),
      visible: visible(button),
      disabled: button.disabled
    }));
    report.commandBeforeTasks = !!(
      commandRow &&
      choiceRow &&
      commandRow.compareDocumentPosition(choiceRow) &
        Node.DOCUMENT_POSITION_FOLLOWING
    );
    report.reroll = (owChoiceState?.options || []).find(
      option => option.label.startsWith('Reroll Offer')
    ) || null;
  } else if (state === 'resume') {
    report.tabs = document.querySelectorAll('.resume-book-tab').length;
    report.selected = document.querySelector(
      '.resume-book-tab[aria-selected="true"]'
    )?.textContent.trim();
    report.flavor = document.querySelector('.resume-proficiency')?.textContent.trim();
    report.xp = document.querySelector('.resume-xp-total')?.textContent.trim();
    report.milestones = {
      pending: document.querySelectorAll(
        '#side-panel .resume-xp-segment.milestone.pending'
      ).length,
      claimed: document.querySelectorAll(
        '#side-panel .resume-xp-segment.milestone.claimed'
      ).length,
      pendingMarker: document.querySelector(
        '#side-panel .resume-xp-segment.milestone.pending'
      )?.textContent.trim(),
      claimedMarker: document.querySelector(
        '#side-panel .resume-xp-segment.milestone.claimed'
      )?.textContent.trim()
    };
    report.impliedCopy = /No path selected|Choose a path at 3/.test(
      document.getElementById('side-panel').innerText
    );
  } else if (state === 'workday') {
    const guide = document.getElementById('day-action-legend');
    report.guideHidden = guide.getAttribute('aria-hidden') === 'true' &&
      !visible(guide);
    report.resultLine = document.getElementById('dt-result')?.textContent.trim();
  } else if (state === 'clockout') {
    report.groups = [...document.querySelectorAll(
      '.clockout-group h3 span:first-child'
    )].map(element => element.textContent.trim());
    report.sourceLog = !!document.querySelector('.clockout-log');
    report.routineXp = /(Coding|Management|Design|Sales|Operations) XP:\\s*\\d/.test(
      panel.innerText
    );
  } else if (
    state === 'night' ||
    state === 'night-sale' ||
    state === 'night-lights' ||
    state === 'outing-lights'
  ) {
    const scene = document.getElementById('home-scene');
    const occupied = document.querySelector('.home-scene-slot.occupied');
    const statusText = document.querySelector('.home-night-status')?.innerText || '';
    report.homeMode = document.body.classList.contains('home-mode');
    report.officeVisible = visible(document.getElementById('office-scene'));
    report.endDayCount = [...document.querySelectorAll('.home-hotspot-sleep')]
      .filter(visible).length;
    report.economy = {
      cash: document.querySelector('.home-night-status .cash')?.textContent.trim(),
      credit: document.querySelector('.home-night-status .credit')?.textContent.trim()
    };
    report.recovery = {
      stress: document.querySelector('.home-night-status .stress')?.textContent.trim(),
      sleep: document.querySelector('.home-night-status .recovery')?.textContent.trim(),
      expected: `SLEEP ${fmt1(R.stress)}% TO ${fmt1(owNightRecoveryPreview().finalStress)}%`,
      concise: !/HOME|DEALS|BONUS|OUTING/.test(statusText)
    };
    report.home = {
      present: visible(scene) && scene.classList.contains('active'),
      title: document.querySelector('.home-scene-title')?.textContent.trim(),
      slots: document.querySelectorAll('.home-scene-slot').length,
      occupied: document.querySelectorAll('.home-scene-slot.occupied').length,
      occupiedIsButton: occupied?.tagName === 'BUTTON',
      occupiedLabel: occupied?.getAttribute('aria-label'),
      stressBar: visible(document.querySelector('.home-stress-bar')),
      phone: visible(document.querySelector('.home-hotspot-phone')),
      oldBook: !!document.querySelector('.home-hotspot-book'),
      decor: [
        '.home-room-art', '.home-room-shelf', '.home-room-plant'
      ].filter(selector => visible(document.querySelector(selector))).length
    };
    const lights = document.querySelector('.home-hotspot-lights');
    report.lightsChecked = lights?.getAttribute('aria-pressed') === 'true';
    report.lightsDisabled = lights?.getAttribute('aria-disabled') === 'true';
    report.purchaseLocked = document.querySelector('.home-hotspot-shop')
      ?.textContent.includes('SHOP LOCKED');
    if (state === 'night-sale') {
      const popup = document.getElementById('sell-popup');
      report.sale = {
        present: !!popup,
        text: popup?.innerText,
        buttons: popup
          ? [...popup.querySelectorAll('button')].map(button =>
              button.textContent.trim()
            )
          : []
      };
    }
    if (state === 'outing-lights') {
      report.outing = {
        used: nightState.outingUsed,
        pid: nightState.outingPid,
        pending: nightState.pendingOuting,
        stalePicker: document.getElementById('overlay-panel')
          .innerText.includes('What are you doing with'),
        completedText: scene.innerText.includes('OUTING DONE')
      };
    }
  }
  return report;
}
"""


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        args=["--disable-extensions", "--no-first-run"],
        timeout=30000,
    )
    failures = []
    try:
        for name, width, height, state in CASES:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=1,
                reduced_motion="reduce",
            )
            page = context.new_page()
            page.goto(GAME_URL, wait_until="load", timeout=30000)
            page.wait_for_function(
                "document.documentElement.dataset.officewarsReady === 'true'",
                timeout=15000,
            )
            complete_orientation(page)
            phase = page.evaluate(SETUP, {"state": state})
            report = page.evaluate(LAYOUT_REPORT)
            readability = page.evaluate(READABILITY_REPORT, {"state": state})
            if report["overflow"]:
                failures.append(f"{name}: viewport overflow {report['overflow']}")
            if report["overlaps"]:
                failures.append(f"{name}: overlap {report['overlaps']}")
            if readability["overlayHorizontalOverflow"] > 1:
                failures.append(
                    f"{name}: overlay horizontal overflow "
                    f"{readability['overlayHorizontalOverflow']}"
                )
            if readability["modalHorizontalOverflow"] > 1:
                failures.append(
                    f"{name}: modal horizontal overflow "
                    f"{readability['modalHorizontalOverflow']}"
                )
            if readability["clippedText"]:
                failures.append(
                    f"{name}: clipped text {readability['clippedText']}"
                )
            project_bar = readability["projectBar"]
            if (
                not project_bar["topFill"]
                or not project_bar["topValue"]
                or not project_bar["topName"]
                or not project_bar["scrim"]
                or project_bar["bottomProject"]
                or not project_bar["bottomStress"]
            ):
                failures.append(f"{name}: project HUD structure {project_bar}")
            if state in {"morning", "text-zoom", "campaign"}:
                rail_art = readability.get("resumeRailArt") or {}
                if (
                    rail_art.get("count") != 5
                    or not rail_art.get("decorative")
                    or not rail_art.get("foregrounded")
                ):
                    failures.append(
                        f"{name}: Resume rail art {rail_art}"
                    )
                if readability["familyBanners"] < 3 or readability["routineXp"]:
                    failures.append(f"{name}: task hierarchy {readability}")
                if state == "campaign":
                    campaign = readability.get("campaign") or {}
                    campaign_text = campaign.get("text") or ""
                    if (
                        not campaign.get("present")
                        or campaign.get("step") != "2"
                        or campaign.get("filled") != 2
                        or "Brand Research" not in campaign_text
                        or "Creative Brief" not in campaign_text
                        or "2 OF 3 STEPS" not in campaign_text
                    ):
                        failures.append(
                            f"{name}: Campaign status {campaign}"
                        )
            elif state in {"context-pins", "context-pins-zoom"}:
                build_context = readability.get("buildContext") or {}
                pins = readability.get("pins") or {}
                art = readability.get("resumeRailArt") or {}
                labels = set(build_context.get("labels") or [])
                details = build_context.get("details") or []
                rows = pins.get("rows") or []
                if (
                    not build_context.get("present")
                    or build_context.get("entries") != 3
                    or not {
                        "DELEGATES 2", "CONTACTS 2", "API FOLLOW-UP"
                    }.issubset(labels)
                    or not any(
                        detail == "Karen, Dave" for detail in details
                    )
                    or not any(
                        detail == "Bob, Priya" for detail in details
                    )
                    or "Next Design primary task gains 1 additional Design XP"
                    not in (build_context.get("apiTip") or "")
                    or pins.get("count") != 2
                    or pins.get("fullCards") != 0
                    or pins.get("sectionOverflow") != 0
                    or any(
                        not row.get("skill")
                        or not row.get("name")
                        or not row.get("rarity")
                        or row.get("height", 999) > 128
                        for row in rows
                    )
                    or art.get("count") != 5
                    or not art.get("decorative")
                    or any(
                        opacity < 0.75
                        for opacity in art.get("baseOpacity") or []
                    )
                ):
                    failures.append(
                        f"{name}: Build Context or compact pins {readability}"
                    )
                if state == "context-pins":
                    first_pin = page.locator(".pinned-task-summary").first
                    first_pin.click()
                    modal = page.locator("#pinned-task-detail")
                    page.wait_for_function(
                        "document.activeElement?.classList"
                        ".contains('hud-modal-close')"
                    )
                    if (
                        "open" not in (modal.get_attribute("class") or "")
                        or page.evaluate(
                            "document.activeElement?.classList"
                            ".contains('hud-modal-close')"
                        ) is not True
                    ):
                        failures.append(
                            f"{name}: pinned detail did not open with focus"
                        )
                    page.keyboard.press("Escape")
                    page.wait_for_function(
                        "document.activeElement?.classList"
                        ".contains('pinned-task-summary')"
                    )
                    if (
                        "open" in (modal.get_attribute("class") or "")
                        or page.evaluate(
                            "document.activeElement?.classList"
                            ".contains('pinned-task-summary')"
                        ) is not True
                    ):
                        failures.append(
                            f"{name}: pinned detail focus was not restored"
                        )
                    first_pin.click()
                    page.get_by_role("button", name="SELECT TASK").click()
                    if page.evaluate(
                        "pendingMorning?.source === 'pin' && "
                        "getComputedStyle(document.getElementById("
                        "'morning-confirm')).display !== 'none'"
                    ) is not True:
                        failures.append(
                            f"{name}: pinned task selection did not arm confirmation"
                        )
            elif state == "pinned-detail":
                detail = readability.get("pinnedDetail") or {}
                if (
                    not detail.get("open")
                    or detail.get("title") != "Version Control"
                    or "CODING" not in (detail.get("skill") or "")
                    or detail.get("metrics") != 2
                    or not detail.get("effect")
                    or set(detail.get("actions") or []) != {
                        "SELECT TASK", "BACK"
                    }
                    or not detail.get("focusedClose")
                ):
                    failures.append(
                        f"{name}: expanded pinned task {readability}"
                    )
            elif state == "resume-tooltips":
                tips = readability.get("milestoneTooltips") or {}
                coding = tips.get("coding") or []
                management = tips.get("management") or []
                if (
                    len(coding) != 3
                    or len(management) != 3
                    or not all(
                        tip and tip.startswith("Automation")
                        for tip in coding
                    )
                    or not all(
                        tip == (
                            "Specialization is not chosen yet for this Skill!"
                        )
                        for tip in management
                    )
                    or "Automation" not in (tips.get("visible") or "")
                    or "6 XP" not in (tips.get("visible") or "")
                    or not tips.get("focusable")
                ):
                    failures.append(
                        f"{name}: Resume milestone tooltips {readability}"
                    )
                chosen = page.locator(
                    "#sp-resume .resume-family"
                ).nth(0).locator(
                    ".resume-xp-segment.milestone"
                ).nth(1)
                chosen.hover()
                if "Automation" not in page.locator("#global-tip").inner_text():
                    failures.append(
                        f"{name}: milestone hover tooltip failed"
                    )
                chosen.focus()
                if "6 XP" not in page.locator("#global-tip").inner_text():
                    failures.append(
                        f"{name}: milestone keyboard tooltip failed"
                    )
                unchosen = page.locator(
                    "#sp-resume .resume-family"
                ).nth(1).locator(
                    ".resume-xp-segment.milestone"
                ).first
                unchosen.dispatch_event(
                    "pointerdown", {"pointerType": "touch"}
                )
                if (
                    page.locator("#global-tip").inner_text().strip() !=
                    "Specialization is not chosen yet for this Skill!"
                ):
                    failures.append(
                        f"{name}: milestone touch tooltip failed"
                    )
            elif state == "trait-keywords":
                glossary = readability.get("keywordGlossary") or {}
                terms = set(glossary.get("terms") or [])
                if (
                    glossary.get("count", 0) < 6
                    or not {"Pinned Tasks", "Polish"}.issubset(terms)
                    or not glossary.get("focusable")
                    or glossary.get("color") != "rgb(140, 236, 255)"
                    or glossary.get("focusText") != "Polish"
                    or not (glossary.get("visible") or "").startswith(
                        "Polish:"
                    )
                ):
                    failures.append(
                        f"{name}: trait keyword glossary {readability}"
                    )
                keyword = page.locator(
                    "#resume-book-content .rules-keyword",
                    has_text="Pinned Tasks",
                ).first
                keyword.hover()
                if not page.locator("#global-tip").inner_text().startswith(
                    "Pinned Task:"
                ):
                    failures.append(
                        f"{name}: trait keyword hover tooltip failed"
                    )
                page.evaluate("hideGlobalTooltip()")
                keyword.dispatch_event(
                    "pointerdown", {"pointerType": "touch"}
                )
                if not page.locator("#global-tip").inner_text().startswith(
                    "Pinned Task:"
                ):
                    failures.append(
                        f"{name}: trait keyword touch tooltip failed"
                    )
            elif state == "promotion-path":
                details = readability.get("choiceDetails") or []
                if (
                    readability.get("choiceTitle") != "Promotion Review: Coding"
                    or not details
                    or any("3 XP:" not in detail for detail in details)
                    or any(
                        marker in detail
                        for detail in details
                        for marker in ("6 XP:", "10 XP:", "Capstone:")
                    )
                    or "revealed when you reach them"
                    not in (readability.get("choiceSubtitle") or "")
                ):
                    failures.append(
                        f"{name}: Promotion path disclosure {readability}"
                    )
            elif state == "promotion-milestone":
                promotion = readability.get("promotion") or {}
                cards = promotion.get("cards") or []
                actions = set(promotion.get("actions") or [])
                if (
                    readability.get("choiceTitle") != "Promotion Review"
                    or not promotion.get("shell")
                    or promotion.get("tabs") != 5
                    or promotion.get("page") != "CODING"
                    or promotion.get("levels") != ["3 XP", "6 XP"]
                    or len(cards) != 2
                    or not any("Common Coding primary tasks" in card for card in cards)
                    or not any("Additional-card prices scale by $50" in card for card in cards)
                    or any("Combo 10" in card for card in cards)
                    or actions != {"CONFIRM PROMOTION", "REVISE CHOICES"}
                    or not promotion.get("footerInPanel")
                    or promotion.get("genericConfirm")
                    or not (promotion.get("cash") or "").startswith("$")
                    or "STRESS" not in (promotion.get("stress") or "")
                ):
                    failures.append(
                        f"{name}: Promotion milestone disclosure {readability}"
                    )
            elif state == "promotion-capstone":
                promotion = readability.get("promotion") or {}
                actions = set(promotion.get("actions") or [])
                capstone = promotion.get("capstone") or ""
                if (
                    readability.get("choiceTitle") != "Promotion Review"
                    or not readability.get("revised")
                    or not promotion.get("shell")
                    or promotion.get("tabs") != 5
                    or promotion.get("page") != "CODING"
                    or "Zero Technical Debt" not in capstone
                    or "apply the Codebase bonus twice" not in capstone
                    or actions != {"CONFIRM PROMOTION", "REVISE CHOICES"}
                    or not promotion.get("footerInPanel")
                ):
                    failures.append(
                        f"{name}: Promotion capstone revision {readability}"
                    )
            elif state == "automation-combo":
                reroll = readability.get("reroll")
                commands = readability.get("commands") or []
                labels = {command.get("label") for command in commands}
                if (
                    readability.get("choiceTitle") != "Automation Combo 1"
                    or readability.get("taskCards") != 3
                    or not (readability.get("taskCardLayout") or {}).get("sameRow")
                    or not (readability.get("taskCardLayout") or {}).get("contained")
                    or not readability.get("commandBeforeTasks")
                    or not all(command.get("visible") for command in commands)
                    or not any(label.startswith("End Combo") for label in labels)
                    or not any(label.startswith("Free Reroll") for label in labels)
                    or not any(label.startswith("Task Reroll") for label in labels)
                    or not any(label.startswith("Reroll Offer") for label in labels)
                    or not reroll
                    or reroll.get("disabled")
                    or "cannot show Legendary cards"
                    not in (reroll.get("detail") or "")
                ):
                    failures.append(
                        f"{name}: Automation Combo reroll {readability}"
                    )
            elif state == "resume":
                if (
                    readability["tabs"] != 5
                    or readability["selected"] != "Coding"
                    or not readability["flavor"]
                    or "XP" not in readability["xp"]
                    or readability["milestones"].get("pending") != 1
                    or readability["milestones"].get("claimed") != 1
                    or readability["milestones"].get("pendingMarker") != "!"
                    or readability["milestones"].get("claimedMarker") != "✓"
                    or readability["impliedCopy"]
                ):
                    failures.append(f"{name}: Resume structure {readability}")
                page.locator(".resume-book-tab.active").press("ArrowRight")
                selected = page.locator(
                    '.resume-book-tab[aria-selected="true"]'
                ).inner_text().strip()
                if selected != "Management":
                    failures.append(f"{name}: Resume keyboard tabs {selected}")
            elif state == "workday":
                if not readability["guideHidden"] or not readability["resultLine"]:
                    failures.append(f"{name}: Workday feedback {readability}")
            elif state == "clockout":
                expected = {
                    "PROGRESS", "STRESS", "CASH", "RELATIONSHIPS", "CARRYOVER"
                }
                if (
                    not expected.issubset(set(readability["groups"]))
                    or not readability["sourceLog"]
                    or readability["routineXp"]
                ):
                    failures.append(f"{name}: Clock Out grouping {readability}")
            elif state in {
                "night", "night-sale", "night-lights", "outing-lights"
            }:
                economy = readability.get("economy") or {}
                recovery = readability.get("recovery") or {}
                home = readability.get("home") or {}
                if (
                    not readability.get("homeMode")
                    or readability.get("officeVisible")
                    or readability.get("endDayCount") != 1
                    or economy.get("cash") != "CASH $725"
                    or economy.get("credit") != "CREDIT $175"
                    or recovery.get("stress") != "STRESS 42%"
                    or recovery.get("sleep") != recovery.get("expected")
                    or not recovery.get("concise")
                    or not home.get("present")
                    or home.get("title") != "APARTMENT"
                    or home.get("slots") != 3
                    or home.get("occupied") != 1
                    or not home.get("occupiedIsButton")
                    or not home.get("stressBar")
                    or not home.get("phone")
                    or home.get("oldBook")
                    or "Standing Desk" not in
                        (home.get("occupiedLabel") or "")
                    or home.get("decor", 0) < 2
                ):
                    failures.append(f"{name}: Home hierarchy {readability}")
                if state == "night" and readability["purchaseLocked"]:
                    failures.append(f"{name}: Home purchases unexpectedly locked")
                if state == "night-sale":
                    sale = readability.get("sale") or {}
                    if (
                        not sale.get("present")
                        or "Sell Standing Desk for $88?" not in
                            (sale.get("text") or "")
                        or set(sale.get("buttons") or []) != {"SELL", "CANCEL"}
                    ):
                        failures.append(
                            f"{name}: Home sale confirmation {sale}"
                        )
                if state == "night-lights" and (
                    not readability["lightsChecked"]
                    or not readability["purchaseLocked"]
                ):
                    failures.append(f"{name}: Home Lights Out lock {readability}")
                if state == "outing-lights":
                    outing = readability.get("outing") or {}
                    if (
                        not readability["lightsChecked"]
                        or not outing.get("used")
                        or outing.get("pid") is not None
                        or outing.get("pending") is not None
                        or outing.get("stalePicker")
                        or not outing.get("completedText")
                    ):
                        failures.append(
                            f"{name}: completed Outing state {readability}"
                        )
                lights = page.locator(".home-hotspot-lights")
                if (
                    state == "night"
                    and
                    not readability["lightsChecked"]
                    and readability["lightsDisabled"] is not True
                ):
                    lights.click()
                    if not page.evaluate("nightState.recPicked"):
                        failures.append(f"{name}: Lights Out toggle did not persist")
            output = os.path.join(ROOT, f".visual-{name}.png")
            page.screenshot(path=output, animations="disabled")
            if not QUIET:
                print(
                    json.dumps(
                        {
                            "name": name,
                            "state": state,
                            "phase": phase,
                            "path": output,
                            "bytes": os.path.getsize(output),
                            "readability": readability,
                            **report,
                        },
                        separators=(",", ":"),
                    )
                )
            context.close()
    finally:
        browser.close()
    if failures:
        print("READABILITY_FAILURES=" + json.dumps(failures))
        raise SystemExit(1)
    print("PASS:READABILITY_VISUAL_MATRIX")
