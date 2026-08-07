# Skip Day Reliability Patch Notes

Release date: 2026-08-06

Implemented game SHA-256:
`41A3CC9823C032C1D80518DB61E0C9289C5CDAADFD9EAE3C16F1E587092A71A0`

## Summary

Skip Day now completes the same locked workday as 1x, 2x, or 4x playback. It
no longer depends on presentation timers, walking, or ambient conversations to
advance, and a recoverable resolution error no longer leaves the interface
frozen on `SKIPPING...`.

This patch changes playback reliability only. It does not change card values,
economy values, project requirements, coworker effects, or other balance
rules.

## What Players Will Notice

- Skip reliably finishes the active action and every remaining scheduled
  action, including days with meetings, Office Chat, desk visits, and sabotage.
- Meeting and chat outcomes no longer change based on whether the day is
  watched, accelerated, or skipped.
- Daily visitors and saboteurs are selected before playback and remain the same
  at every playback speed.
- Sabotage resolves at a consistent midpoint: immediately after the normal
  daily desk visit.
- Pressing Skip more than once cannot resolve the day twice.
- If an unexpected action error occurs, the workday is restored to its
  pre-Skip state and Skip becomes available for a deterministic retry instead
  of freezing the game.
- Burnout during an opening event or workday now clears the active playback
  lifecycle cleanly.

## Root Cause

The meeting presentation layer saved visual sprite identifiers such as `cw1`
and `rival` into gameplay participant records. The resolver expects canonical
gameplay identifiers such as `karen` and `chad`. When Skip tried to resolve one
of those meetings, participant lookup returned no character and JavaScript
threw after the Skip control had already been disabled and animation timers had
been cleared. With no remaining timer or resolver to advance the day, the UI
appeared frozen.

Several related timing paths could also choose gameplay participants or apply
midday events at different moments depending on presentation speed. Those
paths made an intermittent failure harder to reproduce and could allow watched
and skipped playback to diverge.

## Engineering Changes

### Canonical participant records

- Added participant normalization that translates legacy sprite identifiers to
  gameplay identifiers.
- Invalid and duplicate participants are removed, and meetings are filled to
  three valid unique participants.
- Meeting dialogue and summaries now persist canonical gameplay identifiers.
- Runtime-converted meetings preserve their already prepared participant trio.

### Locked deterministic workdays

- Team Meeting participants and outcomes, Office Chat partner and outcome, the
  daily visitor, and sabotage identity are prepared before presentation.
- Watched, accelerated, skipped, and headless resolution use the same prepared
  gameplay data.
- Dialogue-only shuffling uses the cosmetic random stream and cannot alter
  gameplay results.
- Daily desk visits and sabotage now resolve in one fixed order across every
  playback mode.

### Transactional Skip recovery

- Skip retains the active resolver until resolution actually succeeds.
- The game snapshots workday state, gameplay and cosmetic random streams,
  schedule position, pending visits, active action data, and resolver state
  before fast-forwarding.
- An exception before or after a gameplay mutation restores that snapshot,
  clears presentation-only state, and re-enables Skip for the same retry.
- Missing-resolver and burnout paths now restore or clear controls, timers,
  reservations, movement, and conversation state instead of leaving playback
  stranded.

## Regression Coverage

The smoke source now compares gameplay state and gameplay random state across
1x, 2x, 4x, and Skip for:

- meeting setup and dialogue;
- Office Chat setup and dialogue;
- active daily desk visits;
- unresolved sabotage;
- stalled workday wrap-up;
- repeated Skip input;
- exceptions before and after gameplay mutation;
- real ambient conversation contention;
- legacy, mixed, duplicate, and invalid participant identifiers;
- a final meeting converted to another action; and
- opening-event burnout and playback lifecycle cleanup.

## Validation Status

Initial implementation checks passed:

- game JavaScript syntax;
- smoke-wrapper and evaluated smoke-script JavaScript syntax;
- focused Node checks for participant normalization, prepared converted
  meetings, deterministic retry, transactional rollback, and burnout cleanup;
- standalone-file integrity and static playback invariants; and
- Git whitespace/error checks.

Subsequent local validation on 2026-08-07 also passed:

- four consecutive runs of the expanded browser smoke suite;
- all eight targeted advanced-interaction groups;
- the full runtime, static, disclosure, accessibility, and sampled-layout
  audit; and
- seven visual captures spanning desktop, compact desktop, landscape phone,
  portrait rotation, Morning, Workday, and Night.

See
[`SKIP_FIX_LOCAL_VALIDATION_2026-08-07.md`](../verification/SKIP_FIX_LOCAL_VALIDATION_2026-08-07.md)
for current-hash evidence and the cross-version simulation comparison.
Structural balance remains open.
