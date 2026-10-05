# Boss A Kernel A Static Repair

Date: 2026-08-25

## Symptom

Human listening selected Kernel A for its energy and reported recurring static,
including during loops.

## Reproduction And Root Cause

The selected page retained the known stacked catch-up scheduler. A delayed
main-thread tick schedules every overdue step; late voices then clamp to the
same near-future start time.

Forced `900 ms` stall:

- Control: `5` steps scheduled in one tick, `0` recoveries, about `668 ms`
  maximum lag.
- Repair: `4` overdue steps skipped, `1` recovery, maximum `1` scheduled step
  per tick.

Normal headless loops produced no overdue calls, so user-device confirmation
remains required. The page already retains windowed-noise percussion.

## Repair Contract

`OW-MUSIC-BOSS-A-KERNEL-A-STATIC-REPAIR` is now `Rejected` at
`Music Legacy/officewars-boss-a-kernel-a-static-repair.html`, retained as the only
remaining stacked-scheduler control and as the byte-pinned melody source for the
Approved ensemble baseline.

Control and Repair preserve exact selected Kernel A:

- notes and melody reduction;
- harmony, bass and chord events;
- intensity and role ownership;
- current palette and windowed percussion;
- length and every monitor.

Only scheduler recovery changes.

## Verification

- Page SHA-256 as verified during the repair round:
  `1391A5281507AC596BB27A194E9B2CFE313F4481BBF4BD9FE31777ACDA09ECD7`
- Page SHA-256 now, after the status-only retag from `Test` to `Rejected`:
  `9D9CB51BA6237C947D9C7016C8BA57BFB2A2B3DFE6295EA43183CA79F22FEB8E`
- Browser verification: `84 passed, 0 failed`.
- Full Control/Repair RMS differs by approximately `0.03 dB`.
- All five monitors complete two loops for both versions.
- Repair passes forced-stall recovery, 60-second playback, pause/resume, seek,
  switching, headroom, bounded sources, cleanup, replay, themes, and console
  checks.
- Game and Approved rollback hashes remain unchanged.

Technical verification establishes scheduler recovery only.

## Listening Outcome

Human listening on the user's own playback system confirmed the recurring static
is gone. Resilient overdue-step skipping is settled for Boss A, and stacked
catch-up scheduling must not be restored.

Automated playback did not and could not establish this. The forced-stall evidence
above showed the mechanism; only the user's listening closed the question.

The page was then retagged from `Test` to `Rejected` on three surfaces: the header
chip, the footer chip, and the `selectionInfo()` lifecycle field. The retag script
reverses its own substitutions and requires the result to equal the original bytes,
which proves no musical, palette, scheduler, or layout byte moved. Verifier hash
pins were updated to the post-retag bytes; both hashes are recorded above.
