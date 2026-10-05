# Boss A Character Dialogue Test

Date: 2026-08-19

## Status

- Lifecycle: `Test`
- Internal label: `OW-MUSIC-BOSS-A-CHARACTER-DIALOGUE`
- Canonical source:
  `prototypes/officewars-boss-a-character-dialogue-audition.html`
- Game integration: none

This Test supersedes the rejected melodic-development and register-dialogue
branches. It remains exploratory until the user listens.

## Musical Contract

- Preserve the Approved static-free Boss A opening exactly.
- Give the Player a light, cheerful, loud, happy high-register voice.
- Give the Boss a serious, measured, no-nonsense low-register voice.
- Begin with non-overlapping private pitch-class vocabularies.
- Let both voices adopt the other's vocabulary after contact.
- Use parallel motion and interruption without reducing the exchange to
  mechanical high-low alternation.
- Resolve the prepared Player ascent at MIDI `88` and hold the apex instead of
  descending before arrival.
- Preserve adopted traits in `Changed by Meeting`.

The movement plan is:

1. `Challenge Issued`
2. `Different Languages`
3. `Heated Exchange`
4. `Changed by Meeting`

## Technical Evidence

- Standalone HTML SHA-256:
  `7E109930FD81CECC5630F0FF731FC8A9753A1852DAD9E997EAE7E6B50A85E465`
- Focused verifier SHA-256:
  `C4C94F1BF09B8045C3983DBB85DADC27D9D8718774152FAAFCD892552580C0A6`
- Embedded WAV SHA-256:
  `8B69FD577657AB2095712E011EA6D8AD5C9D02B288F7D01E809615B02503D1CC`
- Embedded WAV bytes: `8,777,188`
- Approved baseline SHA-256:
  `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`
- Game SHA-256:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`

The focused verifier passed:

- exact Approved opening preservation;
- Player and Boss personality metadata;
- private pitch vocabularies;
- mutual vocabulary adoption;
- parallel-path behavior;
- promised-apex arrival and hold;
- all four movement starts;
- clean waveform with no large impulse;
- pause, resume, seek, responsive layout, and zero-source cleanup;
- no external script or audio dependency; and
- no game integration.

The complete verifier also passed two uninterrupted loops with one active
source, no clipping, stable wraparound, and zero-source cleanup.

## Lifecycle Result

- `OW-MUSIC-BOSS-A-MELODIC-DEVELOPMENT` is Rejected in `Music Legacy/`.
- `OW-MUSIC-BOSS-A-REGISTER-DIALOGUE` is Rejected in `Music Legacy/`.
- `OW-MUSIC-BOSS-A-CHARACTER-DIALOGUE` is the sole active Boss Test.

Technical success does not approve the composition. The next evidence must be
the user's listening reaction to the Player/Boss personalities, mutual
borrowing, and earned apex.
