# OfficeWars Full Verification

Date: 2026-09-21

Candidate:

- SHA-256:
  `8BB0FB12B34D6058EB505B0404A4AE33380F9097CCBBCD6E804C9CE3D8214A07`
- Size: `1,212,152` bytes
- Active-run schema: 9
- Tutorial-meta schema: 6

## Verdict

| Gate | Verdict |
|---|---|
| Phase 1-5 regression stability | Pass |
| Home Phase 1 runtime and UI stability | Pass |
| Deterministic Workday and persistence | Pass |
| Desktop and short-landscape usability | Pass |
| Current documentation status boundary | Pass |
| 100-seed legality execution | Pass |
| Exhaustive per-item and per-set effect matrix | Not Run |
| 1,000 paired-seed Draft tuning | Not Run |
| Formal screen-reader execution | Not Run |
| Broad human playtest | Not Run |
| Home Phase 1 implementation readiness | Pass |
| Balance readiness | Not Ready |
| Release readiness | Not Ready |

## Implemented Boundary

The current candidate implements:

- Workday and Office Politics Phases 1-5;
- seven Homes;
- 28 available Home items plus a gated Cash Jar definition;
- nine active sets and Connected upgrades;
- Morning salary and Accounted Cash ordering;
- Home deposits, moves, catalog generation, rerolls, purchases, held items,
  Cash-basis sales, mastery, and restoration;
- Home Setup, Prepare Tomorrow, Active Buffs, Automated Task Resolution,
  Remote Task, Planning, and direct social integrations; and
- schema-9 invalidation of incompatible active runs while preserving settings,
  profile, orientation, and Guided Intern metadata.

Cash Jar acquisition and 24 outcomes, Galactic acquisition/events, and Guided
Intern remain unimplemented.

## Automated Evidence

| Suite | Result |
|---|---|
| Phase 1 | Pass, 25/25 |
| Phase 2 | Pass, 20/20 |
| Phase 3 | Pass, 21/21 |
| Cinematic Workday | Pass, 32/32 |
| Today’s Directive | Pass, 13/13 |
| Phase 4 | Pass |
| Phase 4 dependency repair | Pass |
| Phase 5 | Pass |
| Home Phase 1 | Pass, 15/15 |
| Home/schedule | Pass |
| Night Planner | Pass |
| Task keywords/celestial direction | Pass |
| Smoke | Pass |
| Persistence/tutorial | Pass |
| Advanced interactions | Pass |
| Full static/browser audit, simulations disabled | Pass |

The directive suite proves that the Night result banner clears before Morning,
the announcement is centered, and manager tooltips contain only Success and
Failure. The Home suites prove seven-Home layout, three-offer catalog
generation, keyword focus/touch/Escape access, Active Buffs, 200-percent text,
and short-landscape Planner readability.

## Simulation Evidence

The legality diagnostic ran 100 fixed seeds, `1110000-1110099`:

- wins: 0;
- Chad losses: 64;
- burnouts: 35; and
- firings: 1.

No browser or console errors occurred. This is legality evidence only. The
policy’s Home purchase, set-building, and long-horizon economy quality has not
been independently validated, so the result cannot authorize tuning.

## Not Run

- one forced behavioral fixture for every one of the 28 available items;
- one forced completion and Connected-upgrade fixture for every set;
- every sale, exhaustion, reacquisition, financing, and empty-pool
  combination;
- 1,000 paired seeds for Draft salary/deposit/rarity values;
- formal screen-reader execution;
- broad human playtests; and
- Cash Jar, Galactic acquisition/events, and Guided Intern runtime.

## Decision

Home Phase 1 is implementation-ready for continued internal development.
OfficeWars is not release-ready and its Draft Home economy is not
balance-ready. The next highest-value verification work is the exhaustive
item/set fixture matrix, followed by a policy-legality audit before the
1,000-seed tuning run.
