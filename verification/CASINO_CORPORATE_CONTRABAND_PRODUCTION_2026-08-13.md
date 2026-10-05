# Casino Corporate Contraband Production Verification

Date: 2026-08-13

## Scope

This source-only pass builds and verifies one authored production candidate
for the selected Festival Contour composition. It does not change
`officewarsautobattler.html`, shipped gameplay, balance, or game audio.

## Decision Status

**Selected ordinary-Casino production**

The user called `Corporate Contraband` Production Pass 06 perfect, selecting
it as the ordinary-Casino production. The comparison preserves the complete
locked composition:

- 164 BPM;
- 192 steps, 24 bars, and approximately 35.12 seconds;
- four six-bar movements;
- the exact foreground-note plan;
- 30-attack Chase Breathing with no reply voice;
- cleaned late False Confidence and Compulsive Return;
- the coordinated macro contour;
- the continuous loop seam; and
- the final `D -> E` return.

The candidate changes only instrument cast, spatial treatment, sound design,
and mix behavior. Entrance, Redline, event stingers, bust and cash-out
behavior, long-term loop variation, and game integration remain open.

## Audition Surface

**Pass**

The focused page provides:

- one preserved Festival Contour production control;
- one Corporate Contraband candidate;
- complete-loop playback and four matched direct starts for each version;
- pause, stop, volume, seeking, and issue timestamps;
- post-listen isolation for full mix, drums and bass, motif lead, and space
  and texture; and
- production notes hidden until the listener chooses to open them.

The desktop capture was visually inspected. The A/B hierarchy, direct starts,
Layer Inspector, and playback state are clear and do not compete with the
listening question.

## Focused Verification

**Pass**

The Playwright runner verified:

- exact note, attack-count, treatment, contour, movement, seam, and final-return
  identity between the control and candidate;
- distinct `reference` and `corporateContraband` production treatments;
- audible, unclipped starts for all four movements on both versions;
- closely level-matched full-mix signal at 50-percent master volume;
- a usable average and peak signal floor for every candidate movement at
  50-percent master volume;
- retained headroom at 100-percent master volume;
- audible, unclipped rhythm, lead, and space isolation;
- natural Answer Chase-to-False Confidence traversal;
- the Compulsive Return-to-Hook Payoff loop seam;
- pause, resume, and seeking into Compulsive Return;
- 40 rapid A/B switches;
- 75 seconds of uninterrupted candidate playback with two complete wraps;
- no active-source accumulation and cleanup to zero tracked sources;
- no page or console errors; and
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls.

An initial portrait failure exposed a CSS-specificity issue that kept the A/B
cards in two columns at 390 pixels. The mobile media rule now explicitly
overrides the comparison grid, and the complete verifier passes.

## Loudness Repairs

**Pass**

The first verified production pass was technically non-zero but failed the
real listening context: Corporate Contraband remained much quieter than the
reference and difficult to hear even with system and audition volume at
100 percent.

The root cause combined three stages:

- synth voices retained low prototype-analysis levels;
- Corporate Contraband applied an additional `0.58` bus trim; and
- the nonlinear master curve yields approximately `0.261` gain at a
  50-percent slider setting.

Production Pass 02:

- raises the Corporate Contraband bus to `1.05`;
- adds a `12x` calibrated makeup stage before the existing dynamics
  compressor;
- defaults this page to a new versioned 50-percent volume profile so the old
  saved 100-percent setting is not reused after the gain increase; and
- replaces the old near-silence threshold with explicit 50-percent movement,
  A/B level-match, and 100-percent headroom assertions.

Pass 02 level-matched the A/B, but the user's real 50-percent system and
50-percent page test remained very quiet. The numerical floor had not exposed
that the page's nonlinear curve still reduced 50 percent to `0.261` gain.

Production Pass 03:

- makes 50-percent page volume unity gain;
- limits 100 percent to `1.35`, approximately `+2.6 dB` above the reference
  level;
- protects the stronger signal with a fast `-8 dB`, `20:1` peak limiter;
- resets saved volume through a versioned `v3` key; and
- raises the 50-percent movement requirements to average above `0.075` and
  sampled peaks above `0.18`.

In the Pass 03 run at 50 percent, the four candidate movements measured
average levels from `0.0865` to `0.1369` and sampled peaks from `0.4446` to
`0.6329`. The full-mix candidate averaged `0.1324` against the reference's
`0.1291`. At 100 percent, the candidate averaged `0.1689` and its maximum
sampled peak was `0.7633`, below the `0.95` headroom ceiling.

Production Pass 04:

- lowers the shared pre-compressor makeup from `12x` to `10.5x`, approximately
  `1.16 dB`, after the user found the stronger direction correct but requested
  a small reduction;
- preserves the exact A/B relationship, composition, production identities,
  50-percent unity curve, `1.35` maximum gain, limiter, and versioned `v3`
  saved profile; and
- adjusts only the movement-average regression floor from `0.075` to `0.065`.
  Every peak, level-match, headroom, lifecycle, and layout assertion remains
  unchanged.

Across two final Pass 04 runs at 50 percent, candidate movement averages
ranged from `0.080505` to `0.109860`. The candidate full mix averaged
`0.124093` to `0.128349` against the reference's `0.124824` to `0.126364`.
At 100 percent, the candidate average ranged from `0.148328` to `0.162715`
and its maximum sampled peaks ranged from `0.751600` to `0.788090`, below the
`0.95` headroom ceiling.

Production Pass 05:

- lowers the shared pre-compressor makeup from `10.5x` to `9.75x`,
  approximately `0.64 dB`, after the user found Pass 04 still slightly loud;
- repairs a static-prone shared envelope schedule in which short voices could
  place their decay target after release and finish;
- clamps attack, decay, release, and finish into strictly increasing times;
- lowers the residual source and bus stop floor from `0.0001` to `0.00001`;
- adds focused regression cases for 55, 80, 110, and 800 millisecond voices;
  and
- moves the 50-percent movement-average floor proportionally from `0.065` to
  `0.060`. Every peak, level-match, headroom, layer, lifecycle, and layout
  assertion remains unchanged.

The reported static was intermittent and was not timestamp-reproduced. The
invalid envelope ordering was directly established from the scheduling math,
removed, and regression-tested. Human listening remains required to confirm
that it was the complete audible cause.

In the final Pass 05 run at 50 percent, candidate movement averages ranged
from `0.073434` to `0.117623`. The candidate full mix averaged `0.106821`
against the reference's `0.105725`. At 100 percent, the candidate averaged
`0.124058` and its maximum sampled peak was `0.746020`, below the `0.95`
headroom ceiling.

Production Pass 06:

- implements the user-approved target equal to twice Pass 02's documented
  50-percent signal path;
- derives Pass 02's effective pre-compressor gain as
  `12 * 0.261 = 3.132`;
- sets shared makeup to exactly `6.264x`, approximately `3.84 dB` below
  Pass 05;
- preserves the A/B relationship, composition, production identities,
  50-percent unity curve, `1.35` maximum gain, limiter, versioned `v3` profile,
  lower stop floor, and monotonic-envelope repair;
- scales the candidate's 50-percent movement floors proportionally to `0.038`
  average and `0.115` sampled peak; and
- sets the 100-percent average floor to `0.060`. Every clipping, level-match,
  headroom, layer, envelope, lifecycle, and layout assertion remains.

In the final Pass 06 run at 50 percent, candidate movement averages ranged
from `0.043565` to `0.104819`. The candidate full mix averaged `0.073415`
against the reference's `0.069196`. At 100 percent, the candidate averaged
`0.094335` and its maximum sampled peak was `0.729810`, below the `0.95`
headroom ceiling.

## Not Run

- Game integration or in-game transition behavior.
- Quickening Lift entrance, Redline, stingers, bust, or cash-out behavior.
- Long-term variation beyond the locked 35.12-second loop.

## Hashes

- `Music Locked/officewars-casino-production-audition.html`:
  `194A07E3A6D1088B46ACBF82BAC210B37C792FBD8194AF44720E754015ED329D`
  (as of this record; repinned to `07074232` by the 2026-08-27 settle repair, which changed no music)
- `.officewars-casino-production-verify.py`:
  `7C863601ADD6548DB3F7F4166B313EDAB27ED1A592101BA83ADD23D3CFB5763D`
- Desktop evidence capture:
  `87274B27D043FE93276FBEE15DB63B31D90E9272A307CF547D84A5CA02C5CF8C`
- Preserved Festival Contour reference:
  `18C856D20E30D399905F72327A739E224670CA448968B73007DD625C71EE5798`
- Preserved Festival Contour verifier:
  `CB1A3D4FC91B353D38BE549DD3ED028DDA27125A28557245C66530DA729A67D3`
- Shipped game, unchanged:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`
