# Workday Title Selection

Date: 2026-08-18

## Decision

The selected Workday cue's player-facing title is **On the Clock**.

`Tribrid D` remains only the internal development label for the selected
four-loop long-cycle plan. The title change does not alter the notes, harmony,
form, production, variation strategy, loop timing, or audio scheduler.

## Scope

The title applies to the selected standalone Workday cue represented by:

`Music Locked/officewars-workday-long-cycle-tribrid-audition.html`

The cue remains outside `officewarsautobattler.html`. Gameplay masking, device
translation, adaptive behavior, implementation, shipping, and final delivery
remain open.

## Verification

The title-only regression confirmed:

- the selected cue API reports `On the Clock`;
- the selected card and page heading display `On the Clock`;
- `Tribrid D` remains available as the internal lineage label;
- Hybrid D, Ensemble C, Candidate C, Passage D, the selected form, and the
  four-loop plan remain exact;
- no boss identity or game integration was selected; and
- the existing audio lifecycle checks still pass.

## Retained Reference

- Audition SHA-256:
  `FF677CC9F4F85501BCE6979D614FAE90DC293A308BCE31E7DC9EA4867F91F4B2`
  (as of this record; repinned to `60DDDF21` by the 2026-08-27 settle repair, which changed no music)
- Verifier SHA-256:
  `5F34425E8887F5AAB0926260E8E295DD8CC1CDD0317D8D63C4F7C2A9EB584D5D`
- Retained visual SHA-256:
  `D0E67A094550C14D2173A1BF04E9BA3A85062E827E28AC0D0A1236D4C22D13AD`
