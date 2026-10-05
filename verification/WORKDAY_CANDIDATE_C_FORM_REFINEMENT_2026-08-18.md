# Workday Candidate C Form Refinement

Date: 2026-08-18

## Listening Verdict

Human listening found the original `Corner Turn` passage around 49 seconds
uncertain and directionless. The rest of the form was not rejected by this
feedback.

The user also approved the usefulness of the Movement Starts area and
requested that its buttons visibly follow the currently playing phrase.

## Musical Change

The opening half of `Corner Turn` remains unchanged. Its final two bars now
commit to the parent return:

- the F-major bar settles on `F-A-G-F`; and
- the G7 bar descends through `F-D-B-D`;
- the parent then enters stepwise on `E`.

This replaces the original `E-F-G-E / D-E-F-D` ending, which changed
direction repeatedly without establishing a clear cadence.

Candidate C, Ensemble C, the four parent phrases, `112 BPM`, total duration,
and Hybrid B's `0 / 0 / 55% / 100%` motion arc remain unchanged.

## Visibility Change

The eight Movement Starts buttons now:

- highlight the one phrase currently playing;
- update during uninterrupted playback, direct movement starts, seeks, and
  loop returns;
- expose `aria-current="step"` on the active movement; and
- clear the active state when playback stops.

## Final Artifacts

- Audition:
  `Music Legacy/officewars-workday-candidate-c-form-audition.html`
  - SHA-256:
    `2C3BDB5D4A59CE15567014EEE2A82B7077D42CFA59D4451558F00163EC08315D`
- Focused verifier:
  `.officewars-workday-candidate-c-form-verify.py`
  - SHA-256:
    `FB554FAD19CDA020CF9F7816738F87EEDC59DF86E1B75A25548D514CF316CF2D`
- Retained visual:
  `.visual-workday-candidate-c-form-audition.png`
  - SHA-256:
    `8B936EA72F87E7B5284D21038E98B303781B9D2E2ED6AD9F173FC5762F0ACB43`

## Verification

The focused browser verifier passed:

- exact selected Candidate C, Ensemble C, parent, tempo, and motion contracts;
- the revised `Corner Turn` note plan;
- smooth arrival from `Corner Turn` into `Parent Returns`;
- one unique active movement button for every movement;
- correct `aria-current` state and stop cleanup;
- all eight movement starts;
- Full Cue and Melody Only audibility;
- pause, resume, seek, timestamp, and clear controls;
- 60 rapid switches;
- 100-percent headroom;
- desktop, landscape, and portrait layouts;
- two uninterrupted loops of both listening modes;
- bounded source counts;
- no page or console errors; and
- cleanup to zero tracked sources.

## Decision Boundary

The original Corner Turn ending is rejected. The revised ending is
technically verified but remains musically exploratory until human listening.
The complete cue is not selected or shipped.
