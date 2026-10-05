# Cash Jar Release Blocker Repair And Policy Verification

Date: 2026-09-22

## Candidate

- SHA-256:
  `6CCB5E58F326FC5D9C453FC8097DA1C0FCD2C0F29A4EB4EFA6B0C0C4EC5CB395`
- Size: `1,541,720` bytes
- Active-run schema: 9
- Cash Jar target schema: 10, inactive
- Cash Jar public gate: disabled

## Delegation Floor Briefing Race

### Symptom

The full simulator intermittently failed after promotion with:

`Simulation expected morning, received floorIntro.`

Known failing seeds included baseline `910001` and random `1010027`.

### Root Cause

The Delegation `floorIntro()` wrapper launched
`owPhase4RunFloorBriefing()` with `void` and returned immediately.
`owRunPromotionReview()` also returned immediately after `nextFloor()`.
Headless simulation could therefore start Morning before the briefing promise
completed; the late callback then rendered Floor Intro and overwrote the phase.

### Repair

- Base `nextFloor()` now returns the current `floorIntro()` result.
- The Phase 4 `nextFloor()` wrapper propagates that result.
- The Phase 4 `floorIntro()` wrapper returns the Floor Briefing promise.
- `owRunPromotionReview()` returns the `nextFloor()` transition.

Interactive callers still ignore the returned promise as before. Headless
callers can now await the existing authored decision boundary without sleeps,
phase suppression, or changed RNG consumption.

### Evidence

- Fixed-seed diagnostic: 5/5 previously failing/control runs completed.
- Full audit: baseline 250/250, random 250/250, skilled 250/250; zero phase
  errors.
- Delegation remained selected in 20 baseline and 3 random runs.
- Phase 4, Phase 5, Timeline, Galactic, Reality, persistence, advanced,
  cinematic, Cash Jar core/release UI, inventory, and smoke suites passed.

## Player-Legal Cash Jar Policy

Policy ID: `cash-jar-visible-v1`

### Information The Policy May Use

- visible task cards and their visible manager-package costs;
- visible Night Home offers and legal purchase state;
- visible Cash Jar Tier, Cash band, exact stake, floor, and Keep availability;
- visible story choice IDs and labels; and
- fully described visible Galactic event choices.

### Information Excluded

- hidden Cash Jar outcome weights;
- hidden outcome text;
- saved secret outcome rolls;
- future RNG; and
- unoffered Home items.

### Behavior

- Buy Cash Jar only when it is in the visible Night offer and
  `owCanPurchaseHomeCard` says the purchase is legal.
- While intact, prefer visible zero-Cash manager packages and avoid visible
  reserve/debt cards that would schedule Cash outflow.
- End Automation Combos rather than buy additional cards while the Jar is
  intact.
- Make no optional Night Cash purchase while the Jar is intact.
- Keep only while a later Weekend exists and current Tier is below the
  experiment's target Tier; otherwise Open.
- Choose the first visible story label. Outcome weights and text are never
  available to the callback.
- Choose the first visible beneficial Galactic event choice.

The target Tier is an experiment parameter, not a gameplay recommendation.

### Simulator Support

The shared simulator now:

- routes intact-Jar Weekends through the live Keep/Open and story authorities;
- uses sanitized visible route and story views for policy callbacks;
- preserves Floor 3 Casino routing;
- falls through to the existing Galactic simulator wrapper after the Jar is
  opened;
- reports Cash Jar status, Tier, acquisition, break/Open state, outcomes, and
  route counts; and
- leaves the public feature gate disabled.

### Legality And Determinism

The policy verifier passed 13/13:

- no hidden-outcome references in route or story callbacks;
- route/story views expose only approved visible fields;
- every purchase was visible, legal, and consumed the complete wallet at its
  Cash Jar purchase transaction;
- every selected route was enabled;
- every story choice was visible;
- intact-Jar mornings selected zero-Cash packages whenever one existed;
- natural acquisition and settled outcomes occurred;
- 20 paired seeds reproduced exact reports and decisions;
- no simulation, browser, or console errors occurred; and
- schema, gate, and Draft-law boundaries remained unchanged.

## 300-Run Telemetry

Seeds:

- target Tier 1: `1120000-1120099`;
- target Tier 2: `1220000-1220099`; and
- target Tier 3: `1320000-1320099`.

| Metric | Result |
|---|---:|
| Runs | 300 |
| Natural legal acquisitions | 90 |
| Opened Jars | 29 |
| Intact at defeat/end | 61 |
| Broken Jars | 0 |
| Settled outcomes | 29 |
| Invalid purchases | 0 |
| Simulation/browser errors | 0 |

Route results:

| Target | Acquisitions | Keeps | Opens | Outcomes |
|---|---:|---:|---:|---:|
| Tier 1 | 27 | 0 | 20 | 20 |
| Tier 2 | 30 | 25 | 9 | 9 |
| Tier 3 | 33 | 25 | 0 | 0 |

Opened cells:

- Tier 1 / Band 1: 3;
- Tier 1 / Band 2: 12;
- Tier 1 / Band 3: 5; and
- Tier 2 / Band 3: 9.

Eight distinct outcome IDs settled. Tier 3 produced no Opens because no
intact-Jar run survived through a third successful Weekend. This is a reach
and policy-quality limitation, not a legality defect.

All 300 runs still lost: the policy is an instrument for legal Cash Jar
exposure, not evidence that current balance meets the 25-35% skilled target.
No balance values were changed.

## Artifact Hashes

- `.officewars-cash-jar-simulation-diagnostic.py`:
  `6F0283319B8C338C645F0194A66C87D63325D79CE9846056D12A2179FF82E886`
- `.officewars-cash-jar-policy-telemetry.py`:
  `DDB3EEF88F00F4263A5DF22516095B6F98C647D2E9868F0AEF21356CCE98DCEC`

## Decision

The Delegation Floor Briefing headless race is fixed. A deterministic,
player-legal Cash Jar simulation policy now exists and has verified natural
acquisition, Keep/Open, and outcome settlement.

Cash Jar remains gated. High-tier balance and player-facing release readiness
still require a stronger legal policy or human evidence that can survive to
later floors, followed by a separate activation decision.
