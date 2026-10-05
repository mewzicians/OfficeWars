# Boss A Kernel A Ensemble Selection

Date: 2026-08-25

## Question

The user liked selected Kernel A's melody and asked whether its ensemble was
weak.

## Diagnosis

Source analysis found the accompaniment competent but **non-responsive**, not
absent.

- Bass rhythm was `[0,+3,+6]` in all eight bars.
- Harmonic rhythm was two hits per bar for seven of eight bars.
- Kick on local `0` and `4` and snare on local `2` and `6` were hard-coded in the
  engine, so percussion functioned as a metronome; `kickExtra` added four hits.
- The melody's `C6` apex is step 54, but the loudest bass note was step 62 and the
  largest chord hit step 56, so the band peaked a bar late.
- Bar 4 withholds its triangle completion and support did not respond.
- Escalation was a global `3.6 dB` intensity ramp: the loudness-only impact
  failure mode.

A mute compare met the ratified rejection condition: removing the bass lost
thickness but deleted no nameable phrase function.

## Comparison Contract

`OW-MUSIC-BOSS-A-KERNEL-A-ENSEMBLE` compared `Current` against `Responsive` with
both candidates derived from one source block. Saw, triangle, reduction, length,
harmony, roots, `intensity`, palette and scheduler were byte-identical under
build-time drift guards, so only bass, chord placement and percussion placement
changed. Both ran on the resilient `skip-overdue` scheduler so the then-unlistened
static defect could not confound the judgement.

`Responsive` gave each role a phrase job:

- **bass as consequence** — events per bar `3,3,4,2,2,4,5,3`, a long low E and an
  unresolved `G#2` for the bar-4 refusal, the loudest note on step 54, and the line
  vacating before step 62;
- **harmony as destination** — hits per bar `2,2,3,1,2,3,4,2`, stabs on triangle
  completions, one unmoving pad in bar 4, densest in bar 7; and
- **percussion as pressure** — bar 4 withholds the snare entirely and keeps one
  kick, so bar 5 reclaims the backbeat.

Percussion placement became data-driven through `kickSteps` and `snareSteps` with
the fixed grid retained as fallback, so no audio-graph node changed.

## Listening Outcome

Human listening selected `Responsive`.

## Approved Artifact

`OW-MUSIC-BOSS-A-KERNEL-A-RESPONSIVE-ENSEMBLE` is `Approved` at
`Music Locked/officewars-boss-a-kernel-a-ensemble-audition.html`. It contains only
the selected candidate; the rejected `Current` control stays in the Rejected
comparison page.

- Page SHA-256:
  `82ADD7D07E61B8E64236B25B73CF77FFB81A3A0FEB9B4172F8723F00D425C570`
- Size: `61530` bytes, live synthesis, no embedded audio, LF-only.
- Source comparison SHA-256 as heard and as recorded in the Approved page's
  `auditionSourceHash`:
  `A2EA555302153B1B2ECEB818A3BD6808CF43C73D14D6FED2026F5AB5F0D2D15E`
- Upstream kernel SHA-256 as heard:
  `1391A5281507AC596BB27A194E9B2CFE313F4481BBF4BD9FE31777ACDA09ECD7`

Both predecessors were then retagged from `Test` to `Rejected` on their header chip,
footer chip, and `selectionInfo()` lifecycle field, matching the identity-kernel
page's precedent. Their current bytes are
`AAD596309E7BC9267B64149628D8CBA64160DE83CB3CCE524DED203AB9BF9075` and
`9D9CB51BA6237C947D9C7016C8BA57BFB2A2B3DFE6295EA43183CA79F22FEB8E`. The retag
script reverses its own substitutions and requires the result to equal the original
bytes, so no musical, palette, scheduler, or layout byte moved. Rebuilding the
Approved page from the retagged source reproduces
`82ADD7D07E61B8E64236B25B73CF77FFB81A3A0FEB9B4172F8723F00D425C570` exactly, which
independently confirms the retag touched nothing the Approved artifact depends on.

Embedded provenance fields record the bytes a page was built from at build time and
are deliberately not rewritten by a later status-only retag. Verifier hash pins
record current on-disk bytes and are.

## Verification

- Static verification `.officewars-boss-a-kernel-a-responsive-ensemble-verify.py`:
  `64 passed, 0 failed`. All eleven music fields are byte-identical to the audition
  heard, the melody is byte-identical to upstream selected Kernel A, both Rejected
  pages' bytes are unchanged by their moves, and the page declares `Approved`,
  `ensembleSelected:true`, `integrated:false` and `shipped:false`.
- Browser smoke test
  `.officewars-boss-a-kernel-a-responsive-ensemble-browser.py`: `51/51` as run on
  2026-08-25. One candidate exposed, every one of the five monitors runs clean and
  creates sources, a 13-second run completes a loop with zero skipped steps,
  sources release after stop, and there is no horizontal overflow at `420 px`.
  This record originally also claimed support-only was "quieter than full". That
  clause is retracted: the analyser sits after a `DynamicsCompressorNode` and the
  meters are smoothed and decaying, so level ordering cannot show that a monitor
  mutes a voice. The test was corrected on 2026-08-26 to assert only audibility
  and headroom and to prove the muting by peak source counts, and it now passes
  `53/53`. The playback conclusions above are unaffected.
- Comparison page verification still passes `60` static and `75` browser checks at
  its Rejected path.
- Game and Approved rollback hashes unchanged.

A real defect was found and fixed during this pass: the longer Approved status chip
grew the header's min-content width and overflowed a `420 px` viewport by `9 px`,
because `.topbar-inner` is a `display:flex` row with `gap:24px` and no
`flex-wrap`, while `.status` is `white-space:nowrap`. The fix is `flex-wrap:wrap`,
applied in the build script rather than by hand-editing the generated page.

## Watchpoints Carried Forward

- `Responsive` is not density-neutral: 26 bass events against 24 and 19 chord hits
  against 15, though percussion is sparser at 18 hits against 20. Some of the
  improvement may come from more pitched support rather than from responsiveness
  alone.
- `intensity` was held byte-identical, so the `3.6 dB` level ramp still does
  escalation work. Whether it can now be reduced is untested.

## Extension Obligation, Discharged

Kernel A is eight bars, so this Approved artifact is a partial track, and under
the extension rule a partial track promoted to `Approved` owes one `Test`
extension branch in `prototypes/`. On 2026-08-26 the obligation was first
recorded as outstanding across `AGENTS.md`, `MUSIC_CATALOG.md`,
`docs/music/officewars/README.md`, `docs/BALANCE_LEDGER.md`, `docs/HANDOFF.md`,
`prototypes/README.md`, and `Music Locked/README.md`, because the branch's
content depended on which open question the user chose and inventing the music to
satisfy the rule is prohibited.

The user then selected the handoff from `Challenge Issued`, and the branch was
built the same day as `OW-MUSIC-BOSS-A-KERNEL-A-HANDOFF` at
`prototypes/officewars-boss-a-kernel-a-handoff-audition.html`. Those seven
surfaces now record the branch as open. Its own evidence is
`verification/BOSS_A_KERNEL_A_HANDOFF_2026-08-26.md`.

## Not Established

Approved is not Completed and not shipped. Which handoff treatment is selected,
harmonic destination and cadence, longer form, and game integration all remain
open. Technical verification is not approval, and automated playback is not human
listening.
