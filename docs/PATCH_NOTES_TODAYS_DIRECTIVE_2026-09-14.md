# Today’s Directive Simplification

Implemented on 2026-09-14.

## Player-Facing Changes

- The manager announcement is centered and text-only: manager name,
  deliverable, and quoted directive title.
- `The Penny Pincher` and `The Slave Driver` now use consistent names
  everywhere.
- Task modifiers still use fixed Comply, Resist, and Negotiate assignments.
  Cost and affordability remain printed on the badge.
- Manager modifier tooltips contain only `SUCCESS` and `FAILURE` effects.
- The Manager HUD now tracks `TODAY’S DIRECTIVE` as `IN PROGRESS`,
  `COMPLETE`, or `FAILED`, then shows the applied reward or penalty.
- Night directive results apply automatically and use a nonblocking banner
  instead of a result-confirmation modal.

## Rules

- Manager directives are deterministic and consume no gameplay RNG.
- Monotonic completion and irreversible failure settle immediately.
  Remaining Workday and Night conditions settle at their period boundary.
- Hold the Line starts tracking spending after the modifier cost is paid.
  Protect the Reserve still sees the reduced Accounted Cash.
- Reorg Approval Leverage adds one Approval on completion for the player role
  or removes one additional Approval on failure for the Chad role.
- Existing modifier costs and Success/Failure effects are unchanged.
- Active-run schema is 6; incompatible active runs are cleared while profile,
  tutorial, and settings metadata remain.

## Readability

The manager tooltip, Help pages, Day Actions explanation, coworker explanation,
Clock Out manager result, and Night result flow were reduced to the effects
the player needs. Chad forecast, Build Context, glossary definitions,
non-manager political odds, and task effects retain their detailed views.

