# Workday Candidate C Passage D Form Verification

Date: 2026-08-18

## Scope

This source-only audition integrates the selected Passage D detour treatment
into the existing exploratory Candidate C Workday form. It does not approve
the complete cue, production, gameplay integration, or shipping.

## Protected Contracts

- The complete form remains `256` eighth-note steps at `112 BPM`, or
  approximately `68.571` seconds.
- Candidate C's exact selected notes, chords, and bass roots remain at steps
  `64` through `127`.
- The four parent phrases, two C-derived development phrases, revised
  `Corner Turn`, eight movement starts, Ensemble C, and Hybrid B's
  `0 / 0 / 55% / 100%` motion arc remain unchanged.
- Passage D maps its exact phrase-role treatment into the full form:
  - connected lead steps:
    `66, 71, 74, 82, 87, 92, 95, 98, 103, 108, 114, 119, 124, 127`;
  - crisp articulation at every other Candidate C note; and
  - the exact restrained G7-to-C6 organ handoff at step `95`.

## Artifacts

- Audition:
  `Music Locked/officewars-workday-candidate-c-passage-d-form-audition.html`
- Audition SHA-256:
  `0166B13C35F03FC19E8AE614337BDAA200D2A5AB2CF38B36D3671608BEC3C108`
- Verifier:
  `.officewars-workday-candidate-c-passage-d-form-verify.py`
- Verifier SHA-256:
  `A2C424EB291CFB99618121DDE4CE6A0AAD415E0420A0888121FAE3B4F6DB62AA`
- Retained visual:
  `.visual-workday-candidate-c-passage-d-form-audition.png`
- Visual SHA-256:
  `FFD0CF9ABA98DDC415C00E250B530F4DEFEE041E0F572A3653499BB9F9F422BB`

## Verification

The focused verifier passed:

- exact equality with the prior full-form notes, harmony, roots, movement
  map, development, parent phrases, duration, and motion arc;
- exact equality with Passage D's selected connected-lead and organ-handoff
  plans;
- all eight direct movement starts and live `aria-current` highlighting;
- audible Full Cue, Melody Only, and detour-handoff playback at the default
  `50%` volume;
- pause, resume, seeking, timestamp marking, and clearing;
- `100%` headroom without clipping;
- `60` rapid track and movement switches without source growth;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls;
- two uninterrupted loops of Full Cue and Melody Only;
- bounded active and peak source counts; and
- zero-source cleanup after stop.

## Decision Status

Technically verified, musically exploratory.

Passage D remains selected as the detour performance foundation. The complete
form, `Thread Returns`, revised `Corner Turn`, duration, production, gameplay
masking, game integration, and shipping remain open pending human listening.
