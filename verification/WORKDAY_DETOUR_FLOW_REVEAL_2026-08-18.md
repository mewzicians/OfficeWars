# Workday Detour Flow Reveal

Date: 2026-08-18

## Listening Result

The first anonymous listen completed its purpose. The listener liked all three
passages but could not reliably identify what changed between them.

This is evidence that the treatments are pleasant and close enough to compare,
but it does not select a winner. The audition now reveals each mechanism
permanently so later reactions can refer to the actual musical cause.

## Durable Comparison

Every passage still shares:

- Candidate C's selected pitches and harmony;
- the same bass, Ensemble C, `112 BPM`, context, duration, and motion identity;
- the same Full Clip and Melody Only monitoring; and
- the same Passage Map and transport behavior.

The revealed differences are:

1. **Passage A: Original**
   - the exact current articulation;
   - shorter lead notes and earlier releases;
   - faster left-to-right stereo motion; and
   - no transition handoff.
2. **Passage B: Connected Lead**
   - every pitch and chord remains exact;
   - longer lead holds and gentler releases;
   - slower stereo motion; and
   - no transition handoff.
3. **Passage C: Organ Handoff**
   - the same connected lead as Passage B; and
   - one restrained organ handoff resolving `B-D` over G7 into `C-E` over C6.

The now-playing panel also states whether the active mode includes connected
articulation, the organ handoff, or neither.

## Final Artifacts

- Audition:
  `Music Legacy/officewars-workday-detour-flow-audition.html`
  - SHA-256:
    `523D39EF30696E542D422B9A080D77EFC2340EBA8B9BB19EED2D2A1E7A756ACA`
- Focused verifier:
  `.officewars-workday-detour-flow-verify.py`
  - SHA-256:
    `3735D15C0F15226F3B6E6C1EB1CB6FA701F90F26D70BCB909A090284F1B544A8`
- Retained visual:
  `.visual-workday-detour-flow-audition.png`
  - SHA-256:
    `676DD59B8D8ED49FADBE52917989990861DF3599E0A0564597E64741F503B9C9`

## Verification

The exact revealed page passed:

- the shared-material and explicit A/B/C label contracts;
- exact selected Candidate C pitches, harmony, roots, Ensemble C, tempo,
  context, and motion identity;
- all six Full Clip and Melody Only modes;
- comparison-safe Full Mix output;
- the intentional connected-sustain difference in Melody Only monitoring;
- the exact G7-to-C6 handoff plan;
- all four Passage Map starts, live highlights, and `aria-current="step"`;
- pause, resume, seeking, timestamps, and clear controls;
- 60 rapid switches;
- 100-percent headroom;
- desktop, landscape, and portrait layouts;
- two uninterrupted loops of every mode;
- bounded source counts; and
- cleanup to zero tracked sources.

Visual inspection confirmed that the revealed explanations, controls, active
passage state, and now-playing description remain readable without overlap.

## Decision Boundary

The anonymous stage is complete and preserved in
`WORKDAY_DETOUR_FLOW_DISCOVERY_2026-08-18.md`. Passage A, Passage B, and Passage
C remain technically verified and musically unselected. The reveal changes
only explanation and monitoring context; it does not change the audio or
approve the complete Workday form.
