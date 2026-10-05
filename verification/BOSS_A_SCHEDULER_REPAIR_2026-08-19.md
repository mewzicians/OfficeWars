# Boss A Scheduler-Backlog Repair

Date: 2026-08-19

## Scope

This source-only diagnostic preserves the liked Boss A tune, sustained
undercurrent, smooth paper-brush envelope, form, and mix while repairing an
intermittent playback burst after a delayed browser scheduler tick.

No music was added to `officewarsautobattler.html`.

## Listening Evidence

Human listening still heard an inconsistent pop after the smooth-envelope
repair. The artifact could disappear after manually seeking backward.

That seek-dependent behavior changed the diagnosis from another brush-envelope
problem to playback-state recovery.

## Lifecycle

- Rejected predecessor:
  `OW-MUSIC-BOSS-A-POP-REPAIR`
  - `Music Legacy/officewars-boss-a-pop-repair-audition.html`
- Rejected live-engine control:
  `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`
  - `Music Legacy/officewars-boss-a-scheduler-repair-audition.html`

The predecessor moved through Limbo because its music and envelope repair were
liked while an intermittent playback defect remained. Once the good material
was preserved in the scheduler Test, the predecessor became Rejected.

## Root Cause

The scheduler looks ahead by `180ms`. After a browser or main-thread delay
longer than that horizon, its old catch-up loop scheduled every overdue step.
Every voice independently clamped its late start to approximately
`currentTime + 2ms`, compressing several missed notes and percussion attacks
onto nearly the same instant.

That source burst could sound like a short static pop without creating a
persistent source leak or exceeding the clipping threshold.

Manual seek destroys the old playback state and starts a new scheduler with
`nextTime` safely in the future. This explains why seeking could make the
artifact disappear.

## Repair

The Test preserves the exact smooth-brush audio design and changes only late
scheduler recovery:

1. measure scheduler lateness before each look-ahead pass;
2. when a Test scheduler is overdue, calculate the number of missed steps;
3. advance the musical step and loop position by that count;
4. move `nextTime` to a safe future timestamp; and
5. schedule only current and future steps.

The Rejected control retains the original stack-overdue behavior for a direct
comparison.

The page exposes:

- `Boss A / Stacked Catch-Up`, the Rejected complete control;
- `Control Brush Only`;
- `Boss A / Clean Recovery`, the active Test;
- `Resilient Brush Only`; and
- a `STALL TEST` control that intentionally blocks the main thread for `900ms`.

## Artifacts

- Rejected audition:
  `Music Legacy/officewars-boss-a-scheduler-repair-audition.html`
  - SHA-256:
    `0E1E5570146C8C2B165AE093168E00378D468915E16DCE7E66321120BAABCEC1`
- Focused verifier:
  `.officewars-boss-a-scheduler-repair-verify.py`
  - SHA-256:
    `C916FE6C57A37911D3D05F61AED0ACF982FE09F9E7C5ADEB96A970602C8E50D6`
- Retained visual:
  `.visual-officewars-boss-a-scheduler-repair-audition.png`
  - SHA-256:
    `1155CCB8C4065D696B0A3033A10C561918D594225DB617272B91BA3C1C2686E1`
- Rejected predecessor:
  `Music Legacy/officewars-boss-a-pop-repair-audition.html`
  - SHA-256:
    `7E6656708335EADFDAD0AD8ECC40E5D7426FCF555DFE3CB36B24C49C922C8469`
- Game:
  `officewarsautobattler.html`
  - SHA-256:
    `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`

## Forced-Stall Regression

Both paths began from the same smooth-brush music and received a forced
`900ms` main-thread stall.

| Measurement | Rejected stack control | Resilient Test |
|---|---:|---:|
| Observed scheduler lag | `694.905ms` | `692.238ms` |
| Maximum steps scheduled in one tick | `5` | `1` |
| Skipped overdue steps | `0` | `4` |
| Scheduler recoveries | `0` | `1` |
| Peak tracked sources | `36` | `21` |

After manually seeking the Rejected control, its fresh playback state peaked
at `13` tracked sources. This reproduces the user's observation that seek can
make the artifact disappear.

Three additional forced `520ms` stalls on the Test produced three recoveries
without scheduling more than two steps in one tick.

## Focused Verification

The quick browser gate passed:

- exact predecessor, selected Boss A, and On the Clock protected hashes;
- exact foreground, harmony, roots, undercurrent, form, movement map, brush
  rhythm, noise source, filters, smooth envelope, and output architecture;
- stable internal label `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`;
- lifecycle status `Test`;
- comparison-safe complete mixes;
- all four playback modes audible;
- all movement starts and live accessible highlighting;
- pause, resume, seeking, rapid switching, `100 percent` headroom, responsive
  layouts, and zero-source cleanup;
- forced-stall reproduction; and
- resilient late-step recovery.

Observed average complete-mix levels at `50 percent` page volume:

- Rejected stack control: `0.01301623`
- Resilient Test: `0.0123834`

## Repeated-Loop Verification

All four modes completed at least two uninterrupted loops:

| Mode | Wraps | Peak sources | Scheduler recoveries |
|---|---:|---:|---:|
| Rejected complete control | 2 | 22 | 0 |
| Rejected brush only | 2 | 3 | 0 |
| Resilient complete Test | 2 | 22 | 0 |
| Resilient brush only | 2 | 3 | 0 |

The full verifier reported:

- no clipping;
- no source accumulation;
- stable normal loop resets;
- zero active sources after every stop; and
- no browser errors.

## Decision Boundary

The forced-stall regression proves that this artifact prevents overdue-step
bursts. Human listening nevertheless continued to hear intermittent pops, so
`OW-MUSIC-BOSS-A-SCHEDULER-REPAIR` is Rejected as the active solution and
retained as the exact live-engine control for
`OW-MUSIC-BOSS-A-PRERENDER-REPAIR`.

Complete boss-form approval, production master, adaptive behavior, game
integration, shipping, and final delivery remain open.
