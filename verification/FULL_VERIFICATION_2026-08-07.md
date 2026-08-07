# OfficeWars Full Verification

Date: 2026-08-07

Implemented file: `officewarsautobattler.html`

Game SHA-256:
`39052BC75E47EBFDE18C858F29D0731C31582F5C22ECC7134B2F5B83A90B0CAD`

Overall result: **FAIL - readability passes, final balance release does not**

The readability overhaul is complete and passes its final browser matrix.
The complete game remains below final release signoff because the
scripted-skilled policy wins 58.4 percent against the approved 25-35 percent
target. Exhaustive assistive-technology, every-picker, save/restore, reset,
rapid-input, and memory-profile rows also remain explicitly unverified.

## Verification Artifacts

| Artifact | SHA-256 |
|---|---|
| `.officewars-smoke.html` | `87A23BB17EEA6BE86AC436E3E490DB50E02950DDB28404B5E5F9AF9E375C6459` |
| `.officewars-smoke-run.py` | `D39D9CE23CC13196D08B6ECAB4DAABF2E1F70299FB776337E0D931E92224925E` |
| `.officewars-advanced-verify.py` | `6A71969B1C6B562E6F462922BF13A745919874161BEDF17462B84C930AEC2295` |
| `.officewars-full-verify.py` | `58BA34367E8A6CCCC8638FB7C45E8F4D6A98BB0066F9DC8613E1BFE793B7EADA` |
| `.officewars-visual-capture.py` | `8956255966B96982D489C5A5613612FBCB5D4D055E09E388FE13F038BDE6ED57` |
| `.officewars-skilled-telemetry.py` | `62378F333A4E783BB52DE6011DAF64F8F6FDCA2FD3267CEC680A82C8BBCCD8C2` |

## Summary Matrix

| Requirement group | Status | Evidence |
|---|---|---|
| Standalone HTML, syntax, IDs, and runtime loading | **Pass** | Full verifier; no page, console, or external-request errors |
| Core balance constants and seven-floor curve | **Pass** | Full verifier exact-value assertions |
| 50-card roster and 4/3/2/1 family distribution | **Pass** | Full verifier, all 50 unique IDs |
| Ordinary rarity, Special, and family distribution | **Pass** | Dedicated generator checks and 3,000-run offer telemetry |
| All 50 cards: preview, markup, and primary resolution | **Pass** | Full verifier; zero preview, markup, or play failures |
| All 50 cards: every delayed edge and UI expiration | **Not Run** | Basic and targeted coverage passed; exhaustive per-card lifecycle matrix was not executed |
| Shared card, replay, copy, and resolution rules | **Pass** | Smoke and advanced worst-case fixtures |
| Schedule, action, Clock Out, and transition ordering | **Pass** | Advanced maximal schedule/economy fixtures |
| Coworker Standard and Forced activation ordering | **Pass** | Advanced coworker and repeated-meeting fixtures |
| All 14 ordinary trait paths | **Pass** | Advanced targeted timing fixture |
| Closing, Brand Strategy, Deals, Schmoozing, and Logistics | **Pass** | Advanced lifecycle fixture |
| Promotion batches and single-capstone ownership | **Pass** | Advanced simultaneous-candidate fixtures |
| Deterministic 1x, 2x, 4x, and Skip playback | **Pass** | Four consecutive overhaul smoke passes |
| Readability overhaul | **Pass** | Thirteen-case visual and layout matrix plus human screenshot inspection |
| Morning task hierarchy and compact comparison | **Pass** | Desktop, compact, landscape, and 200-percent text cases |
| Resume rail and Resume Book | **Pass** | Five tabs, XP track, scalable flavor, keyboard tab movement |
| Resolved Workday feedback | **Pass** | Real resolved-action captures at desktop and landscape sizes |
| Clock Out grouping and source log | **Pass** | Desktop and landscape captures |
| Night navigation, Lights Out, and one final action | **Pass** | Desktop and landscape captures plus toggle state assertion |
| Portrait rotation gate | **Pass** | 390 x 844 capture |
| Persistent HUD overlap and viewport overflow | **Pass** | No failures in all sampled viewports and phases |
| Basic semantic names, focus return, and keyboard tooltip | **Pass** | Full verifier |
| Every modal and picker focus cycle | **Not Run** | Resume, inventory, and sampled surfaces passed; every advanced picker was not traversed |
| Color independence and formal contrast in every state | **Not Run** | Human visual review only; no exhaustive contrast calculation |
| Dynamic screen-reader announcements | **Blocked** | No screen-reader execution environment |
| Keyboard-only complete run | **Not Run** | Sampled controls passed; a complete run was not executed keyboard-only |
| Every advanced decision surface at every viewport | **Not Run** | Ordinary phases and representative exceptional modes passed |
| Save/restore at every phase boundary | **Not Run** | Deterministic snapshots are present; exhaustive restoration matrix was not executed |
| New-run reset after every ending | **Not Run** | Simulation resets pass; UI timer/listener reset after all four endings was not exhaustively measured |
| Rapid-input and double-click fuzzing for every control | **Not Run** | Resolution locks and repeated Skip passed; every control was not fuzzed |
| Worst-case chain termination | **Pass** | 16-play replay, 15-play storage, and 121-action fixtures terminate |
| Worst-case memory growth | **Not Run** | Termination passed; heap growth was not profiled |
| Public and portable distribution integrity | **Pass** | Post-cleanup hash equality and local-link checks |
| Structural skilled win-rate target | **Fail** | Scripted-skilled 58.4 percent versus 25-35 percent target |
| Human balance evidence | **Not Run** | Human playtesting remains pending |
| Deferred Home set design | **Not Run** | Intentionally outside this update; inert metadata only |

## Readability Matrix

The expanded visual runner passed all thirteen cases:

- desktop, compact desktop, and landscape-phone Morning;
- portrait-phone rotation;
- desktop and landscape Resume Book;
- desktop and landscape Workday after a real action resolved;
- desktop and landscape Clock Out;
- desktop and landscape Night; and
- desktop Morning at 200 percent root text size.

Assertions cover viewport overflow, persistent-HUD overlap, clipped text,
horizontal modal overflow, task family hierarchy, removal of routine XP copy,
Resume structure and keyboard tab behavior, Workday result feedback, Clock
Out grouping, Night finalization, and Lights Out state.

Human inspection found no incoherent overlap or unreadable primary decision
surface in the generated screenshots. Advanced pickers not reached by this
matrix retain **Not Run** status.

## Behavioral And Edge-Case Evidence

Four consecutive `.officewars-smoke-run.py` executions returned
`PASS:OVERHAUL`.

All eight advanced groups passed:

1. maximal schedule conflicts and ordering;
2. Clock Out economy and debt;
3. Standard and Forced coworker ordering;
4. repeated meetings, multipliers, and stress drawbacks;
5. Promotion Claim Batches and simultaneous capstones;
6. timing for all 14 ordinary trait paths;
7. advanced-system lifecycles; and
8. worst-case replay, copy, storage, and action chains.

The maximal fixture still resolves 121 actions for 2,403 project progress.
It is finite and rules-correct, so it is not an implementation failure. It
remains a serious balance and readability watchpoint.

## Simulation

Seed ranges and policies match the prior current-candidate comparison.
All 3,000 runs completed without errors.

| Policy | Runs | Win rate | Primary failures |
|---|---:|---:|---|
| Baseline | 1,000 | 0.7% | 968 burnout, 14 deadline, 11 rival |
| Random | 1,000 | 12.2% | 361 burnout, 136 deadline, 381 rival |
| Scripted-skilled | 1,000 | 58.4% | 179 burnout, 60 deadline, 177 rival |

The results exactly reproduce the pre-readability candidate. This is evidence
that the UI update did not alter sampled gameplay behavior. It is also the
current release blocker: 58.4 percent is substantially above the approved
25-35 percent skilled target. `Regression Tests` remains the skilled policy's
largest selection outlier at 3,160 selections.

## Ship Decision

- **Readability update:** Pass. No further UI feature is required by the
  approved readability scope.
- **Implementation candidate:** Pass for the automated static, behavioral,
  deterministic, sampled accessibility, and sampled responsive suites.
- **Final balance release:** Fail until structural tuning is approved and the
  skilled result is brought into the target range.
- **Exhaustive certification:** Incomplete. Every row listed above as
  **Not Run** or **Blocked** remains unverified and must not be implied to pass.

The next design gate is human playtest evidence followed by explicit structural
balance decisions. Gameplay tuning still requires separate approval.
