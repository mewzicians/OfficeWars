# Boss A Windowed Percussion Approval

Date: 2026-08-19

## Decision

Human listening reported that the windowed-percussion Boss A repair removed
the intermittent static and preserved a liked tune.

`OW-MUSIC-BOSS-A-WINDOWED-PERCUSSION-REPAIR` is therefore `Approved` at:

`Music Locked/officewars-boss-a-windowed-percussion-audition.html`

The cue remains outside `officewarsautobattler.html`.

## Root Cause And Repair

The rejected pre-render contained one-sample impulses where deterministic
brush and snare slices began or ended away from zero. The final render windows
each percussion slice to zero at both boundaries without changing the
composition, harmony, form, undercurrent, timing, or broad production.

Waveform comparison:

- old adjacent-sample jumps at or above `0.02`: `76`;
- repaired adjacent-sample jumps at or above `0.02`: `0`;
- old maximum adjacent-sample jump: `0.199`;
- repaired maximum adjacent-sample jump: `0.0081`.

## Verification

`.officewars-boss-a-approved-verify.py` passed:

- one self-contained HTML with no external script or WAV dependency;
- embedded audio hash and format validation;
- impulse-free waveform threshold;
- playback, pause, resume, seeking, movement starts, and rapid switching;
- one runtime source with no source accumulation;
- two complete loop wraps;
- responsive layout and zero-source cleanup;
- no game integration.

## Lifecycle

- Approved cue:
  `Music Locked/officewars-boss-a-windowed-percussion-audition.html`
- Rejected pre-render control:
  `Music Legacy/officewars-boss-a-prerender-repair-audition.html`
- Rejected comparison:
  `Music Legacy/officewars-boss-a-windowed-percussion-comparison.html`

## Final Hashes

- Approved HTML:
  `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`
- Approved verifier:
  `C3F279FE03CB3D64AE5209999C3D2228EB3DC1A4EFB0FEAB496EF27CDB2751A4`
- Rejected pre-render control:
  `BD99F828665686E4EEE0357220212FDE5498634FCF715BEED6FC0D43C1A481CC`
- Rejected comparison:
  `C1D6C8B9212093AD21227DE23D3611D03857EC6FA8176007744089BB288235F9`
- Game HTML:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`
