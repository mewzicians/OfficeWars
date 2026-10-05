# Music Workspace QA Cleanup

Date: 2026-08-19

## Scope

This cleanup reorganized source-only OfficeWars music auditions, repaired
their active references and verifier paths, synchronized durable records and
mirrors, and rebuilt the GitHub-ready public ZIP.

No gameplay code or shipped audio changed.

## Workspace Organization

The original `prototypes/` inventory contained 31 audition HTML files.

- `prototypes/` now contains exactly 2 unresolved auditions:
  - `officewars-boss-a-percussion-repair-audition.html`
  - `officewars-casino-scene-audition.html`
- `Music Locked/` contains 12 explicitly selected references.
- `Music Legacy/` contains 17 rejected, superseded, intermediate, or
  historical auditions.

All 29 moved HTML files retained their exact SHA-256 bytes. Folder indexes
explain the status boundaries and state that locked music is not shipped.

## Documentation Cleanup

- Updated `AGENTS.md`, `docs/WORKING_WITH_AGENTS.md`, and
  `docs/HANDOFF.md` to use the three-folder music model.
- Updated the OfficeWars music brief and soundtrack worklog.
- Corrected stale `active` labels on superseded Workday and Boss experiments.
- Updated every active music reference to its new location.
- Preserved dated evidence and historical pages without reactivating them.
- Added the current Boss percussion-repair diagnosis and technical status to
  the balance ledger, handoff, and music brief.

Verifier files that directly name moved auditions changed only in their source
paths. Protected-verifier hashes were updated through the Boss dependency
chain, and every affected Boss verifier was rerun.

## Active Boss Percussion Evidence

The active Boss percussion page replaces the remaining tonal square-wave hat
and snare edge with deterministic, non-tonal paper-brush noise while preserving
the liked tune, harmony, bass, undercurrent, form, and mix architecture.

The final exact verifier passed:

- two complete loops of the control, repaired full mix, and Brush Only mode;
- comparison-safe full-mix levels;
- direct movement starts, pause, resume, seeking, and rapid switching;
- desktop, landscape, and portrait layouts;
- maximum 22 tracked sources;
- no clipping; and
- cleanup to zero tracked sources.

Detailed evidence is
`verification/BOSS_A_PERCUSSION_REPAIR_2026-08-19.md`.

## Validation

### Pass

- 31-page audition inventory classified exactly as `2 active / 12 locked /
  17 legacy`.
- 29 moved audition hashes preserved.
- All 37 OfficeWars verifier scripts compile.
- Active Boss percussion full two-loop verifier.
- Active Casino entrance focused browser verifier.
- Locked Boss identity and On the Clock focused browser verifiers.
- Legacy Boss form and undercurrent dependency-chain verifiers.
- 89 active music-reference occurrences resolve to existing files.
- Root, public, and rollout game hashes remain
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`.
- Active text artifacts decode as strict UTF-8.
- Root-to-public and root-to-rollout mapped documents match byte-for-byte.
- Source-only auditions, verifiers, screenshots, and continuity ledgers remain
  excluded from both portable distributions.
- Rollout inventory contains 141 verified rows after this report is mirrored.
- Public ZIP contains 147 files after this report is mirrored and extracts
  byte-for-byte against the public mirror, including hidden files.

### Fail

None.

### Not Run

- Broad gameplay, balance, accessibility, persistence, and simulation suites;
  this cleanup changed no gameplay implementation.

### Blocked

None.

## Decision Boundary

The paper-brush Boss candidate is technically verified but remains
musically exploratory until human listening.

No music has been added to `officewarsautobattler.html`.
