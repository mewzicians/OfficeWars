# OfficeWars Current Handoff

Last updated: 2026-08-11

## Read First

1. `AGENTS.md`
2. `docs/GAME_DESIGN.md`
3. `docs/BALANCE_LEDGER.md`
4. `docs/PROJECT_STATUS.md`
5. This file
6. `docs/PATCH_NOTES_SKIP_FIX_2026-08-06.md`
7. `verification/PERSISTENCE_TUTORIAL_2026-08-07.md`
8. `verification/PROJECT_HUD_CONSOLIDATION_2026-08-07.md`
9. `verification/WORKDAY_TICKER_SYNC_2026-08-07.md`
10. `docs/PATCH_NOTES_RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md`
11. `verification/RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md`
12. `verification/FULL_VERIFICATION_2026-08-07_30214B7F.md`
13. `docs/PATCH_NOTES_NIGHT_RESUME_AUTOMATION_UI_2026-08-10.md`
14. `verification/NIGHT_RESUME_AUTOMATION_UI_2026-08-10.md`
15. `docs/PATCH_NOTES_TASK_PICKERS_TUTORIAL_2026-08-10.md`
16. `verification/FULL_VERIFICATION_2026-08-10_55D9A6ED.md`
17. `docs/PATCH_NOTES_OPTIONS_NIGHT_POLICY_2026-08-10.md`
18. `verification/OPTIONS_NIGHT_POLICY_2026-08-10.md`
19. `docs/PATCH_NOTES_RESUME_SKILL_ART_2026-08-10.md`
20. `verification/RESUME_SKILL_ART_2026-08-10.md`
21. `docs/PATCH_NOTES_BUILD_CONTEXT_PINS_2026-08-10.md`
22. `verification/BUILD_CONTEXT_PINS_2026-08-10.md`
23. `docs/PATCH_NOTES_HOME_SCHEDULE_TUTORIAL_2026-08-10.md`
24. `verification/HOME_SCHEDULE_TUTORIAL_2026-08-10.md`
25. `verification/FULL_VERIFICATION_2026-08-10_0A8F74E5.md`
26. `docs/PATCH_NOTES_HOME_MANAGER_VISUAL_PASS_2026-08-10.md`
27. `verification/HOME_MANAGER_VISUAL_PASS_2026-08-10.md`
28. `docs/PATCH_NOTES_HOME_SIDE_VIEW_ARCS_2026-08-10.md`
29. `verification/HOME_SIDE_VIEW_ARCS_2026-08-10.md`
30. `docs/PATCH_NOTES_HOME_GROUNDING_CELESTIAL_SEQUENCE_2026-08-10.md`
31. `verification/HOME_GROUNDING_CELESTIAL_SEQUENCE_2026-08-10.md`
32. `docs/PATCH_NOTES_HOME_ART_REDESIGN_2026-08-10.md`
33. `docs/PATCH_NOTES_CELESTIAL_OPPOSING_ARCS_2026-08-10.md`
34. `verification/FULL_VERIFICATION_2026-08-10_F51F2F7C.md`
35. `verification/FULL_VERIFICATION_2026-08-11_F51F2F7C.md`
36. `docs/PATCH_NOTES_TASK_KEYWORDS_CELESTIAL_NIGHT_PLANNER_2026-08-11.md`
37. `verification/TASK_KEYWORDS_CELESTIAL_NIGHT_PLANNER_2026-08-11.md`

Read `docs/ARCHIVE_SUPERSEDED.md` only when historical reasoning is needed.

## Sources Of Truth

- `officewarsautobattler.html` is the implemented game.
- `docs/GAME_DESIGN.md` is the stable product model.
- `docs/BALANCE_LEDGER.md` contains active Implemented, Locked, Draft, and Open
  decisions.
- `docs/PROJECT_STATUS.md` records the current candidate and balance evidence.
- `officewars-ui-prototype.html` is a visual reference, not gameplay truth.

## Implementation Status

`officewarsautobattler.html` now contains the complete approved overhaul
candidate through rollout Phase 6: core balance, the fixed-rarity 50-card
roster, shared card and schedule resolution, Skill-XP career paths and
capstones, advanced Skill systems, centralized Home effects, legacy replacements, the
real HUD, deterministic cycling playback controls, the office port, versioned
active-run persistence, and the contextual first-day orientation.

The current HTML includes the deterministic Skip repair described in
`docs/PATCH_NOTES_SKIP_FIX_2026-08-06.md`. It prelocks meeting and Office Chat
participants and outcomes, the daily visitor, and sabotage; stores canonical
gameplay IDs; resolves sabotage immediately after the midpoint desk visit; and
rolls back gameplay state and both random streams if Skip resolution throws.

The current HTML has SHA-256
`387FB7F1062CFEA15E3D14A44D40E85FA4455EA53AE3B37BCC0E182DD9B6C969`.
Hashes are taken over LF content, matching the repository and public package; a
CRLF working copy produces a different value.
It replaces the three speed buttons with one cycling 1x/2x/4x button and makes
the new 1x equal to the previous 2x presentation pace. It also replaces
Endless with Continue Run, autosaves committed state, restores prepared
Workdays deterministically to Clock Out, preserves casino games and run
results, and teaches the basic journey through ten contextual callouts. The
player's project progress now fills behind the top-center project title under
a fixed readability scrim, shows the exact fraction, and pulses on change. The
bottom-left player HUD now contains only the portrait and Stress bar. Workday
action results now clear when the next action starts and update in the same
settlement step as the HUD, rather than remaining one action behind.

Relationship tooltips now show only each coworker's actual bonus, and the
Outings footer explains that coworkers grant bonuses when met during the
Workday. Manual Lights Out and Home or Deal purchases now exclude one another
in both directions; Outings stay independent, and Moodboard's automatic Lights
Out remains the explicit exception. Active Brand Strategy mornings use a
four-part Campaign status band showing the Campaign name, requested task and
family, completed steps, and Campaigns completed. `Rebrand Initiative` now
explains Campaign replacement, ordered completion, and its reward promise.
Night now removes the office HUD and presents the player's current living
space. The iPad-style Night Planner consolidates Home Shop, Outings,
Relationships, and conditional Deal Desk tabs with persistent Stress, Lights
Out, Finalize Night, and Hide Planner controls. Room shortcuts open the full
Planner, Home Shop, Social tabs, Deal Desk, Lights Out, and End Day. Finalizing
from the Planner or bed preserves that interface as the next Night's opening
preference. Cash, Expense Credit, Stress, and projected post-sleep Stress
remain prominent; occupied item slots expose tooltips and an accessible sale
confirmation. Apartment, Townhouse, House, and Penthouse use distinct wall
treatments while sharing one flat side-view layout. The bed, Night Planner
iPad, full Home Shop PC, Deal laptop, plant, and Social door follow a stable
left-to-right order and meet one shallow patterned floor boundary. Furniture
bodies remain above the baseboard instead of sitting inside a deep floor band.
Item capacity appears on a wall storage shelf instead of a perspective rug.
The moon appears inside the window, the Home name sits below the furniture,
the top status includes a Stress bar, and Lights Out visibly dims the room.

The manager office now shows the current manager with a distinct portrait and
color. Managers remain seated on ordinary floors and use a cosmetic patrol on
boss floors. The patrol is not part of `CAST`, consumes no RNG, reserves no
space, and cannot change Workday outcomes or Skip behavior.

Clock Out enters Home through a sunset and door-opening presentation. Outings
fade to their story and back to the room; End Day uses sunrise to return to the
office. The sun and moon share one east-to-west arc but never occupy the same
stretch of it. Screen-right is east and screen-left is west. The departing
body completes the western half and drops below the left edge while the
arriving body enters from the right/eastern edge and climbs to the vacated
resting position, so the two never cross. Automated and reduced-motion paths
bypass presentation timing without changing state. Sleep writes a stable
`nightResolved` checkpoint before sunrise so a refresh cannot repeat recovery.

Schedule previews and choices now use action-icon timelines with source badges
and highlighted differences. Prototype Test stacks its schedule options;
Schedule Adjustment and Leadership select directly on the timeline; action
guarantees use matching icon tiles; the final Schedule Desk shows the locked
day in the same visual language.

Resume milestones show distinct unreached, pending, and claimed states.
Automation Combo places End Combo and every legal reroll before its task
cards.

The Resume rail now places a distinct bright 8-bit scene behind each
Skill: a code workstation, meeting space, design desk, storefront, and
operations rack. A fixed scrim keeps names, XP segments, paths, and milestone
markers in the foreground. The scenes remain decorative and pointer-inert,
and the collapsed Workday rail uses a dimmer treatment behind its initials.

Morning Build Context now lists active delayed effects and selected targets,
named Delegates, named Contacts, and relevant run resources before task
selection. The strip caps its visible entries and routes overflow into the
Resume. Pinned Tasks now use compact Skill, name, and rarity rows; activating
one opens a full task card before selection. Resume milestone boxes expose
their exact selected-path effects through hover, keyboard focus, and tap, or
state that specialization is not chosen yet.

Eye for Detail now records the previous primary task's selection source.
Revision does not create another Revision pin when the task came from Pinned
Tasks, while the same task can pin again after a later generated-offer play.
Masterpiece and other independent pin sources are unchanged. Named trait
mechanics and task-card rules terms use a shared high-contrast glossary in
path-choice, Promotion, Resume, Morning, Pinned Task, and separate-picker
text, with short definitions on hover, keyboard focus, and tap. Tapping a
keyword inside a selectable card does not select that card.

Every separate task picker uses the Morning task-card visual language.
Complete-play and future-primary decisions show the full card, printed-effect
copy choices hide stats, Schmoozing Assist choices show stats only, and
category-only choices show identity only. Automation additional Combo cards
explicitly grant no Skill XP while retaining completion counters, Codebase,
and other Complete Play triggers.

The first Night tutorial automatically opens and spotlights the consolidated
Planner. It explains shopping, Outings, Relationships, coworker bonus timing,
Lights Out, finalization, and the optional room interface in one callout. The
orientation then explains the first three-path Promotion choice and later 6/10
XP milestones, covers the first boss-floor introduction, and finishes when the
first Capstone is claimed. Its Workday callout opens the live Action Guide and
explains all six ordinary actions with current values. Conditional Deals are
not separately taught. Options contains the persistent master-volume setting
and the tutorial reset command; How to Play no longer duplicates that command.

Player-facing progression language now calls Coding, Management, Design,
Sales, and Operations `Skills`; internal data still uses `family` identifiers.
Final Promotion Review is a visual five-page Skill summary. It shows only
milestones earned in that promotion, presents a newly claimed capstone as a
prominent card, shows Stress as a bar and Cash as green text, and uses direct
Confirm Promotion and Revise Choices actions without a second generic confirm.
If the player accepts Finalize Night without manually choosing Lights Out,
Lights Out is applied automatically when it remains legal. Home and Deal
purchases still block it unless an explicit exception applies.

Player and headless Night finalization now share the same automatic
Lights-Out legality gate. A simulated Home or Deal purchase therefore receives
only automatic sleep unless Moodboard or another explicit exception permits
both.

The current implementation report is
`verification/TASK_KEYWORDS_CELESTIAL_NIGHT_PLANNER_2026-08-11.md`. The current
hash passes the focused keyword/celestial, Night Planner, Home/schedule, smoke,
24-check persistence/tutorial, eight-group advanced interaction, and
readability visual suites plus the full no-simulation verifier. All 50 ordinary
cards pass preview, markup, and primary Complete Play traversal. No sampled
page error, console error, external runtime request, clipped text, or viewport
overflow was found.

The preceding exhaustive report is
`verification/FULL_VERIFICATION_2026-08-11_F51F2F7C.md`. It remains exact
historical evidence for its named earlier hash.

The imported Home verifier initially failed because its keyframe discovery set
still named four retired animations while its assertions expected the two
current half-arcs. The discovery set was repaired without changing gameplay,
and the focused runner now passes at desktop and landscape sizes.

The preceding exhaustive implementation report is
`verification/FULL_VERIFICATION_2026-08-10_0A8F74E5.md`. It finds no
implementation blocker on its named hash while preserving structural simulation, formal
screen-reader execution, exhaustive picker and save-boundary traversal,
rapid-input fuzzing, and memory profiling as Not Run or Blocked.

The earlier 58.4 percent scripted-skilled result remains historical snapshot
telemetry because it predates the corrected Night policy. Fresh structural
simulation has not run.

Exhaustive screen-reader, every-picker, every-boundary save/restore, reset,
rapid-input, and memory-profile rows remain explicitly Not Run or Blocked; do
not imply that the focused suites close those broader rows.

## Implemented Scope

- All 50 ordinary family cards are implemented: each family has four Common,
  three Uncommon, two Rare, and one Legendary card.
- The 14 visible family paths, including Closing, and the hidden Brand Strategy
  path are implemented in the candidate. Their exact effects remain defined in
  the ledger.
- `Rebrand Initiative` is a Special card outside the 50-card roster. It is the
  implemented unlock for Brand Strategy.
- Eligible ordinary random slots use Common 70 percent, Uncommon 20 percent,
  Rare 9 percent, and Legendary 1 percent after the 0.2 percent Special check.
  At most one Special can replace a slot in one generated window.
- The implemented base floor curve is
  `110/10, 130/8, 165/7, 210/6, 250/6, 285/6, 300/5`.
- Meeting variance, manager tuning, Weekend casino frequency, Chad's
  ten-upgrade cap, and the retained Chad coefficients are implemented as the
  structural simulation baseline.
- All eight decision gates are represented in the candidate, including the
  legacy Resume replacements, advanced family systems, deterministic playback,
  real HUD, and responsive office.
- One active run persists in browser storage. Continue Run, replacement-run
  confirmation, deterministic prepared-Workday restore, casino continuation,
  persistent results, return to menu, tutorial completion, skip, and replay
  are implemented.
- The verification checklist remains the requirement inventory. The dated
  full-verification report records item-level Pass, Fail, Not Run, and Blocked
  evidence; unchecked checklist boxes must not be interpreted as passes.

## Family Card Identities

- **Coding - Build, Automate, Integrate:** turn prior work into future value,
  sequence additional cards, and bridge progression between Skills.
- **Management - Coordinate, Schedule, Amplify:** observe people and actions,
  rearrange or guarantee the schedule, and multiply successful coordination.
- **Design - Observe, Iterate, Transform:** reveal information, refine repeated
  work, and copy or convert existing card effects.
- **Sales - Earn, Spend, Network:** generate purchasing power, convert spending
  into leverage, and monetize relationships.
- **Operations - Reserve, Stabilize, Deliver:** bank resources for later,
  replace unreliable outcomes, and turn successful processes into dependable
  throughput.

## Simulation Status And Priorities

The current headless Night policy is rules-faithful at finalization. It uses the
same helper as the player path to reject manual or automatic Lights Out after a
Home or Deal purchase unless an explicit exception applies.

The prior exact-snapshot audit completed 3,000 seeded runs without runtime
errors: baseline won 0.7 percent, random won 12.2 percent, and
scripted-skilled won 58.4 percent. `Regression Tests` was the policy's largest
selection outlier. Preserve those numbers only as historical telemetry until a
rules-faithful rerun replaces them.

The advanced suite found no rules defects. Its maximal action fixture did,
however, resolve 121 actions for 2,403 project progress. Treat that as a
serious balance and readability watchpoint alongside the skilled-policy
outlier.

Continue to test all 50 cards against standalone value, family identity,
trait-breakpoint pressure, floor pacing, stress, deadlines, rival pressure,
managers, Homes, economy, and every additional-card or replay rule. Pay
particular attention to:

- repeated Legendary effects through Pilot Approved, Logistics, Rapid
  Prototype, Design System, and other complete-play effects;
- action inflation from War Room, Perfect Execution, Efficiency, Agile,
  Leadership, Deals, and bonus Work sources;
- economy compounding across Sales cards, Negotiation, Compound Interest,
  discounts, financing, and Expense Credit;
- Success Fee's late-run cash spikes and Productivity License plus Contractor
  Support's Work-action burst;
- information overload from schedule, task, and outcome-selection effects;
- early dead cards versus acceptable high-ceiling setup pieces; and
- whether any card is an automatic pick or never worth delaying a trait
  breakpoint.

Treat measured outliers as evidence rather than automatic nerfs. Any balance
change still requires explicit approval and a ledger update.

## Remaining Work

Run persistence and first-day onboarding are implemented. Focused restoration
coverage passes, including pending Slots, Blackjack, and Poker. Exhaustive
every-picker and every-transition restoration remains part of the broader
unverified matrix rather than an implementation blocker discovered in this
pass.

Rerun the balance matrix on the corrected policy, then test the structural
curve and all trait paths against the 25-35 percent skilled target. Numeric
changes require explicit approval. Unverified rows retain their exact status
in the preceding full report.

Home effects are centralized and optional inert set metadata is supported.
Actual Home sets, thresholds, bonuses, prices, and resale tuning remain
deliberately deferred until after implementation verification.

## Product Guardrails

- Preserve one standalone HTML file with no required server or build step.
- Preserve office-friendly AFK playback.
- Keep meaningful choices at morning, night, weekend, and promotion phases.
- Prefer concise card text, forecasts, icons, bars, and tooltips.
- Never describe Draft or Open material as approved or implemented.

## Project Skills

- `$officewars-plan` owns design and balance planning.
- `$officewars-implement` owns approved end-to-end feature implementation,
  including UI, persistence, tests, documentation, mirrors, and packages.
- `$officewars-debug` owns exact-state reproduction, root-cause repair, and
  focused regression coverage without unrelated redesign or tuning.
- `$officewars-balance-lab` owns policy-legality audits, fixed-seed
  simulations, telemetry, ablations, and Draft-only tuning recommendations.
- `$officewars-ux-audit` owns onboarding, navigation, information hierarchy,
  responsive rendering, interaction feedback, and accessibility analysis.
- `$officewars-playtest-analysis` owns evidence synthesis from human notes,
  saves, screenshots, recordings, surveys, and telemetry.
- `$officewars-qa-cleanup` owns active-document cleanup, decision-status
  reconciliation, mirror synchronization, manifests, and release packages. It
  does not modify gameplay.
- `$officewars-full-verification` owns the bidirectional requirement matrix and
  exhaustive static, behavioral, deterministic, persistence, browser,
  accessibility, distribution, edge-case, and legal-simulation evidence. It
  reports every item as Pass, Fail, Not Run, or Blocked and does not repair
  gameplay unless fixes are separately requested.
- `$officewars-github-package` owns public-mirror synchronization, release
  truth and hash updates, deterministic GitHub-ready ZIP creation, and
  byte-for-byte package verification.

All nine project skills support explicit `$` invocation and may also be
invoked automatically when a request clearly matches their scope.

## Portable Handoff

`officewars-rollout-handoff-2026-07-31/` is the current portable package.
`officewars-public-repo-2026-08-07/` is the source workspace's public
repository package; its contents become the repository root when exported.
Both packages' mapped game, guidance, active documents, verifiers, reports, and
hashes were synchronized with the root candidate on 2026-08-11.
