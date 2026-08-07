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
        "schema": 1,
        "tutorial": {
            "completed": True,
            "nextStep": 6,
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
    ("desktop-night-lights", 1440, 900, "night-lights"),
    ("landscape-night-lights", 844, 390, "night-lights"),
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
  if (state === 'campaign') {
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
  } else if (state === 'night' || state === 'night-lights') {
    nightPhase();
    await waitFor(() => R.phase === 'night');
    if (state === 'night-lights') owToggleLightsOut(true);
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
    'resume-book'
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
    '#project-hud *,#overlay-panel *,#resume-book *,#day-ticker *,#side-panel *'
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
  } else if (state === 'resume') {
    report.tabs = document.querySelectorAll('.resume-book-tab').length;
    report.selected = document.querySelector(
      '.resume-book-tab[aria-selected="true"]'
    )?.textContent.trim();
    report.flavor = document.querySelector('.resume-proficiency')?.textContent.trim();
    report.xp = document.querySelector('.resume-xp-total')?.textContent.trim();
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
  } else if (state === 'night' || state === 'night-lights') {
    report.finalizeCount = [...document.querySelectorAll('button')]
      .filter(button => visible(button) &&
        button.textContent.trim() === 'FINALIZE NIGHT').length;
    report.lightsCard = [...document.querySelectorAll('.card')]
      .some(card => /Lights Out/i.test(card.textContent));
    report.footer = document.querySelector('.night-footer-summary')?.innerText;
    report.lightsChecked = document.querySelector(
      '.night-lights-toggle input'
    )?.checked;
    report.purchaseCardsDisabled = [...document.querySelectorAll(
      '#overlay-panel .card'
    )].every(card => card.disabled);
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
            elif state == "resume":
                if (
                    readability["tabs"] != 5
                    or readability["selected"] != "Coding"
                    or not readability["flavor"]
                    or "XP" not in readability["xp"]
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
            elif state in {"night", "night-lights"}:
                if (
                    readability["finalizeCount"] != 1
                    or readability["lightsCard"]
                    or "TONIGHT" not in readability["footer"]
                ):
                    failures.append(f"{name}: Night hierarchy {readability}")
                if state == "night-lights" and (
                    not readability["lightsChecked"]
                    or not readability["purchaseCardsDisabled"]
                    or "purchases unavailable" not in readability["footer"]
                ):
                    failures.append(f"{name}: Night Lights Out lock {readability}")
                lights = page.locator(".night-lights-toggle input")
                if not readability["lightsChecked"] and lights.is_enabled():
                    lights.check()
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
