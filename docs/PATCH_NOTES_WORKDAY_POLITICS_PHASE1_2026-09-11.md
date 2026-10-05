# Workday And Office Politics Phase 1

Implemented game SHA-256:
`BC0EC333C24C66C797804DEDCB92CBA1AB6A3D9EE0C0CDA1E759D4CF62A07081`

Implemented game size: `876,070` bytes.

## Calendar And Completion

- Intern now runs Wednesday-Friday at 45 required progress.
- Associate through CEO run Monday-Friday at
  `80/115/155/205/265/330`.
- The HUD shows the weekday and Overtime Bank.
- The first favorable meeting, Scope Renegotiation, and Master Services
  Agreement can bank overtime, up to Saturday and Sunday.
- Completing early locks the promotion but continues normal weekdays in
  Overdelivery.
- The player wins same-Clock-Out ties. Chad-first and unfinished Sunday states
  lose immediately. CEO completion wins immediately.
- Every successful non-final floor now routes through final Night, promotion
  recovery, Weekend, and Promotion Review.

## Overdelivery

- Overdelivery activates after the complete resolution chain that reaches the
  target.
- Later task-card and ordinary-action base progress and positive base stress
  use 20 percent values.
- Printed effects, traits, recovery, special effects, and generated effects
  remain full strength.
- Each extra 10 percent of the snapshotted target creates one tier.
- The player chooses Cash or recovery once for the complete payout.
- Reward growth flattens after tier 10.
- The first ten tiers each add 10 percent next-floor size and 10 percent Chad
  pace for one floor.
- Overdelivery recovery can create Focus but cannot trigger
  recovery-to-progress conversion.

## Chad

- Removed stacks, upgrades, quality wobble, bad-day coefficients, and the
  hidden boss multiplier.
- Neutral pace is derived directly from the current project target and the
  intended finish weekday.
- The forecast exposes neutral pace, expectations, placeholder modifier
  categories for later phases, direct subtraction, next-workday progress, and
  expected finish weekday.
- Boss floors retain their visible hostile actions for now but no longer
  secretly accelerate Chad.

## Persistence And Testing

- Active-run schema is now 2. Incompatible schema-1 runs are invalidated.
- Added the `overdeliveryPayout` checkpoint and exactly-once payout state.
- Added Phase 1 test API state for calendar, overtime, Overdelivery,
  expectations, and Chad decomposition.
- Later prepared-Workday-to-Politics-Review restoration remains Phase 2 work.

## Balance Boundary

A 100-seed scripted-skilled diagnostic produced 0 wins, 94 Chad losses, and 6
burnouts without runtime errors. This partial implementation does not yet
contain the politics tools designed to slow Chad, so the result does not
authorize tuning.
