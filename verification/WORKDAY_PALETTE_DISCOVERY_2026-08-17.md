# Workday Palette Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday palette audition. It
tests three sound-world and groove treatments while preserving the selected
Sketch B parent melody, harmony, tempo, and four-phrase form.

## Decision Status

**Technically verified, musically exploratory**

The user selected the Workday brief:

- mix comfortable background listening with enough engagement to make watching
  the office enjoyable; and
- prioritize a playful, fun emotional character.

No Workday palette, arrangement, production, or complete cue is selected.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-palette-audition.html`
- Audition SHA-256:
  `A88D75DC6EAB6E7343957D5C148F4598B5CA8A6362350734EB2385B9AE5CE97D`
- Verifier:
  `.officewars-workday-palette-verify.py`
- Verifier SHA-256:
  `3C17D492A833949DE4D0050ADACB6078C3501972265E617535EF6FAAFA6A6E46`
- Desktop capture:
  `.visual-workday-palette-audition.png`
- Capture SHA-256:
  `4CAD4F1A385C76C400A931F183B16B7D5D1D54188ABE6263C5E26D6AD2F06B2A`

## Controlled Musical Contract

All three samples preserve:

- the exact selected 128-step Sketch B foreground;
- all four selected phrases and their note timing;
- the selected chord plan and bass roots;
- 104 BPM;
- an approximately 36.92-second loop; and
- the Establish, Answer, Develop, and Return phrase functions.

The coordinated exploratory treatments are:

1. a rounded digital-pop treatment with sustained harmony, smooth bass, and a
   restrained buoyant pulse;
2. a soft pixel-lounge treatment with filtered square and triangle
   articulation, gentle chord arpeggiation, and sparse accents; and
3. a restrained office-funk treatment with short chord responses, syncopated
   bass motion, tighter drums, and a quiet sustained harmonic thread.

The audition labels these anonymously as Workday A, B, and C.

## Browser Evidence

The focused Playwright runner passes:

- page parsing with no page or console errors;
- exact melodic, harmonic, tempo, form, and loop equality across all samples;
- strictly increasing automation envelopes;
- audible and unclipped playback at 50-percent page volume;
- comparison-safe average signals of `0.042344`, `0.040670`, and `0.031966`;
- maximum sampled 50-percent peaks of `0.186145`, `0.137956`, and `0.155249`;
- retained 100-percent headroom with a maximum sampled peak of `0.284458`;
- pause, resume, seeking, timestamp marking, and timestamp clearing;
- 48 rapid sample switches without scheduler or source accumulation;
- 77 seconds and two complete uninterrupted wraps for every sample;
- peak live-source counts of `24`, `12`, and `20`;
- stop cleanup to zero tracked sources;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls; and
- visual inspection of the desktop capture.

## Not Run

- Human comparative listening verdict.
- Long-exposure fatigue testing beyond two loops.
- Final Workday form, arrangement development, production, or game
  integration.
- UI-sound and gameplay-sound masking tests inside the shipped game.
