---
name: officewars-ux-audit
description: Audit OfficeWars usability, onboarding, information architecture, readability, responsive behavior, interaction feedback, and accessibility. Use when the user asks whether the game is understandable, easy to navigate, readable, mobile-friendly, accessible, visually clear, or ready for average players.
---

# OfficeWars UX Audit

## Locate And Understand The Product

1. Locate the active OfficeWars root from the current working directory.
2. Read `AGENTS.md`, `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`,
   `docs/PROJECT_STATUS.md`, `docs/HANDOFF.md`, and relevant UX evidence.
3. Inspect the implemented HTML rather than auditing from screenshots alone.
4. Preserve the office-friendly autonomous Workday and single-file product
   constraints.
5. Separate usability defects from visual taste and balance preferences.

## Audit The Complete Journey

Inspect each player surface and transition:

- first launch, main menu, Continue Run, replacement confirmation, and reset;
- tutorial callouts, spotlight focus, skip, replay, and first-day comprehension;
- Morning task cards, rarity, family, costs, outcomes, rerolls, extra slots,
  pinned cards, Campaigns, Sales Cycles, and other exceptional modes;
- Resume HUD, Resume window, family tabs, XP, paths, capstones, tooltips, and
  flavor text;
- project, stress, workdays, cash, manager, Today effect, portraits, and speed;
- Workday schedule, movement, conversations, action ticker, outcome feedback,
  Skip, pause points, and Clock Out;
- Night outings, Homes, Deals, Lights Out, disabled choices, and finalization;
- Weekend, casino, Promotion, path selection, victory, defeat, and return to
  menu;
- save, refresh, restoration, and error recovery.

Check that exceptional modes visibly replace or augment the ordinary mental
model rather than relying on a buried sentence.

## Evaluate Information And Decisions

For every decision, verify that the player can learn before commitment:

- what is selectable and why;
- immediate progress, stress, cash, and relationship consequences;
- future effects, duration, charges, targets, and exclusions;
- what will be replaced, repeated, copied, guaranteed, or consumed;
- phase and timing of resolution;
- disabled-state reason and recovery path;
- current objective, next required step, and completion progress.

Progressive disclosure may reduce clutter but must not hide decision-critical
information. Prefer concise visible summaries with complete accessible details.

## Test Responsive And Accessible Behavior

Use real browser rendering and screenshots when available. Check:

- representative desktop, compact desktop, and supported mobile-landscape
  viewports;
- the portrait rotation gate and viewport changes;
- 200 percent text zoom and long labels;
- clipping, overlap, occlusion, overflow, layout shift, and stable controls;
- keyboard order, focus visibility, modal trapping, escape behavior, and
  restoration of focus;
- semantic names, roles, states, live feedback, and screen-reader reading order;
- color contrast, non-color state cues, reduced motion, animation timing, and
  flashing;
- pointer targets, hover-only information, touch alternatives, and disabled
  affordances;
- console errors, external requests, and blank or stale UI states.

Inspect screenshots visually; automated geometry checks alone do not establish
clarity.

## Prioritize Findings

Classify each finding:

- **Blocker**: prevents play, loses state, or makes a required decision
  inaccessible.
- **High**: likely causes wrong decisions or broad confusion.
- **Medium**: repeated friction, weak feedback, or meaningful accessibility
  cost.
- **Low**: polish or taste with limited gameplay impact.

For each finding, provide evidence, affected player and phase, frequency,
consequence, and a concrete recommendation. Identify text or mechanics that are
becoming too dense and suggest a leaner presentation rather than simply adding
more help text.

## Preserve Decision Boundaries

An audit produces recommendations, not automatic gameplay changes. Do not edit
the game unless the user asks for implementation. Record design changes as
Draft until approved, then use `$officewars-implement`. Use
`$officewars-full-verification` when the user asks for exhaustive release
evidence rather than a UX-focused pass.

## Report

Lead with prioritized findings and file or screenshot evidence. Then summarize
what passed, what was not run, responsive and accessibility coverage, and the
smallest high-value next pass.
