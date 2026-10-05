---
name: officewars-debug
description: Reproduce, diagnose, fix, and regression-test OfficeWars defects without changing unrelated behavior. Use when the user reports broken, desynchronized, inconsistent, stuck, duplicated, missing, or incorrect game behavior, including persistence, deterministic playback, UI state, simulation, and packaging failures.
---

# OfficeWars Debug

## Locate And Establish Truth

1. Locate the active OfficeWars root from the current working directory.
   Require `AGENTS.md`, `officewarsautobattler.html`,
   `docs/GAME_DESIGN.md`, and `docs/BALANCE_LEDGER.md`.
2. Read `AGENTS.md`, the relevant active documents, and the latest handoff.
3. Record the exact HTML hash and inspect the affected implementation.
4. Distinguish an implementation defect from intended behavior, a stale
   document, a test-policy error, corrupted input, or an unsupported state.
5. Do not treat a proposed balance preference as a bug.

## Reproduce Precisely

Capture as much of the failing state as the evidence permits:

- game hash, browser, viewport, and text scale;
- seed and gameplay or ambient RNG state;
- save version and relevant persisted payload;
- floor, day, phase, manager, project, stress, cash, and Chad state;
- selected card, trait paths, Homes, coworkers, pending resources, and modes;
- playback speed or Skip;
- exact actions immediately before and after the failure;
- console, assertion, screenshot, or telemetry evidence.

Prefer the smallest deterministic reproducer. If the report is intermittent,
instrument the relevant boundary without changing game outcomes.

## Diagnose Root Cause

1. Trace the failure through state mutation, rendering, persistence, and
   resolution ordering.
2. Check repeated invocation, stale closures, delayed callbacks, rollback,
   phase transitions, and mismatched canonical IDs.
3. Compare normal playback with 1x, 2x, 4x, and Skip when the Workday is
   involved.
4. Compare fresh play with save and restore when persistent state is involved.
5. Inspect neighboring rules that share the same helper or state field.
6. Name the root cause before editing. Do not patch only the visible symptom.

## Fix Narrowly And Completely

- Reuse existing helpers and preserve the standalone HTML architecture.
- Make the smallest change that repairs the root cause and all affected
  entry points.
- Preserve unrelated behavior, RNG consumption, and decision ordering.
- Keep atomic resolution and transactional rollback intact.
- Do not silently rebalance numbers, rewrite rules, or invalidate saves.
- Update player-facing copy only when it was wrong because of the defect.

## Prove The Repair

1. Add or extend a focused regression that fails before the fix and passes
   after it.
2. Test the exact reproducer and at least one neighboring legal state.
3. Test empty, maximum, repeated, interrupted, and phase-boundary cases when
   relevant.
4. Verify playback parity and save or restore parity when relevant.
5. Run syntax, smoke, advanced, persistence, visual, or simulation checks in
   proportion to the shared code touched.
6. Record exact hashes, seeds, fixtures, and Pass, Fail, Not Run, or Blocked
   status.

If the failure cannot be reproduced, do not invent a fix. Preserve useful
instrumentation or a minimal test and report the missing evidence.

## Synchronize The Repair

Update affected documentation, handoff, patch notes, verification evidence,
public mirror, and manifests. Keep the HTML and active
documents aligned. Invoke `$officewars-qa-cleanup` when drift extends beyond
the defect and `$officewars-full-verification` when the fix is release-wide or
the user requests ship readiness.

## Report

State the symptom, root cause, fix, regression evidence, exact changed files,
current game hash when changed, and any residual risk or unverified surface.
