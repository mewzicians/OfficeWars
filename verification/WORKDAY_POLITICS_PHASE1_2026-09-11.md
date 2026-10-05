# Workday And Office Politics Phase 1 Verification

Date: 2026-09-11

Game SHA-256:
`BC0EC333C24C66C797804DEDCB92CBA1AB6A3D9EE0C0CDA1E759D4CF62A07081`

Game size: `876,070` bytes.

Rigor: standard.

## Results

| Layer | Verdict | Evidence |
|---|---|---|
| Focused Phase 1 rules | Pass | `.officewars-phase1-verify.py`: 25/25 |
| Browser smoke | Pass | `.officewars-smoke-run.py`: `PASS:OVERHAUL` |
| Persistence and tutorial | Pass | `.officewars-persistence-verify.py`: 24/24 |
| Advanced interactions | Pass | `.officewars-advanced-verify.py`: all groups pass |
| Home and schedule browser matrix | Pass | `.officewars-home-schedule-verify.py` |
| Full static/browser audit | Pass | `.officewars-full-verify.py 0`; simulations disabled |
| 100-seed scripted-skilled diagnostic | Pass for runtime; Fail for target | 0 wins, 94 Chad losses, 6 burnouts |
| Formal accessibility execution | Not Run | Phase 7 |
| Human playtesting | Not Run | Phase 7 |

## Focused Coverage

The Phase 1 verifier covers:

- all seven fixed size/calendar/Chad-target records;
- Intern Friday and ordinary Thursday neutral Chad pace;
- overtime cap and Sunday failure;
- same-day player priority and early completion lock;
- resolution-chain Overdelivery activation;
- task and ordinary-action 20-percent base scaling;
- Cash and recovery formulas;
- exactly-once payout persistence;
- next-floor expectation ordering;
- Chad direct subtraction;
- HUD weekday/overtime state;
- removal of Chad stack/upgrade state;
- save schema 2 and payout checkpoint; and
- floor-based Weekend routing.

## Simulation Interpretation

The 100-seed diagnostic is not a balance verdict for the approved overhaul.
Phases 3-5 will add the supporter, role, manager, campaign, Favor, and politics
tools that modify Chad. Preserve the Locked Phase 1 values until the complete
rules-faithful policy exists.

## Not Run

- Politics Review and its restoration boundary;
- dynamic rosters and standing;
- manager directives and boss schemes;
- Guided Intern;
- formal screen-reader execution;
- rapid-input fuzzing;
- memory profiling; and
- human comprehension and balance playtests.
