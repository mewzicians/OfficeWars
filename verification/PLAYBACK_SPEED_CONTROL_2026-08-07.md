# Playback Speed Control Validation

Date: 2026-08-07

Game SHA-256:
`1A0B7E86E2E0B64A06B5B99895A078A325584352F8D37E4A96F9DB9FCB2BB64A`

## Change

- Replaced the three separate speed buttons with one button that displays the
  current speed and cycles `1x -> 2x -> 4x -> 1x`.
- Doubled the presentation baseline. Player-facing `1x`, `2x`, and `4x` now
  use effective timing multipliers `2`, `4`, and `8` relative to the previous
  baseline.
- Preserved the selected player-facing speed between workdays.
- Updated movement timing, accessible labels, tooltips, How to Play text, and
  automated control checks.

## Evidence

- `python .officewars-smoke-run.py`: `PASS:OVERHAUL`.
- `python .officewars-full-verify.py 10`: every automated audit check passed,
  including semantic button checks and the exact
  `1x/2x/4x/1x -> 2/4/8/2` cycle.
- `python .officewars-advanced-verify.py`: all eight high-risk interaction
  groups passed with no page errors, console errors, or external requests.
- `python .officewars-visual-capture.py`: the 13-case readability matrix
  passed with no sampled clipping, viewport overflow, or persistent-HUD
  overlap.
- Desktop and landscape-phone Workday screenshots were inspected. The cycling
  speed button and Skip remain readable and do not overlap adjacent HUD
  elements.

## Scope

This is a presentation-speed and control-layout change. Gameplay resolution,
randomness, task values, workday ordering, and Skip behavior are unchanged.
The broader Pass, Fail, Not Run, and Blocked matrix remains recorded against
its exact dated hash in `FULL_VERIFICATION_2026-08-07.md`.
