# Parent Leitmotif Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars parent-leitmotif discovery
page. It establishes audition stability, candidate separation, and interface
readiness. It does not establish musical approval.

## Artifacts

- Audition:
  `Music Locked/officewars-parent-leitmotif-audition.html`
- Audition SHA-256:
  `F66DFBA2B9CF195AC0737DC8E49EA350FDDA04B06434F501C374F682B0479FBB`
- Verifier:
  `.officewars-parent-leitmotif-verify.py`
- Verifier SHA-256:
  `8C81205A0D804F5A169DDAC7F3BA72208ABD6A8D4C74F8DA0F04FBCB2C3FA4B5`
- Desktop capture:
  `.visual-parent-leitmotif-audition.png`
- Capture SHA-256:
  `D4EDE562A7C78F47BCD4CD9AC3E1D63590D6B50AF6237E158CA2A60AF4D0813C`

## Musical Structure

- Three anonymous and distinct parent candidates are present.
- Each Core is a 32-step, approximately 9.23-second one-shot at 104 BPM.
- Each Workday form is a 128-step, approximately 36.92-second loop at
  104 BPM.
- Every Workday loop begins with the exact notes of its corresponding Core and
  then develops through Answer, Develop, and Return phrases.
- Candidate A preserves a descent-and-completion identity.
- Candidate B preserves a rise-and-return identity.
- Candidate C introduces a new lift-and-settle identity with a semitone loop
  return.
- The selected Casino composition and production files were not edited.

## Browser Evidence

The focused Playwright runner passes:

- page parsing with no page or console errors;
- exact candidate, theme, note-plan, duration, and loop assertions;
- monotonic short- and long-tone envelopes;
- audible Core and Workday output at 50-percent volume;
- comparison-safe Workday levels;
- retained headroom at 100-percent volume;
- pause and resume;
- seeking into the third phrase;
- issue timestamp marking and clearing;
- 48 rapid track switches without scheduler or source accumulation;
- 78 seconds of uninterrupted playback with two complete Workday wraps;
- stop cleanup to zero tracked sources;
- a three-column desktop layout;
- a two-column landscape layout;
- a one-column portrait layout; and
- no horizontal overflow or clipped controls.

## Decision Status

All three candidates remain exploratory. No parent leitmotif, Workday cue,
scene assignment, or Casino transformation is selected or approved.
