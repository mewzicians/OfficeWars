# Boss A Elastic Story Test

Date: 2026-08-20

## Decision Boundary

This file records the technical gate completed while
`OW-MUSIC-BOSS-A-ELASTIC-STORY` was the active Boss development `Test`.
It was never Approved, Completed, integrated into the game, or shipped.

The artifact is now `Rejected` and retained as the exact musical listening
control for `OW-MUSIC-BOSS-A-STATUS-STORY`.

The Test preserves the liked `Challenge Issued` and `Finding a Rhythm`
movements, then replaces the rejected back half with a seven-movement,
function-driven confrontation story:

1. `Challenge Issued` - 128 steps.
2. `Finding a Rhythm` - 128 steps.
3. `Over Your Shoulder` - 64 steps.
4. `Accidental Sync` - 64 steps.
5. `Back to Business` - 64 steps.
6. `Changed Apart` - 64 steps.
7. `Changed by Meeting` - 128 steps.

Each movement leaves when its dramatic job is complete. The regression retains
battle pulse and pressure, and the payoff reaches the Player apex at MIDI 88.

The Limbo predecessor is Rejected history at
`Music Legacy/officewars-boss-a-character-flow-audition.html`.

## Artifacts

- Retained listening control:
  `Music Legacy/officewars-boss-a-elastic-story-audition.html`
  - SHA-256:
    `B329E3EA6389336349A8A706BE2BE5CE0ACC3F82FF2E29882BE63B7963BE8459`
  - embedded audio SHA-256:
    `2F89A24CACA693A3C7208E8784E2DE29F79AF96991C5259EC62070C57EEC9C63`
- Focused verifier:
  `.officewars-boss-a-elastic-story-verify.py`
  - SHA-256:
    `2E2E11E10DEC28B72B132588BAA6BDB4465CC8A0702B2CB8B88468AB14EC2F78`
- Rejected predecessor:
  `Music Legacy/officewars-boss-a-character-flow-audition.html`
  - SHA-256:
    `5F4BDF0D0C8AEE0388418530E2F8770EDF6E44CC43E3E7F6C04A5E88C1323AA3`
- Protected Approved rollback:
  `Music Locked/officewars-boss-a-windowed-percussion-audition.html`
  - SHA-256:
    `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`

## Verification

Pass:

- one standalone HTML with embedded audio and no external media dependency;
- rendered `1:54.3` duration chip and complete 640-step form;
- exact first 256 preserved steps;
- variable movement starts `[0, 128, 256, 320, 384, 448, 512]`;
- variable lengths `[128, 128, 64, 64, 64, 64, 128]`;
- distinct Player and Boss opening vocabularies;
- both voices present during hovering pressure;
- contracted Player line during regression;
- substantial final shared language and MIDI 88 apex;
- bounded melodic jumps in the tested conversational phrases;
- all seven direct movement starts;
- pause, resume, seek, responsive layouts, and browser-error capture;
- clean waveform below the large-impulse threshold;
- two uninterrupted complete loops with one runtime source;
- zero-source cleanup after stop; and
- no game integration.

Technical success established the artifact as a valid Test at the time. Its
audio and transport behavior are now preserved as a Rejected listening
control; this evidence does not approve the composition.
