# OfficeWars Project Status

Snapshot date: 2026-08-06

Implemented game SHA-256:
`2A4880220763678436C6BDFA043EAD7777BB71F01547F8B17B047768206C1D78`

## Current Candidate

`officewarsautobattler.html` contains the approved implementation candidate
through rollout Phases 0-6:

- the fixed-rarity 50-card roster;
- family XP, ordinary trait paths, capstones, and advanced family systems;
- shared card, schedule, coworker, Clock Out, and transition resolution;
- centralized Home effects and legacy-system replacements;
- the real HUD, Resume Book, deterministic playback, responsive office, and
  portrait rotation gate.

## Verification

- Findings F1-F4 from the first full audit are fixed.
- All eight targeted high-risk interaction groups pass deterministic fixtures.
- The smoke suite passed four consecutive post-fix runs.
- The sampled responsive matrix found no persistent-HUD overlap or viewport
  overflow.
- The current candidate is still not ready for final ship signoff because
  structural balance and several exhaustive UI, accessibility, reset, and
  lifecycle rows remain open.

See `verification/` for exact evidence and limitations.

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
