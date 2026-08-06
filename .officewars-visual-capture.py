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

CASES = [
    ("desktop-morning", 1440, 900, "morning"),
    ("compact-morning", 1024, 700, "morning"),
    ("landscape-morning", 844, 390, "morning"),
    ("portrait-rotate", 390, 844, "morning"),
    ("desktop-workday", 1440, 900, "workday"),
    ("landscape-workday", 844, 390, "workday"),
    ("desktop-night", 1440, 900, "night"),
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
  if (state === 'workday') {
    OfficeWarsTest.setTimingScale(3);
    const common = R.morningCards.findIndex(card => card.rarity === 'common');
    selectMorning(common >= 0 ? common : 0, 'offer');
    await confirmMorning();
    await waitFor(() => R.phase === 'workday');
  } else if (state === 'night') {
    nightPhase();
    await waitFor(() => R.phase === 'night');
  }
  return R.phase;
}
"""

LAYOUT_REPORT = """
() => {
  const ids = [
    'run-hud', 'project-hud', 'rival-hud', 'player-hud', 'side-panel',
    'day-playback-controls', 'day-ticker', 'day-action-legend', 'overlay-panel'
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


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        args=["--disable-extensions", "--no-first-run"],
        timeout=30000,
    )
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
            phase = page.evaluate(SETUP, {"state": state})
            report = page.evaluate(LAYOUT_REPORT)
            output = os.path.join(ROOT, f".visual-{name}.png")
            page.screenshot(path=output, animations="disabled")
            print(
                json.dumps(
                    {
                        "name": name,
                        "state": state,
                        "phase": phase,
                        "path": output,
                        "bytes": os.path.getsize(output),
                        **report,
                    },
                    separators=(",", ":"),
                )
            )
            context.close()
    finally:
        browser.close()
