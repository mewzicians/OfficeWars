# Office Politics Wrap-Up Chrome Repair

Date: 2026-10-22  
Rigor: standard  
Candidate SHA-256:
`1DA11A1FEC21B8AED383B1BDD53F2AAB0DAB55ADA8E2F1B188F26407DEFEC149`  
Candidate size: `1,731,492` bytes  
Predecessor: `816A35B40CD4F36C6CF25CD766BF6FEB94A1D77D885C56947B73F6C4228F52AA`

## Defect

While the Office Politics wrap-up reel was open, the day ticker, the 1x and
SKIP DAY playback controls, and the HUD (`#run-hud`, `#project-hud`,
`#rival-hud`, `#player-hud`) stayed on top of it. At 1280x800 the ticker
covered the reel title and the HUD covered its first result; at 844x390 the
HUD covered the title and most of the first page. SKIP DAY stayed enabled and
only relabelled itself SKIPPING.

Reproduced with seed 73001 at 844x390, 1280x800, and 1440x900, with and
without reduced motion, in headless Chromium, by playing Morning through the
first political choice to the reel.

## Root Cause

`owRunCinematicWorkDay` presents the reel while the Workday is still active
and clears the ticker, Action Guide, and playback controls only after the reel
resolves. The reel renders inside `#workday-stage` (`z-index:52`), below the
fixed ticker (`z-index:60`) and HUD, and nothing hid them for the reel. The
restored reel never re-activates the ticker, so live and restored reels
differed.

## Repair

One CSS rule beside the political-focus rule hides the day ticker, Action
Guide, playback controls, and the four HUD elements whenever
`#workday-stage.results-active` is present, following the existing Clock Out
`:has()` rule. The user approved hiding the HUD for the wrap-up on 2026-10-22.

No JavaScript, gameplay state, RNG, schema, persistence, or balance value
changed.

## Evidence

| Suite | Result |
|---|---|
| `.officewars-no-scroll-verify.py`, extended with a wrap-up check | Pass 354/354 surface checks, 38 cases |
| Same suite against the predecessor | Fail: 14 wrap-up surfaces at desktop, short landscape, and 200% text; only the new check failed |
| `.officewars-cinematic-workday-verify.py` | Pass 33/33 |
| `.officewars-guided-intern-verify.py` | Pass 47/47 |
| `.officewars-guided-reachability-verify.py` | Pass 364/364 |
| `.officewars-persistence-verify.py` | Pass 30/30 |
| `.officewars-smoke-run.py` | Pass |
| `.officewars-visual-capture.py` | Pass |
| Inline script parse and page errors | Pass; none |
| Live and restored reel, seed 73001, at 844x390, 1280x800, and 1440x900 | Pass: chrome hidden over both reels; ticker and controls still shown during actions; Clock Out unchanged |

## Boundaries

Not Run: the remaining focused suites, simulations, formal screen-reader
execution, real-browser checks outside headless Chromium, and human
playtesting. The mirror is synchronized, and the candidate was published to
GitHub `main` on 2026-10-22 without the balance ledger. No release ZIP was
built.
