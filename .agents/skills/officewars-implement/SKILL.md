---
name: officewars-implement
description: Implement approved OfficeWars gameplay, UI, persistence, documentation, and release changes end to end. Use when the user asks Codex to build, implement, ship, wire up, or apply an approved OfficeWars feature or fix, including when implementation work is the clear next step after a design decision.
---

# OfficeWars Implement

## Locate The Workspace

1. Locate the active OfficeWars root from the current working directory.
   Require `AGENTS.md`, `officewarsautobattler.html`,
   `docs/GAME_DESIGN.md`, and `docs/BALANCE_LEDGER.md`. Never resolve project
   files relative to the installed skill directory.
2. Read `AGENTS.md`, `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`,
   `docs/PROJECT_STATUS.md`, and `docs/HANDOFF.md`.
3. Treat the HTML as implemented truth, the game design as stable product
   truth, and the balance ledger as decision-status truth.
4. Inspect the smallest relevant HTML systems before proposing an edit.

## Confirm The Implementation Contract

- Separate the requested behavior from adjacent ideas, Drafts, and Open
  questions.
- Implement only the behavior the user approved or directly instructed Codex
  to build. Do not choose between unresolved alternatives silently.
- Report any conflict between the request, ledger, design document, and HTML
  before editing.
- Preserve unrelated user changes and existing local patterns.
- Do not turn a narrow request into a broad refactor unless the existing
  architecture makes the broader change necessary.

## Build An Impact Map

Before editing, trace the change through every affected surface:

- card, trait, action, phase, economy, relationship, rival, or manager rules;
- selection, Complete Play, Replay, effect-copy, Assist, and resolution order;
- deterministic 1x, 2x, 4x, and Skip behavior;
- active-run save schema, restore checkpoints, migrations, and reset behavior;
- morning, Workday, Clock Out, Night, Weekend, Promotion, and result UI;
- descriptions, tooltips, forecasts, legends, How to Play, and tutorial copy;
- simulations, fixtures, browser checks, and verification evidence;
- active documentation, rollout handoff, public mirror, manifests, and ZIP.

Use the map to find required edits, not to expand the approved design.

## Implement Coherently

1. Prefer existing helpers, state objects, rendering functions, and
   data-driven tables in the standalone HTML.
2. Make the smallest coherent edit that implements the complete behavior.
3. Keep task outcomes atomic and preserve the documented ordering model.
4. Keep playback speed presentation-only. Watching, accelerating, and
   skipping must produce identical gameplay state and RNG consumption.
5. Preserve the office-friendly AFK workday. Add decisions only at natural
   decision points unless the approved mechanic explicitly requires otherwise.
6. Keep player-facing rules inspectable. Update every affected label,
   description, tooltip, forecast, help entry, and exceptional-mode surface.
7. Preserve backward-compatible active saves when practical. If a migration
   or invalidation is necessary, make it explicit, versioned, and tested.
8. Keep the shipped game as one standalone HTML file with no required build
   step, server, framework, or external runtime dependency.

## Validate In Risk Order

Run the narrowest useful checks first, then broaden according to blast radius:

1. Validate JavaScript syntax and static integrity.
2. Exercise the changed path in a focused deterministic fixture.
3. Test neighboring interactions, failure paths, duplicate invocation, and
   boundary values.
4. Compare 1x, 2x, 4x, and Skip when Workday resolution is affected.
5. Test save, refresh, continue, and phase restoration when persistent state is
   affected.
6. Capture desktop and mobile or landscape UI evidence when player-facing
   layout changes.
7. Run broader smoke, advanced, persistence, visual, or simulation suites only
   when their systems are in the impact map.

Never claim a suite passed when it did not run. Record Pass, Fail, Not Run, or
Blocked and preserve exact hashes or seeds for meaningful evidence.

## Synchronize Project Truth

- Update stable design documentation only when the product model changed.
- Update the balance ledger with the exact implemented or approved decision;
  do not promote unrelated Drafts or Open questions.
- Update project status, handoff, patch notes, and verification evidence as
  appropriate.
- Synchronize mapped root files to the rollout and public mirrors.
- Refresh manifests, hashes, and the public ZIP after release-package changes.
- Use `$officewars-qa-cleanup` for broad synchronization or stale-document
  cleanup and `$officewars-full-verification` for exhaustive ship readiness.

## Report

Summarize the implemented behavior, important files, validation evidence,
current game hash when changed, and any remaining Draft, Open, Not Run, or
Blocked work.
