# Adaptive Cinematic Workday — Phase 3.5

Implemented on 2026-09-11.

## Player-Facing Changes

- Workday actions now use embedded pixel-cinematic scenes instead of active
  walking, pathfinding, ambient wandering, and cubicle reservations.
- Managers announce directives before task choice. Every visible primary
  package carries one fixed Comply, Resist, or Negotiate response badge.
- Political events interrupt chronologically with irreversible choices and no
  timer, Back, or defer path.
- Skip hides animation and future HUD information, then stops at each
  unanswered event in order.
- Wrap-up uses a chronological results reel. Night objectives appear as
  `Pending Tonight` and reveal separately at Night finalization.

## Persistence And Accessibility

- Active-run schema is 5; incompatible active runs are cleared with settings
  and profile/tutorial metadata preserved.
- Prepared, interrupted, hidden-queue, and results-reel restoration preserve
  event snapshots, choices, secret rolls, reservations, within-entry phase,
  focus, hidden state, and reel position.
- Short landscape and 200-percent text use full-screen politics with a
  labelled current-action thumbnail.
- Reduced motion reveals the full results list immediately.

## Verification

The focused cinematic suite passes 31/31. Smoke, persistence/tutorial,
Phase 1-3, advanced interactions, Home/schedule, Night Planner, and
task-keyword/Help suites pass. A 100-seed diagnostic completed legally with
1 victory, 93 Chad losses, and 6 burnouts; it is not balance-readiness
evidence because Phases 4-5 remain unimplemented.

