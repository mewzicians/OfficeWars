# Workday Long-Form Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday Longform audition. It
develops the selected Hybrid B foundation into an exploratory four-movement
cue intended to remain playful, readable, and sustainable during longer
Workday listening.

## Decision Status

**Technically verified; middle rejected; return retained as liked material**

The selected Hybrid B foundation remains unchanged. Human listening rejected
Movement 2 and its transition as wonky, and rejected Movement 3 as weak,
sleepy, and fragmented. Movement 4 was liked. Cue length remains unresolved
because the rejected middle prevented a fair duration judgment.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-cue-audition.html`
- Audition SHA-256:
  `281A894D6049777D39DF0F41CE982E767EE6B97A16EA4560DEC604064EDBD064`
- Verifier:
  `.officewars-workday-cue-verify.py`
- Verifier SHA-256:
  `CB5D004C2624498EB1B3E1A71D08E23820D84122625FA213F03FBABD1A3E0551`
- Desktop capture:
  `.visual-workday-cue-audition.png`
- Capture SHA-256:
  `3695570FF111735225B00C438337EAF0046D79E05D7D0CE1DFA94215711AB48F`

## Controlled Musical Contract

The full cue uses `512` eighth-note steps at `112 BPM`, producing an
approximately `137.143-second` loop.

1. **Movement 1** preserves the complete selected Hybrid B foreground,
   harmony, groove, phrase-motion arc, effects, and output calibration.
2. **Movement 2** introduces a distinct `49-attack` offbeat secondary melody
   over related `F-A-G-C` bass roots while retaining the office-funk pocket.
3. **Movement 3** reduces foreground exposure to `25` warm attacks, preserves
   kick, snare, bass, harmony, and pulse, and avoids a silent or sleepy break.
4. **Movement 4** restores the complete parent foreground and adds a
   `17-attack` secondary counterline that enters after the opening phrase.

The resulting macro-form is `A-B-C-A'`. The parent theme is heard directly in
Movements 1 and 4 rather than being quoted continuously.

## Browser Evidence

The focused Playwright runner passes:

- page parsing with no page or console errors;
- exact selected-foundation tempo, foreground, harmony, motion, effects,
  output, duration, and looping behavior;
- exact `512-step` full-cue form and four `128-step` movement boundaries;
- compositionally distinct secondary and breathing foregrounds;
- audible movement starts with average 50-percent signals of `0.031536`,
  `0.019955`, `0.020077`, and `0.030890`;
- maximum sampled movement peaks of `0.185645`, `0.129397`, `0.099001`, and
  `0.144129`;
- retained 100-percent headroom with a maximum sampled peak of `0.317880`;
- pause, resume, seeking, timestamp marking, and timestamp clearing;
- 54 rapid foundation, cue, and movement switches without accumulation;
- one uninterrupted foundation wrap;
- `278` seconds and two complete uninterrupted full-cue wraps;
- a peak live-source count of `23`;
- stop cleanup to zero tracked sources;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls; and
- visual inspection of the desktop capture.

## Listening Verdict

- Movement 1 remains the protected selected foundation.
- Movement 2 and its transition do not carry forward.
- Movement 3 does not carry forward.
- Movement 4's parent return and secondary counterline carry forward as liked
  exploratory material.
- Neither the full Draft 01 form nor its `2:17.14` duration is selected.
- The active repair is recorded in
  `verification/WORKDAY_FORM_REPAIR_DISCOVERY_2026-08-17.md`.

## Not Run

- Listening exposure beyond two full cue loops.
- Final sound design, mix, or production approval.
- UI-sound and gameplay-sound masking inside the shipped game.
- Game integration, pause/mute/refresh behavior, or playback-speed tests.
