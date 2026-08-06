# Contributing To OfficeWars

Thanks for helping improve OfficeWars.

## Before Starting

Read `AGENTS.md`, `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`, and
`docs/PROJECT_STATUS.md`. Search existing issues before opening a new one.

## Good Reports

For gameplay or balance feedback, include:

- the game hash or release tag;
- whether the run was human, random, scripted, or seeded;
- floor, workday, selected traits, important cards, and Home upgrades;
- the observed failure or dominant interaction;
- whether the concern is power, clarity, pacing, reliability, or enjoyment;
- screenshots or seeds when available.

Use the balance issue template rather than presenting one run as proof.

## Pull Requests

- Keep gameplay in `officewarsautobattler.html`.
- Do not add required packages, servers, external assets, or build tools.
- Keep workday playback AFK-friendly and deterministic across 1x, 2x, 4x, and
  Skip.
- Update player-facing text and active documentation with behavior changes.
- Run the smoke suite for narrow changes and broader verification for shared
  resolution, economy, traits, schedules, or UI changes.
- State what was tested and what remains unverified.

Balance changes need explicit design approval before implementation. A pull
request should not quietly turn a Draft recommendation into a Locked rule.

## AI-Assisted Contributions

AI assistance is welcome. Contributors remain responsible for checking generated
claims against the current HTML, preserving decision status, and disclosing
which tests actually ran.

## Scope

Focused fixes and well-supported design changes are preferred. Avoid unrelated
refactors, document churn, or new abstractions that do not remove real
complexity.
