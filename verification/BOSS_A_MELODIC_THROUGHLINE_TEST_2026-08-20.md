# Boss A Melodic Throughline Test

Date: 2026-08-20

## Decision Boundary

This file records the technical gate completed while
`OW-MUSIC-BOSS-A-MELODIC-THROUGHLINE` was the active Boss development `Test`.
It was never Approved, Completed, integrated into the game, or shipped.

The Test responds to human listening that:

- rejected `Under Review`;
- found `Finding Footing` usable but interrupted by too many pauses;
- rejected the current `Holding the Line` and `Own the Cadence` melodies as
  insufficiently related development;
- found the separate `Clock Back In` tune alien; and
- rejected uniform-feeling movement durations in favor of phrase-led spans.

Human listening later found `Finding Footing` was getting closer but found
`Pressure Turn`, `Melodic Drive`, and `Full Statement` strange to hear,
unsatisfying as tunes, and unconvincing as Boss music. Source review confirmed
that the later form repeated one eight-note contour as a mechanical template
while sparse Boss accents failed to sustain the selected galloping identity.
Those movements are retired.

The artifact is now `Rejected` and retained as the exact listening control for
`OW-MUSIC-BOSS-A-TUNE-DISCOVERY` at
`Music Legacy/officewars-boss-a-melodic-throughline-audition.html`. The
Approved rollback remains unchanged at
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`.

## Musical Contract

The five movements total `512` eighth-note steps at `168 BPM`:

1. `Challenge Issued` - `128` steps;
2. `Finding Footing` - `88` steps;
3. `Pressure Turn` - `56` steps;
4. `Melodic Drive` - `144` steps; and
5. `Full Statement` - `96` steps.

Movement lengths are consequences of phrase jobs and cadences rather than a
shared duration standard.

After the protected opening:

- the triangle Player voice remains the foreground identity;
- one deliberate eight-step breath is the only melodic gap longer than four
  steps;
- nine sparse Boss saw accents overlap Player attacks;
- thirteen declared Player statements derive from the recognizable
  scale-degree contour `1-2-3-5-4-3-2-1`;
- the movement register ceiling grows from MIDI `81` to `83`, `86`, and one
  MIDI `88` apex;
- the apex occurs inside a transposed version of the familiar contour; and
- the final `32` steps reproduce the exact opening Player callback pattern
  inside the final movement rather than introducing a separate return tune.

This tests one coordinated hypothesis: recognizable melodic development,
reduced pause exposure, and phrase-led unequal form will let the cheerful
Player gain authority without losing identity.

## Artifacts

- Retained listening control:
  `Music Legacy/officewars-boss-a-melodic-throughline-audition.html`
  - SHA-256:
    `7EA17F521AEFA9772C9BC7A82F357819098901B70563A39DF41EBBF959B332B5`
- Embedded melodic-throughline WAV:
  - SHA-256:
    `DF60B8A506EAF48D52A924A9CEF10D797A3957A02C0FBC414EC5BD0425CBEE1D`
  - byte length: `8777188`
- Checked source generator:
  `.officewars-build-boss-melodic-throughline-source.ps1`
  - SHA-256:
    `8592345CCE559FD9A3D59A0DB6FC38F268DB782DC17317396359AB33C8B74A0F`
- Render driver:
  `.officewars-render-boss-melodic-throughline.py`
  - SHA-256:
    `1B38018F0B49F793C8E9610E2F5962F4E28041A20415B681522CE86ECE116EB2`
- Standalone packager:
  `.officewars-package-boss-melodic-throughline.ps1`
  - SHA-256:
    `F363403A409842C134A345BA9F6629788BC7A46D29FDFD29D557945339253342`
- Focused verifier:
  `.officewars-boss-a-melodic-throughline-verify.py`
  - SHA-256:
    `9FB7FD21765BC0CDC15AB58C91171DF6E13167C0D722C7AEB7BC167DB7FC926F`
- Active replacement Test:
  `prototypes/officewars-boss-a-tune-discovery-audition.html`
  - SHA-256:
    `EA490615C007AEB059C37790ABB238494C94F23D72AF3FC14ADBCFDFCABF0A9A`
- Protected Approved rollback:
  `Music Locked/officewars-boss-a-windowed-percussion-audition.html`
  - SHA-256:
    `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`

## Verification

Pass:

- the generator refuses a drifted Player-voice source and produces one
  deterministic `512-step` render source;
- one standalone Test HTML contains one embedded `24kHz`, stereo, `16-bit`
  WAV and no external script or media dependency;
- `Challenge Issued` matches the Status Story control's high voice, low voice,
  undercurrent, harmony, roots, and percussion pattern;
- after the inherited `250ms` loop-tail state, opening audio differs from the
  control by at most one PCM least-significant bit, with `99.999263 percent`
  exact samples;
- the only post-opening melodic gap longer than four steps is the declared
  eight-step breath;
- all Boss accents overlap Player attacks and remain sparse;
- all thirteen declared motif statements match their source note plans;
- the MIDI `88` apex occurs once, only inside `Full Statement`;
- the final callback tag exactly matches the opening Player callback pattern;
- movement RMS rises from `0.005159` through `0.006301` and `0.007188` to
  `0.007870` in `Full Statement`;
- waveform peak `0.056000`, RMS `0.006487`, maximum adjacent-sample delta
  `0.009125`, and loop-seam delta `0.000031`;
- all five direct movement starts, stop and replay, pause and resume, seeking,
  and `30` rapid movement switches;
- desktop and portrait responsive layouts without horizontal overflow;
- two uninterrupted complete `1:31.4` loops with one runtime source and no
  source accumulation;
- zero-source cleanup after stop;
- no browser console or page errors; and
- no game integration.

The full two-loop gate passed while this artifact was active. After human
rejection, the wrapper moved to Rejected history and was metadata-retagged as
the listening control without changing its embedded WAV. The final control
passed the focused lifecycle and browser suite again in quick mode.

Technical success established a valid Test at the time. It did not make the
mechanical motif-template continuation a satisfying tune or Boss song.
