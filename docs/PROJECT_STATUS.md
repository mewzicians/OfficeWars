# OfficeWars Project Status

Snapshot date: 2026-08-07

Implemented game SHA-256:
`30214B7FFF8FB4ED44690B90B64EE991E8F300ACE1A4E66E9100BBDAFCC81D12`

Skip repair details and validation scope are recorded in
`docs/PATCH_NOTES_SKIP_FIX_2026-08-06.md`.

## Current Candidate

`officewarsautobattler.html` contains the approved implementation candidate
through rollout Phases 0-6:

- the fixed-rarity 50-card roster;
- family XP, ordinary trait paths, capstones, and advanced family systems;
- shared card, schedule, coworker, Clock Out, and transition resolution;
- centralized Home effects and legacy-system replacements;
- the real HUD, Resume Book, deterministic playback, responsive office, and
  portrait rotation gate;
- a consolidated player project HUD with the progress fill behind the
  top-center project title, a fixed readability scrim, exact progress, and a
  brief change pulse; the bottom-left player HUD is portrait plus Stress only;
- Workday ticker outcomes clear at the start of each action and update when
  that action settles, in sync with the persistent HUD;
- one cycling 1x/2x/4x playback button, with the new 1x using the previous 2x
  presentation pace;
- one versioned active-run save with Continue Run, replacement confirmation,
  deterministic prepared-Workday restore, casino continuation, persistent
  results, and return to menu;
- a six-step contextual first-day orientation with spotlighted existing UI,
  Skip Orientation, persisted progress, and replay through How to Play;
- the readability overhaul for Morning cards, Resume, resolved Workday
  feedback, Clock Out grouping, and the Night decision surface; and
- concise relationship bonuses plus a Workday-bonus explanation in Outings;
- a two-way lock between manual Lights Out and Home or Deal purchases, with
  Outings independent and automatic Moodboard Lights Out exempt;
- a dedicated active-Campaign status band and clearer `Rebrand Initiative`
  description; and
- Skip now resolves the active action and remaining locked schedule directly,
  bypassing presentation-only walking and conversation waits while preserving
  action, desk-visit, sabotage, and Clock Out resolution. Meeting and Office
  Chat participants and Outcomes, the daily visitor, and the saboteur are
  prelocked; participant records use canonical gameplay IDs; and an unexpected
  resolver error rolls back gameplay state and both RNG streams before
  restoring Skip for a deterministic retry.

## Verification

- Findings F1-F4 from the first full audit are fixed.
- All eight targeted high-risk interaction groups pass deterministic fixtures.
- On the preceding broad-verification hash, the final smoke suite passed four
  consecutive runs.
- The 17-case readability matrix found no sampled clipped text,
  persistent-HUD overlap, or viewport overflow.
- The current candidate hash passes smoke, persistence, the focused automated
  player-surface audit, all eight advanced interaction groups, and the
  refreshed 17-case visual matrix. Evidence is recorded in
  `../verification/RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md`.
- The current Skip fix passes game, smoke-wrapper, and evaluated-smoke
  JavaScript syntax; repository-diff checks; and focused Node behavioral checks
  for legacy participant normalization, prepared converted meetings, and Skip
  transactional error recovery.
- The smoke source compares full gameplay state and gameplay RNG across
  1x/2x/4x/Skip, real ambient contention, meeting/chat setup and dialogue,
  desk visits, sabotage, stalled wrap-up, double invocation, exceptions before
  and after gameplay mutation, opening-event burnout, and a final converted
  meeting. It passed again on the current speed-control hash.
- The current hash passed the advanced interaction suite, full automated
  runtime audit, sampled accessibility checks, and expanded visual inspection
  without page errors, console errors, or external requests. The focused
  persistence suite passed 23 checks, including deterministic Workday restore,
  pending Slots settlement exactly once, active Blackjack and Poker restore,
  and all orientation transitions. Current-hash evidence is in
  `../verification/PERSISTENCE_TUTORIAL_2026-08-07.md`.
- `../verification/FULL_VERIFICATION_2026-08-07_30214B7F.md` is the current
  exhaustive verdict. It passes player-facing implementation, deterministic
  playback, persistence, responsive UI, and distribution, but fails the
  headless Night policy's rules parity. Exhaustive every-picker,
  assistive-technology, save/restore, reset, rapid-input, and memory-profile
  rows remain explicitly Not Run or Blocked.

Older dated reports remain exact-snapshot historical evidence. Use
`RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md` for the current-hash rerun,
`WORKDAY_TICKER_SYNC_2026-08-07.md` for the preceding ticker snapshot,
`PROJECT_HUD_CONSOLIDATION_2026-08-07.md` for the preceding HUD snapshot,
`PERSISTENCE_TUTORIAL_2026-08-07.md` for detailed continuity evidence, and
`FULL_VERIFICATION_2026-08-07_30214B7F.md` for the current Pass, Fail, Not Run,
and Blocked matrix. `FULL_VERIFICATION_2026-08-07.md` remains historical
evidence for its named preceding hash.

## Historical Balance Evidence

Across the last 1,000 scripted-skilled seeds before the two-way Night rule:

- victories: 584;
- burnouts: 179;
- Chad losses: 177;
- deadline losses: 60;
- scripted-skilled win rate: 58.4 percent against a 25-35 percent target.

The prior hash produced 55.3 percent skilled wins on the same seeds. The Skip
repair changes no numeric balance constants, but prelocking gameplay changes
RNG consumption and therefore cross-version run trajectories. `Regression
Tests` selections increased from 2,567 to 3,160.

These results are not valid current balance evidence. The headless policy
currently purchases a Home item and then also grants itself manual Lights Out,
which the player cannot do. The policy must be repaired and the fixed seed
matrix rerun before drawing current win-rate or Closing conclusions.

The difficulty curve is misshapen rather than uniformly low. Floor 3 is the
largest competitive wall, while successful builds accelerate sharply after
Floor 4.

The strongest sampled trait cores used Eye for Detail with Agile, often adding
Clean Code or Efficiency. Closing was the weakest sampled path, primarily
losing tempo to Chad rather than burning out.

A policy forced to pursue actual Chain 9 completed 159 Chain 9 Closes and won
62 of those runs, a 39.0 percent conditional win rate. This is evidence that
high-chain Closing may not deliver its intended heavily favored payoff.

## Pending Human Evidence

No balance change has been approved from these simulations. The project owner
is testing Closing with human players before deciding whether to change its
rewards, cycle tempo, or chain thresholds.

Record human results using `docs/PLAYTEST_GUIDE.md`.

## Next Engineering Gate

1. Make the headless Night policy obey the Locked purchase-versus-Lights-Out
   rule and add its regression assertion to the full verifier.
2. Collect human playtest evidence.
3. Run a structural matrix that holds Floors 1-3 stable while testing Floors
   4-7 project requirements and late Chad pressure.
4. Test all trait paths with policies capable of selecting and using them.
5. Apply only explicitly approved tuning.
6. Close or explicitly accept the current full report's Not Run and Blocked
   rows, then rerun verification after approved tuning.

Home item sets remain deferred until the current verification and balance gate
is closed.
