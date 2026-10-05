# OfficeWars Music Catalog

Last updated: 2026-08-31

## Purpose

This is the authoritative lifecycle catalog for source-only OfficeWars music
artifacts. Every audition HTML receives:

- one stable internal label beginning with `OW-MUSIC-`;
- one lifecycle status;
- one canonical workspace path; and
- one short description of what the artifact contributes or why it was
  retired.

The internal label survives title, filename, folder, and status changes.
Changing status requires moving the artifact to the matching folder and
updating this catalog in the same task.

## Lifecycle

| Status | Meaning | Canonical folder |
|---|---|---|
| `Completed` | Final standalone master with its chosen creative, technical, translation, metadata, and delivery gates closed. | `Music Official/` |
| `Approved` | Exact selected music or component protected as current direction, but not yet a completed master. | `Music Locked/` |
| `Test` | Active experiment or diagnostic awaiting listening evidence. | `prototypes/` |
| `Limbo` | One artifact contains both liked and disliked or defective material. Diagnose it, create a Test that preserves only the good material, then reject the Limbo artifact. | `prototypes/` |
| `Rejected` | No longer carries forward. This includes failed, superseded, and retired controls retained as evidence. | `Music Legacy/` |

Folder placement and lifecycle status answer different questions:

- the folder tells agents how the file may be used now;
- the status tells agents what evidence and approval it currently has.

`Approved` is not `Completed`. `Completed` is not automatically integrated or
shipped. Game integration remains a separate decision recorded in the active
music brief and implementation evidence.

An unfinished track must have both:

- an `Approved` protected baseline in `Music Locked/`; and
- one `Test` extension branch in `prototypes/`.

Promoting a partial track to `Approved` therefore opens its next extension
branch in the same task. The branch carries the Approved music forward
unchanged and adds the next extension, and the cycle repeats until the track is
a full track, at which point the finished master becomes `Completed` in
`Music Official/`. A component audition that is not a track on its own, such as
a motif, palette, percussion, or diagnostic study, feeds a track's branch
instead of opening one.

The two artifacts must use different internal labels. Future edits belong in
the Test branch until the user approves a replacement baseline or completes
the cue. Do not edit the Approved rollback reference while development remains
open. Do not invent the extension's musical content in order to satisfy this
rule; ask which open question the branch should answer.

## Catalog

### Completed

No completed OfficeWars music masters yet.

### Approved

| Internal label | Status | Canonical path | Role |
|---|---|---|---|
| `OW-MUSIC-PARENT-LEITMOTIF` | `Approved` | `Music Locked/officewars-parent-leitmotif-audition.html` | Selected Sketch B parent identity. |
| `OW-MUSIC-PARENT-TRANSFORM` | `Approved` | `Music Locked/officewars-parent-transform-audition.html` | Selected Workday-to-Casino transformation reference. |
| `OW-MUSIC-WORKDAY-HYBRID-B` | `Approved` | `Music Locked/officewars-workday-hybrid-audition.html` | Selected gradual Workday motion architecture. |
| `OW-MUSIC-WORKDAY-ENSEMBLE-C` | `Approved` | `Music Locked/officewars-workday-ensemble-audition.html` | Selected reciprocal organ ensemble. |
| `OW-MUSIC-WORKDAY-MIDDLE-C` | `Approved` | `Music Locked/officewars-workday-middle-melody-audition.html` | Selected Candidate C middle identity. |
| `OW-MUSIC-WORKDAY-DETOUR-D` | `Approved` | `Music Locked/officewars-workday-detour-hybrid-audition.html` | Selected adaptive detour performance. |
| `OW-MUSIC-WORKDAY-FORM` | `Approved` | `Music Locked/officewars-workday-candidate-c-passage-d-form-audition.html` | Selected complete Workday composition and form foundation. |
| `OW-MUSIC-WORKDAY-PRODUCTION-D` | `Approved` | `Music Locked/officewars-workday-production-hybrid-audition.html` | Selected Hybrid D production identity. |
| `OW-MUSIC-WORKDAY-ON-THE-CLOCK` | `Approved` | `Music Locked/officewars-workday-long-cycle-tribrid-audition.html` | Selected four-loop Workday cue titled On the Clock. Repaired on 2026-08-27, with the user's confirmation, to carry a `COMPRESSOR_SETTLE` pre-roll of `1.25 s` of rendered silence before the first note on the first play after a page load. The length was measured on this page's own compressor in the same run as its completion prototype and came back identical crossing for crossing, which is a measured result rather than a borrowed constant. Bytes went from `74,008` and `FF677CC9` to `79,225` and `60DDDF21`. Gain reduction at the first note is now `-0.388 dB` against a `-16.501 dB` sweep observed before the wait finished, and the second play returns to the ordinary `60 ms` lead. This page was repaired because its completion prototype already was, so an unrepaired baseline meant the branch sounded clean while the reference it rolls back to did not. The repair changes when the first note sounds, never which note sounds, so the music, length and schedule are unchanged; its own verifier pays the settle once per page load rather than re-timing every assertion, and six Rejected-page verifiers that pin these bytes as unmodified parent evidence were repinned in the same task. Behaviour is asserted by 22 checks in `.officewars-compressor-settle-scene-browser.py`. Pre-repair bytes are quarantined as a reference, not as a rollback candidate. |
| `OW-MUSIC-CASINO-FESTIVAL-CONTOUR` | `Approved` | `Music Locked/officewars-casino-motif-audition.html` | Selected ordinary-Casino composition. |
| `OW-MUSIC-CASINO-CORPORATE-CONTRABAND` | `Approved` | `Music Locked/officewars-casino-production-audition.html` | Selected ordinary-Casino production. Repaired on 2026-08-27, with the user's confirmation, to carry a `COMPRESSOR_SETTLE` pre-roll of `1.35 s` of rendered silence before the first note on the first play after a page load. The length was measured on this page's own compressor in the same run as its entrance prototype and came back identical crossing for crossing, which is a measured result rather than a borrowed constant; its threshold of `-8` and ratio of `20` start it `4.2 dB` deeper than the Boss A lineage, so `1.25 s` would have left part of a `20.7 dB` sweep inside the music. Bytes went from `87,101` and `194A07E3` to `92,318` and `07074232`. Gain reduction at the first note is now `-0.353 dB` against a `-20.722 dB` sweep observed before the wait finished, and the second play returns to the ordinary `60 ms` lead. This page was repaired because its entrance prototype already was, so an unrepaired baseline meant the branch sounded clean while the reference it rolls back to did not. The repair changes when the first note sounds, never which note sounds, so the music, length and schedule are unchanged; its own verifier pays the settle once per page load rather than re-timing every assertion. Behaviour is asserted by 22 checks in `.officewars-compressor-settle-scene-browser.py`. Three verification records that pin these bytes were annotated rather than rewritten, because a record states what was true when it was written. Pre-repair bytes are quarantined as a reference, not as a rollback candidate. |
| `OW-MUSIC-BOSS-A-IDENTITY` | `Approved` | `Music Locked/officewars-boss-identity-audition.html` | Selected melodic boss-floor identity foundation. |
| `OW-MUSIC-BOSS-A-WINDOWED-PERCUSSION-REPAIR` | `Approved` | `Music Locked/officewars-boss-a-windowed-percussion-audition.html` | Approved standalone Boss A cue with windowed percussion boundaries and no reported static in the final listening pass. |
| `OW-MUSIC-BOSS-A-KERNEL-A-RESPONSIVE-ENSEMBLE` | `Approved` | `Music Locked/officewars-boss-a-kernel-a-ensemble-audition.html` | Selected Kernel A melody with its selected responsive ensemble, on the resilient `skip-overdue` scheduler. Human listening confirmed the static is gone and selected `Responsive` over the uniform accompaniment. Contains only the selected candidate; its saw, triangle, reduction, length, harmony, roots and intensity are byte-identical to the audition heard. Bass events per bar `3,3,4,2,2,4,5,3`, chord hits per bar `2,2,3,1,2,3,4,2`, bar 4 withholding the snare, bar 7 densest under the `C6` apex at step 54. The handoff from `Challenge Issued` was settled afterwards by `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF`; harmonic destination and cadence, longer form, and game integration remain open. This is a component audition, which under the partial-track rule feeds a track's branch rather than opening one, so it stays `Approved` even though the page it fed has since been superseded. 61 KB, live synthesis, no embedded audio. |
| `OW-MUSIC-BOSS-A-KERNEL-A-DROP` | `Approved` | `Music Locked/officewars-boss-a-kernel-a-drop-audition.html` | Current protected Boss A partial-track baseline. Carries the selected 264 steps forward unchanged and adds bars 34 to 41, for 328 steps and `58.571 s`. Human listening on 2026-08-27 confirmed that bar 34 reads as a good pull-back and that eight bars is the right length; the user delegated the resulting lifecycle action on 2026-08-31. The drop is arrangement rather than a melody replacement: the saw continues, the triangle withdraws for six bars, bar 35 loses percussion, and the rebuild stops at `1.26` below bar 33's `1.40`. It adds no melodic pitch, tops out at `C6` below the spent `D6`, and leaves bar 41 on unresolved `E7`. Triangle balance remains `0.86`; `COMPRESSOR_SETTLE` remains `1.25 s`; game integration remains unapproved. Static verifier `137/137`; source SHA-256 `C6C45B47`. Its one active extension branch is `OW-MUSIC-BOSS-A-DROP-CADENCE`. |

### Test

| Internal label | Status | Canonical path | Role |
|---|---|---|---|
| `OW-MUSIC-WORKDAY-DEVELOPMENT` | `Test` | `prototypes/officewars-workday-development-audition.html` | Active On the Clock completion and translation branch; audio-identical to the Approved four-loop baseline while masking, low-volume, mono, fatigue, and delivery gates remain open. Repaired on 2026-08-27, with the user's confirmation, to carry a `COMPRESSOR_SETTLE` pre-roll of `1.25 s` of rendered silence before the first note on the first play after a page load. The length was measured on this page's own compressor rather than copied from the Boss A lineage, because the settle is a property of the node's own settings: measurement returned the same `1.25 s` the Boss A lineage uses, which is a result here rather than an assumption. Bytes went from `74,144` and `69B6A05F` to `79,361` and `A300260A`. Gain reduction at the first note is now `-0.388 dB` against a `-16.501 dB` sweep observed before the wait finished, and the second play returns to the ordinary `60 ms` lead, so only the first start after a load pays anything. Because the wait is over a second of deliberate silence, the transport reads `WAIT` during it and repaints to `PAUSE` when the music sounds, and the movement readout reads `READY` until a step is actually scheduled rather than naming the previous theme's movement through the wait. The repair changes when the first note sounds, never which note sounds, so the music, length and schedule are unchanged. Behaviour is asserted by 22 checks in `.officewars-compressor-settle-scene-browser.py`. Three stray CRLF line endings inside a metadata object literal were normalized to LF first, because the repair refuses to edit mixed endings. |
| `OW-MUSIC-CASINO-ENTRANCE` | `Test` | `prototypes/officewars-casino-scene-audition.html` | Active unresolved Casino entrance comparison. Repaired on 2026-08-27, with the user's confirmation, to carry a `COMPRESSOR_SETTLE` pre-roll of `1.35 s` of rendered silence before the first note on the first play after a page load. The length was measured on this page's own compressor rather than copied from the Boss A lineage, because the settle is a property of the node's own settings: this node's threshold of `-8` and ratio of `20` start it `4.2 dB` deeper than Boss A's and clear `-0.5 dB` `70 ms` later, so `1.25 s` would have left part of a `20.7 dB` sweep inside the music. Bytes went from `94,403` and `A06672D6` to `99,620` and `D6AAF6D3`. Gain reduction at the first note is now `-0.353 dB` against a `-20.784 dB` sweep observed before the wait finished, and the second play returns to the ordinary `60 ms` lead, so only the first start after a load pays anything. Because the wait is over a second of deliberate silence, the transport reads `WAIT` during it and repaints to `PAUSE` when the music sounds, and the movement readout reads `READY` until a step is actually scheduled rather than naming the previous theme's movement through the wait. The repair changes when the first note sounds, never which note sounds, so the music, length and schedule are unchanged. Behaviour is asserted by 22 checks in `.officewars-compressor-settle-scene-browser.py`. This page has eight pre-existing uses of `??`, which the project's esprima grammar predates, so a clean browser load is its only syntax check. |
| `OW-MUSIC-BOSS-A-DROP-CADENCE` | `Test` | `prototypes/officewars-boss-a-drop-cadence-audition.html` | Sole active Boss A cadence-repair and static-diagnostic branch, built from the Approved drop at source hash `C6C45B47`. Carries all 328 selected steps forward and exposes `Drop`, exact `Am Original` and `C Original` controls, and `Am Cadence` and `C Cadence` repairs. Both repairs worked by listening but provide only about `1.43 s` of post-arrival exposure, so longer form remains open. Payoff and Turnaround remain inactive generator data. Human glitch marks show no browser underruns or scheduler fault. The page exposes six unselected isolation modes: exact `Layered control`, default `Snare priority`, `Snare air only` (all paper brush muted), `Paper brush only` (snare noise-air muted, triangle body retained), `No noise percussion` (both windowed-noise layers muted, triangle body retained), and `Silent noise percussion` (every noise hit scheduled exactly as Layered but at `SILENCE` gain, so source churn and timing are preserved while the audible signal is removed), the last two added with user approval on 2026-09-04 because listening on 2026-09-02 heard glitches around the same times in every prior mode, so no single noise isolate was implicated (`Snare priority` marks at steps `49`, `89`, `226` on `landMinorCadence`; `Paper brush only` marks at step `86` on `landMinorCadence` and steps `31`, `155` on `landMajorCadence`). Source analysis validated against the logs refuted the two-noise-onset collision hypothesis; kick, brush snare, bass, and saw are constant in every source window, and `No noise percussion` now exists to test whether the artifact survives with no windowed noise at all. The pause crackle is diagnosed (a bare `audioContext.suspend()` with no fade), repaired with user approval (pause ramps the master bus to `SILENCE` over `35 ms` of rendered time and suspends about `60 ms` later; every resume path restores the gain over `20 ms`; the browser suite asserts amplitude at both ends), and confirmed gone by listening on 2026-09-04. The same session heard no static in `No noise percussion`, localizing the recurring static to the presence of windowed-noise percussion; whether the cause is the audible noise signal or source start/stop churn remains open, and the churn-preserving `Silent noise percussion` mode was built to answer it (static that survives it implicates churn; silence implicates the noise signal), pending the listening comparison. Both cadence repairs remain liked but too short for the payoff to be realized, so length precedes the Am-versus-C choice; the user deferred longer-form work until the static is resolved. `MARK GLITCH` / `G` and `COPY LOG` remain available. No cadence destination, percussion treatment, mitigation, or extension is selected. Longest form `360` steps / `64.286 s`; SHA-256 `0E87C920`; browser `330/330`; cadence settle suite `29/29`. Noise-mechanism separation (signal versus churn), cadence extension, destination, completion, and integration remain open. |

### Limbo

None.

### Rejected

| Internal label | Status | Canonical path | Role |
|---|---|---|---|
| `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF` | `Rejected` | `Music Legacy/officewars-boss-a-kernel-a-handoff-audition.html` | **Superseded by its own extension on 2026-08-26, not rejected on merit.** This music was selected by ear and was the Approved baseline; `OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION` carries all 200 of its steps forward note for note and adds bars 26 to 33, so the shorter form is no longer the baseline. The lifecycle has exactly five labels and none of them is *superseded*, so it is tagged `Rejected` and this row carries the distinction; `supersededOnMerit:false` records the same thing in the page. Retained as the rollback reference for the 200-step form: 200 steps and `35.714 s`, theme entering at `24.286 s`, one composed `E7` approach bar, one new melodic pitch `G#4`, `C6` ceiling reached in the protected opening at step 106. Contains only the selected `Prepared` take at source hash `1A4DF3EE`, with the `0.86` balance baked in. Static verification 112 checks, browser smoke test 86 checks. |
| `OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION` | `Rejected` | `Music Legacy/officewars-boss-a-kernel-a-extension-audition.html` | **Superseded by its own drop extension on 2026-08-31, not rejected on merit.** This selected 264-step baseline carries the protected opening, prepared seam, Kernel A, responsive ensemble, and bars 26 to 33 with the single `D6` ceiling break. `OW-MUSIC-BOSS-A-KERNEL-A-DROP` carries every step forward unchanged and adds bars 34 to 41, so the shorter form is no longer the protected baseline. The page records `supersededOnMerit:false` and remains the rollback reference for the 264-step form. Static verifier `159/159`; SHA-256 `AA927DBB`. |
| `OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION-COMPARISON` | `Rejected` | `Music Legacy/officewars-boss-a-kernel-a-extension-comparison.html` | Resolved two-candidate ceiling comparison, previously labelled `OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION`; the selected music now carries that label as Approved. Asked whether the melodic ceiling breaks to `D6` in bars 26 to 33 or is saved for a later climax. The two candidates were identical in every field except five triangle notes at steps 252, 253, 255, 259 and 261, so a preference could not be explained by harmony, groove, level, length or cadence; both ended on `B5`. Human listening on 2026-08-26 selected `Reach` with the verdict "i like the reach ceiling broken". Retained as the only page holding the rejected `Hold` control, the ceiling that was not taken, and as the evidence of what was heard. Its judging prose is deliberately left in the present tense about a closed question rather than rewritten, and its inherited startup no-op is left unrepaired. Static verification 249 checks, browser smoke test 138 checks. |
| `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF-COMPARISON` | `Rejected` | `Music Legacy/officewars-boss-a-kernel-a-handoff-comparison.html` | Resolved two-candidate handoff comparison, previously labelled `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF`; the selected music now carries that label as Approved. Retained as the only page holding the rejected `Direct` control, 192 steps and `34.286 s` with the theme entering at `22.857 s` and no composed approach bar, and as the only page holding the triangle balance slider the user set `0.86` on. Byte-pinned as the evidence of what was heard, so its inherited startup no-op is deliberately left unrepaired rather than tidied. |
| `OW-MUSIC-BOSS-A-KERNEL-A-ENSEMBLE` | `Rejected` | `Music Legacy/officewars-boss-a-kernel-a-ensemble-comparison.html` | Resolved support-response comparison for selected Kernel A, opened because the melody was liked but the ensemble was suspected weak. Both candidates derived from the same source block, so saw, triangle, reduction, length, harmony, roots, intensity, palette and scheduler were byte-identical and only bass, chord placement and percussion placement changed. Human listening selected `Responsive`, which is now Approved on its own. Retained as the only page holding the rejected `Current` control: identical bass rhythm in all eight bars, two chord hits per bar, a fixed kick and snare grid, and escalation carried only by a `3.6 dB` level ramp. That is the measurable uniform-accompaniment failure mode. |
| `OW-MUSIC-BOSS-A-KERNEL-A-STATIC-REPAIR` | `Rejected` | `Music Legacy/officewars-boss-a-kernel-a-static-repair.html` | Resolved scheduler-only repair for selected Kernel A. Control and Repair preserved exact notes, reductions, harmony, bass, intensity, roles, current palette, windowed percussion, length, and all five monitors. A forced `900 ms` stall made Control stack five overdue steps with about `668 ms` lag; Repair skipped four missed steps, scheduled one current step, and stayed level-identical within `0.03 dB`. Normal headless loops never reproduced late calls, so the question needed human listening; the user confirmed the recurring static is gone. Retained as the only page holding the `stack-overdue` control and as the byte-pinned melody source for the Approved responsive ensemble. |
| `OW-MUSIC-BOSS-A-IDENTITY-KERNEL` | `Rejected` | `Music Legacy/officewars-boss-a-identity-kernel-audition.html` | Superseded two-kernel Test. Human listening selected A because it felt the most energizing, left B unselected, and reported recurring static even on loops. Retained as the exact musical and scheduler control for the focused A repair. |
| `OW-MUSIC-BOSS-A-PALETTE-CHECK` | `Rejected` | `Music Legacy/officewars-boss-a-palette-check-audition.html` | Resolved exact-Sketch-A palette diagnostic. A was the unchanged current palette; B was a matched `-2 dB` shelf below `140 Hz`. Human listening heard no clear difference and said the material sounded good, so the simpler current palette is exonerated and carries into the identity-kernel Test. |
| `OW-MUSIC-BOSS-A-BARE-THEME` | `Rejected` | `Music Legacy/officewars-boss-a-bare-theme-audition.html` | Rejected four-theme method retained as a listening control. Human listening found T1-T4 disappointing in both Bare melody and Full ensemble. The ensemble was noticeable but did nothing to support the melody. The round over-isolated melody into equal 32-step monophonic saw lines over one shared harmony, then added the same nonresponsive backing engine to every line. |
| `OW-MUSIC-BOSS-A-INTENSITY-3-REPAIR` | `Rejected` | `Music Legacy/officewars-boss-a-intensity-3-repair.html` | Rejected focused repair for B2 from step 28 onward. Human listening rejected R1 as random noises with no tune and a bar 1 that never paid off, then scrapped Control, R1, R2, and R3 together. Retained as the byte-pinned derivation source and direct control for the later bare-theme round. |
| `OW-MUSIC-BOSS-A-INTENSITY-3-FLOW` | `Rejected` | `Music Legacy/officewars-boss-a-intensity-3-flow-audition.html` | Retired `Intensity 3` replacement. Both sketches developed the byte-exact bar 1 seed instead of transposing it: F1 filled the bar-1 fourth stepwise and escalated by subdivision, F2 hammered the bar-1 landing note and held its ceiling at C6. Human listening rejected the round for straying from melody and from the idea of a boss fight, and the user then freed the whole continuation including the bar 1 seed. Retained as the exact control for two figuration defects: F1 shows that filling a leap stepwise produces running scales, and F2 shows that repeated notes read as hammering rather than as a tune. Both are now measurable, as the parent leaps on 40 to 45 percent of intervals and never repeats a consecutive pitch. |
| `OW-MUSIC-BOSS-A-SECOND-MOVEMENT-SKETCHES` | `Rejected` | `Music Legacy/officewars-boss-a-second-movement-sketches.html` | Superseded A/B/B2/C discovery page. Human listening liked A and B, rejected C and B's gear change, then rejected B2 from `Intensity 3` onward for self-clashing upper voices and disliked E6 in this track. Retained as the exact source and direct control for the focused repair. |
| `OW-MUSIC-BOSS-A-NEXT-MOVEMENT-DISCOVERY` | `Rejected` | `Music Legacy/officewars-boss-a-next-movement-audition.html` | Retired three-way length and seam-voicing comparison. Diagnosis found all three candidates recombine the same quoted opening cell, so the comparison could not be answered; also carried the agent-invented MIDI 81 apex cap. Retained as the exact control for the quotation defect. |
| `OW-MUSIC-BOSS-A-OPENING-GRAMMAR-DISCOVERY` | `Rejected` | `Music Legacy/officewars-boss-a-opening-grammar-audition.html` | Direct listening control rejected because all three shared-continuation versions still strayed from the opening, had weak tunes, and failed their handoffs. |
| `OW-MUSIC-BOSS-A-CONTINUOUS-TUNE` | `Rejected` | `Music Legacy/officewars-boss-a-continuous-tune-audition.html` | Direct listening control rejected because its post-opening melody remained one continuous triangle-led foreground instead of preserving the opening's changing instrumental ownership. |
| `OW-MUSIC-BOSS-A-PLAYER-THROUGHLINE` | `Rejected` | `Music Legacy/officewars-boss-a-player-throughline-audition.html` | Older control rejected because its story-led movements and Player handoffs did not form one convincing tune. |
| `OW-MUSIC-BOSS-A-CONFRONTATION-THREAD` | `Rejected` | `Music Legacy/officewars-boss-a-confrontation-thread-audition.html` | Direct control proving that restored Boss phrases, gallop, backbeat, and opening harmony did not rescue the rejected later Player writing. |
| `OW-MUSIC-BOSS-A-CONTINUATION-FORM` | `Rejected` | `Music Legacy/officewars-boss-a-continuation-form-audition.html` | Rejected seven-movement form with clunky boundaries and later Player notes that lost the established tune. |
| `OW-MUSIC-BOSS-A-TUNE-DISCOVERY` | `Rejected` | `Music Legacy/officewars-boss-a-tune-discovery-audition.html` | Superseded anonymous comparison. Candidate C had the preferred pacing, but every continuation sounded like a separate piece after Finding Footing. |
| `OW-MUSIC-BOSS-A-MELODIC-THROUGHLINE` | `Rejected` | `Music Legacy/officewars-boss-a-melodic-throughline-audition.html` | Technically valid but musically rejected motif-template form retained as older Boss development evidence. |
| `OW-MUSIC-BOSS-A-STATUS-STORY` | `Rejected` | `Music Legacy/officewars-boss-a-status-story-audition.html` | Superseded pause-heavy status-transformation Test retained as older Boss form evidence. |
| `OW-MUSIC-BOSS-A-ELASTIC-STORY` | `Rejected` | `Music Legacy/officewars-boss-a-elastic-story-audition.html` | Earlier superseded seven-movement Boss form retained as secondary historical comparison evidence. |
| `OW-MUSIC-BOSS-A-CHARACTER-FLOW` | `Rejected` | `Music Legacy/officewars-boss-a-character-flow-audition.html` | Limbo predecessor with liked Challenge Issued and Finding a Rhythm movements but a rejected back half; retained as historical form evidence. |
| `OW-MUSIC-BOSS-A-CHARACTER-DIALOGUE` | `Rejected` | `Music Legacy/officewars-boss-a-character-dialogue-audition.html` | Superseded Player/Boss character draft that informed later Player-led development. |
| `OW-MUSIC-BOSS-A-PERSISTENT-THREAD` | `Rejected` | `Music Legacy/officewars-boss-a-form-audition.html` | Rejected constant-thread form with identity drift. |
| `OW-MUSIC-BOSS-A-UNDERCURRENT-REPAIR` | `Rejected` | `Music Legacy/officewars-boss-a-undercurrent-repair-audition.html` | Superseded harmonic repair control. |
| `OW-MUSIC-BOSS-A-PAPER-BRUSH` | `Rejected` | `Music Legacy/officewars-boss-a-percussion-repair-audition.html` | Former Limbo artifact; liked brush treatment preserved in the pop-repair Test, abrupt envelope retired. |
| `OW-MUSIC-BOSS-A-POP-REPAIR` | `Rejected` | `Music Legacy/officewars-boss-a-pop-repair-audition.html` | Fixed the brush envelope but retained scheduler backlog bursts after main-thread stalls. |
| `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR` | `Rejected` | `Music Legacy/officewars-boss-a-scheduler-repair-audition.html` | Fixed overdue scheduler bursts but still produced intermittent pops on the user's playback system; retained as the exact live-engine control. |
| `OW-MUSIC-BOSS-A-PRERENDER-REPAIR` | `Rejected` | `Music Legacy/officewars-boss-a-prerender-repair-audition.html` | Removed live scheduling and node churn but preserved baked percussion-boundary impulses; retained as a superseded single-buffer control. |
| `OW-MUSIC-BOSS-A-WINDOWED-PERCUSSION-COMPARISON` | `Rejected` | `Music Legacy/officewars-boss-a-windowed-percussion-comparison.html` | Superseded old-versus-windowed comparison retained as evidence after the repaired cue was approved. |
| `OW-MUSIC-BOSS-A-DEVELOPMENT` | `Rejected` | `Music Legacy/officewars-boss-a-long-cycle-callback-limbo.html` | Liked Boss tune whose four-loop plan changed only callback overlays while repeating the same foreground and harmony. Superseded by melodic development. |
| `OW-MUSIC-BOSS-A-MELODIC-DEVELOPMENT` | `Rejected` | `Music Legacy/officewars-boss-a-melodic-development-audition.html` | Liked melodic-development Test superseded because its high and low registers lacked distinct character identities. |
| `OW-MUSIC-BOSS-A-REGISTER-DIALOGUE` | `Rejected` | `Music Legacy/officewars-boss-a-register-dialogue-audition.html` | Promising two-register conversation superseded because the voices lacked Player/Boss personalities and some prepared ascents failed to reach their promised peaks. |
| `OW-MUSIC-HISTORICAL-AUDITION` | `Rejected` | `Music Legacy/officewars-music-audition.html` | Superseded broad audition history. |
| `OW-MUSIC-WORKDAY-BAND-ANSWER` | `Rejected` | `Music Legacy/officewars-workday-band-answer-audition.html` | Rejected Band Answers middle. |
| `OW-MUSIC-WORKDAY-CANDIDATE-C-FORM` | `Rejected` | `Music Legacy/officewars-workday-candidate-c-form-audition.html` | Superseded pre-Passage-D Candidate C form. |
| `OW-MUSIC-WORKDAY-DRAFT-01` | `Rejected` | `Music Legacy/officewars-workday-cue-audition.html` | Rejected sleepy and fragmented longform middle. |
| `OW-MUSIC-WORKDAY-DETOUR-FLOW` | `Rejected` | `Music Legacy/officewars-workday-detour-flow-audition.html` | Superseded A/B/C detour-flow comparison. |
| `OW-MUSIC-WORKDAY-FORM-REPAIR` | `Rejected` | `Music Legacy/officewars-workday-form-repair-audition.html` | Rejected awkward Compact and Extended rewrites. |
| `OW-MUSIC-WORKDAY-LONG-CYCLE` | `Rejected` | `Music Legacy/officewars-workday-long-cycle-audition.html` | Superseded three-way long-cycle discovery. |
| `OW-MUSIC-WORKDAY-MICROFORM` | `Rejected` | `Music Legacy/officewars-workday-microform-audition.html` | Retired six-versus-twelve movement diagnostic. |
| `OW-MUSIC-WORKDAY-MOTION` | `Rejected` | `Music Legacy/officewars-workday-motion-audition.html` | Superseded pace diagnostic. |
| `OW-MUSIC-WORKDAY-PALETTE` | `Rejected` | `Music Legacy/officewars-workday-palette-audition.html` | Superseded Workday palette discovery. |
| `OW-MUSIC-WORKDAY-PRODUCTION-IDENTITY` | `Rejected` | `Music Legacy/officewars-workday-production-identity-audition.html` | Superseded A/B/C production discovery. |
| `OW-MUSIC-WORKDAY-RELATIONAL-FORM` | `Rejected` | `Music Legacy/officewars-workday-relational-form-audition.html` | Rejected relational Draft 02. |
| `OW-MUSIC-WORKDAY-ROLE-TRANSFER` | `Rejected` | `Music Legacy/officewars-workday-role-transfer-audition.html` | Rejected role-reversal direction. |
| `OW-MUSIC-WORKDAY-SUPPORT` | `Rejected` | `Music Legacy/officewars-workday-support-audition.html` | Rejected subtle support-role diagnostic. |
| `OW-MUSIC-WORKDAY-TRANSITION-REPAIR` | `Rejected` | `Music Legacy/officewars-workday-transition-repair-audition.html` | Superseded local transition repair. |

### Rejection Lineage

Compact lineage and reusable lessons for rejected artifacts. The `Role` column
above carries each artifact's specific cause; this table carries only the
predecessor it derived from and the generalizable rule that should stop the
failure recurring. Generalized taste findings live in
`Wiki/Knowledge/Music/Listening Evidence/OfficeWars Melody and Handoffs.md`.

Only lineage stated in existing evidence appears here. A blank predecessor means
no explicit predecessor is recorded, not that none existed.

| Artifact | Predecessor | Reusable lesson |
|---|---|---|
| `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF` | `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF-COMPARISON` | Superseded, not rejected. A partial track's Approved baseline is replaced by its own extension every time the branch is promoted, so `Rejected` in this catalog does not always mean the music failed. Check `supersededOnMerit` before reusing a rejected page as a negative control. |
| `OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION` | `OW-MUSIC-BOSS-A-KERNEL-A-DROP` | Superseded, not rejected on merit. When a selected partial-track branch is promoted, its music carries forward unchanged and the shorter protected baseline becomes retained Legacy evidence. |
| `OW-MUSIC-BOSS-A-KERNEL-A-EXTENSION-COMPARISON` | `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF` | A comparison whose candidates differ in five notes and nothing else does return a verdict, unlike a production-only comparison. The discriminator was register, which is structural rather than a mix property. |
| `OW-MUSIC-BOSS-A-KERNEL-A-ENSEMBLE` | `OW-MUSIC-BOSS-A-KERNEL-A-STATIC-REPAIR` | Escalation carried only by a level ramp over a fixed accompaniment grid reads as uniform rather than rising. |
| `OW-MUSIC-BOSS-A-KERNEL-A-STATIC-REPAIR` | `OW-MUSIC-BOSS-A-IDENTITY-KERNEL` | After a main-thread stall, stacking overdue steps produces audible static. Skip late steps instead. |
| `OW-MUSIC-BOSS-A-IDENTITY-KERNEL` | `OW-MUSIC-BOSS-A-PALETTE-CHECK` | A scheduler defect can survive looping, so recurring artifacts are not fixed by longer exposure. |
| `OW-MUSIC-BOSS-A-PALETTE-CHECK` | | A matched `-2 dB` shelf below `140 Hz` was not perceptible. Direct evidence that production-only comparisons return no verdict. |
| `OW-MUSIC-BOSS-A-BARE-THEME` | `OW-MUSIC-BOSS-A-INTENSITY-3-REPAIR` | Equal-length monophonic lines over one shared harmony, plus the same nonresponsive backing engine on each, fail in both bare and full listening. |
| `OW-MUSIC-BOSS-A-INTENSITY-3-REPAIR` | `OW-MUSIC-BOSS-A-SECOND-MOVEMENT-SKETCHES` | A setup in bar 1 that never pays off is rejected regardless of what follows it. |
| `OW-MUSIC-BOSS-A-INTENSITY-3-FLOW` | `OW-MUSIC-BOSS-A-INTENSITY-3-REPAIR` | Filling a leap stepwise produces running scales. Repeating a landing note reads as hammering rather than as a tune. |
| `OW-MUSIC-BOSS-A-NEXT-MOVEMENT-DISCOVERY` | `OW-MUSIC-BOSS-A-OPENING-GRAMMAR-DISCOVERY` | Candidates recombined from the same quoted cells cannot be distinguished, so the comparison has no answer. Never encode an agent-invented apex cap. |
| `OW-MUSIC-BOSS-A-CONTINUOUS-TUNE` | | One continuous soloist loses the opening's changing instrumental ownership. |
| `OW-MUSIC-BOSS-A-DEVELOPMENT` | | Changing only callback overlays while repeating the same foreground and harmony is not development. |
| `OW-MUSIC-BOSS-A-REGISTER-DIALOGUE` | `OW-MUSIC-BOSS-A-MELODIC-DEVELOPMENT` | Two registers need distinct character identities, and a prepared ascent must reach its promised peak. |
| `OW-MUSIC-BOSS-A-POP-REPAIR` | `OW-MUSIC-BOSS-A-PAPER-BRUSH` | Fixing an envelope does not fix a scheduler backlog. |
| `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR` | `OW-MUSIC-BOSS-A-POP-REPAIR` | Headless loops did not reproduce the user's pops. A playback-system defect needs human confirmation. |
| `OW-MUSIC-BOSS-A-PRERENDER-REPAIR` | `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR` | Removing live scheduling does not remove impulses already baked at percussion boundaries. |
| `OW-MUSIC-WORKDAY-SUPPORT` | | A subtle support-role difference returned no verdict. Second direct evidence for the perceptibility gate. |

**Known gap.** Thirteen Workday rejections carry a one-line role and no recorded
cause: `BAND-ANSWER`, `CANDIDATE-C-FORM`, `DRAFT-01`, `DETOUR-FLOW`,
`FORM-REPAIR`, `LONG-CYCLE`, `MICROFORM`, `MOTION`, `PALETTE`,
`PRODUCTION-IDENTITY`, `RELATIONAL-FORM`, `ROLE-TRANSFER`,
`TRANSITION-REPAIR`. Recover a cause only from listening evidence in
`SOUNDTRACK_WORKLOG.md` or a verification record. Do not infer one from the
artifact's contents.

## Required Workflow

For every new or changed music artifact:

1. Assign a stable `OW-MUSIC-*` internal label before broad iteration.
2. Set exactly one lifecycle status.
3. Place the file in the matching canonical folder.
4. Update this catalog in the same task.
5. Build and verify a replacement before demoting its predecessor.
6. Once the replacement is valid, retag and relocate the predecessor in the
   same task. Do not leave superseded Test or Limbo files in `prototypes/`.
7. Retain audition artifacts as standalone HTML files. Temporary WAV, JS,
   render, or export assets may be used during development but must be embedded
   or removed before the lifecycle transition is complete.
8. Update the active music brief, worklog, decision ledger, handoff, verifier
   paths, documented hashes, mirrors, manifests, and packages when affected.
9. Preserve the last Approved or Completed bytes before experimentation.
10. Never infer approval from technical verification.
11. When an Approved cue remains unfinished, preserve that baseline in
    `Music Locked/` and create a separately labeled Test branch in
    `prototypes/`. Remove the Test branch only when development is explicitly
    closed or a Completed master replaces it.

When a Limbo artifact is diagnosed, preserve the useful material in a new Test
artifact. Once that Test exists, move the old Limbo artifact to
`Music Legacy/` and relabel it Rejected.
