# Workday Form Repair Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday form-repair audition.
It replaces the rejected middle of Draft 01 while preserving the selected
Hybrid B opening and the liked parent-and-counterline return.

## Decision Status

**Technically verified, musically rejected**

Draft 01 Movements 2 and 3 remain rejected. Its Movement 4 return is retained
as liked material, not selected as a complete cue.

Human listening found both the Compact and Extended rewrites awkward. Their
large movements still felt long and stale, and the return behaved like too few
perceived states despite containing multiple melodic phrases. Neither rewrite
carries forward as the active Workday form.

The active cadence repair is recorded in
`verification/WORKDAY_MICROFORM_DISCOVERY_2026-08-17.md`.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-form-repair-audition.html`
- Audition SHA-256:
  `37CE0BCC15E49CB49D76D79D4B8DB9184A4071E023E57A2080427C6B9AC74B2D`
- Verifier:
  `.officewars-workday-form-repair-verify.py`
- Verifier SHA-256:
  `1BB31C5CBDD37E0FF073D0FF5AE877977573B33FCB77CD0492614423E69362BF`
- Desktop capture:
  `.visual-workday-form-repair-audition.png`
- Capture SHA-256:
  `955B3036641E79F884476143B210B469957EC9BD085D56D724464288B6BA3ED0`

## Controlled Musical Contract

All material remains at `112 BPM` in the selected restrained office-funk
sound world.

1. Both rewrites preserve the exact `128-step` Hybrid B opening.
2. Both use the same new `128-step`, `60-attack` Connected Middle.
3. The Compact Rewrite returns immediately, producing a `384-step`,
   approximately `102.857-second` loop.
4. The Extended Rewrite adds one `128-step`, `64-attack` Momentum movement,
   producing a `512-step`, approximately `137.143-second` loop.
5. Both returns preserve the complete parent foreground and Draft 01's liked
   `17-attack` counterline.

The opening ends on an F-root harmony and B melody note. The Connected Middle
begins on the same F root and resolves its last B into the returning C. In the
Extended form, the Connected Middle hands into the Momentum movement on a
shared C root; Momentum ends on G and B before the return resolves to C.

## Browser Evidence

The focused Playwright runner passes:

- page parsing with no page or console errors;
- exact selected-foundation notes, harmony, phrase-motion plan, effects,
  output, timing, and loop behavior;
- exact shared Connected Middle across both repaired forms;
- exact retained parent foreground and 17-attack return counterline;
- exact `384-step` Compact and `512-step` Extended forms;
- intended harmony and melody preparation at every movement boundary;
- audible movement starts with average 50-percent signals between `0.028619`
  and `0.031634`;
- sampled movement peaks between `0.133178` and `0.165005`;
- retained 100-percent headroom with a maximum sampled peak of `0.317880`;
- pause, resume, seeking, timestamp marking, and timestamp clearing;
- 60 rapid foundation, Compact, Extended, and movement switches;
- parallel long playback through eight foundation wraps, two Compact wraps,
  and two Extended wraps;
- a peak live-source count of `23` during long playback;
- stop cleanup to zero tracked sources;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls; and
- visual inspection of the desktop capture.

## Not Run

- Long-exposure listening beyond the verified repeated loops.
- Final sound design, mix, complete composition, or production approval.
- UI-sound and gameplay-sound masking inside the shipped game.
- Game integration, pause/mute/refresh behavior, or playback-speed tests.
