# Workday Support Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday support-role audition.
It follows the unresolved Six-versus-Twelve movement comparison and tests
whether the shared cue feels empty because it lacks a clear supporting
instrumental role.

## Decision Status

**Technically verified; listening hypothesis not supported**

The current Six-Movement arrangement remains the exact control. Human
listening found that Candidate A and Candidate B still felt empty, left the
melody sounding standalone, and did not communicate a recognizable
harmonization instrument or clear instrumental intention. Neither treatment
is selected or carried forward as the active solution.

The successor ensemble-identity audition tests clearly differentiated
instrument behaviors and exposes Full Mix, Backing Only, and Harmony Only
playback. See
`verification/WORKDAY_ENSEMBLE_DISCOVERY_2026-08-17.md`.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-support-audition.html`
- Audition SHA-256:
  `31938B99EA60F7658FC170EEA08AE6771F29BB22CB424B15A77800D61C37626D`
- Verifier:
  `.officewars-workday-support-verify.py`
- Verifier SHA-256:
  `CC11D1EC0DFD40375FB1D41C18DCB833F75F8C073B9E34DFA15E78317B934179`
- Desktop capture:
  `.visual-workday-support-audition.png`
- Capture SHA-256:
  `A5625EEB8BC90089E7BB5D2232BC2A3746B301737994F73F8B9789DB0C8BF327`

## Controlled Musical Contract

All three candidates remain `384` steps, approximately `1:42.86`, and
`112 BPM`. They share the exact foreground, harmony, Six-Movement phrase
profiles, drums, bass, effects, palette, and loop behavior.

1. **Current Arrangement** adds no support and matches the preceding
   Six-Movement source.
2. **Candidate A** adds two warm sustained inner voices at each bar without
   changing any existing part.
3. **Candidate B** adds eighteen restrained reply attacks: one three-note
   response near the end of every two-phrase movement.

The page keeps the support identities anonymous during first listening.
Move 3, Move 4, and Move 5 jump controls provide direct comparison around the
disliked and potentially empty span.

## Browser Evidence

The focused Playwright runner passes:

- page parsing with no page or console errors;
- exact foreground and Six-Movement profile equality with the preceding
  micro-movement source;
- exact foreground, harmony, tempo, form, groove, and movement equality across
  the control and both candidates;
- the intended zero-support, two-sustained-voice, and eighteen-reply-attack
  contracts;
- audible Move 3, Move 4, and Move 5 starts for every candidate;
- 50-percent movement averages between `0.031409` and `0.040836`;
- comparison-window averages of `0.034967`, `0.033878`, and `0.031370`;
- retained 100-percent headroom with a maximum sampled peak of `0.344819`;
- pause, resume, seeking, timestamp marking, and timestamp clearing;
- 60 rapid control and candidate switches;
- two uninterrupted complete loops of all three candidates;
- peak live-source counts of `23`, `29`, and `24` during long playback;
- stop cleanup to zero tracked sources;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls; and
- visual inspection of the `1365 x 1011` desktop capture.

## Not Run

- Long-exposure listening beyond the verified repeated loops.
- A combined support arrangement.
- Final sound design, mix, complete composition, or production approval.
- UI-sound and gameplay-sound masking inside the shipped game.
- Game integration, pause/mute/refresh behavior, or playback-speed tests.
