# Boss A Tune Discovery Test

Date: 2026-08-21

## Decision Boundary

`OW-MUSIC-BOSS-A-TUNE-DISCOVERY` is the active Boss development `Test`. It is
not Approved, Completed, integrated into the game, or shipped.

Human listening found the prior Melodic Throughline revision's
`Finding Footing` direction promising but rejected `Pressure Turn`,
`Melodic Drive`, and `Full Statement` as strange, unsatisfying tunes that did
not read as Boss music. The next question is therefore smaller than complete
form:

> Which continuation is memorable, sounds like a Boss tune, and forms a
> natural next sentence after Finding Footing?

The exact Melodic Throughline audio remains the direct listening control at
`Music Legacy/officewars-boss-a-melodic-throughline-audition.html`. The
Approved rollback remains unchanged at
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`.

## Musical Contract

Each candidate totals `312` eighth-note steps at `168 BPM`, approximately
`0:55.7`:

1. `Challenge Issued` - `128` shared steps;
2. `Finding Footing` - `88` shared steps; and
3. `Candidate Continuation` - `96` candidate-specific steps.

The first `216` steps are exact shared context. `Finding Footing` retains one
deliberate eight-step breath and no other pause longer than four steps.

All three continuations share:

- the bright triangle Player lead with soft sine-octave support;
- the Player as foreground protagonist;
- the same galloping Boss bass and broad backbeat;
- the same low rising Boss pressure contour;
- comparable harmony density and loudness target; and
- a cadence on MIDI `74` before returning to the loop opening.

Only melody, supporting harmony, and cadence route change as one coordinated
candidate identity:

- Candidate A: three `32-step` phrases, `31` attacks, MIDI `86` apex;
- Candidate B: six `16-step` phrases with changed endings, `43` attacks,
  MIDI `86` apex; and
- Candidate C: two `48-step` sentences, `26` attacks, MIDI `88` apex.

The listening page reveals only neutral A, B, and C labels. No candidate or
complete Boss form is selected.

## Artifacts

- Active Test:
  `prototypes/officewars-boss-a-tune-discovery-audition.html`
  - SHA-256:
    `EA490615C007AEB059C37790ABB238494C94F23D72AF3FC14ADBCFDFCABF0A9A`
- Embedded Candidate A WAV:
  - SHA-256:
    `D6D2312DC123D9B2B82BFD19487FF9040B632F912CF56F59006A80884453103C`
  - byte length: `5348616`
- Embedded Candidate B WAV:
  - SHA-256:
    `419F2BB01CF26A8140B0C738732F4594EB8C5A02D6B82498ABBA44FC599FC827`
  - byte length: `5348616`
- Embedded Candidate C WAV:
  - SHA-256:
    `CA4777A4496D1E41F4D948EED6684AC36225B1376C150B6C79195A7D82274F56`
  - byte length: `5348616`
- Checked source generator:
  `.officewars-build-boss-tune-discovery-source.ps1`
  - SHA-256:
    `6D10B37C3D202C71961B91C32320338D21D9F6F8FD87A3F47024105FDB603C84`
- Render and source-contract driver:
  `.officewars-render-boss-tune-discovery.py`
  - SHA-256:
    `6389BC408C7811335182B945FCAE08E25384108994DE6E539E909E9D05A13851`
- Standalone packager:
  `.officewars-package-boss-tune-discovery.ps1`
  - SHA-256:
    `9F40C78B4A1A6506CA262804CCD4D0B24172002494CE37626A8C6779A640FAA0`
- Focused verifier:
  `.officewars-boss-a-tune-discovery-verify.py`
  - SHA-256:
    `2C2C619D745BD2298FADB156207A721A5FEB6EDB23AC343FCB7ADE823C96FBE4`
- Retag helper:
  `.officewars-retag-boss-melodic-throughline-control.ps1`
  - SHA-256:
    `B8728B9C7762AB413256621BBB32B5CB783A0A88B020209303C2C76D140E65D6`
- Retained Melodic Throughline control:
  `Music Legacy/officewars-boss-a-melodic-throughline-audition.html`
  - wrapper SHA-256:
    `7EA17F521AEFA9772C9BC7A82F357819098901B70563A39DF41EBBF959B332B5`
  - embedded audio SHA-256:
    `DF60B8A506EAF48D52A924A9CEF10D797A3957A02C0FBC414EC5BD0425CBEE1D`
- Protected Approved rollback:
  `Music Locked/officewars-boss-a-windowed-percussion-audition.html`
  - SHA-256:
    `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`
- Unchanged game:
  `officewarsautobattler.html`
  - SHA-256:
    `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`

## Verification

Pass:

- the hash-pinned generator refuses drifted protected source dependencies and
  produces three deterministic `312-step` render sources;
- source metadata proves exact shared Player and Boss context through step
  `216`, one deliberate pause, distinct candidate melodies, declared phrase
  geometry, apex, attack count, and cadence;
- all three renders are `24kHz`, stereo, `16-bit`, `1337143` frames, and
  `5348616` bytes;
- after the inherited `250ms` loop-tail state, all three shared contexts and
  the Melodic Throughline control differ by at most one PCM
  least-significant bit with more than `99.95 percent` exact samples;
- continuation RMS is comparison-safe at `0.00741216`, `0.00732616`, and
  `0.00741397`;
- Candidate A waveform peak `0.052948`, maximum adjacent-sample delta
  `0.007874`, and seam delta `0`;
- Candidate B waveform peak `0.052734`, maximum adjacent-sample delta
  `0.007874`, and seam delta `0.000031`;
- Candidate C waveform peak `0.047485`, maximum adjacent-sample delta
  `0.008240`, and seam delta `0`;
- one standalone HTML embeds all three exact WAVs and has no external script
  or media dependency;
- visible UI exposes only neutral A/B/C candidate labels;
- live waveform pixels, play, pause, resume, stop, seeking, and all three
  direct context starts;
- `30` rapid candidate switches retain one AudioContext graph and one
  MediaElementSource;
- desktop and portrait layouts have no horizontal overflow;
- each candidate completes two uninterrupted normal-speed `0:55.7` loops
  while playback remains active;
- final stop rewinds cleanly with no browser console or page errors;
- the final Rejected Melodic Throughline wrapper retains the exact embedded
  control audio; and
- no game integration.

Technical verification makes the anonymous comparison ready for human
listening. It does not select a tune or approve a complete Boss form.
