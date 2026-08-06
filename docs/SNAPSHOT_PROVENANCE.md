# Snapshot Provenance

Created: 2026-08-06

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

The public copies of the ledger, handoff, skill, and verification checklist
were adjusted only to remove references to the old private portable-package
layout and to include the latest Chain 9 simulation status.

The copied Python runners received one portability change: the optional
workspace-local Playwright import path is now conditional, allowing a normal
environment installed from `requirements-dev.txt`.

## New Public Files

The README, repository setup guide, contribution guide, license guide, agent
collaboration guide, project status, playtest guide, issue templates, Pages
launcher, and repository metadata were written for this public snapshot.

## Intentionally Excluded

- browser profiles and temporary browser output;
- generated verification screenshots outside the three selected README assets;
- private historical handoff folders and full brainstorming archives;
- the historical non-gameplay UI prototype;
- editor-specific settings;
- credentials, local machine configuration, and personal paths.
