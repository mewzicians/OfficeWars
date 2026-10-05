# Boss A Status Story Test

Date: 2026-08-20

## Decision Boundary

This file records the technical gate completed while
`OW-MUSIC-BOSS-A-STATUS-STORY` was the active Boss development `Test`.
It was never Approved, Completed, integrated into the game, or shipped.

Human listening later rejected `Under Review`, found `Finding Footing` usable
but too pause-heavy, found the `Holding the Line` and `Own the Cadence`
melodies insufficiently related to the established material, found
`Clock Back In` alien, and rejected uniform-feeling movement lengths.

The artifact is now `Rejected` and retained as the exact listening control for
`OW-MUSIC-BOSS-A-MELODIC-THROUGHLINE` at
`Music Legacy/officewars-boss-a-status-story-audition.html`. The Approved
rollback remains unchanged at
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`.

## Musical Contract

The six movements total `640` eighth-note steps at `168 BPM`:

1. `Challenge Issued` - `128` steps;
2. `Finding Footing` - `96` steps;
3. `Under Review` - `96` steps;
4. `Holding the Line` - `96` steps;
5. `Own the Cadence` - `128` steps; and
6. `Clock Back In` - `96` steps.

After the protected opening:

- the triangle Player voice has `148` attacks;
- the saw-led Boss has `12` sparse accents;
- every Boss accent overlaps a Player note;
- six rhythmic slots withheld in `Finding Footing` are filled in
  `Holding the Line`;
- the Player's register ceiling grows from MIDI `81` to `83` and then to one
  MIDI `88` apex; and
- `Clock Back In` removes Boss accents while restoring the cheerful callback
  contour for the loop return.

This tests one coordinated status-transformation hypothesis. Boss influence
is expressed through pressure, accompaniment, harmony, bass weight, cadence,
phrase boundaries, register, and selective borrowing rather than literal
alternating dialogue.

## Artifacts

- Retained listening control:
  `Music Legacy/officewars-boss-a-status-story-audition.html`
  - SHA-256:
    `9798FDEE52A036F404F1604E626AE52F1EF4B5C616056D4933C568C9F4986CF7`
- Embedded status-story WAV:
  - SHA-256:
    `8126F90F379FCFA6D065736C21A229672E9E702B3767DC4CD543BDDE58542DD1`
  - byte length: `10971472`
- Checked source generator:
  `.officewars-build-boss-status-story-source.ps1`
  - SHA-256:
    `E717AF4CA91C4BDF630882161FA91B01D1FB43610C114399E162C4D39A7F4F15`
- Render driver:
  `.officewars-render-boss-status-story.py`
  - SHA-256:
    `01D6914D40850332F7194FE4B325A9F5304B654B31750077379F13E6E709A62F`
- Standalone packager:
  `.officewars-package-boss-status-story.ps1`
  - SHA-256:
    `EE473295FF45BBC46A2A7460BCC1608ED579BE6C7215DD07B859BB8A85BDC073`
- Focused verifier:
  `.officewars-boss-a-status-story-verify.py`
  - SHA-256:
    `1F392069401BA298226D3412B20301C96E72E64F3AF11B924FA2CF384292488CC`
- Retained Elastic Story listening control:
  `Music Legacy/officewars-boss-a-elastic-story-audition.html`
  - wrapper SHA-256:
    `B329E3EA6389336349A8A706BE2BE5CE0ACC3F82FF2E29882BE63B7963BE8459`
  - embedded audio SHA-256:
    `2F89A24CACA693A3C7208E8784E2DE29F79AF96991C5259EC62070C57EEC9C63`
- Protected Approved rollback:
  `Music Locked/officewars-boss-a-windowed-percussion-audition.html`
  - SHA-256:
    `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`

## Verification

Pass:

- the checked generator refuses a drifted Player-voice source and produces one
  deterministic `640-step` render source;
- one standalone Test HTML contains one embedded `24kHz`, stereo, `16-bit`
  WAV and no external script or media dependency;
- `Challenge Issued` matches the Elastic control's high voice, low voice,
  undercurrent, harmony, roots, and percussion pattern;
- after the inherited `250ms` loop-tail state, opening audio differs from the
  Elastic control by at most one PCM least-significant bit, with more than
  `99.95 percent` sample equality;
- the Player timbre remains triangle with soft sine-octave support;
- all `12` Boss accents overlap Player attacks and remain below `10 percent`
  of the post-opening Player attack count;
- every reserved rhythmic slot is silent early and completed later;
- the MIDI `88` apex occurs once, only in `Own the Cadence`;
- the apex movement is the rendered energy high and exceeds
  `Finding Footing` RMS by more than `50 percent`;
- waveform peak `0.056519`, RMS `0.006238`, maximum adjacent-sample delta
  `0.008148`, and loop-seam delta `0.000031`;
- all six direct movement starts, stop and replay, pause and resume, seeking
  before and after the status turn, and `30` rapid movement switches;
- desktop and portrait responsive layouts without horizontal overflow;
- two uninterrupted complete `1:54.3` loops with one runtime source and no
  source accumulation;
- zero-source cleanup after stop;
- no browser console or page errors; and
- no game integration.

The full two-loop gate passed before lifecycle records changed. After the
predecessor Elastic Story wrapper was retagged and moved during that earlier
transition, the final packaged Status Story Test passed the same focused suite
in quick mode; its embedded WAV is unchanged.

Technical success established a valid Test at the time. Its audio and
transport behavior are now preserved as the Rejected direct control for the
Melodic Throughline Test; this evidence does not approve either composition.
