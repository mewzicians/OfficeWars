# Persistence And Orientation Validation

Date: 2026-08-07

Game SHA-256:
`9BFBBA2053BD5F5ED240D4BBC445A4C49B28930F4618610737160E300CAB2842`

## Implemented Scope

- One schema-versioned active-run save uses `officewars.save.v1`.
- Tutorial progress and replay preference use separate
  `officewars.meta.v1` storage.
- Continue Run restores valid saves; corrupt and incompatible saves are
  discarded.
- Stable phases and committed decisions autosave. A prepared Workday restores
  deterministically and resolves headlessly to Clock Out.
- Victory and defeat summaries persist until dismissed or replaced.
- Casino checkpoints preserve chips and active state. Pending Slots settle
  once, while Blackjack and Poker return to legal continuation states.
- Six contextual orientation steps spotlight the existing interface. Players
  can advance, skip, or schedule a replay through How to Play.

## Focused Evidence

`python .officewars-persistence-verify.py` passed 23 checks:

- serializer round trip for Set, Map, and non-finite numbers;
- corrupt and incompatible save rejection;
- Floor Intro, Morning offer, prepared Workday, Night, and result restoration;
- deterministic prepared-Workday replay with no duplicate task rewards;
- New Run replacement confirmation and Return to Main Menu cleanup;
- pending Slots settlement exactly once across repeated reloads;
- active Blackjack hand and Poker decision restoration;
- six-step orientation order, persistent skip, and replay reset; and
- no page errors in persistence, casino, or tutorial contexts.

The same hash also passed:

- `python .officewars-smoke-run.py`;
- `python .officewars-advanced-verify.py`;
- `python .officewars-full-verify.py 10`; and
- `python .officewars-visual-capture.py --quiet`.

The 13-case ordinary visual matrix explicitly completes orientation before
non-tutorial fixtures. Tutorial desktop and landscape screenshots were
captured separately and inspected.

## Defect Found And Fixed

The first casino restore test found that `beforeunload` could overwrite
`weekendCasino` with a generic `weekend` checkpoint. Stable-phase autosave now
preserves `weekendCasino` whenever the casino is active. The Slots, Blackjack,
and Poker restore checks pass after this repair.

## Remaining Scope

This focused suite does not close the broad report's exhaustive
every-picker, every-transition, screen-reader, rapid-input, or memory-profile
rows. Final balance release also remains blocked by the 58.4 percent
scripted-skilled result against the 25-35 percent target.
