import json
import os
import sys
from pathlib import Path


TEMP_ROOT = os.environ.get("TEMP") or os.environ.get("TMPDIR")
if TEMP_ROOT:
    sys.path.insert(0, os.path.join(TEMP_ROOT, "officewars-python"))

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
URL = (ROOT / "officewarsautobattler.html").as_uri()
META = {
    "schema": 4,
    "tutorial": {
        "completed": True,
        "nextStep": 10,
        "skipped": False,
        "replayRequested": False,
    },
    "settings": {"volume": 70},
}


def load(page):
    page.goto(URL, wait_until="load", timeout=30_000)
    page.evaluate(
        "(meta) => localStorage.setItem('officewars.meta.v1', JSON.stringify(meta))",
        META,
    )
    page.reload(wait_until="load", timeout=30_000)
    page.wait_for_function(
        "document.documentElement.dataset.officewarsReady === 'true'",
        timeout=30_000,
    )


def setup_home(page, home_id):
    page.evaluate(
        """(homeId) => {
          startRun({seed: 81210});
          hideOverlay();
          R.stress = 42;
          R.cash = 725;
          R.expenseCredit = 175;
          R.nightViewPreference = 'room';
          R.home = homeId;
          R.house = ['standingDesk'];
          R.today = R.today || {log: [], cardFlags: {}};
          R.today.additionalNightPurchases = 0;
          nightPhase();
          nightState.extraPurchaseCredits = 1;
          owRenderHomeScene();
        }""",
        home_id,
    )
    page.wait_for_function(
        "R.phase === 'night' && document.querySelector('#home-scene.active')"
    )


def visible_geometry(page, selector):
    return page.eval_on_selector_all(
        selector,
        """elements => elements.filter(element => {
          const style = getComputedStyle(element);
          const rect = element.getBoundingClientRect();
          return style.display !== 'none' && style.visibility !== 'hidden' &&
            rect.width > 0 && rect.height > 0;
        }).map(element => {
          const rect = element.getBoundingClientRect();
          return {
            label: element.textContent.trim(),
            left: rect.left,
            top: rect.top,
            right: rect.right,
            bottom: rect.bottom,
            width: rect.width,
            height: rect.height
          };
        })""",
    )


def check_viewport(rects, width, height):
    return all(
        rect["left"] >= -1
        and rect["top"] >= -1
        and rect["right"] <= width + 1
        and rect["bottom"] <= height + 1
        for rect in rects
    )


def main():
    failures = []
    evidence = {}
    homes = [
        ("apartment", "APARTMENT", 3),
        ("townhouse", "TOWNHOUSE", 6),
        ("house", "HOUSE", 9),
        ("penthouse", "PENTHOUSE", 12),
    ]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            args=["--allow-file-access-from-files", "--disable-extensions"],
        )
        try:
            for name, width, height in [
                ("desktop", 1440, 900),
                ("landscape", 844, 390),
            ]:
                context = browser.new_context(viewport={"width": width, "height": height})
                page = context.new_page()
                page_errors = []
                console_errors = []
                page.on("pageerror", lambda error: page_errors.append(str(error)))
                page.on(
                    "console",
                    lambda message: (
                        console_errors.append(message.text)
                        if message.type == "error"
                        else None
                    ),
                )
                load(page)
                evidence[name] = {"homes": {}}
                for home_id, home_title, slot_count in homes:
                    setup_home(page, home_id)
                    home = page.evaluate(
                        """() => {
                          const rect = selector => {
                            const element = document.querySelector(selector);
                            if (!element) return null;
                            const value = element.getBoundingClientRect();
                            return {
                              left:value.left, top:value.top, right:value.right,
                              bottom:value.bottom, width:value.width, height:value.height
                            };
                          };
                          const room = rect('.home-room');
                          const windowRect = rect('.home-room-window');
                          const moon = rect('.home-window-moon');
                          const slotRects = [...document.querySelectorAll('.home-scene-slot')]
                            .map(element => {
                              const value = element.getBoundingClientRect();
                              return {
                                left:value.left, top:value.top, right:value.right,
                                bottom:value.bottom, width:value.width, height:value.height
                              };
                            });
                          const stressTrack = rect('.home-stress-bar');
                          const stressFill = rect('.home-stress-fill');
                          return {
                            phase: R.phase,
                            homeMode: document.body.classList.contains('home-mode'),
                            scene: !!document.querySelector('#home-scene.active'),
                            overlay: document.getElementById('overlay').classList.contains('active'),
                            officeHudHidden: getComputedStyle(
                              document.getElementById('run-hud')
                            ).display === 'none',
                            slots: slotRects.length,
                            slotRects,
                            occupied: document.querySelectorAll(
                              '.home-scene-slot.occupied'
                            ).length,
                            occupiedLabel: document.querySelector(
                              '.home-scene-slot.occupied'
                            )?.getAttribute('aria-label'),
                            status: document.querySelector(
                              '.home-night-status'
                            )?.innerText,
                            title: document.querySelector(
                              '.home-scene-title'
                            )?.textContent.trim(),
                            titleRect: rect('.home-scene-title'),
                            room,
                            windowRect,
                            moon,
                            shop: rect('.home-hotspot-shop'),
                            tablet: rect('.home-hotspot-tablet'),
                            deals: rect('.home-hotspot-deals'),
                            bed: rect('.home-hotspot-sleep'),
                            door: rect('.home-hotspot-outings'),
                            plant: rect('.home-room-plant'),
                            switchRect: rect('.home-hotspot-lights'),
                            pcParts: document.querySelectorAll(
                              '.home-pc-monitor,.home-pc-neck,.home-pc-base,' +
                              '.home-pc-tower,.home-pc-keyboard,.home-pc-mouse'
                            ).length,
                            tabletPresent: !!document.querySelector(
                              '.home-hotspot-tablet .home-phone-visual'
                            ),
                            oldBookPresent: !!document.querySelector('.home-hotspot-book'),
                            stressRatio: stressTrack && stressFill
                              ? stressFill.width / stressTrack.width
                              : -1
                          };
                        }"""
                    )
                    rects = visible_geometry(
                        page,
                        ".home-hotspot,.home-night-status,.home-scene-slot",
                    )
                    window_contains_moon = (
                        home["moon"]
                        and home["windowRect"]
                        and home["moon"]["left"] >= home["windowRect"]["left"] - 1
                        and home["moon"]["top"] >= home["windowRect"]["top"] - 1
                        and home["moon"]["right"] <= home["windowRect"]["right"] + 1
                        and home["moon"]["bottom"] <= home["windowRect"]["bottom"] + 1
                    )
                    wall_bottom = (
                        home["room"]["top"] + home["room"]["height"] * 0.865
                        if home["room"]
                        else height
                    )
                    slots_on_wall = bool(home["slotRects"]) and all(
                        rect["top"] >= home["room"]["top"] - 1
                        and rect["bottom"] <= wall_bottom + 5
                        for rect in home["slotRects"]
                    )
                    floor_line = (
                        home["room"]["bottom"] - home["room"]["height"] * 0.10
                        if home["room"]
                        else height
                    )
                    grounded = all(
                        rect
                        and abs(rect["bottom"] - floor_line)
                        <= max(3, home["room"]["height"] * 0.018)
                        for rect in [
                            home["shop"],
                            home["tablet"],
                            home["deals"],
                            home["bed"],
                            home["door"],
                            home["plant"],
                        ]
                    )
                    title_below_furniture = (
                        home["titleRect"]
                        and home["titleRect"]["top"] >= floor_line - 1
                        and home["titleRect"]["bottom"] <= home["room"]["bottom"] + 1
                    )
                    side_view_order = all(
                        home[left]["left"] < home[right]["left"]
                        for left, right in [
                            ("bed", "tablet"),
                            ("tablet", "shop"),
                            ("shop", "deals"),
                            ("deals", "door"),
                        ]
                    )
                    bed_reads_large = (
                        home["bed"]
                        and home["tablet"]
                        and home["bed"]["width"] >= home["tablet"]["width"] * 2.4
                        and home["bed"]["height"] >= home["tablet"]["height"] * 1.2
                    )
                    if not (
                        home["phase"] == "night"
                        and home["homeMode"]
                        and home["scene"]
                        and not home["overlay"]
                        and home["officeHudHidden"]
                        and home["slots"] == slot_count
                        and home["occupied"] == 1
                        and "Standing Desk" in (home["occupiedLabel"] or "")
                        and "CASH $725" in (home["status"] or "")
                        and "CREDIT $175" in (home["status"] or "")
                        and home["title"] == home_title
                        and "SLOT" not in home["title"]
                        and window_contains_moon
                        and slots_on_wall
                        and grounded
                        and title_below_furniture
                        and side_view_order
                        and bed_reads_large
                        and home["pcParts"] == 6
                        and home["tabletPresent"]
                        and not home["oldBookPresent"]
                        and abs(home["stressRatio"] - 0.42) <= 0.03
                        and check_viewport(rects, width, height)
                    ):
                        failures.append(
                            f"{name}:{home_id}:home-shell:{home}:{rects}:"
                            f"moon={window_contains_moon}:wall={slots_on_wall}:"
                            f"floor={floor_line}:grounded={grounded}:"
                            f"titleBelow={title_below_furniture}:order={side_view_order}:"
                            f"bed={bed_reads_large}"
                        )

                    page.click(".home-hotspot-shop")
                    shop = page.evaluate(
                        """() => ({
                          overlay: document.getElementById('overlay').classList.contains('active'),
                          title: document.querySelector('.night-panel-header h2')?.textContent,
                          cards: document.querySelectorAll(
                            '.night-home-desk .card'
                          ).length,
                          back: [...document.querySelectorAll(
                            '.night-panel-header button'
                            )].some(button => button.textContent.includes('RETURN TO ROOM'))
                        })"""
                    )
                    if not (
                        shop["overlay"]
                        and shop["title"] == "Home Shop"
                        and shop["cards"] == 3
                        and shop["back"]
                    ):
                        failures.append(f"{name}:{home_id}:home-shop:{shop}")
                    page.click(".night-panel-header button")
                    page.wait_for_function(
                        "!document.getElementById('overlay').classList.contains('active')"
                    )

                    page.click(".home-hotspot-lights")
                    lights = page.evaluate(
                        """() => ({
                          picked: nightState.recPicked,
                          pressed: document.querySelector(
                            '.home-hotspot-lights'
                          )?.getAttribute('aria-pressed'),
                          sceneDimmed: document.getElementById(
                            'home-scene'
                          )?.classList.contains('lights-out'),
                          roomDimOpacity: Number(getComputedStyle(
                            document.querySelector('.home-room'),
                            '::before'
                          ).opacity),
                          switchActive: document.querySelector(
                            '.home-hotspot-lights'
                          )?.classList.contains('active'),
                          shopLabel: document.querySelector(
                            '.home-hotspot-shop .home-hotspot-label'
                          )?.textContent
                        })"""
                    )
                    if not (
                        lights["picked"]
                        and lights["pressed"] == "true"
                        and lights["sceneDimmed"]
                        and lights["roomDimOpacity"] > 0.5
                        and lights["switchActive"]
                        and lights["shopLabel"] == "SHOP LOCKED"
                    ):
                        failures.append(f"{name}:{home_id}:lights-out:{lights}")

                    page.evaluate("owToggleLightsOut(false)")
                    page.screenshot(
                        path=ROOT / f".visual-home-{home_id}-{name}.png",
                        animations="disabled",
                    )
                    evidence[name]["homes"][home_id] = {
                        "home": home,
                        "shop": shop,
                        "lights": lights,
                        "hotspotGeometry": rects,
                    }

                page.evaluate(
                    """() => {
                      owExitHomeMode();
                      R.floor = 1;
                      R.manager = MANAGERS[0];
                      R.phase = 'morning';
                      renderCast();
                      updateHUD();
                    }"""
                )
                static_manager = page.evaluate(
                    """() => {
                      const avatar = document.getElementById('manager-office-avatar');
                      return {
                        manager: R.manager.id,
                        visible: getComputedStyle(avatar).display !== 'none',
                        roamer: !!document.querySelector('.manager-roamer'),
                        aria: avatar.getAttribute('aria-label'),
                        color: getComputedStyle(avatar).backgroundColor,
                        label: document.getElementById('manager-office-label')?.textContent
                      };
                    }"""
                )
                page.screenshot(
                    path=ROOT / f".visual-manager-static-v2-{name}.png",
                    animations="disabled",
                )
                manager_variants = page.evaluate(
                    """() => MANAGERS.map(manager => {
                      R.manager = manager;
                      renderCast();
                      const avatar = document.getElementById('manager-office-avatar');
                      return {
                        id: manager.id,
                        aria: avatar.getAttribute('aria-label'),
                        color: getComputedStyle(avatar).backgroundColor,
                        glyph: avatar.textContent.trim()
                      };
                    })"""
                )
                page.evaluate(
                    """() => {
                      R.floor = 3;
                      R.manager = MANAGERS[2];
                      renderCast();
                    }"""
                )
                boss_manager = page.evaluate(
                    """() => {
                      const avatar = document.getElementById('manager-office-avatar');
                      const roamer = document.querySelector('.manager-roamer');
                      const rect = roamer?.getBoundingClientRect();
                      return {
                        manager: R.manager.id,
                        staticHidden: getComputedStyle(avatar).display === 'none',
                        roamer: !!roamer,
                        roamerVisible: !!(
                          roamer &&
                          getComputedStyle(roamer).display !== 'none' &&
                          rect && rect.width > 0 && rect.height > 0 &&
                          rect.left >= 0 && rect.top >= 0 &&
                          rect.right <= innerWidth && rect.bottom <= innerHeight
                        ),
                        roamerRect: rect ? {
                          left:rect.left, top:rect.top, right:rect.right,
                          bottom:rect.bottom, width:rect.width, height:rect.height
                        } : null,
                        animationName: roamer ? getComputedStyle(roamer).animationName : '',
                        animationDuration: roamer
                          ? getComputedStyle(roamer).animationDuration
                          : '',
                        label: document.getElementById('manager-office-label')?.textContent,
                        castCount: CAST.length,
                        gameplayManagerAbsent: !CAST.some(member => member.id === 'manager')
                      };
                    }"""
                )
                manager_colors = {item["color"] for item in manager_variants}
                if not (
                    static_manager["visible"]
                    and not static_manager["roamer"]
                    and "Micromanager" in (static_manager["aria"] or "")
                    and len(manager_variants) == 8
                    and len(manager_colors) == 8
                    and all(item["glyph"] and item["aria"] for item in manager_variants)
                    and boss_manager["staticHidden"]
                    and boss_manager["roamer"]
                    and boss_manager["roamerVisible"]
                    and boss_manager["animationName"] == "manager-office-patrol"
                    and boss_manager["label"] == "PENNY-PINCHER"
                    and boss_manager["gameplayManagerAbsent"]
                ):
                    failures.append(
                        f"{name}:manager:{static_manager}:"
                        f"{manager_variants}:{boss_manager}"
                    )
                transition_arcs = page.evaluate(
                    """() => {
                      const wanted = new Set([
                        'ow-arc-ascend','ow-arc-descend'
                      ]);
                      const found = {};
                      for (const sheet of document.styleSheets) {
                        for (const rule of sheet.cssRules || []) {
                          if (rule.type === CSSRule.KEYFRAMES_RULE && wanted.has(rule.name)) {
                            found[rule.name] = {
                              steps: rule.cssRules.length,
                              text: [...rule.cssRules].map(step => step.cssText).join(' '),
                              transforms: [...rule.cssRules].map(
                                step => step.style.transform
                              )
                            };
                          }
                        }
                      }
                      return found;
                    }"""
                )
                # The sun and moon share one right/east-to-left/west arc but
                # never occupy the same stretch of it. One body plays the
                # ascending eastern half while the other plays the descending
                # western half.
                expected_arc_directions = {
                    "ow-arc-ascend": "translate(-26vw",
                    "ow-arc-descend": "translate(-74vw",
                }
                if any(
                    transition_arcs.get(key, {}).get("steps", 0) < 3
                    or expected not in transition_arcs.get(key, {}).get("text", "")
                    for key, expected in expected_arc_directions.items()
                ):
                    failures.append(f"{name}:transition-arcs:{transition_arcs}")
                exit_text = transition_arcs.get("ow-arc-descend", {}).get(
                    "text", ""
                )
                if "100vw" not in exit_text or "6rem" not in exit_text:
                    failures.append(f"{name}:transition-arc-exit:{transition_arcs}")
                ascend = transition_arcs.get("ow-arc-ascend", {}).get("transforms", [])
                descend = transition_arcs.get("ow-arc-descend", {}).get(
                    "transforms", []
                )
                # The two halves must be cut from one path and join at the apex,
                # so the arriving body lands exactly where the departing body
                # started.
                if not ascend or not descend or ascend[-1] != descend[0]:
                    failures.append(f"{name}:transition-apex:{ascend}:{descend}")
                transition_phasing = page.evaluate(
                    """() => {
                      const root = document.getElementById('phase-transition');
                      const read = phase => {
                        root.className = `active ${phase}`;
                        const sun = getComputedStyle(
                          root.querySelector('.transition-sun')
                        );
                        const moon = getComputedStyle(
                          root.querySelector('.transition-moon')
                        );
                        return {
                          sun: {
                            name:sun.animationName,
                            delay:sun.animationDelay,
                            duration:sun.animationDuration,
                            timing:sun.animationTimingFunction,
                            left:sun.left,
                            right:sun.right
                          },
                          moon: {
                            name:moon.animationName,
                            delay:moon.animationDelay,
                            duration:moon.animationDuration,
                            timing:moon.animationTimingFunction,
                            left:moon.left,
                            right:moon.right
                          }
                        };
                      };
                      const result = {
                        sunset:read('sunset'),
                        sunrise:read('sunrise')
                      };
                      root.className = '';
                      return result;
                    }"""
                )
                sunset_phase = transition_phasing["sunset"]
                sunrise_phase = transition_phasing["sunrise"]
                # Opposing halves, not a shared path with a delay offset: every
                # delay is zero and the two bodies always run opposite halves.
                if not (
                    sunset_phase["sun"]["delay"] == "0s"
                    and sunset_phase["moon"]["delay"] == "0s"
                    and sunrise_phase["sun"]["delay"] == "0s"
                    and sunrise_phase["moon"]["delay"] == "0s"
                    and sunset_phase["sun"]["name"] == "ow-arc-descend"
                    and sunset_phase["moon"]["name"] == "ow-arc-ascend"
                    and sunrise_phase["sun"]["name"] == "ow-arc-ascend"
                    and sunrise_phase["moon"]["name"] == "ow-arc-descend"
                    and sunset_phase["sun"]["duration"]
                    == sunset_phase["moon"]["duration"]
                    and sunrise_phase["sun"]["duration"]
                    == sunrise_phase["moon"]["duration"]
                    and sunset_phase["sun"]["timing"] == "linear"
                    and sunset_phase["moon"]["timing"] == "linear"
                    and sunrise_phase["sun"]["timing"] == "linear"
                    and sunrise_phase["moon"]["timing"] == "linear"
                    and all(
                        float(body["right"].replace("px", "")) < 0
                        for phase in [sunset_phase, sunrise_phase]
                        for body in phase.values()
                    )
                ):
                    failures.append(
                        f"{name}:transition-phasing:{transition_phasing}"
                    )
                page.screenshot(
                    path=ROOT / f".visual-manager-boss-v2-{name}.png",
                    animations="disabled",
                )

                page.evaluate(
                    """() => {
                      owExitHomeMode();
                      R.phase = 'morning';
                      updateHUD();
                      owChoiceState = {
                        title: 'Prototype Test',
                        subtitle: 'Compare the highlighted differences.',
                        options: [
                          {
                            label: 'Schedule 1',
                            scheduleRow: owScheduleDisplayEntries([
                              'work','cooler','lunch','mad','meeting'
                            ]),
                            value: 1
                          },
                          {
                            label: 'Schedule 2',
                            scheduleRow: owScheduleDisplayEntries([
                              'work','slump','lunch','meeting','cooler'
                            ]),
                            value: 2
                          }
                        ],
                        min: 1,
                        max: 1,
                        selected: [],
                        resolve: () => {}
                      };
                      owRenderChoice();
                    }"""
                )
                schedule = page.evaluate(
                    """() => ({
                      rows: document.querySelectorAll(
                        '.schedule-choice-row'
                      ).length,
                      nodes: document.querySelectorAll(
                        '.schedule-choice-row .schedule-node'
                      ).length,
                      differences: document.querySelectorAll(
                        '.schedule-node.different'
                      ).length,
                      overflow: Math.max(
                        0,
                        document.getElementById('overlay-panel').scrollWidth -
                        document.getElementById('overlay-panel').clientWidth
                      )
                    })"""
                )
                if not (
                    schedule["rows"] == 2
                    and schedule["nodes"] == 10
                    and schedule["differences"] >= 2
                    and schedule["overflow"] == 0
                ):
                    failures.append(f"{name}:schedule-comparison:{schedule}")
                page.screenshot(
                    path=ROOT / f".visual-schedule-tracker-{name}.png",
                    animations="disabled",
                )

                if page_errors or console_errors:
                    failures.append(
                        f"{name}:browser-errors:{page_errors}:{console_errors}"
                    )
                evidence[name]["manager"] = {
                    "static": static_manager,
                    "variants": manager_variants,
                    "boss": boss_manager,
                    "transitionArcs": transition_arcs,
                }
                evidence[name]["schedule"] = schedule
                context.close()
        finally:
            browser.close()

    print(json.dumps(evidence, separators=(",", ":")))
    if failures:
        print("FAIL:" + json.dumps(failures))
        return 1
    print("PASS:HOME_SCHEDULE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
