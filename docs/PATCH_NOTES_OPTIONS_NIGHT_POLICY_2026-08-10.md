# Options And Night Policy Patch

Date: 2026-08-10

Implemented game SHA-256:
`037A7BA364D0CAC4E40A4BAA78C8AF36022B0FF8D089D65AE6EE2F51F7AE9D0B`

## Player Options

- Replaced the placeholder Options button with a real Options screen.
- Added a persistent master-volume slider from 0 to 100 percent. No audio is
  shipped yet; future audio elements use the stored setting automatically.
- Moved tutorial reset from How to Play into Options.
- Resetting the tutorial schedules the full orientation for the next New Run
  without changing or deleting the active run.
- Existing meta saves without a volume field remain compatible and receive the
  70 percent default.

## Headless Night Repair

- Added one shared Night-finalization helper for the player and simulation
  paths.
- Automatic Lights Out is applied only when no Home or Deal purchase blocks
  it.
- Moodboard and other explicit purchase exceptions still allow both.
- The headless policy no longer grants itself Lights Out after shopping.

## Verification

- `python .officewars-smoke-run.py`: **Pass**
- `python .officewars-persistence-verify.py`: **Pass**, 23/23 checks
- `python .officewars-advanced-verify.py`: **Pass**, 8/8 groups
- `python .officewars-full-verify.py 0`: **Pass**
- Options desktop and landscape-phone samples: **Pass**, with no sampled
  clipping, viewport overflow, page errors, console errors, or external
  requests
- Fresh structural balance simulation: **Not Run**

Detailed evidence is in
`../verification/OPTIONS_NIGHT_POLICY_2026-08-10.md`.
