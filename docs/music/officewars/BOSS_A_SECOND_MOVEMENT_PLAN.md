# Boss A Second Movement — Register And Function Plan

Status: Approved drop stage. Kernel A is the selected identity-kernel
foundation because it felt most energizing. Its scheduler repair, its responsive
ensemble, its handoff from `Challenge Issued`, its triangle balance, and its
melodic ceiling are all settled by human listening. One Boss Test is open, the
drop-cadence branch. The current baseline and branch are recorded in
`docs/music/officewars/README.md` and
`docs/music/officewars/MUSIC_CATALOG.md`, which govern if this plan disagrees.

Sketches A and B are liked, Sketch C is not, B's bar-5 gear change is rejected,
and the offbeat percussion was rejected as metronomic. B2 answered the gear
change, but its `Intensity 3` region is rejected because the upper voices clash
with themselves, and E6 is not liked in this track. Two further rounds were then
rejected: the focused repair for having no tune and a bar 1 that never paid off,
and the flow continuation for straying from melody and from the idea of a boss
fight.

**The redo scope and the bar 1 seed are now both freed by approved user
decision.** Everything after the opening may be newly written; `Challenge
Issued` stays exactly as it is. The bar 1 rising fourth is no longer a required
starting point, so the register-and-function planning below applies to whichever
theme survives listening rather than to a continuation of that cell.

The most recent audition is Rejected history at
`Music Legacy/officewars-boss-a-bare-theme-audition.html`
(`OW-MUSIC-BOSS-A-BARE-THEME`). T1-T4 disappointed in both Bare melody and Full
ensemble. The ensemble was noticeable but did nothing to support the melody.

Its byte-pinned derivation source is now Rejected history at
`Music Legacy/officewars-boss-a-intensity-3-repair.html`.

The exact A/B/B2/C predecessor is Rejected history at
`Music Legacy/officewars-boss-a-second-movement-sketches.html`.

Approved companion artifact:
`Music Locked/officewars-boss-a-kernel-a-ensemble-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-RESPONSIVE-ENSEMBLE`, `Approved`). Its two resolved
predecessors are Rejected controls at
`Music Legacy/officewars-boss-a-kernel-a-static-repair.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-STATIC-REPAIR`, the only remaining stacked-scheduler
control) and
`Music Legacy/officewars-boss-a-kernel-a-ensemble-comparison.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-ENSEMBLE`, the only remaining uniform-accompaniment
control).

## 1. What This Plan Replaces

Fourteen rejected attempts have extended the Approved opening by recombining its
own phrases. The immediately preceding Test, now Rejected at
`Music Legacy/officewars-boss-a-next-movement-audition.html`, made that method
explicit in its own contract field: `openingTemplateUse:
'recombined-contours-rhythms-cadences-and-role-transfers'`. All three of its
candidates shared one borrowed melodic cell, so no candidate could win.

This plan changes the method rather than the parameters. Ancestry travels
through harmony, bass, groove, register, and cadence. Melody is newly written.

## 2. The Opening's Plan, Measured

Read from `BOSS_A` in `.officewars-boss-a-tune-discovery-c-render-source.html`.
This is the reference the second movement must answer, not copy.

| Property | Value |
|---|---|
| Tempo | 168 BPM, 1 step = 1/2 beat = 0.178571 s, 8 steps per bar |
| Length | 128 steps, 22.857 s, 16 bars |
| First note | G4 (67) |
| Apex | C6 (84) at step 106 = 18.93 s = **83% through** |
| Final note | C5 (72) |
| Range | G4–C6, 17 semitones |
| Largest interval | 5 semitones (G5→C6 at steps 104–106) |
| Note events | 79 across two voices = 0.62 per step |
| Harmony | Am7 – Fmaj7 – Cmaj7 – G \| Am7 – Dm7 – Fmaj7 – **G7**, twice |
| Voices | `identity` (broad saw) and `callbacks` (bright triangle), two independent lines |
| Triangle entry | step 64 = **11.429 s**, protected |

Voice layout across the opening:

```
steps   0- 63   saw alone, establishing the hook
steps  64- 95   triangle leads its own line; saw plays its own line underneath
steps  96-111   saw alone, climbing to the C6 apex
steps 112-127   triangle closes; saw interjects C6 and B5 above it
```

Two facts from this table drive everything below.

- **The peak arrives late.** 83% through. A continuation that peaks in its
  first half reverses the shape the opening taught the listener to expect.
- **Both voices are real lines.** Neither is a decoration of the other, and
  neither is one melody handed between two timbres.

## 3. Retired Constraints

These were enforced by prior rounds. None came from the user. All are retired
for this plan, with the reason each was wrong.

| Retired constraint | Where it was enforced | Why it is retired |
|---|---|---|
| Apex must not exceed MIDI 81 | `.officewars-boss-a-next-movement-verify.py:284`, `developmentalReserveMaxMidi == 81` | The opening's own apex is 84. A continuation capped below the opening's ceiling cannot escalate. Earlier rounds the user called "closer" reached 84 to 88. |
| Pitch vocabulary limited to `{67,69,72,74,76,77,79,81}` | Candidate note tables | Excludes 83 and 84, the opening's top two pitches, so the opening's climax gesture could be quoted but never completed. |
| Zero deliberate pauses | `deliberateLongPauseCount:0` | The user's complaint was that one specific movement was pause-heavy, not that breath is forbidden. One deliberate breath per movement is allowed again. |
| Attack gaps no greater than 4 steps | `maxAttackGap` assertion | An agent quantification of the same complaint. The opening's own gaps never exceed 3 steps, so this rule never constrained the opening — only its continuations. |
| One melody time-sliced between two timbres | `routeNextMovement()` in `.officewars-build-boss-next-movement-source.ps1:136-153` | Produces two half-lines, not two voices. Density fell to 0.38–0.45 events per step against the opening's 0.62. |

**Implementation note on lifting the apex cap.** The `== 81` assertion in
`.officewars-boss-a-next-movement-verify.py` is deliberately left in place. That
verifier is the recorded evidence for the now-Rejected
`OW-MUSIC-BOSS-A-NEXT-MOVEMENT-DISCOVERY` artifact, and editing it would
invalidate that artifact's documented hash without improving anything. The cap
is lifted by not applying it: the sketches below reach 84, 88, 88, and 88, and
this table plus `docs/BALANCE_LEDGER.md` are the authoritative record that the
constraint is withdrawn.

The audition has since been retired to
`Music Legacy/officewars-boss-a-next-movement-audition.html`. By this project's
established convention only the audition HTML moves on a lifecycle change; every
retired artifact's generator, renderer, packager, and verifier stays at the
workspace root as an inert dotfile. Those four files are no longer active
tooling and no longer govern anything.

## 4. Rules For This Round

1. **No verbatim quotation.** No sketch may reproduce a phrase of the opening
   in both pitch and rhythm, and no two sketches may share a phrase. Ancestry
   comes from harmony, bass, groove, and cadence. This is a discovery-round
   safeguard, not a permanent ban on selective callbacks later in the cue.
2. **Two independent lines.** Each sketch has a separate saw sequence and a
   separate triangle sequence, each singable on its own. No timbre change
   inside a phrase. This proves that the current sketches are not one chopped
   solo; it does not require both voices to remain equally active in every
   phrase of the eventual complete cue. Player identity may move through the
   ensemble while the triangle remains a bright selective marker.
3. **One declared function per sketch.** A sketch is an answer to "what does
   this movement *do*", not a rearrangement of the same material.
4. **Restored harmony.** The dominant is **G7** `[55,59,62,65]`, not the
   doubled-root `[55,59,62,67]` the last round substituted. `Dm7` stays in the
   mid register at `[62,65,69,72]`.
5. **Harmonic rhythm changes.** Each sketch departs from the opening's
   unvarying eight-bar loop in a way that matches its function.
6. **Audible escalation.** Intensity spans at least 2.5 dB across the sketch,
   against the last round's 1.3 dB.
7. **Standalone first.** These are heard alone. Nothing is spliced onto the
   opening and nothing is baked into a large artifact until one direction
   survives listening.

## 5. The Sketches

Each is a self-contained loop of 8 to 12 seconds. A, B, and C are deliberately
different in function, hook, rhythmic signature, register plan, and groove. B2
is a declared revision of B that changes melodic motion and nothing else.

**Listening verdict, first pass.** A and B are both liked. B's opening is
preferred to A's. B's bar-5 gear change and stepwise climb are rejected. C is
rejected outright. The offbeat percussion, common to all of them, was rejected
as sounding like a metronome; see Section 8.

Nothing was removed in response. C stays playable as the rejected control, B
stays unchanged as the control for its own revision, and B2 is the only new
material.

### Sketch A — pressure without ascent

**Verdict: liked.** Kept unchanged apart from the shared percussion fix.


- **Function.** Raise pressure while refusing to climb. The engine gets more
  insistent; the melody stays where it is.
- **Length.** 48 steps, 6 bars, 8.57 s.
- **Hook.** Three hammered consecutive eighths, then a step away. The opening
  never plays two consecutive eighths — its minimum gap is 2 steps — so this
  rhythm cannot be mistaken for quotation.
- **Register plan.** Saw hammers in A4–G5 and never leaves it. Triangle answers
  in E5–C6. Apex C6 (84) at step 27, 56% through. Ends on D5 over G7.
- **Apex choice.** Matches the opening's ceiling of 84 and deliberately does
  not exceed it. This sketch's function is pressure, so exceeding the ceiling
  would contradict it.
- **Harmony.** Am7 – Dm7 – Fmaj7 – G7 – Am7 – G7. Six bars instead of eight, so
  the turnaround arrives early and repeatedly. That shortened cycle is the
  harmonic form of pressure.
- **Groove.** Shortest bass notes (0.62 of a step), heaviest bass gain,
  frequent sixth-beat kick.
- **Internal shape.** Bars 1–3 hammer and rise by thirds; bar 4 breaks the
  hammer with a held note so the pattern does not become mechanical; bar 5
  returns with a compressed two-hit hammer; bar 6 walks down to the cadence.

### Sketch B — escalation past the opening's ceiling

**Verdict: opening liked, bars 5–7 rejected.** Retained unchanged as the control
for Sketch B2.

- **Function.** Go higher than the opening went, and arrive late.
- **Length.** 56 steps, 7 bars, 10.0 s.
- **Hook.** A rising perfect fourth followed by a step down, transposed
  upward. The opening's largest interval is 5 semitones and it never uses a
  fourth as a repeating cell.
- **Register plan.** Saw spans A4–D6 (86), starting on C5, dipping to A4 in bar
  2, then climbing. Triangle spans F5–E6 (88) and breaks the ceiling first. Saw
  apex D6 at step 43, 77% through; triangle apex E6 at step 44, 79% through.
  Ends on F5 and A5 over G7 — the seventh, left unresolved so the movement
  clearly wants a successor.
- **Harmony.** Am7 – Fmaj7 – Dm7 – G7 – Cmaj7 – Fmaj7 – G7. Seven bars, and
  the Cmaj7 in bar 5 is the lift under the highest writing.
- **Groove.** Middle settings. The escalation lives in pitch and intensity, not
  in the drums.
- **Internal shape.** Bars 1–4 sequence the fourth cell upward; bar 5 abandons
  the cell and climbs by step, which is the gear change; bar 6 is the apex; bar
  7 descends to an unresolved dominant.
- **Reservation to settle before this direction is locked.** If the second
  movement reaches E6 at ten seconds, later movements have little room left to
  climb. Either the cue's climax belongs here and later movements develop
  differently, or this sketch's ceiling should come down. That is a form
  decision, and it is open.

### Sketch B2 — escalation by sequence, not by scale

**Answers the rejected gear change.** This is a revision of B, not a fifth
independent idea, and the page declares it as one.

- **What is unchanged.** Bars 1–4 are Sketch B verbatim — the same first 13 saw
  events. Length, harmony, roots, intensity and groove are identical to B. The
  page's gate tool asserts all of that, so melodic motion from bar 5 onward is
  the only variable between the two.
- **What changed.** B's bar 5 (`77 79 81 83`) is pure whole-step motion and its
  bar 7 (`83 81 79 77`) a pure step descent. Those are the gear change and the
  stepwise climb. B2 removes both by continuing to do what bars 1–4 already do:
  transpose the rising fourth upward. The longest unbroken run of step motion
  falls from 6 notes to 2.
- **Register plan.** Saw reaches D6 (86) at step 43; triangle reaches E6 (88) at
  step 49, **88% through** — later than the opening's own 83%. The close inverts
  the hook into a falling fourth rather than a scale, so the movement ends by
  answering its own idea.
- **Watchpoint, not an objection.** B2 inherits B's ceiling of E6, so the open
  form question in Sketch B's reservation applies to it unchanged: if the second
  movement reaches E6 at ten seconds, later movements have little room to climb.

### Sketch C — role reversal

**Verdict: rejected.** Retained playable as the control for the role-reversal
idea; it is the reference for what "Player leads" sounded like if that question
returns.

- **Function.** Give the movement to the Player voice. The triangle leads, the
  saw comments.
- **Length.** 64 steps, 8 bars, 11.43 s.
- **Hook.** A syncopated rising sixth. The opening's largest interval is 5
  semitones, so an 8 or 9 semitone leap is unmistakably new material. Every
  triangle phrase begins on an odd step, so the Player is always off the beat.
- **Register plan.** Triangle covers B4 → E6 (88), apex at step 51, 80%
  through — the closest match to the opening's own 83%. Saw makes a slow
  counter-ascent from A4 up to G5, dipping to G4 in bar 1, entirely on even
  steps. Both voices land together on D5.
- **Counterpoint.** The two voices never attack on the same step. Triangle
  events are all odd, saw events all even. That guarantees two audibly separate
  lines and is the direct structural answer to the split-line defect.
- **Harmony.** Am7 – Am7 – Fmaj7 – G7 – Cmaj7 – Am7 – Dm7 – G7. The repeated
  Am7 opening gives the Player room to establish itself before the harmony
  starts moving every bar.
- **Groove.** Longest bass notes, lightest bass gain, sparsest kick, so the
  Player has space.
- **Character source.** The user's earlier description of the Player voice:
  high, light, cheerful, loud, syncopated, and emotionally open.

## 6. Comparison Table

| | A | B | B2 | C |
|---|---|---|---|---|
| Verdict | liked | opening liked, bars 5–7 rejected | answers the rejection | rejected |
| Function | pressure, no ascent | escalation past 84 | escalation by sequence | role reversal, Player leads |
| Steps / seconds | 48 / 8.57 | 56 / 10.0 | 56 / 10.0 | 64 / 11.43 |
| Hook | 3 hammered eighths | rising fourth chain | rising fourth chain, sustained | syncopated rising sixth |
| Rhythmic signature | consecutive eighths | 3-step cell | 3-step cell | all-odd-step entries |
| Leader | saw | saw, triangle above | saw, triangle above | triangle |
| Apex | 84 at 56% | 88 at 79% | 88 at 88% | 88 at 80% |
| Final note | D5 | F5 / A5, unresolved | F5 / A5, falling fourth | D5, both voices |
| Harmonic cycle | 6 bars | 7 bars | 7 bars, same as B | 8 bars, slow start |
| Intensity span | 0.82–1.18, 3.2 dB | 0.78–1.24, 4.0 dB | 0.78–1.24, 4.0 dB | 0.86–1.16, 2.6 dB |
| Longest step run | — | 6 notes | 2 notes | — |

No sketch shares an eight-note run with the opening. A, B, and C share no run
with each other. B and B2 share bars 1–4 by design; that is the one declared
exemption, and the gate tool requires the page to declare it.

## 7. What Is Deliberately Not Done Yet

- **No splice onto the opening.** The seam is composed only after a direction
  survives standalone listening. The user confirms that a future Test may use
  DJ-style phrase-matched overlap logic: the exact Approved opening events stay
  unchanged while one additive pickup or dominant approach from the incoming
  movement enters during the opening's final bar. The Approved rollback file
  remains byte-identical. The overlay may foreshadow the chosen hook but may
  not rewrite or replace an opening note.
- **No baked render.** The sketch page synthesizes live, so it is kilobytes
  rather than megabytes and can be revised in seconds.
- **No mix rebuild.** The measured render problem — 57% of energy below 120 Hz,
  85% below 500 Hz, RMS around 20 dB under a usable target — is a separate
  non-musical task. The sketch page exposes a boost control and a live level
  readout so loudness can be discussed with numbers instead of another
  "raise it 30%" round, and an optional low-shelf trim that is **off by
  default** so the sketches are judged on the Boss cue's established tone.

## 8. Percussion — The Reported Metronome

Listening reported that the offbeat percussion sounded like a metronome and
asked whether that sound could be replaced. It could, and the replacement was
already inside the cue the user likes.

**What was wrong.** The offbeat layer was a pitched square oscillator at MIDI 89
(F6, about 1397 Hz), 35 ms long, on **every odd step**, at a constant gain of
`0.0038` that was never scaled by intensity, at an identical pan every hit.
Three independent properties each pushed it toward reading as a machine:

- a pitched square timbre, which gives every hit the same recognizable note;
- perfectly even subdivision, which is literally what a metronome does; and
- a level that never breathes, so the layer does not participate in the
  escalation happening around it.

**Root cause.** The Approved cue's percussion scheduler has two branches. The
sketch page had copied the **non-brush fallback**, not the branch the cue
actually plays. This was a porting error, not a design decision — the fix did
not require inventing a new sound.

**What it is now.** The Approved cue's own `playPaperBrush`: windowed noise
rather than a pitched tone, placed on the cue's own alternating figure
`[1, 3, 6]` then `[1, 4, 7]` rather than on every odd step, with the bandpass
moving in four steps, the noise offset in seven, and the pan alternating, so no
two consecutive hits are identical. Gain is `0.005 × intensity × accent`, with
accents of 1.08 on steps 6 and 7 and 0.88 elsewhere, so the layer grows with the
escalation. The snare is likewise the cue's noise-based `playBrushSnare` instead
of a pitched-only tone. Noise is generated by the cue's seeded LCG, so every hit
is reproducible.

**The old sound is retained as a labelled rejected control.** The offbeat
selector offers Brush (default), Steady, Tick, and Off. Tick is the exact
rejected square tone, kept so the change can be A/B compared rather than taken
on trust. The gate tool asserts that Tick has exactly one call site and that it
is reachable only from that control.

## 9. Verification Evidence

Three lightweight tools replace the previous rounds' generator, renderer,
packager, and verifier chain. All run from the workspace root.

`python .officewars-sketch-gate-check.py` — **106 passed, 0 failed.**

| Gate | Result |
|---|---|
| Quotation: no 8-note run shared with the opening, in pitch or pitch-and-rhythm | Pass, all four |
| Quotation: no 8-note run shared between any two sketches | Pass. B/B2 is the one declared exemption and must declare `revisionOf` |
| Arc: apex in the last third and above MIDI 84 | Pass for B (88 at 79%), B2 (88 at 88%) and C (88 at 80%); A exempt at 84 / 56% because it declares a pressure engine |
| Counterpoint: two substantial voices, each spanning all four quarters | Pass. A saw 25 / tri 13, B saw 24 / tri 14, B2 saw 22 / tri 13, C saw 18 / tri 32 |
| Counterpoint: Sketch C's voices never attack on the same step | Pass, zero collisions |
| Revision: B2 declares its parent and holds B's length, chords, roots, intensity and groove unchanged | Pass |
| Revision: B2 keeps B's first 13 saw events verbatim | Pass |
| Revision: B2 shortens B's stepwise ladder | Pass. B 6 notes, B2 2 notes |
| Harmony: restored G7 present; doubled-root G and octave-dropped Dm7 absent | Pass, all four |
| Harmony: chord and root counts match bar counts | Pass, 6 / 7 / 7 / 8 bars |
| Escalation: intensity span at least 2.5 dB | Pass. A +3.2, B +4.0, B2 +4.0, C +2.6 dB |
| Apex cap lifted | Pass. Apexes 84, 88, 88, 88, all above the retired cap of 81 |
| Pitch vocabulary restored | Pass. Now includes 83, 84, 86 and 88 |
| Percussion: brush is the default; the five noise functions are present; the seed and the `[1,3,6]`/`[1,4,7]` figure match the verified render source | Pass, about 15 gates |
| Percussion: offbeat gain scales with intensity and is accented; the pitched-only snare is gone; the square tick has one call site behind the rejected control | Pass |
| Player UI: design tokens shared with the reference audition, all eight structural selectors, theme toggle, reduced motion, focus ring, ARIA roles, footer label | Pass, about 20 gates |
| Progress bar: anchored to a scheduled step, read from the AudioContext clock, animated, and seek quantised to the nearest step | Pass |
| No embedded Base64 or audio data URI | Pass. Page is 62 KB |
| Approved baseline hash unchanged | Pass. `0A6BC2BB…273B636C` |

`python .officewars-sketch-level-check.py` — reimplements the page's scheduler
and envelope shapes, including the brush's distinct noise envelope, and sums
per-voice amplitudes over one loop, then carries the measured Approved-cue level
across. The opening reference is scheduled through the same brush branch the
sketches now use, so the comparison is faithful.

| Sketch | Coincident peak vs the opening | Mean vs the opening |
|---|---|---|
| A | +0.75 dB | +0.71 dB |
| B | +1.21 dB | +0.96 dB |
| B2 | +0.88 dB | +0.94 dB |
| C | +0.34 dB | +0.54 dB |

All four sit within 0.9 dB of each other, so loudness is not biasing the
comparison, and within 1.3 dB of the opening, so the opening's measured level
transfers. At the default boost of 15 the worst case is about −3.3 dBFS peak and
−21.9 dBFS RMS before the compressor, with the compressor at −11 dB threshold
holding peaks. This estimator is an explicit upper bound: it sums coincident
envelope gains without phase cancellation or filtering. The browser measurement
below confirms it is pessimistic — at the top of the boost slider it predicts
about +0.1 dBFS, and the browser measured between −2.8 and −8.2 dBFS across two
runs without clipping.

`python` with `esprima` parses the page's single script block cleanly, with no
syntax errors, and every oscillator and buffer source creation site is
registered and has a scheduled stop.

### Browser Evidence

`PYTHONPATH=".officewars-python" python .officewars-sketch-browser-check.py` —
**50 passed, 0 failed.** Playwright 1.62.0 drives headless Chromium, which
renders the Web Audio graph for real, so the checks earlier rounds had to record
as Not Run are now measured. This closes that gap.

Level figures below are from one representative run. They are analyser samples
taken at a moment in the loop, so they move by a few dB between runs; the
pass/fail conditions, not the exact decibel values, are what the tool asserts.

| Check | Measured result |
|---|---|
| Analyser reads real signal | Peak 0.3842 (−8.3 dBFS), RMS −19.5 dBFS, so the graph is genuinely producing audio |
| Progress bar tracks playback | Slider drift 0.006 s against the reported position |
| Pause freezes position | 2.516 s → 2.516 s across 900 ms suspended; slider frozen with it |
| Resume continues | Position advances and level returns |
| Seek quantises to a step | Asked 5.31 s, quantised 5.357 s, resumed at 5.342 s, then continued |
| Offbeat switching | Brush, Steady, Tick and Off each apply without interrupting playback |
| Mix and tab switching | Full/reduced both ways; all four sketches audible after the switch |
| Long playback | Two complete uninterrupted loops of Sketch C, peak −5.5 dBFS, no clipping |
| Node bound | Peak 23 concurrent sources |
| Boost ceiling | Slider at 22 measured −8.2 and −2.8 dBFS on two runs, no clipping either time, against a predicted +0.1 dBFS |
| Stop | Live nodes drain to 0; progress bar and button reset |
| Replay after Stop | Works, with signal |
| Theme toggle | Light applies and dark restores |
| Narrow viewport | 0 px horizontal overflow at 420 px wide |
| Errors | No page errors, no console errors |

Two real defects were found and fixed by this run: an unbreakable inline path
token caused 41 px of horizontal overflow at 420 px, now handled with
`overflow-wrap:anywhere`, and an intensity readout rendered "+4 dB" instead of
"+4.0 dB" because the value was numerically round-tripped before display.

The only verification that still matters is listening, and it is not something
these tools can do.

## 10. Next Listening Pass

Keep all playback settings fixed:

- device volume: `50%`;
- in-page Volume: `80`;
- Boost: `15.00x`;
- Offbeat percussion: `Paper brush (Approved cue)`; and
- Low trim: `off`.

### Pass 1 - Tune And Motion

Use `Mix: Melody + pulse`.

1. B for two complete loops.
2. B2 for two complete loops.
3. B for one loop directly into B2 for one loop.
4. A for two complete loops.

Judge B against B2 as the controlled melodic-motion diagnosis. A is heard
afterward as a different pressure-function alternative, not as a third version
of the B/B2 variable.

### Pass 2 - Boss Scale And Player Identity

Use `Mix: Full ensemble`.

1. B for two complete loops.
2. B2 for two complete loops.
3. A for two complete loops.

Player identity may be carried by the ensemble while the triangle remains
selective. Do not reject a sketch merely because triangle is not the constant
lead.

If B2's motion fixes the gear change but E6 feels premature, preserve the
motion finding and reopen register separately.

## 11. Bare Theme Verdict

The bare-theme method is rejected.

1. T1-T4 disappointed in the lead-alone monitor, so the problem begins in raw
   melodic identity rather than mix thickness.
2. Full ensemble made the backing noticeable but did not make it support,
   complete, pressure, or redirect the melody.
3. Equal `32`-step lengths and one shared harmony made unlike ideas conform to
   one container instead of letting each sentence find its own duration and
   destination.
4. Numeric ancestry gates described the opening's statistics but did not
   reproduce its phrase grammar, consequence, or multi-role identity.
5. A generic backing loop cannot be added after the fact and called ensemble
   support. Muting a support role must remove a specific musical function, not
   merely make the mix thinner.

The rejected page and its derivation source remain executable historical
controls in `Music Legacy/`. Their technical verification remains valid for
their archived bytes and does not select any theme.

## 12. Identity-Kernel Planning Contract

The next compositional unit is an **identity kernel**: a short, naturally sized
musical sentence in which melody, harmonic destination, bass motion, cadence,
and a minimal ensemble relationship are composed together.

Binding constraints:

- preserve `Challenge Issued` exactly, including the triangle entry at
  `11.429` seconds;
- everything after the opening and the former bar 1 seed remain free;
- no equal-length rule, shared-harmony rule, leap quota, late-apex quota, or
  requirement that an answer out-reach its statement;
- no story-first movement labels;
- no literal alternating dialogue;
- the bright triangle may remain selective, but any claimed ensemble role must
  change what the phrase means or where it goes;
- test a coherent melody-only reduction and the coupled identity kernel; and
- do not build the next audition until independent Codex and Claude briefs are
  both available and compared.

The ratified working bundle is
`Wiki/Knowledge/Music/Approach Bundles/OfficeWars Boss A Identity Kernel - Ratified Bundle.md`.
The independent Codex and Claude briefs remain preserved evidence.

The comparison produced three approved decisions:

1. Melody-only reduction is a rejection gate, not merely a monitor. The
   distributed architecture in which no single voice carries a coherent tune is
   retired for this round.
2. Sketch A may be developed. Its hammered-eighth figure becomes the source for
   the future riff-into-sentence candidate; freeing Sketch B's bar-1 rising
   fourth did not forbid A.
3. Palette diagnosis runs before kernel composition. Exact live Sketch A is
   measured and compared through the current palette and at most one minimally
   corrected, matched-level treatment.

After the palette result, the kernel round is limited to two candidates:

- a connected sentence with consequential punctuation and overlapping voices
  that finish one another; and
- riff into sentence, developing Sketch A.

`Support only` and role-mute monitors are included in the future contracts.
Build guards against an empty declared second voice or a falsely claimed energy
arc with a constant intensity profile remain implementation safeguards, not
new musical content.

## 13. Open Questions

Two earlier questions are now answered by human listening and are recorded in
sections 16 and 17: the resilient scheduler removed the recurring static, and
Kernel A's ensemble is the responsive one.

1. What should the selected drop's unresolved `E7` resolve into, and which
   cadence treatment belongs to the track? The liked Am and C landings now each
   have an exact control and a bars 44-45 cadence repair. Payoff and Turnaround
   were removed from the active audition. No repair or destination is selected.
2. How should Kernel A hand off from Challenge Issued? Answered: the prepared
   `E7` approach bar is selected.
3. How should the Approved 328-step form extend without losing its energy?
4. Can the `3.6 dB` intensity ramp now be reduced, given that the responsive
   ensemble carries escalation structurally? Untested; the ramp was held
   byte-identical through the ensemble comparison so it could not confound the
   judgement.
5. Is `Responsive` better because it responds, or because it is denser? It has
   26 bass events against 24 and 19 chord hits against 15, so a density-matched
   control would isolate the cause. Not required by the selection, which stands.

Kernel A is eight bars, so its Approved ensemble was a partial track. Under the
extension rule each Approved section owes one `Test` branch in `prototypes/` that
carries the Approved music forward unchanged and answers exactly one question.
The user chose question 2 first, and human listening settled it by selecting the
composed `E7` approach bar. Question 3 then produced the build sentence to bar
33, where the ceiling broke to `D6`, followed by the selected eight-bar drop to
bar 41. Question 1 is now the sole active Boss branch;
questions 4 and 5 remain controlled experiments on the existing eight bars, and
neither has been approved.

## 14. Palette Test

The current live control was measured across two complete loops at Volume `80`,
Boost `15`, and Paper brush:

- Full RMS approximately `-15.9 dBFS`;
- sub-120 Hz share approximately `27.1%`; and
- `500-2000 Hz` melody-band share approximately `47.0%`.

This exonerates the retired baked-render estimate as a description of the live
page: the live melody band is not nine decibels beneath the low end.

The smallest justified treatment is therefore restrained:

- anonymous A is the exact current palette;
- anonymous B changes only a `-2 dB` shelf below `140 Hz`;
- B uses a `1.05x` disposable session trim to compensate the measured
  `0.42 dB` unmatched level loss; and
- all musical and role data remain exact.

Real-browser verification measures A/B full RMS within `0.13 dB`, with sub
share moving about `27.1% -> 21.2%` and melody-band share about
`47.0% -> 52.0%`. Full, Melodic roles, and Support only monitors each complete
two loops; 60-second playback, switching, transport, headroom, source bounds,
cleanup, and themes pass.

Human listening reported no clear difference and said the material sounded
good. A was the unchanged current palette; B was the `-2 dB` shelf treatment.
The current palette is therefore exonerated and carries forward. The palette
page is Rejected history at
`Music Legacy/officewars-boss-a-palette-check-audition.html`.

## 15. Identity-Kernel Test

The active page compares two anonymous kernels:

- one `64`-step, eight-bar sentence uses overlapping saw and triangle
  completions, withholds one expected completion, and lets harmony and bass
  decide whether later completions count; and
- one `56`-step, seven-bar sentence develops Sketch A's hammered-eighth figure,
  preserves its first five bars substantially, then dissolves the riff into a
  connected E7 cadence.

Both use the exonerated current palette. Both have populated saw, triangle, and
single-voice reduction plans; nonconstant bar-level intensity; distinct
harmony and bass routes; no E6; and naturally different lengths. The opening
splice remains deferred.

Real-browser verification passes `94` checks. Every candidate in Full,
Reduction, Saw, Triangle, and Support only completes two loops with headroom,
bounded sources, and zero-source cleanup. Full RMS measures approximately
`-16.82 / -16.24 dBFS`; reductions approximately
`-23.54 / -23.41 dBFS`. Pause, resume, seek, switching, 60-second playback,
replay, themes, and console checks pass.

Human listening selected A because it felt the most energizing. B remains
unselected. The page is Rejected history at
`Music Legacy/officewars-boss-a-identity-kernel-audition.html` because recurring
static blocks the selected material.

## 16. Kernel A Static Repair

The selected music is preserved exactly. Source diagnosis found that the
kernel page retained the previously rejected stacked catch-up scheduler:
after a delayed main-thread tick it schedules every overdue step, and each late
voice clamps to the same near-future start time.

In a forced `900 ms` stall:

- Control schedules five steps in one tick, with maximum lag around `668 ms`;
- Repair skips four missed steps and schedules one current step;
- Repair records one scheduler recovery and preserves the musical clock; and
- Full Control/Repair RMS matches within `0.03 dB`.

The page already contains the later windowed-noise percussion repair. No notes,
reductions, harmony, bass, intensity, roles, palette, percussion, length, or
monitor behavior change.

Normal headless loops did not generate overdue calls, so this reproduced the
known intermittent mechanism rather than the user's exact device timing.

**Outcome: human listening confirmed the static is gone.** Resilient
overdue-step skipping is settled for Boss A, and stacked catch-up scheduling
must not be restored. The page is Rejected history at
`Music Legacy/officewars-boss-a-kernel-a-static-repair.html`, retained as the only
remaining stacked-scheduler control and as the byte-pinned melody source for the
Approved ensemble baseline.

## 17. Kernel A Ensemble Selection

The user liked Kernel A's melody but suspected the ensemble was weak. Source
analysis agreed and named the defect precisely: the accompaniment was competent
but **non-responsive**, not absent.

- Bass rhythm was `[0,+3,+6]` in all eight bars.
- Harmonic rhythm was two hits per bar for seven of eight bars.
- Kick on local `0` and `4` and snare on local `2` and `6` were hard-coded in the
  engine, so percussion was a metronome; `kickExtra` added only four hits.
- The melody's `C6` apex is step 54, but the loudest bass note was step 62 and
  the biggest chord hit step 56, so the band peaked a bar late.
- Bar 4 withholds its triangle completion, and support did not respond.
- Escalation was a global `3.6 dB` intensity ramp: the loudness-only impact
  failure mode.

A mute test confirmed the rejection condition: removing the bass lost thickness
but deleted no nameable phrase function.

The comparison held melody, length, harmony, roots and `intensity` byte-identical
across both candidates, with build-time drift guards, and put both on the
resilient scheduler so the then-unlistened static defect could not confound the
judgement. Only bass, chord placement and percussion placement changed.
`Responsive` gave each role a phrase job:

- **bass as consequence** — events per bar `3,3,4,2,2,4,5,3`, a long low E and an
  unresolved `G#2` for the bar-4 refusal, the loudest note moved onto step 54, and
  the line vacating before step 62 so the closing note hangs alone into the loop
  seam;
- **harmony as destination** — hits per bar `2,2,3,1,2,3,4,2`, stabs on triangle
  completions, one unmoving pad in bar 4, densest in bar 7; and
- **percussion as pressure** — bar 4 withholds the snare entirely and keeps one
  kick, so bar 5 *reclaims* the backbeat.

Percussion placement became data-driven through `kickSteps` and `snareSteps` with
the fixed grid retained as fallback, so no audio-graph node changed.

**Outcome: human listening selected `Responsive`.** The selection is Approved at
`Music Locked/officewars-boss-a-kernel-a-ensemble-audition.html`, containing only
the selected candidate. The comparison page is Rejected history at
`Music Legacy/officewars-boss-a-kernel-a-ensemble-comparison.html`, retained as
the only remaining uniform-accompaniment control.

Two watchpoints survive the selection and belong to the next round rather than
this one:

- `Responsive` is not density-neutral. It has 26 bass events against 24 and 19
  chord hits against 15, so some of the improvement may come from more pitched
  support rather than from responsiveness alone. Percussion is sparser, at 18
  hits against 20.
- Because `intensity` was held constant, the `3.6 dB` level ramp still does
  escalation work in the Approved baseline. Whether it can now come down is open
  question 4.
