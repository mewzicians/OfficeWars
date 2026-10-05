# Music Lifecycle QA Cleanup

Date: 2026-08-19

## Scope

This cleanup made the OfficeWars music lifecycle durable, added the
`Music Official/` destination for completed masters, cataloged every audition
with a stable internal label, and repaired two independently reproduced
static-pop causes inside the liked Boss A paper-brush treatment, then added a
single-buffer diagnostic for the remaining intermittent artifact.

No gameplay code or shipped audio changed.

## Lifecycle Model

Folder placement and lifecycle status have separate responsibilities:

- `Music Official/` contains only `Completed` standalone masters.
- `Music Locked/` contains `Approved` selected references.
- `prototypes/` contains active `Test` and temporary `Limbo` artifacts.
- `Music Legacy/` contains `Rejected` artifacts.

Every audition has one stable `OW-MUSIC-*` internal label, one status, and one
canonical path in `docs/music/officewars/MUSIC_CATALOG.md`.

`Approved` does not mean `Completed`, and `Completed` does not automatically
mean integrated or shipped. `Limbo` is intentionally temporary: diagnose the
mixed artifact, preserve its good material in a new Test, then reject the old
artifact.

Current catalog counts:

- `Completed`: 0
- `Approved`: 12
- `Test`: 2
- `Limbo`: 0
- `Rejected`: 20

`Music Official/` therefore begins empty except for its guidance.

## Boss A Pop Repair

The liked paper-brush pass moved through Limbo during diagnosis. Its noise
envelope contained an instantaneous gain drop from full level to `68 percent`,
creating a discontinuous `32 percent` transition that could produce an
intermittent broadband pop without clipping.

The old artifact is now the Rejected historical control:

- `OW-MUSIC-BOSS-A-PAPER-BRUSH`
- `Music Legacy/officewars-boss-a-percussion-repair-audition.html`

The envelope Test preserved its music and replaced only the abrupt gain
assignment with a continuous exponential decay:

- `OW-MUSIC-BOSS-A-POP-REPAIR`
- `Music Legacy/officewars-boss-a-pop-repair-audition.html`

Browser-rendered constant-signal envelope evidence measured:

- Rejected abrupt transition delta: `0.32`
- Smooth Test transition delta: `0.003025`

All four playback modes completed two uninterrupted loops with no clipping,
source accumulation, browser error, or cleanup leak. Human listening still
heard an inconsistent pop that could disappear after manual seek, so this
artifact became Rejected.

## Boss A Scheduler Repair

The remaining defect came from overdue scheduler steps rather than another
noise-envelope discontinuity. After a delayed main-thread tick, the old
catch-up loop scheduled several missed steps while every voice clamped to the
same near-future timestamp.

The scheduler Test preserved the smooth-brush music and advanced past overdue
steps:

- `OW-MUSIC-BOSS-A-SCHEDULER-REPAIR`
- `Music Legacy/officewars-boss-a-scheduler-repair-audition.html`

Under a forced `900ms` stall, the Rejected control scheduled five steps in one
tick and peaked at 36 sources. The Test skipped four overdue steps, scheduled
one current step, and stayed at the normal 21-source peak. Manual seek reset
the Rejected state to a 13-source peak, reproducing the user's observation.

All four scheduler-lab modes completed two loops with no clipping, source
accumulation, browser error, or cleanup leak. Human listening still heard
intermittent pops, so the artifact is Rejected as the active solution.
Detailed evidence is in
`verification/BOSS_A_POP_REPAIR_2026-08-19.md` and
`verification/BOSS_A_SCHEDULER_REPAIR_2026-08-19.md`.

## Boss A Pre-Rendered Playback Repair

The active Test preserves the exact resilient live mix while removing
continuous per-note scheduling, oscillator starts, effect allocation, and
node churn:

- `OW-MUSIC-BOSS-A-PRERENDER-REPAIR`
- `prototypes/officewars-boss-a-prerender-repair-audition.html`

A deterministic `24kHz` steady-state render uses a `24-step` preroll and one
complete `91.4286-second` cycle. The locally bundled stereo asset decodes in
approximately `256-288ms` and plays through one looping source.

The live control and Test each complete two uninterrupted loops. The live
control peaks at `22` sources; the Test peaks at one. Stalls, pause, resume,
seek, movement starts, rapid switching, maximum volume, responsive layout,
loop seam, and cleanup pass. Detailed evidence is in
`verification/BOSS_A_PRERENDER_REPAIR_2026-08-19.md`.

## Validation

### Pass

- All 34 audition HTML files are cataloged exactly once.
- Every internal label is unique.
- Every lifecycle status matches its canonical folder.
- Current folder inventory is `0 official / 12 locked / 2 prototypes /
  20 legacy`.
- The Rejected paper-brush control retained its exact audition bytes after
  moving to `Music Legacy/`.
- The smooth-envelope Test passed focused and repeated-loop verification.
- The resilient-scheduler Test passed forced-stall, focused, and repeated-loop
  verification.
- The pre-rendered Test passed asset-identity, seam, one-source runtime,
  forced-stall, focused, and repeated-loop verification.
- Active guidance routes future music work through the catalog.
- Root-to-public and root-to-rollout mapped documents match byte-for-byte.
- The rollout inventory contains 146 verified package rows after this report
  is mirrored.
- The public ZIP contains all 152 public-mirror files and extracts
  byte-for-byte, including hidden files.
- Source-only auditions, verifiers, screenshots, and continuity ledgers remain
  excluded from both portable distributions.
- Root game SHA-256 remains
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`.

### Fail

None.

### Not Run

- Human complete-form listening of the pre-rendered Test on the affected
  playback system.
- Broad gameplay, balance, accessibility, persistence, and simulation suites;
  this task changed no gameplay implementation.

### Blocked

None.

## Decision Boundary

`OW-MUSIC-BOSS-A-PRERENDER-REPAIR` remains `Test`. Technical verification does
not prove that the intermittent pop is absent on the user's playback system
and does not approve the complete boss cue.

No OfficeWars music currently qualifies as `Completed`, and no music was
added to `officewarsautobattler.html`.
