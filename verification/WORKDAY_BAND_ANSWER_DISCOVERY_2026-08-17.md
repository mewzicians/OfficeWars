# Workday Band Answer Discovery

Date: 2026-08-17

## Scope

Human listening found Role Transfer Version B generally good, but identified
the added invitation note as jarring and the reversed middle as clash-heavy.
The user explicitly retired Role Reverse and approved a simpler replacement.

This source-only diagnostic preserves Role Transfer Version B as exact
Version A. Version B keeps the same selected Ensemble C foundation, `112 BPM`
tempo, `384-step` form, harmony, Recognition treatment, Teamwork treatment,
and loop duration while changing only the invitation and middle exchange.

## Comparison

Version B tests one simplified relationship:

1. the prepared organ `C` remains, but the added organ `D` and three later
   organ pickups are removed;
2. the retired reversed phrase becomes an eight-note Band Answers statement
   using only chord tones over the existing harmony;
3. the lead rests while the organ answers, then owns the complete following
   phrase from its first note; and
4. Recognition and Teamwork remain exactly as they were in Role Transfer
   Version B.

The audition provides both complete forms plus direct A/B clips for the
invitation and middle exchange.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-band-answer-audition.html`
- Audition SHA-256:
  `002C22EE7304872E96F6A517A4C465FACE2483CD170BD7A2D96AC66A5FA2CFF4`
- Verifier:
  `.officewars-workday-band-answer-verify.py`
- Verifier SHA-256:
  `B9D7D41CCF5DBDEF5E775948ECAA2D4C8B807BE67D7831A55C4AB38FFE5D35DB`
- Visual capture:
  `.visual-workday-band-answer-audition.png`
- Visual-capture SHA-256:
  `1061A8D7A7DBFEEDD031BFB6CD2F176DA0116154319EE507B8152609FA28DFC4`
- Protected Role Transfer control SHA-256:
  `F33F4E714D27109C4419A71A45C4577B11538151F47C3E5E6799B3BEC43EC55B`
- Protected Transition Repair source SHA-256:
  `F9D0B935D2D3A9A7DE8E3EC534362D2A39E5279FBF4355E5C05B9852010BFBE9`

## Verification

The focused Playwright run passes:

- exact Version A equality with Role Transfer Version B;
- unchanged tempo, form, harmony, selected ensemble, Recognition
  counterlines, and Teamwork counterlines;
- direct `B -> C` preparation without the added invitation `D`;
- zero candidate organ pickups in the two affected phrases;
- one eight-attack Band Answers statement using only chord tones;
- complete organ ownership of Band Answers and complete lead ownership of the
  following reply;
- six audible and comparison-safe playback modes at 50-percent volume;
- 100-percent output headroom;
- pause, resume, seek, timestamp, and mark clearing;
- 72 rapid A/B switches;
- one-shot focused-clip completion;
- two uninterrupted wraps of both complete forms;
- bounded active and peak source counts;
- cleanup to zero active sources; and
- desktop, landscape, and portrait layout checks.

## Listening Verdict

The user did not like Band Answers at all. The replacement is rejected rather
than retained for tuning.

Role Reverse remains retired. Recognition, Teamwork, selected Ensemble C,
`112 BPM`, and the Hybrid B foundation remain protected. No complete Workday
cue, final production, mix, gameplay integration, or shipped audio is
selected.
