# OfficeWars Current Handoff

Last updated: 2026-08-06

## Read First

1. `AGENTS.md`
2. `docs/GAME_DESIGN.md`
3. `docs/BALANCE_LEDGER.md`
4. This file
5. `docs/PATCH_NOTES_SKIP_FIX_2026-08-06.md` for the current Skip repair

Read `docs/ARCHIVE_SUPERSEDED.md` only when historical reasoning is needed.

## Sources Of Truth

- `officewarsautobattler.html` is the implemented game.
- `docs/GAME_DESIGN.md` is the stable product model.
- `docs/BALANCE_LEDGER.md` contains active Implemented, Locked, Draft, and Open
  decisions.
- `docs/PROJECT_STATUS.md` records the latest public snapshot and balance
  evidence.

## Implementation Status

`officewarsautobattler.html` now contains the complete approved overhaul
candidate through rollout Phase 6: core balance, the fixed-rarity 50-card
roster, shared card and schedule resolution, family-XP traits and capstones,
advanced family systems, centralized Home effects, legacy replacements, the
real HUD, deterministic playback controls, and the office port.

The current post-snapshot HTML fixes Skip so it resolves the active action and
remaining locked workday without relying on animation timers. Gameplay now
prelocks meeting and Office Chat participants and Outcomes, the daily visitor,
and sabotage identity before presentation; meeting records use canonical
gameplay IDs; sabotage resolves at the fixed midpoint after the daily visit;
and an unexpected resolver error rolls back gameplay state and both RNG streams
before restoring Skip with the prepared resolution for retry. Burnout also
clears the Workday playback lifecycle.

The expanded smoke source compares full gameplay state and gameplay RNG across
1x/2x/4x/Skip, real ambient contention, meeting/chat setup and dialogue, desk
visits, sabotage, stalled wrap-up, double invocation, exceptions before and
after gameplay mutation, opening-event burnout, and a final converted meeting.
Game and smoke JavaScript syntax, repository-diff checks, and focused Node
behavioral checks pass. The updated browser suite was not executed here because
no browser backend is connected, and the Python runner is unavailable. The
dated verification reports still apply to the prior snapshot hash.

The first full bidirectional verification ran on 2026-08-06 and is recorded in
`verification/FULL_VERIFICATION_2026-08-06.md`. The candidate failed ship
signoff. Findings F1-F4 were subsequently fixed and passed the focused retest
in `verification/BLOCKERS_1_4_RETEST_2026-08-06.md`: exact delayed-effect and
economy disclosure, all nine card disclosures, Help glossary coverage, and
behavioral keyboard scrolling now pass.

The smoke harness now uses state-based accessibility waits and passed four
consecutive post-fix runs. The responsive visual matrix found no sampled
viewport overflow or persistent-HUD overlap. All eight targeted high-risk
interaction groups passed
`verification/ADVANCED_INTERACTION_VERIFICATION_2026-08-06.md`. F5 remains
open at a 55.3 percent scripted-skilled win rate.

## Current Implementation Status

- All 50 ordinary family cards are implemented: each family has four Common,
  three Uncommon, two Rare, and one Legendary card.
- The 14 visible family paths, including Closing, and the hidden Brand Strategy
  path are implemented in the candidate. Their exact effects remain defined in
  the ledger.
- `Rebrand Initiative` is a Special card outside the 50-card roster. It is the
  implemented unlock for Brand Strategy.
- Eligible ordinary random slots use Common 70 percent, Uncommon 20 percent,
  Rare 9 percent, and Legendary 1 percent after the 0.2 percent Special check.
  At most one Special can replace a slot in one generated window.
- The implemented base floor curve is
  `110/10, 130/8, 165/7, 210/6, 250/6, 285/6, 300/5`.
- Meeting variance, manager tuning, Weekend casino frequency, Chad's
  ten-upgrade cap, and the retained Chad coefficients are implemented as the
  structural simulation baseline.
- All eight decision gates are represented in the candidate, including the
  legacy Resume replacements, advanced family systems, deterministic playback,
  real HUD, and responsive office.
- `verification/VERIFICATION_CHECKLIST.md` remains the requirement inventory.
  The dated
  full-verification report records item-level Pass, Fail, Not Run, and Blocked
  evidence; unchecked checklist boxes must not be interpreted as passes.

## Family Card Identities

- **Coding - Build, Automate, Integrate:** turn prior work into future value,
  sequence additional cards, and bridge progression between families.
- **Management - Coordinate, Schedule, Amplify:** observe people and actions,
  rearrange or guarantee the schedule, and multiply successful coordination.
- **Design - Observe, Iterate, Transform:** reveal information, refine repeated
  work, and copy or convert existing card effects.
- **Sales - Earn, Spend, Network:** generate purchasing power, convert spending
  into leverage, and monetize relationships.
- **Operations - Reserve, Stabilize, Deliver:** bank resources for later,
  replace unreliable outcomes, and turn successful processes into dependable
  throughput.

## Simulation Status And Priorities

The initial audit completed 3,000 seeded runs without simulation errors:
baseline won 0.7 percent, random won 12.2 percent, and scripted-skilled won
55.3 percent. The skilled heuristic is evidence, not a human-expert model.
`Regression Tests` was selected 2,567 times and is the first targeted
watchpoint, not an automatic balance change.

A later focused policy completed 159 actual Chain 9 Closes and won 62 of those
runs, a 39.0 percent conditional win rate. This remains simulation evidence,
not an approved Closing change. Human Closing playtests are pending.

The advanced suite found no rules defects. Its maximal action fixture did,
however, resolve 121 actions for 2,403 project progress. Treat that as a
serious balance and readability watchpoint alongside the skilled-policy
outlier.

Continue to test all 50 cards against standalone value, family identity,
trait-breakpoint pressure, floor pacing, stress, deadlines, rival pressure,
managers, Homes, economy, and every additional-card or replay rule. Pay
particular attention to:

- repeated Legendary effects through Pilot Approved, Logistics, Rapid
  Prototype, Design System, and other complete-play effects;
- action inflation from War Room, Perfect Execution, Efficiency, Agile,
  Leadership, Deals, and bonus Work sources;
- economy compounding across Sales cards, Negotiation, Compound Interest,
  discounts, financing, and Expense Credit;
- Success Fee's late-run cash spikes and Productivity License plus Contractor
  Support's Work-action burst;
- information overload from schedule, task, and outcome-selection effects;
- early dead cards versus acceptable high-ceiling setup pieces; and
- whether any card is an automatic pick or never worth delaying a trait
  breakpoint.

Treat measured outliers as evidence rather than automatic nerfs. Any balance
change still requires explicit approval and a ledger update.

## Remaining Decisions

No implementation rules gate remains Open, and the eight highest-risk
interaction groups now have deterministic coverage. Balance work next needs to
define the structural simulation matrix and address the 55.3 percent
scripted-skilled result against the 25-35 percent target. Numeric changes still
require explicit approval. UI, accessibility, reset, and lifecycle rows not
exercised by the targeted suite remain Not Run or Blocked as recorded in the
full report.

Home effects are centralized and optional inert set metadata is supported.
Actual Home sets, thresholds, bonuses, prices, and resale tuning remain
deliberately deferred until after implementation verification.

## Product Guardrails

- Preserve one standalone HTML file with no required server or build step.
- Preserve office-friendly AFK playback.
- Keep meaningful choices at morning, night, weekend, and promotion phases.
- Prefer concise card text, forecasts, icons, bars, and tooltips.
- Never describe Draft or Open material as approved or implemented.

## Planning Shorthand

- `<family> review` means a candid preliminary review of that family's complete
  roster against all locked systems and multiplier interactions.
- `qa cleanup` means audit every active OfficeWars planning document and
  generated public copy for stale status, contradictions, legacy mechanics,
  broken references, and synchronization drift. Rewrite, consolidate, move, or
  remove existing sections instead of appending verification notes; preserve
  useful history only in `ARCHIVE_SUPERSEDED.md`.
- `full verification` means reconstruct every requirement from the sources of
  truth, trace it to implementation, UI, and test evidence, and run the full
  static, behavioral, deterministic, browser, accessibility, distribution,
  and simulation checklist. Report Pass, Fail, Not Run, or Blocked for every
  item and never hide unverified scope.

## Public Continuation

New contributors and agents should begin with `README.md`, `AGENTS.md`,
`docs/PROJECT_STATUS.md`, and `docs/WORKING_WITH_AGENTS.md`. Do not infer that a
dated verification result still applies after the game hash changes.
