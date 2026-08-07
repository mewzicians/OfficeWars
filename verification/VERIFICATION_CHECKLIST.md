# OfficeWars Verification Checklist

## Current Status

The rollout and readability candidate exists. The current `full verification`
ran on 2026-08-07; its Pass, Fail, Not Run, and Blocked evidence is in
`verification/FULL_VERIFICATION_2026-08-07_30214B7F.md`. Player-facing
implementation, readability, deterministic playback, persistence, and
distribution pass. The headless Night policy fails the same purchase-versus-
Lights-Out rule that the player UI enforces, so current balance simulation is
Blocked. The current focused persistence and orientation suite is recorded in
`verification/PERSISTENCE_TUTORIAL_2026-08-07.md`. The broad report still names
every group that remains unverified.

The boxes below remain a reusable requirement inventory rather than a claim of
completion. An unchecked box does not mean the feature is absent, and a result
from the dated report must not be promoted to Pass without its cited evidence.

## Verification Protocol

`full verification` runs this entire checklist. Do not treat the checklist as
the requirement source or assume it is complete:

1. Reconstruct a bidirectional traceability matrix from `AGENTS.md`,
   `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`, `docs/HANDOFF.md`,
   `docs/PROJECT_STATUS.md`, and the implemented HTML.
2. Map every Locked requirement to its state, code path, player-facing surface,
   deterministic test, and documentation.
3. Map every gameplay state and player-facing control back to an active
   requirement. Flag undocumented behavior and unreachable or hidden state.
4. Run documentation cleanup, static checks, behavioral and edge-case tests,
   deterministic playback, browser and accessibility checks, distribution
   tests, and applicable simulations.
5. Record each item as `Pass`, `Fail`, `Not Run`, or `Blocked` with evidence.
   Never omit or silently pass an item that could not be verified.

Do not claim completion from visual inspection alone. Do not change gameplay
during a verification-only request unless the user separately asks for fixes.

## Static Checks

- [ ] The game remains one standalone HTML file.
- [ ] No required external script, font, image, server, or build step.
- [ ] JavaScript parses successfully.
- [ ] No duplicate HTML ids.
- [ ] Every `getElementById` target exists.
- [ ] CSS and JavaScript braces are balanced.
- [ ] No obsolete Resume-stack copy remains after migration.
- [ ] Library grants its additional family XP exactly once per floor and only
  from an ordinary primary task.
- [ ] Hackathon and Networking Brunch use their Locked replacement rewards.
- [ ] Removing player Resume stacks does not remove Chad's rival stacks or
  accumulated upgrades.
- [ ] Every Home effect resolves through the centralized registry; repository
  search finds no live scattered upgrade-id behavior checks outside that
  registry and its presentation helpers.
- [ ] Optional Home set metadata, set-progress tooltips, and sale-break previews
  are supported, but no active set definition or set bonus ships in this
  overhaul.
- [ ] Tooltips, forecasts, legends, and Help match behavior.

## Documentation QA

- [ ] Active guidance does not describe the completed 50-card roster as
  unfinished or reopened.
- [ ] Implemented Baseline text is clearly separated from approved rollout
  behavior.
- [ ] Draft and Open values are never described as Locked.
- [ ] Every public documentation link resolves to an included file.
- [ ] `docs/PROJECT_STATUS.md` names the current gameplay hash.
- [ ] Superseded planning directions appear only in a clearly labeled
  Implemented Baseline, `docs/ARCHIVE_SUPERSEDED.md`, or its indexed
  historical snapshots.

## Determinism And Playback

- [ ] Identical seed and choices produce identical complete runs.
- [ ] 1x, 2x, 4x, and Skip produce identical final state.
- [ ] Animation timing never changes random calls or outcomes.
- [ ] Saving and restoring at phase boundaries preserves the next result.

## Persistence And Orientation

- [ ] Continue Run appears only for a valid compatible active save.
- [ ] Corrupt and incompatible saves are discarded without blocking New Run.
- [ ] New Run requires confirmation before replacing an active save.
- [ ] Stable phases and committed irreversible decisions autosave.
- [ ] Refreshing Morning preserves the exact offer and random state.
- [ ] A prepared Workday restores its deterministic checkpoint, resolves
  headlessly to Clock Out, and never duplicates task rewards.
- [ ] Night restores its active tab, Lights Out choice, catalogs, limits, and
  committed purchases without refunding or rerolling them.
- [ ] Restoring an older Night state that contains both a committed Home or
  Deal purchase and manual Lights Out preserves the purchase and clears manual
  Lights Out; automatic Moodboard Lights Out remains exempt.
- [ ] Active casino chips, game state, and hand limits restore. Pending Slots
  settle exactly once; Blackjack and Poker return to a legal continuation.
- [ ] Victory and defeat summaries survive refresh and Return to Main Menu
  clears only the active run.
- [ ] Tutorial completion is stored separately from the run save.
- [ ] The six orientation steps spotlight the correct existing UI at Floor
  Intro, Morning, pre-Workday, Clock Out, and Night.
- [ ] Skip Orientation persists, and How to Play can schedule a replay for the
  next New Run.
- [ ] The orientation never rigs offers or outcomes and never interrupts
  Workday playback after it starts.

## Core Balance

- [ ] Floor stress multiplier is 20 percent per floor after floor 1.
- [ ] Recovery is never multiplied by floor pressure.
- [ ] Automatic sleep is 4 percent.
- [ ] Comfy Mattress produces 6 percent automatic sleep.
- [ ] Lights Out adds 5 percent base recovery.
- [ ] Non-final promotion recovery is 25 percent.
- [ ] Base interest is 15 percent.
- [ ] The seven base size/deadline pairs are exactly
  `110/10, 130/8, 165/7, 210/6, 250/6, 285/6, 300/5`.
- [ ] Meeting and manager rules match the Locked ledger.
- [ ] Managers do not repeat in one seven-floor run.
- [ ] Deadline Hawk evaluates the project after persistent modifiers and before
  applying its own size/deadline change.
- [ ] The first Weekend is not forced to the casino; Floor 3 is guaranteed and
  every other Weekend uses the ordinary 12.5 percent chance.
- [ ] Chad retains the Locked provisional compounding coefficients and never
  exceeds ten accumulated upgrades.
- [ ] Chad's detailed forecast shows his current stacks, upgrade count, and
  estimated next-workday progress range.

## Offers And Cards

- [ ] Each random slot uses 20 percent family weighting before explicit
  family-modifying effects.
- [ ] The ordinary roster contains exactly 50 cards.
- [ ] Every family contains four Common, three Uncommon, two Rare, and one
  Legendary card.
- [ ] After eligible Special checks fail, ordinary rarity converges on
  70 percent Common, 20 percent Uncommon, 9 percent Rare, and 1 percent
  Legendary.
- [ ] Legendary frequency is 1 percent per eligible ordinary random slot.
- [ ] Paid rerolls never show Legendary cards.
- [ ] Paid-reroll Common, Uncommon, and Rare results preserve the renormalized
  70/20/9 proportions.
- [ ] Free rerolls may show Legendary cards.
- [ ] Special cards appear in eligible initial, ordinary added-slot, and
  standard free or paid reroll generation at 0.2 percent per eligible slot.
- [ ] Special rolls check slots in display order and stop after the first
  success, so one generated window never contains multiple Specials.
- [ ] Special-pool eligibility, equal default weighting, same-morning
  preservation, and no-generic-pinning rules match the ledger.
- [ ] Card-created task windows, family guarantees, additional-card choices,
  and Campaign replacements never newly generate Special cards.
- [ ] No offer contains duplicate copies of one exact task.
- [ ] Cards can return on later workdays.
- [ ] Generated offers reroll exact duplicates of Pinned Tasks without
  consuming or hiding the pin.
- [ ] Pinned Tasks retain their source, modifiers, and expiration; equivalent
  pins merge while mechanically different variants remain separate.
- [ ] Every Common has exactly one short, automatic micro-effect; any unbounded
  card-local progression is explicitly documented.
- [ ] Common micro-effects never open an additional decision prompt.
- [ ] Direct progress, stress, cash, recovery, and relationships resolve on
  selection.
- [ ] Family XP and counters update after a complete play.
- [ ] Later same-morning plays see updated counters.
- [ ] Effects tied to workday, Clock Out, or a future day wait for that trigger.
- [ ] Independent `play twice` sources add one Replay each rather than
  multiplying total play count.
- [ ] Printed-effect copy branches cannot reuse a Source already in their
  active ancestry.
- [ ] Pilot Approved suppresses only its paired primary-card Replay's duplicate
  stress; child Complete Plays and other sources' Replays pay normally.
- [ ] A printed-Common Repository Fork target receives Clean Code and may start
  Automation, but never enters Automation's generated Common Coding pools.
- [ ] Comparison Shopping waits for the Night catalogs before opening its
  choice.
- [ ] Working Capital takes its reserve-cap choice in the morning and opens no
  Clock Out prompt.

## Resolution And Transitions

- [ ] Selection occurs once per workday and remains distinct from every card
  play it creates.
- [ ] Complete Plays, Replays, Complete Additional Plays, Printed-Effect
  Resolutions, and Assists grant only their documented components.
- [ ] A completed project does not interrupt the active Resolution Chain or
  workday; unresolved content continues unless burnout ends the run.
- [ ] The Natural Schedule is generated before task resolution and remains
  distinguishable from replacements, bonus entries, repeats, Triggered
  Schedule Entries, and Workday Events.
- [ ] The consolidated Schedule Desk revalidates guarantees before locking.
- [ ] Opening actions, core entries, ordinary bonus additions, Standard
  Procedures, immediate child triggers, and fixed Workday Events follow the
  documented order.
- [ ] Clock Out follows the documented recovery, progress, Chad, performance,
  cash, interest, debt, reserve, duration, and final-result order.
- [ ] Final-result priority is
  `burnout -> player completion -> Chad completion -> missed deadline`.
- [ ] Ordinary days, non-final project completions, and final victory use their
  distinct documented Night, Weekend, promotion, and next-floor routes.
- [ ] Night purchases remain available in any legal order until explicit
  finalization. Manual Lights Out and Home or Deal purchases lock each other
  out in both directions unless an explicit exception applies; Outings remain
  independent. Automatic sleep and Lights Out resolve only at finalization.
- [ ] Every headless simulation policy obeys the same Night purchase,
  Lights Out, exception, recovery, and finalization rules as a player.

## Coworker Activations

- [ ] Every non-Chad coworker begins each workday with one Standard Bonus
  Opportunity.
- [ ] Forced Bonus Activations ignore and do not consume that opportunity
  unless their source says otherwise.
- [ ] Overlapping activation-count rules use the highest applicable count
  unless a source explicitly says `additional`.
- [ ] Repeated meetings determine activation counts again while preserving
  ordinary once-per-day Standard limits.
- [ ] Activation strength multiplies every numerical component, including
  stress drawbacks, before floor scaling.
- [ ] Opening coworker events, Sponsor visits, Staff Check-Ins, scheduled
  meetings, and the normal visitor use the locked order.

## Traits

- [ ] Every completed ordinary task grants exactly 1 family XP.
- [ ] Milestones are claimed only at promotion.
- [ ] Earlier milestone effects remain unless explicitly replaced.
- [ ] Family XP and required counters continue above 10.
- [ ] The staged Promotion Claim Batch resolves all simultaneous candidates
  without family or click-order bias and activates only after confirmation.
- [ ] Only one capstone can be owned during a run.
- [ ] Codebase, Polish, Velocity, Focus, Reserve, stored-card, Contact, and
  Closing counters use the exact timing in the ledger.

## Sales Systems

- [ ] Pending Schmoozing slots remain optional and nonblocking, Inner Circle
  targets up to two legal Assist cards, and Portfolio Expansion uses its
  equal-tier-then-weighted-pool draw.
- [ ] Deal offers are weighted and distinct.
- [ ] Deal rerolls replace the complete three-Deal offer, exclude purchases,
  permit original-offer repeats, and expire at Lights Out exactly as Locked.
- [ ] Client Call uses listed Deal price and its 30-progress cap.
- [ ] Expense credit expires and cannot become ordinary cash.
- [ ] Contact-team choices persist and cannot be changed.
- [ ] Secondary tasks omit prohibited stress, effects, XP, and counters.
- [ ] Sales Cycle cards override all lower-priority offer systems.
- [ ] Cycle stress resolves before the player can Close.
- [ ] Close consumes the day.
- [ ] Actual Chain and reward Chain never drift.
- [ ] Unique Closing rewards leave all relevant pools.
- [ ] Seasoned stacks bank and pay out in the documented order.
- [ ] Chain 9 capstone and Anchor Account restrictions work.
- [ ] Brand Strategy matches the complete Locked Campaign sequences, Bonuses,
  offer rules, additional-play order, and capstone behavior.

## Operations Systems

- [ ] All ten Operations cards match the approved roster and no superseded
  Operations task effect remains active.
- [ ] Efficiency's Standard Procedures, positive-action bonuses, and capstone
  repetition match the Locked 3/6/10 path.
- [ ] Logistics uses one committed stored-task slot and applies the exact
  Turns Held, delivery-bonus, and replay rules from the ledger.
- [ ] Compound Interest calculates Reserve Levels, benefits, eligible
  principal, and the 15 percent base interest rate in the documented order.

## Card Behavior And UI Traceability

Every row requires an exact behavior test, a player-facing forecast before an
irreversible choice when relevant, readable resolution feedback, and a visible
armed state or expiration for delayed effects. Passive cards are not exempt:
their current condition or calculated value must be inspectable on the card,
its details, or the appropriate phase summary.

### Coding Cards

| Card | Required player-facing trace |
|---|---|
| README Update | Preview the current play and arm a visible next-workday non-Coding-primary `+2 progress` status. |
| Regression Tests | Show the pre-play printed-Common count and calculated stress reduction or recovery, including the 5-recovery cap. |
| Bug Triage | Show whether Chad currently satisfies the condition and include the conditional progress in the card preview. |
| Production Hotfix | Show whether two or fewer workdays remain and include the conditional progress in the card preview. |
| Version Control | Highlight eligible unselected tasks, confirm the target, then show its tomorrow pin, source, expiration, and pending Commit. |
| Build Script | Show the armed next-morning reroll; let the player target an offered or eligible pinned task; preserve rarity and visibly mark the replacement's `-2 base stress`. |
| API Integration | Show eligible other-family targets, redirected XP, and the selected family's next-workday bonus with its expiration. |
| Repository Fork | Open a completed non-Coding task picker, explain an empty pool, and show the resulting pin's temporary Coding conversion, Commit, and expiration. |
| Parallel Processing | Choose an eligible offered task, show its complete additional-play package and 10 percent positive-stress increase, and display the locked resolution order. |
| Hackathon | Reveal one task per family in one window; select exactly two, order them, preview their 50 percent positive stress, and confirm the complete play chain. |

### Management Cards

| Card | Required player-facing trace |
|---|---|
| One-on-One | Show whether its first successful coworker activation is pending or spent and identify the activation that granted progress. |
| Meeting Minutes | Show whether the first Team Meeting rider is pending or spent and identify the triggering meeting. |
| Action Plan | Show whether the first Work rider is pending or spent and identify the triggering Work action. |
| Capacity Planning | Show the final locked Schedule Entry count and whether the six-entry threshold succeeds before playback. |
| Meeting Prep | Mark the guaranteed meeting and any replacement it caused in the Schedule Desk with its source. |
| Staff Check-In | Open a coworker picker with exact current bonus packages, then show the bonus visit and Forced activation. |
| Schedule Adjustment | Let the player target an eligible Schedule Entry and show its rerolled action before final schedule confirmation. |
| Cross-Functional Sync | Choose exactly three coworkers with exact bonuses and show the added meeting, participants, and Forced activations. |
| Executive Review | Choose one eligible action type and show both opening bonus entries before the schedule locks. |
| War Room | Choose the bonus action, show its two resolutions, mark every eligible natural repeat, and mark guaranteed favorable Outcomes. |

### Design Cards

| Card | Required player-facing trace |
|---|---|
| Iteration Pass | Show its current card-specific base progress and the post-play increase in card details and history. |
| Reference Study | Show yesterday's primary family, whether the condition succeeds, and its resulting progress. |
| Accessibility Review | Show the current-stress condition and resulting recovery in the card preview. |
| White Space | Show the frozen comparison threshold after selection and its pending or resolved Clock Out status. |
| Prototype Test | Show one combined next-morning schedule chooser with every candidate and source count before the primary task choice. |
| Concept Selection | Provide one preserve-and-reroll pass per Effect Instance, clearly distinguishing preserved ordinary cards, eligible Specials, and rerolled slots. |
| User Testing | Reveal the combined exact Lunch candidates before playback and require one accepted Outcome. |
| Creative Breakthrough | Show conversion rate, included recovery sources, excluded sources, remaining workdays, and each overlapping instance. |
| Rapid Prototype | Highlight eligible visible Sources, visibly disable recursion and identity-bound targets, and preview the complete borrowed positive and negative text. |
| Design System | Open a distinct four-task source window with no rerolls, require one choice, and show every borrowed-effect instance and remaining workday. |

### Sales Cards

| Card | Required player-facing trace |
|---|---|
| Expense Allowance | Add the exact Expense Credit to the economy breakdown and Night Desk, with eligible uses and Lights Out expiration. |
| Referral Fee | Track distinct successful coworker activations up to three and itemize each Effect Instance's Clock Out payment. |
| Sales Quota | Show net workday progress toward 20 and the pending or earned Clock Out payment. |
| Cross-Sell | Mark paid Home, Deal, and Outing categories, pending rebate progress, and each instance's payout or expiration. |
| Client Entertainment | Choose a coworker with current relationship shown and mark the free 8-relationship Outing allowance in the Night Desk. |
| Comparison Shopping | After catalogs generate, choose one visible item, reveal exactly two eligible alternatives, and compare all three prices and effects in a compact window. |
| Commission Advance | Show the immediate cash, completion deadline, and pending 20 flat-stress consequence through tomorrow's Clock Out. |
| Corporate Expense Account | Show Expense Credit, the additional Home-or-Deal purchase, remaining uses, and Lights Out expiration. |
| Referral Network | Choose exactly three coworkers with exact doubled packages, then show the armed next-workday replacement and its consumption. |
| Net 30 Contract | Open the standard Deal Desk, identify the one financed Home or Deal choice, show final amount and due time, and keep debt visible until settlement. |

### Operations Cards

| Card | Required player-facing trace |
|---|---|
| Process Audit | Track distinct positive action types up to four and itemize the Clock Out progress. |
| Preventive Maintenance | Show its pending first-Slump conversion and identify the replacement Water Cooler and resulting triggers. |
| Priority Requisition | Show current Home-reroll eligibility and the exact task-reroll exchange before selection resolves. |
| Overnight Reserve | Show whether $250 was reserved, its unavailable status, return morning, and $100 profit. |
| Contingency Plan | Show the pending eligible Outcome reroll, both Outcomes when consumed, and any task reroll awarded. |
| Shift Handoff | Identify the captured natural positive action at Clock Out and show tomorrow's sourced bonus entry. |
| Accrual Accounting | Show qualifying cash spend, recorded value up to $500, affected next-workday Reserve and interest values, and expiration. |
| Working Capital | Require a `$500` or `$1,000` morning cap choice; show the final automatic reserve, unavailable cash, maturity, and generated Work actions. |
| Failover Protocol | Show the ordered Backup queue, each recorded action and Outcome, eligible harmful replacements, and consumption. |
| Perfect Execution | Mark the armed trigger, Slump conversions, generated child Work actions, and the total per-Work progress bonus from every replayed instance. |

## Trait And Exceptional-System UI Traceability

| Path or system | Required player-facing trace |
|---|---|
| Clean Code | Resume Book shows uncapped Codebase and Commit; every eligible printed-Common Coding card previews its exact scaled progress and stress. |
| Automation | Morning shows live Combo, next card and reroll costs, eligible Common Coding choices, free and paid rerolls, offer weighting state, milestone bursts, and reset timing. |
| Debugging | Show prior-day Coding eligibility, primary-task bonus XP, total family XP used by the daily conversion, and Production Ready's pending Replay. |
| Delegation | Promotion Review chooses permanent Delegates with exact bonuses; Resume and playback show doubled relationship gains, start contributions, Work alternation, meeting activations, and All Hands. |
| Agile | Resume and workday show uncapped Velocity, exact favorable chance, current meeting and Work progress, Daily Stand-Up, and Continuous Delivery child actions. |
| Leadership | Schedule Desk shows each optional Team Briefing, replacement or capstone bonus mode, bound target, repeat count, and invalid target reason. |
| Eye for Detail | Cards and Resume Book expose per-card Polish; Pinned Tasks show Revision or Masterpiece source, exact scaling, and permanence. |
| Moodboard | HUD and Resume show current Focus, cap, expiration or carryover, absorption, progress conversion, refresh, and automatic Lights Out; its automatic Lights Out does not block Home or Deal purchases. |
| Brand Strategy | Resume shows the separate questline, current Campaign and ordered step, multiplier and unlocked rewards; Morning shows the Campaign name, requested task and family, completed-step count, Campaigns completed, protected Campaign card, and final-capstone two-card selection. |
| Negotiation | Night Desk shows Deal weights through actual distinct offers, free reroll, purchase count, exact Client Call values, pay and interest modifiers, Scope eligibility, and capstone strength. |
| Schmoozing | Resume Book shows optional pending slots and eligible Contacts during every non-workday phase without blocking progression; morning previews each secondary Assist, specialty, Raj payment, Priya XP, cap, and up to two Inner Circle targets. |
| Closing | Morning marks the Hot Lead or fully replaces the offer with two Cycle cards and Close; Deal Ladder shows actual and reward Chain, exact next stress, Close tier, tokens, Seasoned stacks, and persistent rewards. |
| Efficiency | Promotion chooses Standard Procedures; Schedule Desk and playback mark their source, order, repeats, and exact positive-action progress. |
| Logistics | Morning shows the committed stored-task slot, Turns Held, current delivery bonus, eligibility, projected extra effects or plays, and irreversible store or deliver choice. |
| Compound Interest | Economy details show Accounted Cash, Reserve Levels, cap, per-level benefits, eligible principal, exact interest estimate, and Infinite Runway state. |
| Rebrand Initiative | The task is visibly Special, explains Campaign replacement, ordered completion, and powerful rewards, leaves the Special pool after unlock, grants no family XP by Special-card rules, and opens Brand Strategy exactly once. |
| Campaign tasks | Use a Campaign label, displayed family and Bonus, current multiplier, step-completion reward, Hot Lead state, Management reward picker, and final-capstone additional-play eligibility without presenting a false ordinary rarity. |
| Sales Cycle cards and Close | Show family-derived Cycle identity, 10 progress, exact floor-scaled Cycle stress after modifiers, no family XP, reward preview rules, Close-day consequences, and burnout risk before confirmation. |

## Deal And Closing-Reward UI Traceability

| Deal or reward | Required player-facing trace |
|---|---|
| Wellness Stipend | Show current recoverable stress, actual recovery, Focus interaction, listed price, and Client Call value. |
| Conference Pass | Open a coworker picker with current relationship, Delegate doubling, normal or capstone gain, price, and Client Call value. |
| Market Intelligence | Open the five-family picker and show one or two guaranteed slots, duration, price, and Client Call value. |
| Success Fee | Show the next-workday completion condition, normal or capstone payout, project-completion-night exclusion, price, and Client Call value. |
| Escalation Coverage | Show charges gained versus the cap, exact eligible harmful effects, automatic consumption, price, and Client Call value. |
| Productivity License | Show tomorrow's Work guarantee, normal or capstone per-Work bonus, duration, price, and Client Call value. |
| Contractor Support | Show the two or four sourced bonus Work entries, duration, price, and Client Call value. |
| Facilitated Workshop | Show the one or two sourced favorable Team Meetings, duration, price, and Client Call value. |
| Scope Renegotiation | Show once-per-floor eligibility, project-completion-night exclusion, revised workdays, fixed non-doubled effect, price, and Client Call value. |
| Follow-Up | Show the next-morning free task reroll and expiration. |
| Account Notes | Choose only a family represented in the closed Cycle and preview its XP. |
| Warm Introduction | Choose a non-Chad coworker and preview the floor-scaled relationship gain. |
| Post-Call Reset | Preview the floor-scaled immediate recovery and Focus interaction. |
| Clean CRM | Add a persistent reward tag and update every future Cycle card's exact stress preview. |
| Qualified Referral | Choose a represented family and show tomorrow's guaranteed-family Hot Lead slot. |
| Internal Champion | Choose a coworker, preview relationship, show Champion tokens and cap, and expose legal top-level Close rerolls only after Close freezes. |
| Discovery Complete | Reveal the complete current Close presentation before confirmation and clearly show that continuing discards and rerolls it. |
| Objection Handling | Show charges and cap, offer an optional pre-Cycle-card spend control, and update exact next stress before confirmation. |
| Preferred Account | Distinguish actual Chain from reward Chain, show its initial nested Nurturing reward, and never grant virtual Seasoned stacks. |
| Pilot Approved | Show the next-ordinary-primary Replay, paired stress exemption, wait condition, and consumption. |
| Executive Sponsor | Choose a coworker with the exact relationship gain and Chain-multiplied bonus package, then show both dated visits. |
| Case Study | Choose from completed ordinary tasks and show two independently expiring pins with rarity and source. |
| Launch Support | Show one sourced Work action on each of the next two workdays and decrement only on actual workdays. |
| Seasoned Closer | Show persistent status, current pending stacks from actual Chain, banked stacks, Close payout, and post-Cycle recovery. |
| Portfolio Expansion | Show the equal Nurturing-or-Qualifying tier roll followed by that tier's eligible weighted result, then future distinct two-reward presentations and the required choice. |
| Joint Venture | Show immediate progress, persistent Chad-share status, and each attributed gain in the workday or Clock Out summary. |
| Master Services Agreement | Show revised current and future project size and deadline rules in project details. |
| Executive Air Cover | Show manager immunity, converted harmful events, automatic Executive Support, and exact random support Outcome. |
| Burnout Insurance | Show permanent Clock Out recovery separately from its one-use Guardian Angel and remove only the consumed Angel. |
| Key Account Status | Show actual Chain 4 at every Cycle start, immediate Close eligibility, first-card Chain 5, and pending Seasoned stack when applicable. |
| Anchor Account | At eligible actual Chain 9, show it beside random rewards, require a family choice, preview immediate and future XP, and explain that choosing it forfeits other options. |
| Enterprise Dividend | After all five Enterprise rewards are owned, show its two rounded current-state values before resolving the automatic reward. |

## Resource And Phase UI Impact Matrix

| Surface | Required coverage |
|---|---|
| Morning Task Desk | Generated offer, Pinned drawer, no duplicate identities, rarity and Special or Campaign labels, final task forecasts, reroll source and cost, targeted effects, multi-card order, Assists, stored task, Hot Lead, Sales Cycle, and Close. |
| Schedule Desk | Candidate schedule choice, automatic guarantees, replacements, bonus entries, Team Briefings, repeats, accepted Outcomes, participant choices, source badges, and final locked count in one consolidated flow. |
| Workday playback | Natural, replacement, bonus, repeated, and Triggered actions; fixed Workday Events; Standard and Forced coworker activations; source and Outcome feedback synchronized to the action as it settles; deterministic 1x, 2x, 4x, and Skip. |
| Clock Out summary | Recovery and conversion, progress, Chad and Joint Venture, performance conditions, pay, interest, debt stress, returned and new reserves, duration changes, and final-result priority in exact order. |
| Night Desk | Home, Deal, and Outing actions in any legal order; spendable cash, Expense Credit, discounts, financing, rebates, purchase limits, family and item pickers, the two-way manual Lights Out purchase lock and exceptions, unused-resource warnings, sleep, and explicit finalization. |
| Weekend | Exact event choices and outcomes, Hackathon study family picker, Networking Brunch coworker picker, Focus and Guardian Angel handling, and due promotion route. |
| Promotion Review | Five-family rail, exact XP, path and milestone choices, Delegates, Contacts, Standard Procedures, Masterpiece, simultaneous capstones, losing consequences, revision, and one final batch confirmation. |
| Resume rail and Book | Exact XP over 10; paths and capstone; Codebase, Commit, per-card Polish and completion history, Velocity, Focus, Delegates, Contacts, Procedures, stored task, Reserve state, Campaigns, Deal Ladder, Seasoned stacks, and persistent Closing rewards. |
| Coworker views and pickers | Relationship, exact complete bonus including stress drawbacks, concise bonus tooltips without redundant scaling labels, Workday-meeting explanation, Standard opportunity state when relevant, Delegate and Contact flags, specialty or multiplier preview, selection limits, and pending visits or Networks. |
| Economy breakdown | Spendable cash, Expense Credit, Overnight Reserve, Working Capital, Accrual value, Net 30 debt, Reserve Levels, eligible principal, estimated interest, and relevant return or due times. |
| Active-effect strip | Guardian Angel, Escalation and Objection charges, task, Home, and Deal rerolls, delayed card effects, pins, guarantees, Sponsor visits, Commission deadline, Client Calls, Campaign and Cycle modifiers, and every duration or stack that can change the next decision. |
| Logs and Help | Plain-language Resolution Glossary, source-attributed values, no obsolete Resume terms, and enough history to explain every generated play, repeat, copy, activation, action, payment, and status consumption. |

## UI And Office

- [ ] Every row in the card, trait, reward, resource, and phase UI impact
  matrices has a reachable, readable, keyboard- and tap-usable implementation.
- [ ] No unavoidable choice opens during AFK workday playback or Clock Out.
  Every choice occurs at the Morning Task Desk, Schedule Desk, Night Desk,
  Weekend, or Promotion Review.
- [ ] No named counter, charge, token, reserve, debt, delayed effect,
  expiration, modifier, or irreversible choice exists only in hidden state.
- [ ] The top-center project title contains the player's green progress fill
  and exact current/required value under a fixed dark readability overlay.
- [ ] Project progress changes briefly pulse without shifting layout, and
  reduced motion disables that pulse.
- [ ] The bottom-left player portrait has one readable health-style Stress bar
  and no duplicate project-progress bar.
- [ ] Chad and workdays remain readable at top-right.
- [ ] Manager and Today controls fit at top-left.
- [ ] Manager hover, focus, and activation expose the complete current modifier
  while preserving the required two-line compact label.
- [ ] Today uses the correct preselection, ordinary, Campaign, Sales Cycle,
  Close, Night, Weekend, and Promotion state without stale task information.
- [ ] Spendable cash remains prominent; the economy breakdown reports temporary
  credit, reserves, Working Capital, debt, and estimated interest accurately.
- [ ] Home inventory is readable outside Night but cannot make purchases.
- [ ] Resume rail has five readable family sections.
- [ ] XP segments and milestone markers communicate the next gate.
- [ ] Closing uses the Deal Ladder instead of visible Sales XP segments.
- [ ] HUD compacts only during workday playback.
- [ ] Help, speed, and Skip controls appear only during workday playback and
  remain usable in compact layouts.
- [ ] `1x`, `2x`, `4x`, and Skip produce identical seeded outcomes and the
  selected non-Skip speed persists between workdays.
- [ ] The active-effect strip reports Focus, Guardian Angel, Escalation charges,
  delayed effects, and durations without obscuring the office.
- [ ] Chad's HUD opens a keyboard- and pointer-accessible detailed forecast
  matching simulation values.
- [ ] Exactly eight indexed cubicles remain.
- [ ] Conversation adjacency blocking still works.
- [ ] Team Meetings wait for conversations and display one bubble at a time.
- [ ] Water cooler, office routes, and active actions remain visible.
- [ ] Portrait phone view shows the rotation gate.
- [ ] Landscape phone view remains playable.
- [ ] Reduced motion removes nonessential movement.

## Boundary, Failure, And Lifecycle Checks

- [ ] Exact-threshold cases are covered: 0 and 100 stress, exact project size,
  last workday, exact cash price, relationship 20, XP 3/6/10, Focus and charge
  caps, Combo milestones, and actual Chains 0/1/4/5/6/8/9.
- [ ] Empty or restricted target pools never softlock the run. The UI explains
  why no target is legal and follows the ledger's no-target behavior.
- [ ] Insufficient cash, Expense Credit, reserve funds, financing, and debt
  settlement cannot spend the same value twice or produce negative hidden
  balances.
- [ ] Simultaneous completion, burnout, capstone candidacy, coworker
  activations, replays, copies, delayed effects, and reward choices use their
  documented atomic boundary and priority.
- [ ] Replays and overlapping Effect Instances preserve source identity,
  duration, creation order, and independent expiration through promotions and
  Weekends.
- [ ] Sales Cycle, Campaign, pins, next-morning effects, next-workday effects,
  and current-project effects survive, pause, trigger, or expire correctly at
  every transition.
- [ ] Project-completion Night excludes only ineligible project-only purchases;
  final-floor completion bypasses Night and proceeds directly to victory.
- [ ] Starting a new run after victory, burnout, rival completion, or deadline
  loss clears every run-local state, modal, timer, animation, and event
  listener while retaining only intended settings such as playback speed.
- [ ] Rapid repeated inputs, disabled controls, double clicks, and Skip during
  active resolution cannot duplicate choices, purchases, rewards, or phase
  transitions.
- [ ] Long Automation, replay, Logistics, action-trigger, and Closing chains
  finish without recursion failure, frozen controls, runaway animation time,
  or materially growing memory.

## Accessibility Evidence

- [ ] Every control is a semantic button, input, menu, tab, or equivalent with
  an accessible name and visible keyboard focus.
- [ ] Every modal or picker moves focus inside, traps it while open when
  appropriate, returns focus on close, and has a clear legal dismissal rule.
- [ ] Hover-only details are also available through keyboard focus and tap.
- [ ] Family, rarity, status, favorable or unfavorable Outcome, and bar state
  never rely on color alone.
- [ ] Text and essential UI meet readable contrast at every documented state.
- [ ] Dynamic choices, phase changes, errors, and resolved rewards are exposed
  to assistive technology without announcing decorative workday motion.
- [ ] Zoom and text scaling do not clip controls, hide effect text, or prevent
  completion of a choice.

## Browser Matrix

- [ ] 1440 x 900 desktop.
- [ ] 1024 x 768 compact desktop.
- [ ] Representative short landscape phone viewport.
- [ ] Representative portrait phone viewport.
- [ ] Keyboard-only navigation.
- [ ] Hover, focus, and tap tooltip access.
- [ ] Task, Deal, Home, Promotion, Campaign, and Closing-reward text remains
  readable without overlap at every browser-matrix viewport.

## Simulation Report

For each batch, record:

- game version or hash;
- number of runs;
- random seed range;
- player policy;
- win rate;
- floor reached;
- loss causes;
- average and percentile stress;
- average project and rival margins;
- card and trait pick rates;
- capstone frequency;
- economy totals;
- Legendary appearance rate; and
- known model limitations.

Do not tune toward the 25-35 percent target until all active card and trait
effects are implemented accurately.
