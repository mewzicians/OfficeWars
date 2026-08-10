# Build Context And Pinned Tasks Patch

Date: 2026-08-10

Implemented game SHA-256:
`2C15A37A71AFA22626B742EF4D88ACC0209DB5AB3FB763ED25549E7050D0CC9C`

## Morning Decisions

- Added a compact `Build Context` strip above the task offer whenever the run
  has active resources, delayed effects, Delegates, or Contacts.
- Targeted delayed effects identify their selected target. For example, API
  Follow-Up names the Skill that will receive its additional Skill XP.
- Delegate and Contact entries name the selected coworkers. Full rules remain
  available through hover, keyboard focus, tap, the Resume, and the existing
  active-effect strip.
- The strip shows at most six entries and sends overflow to the Resume instead
  of expanding indefinitely.

## Pinned Tasks

- Replaced full pinned cards in the Morning panel with compact rows containing
  only Skill, task name, and rarity.
- Activating a pinned row opens the ordinary full task-card presentation with
  its current progress, stress, effect, source, Select Task, and Back actions.
- The dialog supports keyboard focus trapping, Escape, backdrop close, touch,
  and focus restoration to the originating pinned row.

## Resume

- Milestone squares at 3, 6, and 10 XP now expose their exact selected-path
  effect through hover, focus, and tap.
- A Skill without a selected specialization explains that specialization has
  not been chosen yet.
- Increased the visibility of all five decorative 8-bit Skill scenes while
  retaining the foreground scrim and stronger high-contrast fallback.

## Verification

- `python .officewars-visual-capture.py --quiet`: **Pass**, 36 cases
- `python .officewars-smoke-run.py`: **Pass**
- `python .officewars-persistence-verify.py`: **Pass**, 23/23 checks
- `python .officewars-advanced-verify.py`: **Pass**, 8/8 groups
- `python .officewars-full-verify.py 0`: **Pass**
- Fresh structural balance simulation: **Not Run**, because this patch changes
  presentation and inspectability rather than gameplay values or resolution
  paths

Detailed evidence is in
`../verification/BUILD_CONTEXT_PINS_2026-08-10.md`.
