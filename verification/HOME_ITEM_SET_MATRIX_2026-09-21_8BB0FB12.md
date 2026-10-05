# OfficeWars Home Item And Set Verification Matrix

Date: 2026-09-21

Candidate SHA-256:
`8BB0FB12B34D6058EB505B0404A4AE33380F9097CCBBCD6E804C9CE3D8214A07`

## Summary

| Inventory | Pass | Fail |
|---|---:|---:|
| Available items | 26 | 2 |
| Sets | 9 | 0 |
| Shared lifecycle checks | 2 | 0 |
| Total | 37 | 2 |

No page or console errors occurred.

## Item Matrix

| Item | Verdict |
|---|---|
| Questionably Acquired Coffee Maker | Pass |
| Blackout Curtains | Pass |
| Neglected Houseplant | Pass |
| Standing Desk | Pass |
| Emergency Snack Drawer | Pass |
| Router With One Good Antenna | Pass |
| Receipts Shoebox | Pass |
| Wall of Sticky Notes | **Fail** |
| Folding Dining Table | Pass |
| Notebook Marked "NOT WORK" | Pass |
| Comfy Mattress | Pass |
| Ergonomic Chair | Pass |
| Savings Account | Pass |
| Game Console | Pass |
| Robot Vacuum | **Fail** |
| Guest Towels | Pass |
| Framed Conference Badge | Pass |
| Second Monitor | Pass |
| Cloud Workstation | Pass |
| Library | Pass |
| Home Gym | Pass |
| Jacuzzi | Pass |
| Business Card Corkboard | Pass |
| Home Office | Pass |
| Personal Assistant | Pass |
| Espresso Machine | Pass |
| Guest Suite | Pass |
| Smart Home Hub | Pass |

### Confirmed Defects

`Wall of Sticky Notes`

- Expected: replace one generated task and consume one charge.
- Actual: activation returns `false`; the task and three charges remain.
- Cause: the public wrapper calls the overwritten global
  `owUseStickyNotes` binding from inside itself. The nested resolution lock
  rejects the recursive call.

`Robot Vacuum`

- Expected: while owned, the first Home purchase each Night recovers 4 Stress.
- Actual: purchasing another Home item recovers 0 Stress.
- Cause: the purchase handler checks whether the purchased item is
  `robotVacuum`, rather than whether Robot Vacuum is active and this is the
  first Home purchase.

## Set Matrix

| Set | Verdict | Evidence |
|---|---|---|
| Energy | Pass | One extra non-Lunch entry |
| Financial Foundation | Pass | 50% equity; Connected 75% |
| Appliance Suite | Pass | Two Home purchases |
| Wellness | Pass | Cap 5; Connected uses higher cap |
| Hospitality | Pass | Invitation pool; Connected full roster |
| Networking | Pass | +5 standing; Connected +8 |
| Connected Home | Pass | Completed-set upgrade authority active |
| Workspace | Pass | +3 PP/-1 Stress; Connected -2 Stress |
| Planning | Pass | Two offers/one choice; super six offers/two choices |

## Lifecycle Matrix

| Lifecycle | Verdict |
|---|---|
| Held item activates after a sale frees capacity | Pass |
| Authored lifetime mastery survives sale and reacquisition | Pass |

## Verdict

Home Phase 1 does not pass the exhaustive item gate while the two failed items
remain active requirements. The nine-set gate passes.
