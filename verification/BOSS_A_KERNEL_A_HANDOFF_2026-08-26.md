# Boss A Kernel A Handoff Extension Branch

Date: 2026-08-26

## Why This Branch Exists

The user's extension rule states that promoting a partial track to `Approved`
also opens, in `prototypes/`, the next version of that track carrying the
extension, repeating until the track is complete, at which point it becomes
`Completed` in `Music Official/`.

`OW-MUSIC-BOSS-A-KERNEL-A-RESPONSIVE-ENSEMBLE` is eight bars, so it is a partial
track and owed such a branch. The obligation was first recorded as outstanding
rather than satisfied, because the branch's musical content depends on which open
question the user chooses and inventing that content is prohibited. The user then
selected the handoff from `Challenge Issued`, which this branch answers.

## Audition Contract

`OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF` is `Test` at
`prototypes/officewars-boss-a-kernel-a-handoff-audition.html`. It asks exactly
one question: does the joint between `Challenge Issued` and Kernel A need a
composed bar of preparation?

| | `Direct` (control) | `Prepared` |
|---|---|---|
| steps | 192 | 200 |
| duration | `34.286 s` | `35.714 s` |
| theme entry | step 128, `22.857 s` | step 136, `24.286 s` |
| seam bars | 0 | 1 |
| saw / triangle events | 82 / 37 | 85 / 39 |

`Direct` is selected on load so the control is heard first.

### Held Constant

- The opening's 128 steps are re-derived at build time from the verified render
  source `.officewars-boss-a-tune-discovery-c-render-source.html`. The build fails
  if the render's `identity`, `callbacks`, `chords`, or `roots` differ from the
  transcription, and the bass, chord hits, kick, snare, and reduction are computed
  from the render's own `scheduleRhythm`, `scheduleHarmony`, and callback-priority
  merge rules rather than transcribed.
- The protected triangle entry is `[[64, 72]]`, which is `11.429 s`. Unchanged.
- The Approved kernel is carried forward in all eleven event fields: `saw`, `tri`,
  `reduction`, `chords`, `roots`, `intensity`, `bass`, `chordHits`, `kickSteps`,
  `snareSteps`, `kickExtra`, plus its chord names.
- Palette, the resilient `skip-overdue` scheduler, all five monitors, and the Web
  Audio graph are unchanged from the Approved parent.
- Between the two candidates, only the seam differs. The opening is identical in
  all seven event fields, and the kernel is identical in all seven modulo the
  8-step shift, with `kickExtra` differing only by the seam's own pickup.

### What Is New

One bar, steps 128 to 135, and one melodic pitch.

- Harmony is `E7`, asserted at build time to equal the kernel's own bar-4 chord
  `[52,56,59,62]` and root `40`, so the joint reads `G7 → E7 → Am7`.
- Saw walks the `E7` arpeggio down, `E5 D5 B4`.
- Triangle leads in on `G#4 B4`, and the theme still enters on `A4`, which those
  two notes enclose.
- Bass approaches `E2 B2 G#2`, leaving `G#2` unresolved so the theme's own `A2`
  downbeat answers it. That is the resolution the kernel later refuses in its
  bar 4.
- Intensity is `0.76`, between the opening's `0.72` and the kernel's `0.78`, so
  level is monotonic across the joint.
- `G#4` (MIDI 68) is the only pitch absent from both Approved artifacts, and it is
  already present in the seam's own harmony.

### Engine Change

One backward-compatible feature. `chordHits` gained an optional fifth element that
slices off the lowest voices:

```js
const voiced = hit[4] ? sketch.chords[hit[1]].slice(hit[4]) : sketch.chords[hit[1]];
```

This is how `Challenge Issued` answers its own downbeat, on local step 6 of every
bar. Four-element hits are unaffected, and the Approved kernel uses none, so its
harmony is unchanged. The browser test confirms the slice is really taken: 16
sliced hits in `Direct` and 17 in `Prepared`, each voicing three notes, against 35
and 36 full hits.

The intensity-tier bookmark was replaced by handoff-aware marks, and four seam
geometry fields were added to the `sketchInfo()` field projection so the tests can
see them.

## Verification

| check suite | result |
|---|---|
| `.officewars-boss-a-kernel-a-handoff-verify.py` | 164 of 164 Pass |
| `.officewars-boss-a-kernel-a-handoff-browser.py` | 102 of 102 Pass, on two consecutive runs |
| `.officewars-music-catalog-verify.py` | Pass, `0 Completed / 14 Approved / 3 Test / 0 Limbo / 45 Rejected` |
| deterministic rebuild | reproduces the pinned page hash |

The static verifier is deliberately independent of the generator. It re-derives
the opening from the render source and the kernel from the Approved page, and
compares **parsed numbers, not text**, because the generator reformats numeric
literals such as `1.40` into `1.4`.

Static coverage includes the three protected hashes, `prototypes/` placement,
LF-only bytes, a single inline script, an `esprima` parse, absence of embedded
audio, exactly two candidates, per-candidate geometry and chord-hit bar
alignment, the `E6` ban, the opening's nine derived fields, the protected triangle
entry, the eleven carried-forward kernel fields, only-the-seam-differs across
seven fields plus `kickExtra`, the seam's harmony, melody, bass, and hits, the
single new pitch, monotonic level at the joint, page wiring, and seven required
disclosure phrases.

Browser coverage includes `selectionInfo()` fields, both candidates exposed, apex
`C6` at step 106 for both, tab and table rendering, the voicing-slice counts,
bookmark ordering and coverage, all five monitors against both candidates, the
joint entered directly at step 124, seek-range updates on selection, monitor
audibility and headroom, deterministic proof that the support monitor really drops
the melody voices, mid-playback candidate switching, a 38-second full loop of
`Prepared` with zero skipped steps, source release after stop, and no horizontal
overflow at 420 px.

### Lifecycle Pins That Had To Move

Opening a Boss Test broke seven artifacts that had pinned an empty Boss Test slot
as their expected state. None of these was a defect in this branch; each had
recorded a true snapshot that the user's extension rule then contradicted. All
were corrected to assert the current state rather than relaxed:

| artifact | was | now |
|---|---|---|
| `.officewars-boss-a-kernel-a-static-repair-verify.py` | `boss_prototypes == []` | equals the handoff branch |
| `.officewars-boss-a-identity-kernel-verify.py` | `boss_prototypes == []` | equals the handoff branch |
| `.officewars-boss-a-intensity-3-repair-verify.py` | `boss_prototypes == []` | equals the handoff branch |
| `.officewars-boss-a-palette-check-verify.py` | equals the static repair | equals the handoff branch |
| `Inbox/Drop/Claude Music Versions/claude-music-version-manifest.md` | "There is no active Boss Test" | names the branch and that it does not compete |
| `.officewars-music-source-claude-alignment-verify.py` | expected the static-repair label | expects the handoff label |
| `.officewars-music-guide-second-brain-verify.py` | three stale `TRUTH_DOC_HASHES` pins | repinned |

The check that the *only* Boss Test present is the sanctioned extension branch
preserves the original intent, which was that a resolved Test must not linger in
`prototypes/`. Two of these were already failing before this branch existed: the
palette-check verifier still expected the static repair, which the promotion had
moved to `Music Legacy/`, and the alignment verifier still expected the
static-repair label, which the manifest had already dropped.

### Suite Result After Synchronization

| verifier | result |
|---|---|
| `.officewars-boss-a-kernel-a-handoff-verify.py` | 164 / 164 |
| `.officewars-boss-a-kernel-a-handoff-browser.py` | 102 / 102, two consecutive runs |
| `.officewars-boss-a-kernel-a-responsive-ensemble-verify.py` | 66 / 66 |
| `.officewars-boss-a-kernel-a-ensemble-verify.py` | 60 / 60 |
| `.officewars-boss-a-kernel-a-static-repair-verify.py` | 65 / 65 |
| `.officewars-boss-a-identity-kernel-verify.py` | 95 / 95 |
| `.officewars-boss-a-intensity-3-repair-verify.py` | 81 / 81 |
| `.officewars-boss-a-palette-check-verify.py` | 53 / 53 |
| `.officewars-music-catalog-verify.py` | Pass |
| `.officewars-music-source-claude-alignment-verify.py` | 120 / 120 |
| `.officewars-agent-guidance-verify.py` | 16 / 16 |
| `.officewars-music-guide-second-brain-verify.py` | 227 / 0 |
| `.officewars-vault-foundation-verify.py` | 313 / 0 |

The three older Boss browser tests were checked for stale page paths and already
point at `Music Legacy/` and `Music Locked/` correctly, so the promotion sweep
repathed them. This suite is the music and lifecycle set, not a full
verification; the gameplay verifiers were not run and the game was not touched.

### Mirror Synchronization

Nine root documents changed, so their mapped copies were resynchronized as exact
bytes: eight shared documents into both mirrors, plus the rollout mirror's
second, root-level copy of the handoff. This verification record is new in both.
`prototypes/README.md` and `Music Locked/README.md` are root-only because
neither mirror carries those folders.

`officewars-public-repo-2026-08-07/README.md` and its `CONTRIBUTING.md` differ
from root deliberately — they carry the play-only license text — so they were
left alone rather than overwritten. Mapped-copy equality afterwards is 165 of 165
for the rollout mirror and 175 of 175 for the public mirror, 0 drifting, with
those 2 files counted as intentionally divergent rather than as matches.

The public ZIP was **not** rebuilt, so it is stale against these documents. That
rebuild is not approved.

### Mutation Tests

Three classes of deliberate defect were injected into the built page and each
produced the expected failures, so the verifier bites rather than merely passing:

1. altered seam music;
2. altered carried-forward opening bass, which failed both the render-rule check
   and the cross-candidate identity check; and
3. removed disclosure text.

### Level Methodology Correction

A monitor's level ordering cannot prove that the monitor mutes a voice on this
page, and two successive corrections were needed to establish that.

An initial browser check compared the `full` and `support` monitors from single
`levelInfo()` samples. That is invalid: `rmsAverage` is a one-pole smoothed
**instantaneous** reading with roughly a 60 ms time constant, and `peakHold` decays
by `0.93` per meter read, so single samples compare two arbitrary short windows
rather than the takes. The check was changed to poll 30 times across a fixed
3-second window and compare maxima.

That was still wrong, and it failed on a later run with `support` RMS `0.16831`
against `full` RMS `0.15726`. The cause is structural, not statistical: the
analyser is connected **after** a `DynamicsCompressorNode`
(`calibrationGain → compressor → analyser → destination`), so the denser mix is
compressed harder and a strict subset of the voices can legitimately measure
louder. Polled maxima also still depend on sampling phase.

Level checks are therefore now limited to what they can support — each monitor is
audible and neither clips — and the muting itself is proven by peak source counts,
which are deterministic: `full` creates 20 concurrent sources and `support` creates
14, identically on both runs. Measured levels across those two runs were `full`
RMS `0.16454` and `0.16316` against `support` RMS `0.14889` and `0.16471`, which is
exactly the instability that makes the level ordering unusable as evidence.

The same invalid single-sample level comparison existed in
`.officewars-boss-a-kernel-a-responsive-ensemble-browser.py`, the Approved
parent's own browser test. It was corrected on 2026-08-26 in the same way: level
checks now poll 26 times across a fixed window and assert only audibility and
headroom, and the muting is proven by peak source counts. That test now passes
`53/53` on two consecutive runs, `full` creating 22 concurrent sources against
`support` creating 14 identically on both, while measured `full` RMS drifted from
`0.20310` to `0.20923` between the runs -- the same instability that makes level
ordering unusable as evidence.

One honest qualification: on this page the old ordering check did pass both
times before the change, `support` `0.19254` against `full` `0.20310`. The
correction removes luck; it did not catch a live failure here. On the handoff
page it had genuinely failed.

## Disclosed Confounds

The page's own "Read this before judging" panel states all of these to the
listener:

- the candidates are **not the same length**, differing by `1.43 s`, and that is
  inherent to the treatment rather than removable;
- the opening is **re-realized, not copied** — this page's engine renders it, with
  per-instrument gains within about `0.4 dB` of the render;
- `G#4` is the one new melodic pitch and the first thing to question if the seam
  sounds foreign;
- the melodic ceiling `C6` is reached in the **opening**, at about 55 percent of
  the joined piece, so the kernel only matches it rather than exceeding it; and
- automated verification is not listening.

## Provenance Precision

The page states that it carries the Approved kernel forward **note for note**, not
byte-identically. The distinction is real: the generator reformats numeric
literals, so the arrays are numerically equal to the Approved parent while not
being the same bytes. `auditionSourceHash` records the parent's exact bytes,
`82ADD7D07E61B8E64236B25B73CF77FFB81A3A0FEB9B4172F8723F00D425C570`, as the source
the numbers were taken from.

## Hash Ledger

| artifact | SHA-256 | bytes |
|---|---|---|
| `prototypes/officewars-boss-a-kernel-a-handoff-audition.html` | `C797C819F0AF086E826A74D050A4881C2761A2AB29504297B24EB8F62BA5DAB4` | 75258 |
| `.officewars-python/build_boss_a_kernel_a_handoff.py` | `81312FB980FA43DBA7B0CC316074E77C7BB14019476E6810F7887790BA7E24CE` | 29485 |
| `.officewars-boss-a-kernel-a-handoff-verify.py` | `BD1C66FE09A30400CCD49E4287B94AFC2184AC6B15C102BEFCCE26E6052A0BF9` | 18249 |
| `.officewars-boss-a-kernel-a-handoff-browser.py` | `3D40135C07018C96B5FF7C7F35E36F2D4B855DA1D6B1626C5AE223ED311DDDD1` | 12914 |
| `.officewars-boss-a-kernel-a-responsive-ensemble-browser.py` | `7CEC43558AABAF8D499B50D2F1825C9E5D84D3C3A88050D7EB3D630CD7C9D959` | 8765 |

Protected bytes confirmed unchanged:

| artifact | SHA-256 |
|---|---|
| `officewarsautobattler.html` | `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A` |
| `Music Locked/officewars-boss-a-windowed-percussion-audition.html` | `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C` |
| `Music Locked/officewars-boss-a-kernel-a-ensemble-audition.html` | `82ADD7D07E61B8E64236B25B73CF77FFB81A3A0FEB9B4172F8723F00D425C570` |

## Not Established

No candidate is selected. Nothing here was heard by a human; source analysis and
automated playback are not listening, and technical verification is not approval.

The apex question is untouched: the joined form still peaks in its opening, so
whether the continuation needs a later or higher apex is open. Whether `Prepared`
is preferable because it prepares, or merely because it is longer, cannot be
separated within this treatment.

Kernel A remains a partial track. Settling the handoff does not complete it, so
the next extension branch will still be owed once a treatment is selected.
Harmonic destination and cadence, longer form, whether the `3.6 dB` intensity ramp
can be reduced, and game integration all remain open.
