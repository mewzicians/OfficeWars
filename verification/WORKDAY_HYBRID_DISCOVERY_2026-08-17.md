# Workday Hybrid Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday hybrid audition. It
preserves the preferred `112 BPM` office-funk treatment and compares two
phrase-level uses of Revision A's extra groove vocabulary.

## Decision Status

**Workday development foundation selected**

The user preferred Hybrid B. This selects the following phrase-motion arc:

- no added Revision A motion in Establish;
- no added Revision A motion in Answer;
- `55 percent` added motion in Develop; and
- full added motion in Return.

The exact `112 BPM` control and Return-only Hybrid A remain historical
comparison references. This selection does not approve a complete
arrangement, production master, or shipped Workday cue.

## Artifacts

- Audition:
  `Music Locked/officewars-workday-hybrid-audition.html`
- Audition SHA-256:
  `7F777F7F20B455EFE170CEF983704B409F71DF98AFD82DE22FE1E02983762E67`
- Verifier:
  `.officewars-workday-hybrid-verify.py`
- Verifier SHA-256:
  `EEDA373297ECB1BCBB79C313587E15F921FFFC6A4A49A82F34067C9C30E7DAC7`
- Desktop capture:
  `.visual-workday-hybrid-audition.png`
- Capture SHA-256:
  `F14D1CCB424DB8793A2233DEEBF3C6CDD78DBD3C8D49350A446F359845D3056B`

## Controlled Musical Contract

All three samples preserve:

- the selected Sketch B foreground and all four phrase timings;
- the selected chord plan and bass roots;
- the restrained office-funk instrument and effects model;
- `112 BPM`;
- a 128-step, approximately `34.29-second` loop; and
- Establish, Answer, Develop, and Return phrase functions.

The exact control contains no added motion. Hybrid A adds the Revision A
motion at full strength only in Return. Hybrid B adds it at `55 percent`
strength in Develop and full strength in Return.

## Browser Evidence

The focused Playwright runner passes:

- page parsing with no page or console errors;
- exact melodic, harmonic, tempo, form, and opening equality;
- exact phrase-level motion plans of `0/0/0/0`, `0/0/0/1`, and
  `0/0/0.55/1`;
- comparison-safe average signals of `0.035214`, `0.035869`, and `0.032118`;
- maximum sampled 50-percent peaks of `0.150544`, `0.189082`, and `0.156505`;
- retained 100-percent headroom with a maximum sampled peak of `0.260138`;
- pause, resume, seeking, timestamp marking, and timestamp clearing;
- 48 rapid sample switches without scheduler or source accumulation;
- 77 seconds and two complete uninterrupted wraps for every sample;
- peak live-source counts no higher than `20`;
- stop cleanup to zero tracked sources;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls; and
- visual inspection of the desktop capture.

## Not Run

- Long-exposure fatigue testing beyond two loops.
- Final Workday form, arrangement, production, or game integration.
- UI-sound and gameplay-sound masking tests inside the shipped game.
