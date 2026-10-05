# Workday Detour Flow Discovery

Date: 2026-08-18

## Listening Question

Human listening found that `Detour Opens` and `Detour Deepens` did not flow
internally or transition into one another as naturally as intended.

The focused question is:

> Can Candidate C feel like one continuous sentence without changing its
> selected pitches, harmony, ensemble, tempo, or surrounding context?

## Controlled Material

Every treatment uses the same `96-step`, approximately `25.714-second` clip:

1. the final `16` steps of `Desk Banter`;
2. the exact `64-step` selected Candidate C middle; and
3. the opening `16` steps of `Thread Returns`.

The following remain exact across all six listening modes:

- Candidate C's selected pitches, chords, and bass roots;
- Ensemble C;
- `112 BPM`;
- the surrounding form material;
- the selected Hybrid B motion identity; and
- the Web Audio graph and playback architecture.

## Anonymous Treatments

- Passage A preserves the current articulation and phrase boundary as the
  exact control.
- Passage B keeps every pitch and chord but lengthens the detour lead
  articulation, slows its stereo movement, and uses longer releases so notes
  connect as a phrase.
- Passage C preserves Passage B's lead treatment and adds one restrained
  organ handoff at the G7-to-C6 boundary. Its two voices resolve `B-D` into
  `C-E`.

Each passage exposes Full Clip, Melody Only, and direct `Detour Deepens`
controls. The Passage Map follows the currently active treatment.

## Final Artifacts

- Audition:
  `Music Legacy/officewars-workday-detour-flow-audition.html`
  - SHA-256:
    `3FF125EA856DBF303EB736F227501674F62BBCED524EAB9BEE51114F599B73F4`
- Focused verifier:
  `.officewars-workday-detour-flow-verify.py`
  - SHA-256:
    `1BC7CD7CC990D12666CD9480CFD906A43F5956CBB194F0A0110CA1755465B8F1`
- Retained visual:
  `.visual-workday-detour-flow-audition.png`
  - SHA-256:
    `A19F04A26C5CAE4F5C7F0E14CA485E503EEE52E81DA24748515A4FAC46A34D88`

## Verification

The focused browser verifier passed:

- exact current-form context;
- exact selected Candidate C pitches, chords, and roots;
- exact Ensemble C identity;
- exact `112 BPM` tempo and selected motion identity;
- anonymous treatment and approval-state contracts;
- all six Full and Melody modes;
- comparison-safe perceived output;
- the G7-to-C6 handoff plan;
- all four Passage Map starts and live highlights;
- `aria-current="step"` state;
- pause, resume, seek, timestamps, and clear controls;
- 60 rapid switches;
- 100-percent headroom;
- desktop, landscape, and portrait layouts;
- two uninterrupted loops of all six modes;
- bounded source counts;
- no page or console errors; and
- cleanup to zero tracked sources.

## Decision Boundary

The listening problem is accepted as evidence that the current detour flow
needs review. Passage A, Passage B, and Passage C remain anonymous,
technically verified, and musically unselected. This diagnostic does not
revise the selected Candidate C source or approve the complete Workday form.
