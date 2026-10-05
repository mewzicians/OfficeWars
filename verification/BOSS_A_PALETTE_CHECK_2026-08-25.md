# Boss A Palette Check

Date: 2026-08-25

## Scope

`OW-MUSIC-BOSS-A-PALETTE-CHECK` is `Rejected` at
`Music Legacy/officewars-boss-a-palette-check-audition.html`.

Both anonymous versions preserve exact liked Sketch A from
`Music Legacy/officewars-boss-a-second-movement-sketches.html`, SHA-256
`2441494767E9C39E2D810783D70C798727A48C9E33D6FD942857851D8D45DF63`.

## Measurement

Exact live Sketch A was measured before treatment authoring:

- Full RMS approximately `-15.9 dBFS`;
- sub-120 Hz share approximately `27.1%`;
- `120-500 Hz` share approximately `23%`;
- `500-2000 Hz` melody share approximately `47.0%`; and
- `2000-4000 Hz` presence share approximately `2%`.

The retired baked-render balance did not describe the live source, so no broad
palette redesign was justified.

## Candidate Contract

- A: exact current palette.
- B: exact music with a `-2 dB` shelf below `140 Hz`.
- B comparison trim: `1.05x`, compensating the measured approximately
  `0.42 dB` unmatched loss.
- Held exact: notes, timing, harmony, roots, intensity, groove, percussion,
  roles, length, synthesis voices, controls, and visible labels.
- Monitors: Full, Melodic roles, and Support only.

## Verification

- Generated page SHA-256:
  `56AA959FB2BA616FB86EB441FE14BE0B3148866C6523FB9F0FD2F0B5E32A4DE6`
- Browser verification: `75 passed, 0 failed`.
- Full A/B RMS: approximately `-15.92 / -16.04 dBFS`.
- Full A/B sub share: approximately `27.1% / 21.2%`.
- Full A/B melody-band share: approximately `47.0% / 52.0%`.
- Every candidate and monitor completes two loops without clipping.
- Continuous 60-second playback, transport, switching, bounded sources,
  cleanup, replay, themes, and console checks pass.
- Game and Approved rollback hashes remain unchanged.

Human listening reported no clear difference and said the material sounded
good. A was the unchanged current palette; B was the `-2 dB` low-shelf
treatment. The simpler current palette carries forward into the identity
kernels.
