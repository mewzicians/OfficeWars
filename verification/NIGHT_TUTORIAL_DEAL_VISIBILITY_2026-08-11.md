# Focused Night Tutorial And Deal Visibility Verification

Date: 2026-08-11

Game SHA-256 over LF content:
`BEE4D38FBDE4309664FDBD5EC49DC254816D0BE393D639A8549D58254EE4E15F`

## Results

| Area | Status | Evidence |
|---|---|---|
| Four Night lessons | Pass | Home Shop, Outings, Relationships, and recovery/finalization each open and spotlight their matching Planner surface |
| Tutorial length | Pass | The full first-play journey contains 13 ordered callouts |
| Tutorial migration | Pass | Schema 3 and schema 4 states migrate without replaying completed material |
| Deal Desk without access | Pass | Planner renders three tabs and omits Deal Desk |
| Deal Desk with access | Pass | Negotiation 3 restores Deal Desk as the fourth tab |
| Home picker alignment | Pass | Card group is centered in the usable desktop and `844 x 390` iPad content area |
| Deal picker alignment | Pass | Compact Deal cards fit and remain centered above the persistent footer |
| Persistence | Pass | All 24 save, casino, result, and tutorial checks |
| Advanced interactions | Pass | All eight groups; Night gameplay rules and finalization remain unchanged |
| Home and schedule | Pass | Desktop and landscape Home geometry, controls, manager presentation, arcs, and schedule trackers |
| Task keywords and celestial direction | Pass | Shared task glossary and east-to-west celestial paths remain intact |
| Deterministic smoke | Pass | `PASS:OVERHAUL` |
| Readability visual matrix | Pass | `PASS:READABILITY_VISUAL_MATRIX` |
| Full no-simulation verification | Pass | Core values, all 50 cards, player surfaces, Night policy, browser integrity, and responsive layouts |

## Commands

```text
python .officewars-night-planner-verify.py
python .officewars-persistence-verify.py
python .officewars-advanced-verify.py
python .officewars-home-schedule-verify.py
python .officewars-task-keyword-verify.py
python .officewars-smoke-run.py
python .officewars-visual-capture.py --quiet
python .officewars-full-verify.py 0
```

## Remaining Scope

- Fresh structural balance simulation is Not Run because this update changes
  onboarding and presentation rather than numeric balance.
- Formal screen-reader execution, exhaustive every-picker restoration,
  rapid-input fuzzing, and long-session memory profiling retain their previous
  Not Run or Blocked status.
