# Boss A Static-Pop Repair

Date: 2026-08-19

## Scope

This source-only diagnostic preserves the liked integrated paper-brush Boss A
pass and changes only an intermittent static-pop cause inside its noise
envelope.

No music was added to `officewarsautobattler.html`.

## Lifecycle

- Rejected historical control:
  `OW-MUSIC-BOSS-A-PAPER-BRUSH`
  - `Music Legacy/officewars-boss-a-percussion-repair-audition.html`
- Rejected envelope-only Test:
  `OW-MUSIC-BOSS-A-POP-REPAIR`
  - `Music Legacy/officewars-boss-a-pop-repair-audition.html`

The older paper-brush artifact moved through Limbo because its musical
treatment was liked while an occasional static pop blocked approval. Once the
good material was preserved in the envelope Test, the Limbo artifact became
Rejected. Human listening later found a second, seek-dependent pop, so this
envelope-only Test also became Rejected and its useful material moved into
`OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`.

## Root Cause

Every deterministic noise hit used a smooth attack, then changed gain
instantaneously from full level to `68 percent` at the release boundary. That
discontinuous `32 percent` drop could produce a brief broadband pop without
clipping the complete mix.

The previous verifier checked signal peak and source lifecycle but did not
isolate gain-envelope continuity, so it could miss this sub-clipping artifact.

## Repair

The Test changes the instantaneous gain assignment into a continuous
exponential ramp. It preserves:

- deterministic noise bytes;
- paper-brush and snare-air rhythm;
- offsets, filters, pan, sends, and output compensation;
- Boss A melody and harmony;
- bass and sustained On the Clock undercurrent;
- the four-movement `512-step`, approximately `91.429-second` form;
- `168 BPM`; and
- the complete mix architecture.

The audition exposes:

- `Paper Brush / Abrupt Envelope`, the exact Rejected control;
- `Pop Brush Only`, its isolated noise monitor;
- `Boss A / Integrated Smooth Brush`, the active Test; and
- `Smooth Brush Only`, its isolated noise monitor.

## Artifacts

- Test audition:
  `Music Legacy/officewars-boss-a-pop-repair-audition.html`
  - SHA-256:
    `7E6656708335EADFDAD0AD8ECC40E5D7426FCF555DFE3CB36B24C49C922C8469`
- Focused verifier:
  `.officewars-boss-a-pop-repair-verify.py`
  - SHA-256:
    `C275941555CDCF69D9F17E0E369AD560D45715813C450F1604A7DAFA0107F095`
- Retained visual:
  `.visual-officewars-boss-a-pop-repair-audition.png`
  - SHA-256:
    `3E4825D889CB34E9C01FB9F2922D8758355E5036BF8E943F3E625D87C5796C6F`
- Rejected control:
  `Music Legacy/officewars-boss-a-percussion-repair-audition.html`
  - SHA-256:
    `86A19FDE1BD0EEF44F35C797F76E7DB0A05AC6878A256B4E306E1A4F79CE1A0F`
- Game:
  `officewarsautobattler.html`
  - SHA-256:
    `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`

## Focused Verification

The quick browser gate passed:

- exact Rejected-control and protected-source hashes;
- exact melody, harmony, bass, undercurrent, form, duration, and movement map;
- stable internal label `OW-MUSIC-BOSS-A-POP-REPAIR`;
- lifecycle status `Test`;
- comparison-safe complete mixes and isolated monitors;
- all movement starts and live accessible highlighting;
- pause, resume, seeking, rapid switching, headroom, responsive layouts, and
  cleanup.

Browser-rendered constant-signal envelope evidence:

- Rejected abrupt transition delta: `0.32`
- Smooth Test transition delta: `0.003025`

Observed average levels at `50 percent` page volume during the retained full
run:

- Rejected complete control: `0.0141523`
- Rejected brush only: `0.00060525`
- Smooth complete Test: `0.01586047`
- Smooth brush only: `0.00051238`

## Repeated-Loop Verification

All four modes completed at least two uninterrupted loops:

| Mode | Wraps | Peak sources | Observed signal peak |
|---|---:|---:|---:|
| Rejected complete control | 2 | 22 | `0.063991` |
| Rejected brush only | 2 | 3 | No clipping detected |
| Smooth complete Test | 2 | 22 | `0.034981` |
| Smooth brush only | 2 | 3 | `0.008947` |

The verifier reported:

- no clipping;
- no source accumulation;
- stable loop resets;
- zero active sources after every stop; and
- no browser errors.

The background launch wrapper emitted non-terminating PowerShell environment
assignment warnings before Python started. The verifier itself ran to its PASS
message and completed every asserted gate.

## Decision Boundary

Human listening still heard an inconsistent pop that could disappear after
manual seeking. The smooth-envelope artifact therefore moved through Limbo and
is now Rejected. Its useful music and envelope repair are preserved in
`OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`.

This evidence remains valid for the envelope defect it tested. It does not
establish scheduler resilience or approve the complete boss cue.
