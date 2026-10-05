# Guided Intern Implementation Verification

Date: 2026-09-22

## Candidate

- Root HTML SHA-256:
  `CB371A89CA31F783BB103E3055B67E10936E2DDAEE6B953CD49CEEA9537CCA95`
- Size: `1,571,059` bytes
- Active-run schema: 9
- Tutorial-meta schema: 6
- Cash Jar public gate: disabled
- Cash Jar target schema 10: inactive
- Public mirror: intentionally unchanged at `360CC6C0...`
- Release ZIP: not built

## Implemented Scope

Guided Intern replaces the original thirteen-step Orientation as the sole
first-play tutorial. It is mandatory once per profile, uses a fixed
Wednesday-Friday Intern floor, contains exactly 18 Coordinator checkpoints,
and carries real results into Associate.

Verified authored journey:

| Boundary | Player | Chad | Other exact state |
|---|---:|---:|---|
| Wednesday Clock Out | 18/45 | 15/45 | Coding XP 1, Approval 3, Overtime 1 |
| Thursday Clock Out | 28/45 | 26/45 | Coding XP 2, Priya Opening |
| Friday Clock Out | 52/45 | 36/45 | Coding XP 3, Approval 3, one Overdelivery tier, $662 before payout |
| Associate Floor Intro | carried | carried | $762, Curtains, $50 equity, one expectation tier, Priya Alumni, +1 reputation |

The real authorities resolve Bug Triage/Comply/Safe, Regression
Tests/Negotiate/Balanced, Production Hotfix/Resist/Risky, the Role Vote,
Priya's Opening and Rapport, Home purchase, Lights Out, payout, deposit,
Weekend, Promotion Review, Alumni, expectations, and manager reputation.

Clean Code, Automation, and Debugging are shown individually. The player
cannot select until all three have been viewed, then chooses freely.

## Defects Found And Repaired

1. Guided Office Chat settlement did not always append action history after
   the Phase 4 wrapper, so Thursday and Friday directives could miss their
   objective. The final Guided action wrapper now records the resolved Chat
   exactly once.
2. Guided Chad pace inherited ordinary supporter modifiers, producing decimal
   gains instead of the authored 15/day. Guided pace now uses the exact fixed
   authority breakdown.
3. Reloading the Coding path walkthrough restored its visible card but lost
   the pending promotion continuation. `owContinueRun` now re-enters Promotion
   Review for a restored Guided path lesson while preserving the review index.
4. Headless graduation could mark the profile complete while the last saved
   checkpoint remained at Weekend Result. Associate `floorIntro` is now saved
   first, including in headless verification, and profile completion is
   committed only after that save succeeds.
5. Shared verifiers still depended on deleted Orientation DOM/functions. They
   now assert Guided Intern routing, replay, migration compatibility, and
   persistence.

## Focused Verification

`.officewars-guided-intern-verify.py`: **Pass 29/29**

Coverage includes:

- exact 18 stable lesson IDs and visit order;
- fixed tasks, directives, stances, schedules, participants, political
  choices, invitations, Home offer, Weekend, and carryover;
- no Coordinator entry in ordinary manager pools;
- exact project, Chad, Cash, XP, Approval, Relationship, loyalty, Alumni,
  equity, expectation, and reputation traces;
- one ordinary New Run after completion and intentional fresh Guided replay;
- original Orientation CSS/DOM/data/functions/test API removal;
- watched 1x, 2x, 4x, Skip, and headless exact Associate-state parity;
- wrong task/reroll/political actions and Repeat/Show Me/Why consuming no
  gameplay or gameplay RNG;
- mid-path reload and pre-review selection rejection;
- existing ordinary active-save compatibility for an incomplete profile;
- recoverable Associate checkpoint before profile completion;
- no Coordinator interruption of first Associate Morning;
- all 18 lesson identities surviving reload;
- keyboard tab order, accessible region name/description/live status;
- reduced motion, desktop, compact, short landscape, and 200% text; and
- no page or console errors.

## Regression Matrix

| Suite | Result |
|---|---|
| Phase 1 | Pass 25/25 |
| Phase 2 | Pass 20/20 |
| Phase 3 | Pass 21/21 |
| Phase 4 | Pass 18/18 |
| Phase 4 repair | Pass 15/15 |
| Phase 5 | Pass 21/21 |
| Home Phase 1 | Pass 15/15 |
| Home schedule | Pass |
| Home item/set matrix | Pass: 28 items, 9 sets, 2 lifecycle cases |
| Night Planner | Pass |
| Today's Directive | Pass 13/13 |
| Task keywords | Pass |
| Cinematic Workday | Pass 32/32 |
| Persistence and Guided replay | Pass 30/30 |
| Advanced systems/collision chains | Pass |
| Cash Jar inventory | Pass 6/6, 96/96 handlers |
| Cash Jar release | Pass 10/10 |
| Cash Jar Reality | Pass 15/15 |
| Full audit and responsive matrix | Pass |
| Full simulation execution | Pass: 750/750 complete, zero runtime errors |
| Smoke | Pass |

The simulation remains an execution-integrity instrument, not balance proof:
baseline, random, and current skilled policies each produced 0 wins in this
250-seed-per-policy run. No tuning was performed.

## Remaining Evidence Gaps

- No formal assistive-technology screen-reader session was run.
- No current-hash human first-session Guided Intern playtest was run.
- Existing automated strategy policies do not establish the 25-35% skilled
  win-rate target or high-tier Cash Jar balance.
- Public mirror synchronization and packaging remain intentionally out of
  scope.

## Verdict

Guided Intern implementation: **Pass**

The replacement tutorial is implemented, deterministic, persistent,
accessible under automated checks, compatible with ordinary saves, and clean
against the requested gameplay regression matrix. No user design decision is
required to finish this implementation.
