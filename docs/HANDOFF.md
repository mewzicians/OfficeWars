# OfficeWars Current Handoff

Last updated: 2026-08-07

## Read First

1. `AGENTS.md`
2. `docs/GAME_DESIGN.md`
3. `docs/BALANCE_LEDGER.md`
4. `docs/PROJECT_STATUS.md`
5. This file
6. `docs/PATCH_NOTES_SKIP_FIX_2026-08-06.md`
7. `verification/PERSISTENCE_TUTORIAL_2026-08-07.md`
8. `verification/PROJECT_HUD_CONSOLIDATION_2026-08-07.md`
9. `verification/WORKDAY_TICKER_SYNC_2026-08-07.md`
10. `docs/PATCH_NOTES_RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md`
11. `verification/RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md`
12. `verification/FULL_VERIFICATION_2026-08-07_30214B7F.md`

Read `docs/ARCHIVE_SUPERSEDED.md` only when historical reasoning is needed.

## Sources Of Truth

- `officewarsautobattler.html` is the implemented game.
- `docs/GAME_DESIGN.md` is the stable product model.
- `docs/BALANCE_LEDGER.md` contains active Implemented, Locked, Draft, and Open
  decisions.
- `docs/PROJECT_STATUS.md` records the current candidate and balance evidence.
- `officewars-ui-prototype.html` is a visual reference, not gameplay truth.

## Implementation Status

`officewarsautobattler.html` now contains the complete approved overhaul
candidate through rollout Phase 6: core balance, the fixed-rarity 50-card
roster, shared card and schedule resolution, family-XP traits and capstones,
advanced family systems, centralized Home effects, legacy replacements, the
real HUD, deterministic cycling playback controls, the office port, versioned
active-run persistence, and the contextual first-day orientation.

The current HTML includes the deterministic Skip repair described in
`docs/PATCH_NOTES_SKIP_FIX_2026-08-06.md`. It prelocks meeting and Office Chat
participants and outcomes, the daily visitor, and sabotage; stores canonical
gameplay IDs; resolves sabotage immediately after the midpoint desk visit; and
rolls back gameplay state and both random streams if Skip resolution throws.

The current HTML has SHA-256
`30214B7FFF8FB4ED44690B90B64EE991E8F300ACE1A4E66E9100BBDAFCC81D12`.
It replaces the three speed buttons with one cycling 1x/2x/4x button and makes
the new 1x equal to the previous 2x presentation pace. It also replaces
Endless with Continue Run, autosaves committed state, restores prepared
Workdays deterministically to Clock Out, preserves casino games and run
results, and teaches the basic loop through six contextual callouts. The
player's project progress now fills behind the top-center project title under
a fixed readability scrim, shows the exact fraction, and pulses on change. The
bottom-left player HUD now contains only the portrait and Stress bar. Workday
action results now clear when the next action starts and update in the same
settlement step as the HUD, rather than remaining one action behind.

Relationship tooltips now show only each coworker's actual bonus, and the
Outings footer explains that coworkers grant bonuses when met during the
Workday. Manual Lights Out and Home or Deal purchases now exclude one another
in both directions; Outings stay independent, and Moodboard's automatic Lights
Out remains the explicit exception. Active Brand Strategy mornings use a
four-part Campaign status band showing the Campaign name, requested task and
family, completed steps, and Campaigns completed. `Rebrand Initiative` now
explains Campaign replacement, ordered completion, and its reward promise.

The current hash passes the smoke, persistence, advanced, and 17-case visual
suites. Persistence and orientation evidence is recorded in
`verification/PERSISTENCE_TUTORIAL_2026-08-07.md`; the speed-control snapshot
remains recorded in `verification/PLAYBACK_SPEED_CONTROL_2026-08-07.md`; and
the current relationship, Night, and Campaign evidence is recorded in
`verification/RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md`.

The current full verification is recorded in
`verification/FULL_VERIFICATION_2026-08-07_30214B7F.md`. It finds one
implementation-verification failure: the headless Night policy buys a Home
item and then unconditionally grants itself manual Lights Out, despite the
player UI correctly enforcing mutual exclusion. This makes current balance
simulation Blocked until that policy is repaired and rerun. The earlier 58.4
percent scripted-skilled result is historical snapshot telemetry, not valid
current balance evidence.

Exhaustive screen-reader, every-picker, every-boundary save/restore, reset,
rapid-input, and memory-profile rows remain explicitly Not Run or Blocked; do
not imply that the focused suites close those broader rows.

## Implemented Scope

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
- One active run persists in browser storage. Continue Run, replacement-run
  confirmation, deterministic prepared-Workday restore, casino continuation,
  persistent results, return to menu, tutorial completion, skip, and replay
  are implemented.
- The verification checklist remains the requirement inventory. The dated
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

The current headless Night policy is not rules-faithful. After making automated
Home or Deal purchases, it sets `nightState.recPicked=true` and receives manual
Lights Out recovery without the Moodboard exception. Do not use a simulation
run from this policy as current balance evidence.

The prior exact-snapshot audit completed 3,000 seeded runs without runtime
errors: baseline won 0.7 percent, random won 12.2 percent, and
scripted-skilled won 58.4 percent. `Regression Tests` was the policy's largest
selection outlier. Preserve those numbers only as historical telemetry until a
rules-faithful rerun replaces them.

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

## Remaining Work

Run persistence and first-day onboarding are implemented. Focused restoration
coverage passes, including pending Slots, Blackjack, and Poker. Exhaustive
every-picker and every-transition restoration remains part of the broader
unverified matrix rather than an implementation blocker discovered in this
pass.

Repair the headless Night policy before running or interpreting another balance
matrix. Then test the structural curve and all trait paths against the 25-35
percent skilled target. Numeric changes require explicit approval. Unverified
rows retain their exact status in the current full report.

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
  portable copy for stale status, contradictions, legacy mechanics, broken
  references, and synchronization drift. Rewrite, consolidate, move, or remove
  existing sections instead of appending verification notes; preserve useful
  history only in `ARCHIVE_SUPERSEDED.md`.
- `full verification` means reconstruct every requirement from the sources of
  truth, trace it to implementation, UI, and test evidence, and run the full
  static, behavioral, deterministic, browser, accessibility, distribution,
  and simulation checklist. Report Pass, Fail, Not Run, or Blocked for every
  item and never hide unverified scope.

## Portable Handoff

`officewars-rollout-handoff-2026-07-31/` is the current portable package.
`officewars-public-repo-2026-08-07/` is the source workspace's public
repository package; its contents become the repository root when exported.
Both packages' mapped game, guidance, active documents, verifiers, reports, and
hashes were synchronized with the root candidate on 2026-08-07.
