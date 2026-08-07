# Skip Fix Local Validation

Validation date: 2026-08-07

Validated game SHA-256:
`41A3CC9823C032C1D80518DB61E0C9289C5CDAADFD9EAE3C16F1E587092A71A0`

## Verdict

The deterministic Skip repair passes local browser validation. The candidate
remains below final ship signoff because structural balance is still open.

## Passed Evidence

- The expanded `.officewars-smoke.html` suite passed four consecutive browser
  runs.
- All eight groups in `.officewars-advanced-verify.py` passed without page
  errors, console errors, or external requests.
- `.officewars-full-verify.py 0` passed every implemented runtime, static,
  accessibility, disclosure, and sampled-layout check.
- Seven visual captures covering desktop, compact desktop, landscape phone,
  portrait rotation, Morning, Workday, and Night reported no persistent-HUD
  overlap or viewport overflow and passed visual inspection.
- Every local Markdown link in the public snapshot resolves to an included
  file.
- The implemented game hash remained unchanged after validation.

The Skip smoke coverage includes 1x/2x/4x/Skip gameplay and RNG parity,
meetings, Office Chat, desk visits, sabotage, stalled wrap-up, repeated Skip,
rollback before and after mutation, ambient contention, malformed participant
identifiers, converted meetings, and opening-event burnout cleanup.

## Structural Simulation Comparison

The same 1,000 seeds per policy completed without errors on both snapshots:

| Policy | Prior `2A488...` | Current `41A3...` |
|---|---:|---:|
| Baseline | 0.7% | 0.7% |
| Random | 12.2% | 12.2% |
| Scripted-skilled | 55.3% | 58.4% |

The current skilled policy recorded 584 victories, 179 burnouts, 177 rival
losses, and 60 deadline losses. `Regression Tests` selections increased from
2,567 to 3,160.

No numeric card, economy, project, coworker, or balance constants changed.
Prelocking workday gameplay changes RNG consumption and therefore changes
cross-version seeded trajectories. Treat the 58.4 percent result and increased
`Regression Tests` selection rate as current balance evidence, not as a new
approved tuning decision.

## Remaining Scope

- Human playtest evidence remains pending.
- The structural balance target remains 25-35 percent for a genuinely skilled
  player or policy.
- Dated reports written against `2A488...` remain valid only for that prior
  snapshot unless their checks were rerun above.
