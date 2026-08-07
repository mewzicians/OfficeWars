# Snapshot Provenance

Created: 2026-08-06

This document records the original public-package snapshot. It is historical
provenance, not current candidate status. See `PROJECT_STATUS.md` for the
active game hash and verification evidence.

## Gameplay Source

`officewarsautobattler.html` was copied byte-for-byte from the active
OfficeWars workspace.

SHA-256:
`2A4880220763678436C6BDFA043EAD7777BB71F01547F8B17B047768206C1D78`

`index.html` is only a GitHub Pages launcher. It contains no gameplay logic.

## Copied Active Sources

- `docs/GAME_DESIGN.md`
- `docs/BALANCE_LEDGER.md`
- `docs/HANDOFF.md`
- `docs/ARCHIVE_SUPERSEDED.md`
- the three dated reports under `verification/`
- `.agents/skills/officewars-plan/`
- the smoke, full-verification, advanced-verification, visual-capture, and
  skilled-telemetry runners

At package creation, the public copies of the ledger, handoff, skill, and
verification checklist were adjusted only to remove references to the old
private portable-package layout and include the then-current simulation
status. Later synchronization may update active status files without changing
this original provenance record.

The copied Python runners received one portability change: the optional
workspace-local Playwright import path is now conditional, allowing a normal
environment installed from `requirements-dev.txt`.

## New Public Files

The README, repository setup guide, contribution guide, agent collaboration
guide, project status, playtest guide, issue templates, Pages launcher, and
repository metadata were written for this public snapshot.

## Intentionally Excluded

- browser profiles and temporary browser output;
- generated verification screenshots outside the three selected README assets;
- private historical handoff folders and full brainstorming archives;
- editor-specific settings;
- credentials, local machine configuration, and personal paths.

The historical non-gameplay `officewars-ui-prototype.html` was absent from the
original snapshot. The 2026-08-07 synchronized export added it because active
handoff documentation names it as a visual reference.
