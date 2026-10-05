# Boss A Pre-Rendered Playback Repair

Date: 2026-08-19

## Scope

This source-only diagnostic preserves the liked Boss A resilient-scheduler
mix while testing whether intermittent popping comes from continuous live
voice scheduling, oscillator starts, effect-node allocation, or
garbage-collection pressure.

No music was added to `officewarsautobattler.html`.

## Listening Evidence

Human listening continued to hear intermittent pops after two independently
valid repairs:

1. replacing an abrupt paper-brush gain step with a continuous decay; and
2. preventing delayed scheduler ticks from stacking overdue notes.

The scheduler repair is therefore Rejected as the active solution even though
its forced-stall regression remains valid.

## Lifecycle

- Rejected exact live-engine control:
  `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`
  - `Music Legacy/officewars-boss-a-scheduler-repair-audition.html`
- Active Test:
  `OW-MUSIC-BOSS-A-PRERENDER-REPAIR`
  - `prototypes/officewars-boss-a-prerender-repair-audition.html`

The Test keeps the tune, foreground, harmony, bass, sustained undercurrent,
smooth brush, form, movement timing, and mix. It changes only playback
architecture.

## Technical Hypothesis

Peak simultaneous live sources remained bounded, but the complete cue still
created and destroyed thousands of Web Audio nodes over time. Intermittent
allocation, garbage collection, scheduler timing, oscillator startup, or
effect-tail work could create an output crackle without producing clipping or
a persistent node leak.

This is a hypothesis, not a proven root cause. The pre-render Test removes that
entire variable class so human playback can resolve it.

## Repair

The Test uses one deterministic steady-state loop:

1. render the preceding cycle's final `24` steps as a `4.285714-second`
   preroll;
2. render one complete `91.4286-second` cycle at `24kHz`;
3. extract the steady-state cycle after the preroll;
4. export and bundle that exact stereo WAV locally;
5. decode the asset once; and
6. play it through one looping `AudioBufferSourceNode`.

The local data script avoids `file://` fetch restrictions and reduces
preparation from approximately `108` seconds to approximately `256-288ms`.

An earlier two-cycle `48kHz` runtime render exceeded five minutes and was
rejected as impractical. That was a preparation-design failure, not a musical
or playback defect.

## Artifacts

- Active Test:
  `prototypes/officewars-boss-a-prerender-repair-audition.html`
  - SHA-256:
    `8E1A8B13885D8EB55B2F8E1BBB00CADEA563490B77C937D42C4317A319736E2A`
- Focused verifier:
  `.officewars-boss-a-prerender-repair-verify.py`
  - SHA-256:
    `89FC1D07EAB892B1194B1A7B802F4F980348325C325472FC8EC5CB2130AF2D35`
- Retained visual:
  `.visual-officewars-boss-a-prerender-repair-audition.png`
  - SHA-256:
    `DCEB1BB3710883912CD35143099BD7326139BF21B338CB3090B9937C930FA992`
- Stable stereo WAV:
  `prototypes/officewars-boss-a-stable-render.wav`
  - SHA-256:
    `5458A54815D16E5ABD96460CE758D4D87814B0EC36D857F6BD45269A5461299F`
- Bundled local data:
  `prototypes/officewars-boss-a-stable-render-data.js`
  - SHA-256:
    `FEB70282D0158A9E232AC9A359C60AD3EE3B76348E94AF6EA710B31D64B57FA0`
- Rejected live control:
  `Music Legacy/officewars-boss-a-scheduler-repair-audition.html`
  - SHA-256:
    `0E1E5570146C8C2B165AE093168E00378D468915E16DCE7E66321120BAABCEC1`
- Rejected-control verifier:
  `.officewars-boss-a-scheduler-repair-verify.py`
  - SHA-256:
    `C916FE6C57A37911D3D05F61AED0ACF982FE09F9E7C5ADEB96A970602C8E50D6`
- Game:
  `officewarsautobattler.html`
  - SHA-256:
    `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`

## Render Metrics

- channels: `2`
- decoded sample rate: `48kHz`
- decoded frames: `4,388,572`
- decoded duration: `91.428583s`
- peak: `0.180397`
- RMS: `0.004801`
- measured loop-seam delta: `0.000056`
- runtime Test sources: `1`
- runtime Test scheduler: none

## Focused Verification

The quick browser gate passed:

- exact protected Boss A and On the Clock sources;
- exact live-control music and mix;
- stable internal label `OW-MUSIC-BOSS-A-PRERENDER-REPAIR`;
- lifecycle status `Test`;
- bundled-asset identity and render metadata;
- comparison-safe complete mixes;
- one-source Test runtime;
- no Test scheduler or recovery path;
- pause, resume, seek, movement starts, rapid switching, forced stalls,
  maximum volume, responsive layouts, and zero-source cleanup; and
- no game integration.

Observed average complete-mix levels at `50 percent` page volume:

- live control: approximately `0.01351`
- pre-rendered Test: approximately `0.01298`

## Repeated-Loop Verification

| Mode | Wraps | Peak runtime sources |
|---|---:|---:|
| Exact live control | 2 | 22 |
| Pre-rendered Test | 2 | 1 |

The complete verifier reported:

- no clipping;
- no source accumulation;
- stable loop resets;
- no Test scheduler activity;
- zero active sources after every stop; and
- no browser errors.

## Decision Boundary

`OW-MUSIC-BOSS-A-PRERENDER-REPAIR` remains `Test`. Technical verification
proves that it removes the live playback variable class while preserving the
liked rendered mix. Only human listening on the affected playback system can
confirm whether the intermittent pop is gone.

Complete boss-form approval, production master, adaptive behavior, game
integration, shipping, and final delivery remain open.
