# OfficeWars Full Verification

Date: 2026-08-06

Implemented file:
`officewarsautobattler.html`

SHA-256:
`2A4880220763678436C6BDFA043EAD7777BB71F01547F8B17B047768206C1D78`

Overall result: **FAIL - not ready for ship signoff**

Post-audit update: F1-F4 were fixed and passed their focused retest. See
`BLOCKERS_1_4_RETEST_2026-08-06.md`. All eight targeted high-risk interaction
groups later passed
`ADVANCED_INTERACTION_VERIFICATION_2026-08-06.md`. F5 and the remaining
unexercised UI, accessibility, reset, and lifecycle rows keep the ship verdict
at Fail.

## Status Legend

- **Pass**: exercised or compared with sufficient evidence for this audit.
- **Fail**: verified behavior or presentation conflicts with a Locked
  requirement.
- **Not Run**: some evidence may exist, but the complete requirement was not
  exercised strongly enough to certify it.
- **Blocked**: the available environment cannot produce the required evidence.

## Findings And Remediation

### F1 - Delayed resources are not fully inspectable

Status: **Resolved - focused retest Pass**

The original candidate reported most delayed effects using only a generic name
and coarse duration. The current candidate exposes exact values, targets,
duration, expiry, reserve return, Working Capital maturity and actions, debt
due timing, and shortfall conversion in both active-effect details and the
economy tooltip.

Original measured example:

- Commission Advance chip: `Commission Advance`
- Economy tooltip: spendable cash, aggregate Overnight Reserve, aggregate
  Working Capital, aggregate debt, and estimated interest
- Originally missing: Commission Advance's 20 flat-stress consequence and exact deadline,
  reserve return day, Working Capital maturity, and debt due day

Evidence:

- `officewarsautobattler.html:7637`
- `officewarsautobattler.html:7663`
- `officewarsautobattler.html:7693`
- `.officewars-full-verify.py` check `delayed-effect-exact-trace`

### F2 - Nine task cards omit material decision information

Status: **Resolved - focused retest Pass**

The morning card is the last reversible surface before these effects begin
resolving. The original audit found the omissions below; every current card
description now includes the missing rule:

| Card | Missing disclosure |
|---|---|
| Repository Fork | Coding XP replaces normal family XP |
| Cross-Functional Sync | bonuses trigger even if already used |
| Creative Breakthrough | excess recovery still grants progress |
| Design System | the four-task source window has no rerolls |
| Client Entertainment | 8 relationship replaces the normal Outing gain |
| Comparison Shopping | alternatives come from the same catalog |
| Corporate Expense Account | unused Expense Credit expires at Lights Out |
| Net 30 Contract | shortfall converts at 1 flat stress per $25 |
| Working Capital | maturity and one Work action per reserved $500 |

All 50 progress and stress values match the Locked ledger. Thirty-three card
effects use shortened wording; the table above contains the material omissions
found by this audit.

Evidence:

- `officewarsautobattler.html:1604`
- `docs/BALANCE_LEDGER.md:719`
- `.officewars-full-verify.py` check `material-card-disclosure`

### F3 - Help does not contain the Locked resolution glossary

Status: **Resolved - focused retest Pass**

How to Play now includes concise Card Resolution and Schedule Resolution pages
covering the Locked terms required to understand card-copy and replay behavior.

Evidence:

- `officewarsautobattler.html:7980`
- `.officewars-full-verify.py` check `help-resolution-glossary`

### F4 - The desktop Day Actions overflow is not keyboard reachable

Status: **Resolved - focused retest Pass**

At 1440x900 and 1024x768, the expanded legend remains a scroll region. It is
now labelled, focusable, visibly outlined on focus, and supports Arrow,
Page Up/Down, Home, and End. An `End` key test moved its scroll position from
0 to 109 on desktop and 0 to 90 on compact desktop.

Measured:

| Viewport | Client height | Scroll height | Focusable descendants |
|---|---:|---:|---:|
| 1440x900 | 336 | 445 | 0 |
| 1024x768 | 287 | 377 | 0 |

Evidence:

- `officewarsautobattler.html:591`
- `officewarsautobattler.html:1408`
- `LAYOUT_JSON` from `.officewars-full-verify.py`

### F5 - The simulated skilled win rate misses the target

Status: **Fail**

Across 1,000 seeds, the current scripted skilled policy won 55.3 percent,
above the Locked 25-35 percent target. This is balance evidence, not a request
to retune automatically.

Regression Tests was selected 2,567 times, far more than any other card under
this policy. Treat that as a high-priority simulation watchpoint, not proof
that the card alone causes the target miss.

### Verification harness watchpoint - accessibility timing

Status: **Resolved - four consecutive smoke passes**

The harness now waits for observable overlay, modal-focus, and Morning states
instead of fixed 40 ms delays. It passed four consecutive post-fix runs.

## Tests Run

| Layer | Result | Evidence |
|---|---|---|
| Existing overhaul smoke suite | **Pass** | four consecutive `PASS:OVERHAUL` post-fix runs |
| Supplemental runtime audit | **Pass for F1-F4** | every focused assertion passed |
| Targeted advanced interaction suite | **Pass** | all eight groups and every assertion passed; no browser or runtime errors |
| All-card basic execution | **Pass** | 50/50 previewed, rendered, and resolved without exceptions |
| Responsive layout matrix | **Pass** | no viewport overflow; keyboard scrolling passed at both desktop widths |
| Package equality | **Pass** | 16 mapped root/package files byte-identical |
| Portable hash manifest | **Pass** | 19/19 package hashes matched |
| Distribution Monte Carlo | **Pass** | existing 100,000-sample rarity, family, paid-reroll, and Special checks |
| Seeded balance simulation | **Fail target** | 3,000 complete runs, no simulation errors |

## Static Integrity

| Requirement | Status | Evidence |
|---|---|---|
| One standalone game HTML | **Pass** | one HTML, one inline script, one inline style |
| No required external asset, server, or build | **Pass** | zero external asset references and zero runtime network requests |
| JavaScript parses and loads | **Pass** | Chromium load, no page errors |
| No duplicate runtime IDs | **Pass** | 71 rendered IDs, all unique |
| Literal DOM targets exist | **Pass** | two source-only dynamic targets resolve at runtime |
| CSS/JavaScript containers parse | **Pass** | browser parse; one matched script/style pair |
| Obsolete player Resume state absent | **Pass** | no live `R.resume` or old stack reward state |
| Library replacement | **Pass** | smoke coverage and centralized Home registry |
| Hackathon/Networking Brunch replacements | **Pass** | smoke/source trace |
| Chad stacks/upgrades preserved | **Pass** | runtime state and 10-upgrade cap |
| Home effects centralized | **Pass** | 15 upgrades and 15 registry entries |
| Home set hooks inert | **Pass** | zero active sets and zero tagged upgrades |
| Tooltips, forecasts, legends, Help match behavior | **Pass for F1-F4** | focused runtime and keyboard retest |

Raw source contains repeated IDs in mutually exclusive old/new render
templates. The live DOM is unique, so these are not runtime duplicate-ID
failures.

## Documentation QA

| Requirement | Status | Evidence |
|---|---|---|
| Roster is described as implemented | **Pass** | active handoff and ledger |
| Baseline and Locked status are separated | **Pass** | ledger headings |
| Draft/Open are not presented as Locked | **Pass** | no active Draft section; two Open questions |
| Root and portable mapped files match | **Pass** | 16/16 byte-identical |
| `START_HERE.md` hashes match | **Pass** | 19/19 |
| Superseded directions are archived | **Pass** | active-source search and archive index |

## Determinism And Playback

| Requirement | Status | Evidence |
|---|---|---|
| Same seed and choices reproduce a full run | **Pass** | duplicate baseline headless run |
| 1x, 2x, 4x, and Skip end identically | **Pass** | smoke state equality |
| Animation timing does not change gameplay RNG | **Pass** | speed/Skip equality and split RNG streams |
| Save/restore at every phase boundary preserves next result | **Not Run** | RNG restoration passed; full-state restoration was not exercised |

## Core Balance

| Requirement | Status | Evidence |
|---|---|---|
| 20 percent floor stress pressure | **Pass** | floor 7 base 10 became 22 |
| Recovery remains unscaled | **Pass** | floor 7 recovery 5 removed exactly 5 |
| Sleep 4, Mattress 6, Lights Out 5 | **Pass** | exact runtime values |
| Promotion recovery 25 | **Pass** | smoke transition test |
| Interest 15 percent | **Pass** | exact runtime value |
| Rank curve | **Pass** | exact seven pairs |
| Complete meeting/manager behavior matrix | **Not Run** | key rules traced; every manager/outcome combination was not executed |
| Managers do not repeat | **Pass** | 100 sampled shuffles, first seven unique |
| Deadline Hawk ordering | **Not Run** | source traced; modifier-combination matrix not executed |
| Weekend casino rules | **Pass** | source and smoke |
| Chad provisional coefficients and cap | **Pass** | exact values and 60-day cap test |
| Chad detailed forecast | **Pass** | stacks, upgrades, and range in tooltip |

## Offers, Cards, And Distribution

| Requirement group | Status | Evidence |
|---|---|---|
| Equal family weighting | **Pass** | 100,000 samples |
| 50 cards and 4/3/2/1 per family | **Pass** | runtime records |
| 70/20/9/1 ordinary rarity | **Pass** | 100,000 samples |
| Paid reroll excludes Legendary and renormalizes | **Pass** | 100,000 samples |
| Free rerolls may show Legendary | **Pass** | shared ordinary rarity path |
| 0.2 percent Special rate and one per window | **Pass** | 100,000 windows |
| Every Special eligibility/exclusion source | **Not Run** | key protection cases passed; every listed source was not executed |
| No exact duplicate in an offer; later reuse allowed | **Pass** | 10,000 windows |
| Pin merge, variants, expiration, and generated duplicates | **Not Run** | merge and selected expiration cases passed; full matrix not run |
| All 20 Commons have an effect and no extra prompt | **Pass** | data and primary-resolution audit |
| Immediate resolution and counter ordering | **Pass** | smoke resolution fixtures |
| Replay/copy/source ancestry rules | **Pass** | smoke nested-copy and Pilot fixtures |
| Repository Fork/Automation pool distinction | **Pass** | smoke fixture |
| Comparison Shopping timing | **Pass** | smoke fixture |
| Working Capital morning choice | **Pass** | card-resolution and reserve-order fixtures |
| Exact player-facing card disclosure | **Pass** | all nine missing disclosures added |

## Resolution And Transitions

| Requirement | Status | Evidence |
|---|---|---|
| Selection and Complete Play are distinct | **Pass** | smoke additional/replay fixtures |
| Project completion does not interrupt chain | **Not Run** | source traced; multi-branch completion fixture not run |
| Natural/bonus/repeat/event distinctions | **Pass** | maximal fixture used 27 tagged entries, 38 scheduled resolutions, and 61 total action-history rows |
| Schedule Desk revalidates guarantees | **Pass** | conflicting guarantees survived the maximal lock fixture |
| Opening/core/bonus/procedure/child order | **Pass** | one maximal deterministic schedule exercised the complete ordering |
| Clock Out order | **Pass** | maximal interest, pay, capital, debt, reserve, delayed-effect, Focus, and Guardian fixture |
| Result priority | **Pass** | burnout, player, Chad, deadline, final-floor fixture |
| Ordinary/completion/final transition routes | **Pass** | smoke phase-route fixture |
| Flexible Night and explicit finalization | **Pass** | runtime Night surface and route fixture |

## Coworkers, Traits, And Advanced Systems

The targeted deterministic advanced suite passed:

- Coworker Standard/Forced opportunity ordering;
- repeated-meeting activation overlap and strength multiplication, including
  stress drawbacks;
- opening contribution and visit order;
- staged Promotion Claim Batches and simultaneous capstones;
- targeted timing assertions for all 14 ordinary paths, including Codebase,
  Polish, Velocity, Focus, Reserve, stored-card, Contact, and Closing state;
- Schmoozing Assist restrictions;
- Deal purchase and carryover behavior;
- complete Sales Cycle and Enterprise Close execution;
- all four Brand Strategy Campaign completions; and
- Efficiency, Logistics, and Compound Interest path behavior.

This behavioral pass does not promote the separate exhaustive per-card,
per-reward, or responsive UI trace rows below.

## Per-Card Traceability

Every card passed a basic final-preview, semantic-markup, and primary-resolution
test. That does not certify every delayed trigger, edge case, or visible
expiration.

**Pass** for the original material morning-disclosure finding:

- Repository Fork
- Cross-Functional Sync
- Creative Breakthrough
- Design System
- Client Entertainment
- Comparison Shopping
- Corporate Expense Account
- Net 30 Contract
- Working Capital

**Not Run** for the complete behavior-plus-UI row for all 50 cards:

- README Update, Regression Tests, Bug Triage, Production Hotfix
- Version Control, Build Script, API Integration, Parallel Processing,
  Repository Fork, Hackathon
- One-on-One, Meeting Minutes, Action Plan, Capacity Planning, Meeting Prep,
  Staff Check-In, Schedule Adjustment, Cross-Functional Sync, Executive Review,
  War Room
- Iteration Pass, Reference Study, Accessibility Review, White Space,
  Prototype Test, Concept Selection, User Testing, Creative Breakthrough,
  Rapid Prototype, Design System
- Expense Allowance, Referral Fee, Sales Quota, Cross-Sell,
  Client Entertainment, Comparison Shopping, Commission Advance,
  Corporate Expense Account, Referral Network, Net 30 Contract
- Process Audit, Preventive Maintenance, Priority Requisition,
  Overnight Reserve, Contingency Plan, Shift Handoff, Accrual Accounting,
  Working Capital, Failover Protocol, Perfect Execution

## Trait, Deal, And Reward UI Rows

All trait-path UI rows are **Not Run** for exhaustive exact-value,
armed-state, resolution, and expiration coverage:

- Clean Code, Automation, Debugging
- Delegation, Agile, Leadership
- Eye for Detail, Moodboard, Brand Strategy
- Negotiation, Schmoozing, Closing
- Efficiency, Logistics, Compound Interest
- Rebrand Initiative, Campaign tasks, Sales Cycle cards, Close

All Deal and Closing-reward UI rows are **Not Run** for exhaustive end-to-end
coverage. This includes all eight standard Deals, Scope Renegotiation, all
Nurturing/Qualifying/Presenting/Enterprise rewards, Anchor Account, and
Enterprise Dividend. Selected Closing behaviors passed smoke tests, but not
their complete player-facing row.

## Resource And Phase Surfaces

| Surface | Status | Evidence |
|---|---|---|
| Morning Task Desk | **Not Run** | basic ordinary, Campaign, and Closing surfaces pass; every advanced mode not run |
| Schedule Desk | **Pass for maximal ordering** | 27-entry conflict fixture passed; every picker presentation remains unverified |
| Workday playback | **Not Run** | deterministic playback passes; every source/activation badge not run |
| Clock Out summary | **Pass for maximal behavior** | complete economy fixture passed; every visual combination remains unverified |
| Night Desk | **Not Run** | basic Home surface passes; all combined resources not run |
| Weekend | **Not Run** | route and recovery cases pass; all pickers/states not run |
| Promotion Review | **Pass for batch behavior** | staged five-path and simultaneous-capstone fixtures passed; complete batch UI remains unverified |
| Resume rail and Book | **Not Run** | basic five-family rendering passes; every named counter not run |
| Coworker views | **Not Run** | exact packages in every picker not run |
| Economy breakdown | **Pass for F1** | exact itemized values and timing in focused retest |
| Active-effect strip | **Pass for F1** | exact delayed-effect details in focused retest |
| Logs and Help | **Pass for F3** | resolution glossary present; source-attribution coverage remains Not Run |

## UI And Office

| Requirement group | Status | Evidence |
|---|---|---|
| Persistent HUD layout | **Pass** | desktop, compact, and landscape captures |
| Portrait rotation gate | **Pass** | 390x844 |
| Landscape phone gameplay | **Pass** | 844x390 morning/workday/night |
| No viewport overflow | **Pass** | ten state/viewport cases |
| Decision text never clips | **Not Run** | sampled states pass; every advanced picker not reached |
| AFK playback has no unavoidable choice | **Pass** | headless and timed workday completion |
| No named delayed-resource state is hidden | **Pass for F1** | active-effect and economy detail retest |
| Manager/Today hover and keyboard tooltip | **Pass** | runtime focus test |
| Spendable cash prominent | **Pass** | visual matrix |
| Complete economy details | **Pass for F1** | reserve, capital, debt, credit, and interest details exposed |
| Read-only Home inventory | **Pass** | modal/focus test |
| Resume rail and XP segments | **Pass** | visual matrix |
| Closing Deal Ladder | **Not Run** | state exists; full responsive trace not captured |
| Workday-only Help/speed/Skip | **Pass** | semantic controls and visual matrix |
| Active-effect strip | **Pass for F1** | exact values and timing exposed on focus/hover |
| Chad forecast | **Pass** | exact tooltip content |
| Eight cubicles and water cooler | **Pass** | 8 and 1 |
| Conversation adjacency and meeting waits | **Not Run** | not stress-tested |
| Reduced motion | **Not Run** | CSS rule exists; full motion behavior not observed |

## Boundary, Failure, And Lifecycle

| Requirement group | Status | Evidence |
|---|---|---|
| Every listed exact threshold | **Not Run** | several priority/Chain thresholds passed; full list not run |
| Every empty/restricted target pool | **Not Run** | selected copy/comparison cases passed |
| No double-spend across all money forms | **Not Run** | no comprehensive combined-economy fixture |
| Every simultaneous atomic boundary | **Not Run** | result priority and selected copy/replay cases passed |
| Effect identity/duration across all transitions | **Not Run** | selected expiry cases passed |
| Completion Night and final-floor route | **Pass** | smoke route fixture |
| New-run reset after every ending | **Not Run** | simulation resets runs; UI timer/listener reset not measured |
| Rapid inputs and double clicks | **Not Run** | resolution lock passed; all controls not fuzzed |
| Worst-case long chains and memory | **Pass for termination** | 16-play replay, 15-play stored-card, and 121-resolution action chains terminated; memory growth was not profiled |

## Accessibility

| Requirement | Status | Evidence |
|---|---|---|
| Basic semantic controls and names | **Pass** | all rendered buttons named in sampled states |
| Every modal/picker focus cycle | **Not Run** | overlay and Home inventory passed; every picker not run |
| Hover details available by focus/tap | **Not Run** | Manager and sampled chips pass; every detail not run |
| Color is never the only signal | **Not Run** | not exhaustively audited |
| Contrast in every state | **Not Run** | no formal contrast calculation |
| Dynamic announcements in assistive technology | **Blocked** | no screen-reader execution available |
| Zoom/text scaling | **Not Run** | responsive viewports tested, browser zoom was not |
| Keyboard access to Day Actions overflow | **Pass** | focus plus behavioral End-key scroll test |

## Browser Matrix

| Matrix item | Status | Evidence |
|---|---|---|
| 1440x900 | **Pass** | Morning, Workday, Night |
| 1024x768 | **Pass** | Morning, Workday, Night |
| 844x390 landscape phone | **Pass** | Morning, Workday, Night |
| 390x844 portrait phone | **Pass** | rotation gate |
| Keyboard-only completion | **Not Run** | sampled focus paths and Day Actions scrolling pass; complete run not executed |
| Hover/focus/tap for every tooltip | **Not Run** | sampled paths only |
| Every advanced decision surface at every viewport | **Not Run** | ordinary surfaces only |

## Simulation Report

Simulation game hash:
`092A58350132C43736C24E36DBAE28EFFC63FCC4511C037433822E5637EBAA4B`

The F1-F4 remediation changed player-facing text, Help, accessibility handling,
and verification timing, but no balance or gameplay values. The prior
simulation remains the current F5 evidence.

Seed ranges:

- Baseline: 910000-910999
- Random: 1010000-1010999
- Skilled: 1110000-1110999

| Policy | Runs | Win rate | Burnout | Rival | Fired | Avg floor | Avg days | Median final stress |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Baseline | 1,000 | 0.7% | 978 | 9 | 6 | 2.40 | 13.55 | 100 |
| Random | 1,000 | 12.2% | 325 | 431 | 122 | 3.66 | 22.39 | 44.6 |
| Skilled | 1,000 | 55.3% | 206 | 183 | 58 | 5.59 | 27.14 | 31.8 |

Skilled top selections:

| Card | Picks |
|---|---:|
| Regression Tests | 2,567 |
| Reference Study | 1,513 |
| README Update | 1,299 |
| Iteration Pass | 1,216 |
| Overnight Reserve | 918 |

End-to-end observed offer rates:

| Policy | Legendary | Special |
|---|---:|---:|
| Baseline | 1.041% | 0.224% |
| Random | 0.911% | 0.192% |
| Skilled | 0.892% | 0.172% |

The end-to-end denominators include Sales Cycle and Campaign slots that are not
ordinary eligible random slots, so these rates are descriptive rather than the
distribution acceptance test. The dedicated 100,000-sample generators passed
the exact 70/20/9/1, paid-reroll, equal-family, and 0.2 percent Special checks.

Model limitations:

- The skilled policy is a deterministic heuristic, not a human expert model.
- It cannot model every information, schedule, or long-horizon choice.
- It auto-resolves many secondary choices with fixed priorities.
- Pick-rate outliers are evidence for targeted simulation, not automatic
  balance changes.

## Ship Decision

Do not tune or ship from this candidate yet.

Recommended order:

1. Define and run the structural balance matrix, starting with the
   skilled-policy target miss, Regression Tests selection pressure, and the
   121-resolution action-inflation fixture.
2. Apply only explicitly approved balance changes.
3. Re-run full verification, including the remaining UI, accessibility,
   save/restore, reset, and lifecycle rows before ship signoff.
