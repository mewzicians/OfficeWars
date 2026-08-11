# Task Keywords, Celestial Direction, And Night Planner Verification

Date: 2026-08-11

Game SHA-256 over LF content:
`387FB7F1062CFEA15E3D14A44D40E85FA4455EA53AE3B37BCC0E182DD9B6C969`

## Results

| Area | Status | Evidence |
|---|---|---|
| Task keyword glossary | Pass | `.officewars-task-keyword-verify.py` finds 41 ordinary cards with shared terms and validates full, Pinned, and picker interaction safety |
| Celestial direction | Pass | Five sampled points at desktop and landscape confirm east-to-west movement without crossing |
| Night Planner desktop | Pass | Four tabs, persistent footer, Hide Planner, room return, and no overflow |
| Night Planner landscape | Pass | Planner fits `844 x 390` without viewport or card obstruction |
| Room shortcuts | Pass | iPad, PC, Social door, Deal laptop, switch, and bed open their intended complete or focused flows |
| Night view preference | Pass | Planner finalization reopens the Planner; bed finalization reopens the room |
| Tutorial migration | Pass | Legacy step positions map into the ten-step schema without replaying completed material |
| Tutorial content | Pass | Night lesson opens the Planner and explains coworker bonus timing plus the optional room |
| Persistence | Pass | All 24 persistence, casino, and tutorial checks |
| Advanced interactions | Pass | All eight groups, including return-from-finalization without accidental Lights Out |
| Home and schedule | Pass | Desktop and landscape Home geometry, controls, manager presentation, arcs, and schedule trackers |
| Deterministic smoke | Pass | `PASS:OVERHAUL` |
| Readability visual matrix | Pass | `PASS:READABILITY_VISUAL_MATRIX` |
| Full no-simulation verification | Pass | Core values, all 50 cards, player surfaces, Night policy, browser integrity, and responsive layouts |

## Commands

```text
python .officewars-night-planner-verify.py
python .officewars-task-keyword-verify.py
python .officewars-home-schedule-verify.py
python .officewars-persistence-verify.py
python .officewars-advanced-verify.py
python .officewars-smoke-run.py
python .officewars-visual-capture.py --quiet
```

## Remaining Scope

- Fresh structural balance simulation is Not Run because this update changes
  presentation and onboarding rather than numeric balance.
- Formal screen-reader execution, exhaustive every-picker restoration,
  rapid-input fuzzing, and long-session memory profiling retain their previous
  Not Run or Blocked status.
