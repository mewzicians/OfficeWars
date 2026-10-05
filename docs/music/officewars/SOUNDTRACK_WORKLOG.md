# OfficeWars Soundtrack Worklog

Last updated: 2026-08-31

## Purpose

This file records OfficeWars music decisions and experiments that span more
than one scene. Casino-only history remains in `CASINO_WORKLOG.md`. Active
direction and approval status remain summarized in `README.md`.

## Current Verdict

- Sketch B is the selected OfficeWars parent-leitmotif foundation.
- The 32-step Workday-to-Casino bridge is the selected cross-scene
  transformation reference.
- The Workday should be playful and fun, mixing comfortable background
  listening with enough engagement to reward watching the office.
- Restrained office funk is the selected Workday palette foundation, and
  `112 BPM` is the selected Workday pace foundation.
- Hybrid B's gradual `0/0/0.55/1` motion arc is the selected Workday
  development foundation.
- Draft 01 Movements 2 and 3 are rejected; its Movement 4 return is liked.
- Role Reverse and Band Answers are rejected Workday middle directions.
- Candidate C's related harmonic detour is the selected Workday middle-melody
  foundation.
- The selected Workday form foundation is a `256-step`, approximately
  `1:08.57` loop with Candidate C, Passage D, Ensemble C, and Hybrid B's
  macro-motion arc.
- Hybrid D is the selected standalone Workday production foundation: warm
  Production A lead and organ over Production B's tighter rhythm section and
  cleaner room.
- The boss-floor cue should become a distinct high-energy Workday
  transformation with callback roles rather than a faster copy.
- Decision music and Night music remain unassigned.
- Festival Contour and Corporate Contraband remain the selected ordinary-Casino
  composition and production; this discovery does not revise them.
- Exact in-game Casino entrance timing remains open.
- `OW-MUSIC-BOSS-A-WINDOWED-PERCUSSION-REPAIR` is the Approved standalone
  Boss A rollback baseline.
- Active Tests are the On the Clock completion branch and Casino entrance
  comparison. Boss A is in a planning-only identity-kernel stage.

## Parent Leitmotif Discovery 01

The current question is:

> Which musical identity feels broad enough to become OfficeWars before any
> one scene transforms it?

The source-only `OfficeWars Identity Lab` presents three anonymous candidates.
Every candidate uses a shared 104 BPM, rounded Workday production skeleton and
contains:

- a 32-step, approximately 9.23-second one-shot Core; and
- a 128-step, approximately 36.92-second four-phrase Workday loop.

The anonymous hypotheses are:

1. Candidate A derives a parent from Prepared Mirror's descent, staged
   completion, and separate answer behavior.
2. Candidate B derives a parent from the earlier Decision material's confident
   rise, prepared high point, and connected return.
3. Candidate C is newly composed around a lift-and-settle rhythm, two related
   sequences, and a final semitone pull back into its opening.

The page withheld those origins so the first response could address memory,
appetite, fatigue, and identity rather than agreement with the design story.
At that stage, no candidate was selected.

The next step after selection is not a complete soundtrack cue. It is a
recognition test that transforms the chosen parent into contrasting Workday
and Casino expressions while preserving the selected Corporate Contraband
composition.

## Technical Evidence

Audition:

`Music Locked/officewars-parent-leitmotif-audition.html`

SHA-256:

`F66DFBA2B9CF195AC0737DC8E49EA350FDDA04B06434F501C374F682B0479FBB`

Verifier:

`.officewars-parent-leitmotif-verify.py`

SHA-256:

`8C81205A0D804F5A169DDAC7F3BA72208ABD6A8D4C74F8DA0F04FBCB2C3FA4B5`

The focused browser run passes:

- six distinct Core and Workday playback modes;
- exact Core-to-Workday motif continuity;
- matched 104 BPM form and timing;
- usable and comparison-safe 50-percent output;
- 100-percent headroom;
- pause, resume, seeking, issue marking, and clearing;
- 48 rapid track switches without source accumulation;
- 78 seconds and two complete Workday wraps;
- cleanup to zero tracked sources; and
- desktop, landscape, and portrait layouts without overflow or clipped
  controls.

Technical success does not select or approve a candidate.

## Parent Leitmotif Discovery 01 Listening Verdict

The user found Candidate B the best fit, while Candidates A and C did not seem
to hold their melodies well. Because the user said "probably," this records a
leading preference rather than selecting the parent.

The current diagnosis is:

- Candidate B's connected rise, prepared high point, and stepwise return form
  one singable melodic sentence.
- Candidate A's fragments depend on delayed completion and do not carry the
  foreground as naturally without the Casino arrangement engine.
- Candidate C's asymmetrical entries and changing phrase footing create local
  identity but weaken the sense of one continuously held melody.

Candidate B's strength also created a useful risk to test: a clear, pleasant
line can be followable without being distinctive enough to unify a soundtrack.
The recognition diagnostic therefore preserved B exactly as the control and
tested whether its identity remained recognizable under one contrasting scene
transformation.

## Parent Leitmotif Recognition 01

The diagnostic asked:

> Does Sketch B remain itself inside the Casino?

It compares three connected states:

1. `Workday Control` preserves the complete 128-step Sketch B Workday loop,
   104 BPM timing, low-fatigue production, and four developed phrases.
2. `Workday to Casino` introduces a 32-step bridge that accelerates from
   104 to 164 BPM before entering the exact selected Corporate Contraband
   loop.
3. `Casino Control` begins the exact selected Corporate Contraband loop
   directly at Hook Payoff.

The bridge preserves B's opening sentence through its first three bars. Its
fourth bar compresses and transposes the rising relationship into
`C-D-E-D`, then the selected Casino loop opens on `E`. The harmony and
instrument roles transfer across the bridge: Workday voicings and rounded lead
behavior give way to the Casino progression, club rhythm, and Corporate
Contraband lead without a pulse reset or silent fakeout.

The bridge began as a coordinated recognition hypothesis rather than a
preselected cue or entrance.

## Parent Leitmotif Recognition 01 Listening Verdict

The user found Sketch B recognizable after the transformation, liked the
transition strongly, and described it as natural while retaining its identity.
This resolves the diagnostic in favor of B.

The selected scope is:

- Sketch B's connected rise, prepared high point, and return become the
  OfficeWars parent-leitmotif foundation.
- The 128-step Workday loop remains the calm reference expression, not a final
  Workday cue.
- The exact 32-step 104-to-164 BPM bridge becomes the selected cross-scene
  transformation reference.
- Prepared Mirror and Corporate Contraband remain the Casino's scene-specific
  motif and production rather than being replaced by the parent.
- Final Workday production, other scene transformations, exact in-game
  entrance timing, Redline, stingers, exits, and shipping remain open.

## Recognition Technical Evidence

Audition:

`Music Locked/officewars-parent-transform-audition.html`

SHA-256:

`C8445FFB55A52D55765EE87147167F4808F1010D802CB8D5F1379AA338638645`

Verifier:

`.officewars-parent-transform-verify.py`

SHA-256:

`A5722DA0B999C40DDAE4061ACFDF3097AF2D2F272619E017C14592724487A6DB`

The focused browser run passes:

- exact Workday B notes, phrasing, duration, output compensation, and
  dynamics profile;
- exact Corporate Contraband notes, production treatments, loop duration, and
  Pass 06 calibration;
- the exact 32-step bridge and 104-to-164 BPM acceleration;
- audible, unclipped continuity into Hook Payoff;
- full mix and Casino layer isolation;
- pause, resume, seeking, 48 rapid switches, and cleanup to zero sources;
- 76 seconds with two complete Workday wraps;
- 82 seconds with two complete post-handoff Casino wraps;
- retained headroom at 100-percent volume; and
- desktop, landscape, and portrait layouts without overflow or clipped
  controls.

Technical success alone did not select Sketch B. The subsequent human
listening verdict selects the parent foundation and bridge reference.

## Workday Palette Discovery 01

The current question is:

> Which sound world makes the Workday fun to watch without becoming tiring?

The source-only `OfficeWars Workday Lab` preserves the exact selected Sketch B
melody, chord plan, bass roots, 104 BPM tempo, 128-step form, and four phrase
functions across three anonymous samples.

The coordinated hypotheses are:

1. rounded digital pop can make the parent buoyant and inviting through
   sustained harmony, smooth bass, and restrained drums;
2. soft pixel lounge can create playful game identity through filtered
   articulation, gentle arpeggiation, and sparse accents without beep fatigue;
   and
3. restrained office funk can make passive watching more physical through
   syncopated bass, short chord responses, and a tighter pocket.

All three pass comparison-level, headroom, transport, rapid-switching,
two-loop, cleanup, and responsive-layout verification. Evidence is recorded
in `verification/WORKDAY_PALETTE_DISCOVERY_2026-08-17.md`.

## Workday Palette Discovery 01 Listening Verdict

The user found Candidate C, the restrained office-funk treatment, the most fun
and the most likely to remain enjoyable over long listening. The remaining
concern was that its original pace could feel slow or become sleepy.

This selects restrained office funk as the Workday palette foundation while
leaving pace, motion, complete arrangement, and production open for focused
testing.

## Workday Motion Diagnostic 01

The diagnostic asked:

> Is Workday C sleepy because of its clock or because too little happens?

It preserved the exact selected melody, harmony, four-phrase form, and
office-funk sound world across:

1. the original C treatment at `104 BPM`;
2. Revision A, which adds syncopated bass, chord, kick, and snare motion at
   `104 BPM`; and
3. Revision B, which preserves the original arrangement exactly at `112 BPM`.

All three pass comparison-level, headroom, transport, switching, two-loop,
cleanup, and responsive-layout verification. Evidence is recorded in
`verification/WORKDAY_MOTION_DIAGNOSTIC_2026-08-17.md`.

## Workday Motion Diagnostic 01 Listening Verdict

The user preferred Revision B while also hearing something appealing in
Revision A. This selects `112 BPM` as the Workday pace foundation and identifies
Revision A's extra syncopated motion as useful arrangement vocabulary rather
than a rejected direction.

The unresolved question is no longer tempo versus motion. It is how much of
that extra motion should enter the selected `112 BPM` treatment without
damaging its relaxed, sustainable groove.

## Workday Hybrid Discovery 01

The hybrid comparison asked:

> How should Revision A live inside Revision B?

All three versions preserve the selected Sketch B melody, harmony,
office-funk sound world, `112 BPM` pace, and 128-step four-phrase form:

1. the exact Revision B control uses no added motion;
2. Hybrid A introduces Revision A's added groove only in the final Return; and
3. Hybrid B introduces it at partial strength in Develop and full strength in
   Return.

The page keeps the two development plans anonymous during listening. All three
pass exact musical-control, comparison-level, headroom, transport, switching,
two-loop, cleanup, and responsive-layout verification. Evidence is recorded in
`verification/WORKDAY_HYBRID_DISCOVERY_2026-08-17.md`.

## Workday Hybrid Discovery 01 Listening Verdict

The user preferred Hybrid B. This selects gradual phrase-level activation of
Revision A's groove vocabulary:

1. Establish retains the relaxed Revision B pocket with no added motion.
2. Answer also remains restrained.
3. Develop introduces the added bass, chord, snare, and reduced-pad behavior
   at `55 percent` strength.
4. Return uses that motion at full strength.

This gives the Workday a direction across one loop without placing constant
activity under the melody. The exact control and Return-only Hybrid A remain
historical comparison references.

The selected scope is the Workday development foundation only. Complete form,
variation across repeated loops, final sound design, mix, gameplay masking,
integration, and shipping remain open.

## Workday Long-Form Discovery 01

The active composition asks:

> Can the Workday stay playful for more than two minutes without overexposing
> the parent melody or becoming sleepy?

`Workday Longform` Draft 01 is a `512-step`, `112 BPM`, approximately
`137.143-second` A-B-C-A' loop:

1. **Movement 1** preserves Hybrid B exactly, including the selected
   `0/0/0.55/1` phrase-motion arc.
2. **Movement 2** moves to an original offbeat secondary foreground with
   `49` attacks and related `F-A-G-C` bass roots.
3. **Movement 3** lowers foreground exposure to `25` warm attacks while
   preserving kick, snare, bass, harmony, and an audible pulse.
4. **Movement 4** restores the complete parent foreground and introduces a
   `17-attack` secondary counterline after the opening phrase.

This form spends parent recognition twice rather than quoting it continuously.
Movement 3 subtracts attention rather than stopping, and Movement 4 changes
the return by joining the identities established earlier.

The focused browser run passes exact selected-foundation preservation,
movement boundaries and foreground plans, movement audibility, headroom,
transport, rapid switching, one foundation wrap, two uninterrupted full-cue
wraps, cleanup, and responsive layouts. Technical evidence is recorded in
`verification/WORKDAY_LONGFORM_DISCOVERY_2026-08-17.md`.

## Workday Long-Form Discovery 01 Listening Verdict

The user rejected Movement 2 and its transition as wonky. Movement 3 was also
rejected as weak, sleepy, and fragmented. Movement 4 was liked.

This means:

- the exact Hybrid B Movement 1 remains protected;
- the old secondary and breathing movements do not carry forward;
- Movement 4's parent foreground and `17-attack` counterline remain liked
  exploratory material; and
- the `2:17.14` duration remains unresolved because the rejected middle
  prevented a fair length judgment.

## Workday Form Repair 01

The active question is:

> Does one coherent middle sustain the Workday, or does a second connected
> movement earn the longer runtime?

Both rewrites remain at `112 BPM`, preserve the exact selected opening, use the
same new `128-step`, `60-attack` Connected Middle, and finish with the liked
parent-and-counterline return.

1. **Compact Rewrite** is `384` steps and approximately `1:42.86`. It moves
   directly from the Connected Middle into the return.
2. **Extended Rewrite** is `512` steps and approximately `2:17.14`. It adds one
   `128-step`, `64-attack` Momentum movement before the same return.

The repair changes fewer identities at each boundary. The opening's final F
root continues into the Connected Middle. That movement ends on C harmony and
a B melody note that resolves into the parent's opening C. In the Extended
form, the added movement begins on the same C root and ends on G and B before
the return resolves to C.

The focused browser run passes exact control preservation, shared-middle
equality, return preservation, movement audibility, headroom, transport,
60 rapid switches, two uninterrupted loops of both forms, cleanup, and
responsive layouts. Evidence is recorded in
`verification/WORKDAY_FORM_REPAIR_DISCOVERY_2026-08-17.md`.

## Workday Form Repair 01 Listening Verdict

The user found both the Compact and Extended rewrites awkward. The large
movements still felt long and stale, and adding or removing one complete
`128-step` block did not solve the perceived form problem.

The revised diagnosis is that phrase count alone did not create movement.
Twelve melodic phrases were grouped into only three or four broad arrangement
states. The liked return likewise behaved like parent alone followed by parent
plus counterline, so its four phrases collapsed into two perceived states.

Neither repaired form carries forward as the active Workday structure.

## Workday Micro-Movement Discovery 01

The active question is:

> How often must the Workday make a consequential turn to stay alive without
> becoming restless?

The source-only lab compares two `384-step`, approximately `1:42.86` relays.
Both remain at `112 BPM` and share the exact same twelve foreground phrases,
harmony, palette, runtime, and selected Hybrid B opening.

1. **Six-Movement Relay** changes arrangement function every `64` steps, or
   two melodic phrases.
2. **Twelve-Movement Relay** changes function every `32` steps, giving every
   melodic phrase a distinct job.

The shared development moves through four related harmonic routes rather than
holding one repeated progression for the complete middle. The return now
progresses through recognition, answer, teamwork, and loop preparation. The
Twelve-Movement Relay exposes those as four separate phrase-sized states.

The focused browser run passes exact shared musical material, all eighteen
movement starts, headroom, transport, 60 rapid switches, two uninterrupted
loops of both relays, cleanup, and responsive layouts. Evidence is recorded in
`verification/WORKDAY_MICROFORM_DISCOVERY_2026-08-17.md`.

Both movement cadences remain musically exploratory until human listening.

## Workday Micro-Movement Discovery 01 Listening Verdict

The user found the Six- and Twelve-Movement relays comparable, so increasing
the number of explicit arrangement turns did not produce a clear winner.
Six-Movement Move 4 was disliked.

The user's unprompted diagnosis was that the tunes may feel empty and may need
more support from other instruments. This is a hypothesis, not a selected
solution.

The implementation supports testing that hypothesis. Six Move 4 raises short
bass, chord, kick, and snare activity while reducing sustained pad support and
adding no counterline. It may therefore read as busier but thinner rather than
fuller.

The next smallest useful audition should preserve the selected melody,
harmony, `112 BPM` pace, office-funk palette, and a representative movement
sequence while comparing:

1. the exact current arrangement;
2. warm voice-led harmonic glue that preserves low-mid body; and
3. a sparse phrase-ending supporting voice that answers without competing
   with the parent melody.

Do not add continuous high-frequency tapping or fill every gap. The question
is which missing role provides connection, not how many instruments can play.

## Workday Support Discovery 01

The active question is:

> Does the Workday need sustained body, conversational support, or neither?

The source-only support lab preserves the complete Six-Movement cue as the
exact control. All three versions remain `384` steps, approximately `1:42.86`,
and `112 BPM`, with identical foreground, harmony, movement profiles, drums,
bass, effects, palette, and loop behavior.

1. **Current Arrangement** adds no new role.
2. **Candidate A** adds two warm sustained inner voices at each bar.
3. **Candidate B** adds one restrained three-note reply near the end of every
   two-phrase movement, for eighteen reply attacks total.

Candidate A tests harmonic glue. Candidate B tests conversation. The page
keeps those identities anonymous during first listening and provides direct
Move 3, Move 4, and Move 5 starts.

The full browser run passes exact source-control preservation, base-material
equality, support-role contracts, movement audibility, comparison-safe output,
100-percent headroom, transport, 60 rapid switches, two uninterrupted loops of
all three candidates, cleanup, and responsive layouts. Evidence is recorded in
`verification/WORKDAY_SUPPORT_DISCOVERY_2026-08-17.md`.

Both added roles remain musically exploratory.

## Workday Support Discovery 01 Listening Verdict

The user found that the control and both support treatments still felt empty.
The parent melody remained perceptually standalone, and the added
harmonization parts were too subtle or timbrally ambiguous to reveal what
instrument they represented or what musical role they intended.

This rejects the current sustained-glue and sparse-reply treatments as the
active solution. It does not reject harmonic body or conversational support
as roles in principle. The earliest broken decision is now instrument identity
and mix hierarchy: the accompaniment must first sound like recognizable
players before its amount can be judged.

## Workday Ensemble Discovery 01

The active question is:

> Which recognizable backing band makes the selected melody feel embedded
> rather than standalone?

The source-only lab returns to the selected `128-step`, approximately
`34.286-second` Hybrid B foundation. All candidates preserve the exact parent
melody, harmony roots, bass, drums, `112 BPM` pace, four phrase functions, and
`0 / 0 / 55% / 100%` development arc.

Only the harmonic ensemble identity changes:

1. **Ensemble A** uses rounded electric-piano behavior with sustained chord
   body and short replies.
2. **Ensemble B** uses percussive clavinet-like interlocks over a restrained
   harmonic bed.
3. **Ensemble C** uses sustained organ-like voicings and measured rhythmic
   swells.

The page keeps these identities anonymous during first listening. Full Mix,
Backing Only, and Harmony Only controls expose each role directly.

The focused browser run passes exact protected-material preservation, nine
layer contracts, isolated-layer audibility, comparison-safe output,
100-percent headroom, transport, 72 rapid switches, two uninterrupted loops
of all three full mixes, cleanup, and responsive layouts. Evidence is recorded
in `verification/WORKDAY_ENSEMBLE_DISCOVERY_2026-08-17.md`.

All three ensembles remain musically exploratory.

## Workday Ensemble Discovery 01 Listening Verdict

The user selected Ensemble C. Its sustained harmonic body and rhythmic swells
do not merely sit behind the parent melody; they integrate with its phrasing,
and the two roles uplift one another.

Ensembles A and B sounded present without creating the same reciprocal
relationship. They remain historical alternatives and do not carry forward
as the Workday accompaniment identity.

This selects Ensemble C's organ-combo relationship as the Workday ensemble
foundation. It does not approve a complete cue, long-form structure, final
production, gameplay masking, or integration.

## Workday Relational Form Draft 02

The active question is:

> Can the selected Ensemble C relationship sustain a complete Workday cue
> without returning to block-based staleness?

The source-only relational-form lab preserves the exact selected `128-step`,
approximately `34.286-second` Ensemble C opening, then extends it into a
`384-step`, approximately `1:42.86` loop. Its six two-phrase movements are:

1. `Lead & Hold`;
2. `Lift Together`;
3. `Band Invites`;
4. `Roles Reverse`;
5. `Recognition`; and
6. `Teamwork`.

The middle uses parent-derived phrase material. Its relationship changes are
the compositional development: the organ invites, the melody replies, the band
takes temporary leadership, and both roles prepare the return. The final four
phrases restore the exact parent foreground while developing the liked
counterline through `0`, `3`, `8`, and `6` attacks.

The focused browser run passes exact selected-source preservation, movement and
phrase contracts, comparison-safe output, 100-percent headroom, transport,
60 rapid switches, two uninterrupted full-cue wraps, six concurrent Foundation
wraps, cleanup, and responsive layouts. Evidence is recorded in
`verification/WORKDAY_RELATIONAL_FORM_DISCOVERY_2026-08-17.md`.

Draft 02 remains musically exploratory until human listening.

## Workday Transition Repair Discovery 01

Human listening found the beginning of `Band Invites` and `Roles Reverse`
awkward. The reversed notes in `Roles Reverse` remained interesting, while
`Teamwork` contained a strange moment.

The music-guide diagnosis is abrupt role transfer rather than weak core
material:

- `Band Invites` withholds the expected `B -> C` resolution and changes
  harmony before the melody resumes;
- `Roles Reverse` changes harmony, foreground behavior, and organ leadership
  at the same boundary; and
- `Teamwork` uses a counterline that closely shadows or doubles the parent.

The source-only transition-repair lab keeps Draft 02 as exact Version A.
Version B changes only the three handoffs:

1. an organ `C` resolves the prior `B`, and the first Band Invites bar begins
   on the parent harmony;
2. the preceding phrase foreshadows organ leadership, then the unchanged
   reversed melody receives a four-bar organ gain ramp; and
3. Teamwork's `8 / 6` close-shadowing counterline becomes `4 / 4`
   complementary harmonic anchors.

The focused browser run passes exact Draft 02 control equality, unchanged
foreground and reversed notes, repair-only contracts, all eight audible
playback modes, comparison-safe output, 100-percent headroom, transport,
64 rapid switches, one-shot completion, two uninterrupted wraps of both
complete forms, cleanup, and responsive layouts. Evidence is recorded in
`verification/WORKDAY_TRANSITION_REPAIR_DISCOVERY_2026-08-17.md`.

## Workday Transition Repair Listening Verdict

Human listening found Version B slightly better than Draft 02, but still short
of the intended result. The full-scope review found that the local seams were
not the earliest remaining problem: the organ changed gain and swell cadence
without truly receiving protagonist material, while the lead remained
continuously foregrounded. The sparse Teamwork anchors also reduced collisions
without creating a convincing conversation.

Version B remains an exact control for the next diagnostic. It is not selected
as the complete Workday solution.

## Workday Role Transfer Discovery 01

The active question is:

> Does genuine organ ownership make the middle develop causally rather than
> merely relabeling the same hierarchy?

The source-only role-transfer lab preserves Transition Repair Version B as
exact Version A. Version B keeps the foreground pitches, harmony, `112 BPM`
tempo, `384-step` form, and selected Ensemble C identity unchanged.

Only musical ownership and reciprocal support change:

1. the organ's repaired `C` continues to `D`, and the existing melody
   completes the parent rise on `E`;
2. three organ pickups foreshadow the transfer;
3. the organ performs the complete reversed phrase while the lead rests, then
   carries the first half of the following phrase before returning it;
4. Recognition retains the parent foreground over a reduced groove and low
   organ halo; and
5. Teamwork replaces the `4 / 4` lead-register anchors with `6 / 6`
   lower-register replies placed in foreground gaps.

The focused browser run passes exact control equality, unchanged foreground
pitches and harmony, role-ownership contracts, all ten audible playback modes,
comparison-safe output, 100-percent headroom, transport, 80 rapid switches,
one-shot completion, two uninterrupted wraps of both complete forms, cleanup,
and responsive layouts. Evidence is recorded in
`verification/WORKDAY_ROLE_TRANSFER_DISCOVERY_2026-08-17.md`.

Version B remains musically exploratory until human listening.

## Workday Role Transfer Listening Verdict

The user found Version B generally good, but heard the added invitation note
as jarring and too many clashes in Role Reverse. The literal reversal is
retired. Recognition and Teamwork remain useful protected treatments, while
the complete role-transfer form is not selected.

## Workday Band Answer Discovery 01

The source-only lab preserved Role Transfer Version B as exact Version A.
Version B removed the invitation `D` and all later organ pickups, replaced the
reversed phrase with eight chord-tone organ attacks, and returned the complete
following phrase to the lead. Harmony, tempo, form, Ensemble C, Recognition,
and Teamwork remained controlled.

The focused browser run passed exact control equality, candidate scope,
comparison-safe output, 100-percent headroom, transport, rapid switching, two
uninterrupted wraps of both complete forms, cleanup, and responsive layouts.
Evidence is recorded in
`verification/WORKDAY_BAND_ANSWER_DISCOVERY_2026-08-17.md`.

## Workday Band Answer Listening Verdict

The user did not like Band Answers at all. The replacement is rejected rather
than retained for tuning.

The new diagnosis is that the middle's earliest broken decision is raw melodic
material. Ensemble C was selected because the organ and melody uplifted one
another; forcing the organ to replace the lead weakened that identity. The
next experiment should return to discovery mode and compare several short,
fluid middle melodies while keeping the organ in its selected supportive role.

## Workday Middle Melody Discovery 01

The source-only lab compares three anonymous `96-step`, approximately
`25.714-second` journeys at the selected `112 BPM`. Every candidate keeps the
selected Ensemble C organ-combo relationship and shares one `16-step`
departure, one `16-step` return, duration, transport, and output architecture.

Only the `64-step` middle changes:

1. Candidate A is a fluid, mostly stepwise continuation.
2. Candidate B uses a more playful syncopated lead rhythm over Candidate A's
   harmony.
3. Candidate C takes the contour through a related harmonic detour.

Each candidate includes `Full Journey` and `Melody Only` playback. The focused
browser run passes anonymity, shared-form, distinct-middle, selected-ensemble,
audibility, comparison-level, headroom, transport, rapid-switching, responsive,
cleanup, and two-loop checks. Evidence is recorded in
`verification/WORKDAY_MIDDLE_MELODY_DISCOVERY_2026-08-17.md`.

## Workday Middle Melody Discovery 01 Listening Verdict

The user selected Candidate C as the strongest middle. Its related harmonic
detour is now the selected Workday middle-melody foundation.

The selected scope includes Candidate C's exact `64-step` middle melody, its
middle harmony, and its relationship with the selected Ensemble C
accompaniment. Candidates A and B remain historical alternatives.

This does not approve the complete `96-step` discovery journey as the final
Workday cue, select long-form structure or duration, finalize arrangement or
production, integrate music into gameplay, or mark a cue shipped. The next
composition should develop Candidate C inside a new form while preserving the
parent melody, Ensemble C relationship, `112 BPM` pace, and Hybrid B motion
arc.

## Workday Candidate C Form Discovery 01

The active question is:

> Can Candidate C support a coherent complete Workday form while preserving
> the selected ensemble and gradual motion arc?

The source-only lab develops the selected material into a `256-step`,
approximately `68.571-second` loop. Its eight 32-step turns are:

1. `Settle In`;
2. `Desk Banter`;
3. `Detour Opens`;
4. `Detour Deepens`;
5. `Thread Returns`;
6. `Corner Turn`;
7. `Parent Returns`; and
8. `Full Groove`.

The four parent phrases remain exact at the opening and return. Candidate C's
selected `64-step` notes, harmony, and roots remain exact in the detour. The
two central development phrases are new but derived from Candidate C's contour
and voice-leading behavior.

The selected Ensemble C relationship remains supportive throughout. Hybrid
B's exact `0 / 0 / 55% / 100%` motion arc is mapped across four 64-step macro
movements, while the eight phrase turns prevent the arrangement from waiting
through another 34-second state block.

The focused browser run passes all selected-source contracts, all eight
movement starts, Full Cue and Melody Only audibility, headroom, transport,
rapid switching, responsive layouts, two uninterrupted wraps of both modes,
and cleanup to zero sources. Evidence is recorded in
`verification/WORKDAY_CANDIDATE_C_FORM_DISCOVERY_2026-08-18.md`.

The complete form, two new development phrases, duration, transitions,
production, gameplay masking, integration, and shipping remain exploratory
until human listening.

## Workday Candidate C Form Refinement 01

Human listening found the original `Corner Turn` passage around 49 seconds
directionless. Its opening remains unchanged, while its final two bars now
settle on `F-A-G-F`, descend through the G7 chord as `F-D-B-D`, and enter the
parent's `E` stepwise. The original `E-F-G-E / D-E-F-D` ending is rejected.

The Movement Starts controls now follow playback in real time. Exactly one
button highlights the current phrase during full-cue playback, direct
movement starts, seeks, and loop returns; the active button exposes
`aria-current="step"` and the state clears on stop.

The focused browser run passes the revised cadence, smooth entry into `Parent
Returns`, all eight live movement states, both listening modes, transport,
headroom, rapid switching, responsive layouts, two uninterrupted wraps, and
cleanup to zero sources. Evidence is recorded in
`verification/WORKDAY_CANDIDATE_C_FORM_REFINEMENT_2026-08-18.md`.

Candidate C, Ensemble C, the four parent phrases, `112 BPM`, total duration,
and Hybrid B's `0 / 0 / 55% / 100%` motion arc remain unchanged. The revised
cadence and complete form remain musically exploratory pending listening.

## Workday Detour Flow Discovery 01

Human listening found that `Detour Opens` and `Detour Deepens` still needed
better internal flow and a more natural transition into one another.

The focused source-only diagnostic uses one shared `96-step`, approximately
`25.714-second` context clip: the end of `Desk Banter`, Candidate C's exact
selected `64-step` middle, and the opening of `Thread Returns`. The anonymous
treatments are:

1. the exact current articulation and boundary;
2. the same pitches and harmony with longer lead articulation, slower stereo
   motion, and longer releases; and
3. the connected lead plus one restrained organ handoff resolving `B-D` into
   `C-E` across the G7-to-C6 boundary.

Full Clip and Melody Only monitoring expose every treatment. The Passage Map
starts the currently active sample at context entry, `Detour Opens`, `Detour
Deepens`, or context exit and visibly follows playback.

All six modes pass comparison level, headroom, transport, rapid switching,
responsive layout, two uninterrupted wraps, and cleanup. Candidate C's
pitches, chords, roots, Ensemble C, `112 BPM`, and surrounding form context
remain exact. Evidence is
`verification/WORKDAY_DETOUR_FLOW_DISCOVERY_2026-08-18.md`.

No treatment was selected during the blind stage.

## Workday Detour Flow Reveal 01

The first blind listen liked all three passages but could not reliably identify
what changed between them. This completed the anonymous stage without
selecting a treatment.

The retained page now reveals the mechanisms permanently:

1. **Passage A: Original** uses the current shorter articulation, earlier
   releases, faster stereo motion, and no handoff.
2. **Passage B: Connected Lead** keeps every pitch and chord while lengthening
   the lead, softening releases, and slowing stereo motion.
3. **Passage C: Organ Handoff** adds one quiet `B-D` to `C-E` organ resolution
   to Passage B at the G7-to-C6 boundary.

A shared-material key makes clear that notes, chords, bass, band, tempo,
context, and duration are identical. The now-playing panel identifies which
mechanism is audible in the active mode. All three passages remain musically
unselected.

The exact revealed page passes the full musical-control, comparison-level,
headroom, transport, switching, responsive, two-loop, and cleanup suite.
Evidence is
`verification/WORKDAY_DETOUR_FLOW_REVEAL_2026-08-18.md`.

## Workday Detour Hybrid Selection 01

The listener liked every revealed flow treatment and identified useful roles
for all three. A focused source-only hybrid therefore preserved the three
references and added Passage D.

Passage D assigns each strategy by musical function:

1. close rhythmic notes use Passage A's shorter, crisper release;
2. spacious notes use Passage B's longer connected hold;
3. the final notes of both Candidate C phrases remain connected; and
4. Passage C's exact G7-to-C6 organ handoff prepares `Detour Deepens`.

The hybrid changes no pitch, harmony, root, ensemble, tempo, context, or motion
foundation. All eight Full Clip and Melody Only modes pass the complete
comparison, headroom, transport, rapid-switching, responsive, two-loop, and
cleanup suite.

Human listening selected Passage D. This selects its detour performance
treatment, not the complete Workday form or production. Evidence is
`verification/WORKDAY_DETOUR_HYBRID_SELECTION_2026-08-18.md`.

## Workday Candidate C Passage D Form Integration 01

The selected source-only reference integrates Passage D into the complete
`256-step`, approximately `68.571-second` Candidate C Workday form.

The prior full-form material remains exact:

1. the four parent phrases;
2. Candidate C's selected notes, harmony, and roots;
3. `Thread Returns` and the revised `Corner Turn`;
4. Ensemble C;
5. `112 BPM`; and
6. Hybrid B's `0 / 0 / 55% / 100%` macro-motion arc.

Inside steps `64` through `127`, the detour now uses Passage D's exact
phrase-role performance: 14 connected-note positions, crisp articulation at
the remaining notes, and the restrained G7-to-C6 organ handoff at step `95`.

The focused verifier passes exact equality with both protected sources, all
eight movement starts, Full Cue and Melody Only audibility, live movement
highlighting, transport, headroom, rapid switching, responsive layouts, two
uninterrupted loops of both modes, bounded source counts, and zero-source
cleanup.

This is a technically verified evaluation build. The complete form,
development phrases, duration, final production, gameplay masking,
integration, and shipping remain musically open. Evidence is
`verification/WORKDAY_CANDIDATE_C_PASSAGE_D_FORM_2026-08-18.md`.

## Workday Form Foundation Selection 01

Human listening liked the complete Passage D integrated form. This selects the
exact `256-step`, approximately `68.571-second` composition and loop as the
Workday form foundation, including its parent phrases, Candidate C middle,
development phrases, revised `Corner Turn`, Passage D performance, Ensemble C,
`112 BPM`, and Hybrid B motion arc.

Final production, mix translation, long-exposure fatigue testing, gameplay
masking, game integration, and shipping remain open. Evidence is
`verification/WORKDAY_FORM_FOUNDATION_SELECTION_2026-08-18.md`.

## Workday Production Identity Discovery 01

The production discovery preserved the complete selected Workday composition,
form, Ensemble C relationship, Passage D treatment, `112 BPM`, and Hybrid B
motion arc while comparing three sound worlds:

1. warmer studio-funk attacks, low end, drums, and room;
2. tighter polished-digital envelopes, rhythm, and space; and
3. a drier, crisper physical groove.

Human listening liked the warmth of A and the definition of B. A focused
hybrid lab then preserved exact A and B references and compared both ownership
splits.

## Workday Production Hybrid Selection 01

Human listening selected Hybrid D:

- Production A's warm lead, connected lead, and organ;
- Production B's tight bass and drums; and
- Production B's cleaner delay, feedback, and wet-space behavior.

The exact selected production passes all twelve Full, Backing, and
Lead-plus-Organ modes, comparison level, 100-percent headroom, transport,
rapid switching, responsive layouts, two uninterrupted loops of all four
complete versions, bounded source counts, and zero-source cleanup. Hybrid D
reported a `41`-source peak and `0.037923` signal peak during the final
two-loop run.

This selects the standalone Workday production foundation. Gameplay masking,
extended fatigue testing, adaptive behavior, game integration, and shipping
remain open. Evidence is
`verification/WORKDAY_PRODUCTION_HYBRID_SELECTION_2026-08-18.md`.

## Workday Long-Cycle Discovery 01

The active question is:

> Does exact Hybrid D repetition remain strongest across long exposure, or can
> a four-loop development plan improve endurance without making the Workday
> demand more attention?

The source-only lab compares three anonymous `1024-step`, approximately
`4:34.286` supercycles. Every candidate begins with exact Hybrid D and
preserves the selected melody, harmony, roots, form, tempo, Candidate C,
Passage D, Ensemble C, motion arc, production identity, and loop seam.

The hypotheses are:

1. exact repetition across all four loops;
2. below-conscious performance drift across loops 2-4; and
3. a clearer organ-response, rhythm-response, ensemble-reunion, and prepared
   reset arc across loops 2-4.

All three candidates pass direct loop starts, live loop tracking, headroom,
transport, rapid switching, responsive layout, two uninterrupted complete
supercycles, bounded source counts, and zero-source cleanup.

No strategy is selected. Hybrid D remains unchanged, and human repeated
listening must determine whether variation improves attachment or merely
raises attention. Evidence is
`verification/WORKDAY_LONG_CYCLE_DISCOVERY_2026-08-18.md`.

## Workday Long-Cycle Tribrid Discovery 01

Human listening found all three original long-cycle strategies enjoyable but
somewhat tame. The focused follow-up asks:

> Can one causal three-strategy arc create a stronger payoff without making
> the Workday demand constant attention?

The source-only comparison preserves exact four-loop Hybrid D as the control.
Tribrid D keeps Loop 1 exact, uses subtle human variation in Loop 2, develops
organ-and-rhythm conversation in Loop 3, then combines those behaviors with
four lower-register organ callbacks and a stronger pocket in Loop 4. The
final sixteen steps pull the organ, bass, and drums back before the exact
Loop 1 reset.

Both candidates preserve every selected note, chord, root, movement,
production decision, and loop seam. Both pass direct loop starts, live loop
tracking, comparison level, headroom, transport, rapid switching, responsive
layout, two complete `4:34.286` supercycles, bounded source counts, and
zero-source cleanup.

Tribrid D remains musically unselected pending human endurance listening.
Evidence is
`verification/WORKDAY_LONG_CYCLE_TRIBRID_DISCOVERY_2026-08-18.md`.

## Workday Long-Cycle Tribrid Selection 01

Human listening liked the complete Tribrid D cycle. This selects its exact
four-loop plan as the Workday long-cycle treatment:

1. exact Hybrid D baseline;
2. restrained human variation;
3. organ-and-rhythm conversation; and
4. combined payoff plus prepared reset.

The exact-repeat candidate remains the historical endurance control. The
selected treatment remains standalone and does not approve gameplay masking,
device translation, adaptive behavior, game integration, shipping, or final
delivery.

Selection evidence is
`verification/WORKDAY_LONG_CYCLE_TRIBRID_SELECTION_2026-08-18.md`.

## Workday Title Selection 01

The selected Workday cue's player-facing title is **On the Clock**.
`Tribrid D` remains only the internal development label for its selected
four-loop plan. The naming change does not alter the selected music or approve
game integration.

Evidence is `verification/WORKDAY_TITLE_SELECTION_2026-08-18.md`.

## Boss-Floor Reference Study 01

The active question is:

> How can the selected Workday cue become a very high-energy boss-floor cue
> that remains recognizable but earns its own identity?

The study reviewed Jacinthe Battle, `Hopes And Dreams`, and Champion Iris
Battle. It retains qualities rather than protected expression.

The useful distinction is:

- Jacinthe demonstrates poised pressure inside an approximately 90-second
  recurring confrontation form;
- `Hopes And Dreams` demonstrates a longer emotional escalation where familiar
  material changes meaning and scale; and
- Iris demonstrates a bright, celebratory, highly active approximately
  92-second loop whose internal role and color changes preserve clarity.

The resulting OfficeWars direction is:

1. create an original boss hook and pressure engine;
2. preserve Workday ancestry through selected relationships rather than a
   complete arrangement copy;
3. assign callbacks to different functions such as omen, propulsion,
   recognition, destabilization, payoff, and loop preparation;
4. coordinate subdivision, harmonic rhythm, bass and drum motion,
   articulation, register, density, brightness, and transition pace instead
   of relying on BPM or loudness alone; and
5. retain enough contrast for the largest transformed Workday statement to
   feel earned.

No boss-floor composition, tempo, form, callback map, production treatment,
adaptive state, or game integration was selected by the reference study.
Evidence is
`verification/BOSS_REFERENCE_ANALYSIS_2026-08-18.md`.

## Boss-Floor Reference Study 02

The follow-up study reviewed:

- Shady Cicada's final-boss composition tutorial;
- Tarro57's silly-battle composition tutorial;
- 8-bit Music Theory's analysis of `Gwyn, Lord of Cinder`; and
- Snazzy Spider's unexpected-NPC boss battle cue.

The most useful new OfficeWars principle is **status transformation**. The
Player's bright, bouncy voice should not be replaced when the fight becomes
more serious. It should gain phrase authority, bass support, harmonic
consequence, and a stronger cadence so the same cheerful identity becomes
capable and consequential.

The unexpected-NPC cue establishes its smaller identity for roughly thirty
seconds, expands it into a heavier statement, withdraws into a lower and less
active passage around `1:11`, then returns with its strongest statement around
`1:30`. Broad tonal similarity remains high across the form, so the reveal
recontextualizes the original identity rather than discarding it.

The Dark Souls analysis reinforces a complementary method: leave deliberate
space in early motif statements, then use later variants to fill, combine, or
redirect that space. The silly-battle tutorial shows that buoyant character
can coexist with disciplined leading tones, phrase truncation, progression
expansion, supportive reuse of the original melody, and a composed loop seam.
The final-boss tutorial demonstrates chromatic motor activity, jumpy
bass-and-chord interlock, and temporary meter change as pressure tools rather
than requirements.

For the current Boss A development:

1. preserve the exact Challenge Issued opening;
2. let the bouncy Player triangle voice remain recognizable;
3. give that voice more authority and consequence over time instead of simply
   adding more notes;
4. reserve early gaps for Boss replies and later shared language;
5. allow the Boss to adopt some Player buoyancy while the Player adopts some
   Boss decisiveness; and
6. make the final payoff complete previously withheld possibilities.

This study does not select a new melody, form, production treatment, or game
integration. The rendered Player-voice replacement remains checkpointed for
packaging and listening after the reference study.

## Boss Identity Discovery 01

The source-only Boss Identity Lab now tests three anonymous original
confrontation sketches at `168 BPM`, `128` eighth-note steps, and approximately
`22.857` seconds:

1. broad rising confrontation with the parent callback as recognition and
   payoff;
2. tactical syncopated pressure with callbacks used for propulsion,
   interruption, and recognition; and
3. volatile register and color turns with callbacks used as omen,
   destabilization, recognition, and loop preparation.

Each candidate exposes Full Sketch, Identity Only, and Callbacks Only modes.
All three preserve a transformed On the Clock contour while retaining distinct
hooks and pressure engines. All nine modes pass two-loop browser and audio
verification.

No boss candidate, complete form, production master, adaptive state, game
integration, shipping, or final delivery is selected. Evidence is
`verification/BOSS_IDENTITY_DISCOVERY_2026-08-18.md`.

## Boss Identity Selection 01

Human listening selected Boss A as the boss identity foundation and described
it as by far the strongest candidate because it is the most melodic.

The selected scope includes Boss A's broad rising original hook, galloping
bass and broad-backbeat pressure engine, `168 BPM` identity-sketch tempo, and
its use of On the Clock callbacks for recognition, payoff, and loop
preparation. Boss B and Boss C remain historical alternatives.

This does not select the `128-step` sketch as a complete boss form, final
duration, long-cycle behavior, production master, adaptive states, game
integration, shipping, or final delivery. Evidence is
`verification/BOSS_IDENTITY_SELECTION_2026-08-18.md`.

## Boss A Persistent Thread Form Discovery 01

Human listening identified Boss A's callback underneath the foreground as the
feature that most strongly connected the boss identity to On the Clock.

The source-only Boss A Persistent Thread Lab therefore preserves the selected
`128-step`, approximately `22.857-second` identity as a direct control and
develops one exploratory `512-step`, approximately `91.429-second` form at
`168 BPM`.

Boss A remains the foreground identity across four movements. The On the
Clock ancestry remains underneath every movement, changing function from low
memory to compressed pursuit, rising recognition, and combined payoff plus a
prepared reset. Full Form, Without Thread, and Thread Only modes expose the
thread's causal contribution.

All modes pass musical-contract, protected-source, level, headroom, transport,
switching, responsive, repeated-loop, bounded-source, and cleanup checks.
Human listening subsequently rejected this form. Its regular short-note
ancestry voice sounded like a ding or metronome, and the later movements
strayed too far from the selected Boss A identity.
Evidence is `verification/BOSS_A_FORM_DISCOVERY_2026-08-19.md`.

## Boss A Integrated Undercurrent Repair 01

The source-only repair preserves the exact selected Boss A sketch as its
control and keeps Boss A's melodic sentence and harmonic route as the spine of
all four movements.

The rejected regular short-note callback is replaced by one sustained
chord-tone organ onset per bar. Slow sine or triangle envelopes, bass contour,
and cadence carry On the Clock ancestry without a bright ping or metronomic
attack. Energy develops through arrangement, register, restrained fills, and
macro intensity rather than replacement melodies.

Full Repair, Boss A Core, and Undercurrent Only monitors pass exact-identity,
chord-tone, envelope, level, headroom, transport, switching, responsive,
two-loop, bounded-source, and cleanup checks. The selected Boss A control
completed eight wraps; each `91.429-second` repair mode completed two wraps
with a maximum `23` concurrent tracked sources and no clipping.

The repair remains musically exploratory pending complete-form listening.
Evidence is
`verification/BOSS_A_UNDERCURRENT_REPAIR_2026-08-19.md`.

## Boss A Paper Brush Limbo And Pop Repair 01

Human listening liked the integrated paper-brush Boss A pass but still heard
an occasional static pop. This classified the paper-brush artifact as Limbo:
its musical treatment was worth preserving, while a technical defect blocked
approval.

Source diagnosis found that every deterministic noise hit rose smoothly but
then changed gain instantly from full level to `68 percent`. That abrupt
`32 percent` envelope discontinuity could create a short broadband pop without
clipping the full mix, which explains why the previous peak-only gate missed
it.

The Limbo artifact is now Rejected and preserved at
`Music Legacy/officewars-boss-a-percussion-repair-audition.html`. The
envelope-only `OW-MUSIC-BOSS-A-POP-REPAIR` artifact is also Rejected and
preserved at `Music Legacy/officewars-boss-a-pop-repair-audition.html`.

The Test preserves the complete paper-brush rhythm, deterministic noise,
offsets, filters, melody, harmony, bass, undercurrent, form, duration, and mix.
It changes only the abrupt gain step into a continuous exponential decay.

A browser-rendered constant-signal envelope diagnostic measures:

- rejected abrupt transition: `0.32`;
- smooth Test transition: `0.003025`.

The focused and complete browser gates pass exact-control, lifecycle, envelope,
level, movement, transport, switching, headroom, responsive, repeated-loop,
bounded-source, and cleanup checks across both complete mixes and both
isolated monitors. Human listening remains open. No music entered the game.

Evidence is `verification/BOSS_A_POP_REPAIR_2026-08-19.md`.

## Boss A Scheduler Backlog And Recovery 01

Human listening still heard an inconsistent pop in the smooth-envelope Test.
The artifact could disappear after manually seeking backward. This classified
`OW-MUSIC-BOSS-A-POP-REPAIR` as Limbo: its music and envelope repair were
worth preserving, while another technical defect blocked approval.

The scheduler looks ahead by `180ms`. A delayed main-thread tick could leave
`nextTime` in the past. The old catch-up loop then scheduled every overdue
step, while each voice clamped its start to approximately
`currentTime + 2ms`. This compressed several missed notes and percussion
attacks into one source burst.

A forced `900ms` stall reproduced the behavior:

- rejected control scheduler lag: `694.905ms`;
- rejected maximum steps in one tick: `5`;
- rejected peak tracked sources: `36`;
- manual-seek fresh-state peak: `13`.

The useful smooth-brush material was preserved in
`OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`, now retained as the Rejected exact
live-engine control at
`Music Legacy/officewars-boss-a-scheduler-repair-audition.html`.
Its predecessor remains Rejected at
`Music Legacy/officewars-boss-a-pop-repair-audition.html`.

The Test advances past overdue steps before scheduling current and future
events. Under the same forced stall it skipped four overdue steps, scheduled
only one current step, and stayed at the normal 21-source peak. Three repeated
forced stalls also recovered without scheduling more than two steps in one
tick.

All four modes pass comparison level, movement, transport, switching,
headroom, responsive, two-loop, bounded-source, and cleanup checks. Human
listening nevertheless continued to reveal intermittent pops. This rejects the
scheduler repair as the active solution without invalidating its forced-stall
fix. No music entered the game.

Evidence is `verification/BOSS_A_SCHEDULER_REPAIR_2026-08-19.md`.

## Boss A Pre-Rendered Playback Diagnostic

The next diagnostic preserves the exact resilient live mix but removes the
remaining live playback variables most consistent with an intermittent
artifact: repeated oscillator starts, real-time scheduler work, effect-node
allocation, and garbage-collection pressure.

`OW-MUSIC-BOSS-A-PRERENDER-REPAIR` uses a deterministic steady-state render:

1. render the final `24` steps of the preceding cycle as preroll;
2. render one complete `91.4286-second` cycle at `24kHz`;
3. extract the steady-state cycle;
4. bundle that exact stereo WAV locally; and
5. decode it once, then loop one `AudioBufferSourceNode`.

The Test preserves the liked foreground, harmony, bass, sustained
undercurrent, smooth brush, form, and mix. Its decoded buffer measures a
`0.180397` peak, `0.004801` RMS, and `0.000056` loop-seam delta. Preparation
takes approximately `256-288ms` instead of the rejected runtime render's
multi-minute wait.

The exact live control and pre-rendered Test each complete two uninterrupted
loops. The live control peaks at `22` tracked sources; the Test peaks at one
runtime source and has no runtime scheduler. Stalls, pause, resume, seeking,
movement starts, rapid switching, maximum volume, responsive layout, and
zero-source cleanup pass.

Human playback later confirmed that this pre-render still contained
intermittent pops. It is now a Rejected control at
`Music Legacy/officewars-boss-a-prerender-repair-audition.html`. Evidence is
`verification/BOSS_A_PRERENDER_REPAIR_2026-08-19.md`.

## Boss A Windowed Percussion Approval

Waveform analysis traced the remaining pops to one-sample impulses at
deterministic brush and snare slice boundaries. The repaired render windows
each slice to zero at both ends while preserving the tune, harmony, form,
undercurrent, production, and timing.

The repair removed all `76` adjacent-sample jumps above `0.02` and reduced the
maximum jump from `0.199` to `0.0081`. Human listening reported no remaining
static and approved the tune.

`OW-MUSIC-BOSS-A-WINDOWED-PERCUSSION-REPAIR` is Approved at
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`. The page
is one standalone HTML with embedded audio, uses one runtime source, and
completes two verified loops. The superseded comparison is Rejected at
`Music Legacy/officewars-boss-a-windowed-percussion-comparison.html`.
Nothing entered the game. Evidence is
`verification/BOSS_A_WINDOWED_PERCUSSION_APPROVAL_2026-08-19.md`.

## Boss A Character Dialogue History

The historical source-only Boss branch is
`Music Legacy/officewars-boss-a-character-dialogue-audition.html`, with
internal label `OW-MUSIC-BOSS-A-CHARACTER-DIALOGUE`.

It preserves the Approved static-free opening exactly, then gives the two
registers distinct characters rather than treating them as one lead changing
octaves:

- the Player is high, light, cheerful, loud, syncopated, and emotionally open;
- the Boss is low, serious, measured, narrow in contour, and cadence-driven;
- `Different Languages` begins with non-overlapping private pitch classes;
- `Heated Exchange` lets each voice adopt all of the other's private pitch
  classes while sometimes interrupting and sometimes moving in parallel; and
- `Changed by Meeting` preserves those adopted traits in the payoff.

The Player's prepared ascent now reaches and holds MIDI `88` before yielding,
rather than retreating before its promised peak.

The page is one standalone HTML with embedded static-free audio. Its complete
verifier passes the exact opening, personality, borrowing, apex, movement,
waveform, transport, responsive, two-loop, and cleanup gates. It is Rejected
history and has not entered the game. Evidence is
`verification/BOSS_A_CHARACTER_DIALOGUE_TEST_2026-08-19.md`.

The prior melodic-development and register-dialogue Tests are also Rejected
history in `Music Legacy/`.

## Boss A Elastic Story Listening Control

The superseded Boss development branch is retained at
`Music Legacy/officewars-boss-a-elastic-story-audition.html`, with internal
label `OW-MUSIC-BOSS-A-ELASTIC-STORY` and lifecycle status `Rejected`.

Human listening strongly liked `Challenge Issued`, found `Finding a Rhythm`
usable, and rejected the Character Flow back half. The replacement preserves
the first two movements, then uses five newly composed functions:

1. the Player tries to work while the Boss hovers and disrupts the phrasing;
2. one brief accidental synchronization reveals possible shared language;
3. rigid Boss pressure returns without losing battle pulse;
4. both voices separate while retaining one borrowed trait; and
5. a stronger shared-language payoff reaches the Player apex and prepares the
   loop.

Movement lengths follow dramatic function rather than a uniform grid:
`128 / 128 / 64 / 64 / 64 / 64 / 128` steps, for a `640-step`,
approximately `1:54.3` form at `168 BPM`.

The page remains one standalone HTML with the exact embedded Elastic Story
audio and transport behavior. Its wrapper is retagged
`Rejected / Listening Control`; the embedded audio hash remains
`2F89A24CACA693A3C7208E8784E2DE29F79AF96991C5259EC62070C57EEC9C63`.
It has not entered the game. Historical Test evidence is
`verification/BOSS_A_ELASTIC_STORY_TEST_2026-08-20.md`.

The Character Flow Limbo predecessor is Rejected history at
`Music Legacy/officewars-boss-a-character-flow-audition.html`.

## Boss A Status Story Listening Control

Human listening found `Finding Footing` usable but rejected its repeated
pauses, rejected `Under Review`, found `Holding the Line` and
`Own the Cadence` insufficiently related to the established melody, found
`Clock Back In` alien, and rejected uniform-feeling movement durations.

The artifact is therefore Rejected history at
`Music Legacy/officewars-boss-a-status-story-audition.html`, with internal
label `OW-MUSIC-BOSS-A-STATUS-STORY`. Its exact embedded audio and transport
remain available as the direct listening control for the replacement. Evidence
is `verification/BOSS_A_STATUS_STORY_TEST_2026-08-20.md`.

## Boss A Melodic Throughline Listening Control

The technically verified but musically rejected Boss branch is retained at
`Music Legacy/officewars-boss-a-melodic-throughline-audition.html`, with
internal label `OW-MUSIC-BOSS-A-MELODIC-THROUGHLINE` and lifecycle status
`Rejected`.

The `512-step`, approximately `1:31.4` form preserves `Challenge Issued`
exactly and uses five unequal movements:

1. `Challenge Issued` - `128` steps;
2. `Finding Footing` - `88` steps;
3. `Pressure Turn` - `56` steps;
4. `Melodic Drive` - `144` steps; and
5. `Full Statement` - `96` steps.

The only post-opening melodic gap longer than four steps is one deliberate
eight-step breath in `Finding Footing`. Every later phrase remains traceable
to the Player's recognizable `1-2-3-5-4-3-2-1` scale-degree contour through
fragmentation, sequence, extension, register, changed harmony, and cadence.

Nine Boss saw accents overlap Player attacks. The Player ceiling rises from
MIDI `81` to `83`, `86`, and one MIDI `88` apex inside a transposed familiar
statement. The final `32` steps reproduce the exact opening Player callback
pattern inside `Full Statement`, avoiding a separate return melody.

The standalone Test embeds one static-free `24kHz` stereo WAV. Its peak is
`0.056000`, RMS is `0.006487`, maximum adjacent-sample delta is `0.009125`,
and loop-seam delta is `0.000031`. Movement RMS rises through the variable
form and peaks at `0.007870` in `Full Statement`. Focused verification passes
exact opening source and audio preservation, Player timbre, one-pause
discipline, motif statements, sparse overlapping Boss influence, singular
apex, exact callback return, transport, rapid switching, desktop and portrait
layouts, two uninterrupted complete loops, and cleanup to zero sources.
Technical success does not approve the composition. Evidence is
`verification/BOSS_A_MELODIC_THROUGHLINE_TEST_2026-08-20.md`.

Human listening found `Finding Footing` was getting closer, but found
`Pressure Turn`, `Melodic Drive`, and `Full Statement` strange to hear and
neither a good tune nor a convincing Boss song. The source diagnosis showed
that the later form repeated one eight-note contour as a mechanical template,
while nine isolated Boss accents were too weak to sustain the selected
galloping Boss identity. Those three movements are retired.

The wrapper is retagged `Rejected / Listening Control`; its embedded audio
hash remains
`DF60B8A506EAF48D52A924A9CEF10D797A3957A02C0FBC414EC5BD0425CBEE1D`.

## Boss A Tune Discovery Test

The branch, now Rejected at
`Music Legacy/officewars-boss-a-tune-discovery-audition.html`, used internal
label `OW-MUSIC-BOSS-A-TUNE-DISCOVERY`.

This is a tune-selection diagnostic rather than a complete Boss form. All
three neutral A/B/C candidates share `216` exact context steps:

1. `Challenge Issued` - `128` steps; and
2. `Finding Footing` - `88` steps with one eight-step breath.

Only the final `96-step` continuation changes. Every continuation uses the
same triangle-and-sine Player voice, loudness target, galloping Boss bass,
broad backbeat, harmony framework, and low rising Boss hook. Candidate A uses
three broad `32-step` phrases, B uses six tighter `16-step` phrases with
changed endings, and C uses two long `48-step` sentences. The listening page
does not reveal those construction labels.

The three embedded `24kHz` stereo WAVs have continuation RMS values of
`0.007412`, `0.007326`, and `0.007414`. The shared context matches the
Melodic Throughline control within one PCM least-significant bit after the
inherited loop-tail state. Focused verification passes three exact embedded
hashes, one deliberate pause, shared Player timbre and Boss pressure,
waveform, transport, thirty A/B/C switches, one media-source graph, desktop
and portrait layouts, cleanup, and two uninterrupted normal-speed loops of
each complete `0:55.7` candidate.

No candidate is selected. The next decision is purely musical: which
continuation is memorable, feels like a Boss tune, and forms a natural next
sentence after `Finding Footing`. Evidence is
`verification/BOSS_A_TUNE_DISCOVERY_TEST_2026-08-21.md`.

## Boss A Continuous Tune Listening Control

Human listening rejected Player Throughline and the preceding story-led forms
because their movement handoffs and later Player notes did not make one good
tune. The replacement therefore composes one continuous `512-step` form first
and assigns only neutral phrase bookmarks afterward.

The standalone Test exposes the same melody, timing, global harmony, and ten
unequal post-opening phrase lengths in two mixes. Melody + Pulse is the
composition monitor. Full Ensemble adds galloping low propulsion, broad
backbeat, connected low-mid harmony, sparse rising Boss statements,
gap-filling mid-register motion, and arrival-only octave and chord impact.

Both `24kHz` stereo renders preserve the exact Challenge Issued source
contract. Full Ensemble post-opening RMS is `0.007042`; Melody + Pulse is
`0.004036`. Both retain safe headroom at the `1.30` playback multiplier,
clean waveform and seam behavior, one reusable media source, and two
uninterrupted normal-speed loops. Technical success does not approve the
tune. Evidence is `verification/BOSS_A_CONTINUOUS_TUNE_TEST_2026-08-21.md`.

Human listening subsequently rejected every post-opening phrase. The full
ensemble did not solve the identity problem because the bright triangle and
sine voice still carried nearly every melodic attack. Challenge Issued works
differently: the broad saw lead, bright callback, bass, harmony, and impacts
assemble its foreground through changing ownership. Continuous Tune is now a
Rejected direct control at
`Music Legacy/officewars-boss-a-continuous-tune-audition.html`.

## Boss A Opening Grammar Listening Control

The active `224-step`, exactly `0:40.0` diagnostic preserves Challenge Issued,
then holds one new `96-step` melody, harmony, roots, gallop, backbeat, arrival
accents, phrase lengths, and loudness target constant. Only the foreground
carrier map changes:

1. Candidate A is saw-led with triangle completions.
2. Candidate B interlocks saw and triangle within each phrase.
3. Candidate C uses short triangle sparks while saw carries structural notes.

The opening's final triangle `C5` is the inherited first tone of the new
sentence. The first new attack is `D5` two steps later, avoiding a repeated
boundary note or empty section reset. Every candidate uses three neutral
`32-step` phrases; the diagnostic does not select a full form.

All three stereo `24kHz` renders remain within `3.7 percent` continuation RMS.
The maximum adjacent-sample delta is `0.009399`, the seam delta is `0.000092`,
and the maximum projected peak at `1.30` playback gain is `0.067285`.
Persistent dark mode, waveform, transport, thirty switches, one media-source
graph, and two uninterrupted normal-speed loops of each candidate pass.
Evidence is
`verification/BOSS_A_OPENING_GRAMMAR_DISCOVERY_2026-08-21.md`.

Human listening found all three candidates closer to the opening, but rejected
their tunes and handoffs as still too far from the musical identity.
Opening Grammar is now a Rejected direct control at
`Music Legacy/officewars-boss-a-opening-grammar-audition.html`.

## Boss A Next Movement Discovery Test

This diagnostic preserved Challenge Issued exactly and compared only the first
post-opening movement at `72`, `64`, and `80` steps, at `1.69` audition gain.
Half-volume post-gain movement RMS was `0.005362 / 0.005466 / 0.005352`, and all
candidates passed exact-opening, waveform, seam, transport, thirty-switch,
single-source, and two-loop gates. Evidence is
`verification/BOSS_A_NEXT_MOVEMENT_DISCOVERY_2026-08-21.md`.

None of those gates tested for quotation, and that is why the audition failed.
Later phrase-by-phrase reading found that every phrase in A, B, and C is a
recombination of one borrowed opening cell, including a rhythm-exact copy of the
triangle line that enters at `11.429` seconds, so the same cell sounded three
times in about 35 seconds and the page looped. Two candidates also quoted the
opening's run toward its apex and then turned around instead of completing it.
A three-way comparison between near-identical options has no correct answer.

The round also carried two constraints the user never asked for: an apex cap at
MIDI `81`, which excluded the opening's own top pitches `83` and `84`, and a ban
on deliberate breath. Both are withdrawn.
`OW-MUSIC-BOSS-A-NEXT-MOVEMENT-DISCOVERY` is Rejected at
`Music Legacy/officewars-boss-a-next-movement-audition.html` and retained as the
exact control for the quotation defect.

## Boss A Second Movement Sketches Test

The historical Boss branch is `OW-MUSIC-BOSS-A-SECOND-MOVEMENT-SKETCHES` at
`Music Legacy/officewars-boss-a-second-movement-sketches.html`. It abandoned the
generator, renderer, packager, and baked-render chain: the page synthesizes live
in about 62 KB, so a musical idea can be revised in seconds instead of costing a
multi-megabyte artifact. Direction, gates, and open questions are recorded in
`docs/music/officewars/BOSS_A_SECOND_MOVEMENT_PLAN.md`.

Four standalone loops of 8.57 to 11.43 seconds each declare a musical function
and carry two independent note sequences rather than one line time-sliced
between timbres. Sketch A raises pressure without ascending; B escalates past
the opening's ceiling; C reverses roles so the Player leads; B2 revises B.
Ancestry travels through harmony, bass, groove, and cadence, and no sketch
shares an eight-note run with the opening.

Human listening likes A and B, prefers B's opening to A's, rejects C, and
rejects B's bar-5 gear change and stepwise climb. Sketch B2 answers that verdict
by keeping B's first four bars verbatim and continuing to transpose the rising
fourth upward, which cuts the longest unbroken run of step motion from six notes
to two and moves the apex to 88 per cent through. Because length, harmony,
roots, intensity and groove are held identical to B, melodic motion is the only
changed variable.

The same pass rejected the offbeat percussion as sounding like a metronome. The
cause was a porting error rather than a design choice: the page had copied the
non-brush fallback branch of the Approved cue's scheduler, giving a fixed-level
pitched square tone on every odd step. The offbeat layer is now the Approved
cue's own windowed-noise paper brush on its alternating `[1, 3, 6]` and
`[1, 4, 7]` figure, with per-hit band, offset and pan variation, accents, and
intensity scaling, and the snare is the cue's noise-based brush snare. The
square tick is retained only as a labelled rejected control so the change can be
compared rather than taken on trust.

Verification is `106` musical and structural gates, a Python level estimate
placing the sketches within `0.9` dB of each other and `1.3` dB of the opening,
and `50` headless-Chromium checks covering play, analyser signal, progress
tracking, pause, resume, step-quantised seek, all four offbeat modes, mix and tab
switching, two complete loops, clipping, node drain, replay, theme, and a `420`
pixel viewport. This is the first round in which the browser-side audio checks
ran rather than being recorded as Not Run. No sketch is selected.

Human listening later rejected B2 from the `Intensity 3` bookmark onward
because its upper voices clash with themselves and did not like E6 in this
track. The page is therefore Rejected as the direct control for the focused
repair.

## Boss A Active Development Boundary

The approved static-free cue remains the protected rollback baseline at
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`.
All current Boss composition work belongs only to the separately labeled
Intensity 3 Repair Test described below. The Second Movement Sketches, Next
Movement, and Opening Grammar pages are direct Rejected listening controls,
while Continuous Tune, Player Throughline, and earlier forms remain Rejected
history in `Music Legacy/`. The Approved baseline must remain unchanged until
the user explicitly approves a replacement or the cue reaches Completed status.

## Boss A Pilot Clarification And Listening Contract

The user confirms two interpretation points before the next listen:

1. Player identity may move through the ensemble while the bright triangle
   remains selective. This is an orchestration and composition decision;
   mixing supports it through balance and focus but does not require triangle
   to lead every phrase.
2. After a movement survives standalone listening, a future Test may use
   DJ-style phrase-matched overlap by adding one incoming pickup during the
   opening's final bar. The Approved baseline artifact remains byte-identical,
   and the Test overlay may not replace an existing opening event.

The two independent lines and no-quotation requirements remain safeguards for
the current second-movement discovery round, not permanent rules for every
future phrase or callback.

The next listening pass fixes device volume at `50%`, in-page Volume at `80`,
Boost at `15.00x`, Paper brush, and Low trim off.

First use `Mix: Melody + pulse`: B for two loops, B2 for two loops, one direct
B-to-B2 loop each, then A for two loops. This diagnoses B2's melodic motion
before hearing A as a different pressure-function alternative.

Then use `Mix: Full ensemble`: B, B2, and A for two loops each. This pass judges
Boss scale and ensemble-carried Player identity.

If B2's motion succeeds but its E6 apex feels premature, preserve the motion
finding and reopen register separately rather than rejecting the complete
motion principle.

## Boss A Intensity 3 Repair Test

`OW-MUSIC-BOSS-A-INTENSITY-3-REPAIR`, now Rejected at
`Music Legacy/officewars-boss-a-intensity-3-repair.html`, was the active Test
for this round.

Control is exact B2. R1, R2, and R3 preserve exact B2 through step `27` and
hold length, harmony, roots, intensity, groove, percussion, sound, and controls
unchanged. Only post-boundary voice ownership, spacing, and register differ:

1. R1 uses selective triangle punctuation while saw carries the sentence.
2. R2 keeps both voices active in open chord-tone spacing.
3. R3 lowers saw structure while triangle remains buoyant and capped at C6.

Every repair removes E6 and the active upper seconds reproduced in Control.
Exact liked A remains the separate pressure-function reference.

Documented session-bus compensation matches changed note density without
altering musical intensity: Control `1.00x`, R1 `1.42x`, R2 `1.05x`, and R3
`1.10x`. Browser time-averaged RMS for Control and repairs spans `0.98 dB`.

Static and musical verification passes `59` checks. Browser verification
passes `63` checks, including two uninterrupted loops of all five versions,
transport, seek, mix, percussion modes, trim, candidate switching, headroom,
source bounds, cleanup, themes, and narrow layout.

No repair is selected. No music entered the game.

## Boss A Intensity 3 Scrap And Flow Replacement

Human listening rejected R1: it sounds like random noises, nothing turns into a
tune, and bar 1 sets up something that never pays off. The user then scrapped
this version of `Intensity 3` completely and asked for something that flows
from bar 1. Control, R1, R2, and R3 are all retired together.

Diagnosis located both halves of that verdict in structure. R1's triangle plays
`4` events across the `26` steps after the repair boundary against Control's
`9`, mean onset gap `1.31 s`, contour flat at `83, 76, 76, 79`, metric slot
drifting, and sitting `5` to `10` semitones below the saw. Bar 1's cell is a
rising perfect fourth with a step back, and bars 2 through 6 only transpose it
upward; R1's bar 7 is a pitch-and-rhythm-exact copy of its bar 5.

The two failures share one cause. Transposing a rising fourth generates its own
D6 ceiling, so E6 was the only diatonic pitch left that could function as an
apex. Rejecting E6 as a timbre removed the only available climax, which is why
the prepared ascent had nowhere to land.

`OW-MUSIC-BOSS-A-INTENSITY-3-FLOW`, now `Rejected` at
`Music Legacy/officewars-boss-a-intensity-3-flow-audition.html`, was the
replacement, derived from the hash-pinned repair prototype so the verified Web
Audio graph, transport, meters, percussion, and controls are preserved
byte-for-byte. It keeps bar 1 byte-exact and develops the cell instead of
transposing it: the leap `C5` to `F5` is treated as a gap containing `D5` and
`E5`. Fifteen prior attempts treated that fourth as a unit to transpose; none
filled it.

1. F1 fills the fourth stepwise, then grows from `3` to `8` saw notes a bar
   while holding at or below `A5`, so escalation is subdivision rather than
   register. The triangle owns the register arc alone and reaches `D6` once, at
   `79.7%`.
2. F2 hammers bar 1's landing note `E5` as a repeated-eighth cell in liked
   Sketch A's proven manner, holds its ceiling at `C6` from bar 4, and answers
   in a fixed slot `5` and slot `7` pair every bar. Its early repeated apex
   deliberately violates the arc gate, testing whether the missing payoff needs
   pitch at all.

Both are `64` steps, so all four intensity tiers land on bar lines at bars `1`,
`3`, `5`, and `7`; Control's `56` steps put every tier change mid-bar. F1 and F2
share only bar 1 with each other and with Control, and no bar repeats another.

Gate thresholds were recalibrated to the liked A reference after an earlier
draft set them stricter than material the user already likes. A reference itself
contains one minor second, a five-semitone triangle leap, and a six-step saw
rest, so none of those is a defect. The measured discriminator is clash
*density*, not clash existence: per `48` steps, A reference `1.0` clash and `0`
crossings, Control `4.29` and `3.43`, R1 `0` and `10.29` with a `6.57`-step mean
triangle gap. F1 and F2 both measure `0` and `0`. Clash detection models the
engine's real note durations, because onset-only checking is what let Control's
sustained collisions pass earlier inspection.

All four sketches are level-matched to the liked A reference by loop-integrated
measurement across two full loops, roughly `1200` samples each: A reference
`-16.48`, F1 `-16.36`, F2 `-16.17`, Control `-15.67 dBFS`, spread `0.81 dB` and
F1 against F2 within `0.19 dB`. A single `levelInfo()` reading cannot do this
job, because `rmsAverage` is a one-pole smoother over roughly `75 ms` and the
four sketches have different loop lengths and intensity ramps, so each snapshot
lands at a different phase; that method was off by `1.7 dB` on Control.

Browser verification passes `159` checks and fails none, covering page maths
against the offline gate, structural gates, two uninterrupted loops per sketch,
pause and resume with position frozen while suspended, seek into the final bar,
stop, cleanup to zero sources, replay, rapid switching across all four, both
mixes, clipping, and usable loudness.

Nothing was selected and no music entered the game. Human listening then
rejected the round; the verdict and its diagnosis are in the next section.

## Boss A Post-Opening Redo, Bare Theme Discovery

Human listening rejected F1 and F2 on two grounds: the music strays from
**melody**, and it strays from **the idea of it being a boss fight**. The user
asked to redo the whole thing.

Two scope decisions were then approved.

1. **Redo scope: everything after the opening.** `Challenge Issued` stays
   exactly as it is, including the `11.429 s` triangle entry. The entire
   continuation is freed: new theme, new harmony, new form.
2. **Bar 1 seed: freed.** The rising fourth is no longer a required starting
   point. Ancestry now travels through harmony, bass, groove and cadence rather
   than through quotation.

### Why the previous round could pass every gate and still fail

F1's answer to "stop transposing bar 1" was to fill the fourth stepwise, which
produces running scales — the least melodic material available. F2's answer was
to hammer a repeated note. Both are figuration, not theme. F1 also cadenced
`G7` to `Cmaj7`, a bright "we won" arrival that is wrong for a boss.

The gates could not see any of it. Clash density, voice crossings and triangle
onset gaps all score a scale run perfectly, and `159` browser checks passed.
Sixteen attempts had been built inside the full engine, where a weak tune leans
on percussion and harmony.

### The parent's melodic signature, measured

The Approved opening was measured directly for the first time, in `32`-step
windows. It is the calibration source for every threshold in this round.

| Property | Opening |
|---|---|
| Intervals that leap `3` or more semitones | `40` to `45` percent, in every window |
| Repeated consecutive pitches | `0` in `56` events |
| Distinct pitches per window | `4` to `7` |
| Window span | `12` semitones or less |
| Largest interval | `5` semitones |
| Events per `4` bars | `12` to `16` |

The character is ascending, leaping confrontation. It develops by rising waves
of differing internal shape, ceilings `77`, `81`, `84`, `84`, not by transposing
a cell. Fifteen attempts copied the cell instead of the method, and F1 removed
the two features that make the parent read as a boss at all: the leaps and the
rise.

### Method: theme first, bare, before anything else

`OW-MUSIC-BOSS-A-BARE-THEME`, now Rejected at
`Music Legacy/officewars-boss-a-bare-theme-audition.html`, was derived from the
hash-pinned repair prototype, so the verified Web Audio graph, transport,
meters, percussion and controls are preserved byte-for-byte. The single engine
change is one early return, because **no mix mode in the page was truly bare** —
`Melody + pulse` still plays a kick on beats `0` and `4`, so a weak tune could
always lean on the pulse. Bare is now lead-alone and is the default.

Four contrasting `32`-step themes, four genuinely different ideas rather than
two variations. Harmony is held constant at `Am7 F Dm7 G7`, the parent's own
opening chords with C major removed so no cadence arrives bright, which means a
four-way comparison reads as a comparison of tunes.

| | Idea | Leaps | Largest interval | Events | Ends on |
|---|---|---|---|---|---|
| T1 | Turn and climb; opens with a descent | `46%` | `5` | `14` | `G5`, the dominant, so it leans |
| T2 | Call and answer; held note drops a fifth | `46%` | `7` | `14` | `E5` |
| T3 | Driving riff; apex on the final step | `47%` | `5` | `16` | `A5`, an octave drop into the loop |
| T4 | Long-breath menace; weight, not density | `40%` | `6` | `11` | `B5`, which resolves nowhere |

`REF` is bars `1` to `4` of the Approved opening, byte-exact, in the same synth.
Without it there is no way to tell a weak theme from bare mode simply sounding
thin.

### Reservations recorded before listening

- **T2 at `7` semitones and T4 at `6` exceed the parent's `5`-semitone ceiling.**
  The standing note is that large unexplained jumps feel stunted. Both are
  flagged in the page itself. T1 and T3 stay inside the ceiling.
- **T4 carries `11` events against the parent's `12` to `16`.** Deliberate, to
  test whether a boss theme has to be busy at all.
- An earlier T4 draft introduced `G#5` for a harmonic-minor dominant. It was
  dropped: adding a pitch class the cue has never used, in the same round meant
  to fix melody and boss character, would confound the comparison.

### Gate calibration, and which gates are not the parent's

Every threshold was calibrated against the Approved opening, and three
uncalibrated gates were caught doing the wrong thing.

- A strong-beat semitone-rub gate initially failed T1, T2 and T4. The opening
  makes `2` such rubs against its own chords, and one of them, `B5` over `Dm7`,
  is the identical rub T2 and T4 make. The absolute gate became a budget.
- An apex-position gate requiring the apex in the last `40` percent is **not**
  the parent's behaviour at this scale; its windows place the apex at `69`, `44`,
  `25` and `31` percent. Same for "the answer must out-reach the statement":
  the parent measures `1`, `-2`, `0`, `0`. Both are retained as this round's
  choices and are printed alongside the parent's real values so a future round
  cannot mistake them for ancestry.

Two new gates target the F1 and F2 failures directly: longest run of
same-direction stepwise motion catches scale-filling, and longest run of
identical consecutive pitches catches hammering. A third gate was simply
missing for fifteen attempts — longest chain of consecutive bars that are exact
transpositions of one another. Nothing had ever checked for the defect everyone
kept describing.

Writing "the parent's method with new notes" also reproduced the parent's actual
notes twice: T1's opening six notes and T3's riff cell were verbatim
quotations, T3's in pitch and rhythm. Both were rewritten. The cause is worth
remembering — the parent works this diatonic alphabet densely, so at `32` steps
the quotation gate is doing real work, not ceremony.

### Verification

`64` static checks and `91` browser checks pass, none fail, and all `28` musical
gates pass.

Two checks exist because the previous round's `159` passing checks did not
prevent a musical failure.

1. The notes gated offline are asserted byte-for-byte identical to the notes the
   page plays, so the gates cannot pass on data that never shipped.
2. Bare mode is proven by measurement, not by reading the source: bare
   `-24.49 dBFS` against full ensemble `-17.69`, with `6` peak voices against
   `20`.

A page-breaking defect was caught only by the browser half. The sketch ids were
renamed but the initial selection still said `control`; `selectSketch()`
early-returns on an unknown id, so `activeSketch()` returned `undefined`, no
detail painted, and the first `PLAY` click threw. The static list of stale
strings could not see it, so the static verifier now resolves every sketch id
named in code against the real inventory instead.

Bare level spread across all five is `0.56 dB`, so no level compensation is
applied and no theme wins on loudness. Peaks sit near `-9 dBFS` with no
clipping.

Nothing was selected and no music entered the game.

## Boss A Bare Theme Rejection And Identity-Kernel Planning

Human listening rejected T1-T4 as a group. Every candidate was disappointing
in Bare melody, proving that the failure begins in raw melodic identity. Full
ensemble was more noticeable, but it did nothing to support the melody.

The compositional diagnosis is:

1. the themes were shaped around measured pitch statistics and invented
   late-apex rules rather than one memorable statement with consequence;
2. every idea was forced into the same `32`-step length and
   `Am7 F Dm7 G7` harmony;
3. every triangle line was empty and every intensity profile was flat;
4. the Full ensemble scheduler added the same chord, bass, kick, snare, and
   brush behavior beneath every melody; and
5. muting that backing removed thickness but not a specific phrase function.

`OW-MUSIC-BOSS-A-BARE-THEME` is therefore Rejected at
`Music Legacy/officewars-boss-a-bare-theme-audition.html`.
Its derivation source, `OW-MUSIC-BOSS-A-INTENSITY-3-REPAIR`, is also Rejected
at `Music Legacy/officewars-boss-a-intensity-3-repair.html`.

The next stage is planning only. Codex and Claude will independently define an
identity kernel in which melody, harmonic destination, bass motion, cadence,
and a minimal ensemble relationship are composed together. Neither agent may
build the next audition until both briefs are available for comparison.

## Boss A Independent Brief Ratification

Claude's independent brief is preserved at
`Inbox/Drop/Claude Music Versions/claude-boss-a-identity-kernel-brief.md`,
SHA-256
`C1C4B3A41EB6072B8684F6637071F61DA7FABBB8B415E8D0D876920D54A63994`.
Its seven-section first draft precedes a separate Post-Draft Cross-Check.
Codex's independent brief remains preserved in the private Wiki.

The briefs independently converged on a material-led, coupled method: melody,
harmonic destination, bass motion, cadence, and foreground ownership must be
composed together. Support succeeds only when muting it removes a named musical
consequence rather than thickness.

The user approved three decisions:

1. melody-only reduction is a rejection gate; the distributed architecture in
   which no single voice carries a coherent tune is retired for this round;
2. Sketch A's liked hammered-eighth figure may be developed in the future
   riff-into-sentence kernel; and
3. a palette check runs before kernel composition.

The palette check uses exact live Sketch A because it already has two
independent lines, a natural six-bar length, and a varying intensity profile.
The current live palette is measured first. At most one minimal clarity
treatment may then change palette and mix only, at matched perceived loudness.
No fixed correction value is selected from the retired baked-render spectrum.

After the palette result, the kernel round is limited to:

- a connected sentence with consequential punctuation and overlapping voices
  that finish one another; and
- riff into sentence, developing Sketch A.

The active private working bundle is
`Wiki/Knowledge/Music/Approach Bundles/OfficeWars Boss A Identity Kernel - Ratified Bundle.md`.
Canonical approval remains in the plan and balance ledger. No music was built
or integrated.

## Boss A Exact Sketch A Palette Test

The source-only diagnostic, now Rejected at
`Music Legacy/officewars-boss-a-palette-check-audition.html`, used internal
label `OW-MUSIC-BOSS-A-PALETTE-CHECK`.

Before authoring a treatment, exact live Sketch A was measured across two loops
at Volume `80`, Boost `15`, and Paper brush. Full-mix power was approximately
`27.1%` below `120 Hz`, `23%` from `120-500 Hz`, `47.0%` from `500-2000 Hz`, and
`2%` from `2000-4000 Hz`. This does not reproduce the retired baked-render
claim that `85%` sat below `500 Hz`.

The audition therefore compares only one restrained hypothesis:

- A preserves the exact current palette;
- B applies `-2 dB` below `140 Hz`; and
- B uses a `1.05x` disposable session trim to compensate the measured
  approximately `0.42 dB` level loss.

All notes, timing, harmony, roots, intensity tiers, groove, percussion, roles,
length, synthesis voices, controls, and visible labels remain held. The
treatment key is hidden for the first reaction.

Real-browser verification passes `75` checks. Full A/B RMS measures
approximately `-15.92 / -16.04 dBFS`, a `0.13 dB` span. Sub share measures
approximately `27.1% / 21.2%`; `500-2000 Hz` melody share measures
approximately `47.0% / 52.0%`. Full, Melodic roles, and Support only monitors
each complete two loops with headroom, bounded sources, and zero-source
cleanup. Pause, resume, seek, switching, 60-second continuous playback, replay,
themes, and console checks pass.

No palette treatment or kernel is selected. Human listening decides A, B, or
no meaningful difference.

Human listening reported no clear difference and said Sketch A sounded good.
A was the exact current palette; B was the matched `-2 dB` low-shelf
treatment. The simpler current palette is therefore exonerated and carries
forward. `OW-MUSIC-BOSS-A-PALETTE-CHECK` is Rejected at
`Music Legacy/officewars-boss-a-palette-check-audition.html`.

## Boss A Identity-Kernel Test

`OW-MUSIC-BOSS-A-IDENTITY-KERNEL`, now Rejected at
`Music Legacy/officewars-boss-a-identity-kernel-audition.html`, was the Test
for this round.

Two anonymous, naturally sized kernels implement the ratified architectures:

1. a `64`-step overlapping-completion sentence with one withheld triangle
   completion and support roles that determine whether later completions count;
2. a `56`-step riff-into-sentence development of Sketch A, ending through a
   connected E7 cadence.

Both use the unchanged current palette. Both expose Full, Melody reduction,
Saw, Triangle, and Support only monitors. Both have populated independent
voices, nonconstant intensity, intentional bass and harmony in every bar, no
E6, and no opening splice.

Real-browser verification passes `94` checks. Every candidate/monitor completes
two loops with headroom, bounded sources, and cleanup. Full RMS measures
approximately `-16.82 / -16.24 dBFS`; reduction RMS approximately
`-23.54 / -23.41 dBFS`. Sixty-second playback, pause, resume, seek, switching,
replay, themes, and console checks pass.

Human listening selected A because it felt the most energizing and reported
recurring static, including on loops. B remains unselected.

## Boss A Kernel A Static Repair

Source inspection found the known stacked-catch-up scheduler in the selected
kernel page. A delayed main-thread tick schedules every overdue step, while
late voices clamp to the same near-future start. The page already uses the
later windowed-noise percussion repair.

`OW-MUSIC-BOSS-A-KERNEL-A-STATIC-REPAIR`, now Rejected at
`Music Legacy/officewars-boss-a-kernel-a-static-repair.html`, preserves exact A
in Control and Repair. Only scheduler recovery differs.

A forced `900 ms` stall reproduces:

- Control: five steps in one tick, no recovery, maximum lag about `668 ms`;
- Repair: four skipped overdue steps, one recovery, one scheduled step; and
- Full Control/Repair RMS within `0.03 dB`.

Every Full, Reduction, Saw, Triangle, and Support-only mode completes two loops
with identical level, headroom, bounded sources, and cleanup. Repair also passes
60-second playback, transport, switching, replay, themes, and console checks.

Normal headless loops produced no late calls, so the user's exact recurring
artifact remained a listening gate. No music or palette changed.

Human listening resolved it: the static is gone. Resilient overdue-step skipping
is settled for Boss A, and stacked catch-up scheduling must not be restored. The
page is retained as the only remaining stacked-scheduler control.

## Boss A Kernel A Ensemble Selection

The user liked Kernel A's melody and asked whether its ensemble was weak. Source
analysis agreed and named the defect: the accompaniment was competent but
**non-responsive**, not absent.

- Bass rhythm was `[0,+3,+6]` in all eight bars.
- Harmonic rhythm was two hits per bar for seven of eight bars.
- Kick on local `0` and `4` and snare on local `2` and `6` were hard-coded in the
  engine, so percussion functioned as a metronome; `kickExtra` added four hits.
- The melody's `C6` apex is step 54, but the loudest bass note was step 62 and the
  largest chord hit step 56, so the band peaked a bar late.
- Bar 4 withholds its triangle completion and support did not respond.
- Escalation was a global `3.6 dB` intensity ramp, the loudness-only impact
  failure mode.

A mute compare confirmed the ratified rejection condition: removing the bass lost
thickness but deleted no nameable phrase function.

`OW-MUSIC-BOSS-A-KERNEL-A-ENSEMBLE`, now Rejected at
`Music Legacy/officewars-boss-a-kernel-a-ensemble-comparison.html`, was the Test.
Both candidates derived from one source block, so saw, triangle, reduction,
length, harmony, roots, `intensity`, palette and scheduler were byte-identical
under build-time drift guards, and only bass, chord placement and percussion
placement changed. Both ran on the resilient scheduler so the then-unlistened
static defect could not confound the judgement.

`Responsive` gave each role a phrase job: bass events per bar `3,3,4,2,2,4,5,3`
with a long low E and unresolved `G#2` for the bar-4 refusal, the loudest note
moved onto step 54 and the line vacating before step 62; chord hits per bar
`2,2,3,1,2,3,4,2` placed on triangle completions with one unmoving pad in bar 4
and the densest bar at 7; and percussion withholding the bar-4 snare entirely
while keeping one kick so bar 5 reclaims the backbeat. Percussion placement became
data-driven through `kickSteps` and `snareSteps` with the fixed grid as fallback,
so no audio-graph node changed. Static verification passed 60 checks and browser
verification 75.

Human listening selected `Responsive`. The selection is Approved at
`Music Locked/officewars-boss-a-kernel-a-ensemble-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-RESPONSIVE-ENSEMBLE`), which contains only the selected
candidate and is byte-identical in melody, length, harmony, roots and intensity to
the audition heard. Its static verification passes 64 checks and its browser smoke
test 51, including a `420 px` overflow check that caught a real header-wrap defect
introduced by the longer Approved status chip.

Two watchpoints carry into the next round. `Responsive` is not density-neutral: 26
bass events against 24 and 19 chord hits against 15, though percussion is sparser
at 18 hits against 20. And because `intensity` was held constant, the `3.6 dB`
level ramp still does escalation work, so whether it can now be reduced is
untested.

## Boss A Kernel A Handoff

Kernel A is eight bars, so the Approved ensemble was a partial track and owed one
Test branch. The user chose the handoff from `Challenge Issued` as its question,
so the branch spliced the Approved opening onto the Approved kernel and asked only
whether that joint needs a composed bar of preparation. `Direct` ran the joint
straight through at 192 steps and `34.286 s`; `Prepared` inserted one composed
`E7` approach bar at 200 steps and `35.714 s`. `E7` is Kernel A's own dominant, so
the joint reads `G7 → E7 → Am7`, and the seam's bass leaves `G#2` unresolved for
the theme's own `A2` downbeat to answer. `G#4` was the only new melodic pitch. The
128-step opening and its protected `11.429 s` triangle entry were re-derived from
the verified render source, and the kernel was carried forward note for note in
all eleven fields. Static verification passed 164 checks and the browser smoke
test 102.

Human listening on 2026-08-26 selected `Prepared`, then faulted the mix: the
bright callback voice was taking the spotlight from the melody. The user moved the
comparison page's triangle balance slider to `0.86` by ear and reported it sounded
"way better". Only gain moved; notes and the entry time never changed. `0.86` is
`2.29 dB` below the render's `1.12` and is now baked into every page in this
lineage as a constant with no slider, so any finished Boss A render must use
`0.86`. That slider survives only on the Rejected comparison page, which is also
the only page still holding the rejected `Direct` control.

The one process lesson worth keeping is that the balance defect was found by ear
in a single listening pass and would not have been found by any check written
here. The audition page carried an adjustable control at the exact parameter under
suspicion, which is what made the verdict actionable in one round rather than two.

## Boss A Kernel A Build Sentence And Melodic Ceiling

The promoted handoff baseline owed its own Test branch. The user asked for an
extension of the boss fight melody with rising energy and asked to test higher
after promotion, so the branch carried the Approved 200 steps forward untouched
and added one eight-bar build sentence, bars 26 to 33, from step 200 which is
`35.714 s`, for 264 steps and `47.143 s`.

It asked exactly one question: does the melodic ceiling break now, or is it saved
for a later climax? `Hold` kept the established `C6` and added no pitch the track
had not already used. `Reach` peaked on `D6` at step 252. `E6` was already rejected
for this track by ear, so `D6` was the last pitch available and breaking the
ceiling was a one-time irreversible spend. The two candidates were identical in
every field except five triangle notes at steps 252, 253, 255, 259 and 261, and
both ended on `B5`, so a preference could not be explained by harmony, groove,
level, length or cadence. That is the opposite of a production-only comparison,
and it returned a verdict in one round: "i like the reach ceiling broken".

The selection is Approved at
`Music Locked/officewars-boss-a-kernel-a-extension-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION`), with static verification passing 154
checks and the browser smoke test 100. Three consequences constrain everything
after bar 33. `D6` is spent and sounds exactly once, so the register ceiling is
final and a later climax can only out-reach this build by density, rhythm, harmony
or register width. The triangle carries the break while the saw stays at `83` and
still owns the opening's `C6`, inverting the register relationship the opening
established. And the new harmony introduces no new chord but four new moves
between them, the important one being `G7 → Cmaj7`, the first time the track
resolves up into the relative major instead of falling back to the tonic.

Promoting this baseline superseded the 200-step handoff form, which moved to
`Music Legacy/officewars-boss-a-kernel-a-handoff-audition.html` as the rollback
reference for the shorter form. The user chose to tag it `Rejected` with a note
rather than invent a sixth lifecycle label, so it records
`supersededOnMerit:false`. Every future branch promotion produces one of these, so
`Rejected` in this project does not always mean the music failed.

Selecting `Reach` also broke a derived label. A bookmark that named the sketch's
global apex had been correct while the apex lived in the protected opening; once
the apex moved to step 252 the label described a climb that does not happen at
step 96. It now derives from the opening rather than from the whole sketch. A
derived label is only as stable as the assumption it derives from.

The owed branch is open at
`prototypes/officewars-boss-a-kernel-a-drop-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-DROP`). The user chose a short drop before the climax,
so it carries the Approved 264 steps forward untouched and adds bars 34 to 41, for
328 steps and `58.571 s`. The drop is arrangement rather than melody: the saw
plays in every new bar while the triangle leaves for bars 34 to 39 and bar 35
loses percussion entirely; intensity falls from `1.4` at bar 33 to `0.72` at bar
34, troughs at `0.70` in that percussion-free bar, then rises every bar to `1.26`
at bar 41, stopping short of bar 33 so the climax stays unspent. Because the
ceiling is final it adds no new melodic pitch and tops out at `C6`. Static
verification passes 137 checks, the browser smoke test 125, and the settle repair
26.

First listening on 2026-08-27 returned two things. Bar 41 is good, which closes
the watchpoint about it deliberately ending below its own bar 33 peak. And the
page had static on a first playthrough that a loop did not reproduce. The cause
was not the music and not the scheduler, which clamped none of 3,026 voices: a
Chromium `DynamicsCompressorNode` reports about `-16.5 dB` of gain reduction
before receiving any audio and then releases upward over roughly a second, so the
opening played through a gain sweep. It was first-play-only because the graph is
built once per page load, and the user confirmed that by ear — a restart cleared
it, a reload brought it back. Repaired with a `COMPRESSOR_SETTLE` pre-roll of
`1.25 s` of rendered silence before the first note on the first play after a load,
injected by the generator so a rebuild cannot revert it. Gain reduction at the
first note fell from `-15.09 dB` to `-0.648 dB` with the music, length, source
counts and clipping unchanged. The platform measurement is recorded under Web
Audio Platform Behaviour in `docs/music/RESEARCH_LIBRARY.md`, and
`.officewars-compressor-settle-policy-verify.py` requires the pre-roll in every
new page.

## Boss A Kernel A Drop Accepted, And A Second Static Mechanism

Listening on 2026-08-27 closed both remaining drop watchpoints. Bar 34 "reads as
a pull back which is good right", and "8 bars is a good length". The arrangement
answer therefore holds: an energy pull-back after a peak reads as a pull-back
rather than as a restart when the melodic voice leaves, one bar loses percussion
entirely, and intensity recovers every bar without reaching the previous peak.
Continuity in the voice that stays is what keeps it from sounding like a new
section.

The same listening reported that static remained, and the description is what
made it tractable: "There is still some static but now it's random and not
repeatable. maybe it was always there, but it's very rare and one offs." Every
clause excludes something. Not repeatable excludes anything deterministic, and
this schedule is deterministic, so the same step produces the same voices at the
same offsets on every loop. Very rare excludes anything per-note or per-bar.
Always there points away from this branch's eight new bars. So this is a second
mechanism, distinct from the settle sweep, which had been reliably reproducible
by reload.

The user gated repairing the two other active prototypes on diagnosing it, so
`.officewars-audio-glitch-diagnosis-browser.py` was built to separate two
possibilities rather than assume one: is a discontinuity composed into the music,
or does the run time insert one? An `AudioWorkletNode` fans out from the live
compressor and inspects every rendered sample, and because the schedule is
deterministic, a discontinuity in the music recurs at the same loop position every
pass while an inserted one does not. A main-thread `ScriptProcessorNode` was
rejected for the probe: it would add main-thread work inside the render path being
measured and manufacture the failure.

The page is excluded as the source. Across `117 s`, every sample was inspected and
the largest sample-to-sample step was `0.1595` against a `0.35` click threshold,
so nothing click-like is composed in. The scheduler skipped no late steps, reported
`0 ms` peak lag, and audio time drifted `+9.6 ms` from wall clock with no sustained render gap. The Approved extension page measures the same: `0.1480` largest step over `94 s`, `-1.3 ms` drift, no gap. The render
thread produced `43,939` quanta against `43,914` expected and peaked at 20
concurrent voices, so the audio thread is not starved. The envelopes cannot
collapse into a step by construction, which is now asserted rather than trusted.

The artifact did not reproduce, so the diagnosis is bounded: the mechanism is
below what the page controls, most likely a device-level render underrun. One
structural finding is actionable. All 60 compressor pages construct their context
as `new AudioContextClass()`, and Chromium's default `latencyHint` is
`interactive`, which requests the smallest render buffer available — measured
`baseLatency` `10 ms`, against `20 ms` for `'playback'`. Buffer size is what
absorbs a late render, so the smallest buffer is the wrong default for a page with
no interactive latency requirement. A scratch copy showed `'playback'` is
musically neutral: length, first-note lead, step position, voice count and
clipping all unchanged, with no late steps. Cranking further is unsafe, because
the scheduler's `0.18 s` lookahead must stay comfortably above the buffer and an
explicit `0.2` hint measures `170 ms`. Nothing has been applied; this is a
mitigation that reduces exposure and cannot be proven to remove a defect that was
never reproduced.

Two verifier lessons came out of building the instrument, and both were defects in
the first version. A capture threshold of `0.25` sat above every transient this
music produces, so it logged nothing and the recurrence test compared two empty
sets and passed — a vacuous assertion. The fix is a low capture threshold inside
the music's own transient distribution plus a separate, higher assertion
threshold. And counting clock intervals from the first sample reported a `21 ms`
"render shortfall at 0.00 s", which is the render thread starting rather than a
dropout; startup is now excluded and the same run reports `+1.1 ms` net drift.

## Boss A Cadence, Five Candidates Built For One Listen

The drop's shape was accepted but its destination was not chosen, so the two
questions left open — harmonic destination and cadence — were put on one page
rather than asked in prose. Offered a set of options and their consequences, the
user answered "can you make an extension for all of the options you listed? then
with a proper listen we can go and see which works best." That is a decision
about method as much as about music: build the whole option space, then let one
listening session pick, instead of building the agent's favourite and asking for
approval.

`prototypes/officewars-boss-a-drop-cadence-audition.html`
(`OW-MUSIC-BOSS-A-DROP-CADENCE`) is that page. It carries all 328 steps and 41
bars forward as one frozen shared block that every candidate references, and the
generator offsets each candidate's local chord indices past the carried harmony,
so a candidate cannot accidentally reach back into the music it inherited. The
carried arrays are read out of the source page rather than retyped, and the
browser verifier proves the identity across pages by opening the drop page in a
second tab and comparing eleven music arrays plus chord names. Retyping 328 steps
and asserting the copy against itself would have passed while being wrong.

Five candidates. `Drop` is the branch unchanged, present as the control, because a
comparison with no unextended reference cannot tell "this ending is good" from
"any ending is better than stopping". `Land Am` and `Land C` land home in the
minor or up in the relative major, four bars each. `Payoff` is eight bars that
spend the reserve bar 41 was holding back. `Turnaround` is four bars that resolve
weakly on purpose and re-open the form.

`Land Am` and `Land C` are a controlled pair, and the control is the point. Their
rhythm, event counts, percussion and intensity are identical, and bar 44 is shared
note for note because `Dm7` belongs to both keys, so the only thing a preference
can be attributed to is harmonic destination. This project's own listening
evidence says gain, filter, subtle layer density and macro-energy differences are
usually not perceptible, and a comparison that varies several of those at once
costs a round and returns no verdict. A key change is not in that category.

The other two candidates differ from the pair by design rather than by degree.
`Payoff` is the only one that passes bar 33's `1.40`, reaching `1.52`, and the only
one with consecutive-step melodic runs, a percussion tutti, two chords per bar and
a new bass floor of `A1`; its `C6` sounds exactly once, on the downbeat of bar 48.
`Turnaround` is the only de-escalating candidate: a bare downbeat, the melody a
step late, a short offbeat stab, `Am7` rather than `Am`, ending on `G7` and
topping out at `G5`. Nothing reaches the spent `D6` or adds a melodic pitch the
track has not used, and the generator asserts both before writing rather than
after, so an out-of-range pitch or a root misaligned with its chord cannot reach
the page.

One measurement changed how the page describes itself. The first level check
assumed the payoff would simply be the loudest continuation and it failed:
sampled over a fixed window, the payoff measured below `Land C`. Two things were
wrong. The window was `2.6 s` while the payoff's peak bars sit about `11 s` into
its continuation, and peak level in this engine is set by transient coincidence
rather than by intensity. Sampled across each whole continuation instead, the
candidates' peaks span `1.059x`, which is `0.50 dB` — so no listening preference
here can be explained by loudness. The honest claim, now asserted, is that the
payoff's climax bars match bar 33's attack count rather than exceeding it, and
that its weight comes from density, subdivision and register width. A page that
had shipped the original assertion would have been claiming an advantage the
signal does not contain.

Two smaller lessons. The `Launch` bookmark was derived as `sketch.length - 8`,
which meant bar 41 until a continuation was appended and then silently meant the
last bar of whatever was appended; derived labels are only as stable as the
assumption they derive from, which is the same defect this lineage already hit
once. And five tabs overflowed the layout by `4 px` at `420 px` because multi-word
tab notes would not break, which is a real defect on a page whose whole purpose is
being listened to on whatever is at hand.

Nothing was promoted. The drop's own promotion to `Approved` was asked about and
not answered, so it stays a `Test` and the file was not moved. That leaves two
active Boss A `Test` branches, which is a fork of the one-active-branch rule; the
fork is a consequence of the open question rather than a decision, and answering
it closes the fork by moving one file.

## Boss A Drop Promoted, Cadence Remains Open

On 2026-08-31 the user delegated every answerable cadence-stage question to the
agent. One question was already supported by explicit listening evidence:
the eight-bar drop itself. On 2026-08-27 the user said bar 34 reads as a good
pull-back and that eight bars is the right length. Those were the branch's two
watchpoints, so the exact 328-step branch was promoted to Approved at
`Music Locked/officewars-boss-a-kernel-a-drop-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-DROP`), SHA-256 `C6C45B47`.

The previous 264-step baseline moved to
`Music Legacy/officewars-boss-a-kernel-a-extension-audition.html`, SHA-256
`AA927DBB`, tagged `Rejected` with `supersededOnMerit:false`. Its music was
extended, not rejected. Static verification passes `137/137` for the new
baseline and `159/159` for the superseded build.

The cadence comparison was rebuilt from the Approved drop and is now the sole
active Boss A Test at
`prototypes/officewars-boss-a-drop-cadence-audition.html`, SHA-256
`4B5ADF21`. The carried 328 steps remain shared by all candidates. `Land Am`,
`Land C`, `Payoff`, and `Turnaround` remain unselected because score analysis
can establish their construction and risks but cannot supply the listener's
preference or prove that bar 48 feels like the payoff.

One wording correction became durable: `Land Am` against `Land C` controls
rhythm, event count, percussion, intensity, and bar 44, but the pair changes
the coordinated tonal destination and the melodic, bass, and voicing pitches
needed to establish it. A verdict would therefore select a destination
treatment, not isolate one chord from melody.

## Boss A Landings Liked, Shared Cadence Repaired

Human listening on 2026-08-31 preferred both `Land Am` and `Land C` but found
their ending bars weak, then directed that `Payoff` and `Turnaround` leave the
active audition. This does not select Am or C. It separates tonal destination
from cadence quality: both destinations survived, while their shared final
mechanism did not.

The shared cause was compositional rather than tonal. Bar 41's `E7` resolved at
bar 42, so the strongest arrival occurred at the beginning. Both candidates
then repeated tonic, moved to shared `Dm7`, and returned directly to tonic
without a destination-specific dominant. Their final melodies arpeggiated
tonic, the triangle repeated confirmation notes, and the main percussion grid
did not punctuate the final downbeat. The written ending therefore had less
preparation than the opening of the continuation.

The focused Test now preserves exact `Am Original` and `C Original` controls and
adds one repair per destination. Bars 42-43 remain exact. In bars 44-45:

- Am uses `Dm7 -> E7 -> Am` and resolves saw `G#4 -> A4`;
- C uses `Dm7 -> G7 -> C` and resolves saw `B4 -> C5`;
- saw, bass, tonic chord, and kick meet on the final downbeat;
- the final-bar snare is withheld; and
- the triangle answers once afterward instead of repeating over the arrival.

Intensity, register ceiling, bass floor, Approved bars 1-41, triangle balance,
scheduler, and audio graph remain unchanged. Payoff and Turnaround are absent
from the active page but their exact composition data remains inactive in the
generator. The retained Test hashes `15CD696A`, is `92,811` bytes, and passes
browser verification `279/279`. Automated playback does not select a repair.

Project lesson: a liked destination can still have a weak cadence. When
controlled keys share the same ending complaint, repair the shared phrase
mechanism before choosing the key. The less-liked Payoff and Turnaround also
reinforce existing OfficeWars evidence: activity cannot substitute for melodic
continuity, and a second deferral after a long pull-back can read as withheld
payoff rather than useful continuation.

## Cadence Repairs Work, Exposure Is Too Short; Static Instrumented

Human listening on 2026-08-31 found both Am and C cadence repairs effective but
still could not choose between them. The new complaint was duration: the
repaired arrival occupies only bar 45, about `1.43 s` at `168 BPM`, before the
form ends. That distinguishes cadence quality from exposure. The next musical
question is no longer how to make the ending land; it is how to let the liked
destination continue long enough to become satisfying. No extension material
or length is selected.

The same listening reported static again. This reopens the rare second mechanism
and invalidates the active claim that it was simply not recurring. A fresh review
also narrowed what the earlier `117 s` sweep proved: it excluded a large
pre-destination discontinuity during that run, not every page or output-path
failure.

The current cadence Test therefore adds instrumentation without changing its
audio graph. `MARK GLITCH`, or the `G` key, captures an immediate snapshot plus
`250 ms` and `1000 ms` follow-ups. `COPY LOG` returns JSON containing Chromium
`AudioContext.playbackStats`, base and output latency, output timestamp,
context/device/visibility and long-task events, scheduler recovery and lag,
source counts, candidate, step, loop, and musical position. The diagnostic block
contains no audio-node creation, connection, worklet, or media-stream call.

The instrumented page hashes `4843D0D5`, is `102,273` bytes, and passes focused
browser verification `296/296`. The verifier confirmed that Chromium 151 exposes
underrun counters and that one marked event records live playback, output timing,
follow-up snapshots, and a copyable report. Its automated run recorded zero
underruns; that is delivery evidence for the run, not a claim that the listener's
rare artifact is resolved. `latencyHint:'playback'` remains unapproved and
unapplied.

## Human Marks Isolate Snare And Paper-Brush Overlap

The listener returned three marked events from one `landMinorCadence` run. Every
mark reported zero Chromium underruns and underrun duration, zero skipped steps,
zero scheduler recovery and lag, no clipping, stable `40 ms` output latency, and
no nearby context, device, visibility, or long-task event.

The logged button positions were `7.641 s`, `10.430 s`, and `32.881 s`.
Subtracting output latency and allowing a conservative human recognition and
response window maps them to steps `38`, `54`, and `182`. The inferred response
delays are approximately `815 ms`, `747 ms`, and `341 ms`, all plausible and
consistent with the observed input occurring after the sound.

All three source steps share one deterministic condition: the brush snare and
paper-brush offbeat occur together. The snare's windowed-noise air begins
`2 ms` after the step; the separate paper brush begins at
`UNIT * 0.025`, about `4.46 ms`, leaving two noise onsets about `2.46 ms` apart.
Steps `38` and `54` are exactly two bars apart, and step `182` repeats the same
local-six overlap later in the form. This explains how a smooth, windowed signal
could sound briefly static without producing a large sample-to-sample jump:
the issue is a short texture collision rather than a discontinuity or underrun.

The active Test now compares exact `Layered control` with unselected
`Snare priority`, which is the default. Snare Priority suppresses only a
paper-brush hit whose step already contains the brush snare. It preserves every
non-overlapping paper brush and changes no score array, note, chord, bass event,
kick, snare, envelope, signal-path node, or lifecycle state.

Focused verification runs both treatments through a marked collision window.
Layered schedules two paper-brush hits and suppresses none; Snare Priority plays
the non-overlapping hit and suppresses exactly the overlap. Both remain
unclipped and scheduler-clean. The page is `105,152` bytes, hashes `493AE988`,
and passes `310/310`. Human listening remains required before the treatment can
be selected.

## Noise Sources Isolated

The next Test retains Layered and Snare Priority and adds two diagnostic
isolates. `Snare air only` mutes every paper-brush hit while keeping the snare's
triangle body and windowed-noise air. `Paper brush only` keeps every paper-brush
hit and the snare's triangle body while muting only the snare noise-air layer.
The triangle body therefore remains present in every mode, so the comparison
does not confuse snare identity with its noise component.

All four modes share the exact score, envelopes, scheduling, graph, mix, and
candidate. In the marked step-38 window the verifier proves:

- Layered retains both complete noise sources;
- Snare Priority suppresses only the overlapping paper brush;
- Snare air only suppresses all paper brush and retains snare air; and
- Paper brush only retains all paper brush and suppresses only snare air.

Every mode remains unclipped and scheduler-clean. The page is `106,589` bytes,
hashes `B375045F`, and passes `316/316`. No noise treatment is selected; human
listening must identify which isolate retains the artifact.

## Four-Mode Verdicts And A Pause Crackle

On 2026-09-02 the listener returned two glitch reports from the four-mode
isolation page and four verdicts.

Cadence verdict, in the listener's words: likes both Am Cadence and C Cadence
but "they are too short. I think they need to be longer in order for the
payoff to truly be realized", asking whether actual game songs have some
pretty long tracks. No destination is selected. Length and post-arrival
exposure remain the earliest open musical decision, ahead of the Am-versus-C
choice.

Isolation verdict, in the listener's words: "I listened to them all but the
glitches were around the same time, I just stopped marking at the end because
better to look at what's the constant throughout the track, and then diagnose
from there." The directive for the next diagnostic step is therefore to
identify what is constant at the marked times rather than to compare modes
further.

The recorded marks, all telemetry clean (zero Chromium underruns, zero skipped
steps, zero scheduler lag, no clipping, stable `40 ms` output latency):

- `Snare priority` run, all on `landMinorCadence`: `8.694 s` step `49`,
  `15.854 s` step `89`, `40.286 s` step `226`.
- `Paper brush only` run: `landMinorCadence` `15.289 s` step `86`;
  `landMajorCadence` `5.385 s` step `31` and `27.545 s` step `155`.
- That second run also spent about `85 s` in `Snare air only` with no marks,
  which under the stated stop-marking decision is not evidence of a clean
  mode.

Both report titles say "before the D6 change". The listener defined that
phrase as the point "where the Am Cadence and C cadence branch out to make
their own identity" — a musical location, not an edit. All marks precede it,
so they sit in material shared across candidates. The page bytes are
unchanged at `B375045F`.

New symptom, confirmed directly: clicking pause more often than not produces
a crackle of static before the sound ends. This is distinct from the
mid-playback artifact and, unlike it, reported as usually reproducible.

## The Constant At The Marked Times

Source-level analysis on 2026-09-02, following the listener's directive; no
page bytes changed. The score reconstruction validated exactly against the
returned snare-priority log at step `292`: `63` snare-air hits, `110`
scheduled paper-brush hits, `16` collision suppressions — all three counters
match, so the event model is trustworthy.

- The two-noise-onset collision hypothesis is refuted. Four of six
  reaction-adjusted source windows (mark minus `5` to minus `2` steps)
  contain no snare/paper collision at all; in the snare-priority marks the
  one colliding paper hit in range was suppressed by the mode yet the
  artifact was still heard; and in `Paper brush only` no second noise onset
  exists anywhere. The earlier implicated steps `38`, `54`, `182` are all
  collision steps, which now reads as coincidence: they are accented local-6
  offbeats where paper brush and backbeat meet, but the new marks show the
  artifact without any collision.
- Constant in every source window, audible in whichever mode the mark was
  taken: the brush-snare hit (triangle body always, noise-air except in
  `Paper brush only`), the kick, the bass, and the saw lead. The triangle
  callback and the chord stabs are each absent from at least one window, so
  neither is the sole cause.
- The isolation grid has a missing cell: no mode mutes both noise layers at
  once, so every mode leaves at least one `playNoiseHit` source audible in
  every window. The shared windowed-noise mechanism is therefore not
  exonerated; only the collision reading is dead. A both-noise-muted mode is
  the highest-information next diagnostic and is proposed, not built.

## Pause Crackle Mechanism Identified

Confirmed against the page bytes by an adversarial re-check: the pause branch
of the transport handler (line `2121`) calls `audioContext.suspend()` bare —
no gain ramp, no source stop, no automation cancel — while stop and seek both
run `stopPlayback()`'s anchored `90 ms` exponential fade with delayed source
stops and deferred disconnects. Chromium suspends the render thread without
fading, so the output truncates at whatever non-zero sample the
compressor-hot mix holds at that instant; that step discontinuity is the
crackle, and it lands near a zero crossing only occasionally, matching "more
often than not". `resume()` (line `2123`) steps symmetrically from silence
back to the frozen sample. This matches the logged
`audio-context-statechange -> suspended` at pause time. Sibling audition
pages share the same transport idiom and likely the same defect, to be
repaired on re-entry per policy. No repair is selected or applied; candidate
repairs (master-gain ramp before a deferred suspend, resume-then-ramp
restore, or a dedicated transport gain node) are recorded as proposals only.

## No-Noise Isolate And Pause Repair Built (2026-09-04)

The user approved the two proposals for this pass and deferred longer-form
cadence work until the static is resolved. Both were built by regenerating
`prototypes/officewars-boss-a-drop-cadence-audition.html` through
`.officewars-build-boss-a-drop-cadence-branch.py`; no baseline was touched.

- `No noise percussion` is the fifth isolation mode: it suppresses both the
  paper brush and the snare noise-air layer at once, keeping the snare's
  triangle body, so it fills the missing diagnostic cell. Suppressions are
  counted in the existing `suppressed*` counters.
- Pause now ramps the master bus to `SILENCE` over `35 ms` of rendered time
  and suspends about `60 ms` later; a pause toggled back inside that window
  cancels cleanly; every resume path (transport button and
  `startSketch`'s suspended-context path) restores the gain through the
  volume slider's own `20 ms` `setTargetAtTime` idiom, recomputed from the
  slider so an interrupted pause cannot strand the bus at silence.
  `transportInfo()` now exposes `masterGainValue` so the suite can assert
  amplitude, not just state.
- Evidence: page SHA-256 `97473837`, `109,814` bytes.
  `.officewars-boss-a-drop-cadence-browser.py` `326/326`, including: gain at
  `SILENCE` (`1.0e-05`) when the context reads `suspended`, gain restored to
  `1.192` after resume, cancel-inside-fade keeps `running`, and the
  five-mode matrix (`No noise percussion`: paper `0` played, air `0` played,
  both suppression counters live, `17` sources still sounding).
  `.officewars-compressor-settle-browser.py cadence` `29/29`;
  `.officewars-compressor-settle-policy-verify.py` `39/39`. Pin closure on
  the old bytes was empty, so no repins beyond the active inventory.
- Whether the pause crackle is audibly gone, and what `No noise percussion`
  reveals about the recurring static, are the user's ear to judge. Nothing
  is selected.

## Listening Verdicts: Pause Repair Confirmed, No-Noise Mode Clean (2026-09-04)

Two verdicts from the user, recorded as given:

- Pause repair: "good crackle gone." The pause-fade repair on
  `OW-MUSIC-BOSS-A-DROP-CADENCE` (`97473837`) is confirmed by listening.
  The pause-crackle question is closed for this page.
- `No noise percussion` mode: "didn't hear any static on no noise
  percussion mode." One clean session with both windowed-noise layers muted,
  against prior sessions that heard static in `Snare priority` and
  `Paper brush only`. This localizes the recurring static to the presence of
  windowed-noise percussion. It does not yet separate the two remaining
  readings: the audible noise signal itself, or the source start/stop churn
  those ~173 short noise sources per loop dominate. The artifact is
  intermittent, so a single clean session is strong but not conclusive;
  the next comparison re-exposes this mode anyway.

Mechanism note recorded with it: the live `noiseHitBuffer` already
Hann-windows both slice ends to exact zero, so the slice-boundary defect
fixed in the Approved windowed-percussion cue is not present here. No
remaining defect is visible in `playNoiseHit` by inspection; the proposed
next discriminator is a `Silent noise percussion` diagnostic mode that
schedules every noise hit at inaudible gain, preserving churn and timing
while removing the audible signal. Static present there implicates
scheduling churn; static absent implicates the noise signal itself.
Proposed, not built.

## Silent Noise Percussion Diagnostic Built (2026-09-04)

The user approved building the churn-versus-signal discriminator. Built by
regenerating the page through the generator; no baseline touched.

- `Silent noise percussion` is the sixth isolation mode. It schedules every
  noise hit exactly as `Layered` — same steps, same `createBufferSource`
  starts, stops, and `ended` disconnects — but forces each noise gain to
  `SILENCE`, so the source churn and timing are preserved while the audible
  noise signal is removed. It is not a suppression: the played counters
  increment and no source is skipped.
- Discriminator, for the user's ear: play `Silent noise percussion` against
  `Layered` on the same candidate. Static that survives implicates the source
  start/stop churn (a scheduling or node-lifecycle cause); static that
  disappears implicates the audible noise signal itself (a filter, envelope,
  or level cause). Either outcome selects the repair family.
- `transportInfo()` now exposes `noiseSilenced`.
- Evidence: page SHA-256 `0E87C920`, `110,825` bytes.
  `.officewars-boss-a-drop-cadence-browser.py` `330/330`, including: silent
  mode matches Layered's hit counts (paper `2` vs `2`, air `2` vs `2`) and
  source count (`17` vs `17`) with zero suppressions and `noiseSilenced`
  true. `.officewars-compressor-settle-browser.py cadence` `29/29`;
  `.officewars-compressor-settle-policy-verify.py` `39/39`. Pin closure on
  the old bytes was empty.
- Nothing is selected. The churn-versus-signal question is open pending the
  listening comparison.

## Static Localized By Dissociation, Pause Crackle Confirmed Fixed (2026-09-09)

Three listening verdicts, recorded as given.

- **Pause crackle: fixed.** "good crackle gone". The `35 ms` master-bus fade
  before `suspend()` plus the `20 ms` restore on every resume path is confirmed
  by ear. This closes the pause defect.
- **`No noise percussion`: clean.** "didn't hear any static on no noise
  percussion mode". Both windowed-noise layers muted, snare triangle body and
  all tones retained.
- **`Silent noise percussion`: static persists.** On `landMajorCadence`, four
  marks: `6.931 s` (step `39`), `35.95 s` (step `202`), `44.902 s`
  (step `252`), `60.91 s` (step `341`). Hit counts equal to the exact
  `Layered` control (paper `138`, air `79`, zero suppressed) with every
  envelope pinned to `SILENCE`. Every mark reported `underrunEvents 0`,
  `schedulerRecoveries 0`, `skippedLateSteps 0`, `maxSchedulerLagMs 0`,
  `maxStepsScheduledPerTick 1`, `clipped false`; `liveSources` swung `3..30`
  and `peakSources` `28..30`.

**What the dissociation establishes.** Removing the noise hits removes the
static; silencing the same hits to about `-100 dBFS` with identical timing,
lifecycle and counts does not. So the artifact reaches the output through a
path not scaled by each hit's `envelope.gain`. The audible noise signal is
exonerated.

**The delay-send bypass candidate is now dead.** `playNoiseHit` line 1210 is
`envelope.connect(output)` and line 1211 passes `output` into `connectVoice`,
which taps `output` for both `state.bus` and the send. Both routes are strictly
post-envelope. Worst-case peak through the feedback delay at `SILENCE` is
`1e-5 x 0.022 x 1.0582 x 0.045 x 0.92 x 15 = 1.45e-7`, about `-136.8 dBFS`.
Summation is arithmetically excluded. This candidate had been live for several
rounds.

**Shared-junction churn is also refuted, and this corrects an earlier
hypothesis.** `playTone` builds its output node with the identical
`createStereoPanner ? createStereoPanner() : createGain()` pattern and calls
the same `connectVoice`, so nothing about a noise-hit connection differs in
kind at `state.bus` or `state.delay`. Tones supply roughly `1,874`
connect/disconnect events at `state.delay` against noise's `424`, and
`No noise percussion` retained all of them while sounding clean. Line 1294
(`send:0.014`, the snare triangle body) also executes *before* the
`no-noise-percussion` early return at lines 1295-1300, so `79` snare-body
sends still churn the delay in the mode that had no static.

**What survives: `AudioBufferSourceNode` lifecycle specifically.**
`audioContext.createBufferSource()` appears exactly once in the file, line
`1191`; the only other sources are `createOscillator()` at `1133`, `1134` and
`1274`. So `No noise percussion` does not remove a fraction of graph churn, it
removes **every** `AudioBufferSourceNode` instance from the graph, about `217`
per loop. Tones are `OscillatorNode`s and travel a different Blink handler
class, so per-quantum buffer-source work — active-source bookkeeping,
`finish()` task posting, buffer-reference release under the graph lock, and
main-thread `ended` dispatch timing — is untested by every control this project
has run. It sits in the shared render path, so it is immune to a `1e-5`
envelope, which is exactly what the dissociation requires.

**The baked-render negative result now constrains rather than refutes.**
`Music Legacy/officewars-boss-a-prerender-repair-audition.html`,
`buildPrerenderedLoop()` lines 1117-1119 set `calibrationGain = null;
compressor = null; analyser = null;` and lines 1116/1122 build only
`masterGain -> offline.destination`. The bake had no compressor, no low shelf
and no calibration boost and the impulses were still present, which eliminates
all three as necessary ingredients. It also used buffer sources, which makes
the surviving hypothesis more suspect rather than less. Its connects all
occurred before `startRendering()`, so it tested a static topology and cannot
rule out a churn mechanism whose realtime rate is the trigger. And an
`OfflineAudioContext` has no device underrun and no timer jitter, which
positively kills every real-time explanation and is consistent with
`underrunEvents 0` in every marked report. Note separately that
`playbackStats` reports *device*-level underruns, so `underrunEvents 0` was
never evidence against a graph-internal artifact.

**Marks are diffuse, which is corroborating rather than decisive.** Across all
sessions and modes the marked steps are `49`, `89`, `226` (`Snare priority`);
`31`, `86`, `155` (`Paper brush only`); `39`, `202`, `252`, `341` (`Silent
noise percussion`), landing on local positions `1, 1, 2 / 7, 6, 3 / 7, 2, 4,
5` within the eight-step bar. Even allowing for reaction delay they spread
across the whole bar, so no musical event is constant. That is the signature of
a density-driven lifecycle cause, not of a specific note.

**Measurement tooling cannot see this defect class.**
`.officewars-audio-glitch-diagnosis-browser.py` taps at `compressor`
(line 238) rather than the last node before destination, mono-sums
(lines 188-190) which cancels exactly the L/R divergence a panner-cycling
artifact produces, and uses an absolute `DELTA_CLICK = 0.35` (line 139) — which
is why the `117 s` sweep passed while measuring a maximum jump of `0.1595`. Its
past passes are therefore not evidence, and the "refuted by measurement" claims
resting on them do not hold.

Nothing is selected, promoted, rejected or superseded by this entry.
