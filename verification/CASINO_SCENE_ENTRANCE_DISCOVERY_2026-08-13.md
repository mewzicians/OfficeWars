# Casino Scene Entrance Discovery Verification

Date: 2026-08-13

## Scope

This source-only pass builds and verifies three ways to enter the selected
Corporate Contraband Casino loop. It does not change
`officewarsautobattler.html`, shipped gameplay, balance, or game audio.

## Decision Status

**Technically verified, musically unselected**

The user approved building the entrance comparison. No entrance is selected
until the user listens and explicitly chooses one.

The audition compares:

- `Direct Start`: immediate Hook Payoff at 164 BPM.
- `Quickening Lift`: a 16-step, approximately 3.02-second entrance that
  accelerates from 154 to 164 BPM.
- `Office Signal Transform`: a 16-step, approximately 2.93-second
  workplace-notification-to-Casino gesture at 164 BPM.

Both authored intros enter the exact selected 192-step Corporate Contraband
loop at step 16, then repeat only that loop.

## Preserved Contract

**Pass**

The focused runner proved that all three candidates preserve:

- the exact selected 192-step foreground;
- the four locked movement treatments;
- Chase Breathing, the cleaned late sections, and the continuous seam;
- the final `D -> E` return;
- Corporate Contraband production identity;
- the Pass 06 `6.264x` calibration; and
- the selected approximately 35.12-second repeating loop.

The locked production page remained unchanged at SHA-256
`194A07E3A6D1088B46ACBF82BAC210B37C792FBD8194AF44720E754015ED329D`.
(as of this record; repinned to `07074232` by the 2026-08-27 settle repair, which changed no music)

## Focused Verification

**Pass**

The Playwright runner verified:

- exact intro note plans and 16-step boundaries;
- Quickening Lift beginning at 154 BPM and reaching 164 BPM before handoff;
- Office Signal Transform remaining at 164 BPM;
- audible, unclipped starts and natural handoffs into Hook Payoff;
- direct loop-seam traversal;
- full mix, drums and bass, motif lead, and space and texture isolation;
- pause, resume, and seeking from an authored intro into the selected loop;
- 45 rapid switches across all three candidates;
- 82 seconds of uninterrupted authored-intro playback with two complete loop
  wraps and no source accumulation;
- cleanup to zero active sources;
- retained headroom at 100-percent master volume;
- no page or console errors; and
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls.

At 50-percent master volume, sampled entrance waveform peaks were `0.75580`
for Direct Start, `0.35229` for Quickening Lift, and `0.12057` for Office
Signal Transform. The 100-percent Office handoff peaked at `0.74415`, below
the `0.95` headroom ceiling.

## Visual Evidence

**Pass**

The desktop capture was inspected. The three candidates, timing and tempo
metadata, shared Layer Inspector, transport, and hidden post-listen notes are
clear. The audition keeps the listening choice primary and does not imply that
an entrance has already been selected.

## Not Run

- Human listening approval of any entrance.
- In-game Casino transition timing or synchronization with scene animation.
- Redline, stingers, bust, cash-out, or exit behavior.
- Shipped-game audio integration.

## Hashes

- `prototypes/officewars-casino-scene-audition.html`:
  `A06672D6DBC833AB231299B93025C63096919ECDB7832EBD733673F060D9A98D`
  (as of this record; repinned to `D6AAF6D3` by the 2026-08-27 settle repair, which changed no music)
- `.officewars-casino-scene-verify.py`:
  `EB7B912E347CB3AC64AFF76E9FCC8B979984F3D27A79C7CCAF5C7955A91C00ED`
- Desktop evidence capture:
  `BEE20E4C1C45BAD84559F5BE57FC9EE057E2625B7315BCC08AD231BE6E31DCAC`
- Selected production reference, unchanged:
  `194A07E3A6D1088B46ACBF82BAC210B37C792FBD8194AF44720E754015ED329D`
  (as of this record; repinned to `07074232` by the 2026-08-27 settle repair, which changed no music)
- Shipped game, unchanged:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`
