# OfficeWars Project Status

Snapshot date: 2026-08-06

Implemented game SHA-256:
`41A3CC9823C032C1D80518DB61E0C9289C5CDAADFD9EAE3C16F1E587092A71A0`

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
  portrait rotation gate.
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
- The smoke suite passed four consecutive post-fix runs.
- The sampled responsive matrix found no persistent-HUD overlap or viewport
  overflow.
- The current Skip fix passes game, smoke-wrapper, and evaluated-smoke
  JavaScript syntax; repository-diff checks; and focused Node behavioral checks
  for legacy participant normalization, prepared converted meetings, and Skip
  transactional error recovery.
- The smoke source now compares full gameplay state and gameplay RNG across
  1x/2x/4x/Skip, real ambient contention, meeting/chat setup and dialogue,
  desk visits, sabotage, stalled wrap-up, double invocation, exceptions before
  and after gameplay mutation, opening-event burnout, and a final converted
  meeting. This updated browser suite was not executed in the implementation
  environment because no browser backend is connected; the Python runner is
  also unavailable.
- The current candidate is still not ready for final ship signoff because
  structural balance and several exhaustive UI, accessibility, reset, and
  lifecycle rows remain open.

The dated reports under `verification/` apply to the prior
`2A4880220763678436C6BDFA043EAD7777BB71F01547F8B17B047768206C1D78`
snapshot. See those reports for their exact evidence and limitations.

## Current Balance Evidence

Across the original 1,000 scripted-skilled seeds:

- victories: 553;
- burnouts: 206;
- Chad losses: 183;
- deadline losses: 58;
- scripted-skilled win rate: 55.3 percent against a 25-35 percent target.

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

1. Collect human playtest evidence.
2. Run a structural matrix that holds Floors 1-3 stable while testing Floors
   4-7 project requirements and late Chad pressure.
3. Test all trait paths with policies capable of selecting and using them.
4. Apply only explicitly approved tuning.
5. Re-run full verification before calling the candidate release-ready.

Home item sets remain deferred until the current verification and balance gate
is closed.
