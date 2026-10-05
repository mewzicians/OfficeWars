# OfficeWars Music Reference

Last updated: 2026-08-31

## Purpose And Status

This folder contains OfficeWars-specific music direction, active audition
state, listening history, and technical constraints. Read the general method
in `docs/MUSIC_GUIDE.md` first, then use this file to enter the OfficeWars
project without leaking its genre or implementation assumptions into unrelated
music.

Music remains exploratory and has not been added to the shipped game. The game
currently stores a master-volume preference for future audio.

Approval status comes from `docs/BALANCE_LEDGER.md`. Cross-scene soundtrack
history lives in `docs/music/officewars/SOUNDTRACK_WORKLOG.md`, and exact
Casino history lives in `docs/music/officewars/CASINO_WORKLOG.md`.

Artifact lifecycle and canonical paths come from
`docs/music/officewars/MUSIC_CATALOG.md`.

The source workspace has four music surfaces:

- `Music Official/` contains Completed standalone masters.
- `Music Locked/` contains Approved creative and technical references.
- `prototypes/` contains only Test or Limbo work: currently the Workday
  completion branch, the Casino entrance comparison, and the Boss A drop
  cadence comparison built on the Approved drop baseline.
- `Music Legacy/` contains Rejected, superseded, and retired auditions.

Every artifact has one stable `OW-MUSIC-*` internal label. Status and folder
must change together. Approved or Completed source music is still not shipped
until game integration is separately approved and verified.

A partial track advances by repeated extension. Promoting one to `Approved`
opens its next `Test` extension branch in `prototypes/` in the same task, under
its own label, carrying the Approved music forward unchanged and adding the next
extension. The cycle repeats until the track is a full track, and only then does
the finished master become `Completed` in `Music Official/`. Component
auditions such as motifs, palettes, percussion, and diagnostics feed a track's
branch instead of opening one, and the extension's musical content is never
invented to satisfy the rule.

The Approved Workday baseline is
`Music Locked/officewars-workday-long-cycle-tribrid-audition.html`, titled
**On the Clock**. The selected Casino composition and production references
are `Music Locked/officewars-casino-motif-audition.html` and
`Music Locked/officewars-casino-production-audition.html`. The selected Boss
identity is `Music Locked/officewars-boss-identity-audition.html`.

The Approved standalone Boss cue is
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`. It embeds
its audio inside one HTML file and has no external WAV or JS dependency. The
protected baseline remains unchanged. The latest bare-theme round is Rejected
at `Music Legacy/officewars-boss-a-bare-theme-audition.html`, and its
byte-pinned derivation source is Rejected at
`Music Legacy/officewars-boss-a-intensity-3-repair.html`. T1-T4 disappointed
in both Bare melody and Full ensemble; the backing was noticeable but did
nothing to support the melody. The independent Codex and Claude briefs are
complete and converged on a coupled identity-kernel method. The user approved
melody reduction as a gate, development of Sketch A, and a palette check before
kernel composition. Direction and open questions are recorded in
`docs/music/officewars/BOSS_A_SECOND_MOVEMENT_PLAN.md`. The retired Intensity 3
Flow, Next Movement, and Opening Grammar auditions are direct Rejected controls at
`Music Legacy/officewars-boss-a-intensity-3-flow-audition.html`,
`Music Legacy/officewars-boss-a-next-movement-audition.html` and
`Music Legacy/officewars-boss-a-opening-grammar-audition.html`.
The active Casino diagnostic is
`prototypes/officewars-casino-scene-audition.html`. The catalog and folder
indexes provide the complete inventory.

The palette diagnostic is Rejected history at
`Music Legacy/officewars-boss-a-palette-check-audition.html`. A was the
unchanged current palette and B a matched `-2 dB` low-shelf treatment. Human
listening heard no clear difference and said Sketch A sounded good, so the
simpler current palette is exonerated and carries forward.

The two-kernel page is Rejected at
`Music Legacy/officewars-boss-a-identity-kernel-audition.html`. Human listening
selected A because it felt the most energizing and reported recurring static,
including during loops. B is unselected.

The Approved Kernel A baseline is
`Music Locked/officewars-boss-a-kernel-a-ensemble-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-RESPONSIVE-ENSEMBLE`). It holds the selected Kernel A
melody with its selected responsive ensemble on the resilient `skip-overdue`
scheduler, and contains only the selected candidate. Its saw, triangle,
reduction, length, harmony, roots and intensity are byte-identical to the
audition the user heard. Bass events per bar run `3,3,4,2,2,4,5,3` and chord hits
per bar run `2,2,3,1,2,3,4,2`: bar 4 stalls on a held low E with the snare
withheld, bar 5 reclaims the backbeat, bar 7 carries the densest harmonic rhythm
and the loudest bass note under the `C6` apex at step 54, and the final bar
vacates so the closing bright note hangs alone into the loop. Percussion
placement is data-driven with the fixed grid retained as fallback, so the audio
graph is unchanged. Do not edit this file; future work belongs in a separately
labeled Test branch.

Two Boss questions closed together on human listening.

`Music Legacy/officewars-boss-a-kernel-a-static-repair.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-STATIC-REPAIR`) preserved exact Kernel A and compared
only the rejected stacked catch-up scheduler against resilient overdue-step
skipping. No musical event or palette value changed. The user confirmed the
recurring static is gone, so resilient overdue-step skipping is settled and
stacked catch-up scheduling must not return. This page is the only one that still
holds the stacked control.

`Music Legacy/officewars-boss-a-kernel-a-ensemble-comparison.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-ENSEMBLE`) asked whether Kernel A's accompaniment was
weak. Both candidates held the melody, length, harmony, roots, intensity, palette
and resilient scheduler byte-identical, so only support changed. Human listening
selected `Responsive`. This page is the only one that still holds the rejected
`Current` control, whose bass rhythm repeats in all eight bars, whose harmonic
rhythm is two hits per bar for seven of eight bars, and whose escalation is
carried only by a `3.6 dB` level ramp. That is the measurable
uniform-accompaniment failure mode, and it remains a useful control for future
ensemble work.

Two watchpoints survive the selection. `Responsive` is not density-neutral: it
has 26 bass events against 24 and 19 chord hits against 15, so some of the
improvement may come from more pitched support rather than from responsiveness
alone. And because `intensity` was held byte-identical, the `3.6 dB` level ramp
still does escalation work in the Approved baseline; whether that ramp can now be
reduced is untested.

Kernel A is eight bars, so the Approved ensemble is a partial track, and its
handoff from `Challenge Issued` is settled. The handoff spliced the Approved
opening onto the Approved kernel through one composed `E7` approach bar: 200
steps and `35.714 s`, theme entering at `24.286 s`. `E7` is Kernel A's own
dominant, so the joint reads `G7 → E7 → Am7`, and the seam's bass leaves `G#2`
unresolved for the theme's own `A2` downbeat to answer. `G#4` is the only new
melodic pitch in the piece. The opening's 128 steps and its `11.429 s` triangle
entry are intact, and the kernel is carried forward note for note in all eleven
fields.

Human listening on 2026-08-26 selected the prepared seam, then settled the mix.
The bright callback voice was faulted for taking the spotlight from the melody,
so the triangle balance was set to `0.86` by ear and is baked into every page in
this lineage as a constant with no slider, `2.29 dB` below the render's `1.12`.
Notes and the entry time never changed; only gain moved. Any finished render of
this material must therefore use `0.86` rather than the `1.12` still baked into
the Approved windowed-percussion cue and the Approved ensemble page. The rejected
`Direct` control, 192 steps with no approach bar, survives only in
`Music Legacy/officewars-boss-a-kernel-a-handoff-comparison.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF-COMPARISON`), which is byte-pinned as the
evidence of what was heard.

The 200-step form is no longer the baseline. Its own extension superseded it on
2026-08-26, so it moved to
`Music Legacy/officewars-boss-a-kernel-a-handoff-audition.html` and is retained
as the rollback reference for the shorter form. It is tagged `Rejected` because
the lifecycle has exactly five labels and none of them is *superseded*; the page
records `supersededOnMerit:false` and the catalog row says the same, so it should
not be read as a negative control.

The former 264-step build baseline is superseded history at
`Music Legacy/officewars-boss-a-kernel-a-extension-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION`). Its exact selected music was not
rejected: the next branch carried all 264 steps forward unchanged, so the page
records `supersededOnMerit:false`.

The current Approved baseline is
`Music Locked/officewars-boss-a-kernel-a-drop-audition.html`
(`OW-MUSIC-BOSS-A-KERNEL-A-DROP`). Human listening on 2026-08-27 confirmed the
two questions that branch was built to answer: bar 34 reads as a good pull-back
and eight bars is the right length. The user delegated the resulting lifecycle
action on 2026-08-31, so the exact 328-step form is now protected.

It carries the opening, prepared seam, Kernel A, responsive ensemble, and build
sentence unchanged, then adds bars 34 to 41. The saw remains continuous while
the triangle withdraws for six bars, bar 35 loses percussion, and the
arrangement rebuilds without reaching bar 33's intensity. The section adds no
melodic pitch, tops out at `C6` below the spent `D6`, and ends on unresolved
`E7`. The `0.86` triangle balance, `11.429 s` entry, paper brush,
`skip-overdue` scheduler, and `1.25 s` first-load settle remain intact.

The sole active Boss A Test is
`prototypes/officewars-boss-a-drop-cadence-audition.html`
(`OW-MUSIC-BOSS-A-DROP-CADENCE`). It is built from the Approved drop at source
hash `C6C45B47` and carries all 328 steps as one shared block. Human listening
preferred both Am and C destinations but found their ending bars weak. The page
now presents exact `Am Original` and `C Original` controls beside
`Am Cadence` and `C Cadence` repairs. Each repair preserves bars 42-43 and
changes only bars 44-45: pre-dominant into the destination's dominant,
leading-tone resolution onto the final saw tonic, bass/chord/kick arriving on
that downbeat, one later triangle confirmation, and no final-bar snare.
Payoff and Turnaround are absent from the active audition by user direction;
their composition data remains inactive in the generator. No repair or
destination is selected. The page is 360 steps / `64.286 s` at its longest,
hashes `493AE988`, and passes browser verification `310/310`.

Human listening then found both repairs effective but the destination exposure
too short: bar 45 lasts only about `1.43 s` before the form ends. This is a form
duration problem rather than a cadence-strength problem. The next musical
experiment is to preserve each repair exactly and append a post-cadence melodic
sentence; no extension length or material is selected yet.

Static verification passes `137/137` on the Approved drop and `159/159` on the
superseded build. The cadence browser and settle checks remain the focused
delivery gates. Automated verification does not choose a continuation.
The residual static was reported again on 2026-08-31. The earlier `117 s`
instrumentation pass still rules against a large pre-destination discontinuity
in that run, but it cannot exclude render underruns or failures after the graph's
tap, so the page itself is no longer described as excluded. The cadence Test now
adds a non-audio-changing `MARK GLITCH` button and `G` hotkey. Each mark captures
Chromium `AudioContext.playbackStats`, base and output latency, output timestamp,
context/device/visibility events, scheduler state, source counts, candidate,
step, and musical position, plus `250 ms` and `1000 ms` follow-ups. `COPY LOG`
returns the structured JSON. The diagnostic block creates and connects no audio
node; the signal path is unchanged. `latencyHint:'playback'` remains unapproved
and unapplied until evidence distinguishes an underrun from the alternatives.

The first returned report contains three marks on `landMinorCadence`. After
subtracting the measured `40 ms` output latency and allowing for human reaction
time, the likely source steps are `38`, `54`, and `182`. All three are the same
deterministic texture: the brush snare's noise layer and the separate paper
brush occupy one step, beginning about `2.46 ms` apart. Browser underruns,
scheduler recovery, skipped steps, lag, clipping, output-timestamp drift, and
nearby lifecycle events are all zero or absent. This points to a perceptually
intermittent but musically deterministic noise-layer collision rather than a
device underrun.

The page now exposes four unselected isolation modes. `Layered control` retains
both complete noise sources. Default `Snare priority` suppresses only a
paper-brush hit sharing a step with the brush snare. `Snare air only` mutes
every paper brush while preserving the snare triangle body and noise-air layer.
`Paper brush only` preserves every paper brush and the snare triangle body while
muting only the snare noise-air layer. Focused verification runs all four
through the same marked collision window, proves the expected played and
suppressed hit counts, and keeps every mode unclipped and scheduler-clean.

Four-mode listening on 2026-09-02 heard glitches around the same times in
every mode, so no single noise isolate is implicated and the noise-layer
collision reading no longer explains the artifact on its own. The listener's
directive is to identify what is constant at the marked times: `Snare
priority` marks at steps `49`, `89`, `226` on `landMinorCadence`; `Paper
brush only` marks at step `86` on `landMinorCadence` and steps `31`, `155` on
`landMajorCadence`. All marks precede what the listener calls the D6 change,
the point where the Am and C cadences branch into their own identities, so
they sit in shared material. The same session confirmed a distinct symptom:
clicking pause more often than not produces a crackle of static before the
sound ends. Source analysis validated against the logs then refuted the
two-noise-onset collision hypothesis (four of six source windows contain no
collision), left kick, brush snare, bass, and saw as the events constant in
every window, and identified the pause crackle's mechanism: the pause branch
calls `audioContext.suspend()` bare, with no fade, while stop and seek both
run a `90 ms` anchored fade. The isolation grid lacks a both-noise-muted
mode, so `playNoiseHit` is not exonerated. No repair or new mode is built;
evidence is recorded in the soundtrack worklog.

The reported second mechanism was distinct from the settle sweep rather than that
sweep returning: "random and not repeatable", very rare, one-off, possibly
present all along, where the settle sweep was reliably reproducible by reload.
`.officewars-audio-glitch-diagnosis-browser.py` excludes the page as its source.
Over `117 s` every rendered sample was inspected and the largest
sample-to-sample step was `0.1595` against a `0.35` click threshold; no late
steps were skipped, peak scheduler lag was `0 ms`, audio time drifted `+9.6 ms`
with no sustained render gap,
and the render thread produced `43,939` quanta against `43,914` expected at a
peak of 20 concurrent voices. The artifact did not reproduce, so the remaining
candidate is a device-level render underrun below what the page controls. All 60
compressor pages leave `latencyHint` at Chromium's default `interactive`, which
requests the smallest render buffer — `10 ms` measured, against `20 ms` for
`'playback'`. That is the one available mitigation, it is musically neutral on a
scratch copy, and it is **not approved and not applied**. Asked directly on
2026-08-27 the user answered "undecided because i dont hear any static anymore",
so the question stays open and its default is not applied. It would reduce
exposure; it cannot be shown to remove a defect that never reproduced.

The two active scene prototypes were repaired on 2026-08-27 with the user's
confirmation, so the pre-roll now covers every active branch rather than the Boss
A lineage alone. Each was measured on its own compressor first:
`prototypes/officewars-casino-scene-audition.html` takes `1.35 s` and went from
`94,403` bytes and `A06672D6` to `99,620` bytes and `D6AAF6D3`;
`prototypes/officewars-workday-development-audition.html` takes `1.25 s` and went
from `74,144` bytes and `69B6A05F` to `79,361` bytes and `A300260A`. Gain
reduction at the first note is now `-0.353 dB` on the Casino page against a
`-20.784 dB` sweep observed before the wait finished, and `-0.388 dB` on the
Workday page against `-16.501 dB`; the second play on each returns to the
ordinary `60 ms` lead. Because that wait is over a second of deliberate silence,
both transports read `WAIT` during it and repaint to `PAUSE` when the music
sounds, painted from the timeline interval because the wait ends on the audio
clock and dispatches no event. A wait that long also exposed a second readout
defect these pages share: the movement label is written only by the step
scheduler, so on a theme switch it went on naming the previous theme's movement
for the whole wait. It now reads `READY` until a step is actually scheduled.
Behaviour is asserted by `.officewars-compressor-settle-scene-browser.py`,
22 checks on each. The Casino
page has eight pre-existing uses of `??`, which the project's esprima grammar
predates, so a clean browser load is that page's only syntax check.

Two watchpoints carry forward. The opening is re-realized by this lineage's
engine rather than copied from the render, with per-instrument gains within
about `0.4 dB`. And because `intensity` was held byte-identical through the
kernel, the `3.6 dB` level ramp still does escalation work underneath the new
build.

The remaining open questions are how long the successful cadence destination
needs to continue, whether Am or C is stronger after adequate exposure, a
density-matched ensemble control, reducing the `3.6 dB` ramp, the cause of
the recurring static, and whether evidence supports `latencyHint:'playback'`.
Listening on 2026-09-02 reaffirmed that both cadence repairs are liked but
too short for the payoff to be realized, so length precedes the Am-versus-C
choice. The collision hypothesis is refuted and `latencyHint:'playback'`
remains deferred. The pause crackle is repaired and closed: pause ramps the
master bus to silence over `35 ms` of rendered time and suspends about
`60 ms` later, every resume path restores the gain over `20 ms`, in-browser
checks assert the amplitude at both ends, and listening on 2026-09-04
confirmed the crackle gone. The same session heard no static in the
fifth mode, `No noise percussion`, which suppresses both windowed-noise
layers and keeps the snare's triangle body — so the recurring static is
localized to the presence of windowed-noise percussion. Still open within
that: whether the cause is the audible noise signal or the source start/stop
churn those hits dominate. A sixth mode, `Silent noise percussion`, now
answers it: with user approval it schedules every noise hit exactly as
`Layered` — same timing, same source starts and stops — but at `SILENCE`
gain, so it keeps the churn while removing the signal. Static that survives
it implicates the churn; silence implicates the noise signal. The page hashes
`0E87C920`, is `110,825` bytes, and passes `330/330` plus the cadence settle
suite `29/29`. Nothing beyond the diagnostic treatments has been selected.

## Project Sound

OfficeWars places absurd pressure inside an ordinary workplace. Routine music
should keep the office warm and alive without exhausting the player. Decision
and danger music can reveal the ambition, temptation, and panic beneath the
mundane surface.

### Listening Preferences Learned Here

- Fluid melodic motion is more important than showy register jumps.
- A phrase should sound as though it knows where it is going.
- Bounce, forward motion, and danceable Casino energy are welcome.
- Large unexplained jumps make melodies feel stunted.
- Repetitive high-frequency tapping becomes irritating when it has no strong
  rhythmic role.
- Reduced-energy passages should preserve a pulse or musical thread.
- Emotional intent should be heard without requiring a technical explanation.
- Dynamic highs and lows work when the musical identity survives the change.

These preferences are reliable for current OfficeWars work. They may inform
future collaboration, but they should not silently become universal genre
rules.

## Selected Parent Leitmotif

`Sketch B` is the selected OfficeWars parent-leitmotif foundation. Its durable
identity is the connected nearby-step rise, prepared high point, and return
that behave as one singable melodic sentence. Preserve those relationships
rather than forcing one key, tempo, instrument, or complete phrase into every
cue.

The discovery lab established that B held its melody more naturally than
Candidates A and C. A depended more heavily on fragment repetition and delayed
completion, while C changed rhythmic footing often enough to weaken continuous
melodic ownership. A and C remain historical evidence and do not carry forward
as parent themes.

The 128-step, 104 BPM Sketch B Workday loop is the selected calm reference
expression of the parent, not the final Workday cue. Its arrangement,
long-exposure development, sound design, and game integration remain open.

The selected cross-scene transformation reference contains:

1. the exact four-phrase Sketch B Workday loop;
2. a 32-step, approximately 7.30-second bridge that accelerates from 104 to
   164 BPM; and
3. the exact selected Corporate Contraband Casino loop.

The bridge preserves and compresses B's sentence through its first three bars.
Its final bar transposes the rising relationship into `C-D-E-D`, then hands
its final `D` into Hook Payoff's opening `E`. Harmony, rhythm, lead sound, and
low-end ownership transfer gradually rather than resetting at one boundary.

The user found Sketch B recognizable after the scene transformation and
described the bridge as natural, identity-preserving, and strongly liked. This
selects both the parent foundation and the bridge as a cross-scene reference.
It does not replace Prepared Mirror or Corporate Contraband as the Casino's
scene-specific identity, approve final Workday production, or lock exact
in-game entrance timing.

## Scene Briefs

### Decision

The player should feel alert, confident, and slightly risky. Phrases can be
concise and active without reaching Casino density. Early Casino melodic DNA
may eventually fit this role, but no assignment is approved.

### Workday

The Workday should mix comfortable background listening with enough melodic
and rhythmic engagement to make watching coworkers move enjoyable. Its
emotional center is playful and fun rather than neutral office ambience.

Favor rounded timbres, restrained percussion, smooth bass, gentle development,
and low fatigue. The selected parent should remain easy to follow without
occupying the foreground continuously.

Restrained office funk is the selected Workday palette foundation. The user
found it the most fun and the most likely to remain enjoyable over long
listening, while identifying possible sleepiness at the original `104 BPM`.
The focused pace diagnostic selects Revision B's unchanged arrangement at
`112 BPM` as the pace foundation. Revision A's added syncopated motion also
contained an appealing quality, so its exact amount remains open.

Hybrid B is the selected Workday development foundation. It preserves the
selected melody, harmony, office-funk sound world, `112 BPM` pace, and
four-phrase form while using no added motion in Establish or Answer,
`55 percent` of Revision A's extra motion in Develop, and full motion in
Return. The user preferred this gradual lift to both the exact control and the
Return-only Hybrid A.

This selects a phrase-development architecture, not a complete arrangement,
production master, or shipped Workday cue. Long-exposure variation, complete
form, final sound design, mix, and game integration remain open.

`Workday Longform` Draft 01 expanded that foundation into a `512-step`,
approximately `2:17.14` A-B-C-A' loop:

1. Movement 1 preserves Hybrid B exactly.
2. Movement 2 introduces an offbeat secondary melody over related harmony.
3. Movement 3 reduces foreground exposure while retaining groove and pulse.
4. Movement 4 restores the parent and lets the secondary voice join it.

Human listening rejected Movement 2 and its transition as wonky, and rejected
Movement 3 as weak, sleepy, and fragmented. Movement 4's parent return with
the secondary counterline was liked. Draft 01's complete form and duration are
not selected because its rejected middle prevented a fair length judgment.

The subsequent form-repair audition preserved exact Movement 1 and the liked
Movement 4 return. It compared:

1. a `384-step`, approximately `1:42.86` Compact Rewrite with one new connected
   middle; and
2. a `512-step`, approximately `2:17.14` Extended Rewrite that adds one
   momentum movement before the same return.

Both rewrites shared the exact new connected middle. Human listening rejected
both as awkward, long, and stale. Their twelve melodic phrases were still
grouped into only three or four broad arrangement states, while the return
behaved like only two perceived states.

The active micro-movement audition keeps both candidates at `384` steps,
approximately `1:42.86`, and preserves the same twelve foreground phrases,
harmony, tempo, palette, and selected opening. It compares:

1. a Six-Movement Relay with one consequential turn every two phrases, or
   approximately `17.14` seconds; and
2. a Twelve-Movement Relay with every phrase receiving a distinct function,
   or approximately `8.57` seconds.

The return now progresses through recognition, answer, teamwork, and loop
preparation rather than waiting through one long parent-and-counterline state.
Both relays remain exploratory until human listening selects or rejects their
movement cadence.

Human listening found the Six- and Twelve-Movement relays comparable and
rejected Six-Movement Move 4. This does not select either cadence. The user
also described the shared musical world as potentially empty.

The support-role diagnosis tested arrangement support before rewriting melody
or form. In Six Move 4, short bass, chord, kick, and snare activity increases
while sustained pad support falls and no counterline enters. Candidate A added
two warm sustained inner voices per bar; Candidate B added eighteen restrained
phrase-ending reply attacks. Human listening found both treatments still
empty: the melody remained standalone, and the supporting instruments were
too subtle or ambiguous to communicate their identity or intention. Neither
treatment carries forward as the active solution.

The source-only Ensemble Lab keeps the selected 34-second Hybrid B foundation
controlled while comparing three recognizable backing casts: rounded
electric-piano behavior, percussive clavinet-like interlocks, and sustained
organ-like voicings. Human listening selected Ensemble C because its sustained
organ-like body and measured swells integrate with the melody's phrasing and
let the two roles uplift one another. Ensembles A and B sounded present without
creating the same reciprocal relationship and do not carry forward for this
role.

This selects Ensemble C as the Workday ensemble foundation. It does not approve
a complete cue, long-form structure, final production, gameplay masking, or
integration.

The source-only `Workday Relational Form Lab` extends that selected foundation
into a `384-step`, approximately `1:42.86` Draft 02. Its first
`128` steps preserve Ensemble C exactly. Six two-phrase movements then change
the melody-band relationship rather than merely adding density:

1. `Lead & Hold`;
2. `Lift Together`;
3. `Band Invites`;
4. `Roles Reverse`;
5. `Recognition`; and
6. `Teamwork`.

The middle derives its phrase language from the parent. The final four phrases
restore the exact parent foreground while developing the liked return
counterline through recognition, answer, cooperation, and loop preparation.
Draft 02 is technically verified but remains musically exploratory. Human
listening found the beginning of `Band Invites` and `Roles Reverse` awkward,
found the reversed `Roles Reverse` notes interesting, and heard a strange
moment in `Teamwork`.

The historical source-only `Workday Transition Repair Lab` preserves Draft 02 as
Version A and tests a coordinated Version B. Version B changes only three
handoffs: it resolves the preceding `B` to an organ `C` before `Band Invites`,
foreshadows and gradually transfers organ leadership into `Roles Reverse`
without changing its reversed foreground, and replaces Teamwork's
close-shadowing `8 / 6` counterline attacks with complementary `4 / 4`
harmonic anchors. Both complete forms and all six boundary clips are
technically verified.

Human listening found Version B slightly better but still short of the intended
cue. The local preparation repairs do not carry forward as a selected complete
solution. The full-scope diagnosis is that the organ still behaves primarily
as accompaniment while the lead remains continuously foregrounded.

The historical source-only `Workday Role Transfer Lab` preserves Transition Repair
Version B as exact Version A. Version B keeps every foreground pitch, chord,
tempo, movement, and Ensemble C foundation while changing musical ownership:

1. the repaired organ `C` continues through `D`, and the melody completes the
   invitation on `E`;
2. the organ performs the complete reversed phrase while the lead rests, then
   hands the following phrase back halfway through;
3. Recognition uses a reduced groove and low organ halo rather than repeating
   the opening arrangement; and
4. Teamwork uses two six-note lower-register replies that enter only in
   foreground gaps.

Both complete forms and all eight relationship clips are technically verified.
Human listening found Version B generally good, but rejected its jarring
invitation note and clash-heavy Role Reverse. Role Reverse is retired.

The subsequent source-only `Workday Band Answer Lab` preserved Role Transfer
Version B as exact Version A. Version B removed the added invitation `D` and
organ pickups, then replaced the reversal with an eight-note chord-tone organ
statement followed by a complete lead reply. Recognition and Teamwork remained
unchanged. Both forms and both focused clips passed technical verification.

Human listening rejected Band Answers outright. This rejects the replacement
material rather than merely its transition or mix. The organ should return to
the supportive, reciprocal Ensemble C role that was selected by listening.

The source-only `Workday Middle Melody Lab` performed that discovery before
another full-cue rebuild. It compared three initially anonymous `96-step`,
approximately `25.714-second` journeys at `112 BPM`. Every journey shares
Ensemble C, one `16-step` departure, one `16-step` return, duration, and output
architecture. Only the `64-step` two-phrase middle identity changes:

1. a fluid, mostly stepwise continuation;
2. a playful syncopated variation over the same middle harmony; and
3. a related harmonic detour that transforms the contour.

`Full Journey` and `Melody Only` controls expose each idea. Human listening
selected Candidate C. Its related harmonic detour is now the selected Workday
middle-melody foundation; Candidates A and B remain historical alternatives.

This selects Candidate C's exact middle melody, middle harmony, and reciprocal
relationship with Ensemble C. It does not approve the complete discovery
journey as the final cue, select a long-form structure or duration, finalize
arrangement or production, integrate music into gameplay, or mark a cue
shipped.

The historical source-only `Workday Candidate C Form Lab` develops those selected
foundations into a `256-step`, approximately `1:08.57` loop. Its eight
phrase-sized turns are `Settle In`, `Desk Banter`, `Detour Opens`, `Detour
Deepens`, `Thread Returns`, `Corner Turn`, `Parent Returns`, and `Full Groove`.

The first two and final two phrases preserve the parent exactly. `Detour
Opens` and `Detour Deepens` preserve Candidate C's selected `64-step` melody,
harmony, and roots exactly. Only `Thread Returns` and `Corner Turn` are new
C-derived development material. Ensemble C remains supportive, while Hybrid
B's exact `0 / 0 / 55% / 100%` motion arc operates across four 64-step macro
movements and the music makes a phrase-level turn every 32 steps.

The form passes focused technical verification, including all eight movement
starts and two uninterrupted loops. The complete form, two new development
phrases, duration, transitions, production, gameplay masking, integration,
and shipping remain exploratory until human listening.

Human listening found the original `Corner Turn` around 49 seconds
directionless. Its revised final bars now settle on `F-A-G-F`, descend through
the G7 chord as `F-D-B-D`, and enter the parent's `E` stepwise. The original
ending is rejected; this revised cadence remains exploratory. The Movement
Starts buttons now visibly follow the currently playing phrase and expose
`aria-current="step"` for the active movement.

Human listening then identified internal flow and transition weakness between
`Detour Opens` and `Detour Deepens`. The focused source-only Detour Flow Lab
keeps Candidate C's selected pitches, chords, and bass roots exact inside the
same `96-step`, approximately `25.714-second` context clip. It compares the
current articulation, a more connected lead treatment, and that connected
treatment plus a restrained organ `B-D` to `C-E` handoff at the G7-to-C6
boundary. The first blind listen liked all three but could not reliably
identify the differences. The page now durably reveals the shared material,
each treatment's exact mechanism, and what the active monitoring mode includes.
The listener then selected Passage D in the focused Detour Hybrid Lab. Its
phrase-role performance uses the original crisp articulation for closely
spaced notes, the connected articulation when a note has at least three steps
of room, connected endings at both Candidate C phrase boundaries, and the
exact restrained G7-to-C6 organ handoff.

This selects Passage D as the Workday detour performance foundation. A, B, and
C remain exact historical ingredients. The complete Candidate C form,
development phrases, duration, final production, gameplay integration, and
shipping remain open.

The selected source-only `Workday Passage D Form Lab` integrates that selected
treatment into the complete `256-step`, approximately `68.571-second`
Candidate C form. It preserves every note, chord, bass root, movement,
development phrase, revised `Corner Turn`, parent phrase, Ensemble C behavior,
`112 BPM` tempo, and Hybrid B motion value from the prior form.

Only Candidate C's performance changes: the exact 14 selected connected-note
positions and exact G7-to-C6 organ handoff are mapped into steps `64` through
`127`. The full form and Melody Only monitor pass all eight movement starts,
headroom, transport, rapid switching, responsive layout, two-loop, bounded
source, and cleanup checks. Human listening selected this exact composition
and form as the Workday form foundation.

Human listening selected Hybrid D as the standalone Workday production
foundation. It combines Production A's warmer lead, connected lead, and organ
with Production B's tighter bass and drums plus its cleaner delay, feedback,
and wet-space treatment.

The production changes no composition, form, harmony, tempo, movement,
Passage D behavior, Ensemble C role, or motion value. Its full verifier passes
all twelve layer modes, comparison level, 100-percent headroom, transport,
rapid switching, responsive layouts, two uninterrupted loops of all four
complete comparison versions, bounded source counts, and zero-source cleanup.

This selects the standalone production identity and mix relationship. Extended
fatigue testing during gameplay, gameplay masking, adaptive behavior, game
integration, and shipping remain open. The cue has not been added to
`officewarsautobattler.html`.

The source-only `Workday Long-Cycle Lab` begins every candidate with exact
Hybrid D and compares three anonymous `1024-step`, approximately `4:34.286`
supercycles:

1. exact Hybrid D repetition across all four loops;
2. below-conscious performance drift through organ phrasing, articulation,
   pocket variation, and a soft reset; and
3. a clearer relationship arc through organ response, rhythm response,
   ensemble reunion, and a prepared reset.

Every loop preserves the selected notes, harmony, roots, form, tempo,
Passage D, Ensemble C, motion arc, and Hybrid D production identity. All three
supercycles pass two complete wraps, headroom, transport, rapid switching,
responsive layout, bounded-source, and zero-source cleanup checks.

The comparison remains musically exploratory. Technical endurance does not
establish fatigue resistance or select a long-cycle strategy.

The focused source-only `Workday Long-Cycle Tribrid Lab` preserves exact
four-loop Hybrid D as its control and compares one three-strategy arc:

1. exact Hybrid D baseline;
2. restrained humanized organ phrasing and pocket drift;
3. organ-and-rhythm conversation; and
4. a stronger combined payoff with lower-register organ callbacks, followed
   by a prepared reset.

Both `1024-step`, approximately `4:34.286` candidates preserve the selected
notes, harmony, roots, form, tempo, Passage D, Ensemble C, Hybrid B motion
arc, production identity, and loop seam. Both pass direct loop starts, live
loop tracking, comparison level, headroom, transport, switching, responsive
layout, two complete supercycles, bounded sources, and cleanup to zero.

Human endurance listening selected the internal Tribrid D plan. Its exact
baseline, humanized second loop, conversational third loop, combined
fourth-loop payoff, and prepared reset now carry forward as the Workday
long-cycle treatment. The selected cue's player-facing title is
**On the Clock**. Exact four-loop Hybrid D remains its historical control.

This selects long-cycle development, not gameplay masking, device
translation, adaptive behavior, game integration, shipping, or final
delivery.

### Boss Floor

The boss-floor cue should transform the selected Workday foundation into a
distinct, very high-energy confrontation cue with many meaningful callbacks.
It should remind the player of ordinary office life without behaving like the
same arrangement at a faster tempo.

Reference study of Jacinthe Battle, `Hopes And Dreams`, and Champion Iris
supports these current design principles:

- establish a new boss hook, cadence, groove, or pressure engine that can stand
  without quotation;
- preserve Workday ancestry through transformed contour, cadence, harmony,
  articulation, organ relationship, or rhythmic behavior;
- give callbacks different jobs such as omen, propulsion, recognition,
  destabilization, payoff, and loop preparation;
- create energy through subdivision, bass and drum motion, harmonic rhythm,
  articulation, register, brightness, density, and faster section turnover,
  not tempo or loudness alone;
- retain enough contrast for the largest Workday statement to feel earned; and
- keep the loop compact and internally varied rather than continuously maximal.

The source-only `OfficeWars Boss Identity Lab` now compares three anonymous,
original `168 BPM`, `128-step`, approximately `22.857-second` sketches. Each
offers Full Sketch, Identity Only, and Callbacks Only modes so parent ancestry
and independent confrontation identity can be judged separately. Candidate A
uses broad rising pressure, Candidate B uses tactical syncopation, and
Candidate C uses volatile color and register changes. Every candidate includes
a transformed On the Clock contour and assigns callbacks different functions.

All nine modes pass audibility, comparison level, headroom, transport, rapid
switching, responsive layout, two uninterrupted loops, bounded-source, and
zero-source cleanup checks.

Human listening selected Boss A as the boss identity foundation because its
broad rising hook was by far the most melodic. Boss B and Boss C remain
historical pressure and color studies rather than equal protagonists.
Human listening rejected the first Boss A Persistent Thread form. Its regular
short-note ancestry voice sounded like a ding or metronome, and its later
movements replaced too much of the selected Boss A identity.

The historical Boss A Undercurrent Repair Lab preserves the exact
selected identity as a direct control and tests a conservative `512-step`,
approximately `91.429-second` form at `168 BPM`. Every movement keeps Boss A's
selected melodic sentence and harmonic route as its spine. Energy develops
through arrangement, register, restrained fills, and macro intensity rather
than replacement melodies.

On the Clock ancestry now uses one sustained chord-tone organ onset per bar,
slow sine or triangle envelopes, bass relationship, and cadence. There is no
square-wave or high-octave ping voice. Full Repair, Boss A Core, and
Undercurrent Only modes expose the layer's contribution.

All four modes pass protected-source, exact-identity, chord-tone, envelope,
comparison-level, headroom, transport, rapid-switching, responsive-layout,
two-loop, bounded-source, and zero-source cleanup checks. The repair is
technically stable, and the user likes its tune, but its remaining high
square-wave percussion still sounded like a constant metronome.

The paper-brush percussion pass preserved that complete tune, undercurrent,
harmony, form, bass, and mix while replacing only the tonal offbeat hat and
snare edge. Human listening liked the integrated result but reported an
occasional static pop. Source inspection found a discontinuous `32 percent`
gain drop inside every deterministic noise hit. That artifact moved through
Limbo and is now Rejected because its liked material is preserved in a new
Test.

The Boss A Pop Repair Lab compared the exact rejected paper-brush control
against `OW-MUSIC-BOSS-A-POP-REPAIR`. The Test changed only that
instantaneous gain drop into a continuous exponential decay. It retains the
same brush rhythm, deterministic noise, offsets, filters, melody, harmony,
bass, undercurrent, form, and mix. Pop Brush Only and Smooth Brush Only
monitors expose the envelope difference.

The browser-rendered envelope diagnostic measures the rejected transition at
`0.32` and the smooth transition at `0.003025`. The focused and complete
repeated-loop gates pass across both full mixes and both isolated monitors.
Human listening still heard an inconsistent pop that could disappear after
manual seeking. The envelope repair is therefore Rejected history rather than
the active solution.

The Boss A Scheduler Repair Lab compared that exact smooth-brush predecessor
against `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`. A delayed main-thread tick can
leave the old scheduler behind its `180ms` look-ahead horizon. Its
catch-up loop then schedules every overdue step, while each late voice clamps
to the same near-future timestamp.

During a forced `900ms` stall, the Rejected control scheduled five steps in
one tick and peaked at 36 tracked sources. Manual seek created a fresh state
and reset the peak to 13, matching the user's observation. The Test advanced
past four overdue steps, scheduled only one current step, and stayed at the
normal 21-source peak. All four modes pass focused and two-loop verification.
Human listening still heard intermittent pops, so the scheduler repair is now
Rejected history at
`Music Legacy/officewars-boss-a-scheduler-repair-audition.html`.

The pre-rendered Test still contained baked one-sample impulses where
deterministic percussion slices began away from zero. Windowing every brush and
snare slice to zero at both boundaries removed all `76` adjacent-sample jumps
above `0.02` and reduced the maximum jump from `0.199` to `0.0081`.

Human listening confirmed that the repaired cue has no remaining static and
that the tune works. The exact fixed render is therefore Approved at
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`. Its
self-contained page uses one cached buffer source, completes two verified
loops, and has no external audio or script dependency. Game integration,
shipping, adaptive behavior, and final delivery remain open. Evidence is recorded
in `verification/BOSS_REFERENCE_ANALYSIS_2026-08-18.md`,
`verification/BOSS_IDENTITY_DISCOVERY_2026-08-18.md`, and
`verification/BOSS_IDENTITY_SELECTION_2026-08-18.md`, with form-development
history in `verification/BOSS_A_FORM_DISCOVERY_2026-08-19.md`, undercurrent
history in `verification/BOSS_A_UNDERCURRENT_REPAIR_2026-08-19.md`, and active
paper-brush history in
`verification/BOSS_A_PERCUSSION_REPAIR_2026-08-19.md`. The pop-repair evidence
is `verification/BOSS_A_POP_REPAIR_2026-08-19.md`; scheduler-repair evidence is
`verification/BOSS_A_SCHEDULER_REPAIR_2026-08-19.md`; pre-render evidence is
`verification/BOSS_A_PRERENDER_REPAIR_2026-08-19.md`; final approval evidence
is `verification/BOSS_A_WINDOWED_PERCUSSION_APPROVAL_2026-08-19.md`.

Human listening later found the revised `Finding Footing` direction promising
but rejected `Pressure Turn`, `Melodic Drive`, and `Full Statement` because
they felt strange, did not form a satisfying tune, and did not read as a Boss
song. The mechanically motif-led Melodic Throughline is therefore Rejected
history and the direct listening control at
`Music Legacy/officewars-boss-a-melodic-throughline-audition.html`.

Human listening later rejected Continuous Tune after Challenge Issued. Its
full ensemble increased scale, but the post-opening foreground remained one
continuous triangle-and-sine soloist. That did not preserve the opening's
strongest compositional behavior: broad saw phrases, bright callback notes,
bass, harmony, and impact assembling the identity through changing roles.

Human listening found all three Opening Grammar candidates closer, but
rejected their tunes and handoffs as still too far from Challenge Issued.
That audition is now the direct Rejected control.

Next Movement compared three lengths and three seam voicings of one new
movement. Diagnosis then found that all three candidates recombined the same
quoted opening cell, so the comparison could not be answered by listening. It
also carried two agent-invented constraints the user never asked for: an apex
cap at MIDI `81`, which excluded the opening's own top two pitches, and a total
ban on deliberate breath. `OW-MUSIC-BOSS-A-NEXT-MOVEMENT-DISCOVERY` is
therefore Rejected and retained as the exact control for the quotation defect.

The A/B/B2/C discovery page is Rejected at
`Music Legacy/officewars-boss-a-second-movement-sketches.html`. It remains the
exact source and direct control for the later Rejected repair.

The Rejected `OW-MUSIC-BOSS-A-INTENSITY-3-REPAIR` control is at
`Music Legacy/officewars-boss-a-intensity-3-repair.html`. It preserves exact
B2 Control, three repairs that preserve B2 through step `27`, and exact A as a
function reference.

Human listening likes Sketches A and B, prefers B's opening to A's, rejects
Sketch C and B's gear change, then rejects B2 from `Intensity 3` onward because
the upper voices clash with themselves and E6 does not fit this track. No
repair is selected, and no music has entered the game.

The ratified next sequence is:

1. measure exact live Sketch A and compare the current palette against at most
   one minimally corrected, matched-level treatment;
2. keep a coherent melody-only reduction as a rejection gate; and
3. after the palette result, compare only two kernels: the merged connected
   sentence/two-voices-finish-each-other architecture and riff into sentence
   developing Sketch A.

The distributed architecture with no coherent single-voice reduction is
retired for this round. No palette correction value or kernel is selected.

The user clarifies that Player identity may be carried across the ensemble
while the bright triangle remains selective; triangle does not need to lead
every phrase. Listening on 2026-08-26 extended that to the mix: the render's
`gainMultiplier:1.12` put the bright triangle `0.98 dB` above the saw, and the
user rejected it because "the triangle was inserting itself as more important
than the melody so it took the spotlight". The selected balance is `0.86`,
which is `2.29 dB` below the render and `1.31 dB` below the saw. Boss A material
built from here uses `0.86`, not the render's `1.12`; the protected notes and
the `11.429 s` triangle entry are unaffected, since only gain changed. After a
movement survives standalone listening, a future Test may
use DJ-style phrase-matched overlap by adding one pickup during the opening's
final bar. The exact Approved rollback artifact remains byte-identical, and the
overlay may not rewrite or replace an opening event.

The same listening pass rejected the offbeat percussion as sounding like a
metronome. The cause was a fixed-level pitched square tone on every offbeat:
the sketch page had copied the fallback branch of the Approved cue's scheduler
instead of the brush branch the cue actually plays. The page now uses the
Approved cue's own windowed-noise paper brush on its own alternating
`[1, 3, 6]` and `[1, 4, 7]` figure, with per-hit band, pan, and noise-offset
variation, accents, and intensity scaling. The square tick survives only as a
labelled rejected control for A/B comparison. Evidence is
`verification/BOSS_A_NEXT_MOVEMENT_DISCOVERY_2026-08-21.md` for the retired
audition and the plan document for the sketches.

### Night

Night should feel private, warm, relieved, and sleepy without becoming empty or
melancholy. Softer attacks, slower motion, warm registers, and a quiet sense of
life suit the Home scene.

### Casino

The player is gambling on company time, knows they should stop, and keeps
putting money in because exhilaration overwhelms restraint.

The emotional priority is:

1. exhilaration;
2. addictive panic;
3. anticipation;
4. unpredictability; and
5. emotional scale.

Festival Hybrid is the approved ordinary-Casino energy family. The broad arc
begins mischievous and restrained, accelerates into temptation, releases into
dance-forward euphoria, briefly loses weight without losing continuity, and
returns in a larger unstable wave.

### Redline

Redline is the Casino identity after safety disappears. It should feel
desperate and dangerous rather than celebratory. Increase subdivision, bass
pressure, harmonic instability, and urgency while preserving the recognizable
motif and groove.

Redline becomes eligible after a settled gambling result leaves current cash
plus chips at 25 percent or less of Casino Starting Wealth. Casino Starting
Wealth is the cash plus chips present when the visit begins; moving money
between cash and chips does not count as loss.

The faster Redline role is approved. The current 174 BPM audition value is not
a locked shipping tempo.

## Current Casino State

### Selected Foundation

`Prepared Mirror` is the selected Casino motif foundation. This approves the
core phrase identity, not a complete cue.

The phrase develops an obsessive descending idea, allows the descent to
complete, gives the answer a separate role, and returns to the established
completion without the mechanical hinge heard in `Obsession into Mirror`.
The user said it was good and felt disappointed when it ended.

### Rejected Control

`Prepared Mirror: Second Pass` repeats the same melody, harmony, and phrase
function while gradually adding upper sheen and octave shadow. It was
technically stable but became repetitive.

Its active lesson is that timbral and orchestration growth cannot substitute
for horizontal phrase development. It remains historical evidence and is no
longer shown on the active focused page.

### Selected Phrase Two

`Prepared Mirror: Answer Development` is the selected phrase-two foundation.
This selects the melodic continuation, not a complete cue.

Its first 48 steps preserve Prepared Mirror exactly. Its second 48 steps make
the existing answer become the new obsession:

1. `C-D`;
2. `C-D-E`;
3. `C-D-E-D`;
4. `D-C-B-A`;
5. `B-C-D`; and
6. `E-D-C-B-A`.

The working 154 BPM tempo, harmony, backing groove, instruments, output level,
rhythmic vocabulary, and final loop pull remain fixed. The candidate adds no
sheen, octave doubling, percussion, or arrangement growth.

The user heard phrase two as a continuation with its own good identity. It was
fun and made another phrase desirable, but the energy did not meaningfully
rise. That is why it is a foundation rather than a finished development arc.

### Melodic Control

`Prepared Mirror: Pressure Phrase` remains the exact melodic control. It is
not approved soundtrack music.

It preserves the selected first 96 steps exactly, then adds:

1. `E-D-E-D`;
2. `C-D-E-D-E`;
3. `E-D-C-D-E-D`;
4. `D-C-B-C-D-C-B`;
5. `B-C-D-E-D-C-B`; and
6. `E-D-C-B-D-B-C-D`.

The third phrase increases from four melodic attacks to eight, compressing
familiar shapes without adding instruments or production layers. Its final
`B-C-D` points into the loop-opening `E`.

It remains useful because Compulsion Arc preserves all of these foreground
notes. The A/B therefore isolates what the selected arrangement relationship
adds without claiming that Pressure Phrase is independently approved as the
final melodic form.

### Selected Arrangement Foundation

`Prepared Mirror: Compulsion Arc` is the selected arrangement foundation. It
is not an approved complete cue.

It preserves Pressure Phrase's complete 144-step foreground note plan,
harmony, 154 BPM tempo, 28.05-second length, and output target. Arrangement is
the only coordinated hypothesis:

1. **Rush** establishes the four-on-the-floor kick and complete offbeat bass
   engine.
2. **Fixation** adds a repeating midrange chord-tone hook without replacing
   the foreground motif.
3. **Panic** adds syncopated kick pickups, faster bass answers, and restrained
   extra snare motion.
4. **Panic Learns the Hook** lets the established `C-D-E` answer enter as a
   gradually clearer counterline.

The candidate stops there. It does not import the historical Panic Morph,
Release, or Overshoot ending.

The A/B passed its arrangement question. The user heard genuine energy
movement beyond Pressure Phrase, could identify the movements without relying
on their labels, and felt Panic learning the hook worked. The candidate still
felt slow for the user's taste despite its 154 BPM tempo. This selects the
causal arrangement relationship without approving the current transition
cadence, complete form, or final tempo.

### Selected Answer Chase And Festival Contour

The Answer Chase diagnostic resolved its question. Both quieter candidates
removed the excessive beeping, and the no-reply version retained a good vibe.
The five softer Echoes and their handoff were not perceptibly different.

`Chase Breathing` is therefore the selected Answer Chase foundation:

- 30 foreground attacks;
- no additional reply voice; and
- the established backing engine and lead sound unchanged.

Previous Clean and Chase Echoes remain historical controls. The Echoes do not
carry forward because they added no audible value. This locks only Answer
Chase at that point in the process; the later Festival Contour selection
resolves the complete ordinary-Casino loop.

The consolidated full-loop listen established four limited findings:

- the four movements feel distinct but related;
- the tune is fun;
- repetition remains enjoyable; and
- Hook Payoff re-entry is fun, but not clearly satisfying as a payoff.

The user could not identify where the larger energy rose or fell. This
preserves the foreground as selected material and moves the earliest broken
decision to arrangement contour.

The user selected `Festival Contour` after hearing and preferring its larger
energy journey. It is now the selected ordinary-Casino loop rather than an
active diagnostic.

The selection locks:

- 164 BPM;
- the exact 192-step foreground and 24-bar, approximately 35.12-second form;
- four six-bar movements;
- Chase Breathing with 30 foreground attacks and no reply voice;
- the cleaned late False Confidence and Compulsive Return;
- the macro contour across Hook Payoff, Answer Chase, False Confidence, and
  Compulsive Return;
- the continuous seam treatment; and
- the final `D -> E` return.

`Festival Foundation` remains historical evidence and is no longer shown on
the focused page. The current audition preserves only Festival Contour as the
composition reference for future Casino work.

This is a composition selection, not final production approval. Instrument
design, sound design, mix, entrance behavior, Redline, event stingers, bust
and cash-out behavior, and game integration remain separate decisions.

### Selected Production

`Corporate Contraband` Production Pass 06 is the selected ordinary-Casino
production built on the selected Festival Contour composition. It preserves
the exact locked tempo, foreground, movement boundaries, contour, seam, and
final return. It changes only the instrument cast, spatial treatment, sound
design, and mix behavior.

The selected production establishes a coordinated OfficeWars identity:

- a digital motif attack with warmer lower-body support;
- a club-focused kick and elastic mono bass;
- restrained office-and-casino transition gestures;
- movement-aware width, filtering, and space; and
- no continuous high-frequency tapping layer.

The focused page preserves the final Corporate Contraband production beside
the Festival Contour production control and retains its movement starts and
Layer Inspector as diagnostic evidence. Future work should not reopen the
ordinary-Casino composition, production identity, or loudness calibration
unless new in-game evidence reveals a specific problem.

Production Pass 06 is the selected loudness calibration. Pass 05 preserved the
stronger linear 50-percent volume curve, repaired the static-prone short-note
envelopes, and used `9.75x` shared pre-compressor makeup. The user still found
that level loud and approved a target equal to twice Pass 02's documented
50-percent signal path.

Pass 02 combined `12x` makeup with approximately `0.261` master gain at
50 percent, for `3.132x` effective pre-compressor gain. Pass 06 therefore uses
exactly `6.264x`. This is approximately `3.84 dB` below Pass 05 and preserves
the A/B relationship, composition, production identities, linear volume
curve, limiter, saved-volume profile, and repaired monotonic envelopes. In the
final passing run at 50 percent, the candidate full mix averaged `0.073415`
against the reference's `0.069196`.

The user called Pass 06 perfect. This locks the Corporate Contraband
instrument cast, spatial treatment, sound design, mix relationship, repaired
envelopes, and `6.264x` calibration as the selected ordinary-Casino
production. It is not yet shipped or integrated into gameplay.

### Preserved Entrance Discovery

The source-only `Casino Scene Music Lab` is the preserved earlier entrance
diagnostic.
It preserves the complete selected Corporate Contraband loop and compares
three musically unselected starts:

1. `Direct Start` begins immediately on Hook Payoff at 164 BPM.
2. `Quickening Lift` uses a 16-step, approximately 3.02-second restrained
   motif entrance that accelerates from 154 to 164 BPM.
3. `Office Signal Transform` uses a 16-step, approximately 2.93-second
   workplace-notification gesture that becomes the Casino answer at 164 BPM.

Both authored entrances hand into the exact selected 192-step loop at step 16,
then repeat only that loop. They preserve the locked foreground, production
treatment, movement contour, `D -> E` return, Pass 06 calibration, and
continuous pulse. None of those three starts is selected. The newer Sketch B
bridge is the selected cross-scene transformation reference, while exact
in-game entrance timing and synchronization remain open.

### Selected Arrangement Reference

The historical `Casino Compulsion Engine - Panic Morph` contains one selected
movement arc:

`Rush -> Fixation -> Panic -> Panic Learns the Hook`

The user likes the tune through that sequence and the sense that each movement
causes the next. Its strongest idea is relational: Panic does not merely become
busier; it learns and absorbs the established hook.

The later `Panic Morph -> Release -> Overshoot` tune remains usable source
material, but those labels do not match what the music communicates. Do not
assume that material performs a morph, release, or overshoot. If it returns,
use neutral structural labels until listening establishes its actual function.

Compulsion Arc applies this reference to Prepared Mirror's own material while
retaining Pressure Phrase as the exact melodic control. The relationship is
selected; neither the historical Panic Morph cue nor the current Compulsion
Arc is approved as a complete composition.

### Open Decisions

- whether Direct Start, Quickening Lift, or Office Signal Transform should
  remain useful as implementation controls beside the selected Sketch B
  cross-scene bridge;
- final Redline tempo, form, and relationship to the selected loop;
- exact Redline transition timing and sync point;
- whether Redline can revert during a visit;
- musical behavior on bust, cash-out, and leaving;
- event stingers and transition accents;
- whether earlier Casino material becomes Decision music.

## Durable Casino Lessons

- Fluid melodic continuity is the strongest existing quality.
- A one-bar high ended before the user could enjoy its impact.
- A longer payoff can create appetite, but duration alone does not create
  emotional purpose.
- More layers, speed, or measured signal do not automatically create urgency.
- A buildup and payoff need an audible emotional relationship.
- Near-silent fakeouts interrupt the dance impulse.
- Crashes and gradual comedowns both fail when phrase, harmony, and groove do
  not land together.
- Changing register, harmony, groove, and palette at one boundary makes a
  transition feel constructed.
- Adding activity does not create a stronger final reward.
- `Obsessive Fragment` carried distinctive compulsion but created too many
  opportunities to mishandle withheld completion.
- `Prepared Mirror` kept that identity while making completion and response
  easier to follow.
- Phrase development gave Answer Development its own identity, but did not by
  itself raise the energy. The next phrase must change momentum as well as
  content.
- A convincing escalation can come from one musical role learning another
  role's hook. That relationship creates more purpose than simply adding
  density.
- A numerically fast tempo can still feel slow when consequential arrangement
  changes are far apart. Perceived pace depends on event cadence, subdivision,
  articulation, and development as well as BPM.
- A foreground phrase and its reply layer can each sound reasonable alone but
  become exhausting together. Reduce role overlap before redesigning timbre.
- When a supporting layer is not perceptibly different and the simpler version
  already succeeds, preserve the simpler arrangement.
- Section names are hypotheses, not evidence. If a passage called Release does
  not feel like release, preserve any good music but discard the misleading
  function label.

## Working Files And Evidence

Selected Workday middle-melody reference:

`Music Locked/officewars-workday-middle-melody-audition.html`

SHA-256:

`021B8B9742D6AA8BFC958AA41D6E3D7504E969F1A3328769EF6F3188784D146E`

Focused Workday middle-melody verifier:

`.officewars-workday-middle-melody-verify.py`

SHA-256:

`6AB5230F8E6B827AD871A7CA67B4D4937787AAFDE415EECF74E7F1CB224996F0`

Selection evidence:

`verification/WORKDAY_MIDDLE_MELODY_DISCOVERY_2026-08-17.md`

Selected Workday form reference:

`Music Locked/officewars-workday-candidate-c-passage-d-form-audition.html`

SHA-256:

`4318ABBEE409D299CA90F86FF4248CA295C2A9DC6AE77005FD094C22A56476D0`

Focused Passage D integrated form verifier:

`.officewars-workday-candidate-c-passage-d-form-verify.py`

SHA-256:

`BE108F962600A675D8E01BC5ADEC7DFDF2B0FD156675637B8C4CB2A9322BC55F`

Integration evidence:

`verification/WORKDAY_CANDIDATE_C_PASSAGE_D_FORM_2026-08-18.md`

Selection evidence:

`verification/WORKDAY_FORM_FOUNDATION_SELECTION_2026-08-18.md`

Selected Workday production reference:

`Music Locked/officewars-workday-production-hybrid-audition.html`

SHA-256:

`8BE0BB035799450ABED8FCA13A5F1BF40634FB54DE65EDD4F019F6DD17610D1B`

Focused Workday production hybrid verifier:

`.officewars-workday-production-hybrid-verify.py`

SHA-256:

`C29E0567F43ADC21760BD53AA3FF5AF5C538B2F1FE7C839312DA41BC4493518C`

Selection evidence:

`verification/WORKDAY_PRODUCTION_HYBRID_SELECTION_2026-08-18.md`

Exploratory Workday long-cycle audition:

`Music Legacy/officewars-workday-long-cycle-audition.html`

SHA-256:

`40C7103DEEFEB3E80A95C7D506356523A93D2C8D5E442D25DF93C4D00AAC8B02`

Focused Workday long-cycle verifier:

`.officewars-workday-long-cycle-verify.py`

SHA-256:

`DB6AC0232187EAA2D46ABC31D9D4F2841AE73B25DA89AF54C672600DFA78F545`

Long-cycle evidence:

`verification/WORKDAY_LONG_CYCLE_DISCOVERY_2026-08-18.md`

Focused Workday long-cycle tribrid audition:

`Music Locked/officewars-workday-long-cycle-tribrid-audition.html`

SHA-256:

`60DDDF210B65CFEDD80664CB765F8E42418B79AE00FB952183E0CB3E92DE4E39`

Focused Workday long-cycle tribrid verifier:

`.officewars-workday-long-cycle-tribrid-verify.py`

SHA-256:

`3C7E1D9AD0A8C87D2866A58D6A8B0F70D6375AD8719261398ECE8156A80AA6D8`

Tribrid discovery evidence:

`verification/WORKDAY_LONG_CYCLE_TRIBRID_DISCOVERY_2026-08-18.md`

Tribrid selection evidence:

`verification/WORKDAY_LONG_CYCLE_TRIBRID_SELECTION_2026-08-18.md`

Workday title-selection evidence:

`verification/WORKDAY_TITLE_SELECTION_2026-08-18.md`

Selected boss identity audition:

`Music Locked/officewars-boss-identity-audition.html`

SHA-256:

`94475C64CE37353EAAB68741A844429EDE3C6D9D709084BE3363112018C8F941`

Focused boss identity verifier:

`.officewars-boss-identity-verify.py`

SHA-256:

`FE1CA73A7D195168C972C78A2D816CDD668077E8B27A70F9B3BA183B00E2A826`

Boss identity discovery evidence:

`verification/BOSS_IDENTITY_DISCOVERY_2026-08-18.md`

Boss identity selection evidence:

`verification/BOSS_IDENTITY_SELECTION_2026-08-18.md`

Rejected Boss A Intensity 3 repair:

`Music Legacy/officewars-boss-a-intensity-3-repair.html`

SHA-256:

`BCB08FB59935E427F86EAFE2B7C3A675C2F1B0A7F7CF6AECDC855D1DB8129A2C`

Intensity 3 repair direction, gates, and open questions:

`docs/music/officewars/BOSS_A_SECOND_MOVEMENT_PLAN.md`

Intensity 3 static and browser checks:

`.officewars-boss-a-intensity-3-repair-verify.py` and
`.officewars-boss-a-intensity-3-repair-browser-check.py`

Retained Next Movement listening control:

`Music Legacy/officewars-boss-a-next-movement-audition.html`

SHA-256:

`17DB249CAEA06234D8D2704066F1CE9979EDB5D2729B30333123DFE140425CCE`

Next-movement evidence:

`verification/BOSS_A_NEXT_MOVEMENT_DISCOVERY_2026-08-21.md`

Retained Opening Grammar listening control:

`Music Legacy/officewars-boss-a-opening-grammar-audition.html`

SHA-256:

`9A20B700179DF8B58080A974341BEBCACE3894B49F289A391F697E1C47DA89C2`

Retained Continuous Tune listening control:

`Music Legacy/officewars-boss-a-continuous-tune-audition.html`

SHA-256:

`1D7970C637D40A687E6E0F6E3BBF599467968D1F1092B16913032B3009BECD60`

Tune-discovery evidence:

`verification/BOSS_A_TUNE_DISCOVERY_TEST_2026-08-21.md`

Retained Melodic Throughline listening control:

`Music Legacy/officewars-boss-a-melodic-throughline-audition.html`

SHA-256:

`7EA17F521AEFA9772C9BC7A82F357819098901B70563A39DF41EBBF959B332B5`

Embedded control-audio SHA-256:

`DF60B8A506EAF48D52A924A9CEF10D797A3957A02C0FBC414EC5BD0425CBEE1D`

Focused Melodic Throughline control verifier:

`.officewars-boss-a-melodic-throughline-verify.py`

SHA-256:

`9FB7FD21765BC0CDC15AB58C91171DF6E13167C0D722C7AEB7BC167DB7FC926F`

Melodic-throughline history:

`verification/BOSS_A_MELODIC_THROUGHLINE_TEST_2026-08-20.md`

Retained Status Story listening control:

`Music Legacy/officewars-boss-a-status-story-audition.html`

SHA-256:

`9798FDEE52A036F404F1604E626AE52F1EF4B5C616056D4933C568C9F4986CF7`

Embedded control-audio SHA-256:

`8126F90F379FCFA6D065736C21A229672E9E702B3767DC4CD543BDDE58542DD1`

Focused Status Story control verifier:

`.officewars-boss-a-status-story-verify.py`

SHA-256:

`1F392069401BA298226D3412B20301C96E72E64F3AF11B924FA2CF384292488CC`

Retained Elastic Story listening control:

`Music Legacy/officewars-boss-a-elastic-story-audition.html`

SHA-256:

`B329E3EA6389336349A8A706BE2BE5CE0ACC3F82FF2E29882BE63B7963BE8459`

Embedded control-audio SHA-256:

`2F89A24CACA693A3C7208E8784E2DE29F79AF96991C5259EC62070C57EEC9C63`

Preserved rejected Boss A persistent-thread form audition:

`Music Legacy/officewars-boss-a-form-audition.html`

SHA-256:

`B24B0C8328837B65062BC377B5FDBA5F0A5DDD44482F52EEEE31C2F2BD14E1CA`

Focused Boss A form verifier:

`.officewars-boss-a-form-verify.py`

SHA-256:

`4F2FB403170E5528F95330A6799A32621CBB6B4BF2B45C39AA9F49BC2868BB44`

Boss A form discovery evidence:

`verification/BOSS_A_FORM_DISCOVERY_2026-08-19.md`

Rejected Boss A integrated-undercurrent history:

`Music Legacy/officewars-boss-a-undercurrent-repair-audition.html`

SHA-256:

`75A89448B43A14CB02E9A02B931B4C57D536B63D0001B3522BB724294A59051D`

Focused Boss A undercurrent-repair verifier:

`.officewars-boss-a-undercurrent-repair-verify.py`

SHA-256:

`99789F584B2A1B89C110062464EB53166DD4086000EF959DA752466A4B26382E`

Boss A undercurrent-repair evidence:

`verification/BOSS_A_UNDERCURRENT_REPAIR_2026-08-19.md`

Preserved Candidate C form control:

`Music Legacy/officewars-workday-candidate-c-form-audition.html`

SHA-256:

`2C3BDB5D4A59CE15567014EEE2A82B7077D42CFA59D4451558F00163EC08315D`

Preserved Candidate C form verifier:

`.officewars-workday-candidate-c-form-verify.py`

SHA-256:

`D03A77FEBCF9F596D2F4CAC2210C9429FB37B940CC4EFC26EA71D0CD0377912E`

Preserved form evidence:

`verification/WORKDAY_CANDIDATE_C_FORM_DISCOVERY_2026-08-18.md`

Corner Turn and movement-highlight refinement evidence:

`verification/WORKDAY_CANDIDATE_C_FORM_REFINEMENT_2026-08-18.md`

Historical Workday detour-flow audition:

`Music Legacy/officewars-workday-detour-flow-audition.html`

SHA-256:

`523D39EF30696E542D422B9A080D77EFC2340EBA8B9BB19EED2D2A1E7A756ACA`

Focused Workday detour-flow verifier:

`.officewars-workday-detour-flow-verify.py`

SHA-256:

`7C874203CCD0C53F5CB4FABC11ACBC188D51746CAD7E5B76BE80235E1E960AE1`

Detour-flow evidence:

`verification/WORKDAY_DETOUR_FLOW_DISCOVERY_2026-08-18.md`

Post-blind reveal evidence:

`verification/WORKDAY_DETOUR_FLOW_REVEAL_2026-08-18.md`

Selected Workday detour-treatment reference:

`Music Locked/officewars-workday-detour-hybrid-audition.html`

SHA-256:

`60B750603AED03BCD927A93F7441F1BB658F100AC857F41F8E54824EA75CFCB8`

Focused Workday detour-hybrid verifier:

`.officewars-workday-detour-hybrid-verify.py`

SHA-256:

`321E21AF58319B38038A51711B025D07578016FA8BF90B8B76A539277801AD66`

Selection evidence:

`verification/WORKDAY_DETOUR_HYBRID_SELECTION_2026-08-18.md`

Preserved Workday transition-repair audition:

`Music Legacy/officewars-workday-transition-repair-audition.html`

SHA-256:

`F9D0B935D2D3A9A7DE8E3EC534362D2A39E5279FBF4355E5C05B9852010BFBE9`

Focused Workday transition-repair verifier:

`.officewars-workday-transition-repair-verify.py`

SHA-256:

`0633FFCA9EB58281B5BED21DA0D3F0795E3949E7BE6FCDC435FCB5D91522779B`

Protected Workday relational-form control:

`Music Legacy/officewars-workday-relational-form-audition.html`

SHA-256:

`AA0DDF1A9F1EFE629CE4E0BC108902533760F14339294C91BB82AF9463270DEB`

Selected Workday ensemble reference:

`Music Locked/officewars-workday-ensemble-audition.html`

SHA-256:

`29283F405A18DE320361BD91500626B494B8008A44921C368CC742DD9D4E9A9D`

Focused Workday ensemble-identity verifier:

`.officewars-workday-ensemble-verify.py`

SHA-256:

`1CA4ED9D6EA4A55F48A48684B99D5E052384F21A84AB608F9D147BB01D7E45AE`

Insufficiently distinct Workday support-role audition:

`Music Legacy/officewars-workday-support-audition.html`

SHA-256:

`31938B99EA60F7658FC170EEA08AE6771F29BB22CB424B15A77800D61C37626D`

Focused Workday support-role verifier:

`.officewars-workday-support-verify.py`

SHA-256:

`3B4E8F317555A6924F6528DFCE34E5698AFD8DD609DFE226D63D8BE2FE109A14`

Unresolved Workday micro-movement audition:

`Music Legacy/officewars-workday-microform-audition.html`

SHA-256:

`F733F0E303D5FA01726769D0427C86F2F92E070F8A975E985E3CEA4B227EBD4A`

Focused Workday micro-movement verifier:

`.officewars-workday-microform-verify.py`

SHA-256:

`8C3E73D92346EFF5916F1E82958689DE65BBF54FA811ACE2A08F2F00F1A3E668`

Rejected Workday form-repair audition:

`Music Legacy/officewars-workday-form-repair-audition.html`

SHA-256:

`37CE0BCC15E49CB49D76D79D4B8DB9184A4071E023E57A2080427C6B9AC74B2D`

Focused Workday form-repair verifier:

`.officewars-workday-form-repair-verify.py`

SHA-256:

`435569E03ABA1C10CF5C30130A7251375AA5C6713FE9F821DB4511F4E09A0550`

Rejected Workday Draft 01 audition:

`Music Legacy/officewars-workday-cue-audition.html`

SHA-256:

`281A894D6049777D39DF0F41CE982E767EE6B97A16EA4560DEC604064EDBD064`

Draft 01 verifier:

`.officewars-workday-cue-verify.py`

SHA-256:

`CF3B62C82CA85B266BFC223CD1C76DFBD8F55B979C8D462943212C838076D893`

Selected Workday development reference:

`Music Locked/officewars-workday-hybrid-audition.html`

SHA-256:

`7F777F7F20B455EFE170CEF983704B409F71DF98AFD82DE22FE1E02983762E67`

Focused Workday hybrid verifier:

`.officewars-workday-hybrid-verify.py`

SHA-256:

`174673EFF5DAEEB826CDCC39C8461D05865189409D07BB009D46D61E2F483EBD`

Preserved Workday pace diagnostic:

`Music Legacy/officewars-workday-motion-audition.html`

SHA-256:

`6850D23E628DDA76D427A80CAC94ECDAFC176B5BA5A4FD0F7D642A60A49E8A49`

Focused Workday pace verifier:

`.officewars-workday-motion-verify.py`

SHA-256:

`67DEB80CCC92472A9330B5F75F42B0E646626A744623F7E86AB7FDFFDA8277DA`

Preserved Workday palette audition:

`Music Legacy/officewars-workday-palette-audition.html`

SHA-256:

`A88D75DC6EAB6E7343957D5C148F4598B5CA8A6362350734EB2385B9AE5CE97D`

Focused Workday palette verifier:

`.officewars-workday-palette-verify.py`

SHA-256:

`B48C3CC251178C8F58862BFD19A7CEB7A0DDE4E59B9425661F3D66E670A72C87`

Selected parent-leitmotif audition:

`Music Locked/officewars-parent-leitmotif-audition.html`

SHA-256:

`F66DFBA2B9CF195AC0737DC8E49EA350FDDA04B06434F501C374F682B0479FBB`

Focused parent-leitmotif verifier:

`.officewars-parent-leitmotif-verify.py`

SHA-256:

`12F0EBBAB939B4F69F95678B721452AB64665F33723435F3BE5917A93940357D`

Selected parent-transformation reference:

`Music Locked/officewars-parent-transform-audition.html`

SHA-256:

`C8445FFB55A52D55765EE87147167F4808F1010D802CB8D5F1379AA338638645`

Focused parent-transformation verifier:

`.officewars-parent-transform-verify.py`

SHA-256:

`79A09A41B60E8E43C4C68B08E2B07A60779D1AF47A6CB799F05186AB08C97FFC`

Selected focused motif audition:

`Music Locked/officewars-casino-motif-audition.html`

SHA-256:

`18C856D20E30D399905F72327A739E224670CA448968B73007DD625C71EE5798`

Focused motif verifier:

`.officewars-casino-motif-verify.py`

SHA-256:

`9B604DCB0E9BB4268732A1DFDB46C45A8100CA30118DED5301C6CE9340D65F30`

Selected production audition:

`Music Locked/officewars-casino-production-audition.html`

SHA-256:

`07074232C0C0A1A25DDAB139B4D8C491A3824A4D4DE653A03DF745BCC0833F7A`

Focused production verifier:

`.officewars-casino-production-verify.py`

SHA-256:

`6E89F82789AB41C7B1D6AE4A94A577EEEC2EAD5D33C8897777B0B63772B3ECB4`

Preserved scene-entrance comparison:

`prototypes/officewars-casino-scene-audition.html`

SHA-256:

`D6AAF6D3691B42DAE69872471FCB79F9E056D37B947C3A625DE0602198801EFD`

Repinned on 2026-08-27 by the settle repair; the pre-repair bytes hashed
`A06672D6DBC833AB231299B93025C63096919ECDB7832EBD733673F060D9A98D`.

Focused scene-entrance verifier:

`.officewars-casino-scene-verify.py`

SHA-256:

`EB7B912E347CB3AC64AFF76E9FCC8B979984F3D27A79C7CCAF5C7955A91C00ED`

Historical full audition prototype:

`Music Legacy/officewars-music-audition.html`

SHA-256:

`4EBCCA8C2004EEE06E4DE6035607C7C9EDB1B06F5438D99C0BBB353828B0A0DD`

Historical full audition verifier:

`.officewars-music-audition-verify.py`

SHA-256:

`E59D3A03D76901DD2C1E5558E3354615EE0EB02E8AEF4624875A739D7A5A5755`

All source audition pages and their focused verifiers are intentionally omitted
from the public and rollout packages. The documentation and dated evidence
remain public so another agent can understand the project state without
mistaking an audition for shipped music.

The active motif verifier proves the selected foreground-note plan, locked
30-attack Answer Chase with no reply voice, cleaned 10-attack late False
Confidence, cleaned 31-attack Compulsive Return, and final `D -> E` loop
return. It also verifies the selected contour plan's Answer Chase build, False
Confidence pullback, Compulsive Return rebuild, continuous seam thread, and
final low-end preparation. The loop passes every movement, natural handoff,
loop seam, pause, resume, seeking, 40 rapid section restarts, and 75 seconds of
uninterrupted playback with two complete wraps and a 50-source peak. It cleans
up to zero tracked sources and passes desktop, landscape, and portrait
one-candidate layouts.

Dated evidence is recorded in
`verification/CASINO_FESTIVAL_CONTOUR_SELECTION_2026-08-13.md`.

The preserved entrance comparison passes exact selected-loop preservation,
entrance timing and tempo, audible handoffs, layer isolation, pause, resume,
seeking, rapid switching, 82 seconds and two wraps without accumulation,
cleanup to zero sources, 100-percent headroom, and desktop, landscape, and
portrait layout checks. Dated evidence is recorded in
`verification/CASINO_SCENE_ENTRANCE_DISCOVERY_2026-08-13.md`.

The parent-leitmotif verifier proves candidate anonymity and distinction,
exact Core-to-Workday continuity, 104 BPM timing, one-shot Core behavior,
complete Workday looping, comparison-safe output, pause, resume, seeking,
timestamp controls, 48 rapid switches, 78 seconds with two complete wraps,
cleanup to zero sources, 100-percent headroom, and desktop, landscape, and
portrait layouts. Dated evidence is recorded in
`verification/PARENT_LEITMOTIF_DISCOVERY_2026-08-17.md`.

The parent-transformation verifier proves exact Sketch B Workday notes and
dynamics, exact selected Casino notes and treatments, the 32-step
transformation plan, the 104-to-164 BPM ramp, the `D -> E` handoff, audible
continuity, layer isolation, pause, resume, seeking, rapid switching,
two uninterrupted Workday wraps, two uninterrupted post-handoff Casino wraps,
cleanup to zero sources, 100-percent headroom, and responsive layouts. Dated
evidence is recorded in
`verification/PARENT_LEITMOTIF_TRANSFORMATION_2026-08-17.md`.

The Workday palette verifier proves exact melodic, harmonic, tempo, form, and
loop equality across all three anonymous treatments; comparison-safe
50-percent output; 100-percent headroom; pause, resume, seeking, timestamp
controls, and 48 rapid switches; two uninterrupted wraps for every sample;
cleanup to zero sources; and responsive layouts. Dated evidence is recorded in
`verification/WORKDAY_PALETTE_DISCOVERY_2026-08-17.md`.

The Workday motion verifier proves exact melodic, harmonic, form, and
sound-world equality across the `104 BPM` control, `104 BPM` motion lift, and
`112 BPM` exact-arrangement pace lift. It also passes comparison level,
headroom, transport, rapid switching, two uninterrupted wraps per version,
cleanup, and responsive layouts. Human listening selects the office-funk
palette and `112 BPM` pace foundations while leaving the amount of added
motion open. Dated evidence is recorded in
`verification/WORKDAY_MOTION_DIAGNOSTIC_2026-08-17.md`.

The Workday hybrid verifier proves exact melody, harmony, `112 BPM` tempo,
form, sound world, and opening behavior across the control and both anonymous
hybrids. It verifies phrase-motion plans of `0/0/0/0`, `0/0/0/1`, and
`0/0/0.55/1`, comparison-safe output, 100-percent headroom, transport, rapid
switching, two uninterrupted wraps per version, cleanup, and responsive
layouts. Human listening selects the `0/0/0.55/1` Hybrid B plan as the Workday
development foundation. Dated evidence is recorded in
`verification/WORKDAY_HYBRID_DISCOVERY_2026-08-17.md`.

The Workday form-repair verifier proves exact preservation of the selected
Hybrid B opening, the shared 60-attack connected middle, the optional
64-attack momentum movement, and the liked 17-attack return counterline. It
also proves the exact `384-step` Compact and `512-step` Extended forms,
prepared movement boundaries, comparison-safe output, 100-percent headroom,
transport, 60 rapid switches, two uninterrupted wraps of both rewrites,
cleanup, and responsive layouts. Dated evidence is recorded in
`verification/WORKDAY_FORM_REPAIR_DISCOVERY_2026-08-17.md`.

Human listening subsequently rejected both repaired forms as awkward, long,
and stale. The Workday micro-movement verifier proves that its replacement
Six- and Twelve-Movement relays share exact notes, harmony, tempo, palette,
runtime, and selected opening while changing only the cadence of consequential
arrangement turns. It also passes all eighteen movement starts, comparison
level, 100-percent headroom, transport, 60 rapid switches, two uninterrupted
wraps of both relays, cleanup, and responsive layouts. Dated evidence is
recorded in
`verification/WORKDAY_MICROFORM_DISCOVERY_2026-08-17.md`.

The subsequent listen did not select either cadence: both relays felt
comparable, and Six Move 4 was rejected.

The Workday support-role verifier proves that the exact control still matches
the Six-Movement source and that both anonymous candidates preserve all base
musical material. Candidate A adds only two sustained inner voices per bar;
Candidate B adds only eighteen sparse phrase-ending replies. The comparison
also passes matched output, 100-percent headroom, transport, 60 rapid switches,
two uninterrupted loops of all three candidates, cleanup, and responsive
layouts. Dated evidence is recorded in
`verification/WORKDAY_SUPPORT_DISCOVERY_2026-08-17.md`.

Human listening subsequently found both treatments too subtle and
instrumentally ambiguous to resolve the standalone-melody problem. The
Workday ensemble verifier proves exact Hybrid B melody, harmony, tempo, and
`0/0/0.55/1` motion preservation across three anonymous backing casts and all
nine Full, Backing, and Harmony playback modes. It also passes isolated-layer
audibility, comparison-safe output, 100-percent headroom, transport, 72 rapid
switches, two uninterrupted loops of all three full mixes, cleanup, and
responsive layouts. Dated evidence is recorded in
`verification/WORKDAY_ENSEMBLE_DISCOVERY_2026-08-17.md`.

Human listening selected Ensemble C as the Workday ensemble foundation. Its
organ-like harmony and rhythmic swells work reciprocally with the melody;
Ensembles A and B remain historical alternatives. Complete form, final
production, mix, gameplay masking, integration, and shipping remain open.

The Workday relational-form verifier proves exact selected Ensemble C
foreground, harmony, opening motion, effects, and output preservation. It also
passes all six movement starts, the twelve phrase-level relationship contracts,
the parent-derived middle, the `0/3/8/6` return-counterline plan,
comparison-safe movement levels, 100-percent headroom, transport, 60 rapid
switches, two uninterrupted full-cue wraps, six concurrent Foundation wraps,
cleanup, and responsive layouts. Dated evidence is recorded in
`verification/WORKDAY_RELATIONAL_FORM_DISCOVERY_2026-08-17.md`.

Human listening then identified awkward starts in `Band Invites` and
`Roles Reverse`, while retaining interest in the reversed melody, plus a
strange Teamwork counterline moment. The transition-repair verifier proves
Version A remains exact Draft 02, Version B preserves every foreground note,
and only the intended harmony, organ-leadership, and counterline paths change.
It also passes all eight playback modes, comparison-safe levels,
100-percent headroom, transport, 64 rapid switches, one-shot completion,
two uninterrupted wraps of both complete forms, cleanup, and responsive
layouts. Dated evidence is recorded in
`verification/WORKDAY_TRANSITION_REPAIR_DISCOVERY_2026-08-17.md`.

Draft 01's technical evidence remains recorded in
`verification/WORKDAY_LONGFORM_DISCOVERY_2026-08-17.md`; its listening verdict
rejects Movements 2 and 3 while retaining Movement 4 as liked material.

The Workday Candidate C form verifier proves exact preservation of Candidate
C, Ensemble C, the four parent phrases, `112 BPM`, and Hybrid B's
`0 / 0 / 55% / 100%` macro-motion arc. It also proves distinct C-derived
development, the revised Corner Turn cadence, smooth boundary intervals, one
live-highlighted movement button with `aria-current`, all eight movement
starts, Full Cue and Melody Only audibility, 100-percent headroom, transport,
60 rapid switches, two uninterrupted wraps of both modes, cleanup to zero
sources, and responsive layouts. Initial evidence is recorded in
`verification/WORKDAY_CANDIDATE_C_FORM_DISCOVERY_2026-08-18.md`; the retained
revision is recorded in
`verification/WORKDAY_CANDIDATE_C_FORM_REFINEMENT_2026-08-18.md`.

The Workday detour-flow verifier proves that the three treatments share the
exact current-form context, selected Candidate C pitches and harmony, Ensemble
C, `112 BPM`, and motion identity. The first listen was anonymous; after that
reaction the retained page reveals the original articulation, connected lead,
and connected-lead-plus-organ-handoff mechanisms in a durable comparison key
and now-playing description. The verifier also proves all six Full and Melody
modes, comparison-safe output, four live-highlighted Passage Map starts,
`aria-current`, transport, 60 rapid switches, 100-percent headroom, two
uninterrupted wraps of all six modes, cleanup to zero sources, and responsive
layouts. Blind-stage and reveal evidence are recorded in
`verification/WORKDAY_DETOUR_FLOW_DISCOVERY_2026-08-18.md` and
`verification/WORKDAY_DETOUR_FLOW_REVEAL_2026-08-18.md`.

The subsequent Workday detour-hybrid verifier proves that Passage D preserves
all selected material while assigning articulation by rhythmic role. It
verifies the exact 14 connected note positions, crisp treatment elsewhere,
the unchanged organ handoff, one selected card and API treatment ID, all eight
Full and Melody modes, comparison-safe output, four Passage Map starts,
`aria-current`, transport, 60 rapid switches, 100-percent headroom, two
uninterrupted wraps of every mode, cleanup to zero sources, and responsive
layouts. Human listening selects D as the detour performance foundation.
Evidence is
`verification/WORKDAY_DETOUR_HYBRID_SELECTION_2026-08-18.md`.

The Workday long-cycle verifier proves that all three anonymous candidates
preserve exact Hybrid D for their complete first loop and preserve the
selected Workday note plan across every subsequent loop. It verifies the
three intended loop 2-4 strategies, direct Loop 1-4 starts, live and
accessible loop highlighting, comparison-safe first-loop output,
100-percent headroom, transport, 48 rapid switches, responsive layouts, two
uninterrupted complete `4:34.286` supercycles per candidate, bounded source
counts, and zero-source cleanup. No long-cycle candidate is selected.
Evidence is
`verification/WORKDAY_LONG_CYCLE_DISCOVERY_2026-08-18.md`.

The focused Workday long-cycle tribrid verifier proves that its exact-repeat
control and Tribrid D preserve the complete selected Hybrid D composition and
production. It verifies exact Loop 1, the humanized Loop 2, ensemble
conversation in Loop 3, the combined lower-register payoff and prepared reset
in Loop 4, direct loop starts, live accessible highlighting, comparison-safe
output, 100-percent headroom, pause, resume, seek, 48 rapid switches,
responsive layouts, two complete supercycles per candidate, bounded source
counts, browser-error capture, and zero-source cleanup. Human listening
selects Tribrid D as the Workday long-cycle treatment. Discovery evidence is
`verification/WORKDAY_LONG_CYCLE_TRIBRID_DISCOVERY_2026-08-18.md`; selection
evidence is
`verification/WORKDAY_LONG_CYCLE_TRIBRID_SELECTION_2026-08-18.md`.

## OfficeWars Web Audio Model

The prototype uses one stable `AudioContext`, master gain, dynamics stage,
analyser, and destination graph. Each playback session owns a disposable bus,
effects, scheduled sources, modulation nodes, and callbacks.

Beat, bar, phrase, and section positions are explicit. `AudioParam` ramps
schedule gain, pan, filter, detune, modulation depth, and effect sends.
OfficeWars playback speed does not change music tempo.

On pause, seek, switch, or stop:

1. invalidate stale scheduler callbacks;
2. stop scheduled sources;
3. cancel future automation;
4. disconnect session-owned modulation and effects; and
5. confirm zero hidden sources and duplicate schedulers.

The graph preserves headroom for overlapping drums, bass, leads, impacts,
stingers, and effect returns. Compression protects the mix but does not replace
arrangement contrast.

A `DynamicsCompressorNode` must be given time to settle before the first note.
It reports deep gain reduction before receiving any audio and releases upward
over roughly a second, so music that starts immediately after the graph is built
plays through that sweep and sounds like static. Every new audition page carries
a `COMPRESSOR_SETTLE` pre-roll: the first note after a page load waits that long
in **rendered** time, and every later start uses the ordinary lead, because the
node is built once per load and is already settled.

The pre-roll's length is a property of that page's own compressor settings, not a
shared constant. Measure it with
`.officewars-compressor-settle-measure.py`, which validates itself against the
Boss A page's recorded crossings before reporting the others. Measured so far:
Boss A and Workday need `1.25 s`, while the Casino node — threshold `-8`, ratio
`20` — starts `4.2 dB` deeper and needs `1.35 s`. Copying `1.25` into the Casino
page would have left part of a `20.7 dB` sweep inside the music. The measured
platform behaviour is recorded under Web Audio Platform Behaviour in
`docs/music/RESEARCH_LIBRARY.md`. The game itself builds no compressor, so this
constrains auditions only.

## Focused Verification

After a substantive prototype change, test:

1. first play after a page reload, then first play after a stop, because a
   graph built once per load hides load-only defects from every later start;
2. two uninterrupted loops;
3. stop and replay;
4. pause and resume;
5. seeking before and after edited boundaries;
6. rapid track switching;
7. at least 60 seconds of continuous playback;
8. browser console errors;
9. clipping, static, clicks, dropouts, and effect accumulation;
10. active-source and scheduler cleanup;
11. transport layout; and
12. headphones plus speakers or monitors.

Technical verification establishes audibility and lifecycle stability. It does
not approve the music.

## Ship Gate

No OfficeWars cue should enter the game until:

- the user approves the complete composition;
- repeated listening remains enjoyable;
- scene function and emotional intent are clear;
- loops and reactive states are musically defined;
- UI and gameplay sounds remain intelligible;
- stored volume, pause, mute, refresh, transitions, and cleanup work;
- playback speed remains outcome- and tempo-neutral; and
- the standalone game still needs no server, build step, or external request
  unless that product constraint is explicitly changed.
