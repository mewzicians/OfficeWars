# OfficeWars Project Status

Snapshot date: 2026-08-11

Implemented game SHA-256:
`387FB7F1062CFEA15E3D14A44D40E85FA4455EA53AE3B37BCC0E182DD9B6C969`

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
- a ten-step contextual orientation covering the first day, consolidated Night
  Planner, first path choice, milestone growth, first boss floor, and first
  claimed Capstone, with spotlighted existing UI, persisted progress, Skip
  Orientation, and reset through Options for the next New Run;
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
  objects for the Night Planner, Home Shop, Social, unlocked Deals, Lights Out,
  and End Day;
- an iPad-style Night Planner with Home Shop, Outings, Relationships, and
  conditional Deal Desk tabs; persistent Stress, Lights Out, Finalize Night,
  and Hide Planner controls; and remembered Planner-versus-room preference;
- prominent Home Cash and Credit, accessible visual item slots with sale
  confirmation, a top Stress bar, current and projected Stress, moon phases,
  pixel-room decor, and Apartment through Penthouse scene variants;
- flat side-view room geometry across every Home tier, with the larger bed,
  Night Planner iPad, complete PC desk, Deal laptop, plant, and Social door
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
  presentations; screen-right is east and screen-left is west, and the sun and
  moon share one right-to-left arc without crossing, the departing body
  finishing the western half while the arriving body enters from the
  right/eastern edge and climbs to the vacated resting position, plus
  deterministic reduced-motion and automated bypasses;
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
- named trait mechanics and rules-loaded task-card terms use a shared cyan
  glossary treatment with short definitions available through hover, keyboard
  focus, and tap; task cards expose the treatment in full Morning cards,
  compact details, Pinned Task details, and separate task pickers without
  letting a keyword tap play the card;
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

The current implementation report is
`TASK_KEYWORDS_CELESTIAL_NIGHT_PLANNER_2026-08-11.md`. The preceding exhaustive
report is `FULL_VERIFICATION_2026-08-11_F51F2F7C.md`; it remains exact evidence
for its named earlier hash.

Verified on the current hash `387FB7F1`:

- Focused task-keyword/celestial, Night Planner, Home/schedule, smoke,
  persistence/tutorial, advanced interaction, visual, and full no-simulation
  verification pass.
- The smoke suite passes its 1x/2x/4x/Skip determinism and RNG-equality checks.
- All 24 persistence and tutorial checks pass, including corrupt saves,
  prepared-Workday restoration, exactly-once Night resolution, casino
  continuation, results, and tutorial lifecycle.
- All eight advanced interaction groups pass, including every ordinary path,
  exceptional-system lifecycles, promotion and capstone priority, coworker
  ordering, Clock Out economy, and worst-case resolution chains.
- All 50 ordinary cards pass preview, markup, and primary Complete Play
  traversal. Roster, rarity, registry, floor-curve, and core-value invariants
  pass.
- The visual and layout matrices pass at desktop, compact desktop, landscape
  phone, portrait rotation, reduced motion, and 200-percent text scaling.
- Home geometry passes across all four tiers at desktop and landscape, with
  every measured furniture piece grounded within 0.01px of the floor line.
- The opposing celestial half-arcs pass current keyframe, apex, phasing, and
  zero-delay checks. Five sampled points per transition confirm right/east to
  left/west movement and no sun/moon crossing.
- Forty-one of the 50 ordinary cards contain at least one glossary term. Full,
  compact, Pinned Task, and separate-picker card modes pass hover, focus, tap,
  and click-safety checks.

Not Run on the current hash:

- fresh structural balance simulation under the corrected Night policy;
- formal screen-reader execution;
- exhaustive every-picker and every-transition save/restore traversal;
- rapid-input fuzzing; and
- long-session memory profiling.

Historical evidence, valid only for its named hash:

- `FULL_VERIFICATION_2026-08-10_0A8F74E5.md` found no implementation blocker on
  hash `0A8F74E5`, with structural simulation, formal screen-reader execution,
  exhaustive picker and save-boundary traversal, rapid-input fuzzing, and
  memory profiling explicitly Not Run or Blocked.
- `FULL_VERIFICATION_2026-08-10_55D9A6ED.md` is the preceding exhaustive
  verdict; its headless Night-policy failure was fixed on hash `470F4146`.
- `FULL_VERIFICATION_2026-08-10_F51F2F7C.md` records the GitHub environment
  where Python was unavailable. Its Blocked runtime rows are superseded as
  current status by the August 11 local report, but remain valid history.
- `FULL_VERIFICATION_2026-08-11_F51F2F7C.md` is the preceding exhaustive local
  report. Its conclusions remain historical evidence for hash `F51F2F7C`.

Older dated reports remain exact-snapshot historical evidence. Use
`HOME_GROUNDING_CELESTIAL_SEQUENCE_2026-08-10.md` for the preceding focused
candidate, `HOME_SIDE_VIEW_ARCS_2026-08-10.md` for the preceding opposing-arc
snapshot,
`HOME_MANAGER_VISUAL_PASS_2026-08-10.md` for the preceding Home and manager
candidate,
`HOME_SCHEDULE_TUTORIAL_2026-08-10.md` for the preceding Home and schedule
candidate,
`FULL_VERIFICATION_2026-08-10_0A8F74E5.md` for the preceding exhaustive
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
5. Close or explicitly accept the current report's remaining Not Run rows,
   then rerun verification after approved tuning.

Home item sets remain deferred until the current verification and balance gate
is closed.
