# OfficeWars Project Status

Snapshot date: 2026-08-10

Implemented game SHA-256:
`F51F2F7C7A11098FA7DABF5692767D14D14B75F45AFA9CADC6EB3DA96A141A46`

Hashes in this project are taken over LF content, which is what the repository
and the public package store. A CRLF working copy produces a different value.

Skip repair details and validation scope are recorded in
`docs/PATCH_NOTES_SKIP_FIX_2026-08-06.md`.

## Current Candidate

`officewarsautobattler.html` contains the approved implementation candidate
through rollout Phases 0-6:

- the fixed-rarity 50-card roster;
- Skill XP, ordinary career paths, capstones, and advanced Skill systems;
- shared card, schedule, coworker, Clock Out, and transition resolution;
- centralized Home effects and legacy-system replacements;
- the real HUD, Resume Book, deterministic playback, responsive office, and
  portrait rotation gate;
- a consolidated player project HUD with the progress fill behind the
  top-center project title, a fixed readability scrim, exact progress, and a
  brief change pulse; the bottom-left player HUD is portrait plus Stress only;
- Workday ticker outcomes clear at the start of each action and update when
  that action settles, in sync with the persistent HUD;
- one cycling 1x/2x/4x playback button, with the new 1x using the previous 2x
  presentation pace;
- one versioned active-run save with Continue Run, replacement confirmation,
  deterministic prepared-Workday restore, casino continuation, persistent
  results, and return to menu;
- a thirteen-step contextual orientation covering the first day, Home Shop,
  Outings, Relationships, ending the night, the first path choice, milestone
  growth, the first boss floor, and the first claimed Capstone, with
  spotlighted existing UI, persisted progress, Skip Orientation, and reset
  through Options for the next New Run;
- a first-Workday tutorial pause that opens the live Action Guide and explains
  Work on Task, Lunch, Water Cooler, Office Chat, Slumped at Desk, and Team
  Meeting using current values;
- an Options screen with a persistent master-volume slider prepared for future
  audio and the tutorial reset command;
- the readability overhaul for Morning cards, Resume, resolved Workday
  feedback, Clock Out grouping, and the Night decision surface; and
- concise relationship bonuses plus a Workday-bonus explanation in Outings;
- a two-way lock between manual Lights Out and Home or Deal purchases, with
  Outings independent and automatic Moodboard Lights Out exempt;
- a dedicated active-Campaign status band and clearer `Rebrand Initiative`
  description; and
- a dedicated Home scene that removes the office HUD at Night and uses room
  objects for Home Shop, Relationships, Outings, unlocked Deals, Lights Out,
  and End Day;
- prominent Home Cash and Credit, accessible visual item slots with sale
  confirmation, a top Stress bar, current and projected Stress, moon phases,
  pixel-room decor, and Apartment through Penthouse scene variants;
- flat side-view room geometry across every Home tier, with the larger bed,
  Relationships phone, complete PC desk, Deal laptop, plant, and Outings door
  grounded on one shallow patterned floor boundary; Home item slots sit on a
  wall storage shelf, the Home name stays below the furniture, the moon remains
  inside the window, and Lights Out dims the complete room;
- a Home room art pass that draws every piece from the shared feet line rather
  than from per-piece offsets, so all six measured pieces ground within 0.01px
  of that line, and that adopts the office scene's outline, wood, metal, glass,
  gold, grid, and flat offset-shadow treatment; item slots rest on the shelf,
  a wall clock fills the open wall, and the tiers differ by material quality;
- distinct manager portraits and colors, with seated ordinary-floor managers
  and a presentation-only boss-floor patrol that never enters gameplay state;
- sunset and door-opening entry, Outing fade and return, and sunrise exit
  presentations; the sun and moon share one east-to-west arc but never occupy
  the same stretch of it, the departing body finishing the western half while
  the arriving body enters from the opposite eastern edge and climbs to the
  vacated resting position, plus deterministic reduced-motion and automated
  bypasses;
- action-icon schedule trackers for Prototype Test, Schedule Adjustment,
  Leadership, action guarantees, and the final Schedule Desk;
- Resume milestone states for unreached, pending, and claimed gates;
- five distinct bright 8-bit Resume-rail scenes, kept behind a
  readability scrim and marked decorative for assistive technology;
- a Morning Build Context strip that names active delayed effects and their
  selected targets, Delegates, Contacts, and relevant run resources before
  task selection;
- compact Pinned Task rows that show Skill, task name, and rarity before
  opening the ordinary full task card for inspection and selection;
- Eye for Detail Revision pins now use primary-task source provenance. A task
  played from Pinned Tasks does not pin itself again, while the same task can
  pin normally after a later generated-offer play; Masterpiece is unchanged;
- exact 3, 6, and 10 XP milestone tooltips through hover, focus, and tap,
  including a clear unchosen-specialization state;
- named trait mechanics use a shared cyan glossary treatment with short
  definitions available through hover, keyboard focus, and tap;
- player-facing progression language calls the five job categories Skills
  while internal `family` identifiers remain unchanged for save and rules
  compatibility;
- final Promotion Review paginates one Skill per page, shows only milestones
  earned in that promotion as visual cards, presents a newly claimed capstone
  prominently, and uses direct Confirm Promotion and Revise Choices actions;
- accepting Finalize Night automatically applies Lights Out when it remains
  legal and was not selected manually; purchase locks and explicit exceptions
  remain unchanged;
- player and headless Night finalization now share the same automatic
  Lights-Out legality gate, so a Home or Deal purchase prevents that recovery
  unless an explicit exception applies;
- Automation Combo controls separated from its cards, with daily, banked, and
  paid rerolls shown before the task offer. Additional Combo cards grant no
  Skill XP while retaining their other Complete Play progression;
- every separate task picker uses full or reduced Morning-style task cards
  according to whether the decision uses the complete play, printed effect,
  stats, or identity; and
- Skip now resolves the active action and remaining locked schedule directly,
  bypassing presentation-only walking and conversation waits while preserving
  action, desk-visit, sabotage, and Clock Out resolution. Meeting and Office
  Chat participants and Outcomes, the daily visitor, and the saboteur are
  prelocked; participant records use canonical gameplay IDs; and an unexpected
  resolver error rolls back gameplay state and both RNG streams before
  restoring Skip for a deterministic retry.

## Verification

The current exhaustive report is
`FULL_VERIFICATION_2026-08-10_F51F2F7C.md`. Read it before trusting any row
below; it records exact Pass, Fail, Not Run, and Blocked status.

Verified on the current hash `F51F2F7C`:

- JavaScript syntax, balanced stylesheet, standalone load with the ready flag
  set, and required element IDs present.
- Zero external network requests, and zero page or console errors across the
  menu, Morning, Resume Book, and Night surfaces.
- Roster and structural invariants read from the loaded tables: 50 ordinary
  cards, ten per Skill, a 4/3/2/1 rarity split in every Skill, no duplicate
  task IDs, `rebrandInitiative` as the only Special, four Homes at 3/6/9/12
  slots, eight managers, an eight-member cast, seven floors, and the
  `110/10, 130/8, 165/7, 210/6, 250/6, 285/6, 300/5` floor curve.
- Player-surface sweep at desktop, compact desktop, and landscape phone: no
  horizontal overflow, no interactive element outside the viewport, and no
  interactive element without an accessible name.
- Home room geometry across all four tiers at desktop and landscape: feet line,
  slot placement above the wall boundary, left-to-right furniture order, moon
  inside the window, and title below the furniture, with every measured piece
  within 0.01px of the floor line.
- Both phase transitions: the sun and moon hold a minimum horizontal separation
  of about 48 percent of viewport width throughout, and reduced motion bypasses
  the transition without leaving the layer active.

Not verified on the current hash. These require Python and Playwright, which
were unavailable on the machine used for this pass, so they are Blocked rather
than passing or failing:

- the smoke suite and its 1x/2x/4x/Skip determinism and RNG-equality
  comparisons;
- the 24-check persistence suite;
- the eight advanced interaction groups and the focused pin, glossary, and
  tutorial contract group;
- the full verifier's automated runtime audit and sampled accessibility checks;
- every simulation and balance measurement.

Historical evidence, valid only for its named hash:

- `FULL_VERIFICATION_2026-08-10_0A8F74E5.md` found no implementation blocker on
  hash `0A8F74E5`, with structural simulation, formal screen-reader execution,
  exhaustive picker and save-boundary traversal, rapid-input fuzzing, and
  memory profiling explicitly Not Run or Blocked.
- `FULL_VERIFICATION_2026-08-10_55D9A6ED.md` is the preceding exhaustive
  verdict; its headless Night-policy failure was fixed on hash `470F4146`.
- On hash `470F4146` the smoke, persistence, advanced interaction, and full
  verifier suites passed, and the focused visual and Home/schedule matrices
  found no clipped text, persistent-HUD overlap, or viewport overflow. Those
  results do not transfer to the current hash.

Older dated reports remain exact-snapshot historical evidence. Use
`HOME_GROUNDING_CELESTIAL_SEQUENCE_2026-08-10.md` for the current focused
candidate, `HOME_SIDE_VIEW_ARCS_2026-08-10.md` for the preceding opposing-arc
snapshot,
`HOME_MANAGER_VISUAL_PASS_2026-08-10.md` for the preceding Home and manager
candidate,
`HOME_SCHEDULE_TUTORIAL_2026-08-10.md` for the preceding Home and schedule
candidate,
`FULL_VERIFICATION_2026-08-10_0A8F74E5.md` for the current exhaustive
implementation verdict on its named preceding hash,
`BUILD_CONTEXT_PINS_2026-08-10.md` for the preceding Build Context candidate,
`RESUME_SKILL_ART_2026-08-10.md` for the preceding Resume-art candidate,
`OPTIONS_NIGHT_POLICY_2026-08-10.md` for the preceding Options and Night-policy
candidate, and
`FULL_VERIFICATION_2026-08-10_55D9A6ED.md` for the preceding exhaustive
snapshot,
`NIGHT_RESUME_AUTOMATION_UI_2026-08-10.md` for the preceding Night and
Automation snapshot, `WORKDAY_TICKER_SYNC_2026-08-07.md` for the preceding
ticker snapshot,
`PROJECT_HUD_CONSOLIDATION_2026-08-07.md` for the preceding HUD snapshot,
`PERSISTENCE_TUTORIAL_2026-08-07.md` for detailed continuity evidence, and
`FULL_VERIFICATION_2026-08-07_30214B7F.md` for that snapshot's Pass, Fail, Not
Run, and Blocked matrix. `FULL_VERIFICATION_2026-08-07.md` remains historical
evidence for its named preceding hash.

## Historical Balance Evidence

Across the last 1,000 scripted-skilled seeds before the two-way Night rule:

- victories: 584;
- burnouts: 179;
- Chad losses: 177;
- deadline losses: 60;
- scripted-skilled win rate: 58.4 percent against a 25-35 percent target.

The prior hash produced 55.3 percent skilled wins on the same seeds. The Skip
repair changes no numeric balance constants, but prelocking gameplay changes
RNG consumption and therefore cross-version run trajectories. `Regression
Tests` selections increased from 2,567 to 3,160.

These results are not valid current balance evidence because they predate the
corrected headless Night policy. The fixed-seed matrix must be rerun before
drawing current win-rate or Closing conclusions.

The difficulty curve is misshapen rather than uniformly low. Floor 3 is the
largest competitive wall, while successful builds accelerate sharply after
Floor 4.

The strongest sampled trait cores used Eye for Detail with Agile, often adding
Clean Code or Efficiency. Closing was the weakest sampled path, primarily
losing tempo to Chad rather than burning out.

A policy forced to pursue actual Chain 9 completed 159 Chain 9 Closes and won
62 of those runs, a 39.0 percent conditional win rate. This is evidence that
high-chain Closing may not deliver its intended heavily favored payoff.

## Pending Human Evidence

No balance change has been approved from these simulations. The project owner
is testing Closing with human players before deciding whether to change its
rewards, cycle tempo, or chain thresholds.

Record human results using `docs/PLAYTEST_GUIDE.md`.

## Next Engineering Gate

1. Collect human playtest evidence.
2. Run a structural matrix with the corrected Night policy that holds Floors
   1-3 stable while testing Floors
   4-7 project requirements and late Chad pressure.
3. Test all trait paths with policies capable of selecting and using them.
4. Apply only explicitly approved tuning.
5. Close or explicitly accept the current full report's Not Run and Blocked
   rows, then rerun verification after approved tuning.

Home item sets remain deferred until the current verification and balance gate
is closed.
