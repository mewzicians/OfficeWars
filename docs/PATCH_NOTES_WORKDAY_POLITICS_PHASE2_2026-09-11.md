# Workday And Office Politics Phase 2

Date: 2026-09-11

Implemented game SHA-256:
`C6B66C4267AE8B2491A8B997F2877E6F92CEE8C30B06A27C229B067FD0F1E38D`

Phase 2 implements the persistence and restoration foundation required by the
approved Office Politics overhaul. It does not add the actual manager,
project, relationship, or boss politics pages reserved for Phase 3.

## Player-Facing Changes

- Every visual Workday and Skip now stops at Politics Review before Clock Out.
- The current Review is an explicit zero-page bridge. It shows the locked
  office story, resource summary, page count, Next Incomplete, and Continue to
  Clock Out without selecting or spending anything automatically.
- Restoring a prepared Workday resolves its locked playback headlessly and
  stops at the same Review bridge.
- Incompatible or corrupt active runs are cleared with a visible menu notice.
  Profile settings remain intact.
- How to Play now explains the Review boundary and its Phase 2 status.

## Persistence And Transaction Changes

- Active-run schema is 3.
- Tutorial-meta schema is 6 and records that Guided Intern must run once for
  the profile when Phase 6 supplies that scenario.
- Review state serializes stable page and choice IDs, resource and target
  reservations, reroll ownership, frozen confirmation data, results, focus,
  revisions, and settlement IDs.
- Review confirmation freezes the transaction. Manager pages settle first,
  followed by timeline order.
- Cash, Favors, and political charges use exactly-once settlement guards.
- Stable checkpoints now include Review staging, confirmed, and settled;
  role vote; pending Night directive; Floor Briefing; and tutorial lesson.
- Overdelivery payout and current Night finalization now share the settlement
  ledger's exactly-once protection.

## Verification

Focused Phase 2 verification passes 20/20. Phase 1 regression passes 25/25.
Smoke, persistence/tutorial 25/25, advanced interactions, task-keyword/Help,
and the no-simulation full static/browser/layout audit also pass.

Balance simulation, formal assistive-technology execution, and human
playtesting were not run because Phase 2 changes persistence and phase routing
without adding the later political decision content.
