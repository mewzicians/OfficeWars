# Workday Micro-Movement Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday micro-movement
audition. It follows the human rejection of both Workday form-repair rewrites
as awkward and stale, and isolates how often the arrangement must make a
consequential turn.

## Decision Status

**Technically verified, movement cadence unresolved**

The selected Hybrid B foundation remains protected. The Six-Movement and
Twelve-Movement relays remain unselected until human listening determines
which cadence stays alive without becoming restless.

Human listening found the Six- and Twelve-Movement relays broadly comparable,
so the experiment did not establish a preferred movement cadence. Six-Movement
Move 4 is rejected. The user described the tunes as potentially empty and
asked whether they need more instrumental support.

Arrangement support is therefore the next diagnostic hypothesis, not an
approved fix.

That successor diagnostic is now recorded in
`verification/WORKDAY_SUPPORT_DISCOVERY_2026-08-17.md`.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-microform-audition.html`
- Audition SHA-256:
  `F733F0E303D5FA01726769D0427C86F2F92E070F8A975E985E3CEA4B227EBD4A`
- Verifier:
  `.officewars-workday-microform-verify.py`
- Verifier SHA-256:
  `0C371896FC72380ED792317E687A50D12B0531057274ECCC854CAD828E253D84`
- Desktop capture:
  `.visual-workday-microform-audition.png`
- Capture SHA-256:
  `64AC2F5295A5401312B3468C0E26586D99096A3255948BA24687686C77D41A67`

## Controlled Musical Contract

Both relays remain in the selected restrained office-funk sound world at
`112 BPM`. Each is `384` eighth-note steps and approximately `102.857`
seconds long.

1. Both preserve the exact selected `128-step` Hybrid B opening.
2. Both use the same twelve foreground phrases, harmony, tempo, palette, and
   total runtime.
3. The Six-Movement Relay changes arrangement function every `64` steps, or
   approximately `17.143` seconds.
4. The Twelve-Movement Relay changes function every `32` steps, or
   approximately `8.571` seconds.
5. The shared development uses four related harmonic routes rather than
   holding one repeated progression for the complete middle.
6. The return progresses through recognition, answer, teamwork, and loop
   preparation. The Twelve-Movement version exposes those as four separate
   phrase-sized states.

The comparison therefore isolates perceived movement cadence. It does not
change the melody, harmony, tempo, palette, form length, or selected opening
between candidates.

## Browser Evidence

The focused Playwright runner passes:

- page parsing with no page or console errors;
- exact preservation of the selected Hybrid B foundation;
- exact note, harmony, tempo, palette, and runtime equality between relays;
- the intended six- and twelve-movement function plans;
- audible playback at all eighteen movement starts;
- average 50-percent movement signals between `0.025021` and `0.041170`;
- retained 100-percent headroom with a maximum sampled peak of `0.361163`;
- pause, resume, seeking, timestamp marking, and timestamp clearing;
- 60 rapid foundation and relay switches;
- parallel long playback through six foundation wraps and two complete wraps
  of each relay;
- a peak live-source count of `23` during long playback;
- stop cleanup to zero tracked sources;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls; and
- visual inspection of the final desktop capture.

The complete runner passed twice. The second pass verified the exact retained
page after the candidate cards were changed to natural rather than equal
heights.

## Not Run

- Long-exposure listening beyond the verified repeated loops.
- Final sound design, mix, complete composition, or production approval.
- UI-sound and gameplay-sound masking inside the shipped game.
- Game integration, pause/mute/refresh behavior, or playback-speed tests.
