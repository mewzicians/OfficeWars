# OfficeWars Balance Ledger

Last updated: 2026-08-06

## Status Rules

- **Implemented Baseline** describes what the HTML does now.
- **Locked** contains explicit user decisions that are not necessarily coded.
- **Draft** contains proposals awaiting approval.
- **Open Questions** lists decisions still needed.

An answered choice locks only that choice. Silence, dismissal, or an expired
question does not approve its recommended default.

Rejected and superseded history is indexed in `ARCHIVE_SUPERSEDED.md` and kept
out of this active ledger.

## Implemented Baseline

The real HTML now contains the approved overhaul candidate:

- the Locked core balance, rank curve, meetings, managers, Weekend rules, and
  Chad cap;
- the exact 50-card fixed-rarity roster with equal family weighting, Special
  generation, Pinned Tasks, and shared resolution primitives;
- uncapped family XP, promotion claims, every ordinary trait path, the
  run-wide capstone owner, and coworker activation ordering;
- Brand Strategy, Deal Desk, Schmoozing Contacts, Closing and its reward
  tables, Logistics storage, Standard Procedures, and named resources;
- centralized Home effects with inert set metadata hooks;
- legacy Library, Hackathon, and Networking Brunch replacements; and
- the real HUD, Resume Book, deterministic 1x/2x/4x/Skip playback, landscape
  phone layout, portrait rotation gate, and eight-cubicle office.

Current core values are floor stress scaling 20 percent, automatic sleep 4
percent, Lights Out 5 percent, promotion recovery 25 percent, interest 15
percent, five base workday actions, and rank pairs
`110/10, 130/8, 165/7, 210/6, 250/6, 285/6, 300/5`.

The current HTML has SHA-256
`A33645E9CC7F1A9F8CC6BD7A700377875D45825F4A8CD8FC5A40B2A7C154197A`.
Skip uses the locked-workday continuation resolver rather than accelerating
presentation timers, so stalled ambient conversations, walking, or desk-visit
presentation cannot block the remaining deterministic resolution.

### Implementation Verification For The 2026-08-06 Snapshot

Checked on 2026-08-06:

- `officewarsautobattler.html` has SHA-256
  `2A4880220763678436C6BDFA043EAD7777BB71F01547F8B17B047768206C1D78`.
- The overhaul smoke suite covers deterministic playback, seeded run
  termination, distributions, phase routes, advanced systems, runtime
  structure, and accessibility basics. Its fixed accessibility delays were
  replaced with state-based waits; the updated harness passed four consecutive
  post-fix runs.
- The seven-case visual matrix reports no overflow or persistent-HUD overlap
  at desktop, compact desktop, landscape phone, portrait rotation, Workday,
  Morning, and Night states.
- The first full bidirectional verification is recorded in
  `verification/FULL_VERIFICATION_2026-08-06.md`. Its implementation and
  readability findings F1-F4 are resolved and passed the focused retest in
  `verification/BLOCKERS_1_4_RETEST_2026-08-06.md`.
- All eight targeted high-risk interaction groups passed deterministic runtime
  fixtures in
  `verification/ADVANCED_INTERACTION_VERIFICATION_2026-08-06.md`: maximal
  schedule ordering, Clock Out economy, coworker ordering, repeated meetings,
  promotion batches, all 14 ordinary trait paths, advanced-system lifecycles,
  and worst-case resolution chains.
- F5 remains open: the scripted-skilled policy won 55.3 percent against the
  25-35 percent target. The advanced suite found no rules defect, but its
  121-resolution, 2,403-progress action chain is a serious balance and
  readability watchpoint.
- The same audit completed 3,000 seeded runs without simulation errors:
  baseline won 0.7 percent, random won 12.2 percent, and scripted-skilled won
  55.3 percent. `Regression Tests` was the skilled policy's largest selection
  outlier and remains a watchpoint rather than an automatic nerf.
- Final implementation signoff, the full structural simulation matrix, and
  balance tuning remain pending. UI and accessibility rows not exercised by
  the targeted advanced suite retain their existing verification status.
- The historical UI prototype, old handoffs, and pre-cleanup full ledger are
  intentionally omitted from the public development snapshot.
- This `docs/BALANCE_LEDGER.md` remains the current decision-status source.

## Locked

### Core Balance Direction

- Set floor stress scaling to 20%.
- Set automatic sleep to 4%.
- Keep Lights Out base recovery at 5%.
- Set non-final promotion recovery to 25%.
- Set the base interest rate to 15%.
- Make Comfy Mattress additive: +2% automatic sleep, for 6% total at the new
  base.
- Balance toward an approximately 25-35 percent skilled-player win rate.

### Meeting Outcomes

- The first favorable Team Meeting on a floor adds one workday to the
  deadline. A floor can gain at most one workday this way.
- After that extension has been used, a favorable first Team Meeting of a
  workday grants 5 project progress instead.
- An unfavorable first meeting removes 5 project progress instead of removing a
  deadline day.
- Every later Team Meeting that workday recovers 10 stress when favorable or
  generates 10 base stress before floor scaling when unfavorable.

### Manager Selection

- Shuffle all eight managers once per run and use seven without replacement.

### Manager Balance

- Toxic Positivity gives every Office Chat a fixed 60 percent unfavorable
  chance and retains its 5 additional Lights Out recovery.
- The Slave-driver adds 1 raw daily stress before floor scaling and retains its
  $50 additional daily pay.
- Apply persistent project-size and deadline modifiers before Deadline Hawk.
  If the resulting pre-Hawk deadline is at least five workdays, remove one
  workday and reduce required project progress by
  `ceil(pre-Hawk size / pre-Hawk deadline)`.

### Weekend Events

- Do not force the first Weekend of a run to be a casino visit.
- Guarantee one casino visit on Floor 3. On every other Weekend, use the
  ordinary 12.5 percent casino chance.

### Structural Baseline Decisions

- Use the complete rank size/deadline curve
  `110/10, 130/8, 165/7, 210/6, 250/6, 285/6, 300/5`.
- Preserve Chad's current run-wide compounding model for the initial simulation
  baseline: a 50 percent daily stack chance, one upgrade every three run-wide
  workdays, 1.2 progress per Work slot for each upgrade, the current
  floor-based quality and bad-day coefficients, Work-slot progression, quality
  wobble, and 1.15 boss-floor multiplier.
- Cap Chad at 10 accumulated upgrades. His stacks remain uncapped.
- Show Chad's current stacks, accumulated upgrades, and estimated next-workday
  progress range in his detailed forecast. Keep the persistent HUD summary
  compact.
- Treat Chad's coefficients as simulation-tunable values rather than changing
  them before the approved cards and traits are implemented accurately.

### Task Roster Review Direction

- The complete 50-card ordinary family roster is approved below. Prior task
  tables are superseded and belong only in `ARCHIVE_SUPERSEDED.md` or its
  indexed historical snapshots.
- Judge every card on three separate qualities: useful standalone
  power, recognizable family expression, and a higher conditional synergy
  ceiling.
- Make task offers create real tension between immediate card value, current
  build interactions, and progress toward a family trait breakpoint.
- Preserve equal 20 percent family weighting. The roster should make players
  adapt to what they are offered rather than reliably chase the same family
  every run.
- Give every Common card exactly one short, automatic micro-effect so each
  Common can become preferable in a specific situation. Keep it bounded unless
  a card-local progression exception is explicitly approved. Commons are no
  longer stat-only.
- Keep Coding the most internally synergistic and comparatively selfish family,
  but redesign it so its higher-rarity cards are not a closed Coding-only
  ecosystem and retain meaningful standalone or cross-family splash value.

### Task Resolution Timing

#### Resolution Glossary

| Term | Locked meaning |
|---|---|
| `Selection` | The player confirms the morning primary task. It occurs once per workday and is the only event that satisfies selection and primary-only triggers. |
| `Complete Play` | Resolve a card's base project progress, base stress, complete printed effect, family XP, card-progression counters, and card-play triggers. Every card play is complete by default. |
| `Replay` | Another Complete Play of the same card. It does not repeat Selection or satisfy primary-only triggers. |
| `Complete Additional Play` | A Complete Play of another card without making it the primary task. It does not repeat Selection or satisfy primary-only triggers. |
| `Printed-Effect Resolution` | Resolve only copied rules text. It is not a card play and grants none of the copied card's base values, progression, completion counters, or card-play triggers. |
| `Assist` | Schmoozing's calculated secondary-task contribution. It is neither a card play nor a Printed-Effect Resolution. |
| `Schedule Entry` | One action placed on the workday timeline. Adding, replacing, and resolving it are separate events. |
| `Natural Schedule Entry` | A Schedule Entry produced by the base workday generator before task, trait, Deal, and other post-selection changes. Extra base slots from Espresso and required boss-floor hostile injections are generated as part of the Natural Schedule. |
| `Action Resolution` | Execute one Schedule Entry once, produce or accept one Outcome, and apply every applicable action trigger. Repeating an action creates another Action Resolution rather than another Schedule Entry. |
| `Triggered Schedule Entry` | A temporary bonus Schedule Entry created during playback by an Action Resolution or Workday Event. It resolves immediately after its parent and receives normal action triggers, but it was not part of the locked schedule. |
| `Workday Event` | A timed workday occurrence that is not a Schedule Entry or Action Resolution, including desk visits, sabotage, passive manager ticks, Delegation contributions, and Executive Sponsor visits. |
| `Outcome` | The favorable, unfavorable, or deterministic result produced by an action. Selecting, guaranteeing, rerolling, or reusing it does not by itself repeat the action. |
| `Flat Stress` | Positive stress applied without floor scaling or numerical stress modifiers. Focus may absorb it, and Guardian Angel may prevent burnout after that absorption. |
| `Coworker Bonus Activation` | Apply one coworker's current relationship-scaled bonus once. `Trigger twice` creates two activations; `doubled strength` creates one activation with doubled numerical values. |
| `Standard Bonus Opportunity` | Each non-Chad coworker begins every workday with one. A normal Team Meeting or normal daily desk visit may spend it to create one Coworker Bonus Activation. |
| `Forced Bonus Activation` | An activation explicitly created by a card, trait, or reward. It ignores and does not consume the coworker's Standard Bonus Opportunity unless its source says otherwise. |
| `Effect Instance` | One independently tracked copy of an armed effect, including its source, duration, modifiers, and expiration. Each play creates a separate instance unless the effect explicitly merges, replaces, or upgrades an existing instance. |
| `Source` | The card or system that owns an effect's original rules text. |
| `Host` | The card currently resolving a copied printed effect. In copied text, `this card` refers to the Host. Explicitly named card progression remains bound to the named Source card and does not transfer to the Host. |
| `Modifier` | A rule that changes an upcoming play, printed-effect resolution, schedule entry, outcome, or value without becoming a separate resolution. |
| `Resolution Chain` | The ordered sequence created by one morning selection and every card play or effect it generates. Finish each play before starting the next. |

- Apply every selected task card's direct gains and losses immediately when its
  selection is confirmed rather than projecting them until Clock Out.
- Treat selecting the morning primary task as a separate event from playing a
  card. It occurs once and is the only event that satisfies selection and
  primary-only triggers.
- Make every card play a `Complete Play` by default. A Complete Play resolves
  the card's base project progress, base stress, complete printed effect,
  family XP, card-progression counters, and card-play triggers.
- A replay is another Complete Play of the same card. A complete additional
  play is a Complete Play of another card. Neither repeats the morning
  selection, satisfies a primary-only trigger, starts another Automation
  Combo, or advances another Brand Strategy Campaign step.
- Each independent source that says to play a card twice adds exactly one
  Replay. Multiple sources stack additively: the original play plus two such
  sources produces three total plays rather than four.
- Resolving a copied printed effect is not a card play. It grants no base
  progress, base stress, family XP, Polish, Codebase, completion counters, or
  card-play triggers unless the copying effect explicitly says otherwise.
  References to `this card` use the Host, while explicitly named card-local
  progression remains bound to its Source and cannot be transferred by a copy.
- A Printed-Effect Resolution may resolve another copy effect. Track the active
  Source ancestry for that copy branch. A Source already present in the branch
  is ineligible: reroll it in a generated copy-source window or disable it as a
  visible target. This preserves nested copy interactions without recursion.
- A card whose complete printed effect is explicitly identity-bound cannot be
  selected as a copy Source. `Iteration Pass` is the only current
  identity-bound ordinary card.
- A Schmoozing Assist is not a card play or printed-effect resolution. It
  grants only the contribution explicitly defined by Schmoozing.
- This includes base and printed immediate project progress, task stress,
  recovery, cash, relationship changes, and similar direct numeric effects.
- Resolve one card play's complete immediate package atomically. Combine its
  stress gains and recovery using their normal scaling rules, apply the final
  result, and check for burnout only after the package is complete.
- After each full card play resolves, immediately grant its family XP and
  update Codebase, Polish, and any other task-completion progression counters.
  The resolving card uses the pre-play counter values, while later cards played
  during the same morning use the updated values.
- An effect explicitly tied to a workday action, Clock Out, or a future day
  remains armed on selection and resolves at its stated trigger.
- Within one generated play chain, the same card cannot resolve more than once
  unless an effect explicitly says to replay it or play it twice.
- Reaching the current project's required progress marks it complete but does
  not stop the Resolution Chain. Every remaining play still resolves for its
  effects and progression, and promotion waits until after the workday.
- If stress reaches 100 percent and no effect prevents burnout, end the run and
  discard every unresolved play, effect, and choice remaining in the current
  Resolution Chain.

#### Workday Schedule And Playback

Build and resolve each workday in this order:

1. Generate and tag the hidden Natural Schedule, including Espresso's extra
   base slot and any required boss-floor hostile injection.
2. If Prototype Test is active, reveal its combined candidate schedules and
   let the player select one Natural Schedule.
3. Confirm the primary task and finish its complete Resolution Chain.
4. Apply automatic schedule guarantees, conversions, and bonus additions.
5. Resolve every player-controlled schedule choice in one consolidated
   Schedule Desk.
6. Revalidate guarantees, bind Team Briefings to their targets, and lock the
   Schedule Entries. Capacity Planning and every other schedule-count effect
   use this final locked count.
7. Attach repeats and accepted outcome choices, then begin deterministic
   playback.

- Place opening actions, including Daily Stand-Up and Executive Review, first.
  Follow them with the natural or replacement core schedule, ordinary bonus
  additions in source-resolution order, and Standard Procedures last.
- Insert each bonus Team Briefing immediately before its bound target.
  Triggered Schedule Entries resolve immediately after their parent Action
  Resolution or Workday Event.
- Schedule guarantees remain true when the Schedule Desk locks. A later choice
  cannot leave a guaranteed action absent.
- Adding an action creates a new bonus Schedule Entry with fresh participants
  and a fresh Outcome unless its source specifies participants or an Outcome.
  Replacing an entry keeps its timeline position but creates a non-natural
  entry.
- A runtime conversion changes only the current Action Resolution. It preserves
  the Schedule Entry's position and natural origin. Repeating an entry creates
  another Action Resolution with the same assigned participants and a fresh
  Outcome; it does not create another Schedule Entry.
- Outcome rerolls inspect only the accepted Outcome and replace that result.
  They do not repeat the action.
- Workday Events use fixed timeline anchors so normal, double-speed, and skipped
  playback have identical order and outcomes. They do not count for Capacity
  Planning, Process Audit, or Efficiency unless an effect explicitly converts
  the event into an action.
- Triggered Schedule Entries receive normal action and trait triggers but do
  not retroactively count for Capacity Planning. Process Audit and Efficiency
  evaluate their Action Resolutions normally.
- Repeated Team Meetings retain their assigned participants, roll fresh
  Outcomes, and advance normal meeting and Velocity tracking on every
  resolution. Ordinary once-per-day coworker bonus limits remain in force
  unless an effect explicitly overrides them.
- Resolve each Action Resolution as one atomic package before checking for
  burnout. If no effect prevents burnout, discard its unresolved child
  triggers, repeats, later Schedule Entries, and later Workday Events.
- Resolve each Workday Event and every Coworker Bonus Activation it generates
  as one atomic package under the same burnout rule.
- Reaching the required project progress does not interrupt playback. Promotion
  waits until the workday and its Clock Out effects finish.

#### Clock Out And Economy Resolution

- Before the morning task choice, record the project's starting progress for
  effects that measure net progress gained that workday.
- After the complete morning Resolution Chain and every morning cash gain,
  purchase, and cost finish, snapshot `Accounted Cash` as spendable cash plus
  active Working Capital plus eligible Accrual Accounting value.
- Calculate Reserve Levels from Accounted Cash at that time. Lock the
  workday's interest-eligible principal from the same snapshot after applying
  the current interest cap. Cash earned after the snapshot begins earning
  interest on the following workday.
- Resolve Clock Out in this order:
  1. Freeze the completed workday's action history and pre-Clock-Out stress.
  2. Resolve Clock-Out recovery and project-progress Effect Instances in
     creation order. White Space compares against the frozen stress value.
     Apply recovery conversions such as Creative Breakthrough as that recovery
     resolves.
  3. Apply Chad's final workday progress after all of his modifiers, then apply
     Joint Venture to that final gain.
  4. Determine the player's final net project-progress gain for the workday,
     then evaluate Sales Quota, Success Fee, Commission Advance, and other
     completion or performance conditions.
  5. Return matured Working Capital, grant ordinary pay and all earned cash
     rewards, then grant interest calculated from the locked morning
     principal.
  6. Aggregate every Net 30 balance due, automatically pay as much as possible
     from spendable cash, and generate flat stress equal to
     `ceil(total unpaid balance / 25)`. Apply that stress together with any
     Commission Advance penalty. Focus absorbs the combined final stress
     before Guardian Angel and burnout are checked.
  7. If the run continues, resolve new Overnight Reserve and Working Capital
     Effect Instances in card-play order.
  8. Increment Turns Held, expire or advance durations, consume the workday,
     and evaluate the final result.
- Mandatory debts always resolve before new reserves. Expense Credit,
  Accounted Cash adjustments, and reserved cash that has not matured are not
  spendable and cannot pay Net 30 balances.
- Calculate interest as
  `eligible principal * 15% * applicable manager multiplier * Negotiation multiplier`
  and round once to the nearest dollar after every multiplier. Determine the
  eligible principal by applying the current interest cap to Accounted Cash;
  Infinite Runway removes that cap.
- After a Net 30 penalty is determined and applied, clear its unpaid balance.
  The shortfall becomes stress rather than persistent debt.
- Use final net project progress rather than gross positive gains for Sales
  Quota. Clock-Out progress and Joint Venture count toward that net result.
- Apply the final result priority
  `burnout -> player completion -> Chad completion -> missed deadline`.
  Player completion therefore wins a same-workday project race, but burnout
  still defeats a completed project.
- A surviving non-final project-completion day proceeds to Night before
  promotion. Winning the floor does not discard Expense Credit, Outings, Deal
  access, or other effects assigned to that night.
- Success Fee and Scope Renegotiation are ineligible on a project-completion
  night because they can affect only the already-completed project. Exclude
  them before generating Deal offers and disable Scope Renegotiation's direct
  purchase control.
- Beating the final floor proceeds directly to victory without a Night phase.

#### Night, Weekend, Promotion, And Carryover

Route each surviving workday through exactly one of these sequences:

- Ordinary day:
  `Clock Out -> Night -> Weekend if due -> next morning`.
- Non-final project completion:
  `Clock Out -> Night -> promotion recovery -> Weekend if due -> promotion trait claims -> next floor`.
- Final project completion:
  `Clock Out -> victory`.

- Lock a successful floor result at Clock Out. Chad and the deadline cannot
  overturn it during Night, the Weekend, or promotion, although later burnout
  can still end the run.
- Apply the locked 25 percent non-final promotion recovery before a due
  Weekend. Claim newly reached trait milestones only after the Weekend, then
  create the next floor's project, deadline, manager, and floor-local state.
- On an ordinary non-completion Weekend, return to the next morning on the
  current floor rather than entering promotion.
- Already-active Moodboard generates Focus from actual automatic-sleep,
  Lights Out, promotion, and Weekend recovery. Creative Breakthrough retains
  its explicit exclusion of those sources.
- Resolve one Weekend outcome as an atomic package. Focus absorbs its final
  harmful stress before Guardian Angel and burnout are checked. Burnout ends
  the run before promotion trait claims.
- Traits claimed after the Weekend cannot retroactively modify that Night,
  promotion recovery, or Weekend.

Use one flexible `Night Desk`:

1. Generate the night's Home and Deal catalogs and initialize every purchase,
   Outing, Expense Credit, discount, and financing allowance.
2. Let the player take available Outings and make eligible Home and Deal
   purchases in any order. Selecting a Home card does not automatically end
   Night.
3. Spend Expense Credit before ordinary cash on every eligible payment.
4. For Cross-Sell, a category counts when at least some cash or Expense Credit
   is actually paid toward Home, Deals, or Outings. Free and fully financed
   transactions do not count. Each Cross-Sell Effect Instance pays its rebate
   immediately after its second distinct category and that cash may fund later
   purchases the same night.
5. Accrual Accounting records only ordinary cash actually paid after
   discounts. Expense Credit, financing, free purchases, and rebates do not
   increase its recorded spending.
6. End Night only through an explicit finalization. Warn about unused
   purchases, Outings, or Expense Credit but allow the player to continue.
7. On confirmation, expire night-only effects and unspent Expense Credit,
   apply automatic sleep, then apply Lights Out when selected or granted, and
   advance to the appropriate Weekend, promotion, or morning.

- A newly purchased Home upgrade or move applies immediately, including to
  automatic sleep and Lights Out during that same Night.
- Every repeated Night-card effect remains a separate Effect Instance.
  Resource grants, credits, rebates, and explicitly additional purchases
  stack. An instance does not bypass the normal Home, Deal, or Outing limit
  unless its text explicitly grants an additional action, purchase, or Outing;
  an instance that cannot be used expires at its stated time.

Interpret duration wording consistently:

| Wording | Locked duration |
|---|---|
| `Tonight` | Expires when that Night finalizes. |
| `Next morning` or `tomorrow morning` | Applies to the next morning task window across Weekends and promotions. A Sales Cycle override still consumes that morning unless the source explicitly waits. |
| `Next workday` or `tomorrow's workday` | Follows the player across Weekends and promotions and triggers on the next actual workday. |
| `Next ordinary primary task` | Waits through Sales Cycle cards, Close days, and any other workday without an ordinary primary task. |
| `For N workdays` | Counts actual workdays, including a Close workday with no primary task. |
| `Current project` or `current floor` | Expires when that project or floor ends unless its source explicitly creates a future-floor effect. |
| `Persistent` | Carries until its source explicitly consumes, replaces, or removes it. |

- Calendar transitions alone never consume a morning- or workday-scoped
  duration.
- Unless its source explicitly snapshots a value, a delayed numerical effect
  uses the floor, relationship values, traits, and applicable manager active
  when it resolves. An explicit snapshot overrides only the values it names.
- The completed-floor manager remains active through the completion Night.
  A delayed effect that resolves after the next floor is created uses the new
  floor and manager. Weekend scaling uses the completed or current floor, but
  manager modifiers do not affect Weekend events unless their text explicitly
  says so.
- Reset project progress, Chad's project progress, deadline state, manager
  state, and per-floor purchase limits when the next floor is created.
- Carry cash, stress, Home inventory, relationships, family XP, selected
  traits, card progression, stored tasks, Focus, active Sales Cycles,
  Campaigns, reserves, debt, Pinned Tasks, charges, rerolls, and delayed Effect
  Instances according to their individual duration rules.

Determine the accepted Outcome and apply protective effects in this priority
order:

1. Outcome guarantees and choices;
2. Executive Air Cover;
3. Contingency Plan;
4. Failover Protocol; and
5. Escalation Coverage.

For Slumped at Desk, use `Executive Air Cover -> Preventive Maintenance ->
Perfect Execution -> Failover Protocol -> Escalation Coverage`. Stop at the
first effect that replaces, converts, or neutralizes the harmful resolution.
For a qualifying harmful Workday Event, Executive Air Cover applies before
Escalation Coverage; action-only protections do not apply.

### Coworker Bonus Activation Order

- Reset every Standard Bonus Opportunity at workday start. Normal Team Meeting
  participation and the normal daily desk visit are the only current Standard
  sources.
- Staff Check-In, Cross-Functional Sync, Delegation's start contributions,
  Delegation's Work and Team Meeting effects, All Hands, Executive Sponsor,
  Senior Sponsor, and Referral Network's generated bonuses create Forced Bonus
  Activations.
- Chad has no relationship-scaled bonus. His appearances create no successful
  Coworker Bonus Activation and cannot satisfy One-on-One or Referral Fee.
- For each coworker in one meeting or visit, determine one total activation
  count for that occurrence. Use the highest applicable count unless an effect
  explicitly says `additional`: a normal meeting offers one Standard
  activation, Cross-Functional Sync guarantees exactly one Forced activation,
  and an attending 10 XP Delegate receives exactly two Forced activations.
  These counts do not add together.
- A repeated Team Meeting is a new occurrence and determines its activation
  counts again. Resolve multiple activations for one coworker consecutively
  before moving to the next coworker.
- Resolve selected coworkers in selection order. Otherwise use their visible
  meeting-seat or office-roster order. These ordering rules affect logs and
  first-activation riders, not burnout timing within the atomic parent action
  or event.
- Resolve opening coworker events in this order: the combined All Hands or
  Delegation contribution event; Executive Sponsor visits from oldest to
  newest Effect Instance; then Staff Check-In visits in card-play order.
  Scheduled actions follow, with the normal daily visitor at its fixed
  midpoint.
- The normal daily visitor prefers a coworker with an unused Standard Bonus
  Opportunity. Delegation's 6 XP guarantee prefers an unused Delegate. If the
  required visitor has already spent that opportunity, the visit still occurs
  without another Standard activation.
- Calculate a coworker's complete bonus from their relationship at activation
  time. Apply strength multipliers to every numerical component, including Raj
  or Priya's stress drawback, before floor stress scaling. One-on-One's
  project-progress rider is separate and is never multiplied.
- Office Chats, Outings, direct relationship gains, ambient conversations, and
  Schmoozing Assists are not Coworker Bonus Activations.
- One-on-One responds to the first successful Coworker Bonus Activation of
  either type. Every One-on-One Effect Instance applies its own rider to that
  same first activation.
- Referral Fee counts distinct non-Chad coworkers with at least one successful
  activation that workday. Triggering twice or at increased strength still
  counts that coworker once. Every Referral Fee Effect Instance calculates and
  pays its own reward at Clock Out.

### Coworker Cash Bonuses

- Globally change Bob's relationship bonus to
  `$50 + $1 per relationship`, for a range of $50-$150.
- Globally change Priya's relationship bonus to
  `$75 + $1.50 per relationship`, rounded to the nearest dollar, for a range of
  $75-$225.
- Keep Priya's existing relationship-scaled stress drawback unchanged.

### Task Roster And Rarity

- Use traits as the only passive Resume progression; do not retain the old
  random stackable Resume skills alongside them.
- Give every completed ordinary family task exactly 1 family XP, regardless of
  rarity.
- Weight each family at 20 percent when generating morning task cards.
- Use exactly 50 ordinary family task cards total.
- Give each family ten cards: four Common, three Uncommon, two Rare, and one
  Legendary.
- Assign rarity permanently to each task card instead of rolling rarity after
  choosing a task.
- Give every ordinary randomly generated task-offer slot a 1 percent chance to
  contain a Legendary card, subject to the existing rules that explicitly
  exclude Legendary cards from paid rerolls.
- After an eligible slot's Special check fails, use this rarity distribution:
  Common 70 percent, Uncommon 20 percent, Rare 9 percent, and Legendary
  1 percent.
- Use the 70/20/9/1 distribution for initial offers, free rerolls, ordinary
  generated extensions, card-created ordinary task windows, and
  guaranteed-family ordinary slots unless a source explicitly fixes rarity.
- Paid task-list rerolls remain eligible for Special cards. After a paid
  slot's Special check fails, exclude Legendary and renormalize the
  70/20/9 Common, Uncommon, and Rare weights.
- Do not apply a universal rarity multiplier, stress tax, or other shared
  numeric modifier. Balance each fixed-rarity task around its individual daily
  effect.
- Never offer duplicate copies of the same task card in one morning.
- Allow the same task card to appear again on later workdays.
- Unless a mechanic explicitly says otherwise, effects that preserve, reroll,
  modify, or otherwise target task cards may affect every printed rarity,
  including Legendary. Do not use a Legendary exclusion as the default balance
  lever for card-targeting effects; the existing paid-reroll restriction
  remains an explicit exception.
- Give every Common card one short, automatic micro-effect in addition to its
  individual base project progress and base stress. Keep it bounded unless an
  explicit card-local progression exception applies.
- Give Uncommon cards weak or specialized effects, with no more than two short
  effect clauses.
- Give Rare cards medium-strength, build-shaping effects for the current day
  through a condition, tradeoff, or synergy.
- Make Legendary cards dramatic and family-defining for the current workday
  without guaranteeing a win.
- Use rarity to raise potential rather than making every higher-rarity card an
  automatic choice.
- Give each rarity a distinct gameplay role:
  - Commons adjust immediate efficiency through small, bounded numerical
    effects.
  - Uncommons interact with one adjacent game system or bend one rule once
    instead of merely offering larger progress or stress adjustments.
  - Rares combine or multiply systems into build-shaping plays.
  - Legendaries transform the current day without automatically winning it.
- Do not let ordinary task cards grant unrestricted persistent player buffs.
  Card-local progression and named resources are allowed only where explicitly
  approved, including Commit and Iteration Pass. Special cards such as
  `Rebrand Initiative` may unlock a persistent system when explicitly stated.

### Special Card Framework

- Special cards sit outside the five families, the 50-card ordinary roster, and
  the Common, Uncommon, Rare, and Legendary distribution.
- `Rebrand Initiative` is the first Special card.
- A Special card can be generated only in a slot belonging to the standard
  morning task window: the initial generated offer, an ordinary generated
  fourth slot that merely expands that offer, or a standard full task-list
  reroll.
- Both free and paid standard task-list rerolls are eligible to generate
  Special cards. The paid-reroll Legendary restriction does not apply because
  Special is not a Legendary rarity.
- Card-created task windows, guaranteed-family slots, generated additional-card
  choices, Campaign replacements, and other card or trait effects cannot newly
  generate a Special card.
- Outside an active Brand Strategy Campaign, Special generation occurs before
  ordinary family and rarity generation for that slot.
- During an active Campaign, generate the ordinary candidates and designate
  the protected required Campaign task first. Run Special checks afterward
  only on the remaining eligible generated slots. A Special card can never
  replace the designated Campaign task.
- Family weighting remains equal among slots that do not become Special.
- Give each eligible generated slot a 0.2 percent Special chance, represented
  as `0.002`.
- Check eligible slots in display order and stop after the first successful
  Special replacement. A generated task window can contain at most one Special
  card.
- Every standard full task-list reroll creates a fresh generated window with
  fresh Special rolls.
- After a successful Special roll, choose uniformly from all currently
  eligible Special cards. Future Specials use equal weight unless an explicit
  individual weight is Locked for that card.
- Remove `Rebrand Initiative` from the eligible pool after Brand Strategy
  unlocks. Replays and other copies still provide no second unlock or
  additional standalone benefit.
- If no Special card is eligible, treat the Special roll as failed and generate
  an ordinary card for that slot.
- A visible Special may be preserved within the current morning by an effect
  such as Concept Selection. It cannot become a Pinned Task or otherwise be
  carried into a future morning unless its own text explicitly allows that.
  A full task-list reroll discards every unpreserved Special normally.

### Pinned Tasks

- Replace every effect that previously created a fixed fourth morning option
  with a `Pinned Task`.
- Keep the ordinary morning offer at its normal two to four generated cards.
  Display Pinned Tasks in a separate drawer with no mechanical capacity limit.
  Show one or two pins inline and place any overflow behind an icon with a
  visible count that opens the full drawer.
- Selecting a Pinned Task consumes the normal primary-task choice for that
  morning.
- Ordinary task-list rerolls affect only the generated offer. Micromanager also
  affects only the generated offer and does not remove or hide Pinned Tasks.
- Every pin displays the effect that created it and when that source expires.
- Merge pins with the same card identity and the same mechanical card-state
  modifiers into one visual entry. Playing that entry resolves the card once
  and applies every attached source bonus. Afterward, consume or retain each
  source according to its own duration.
- Keep mechanically different variants as separate pins even when they share
  the same printed card identity.
- If the ordinary generated offer naturally rolls a card that is already
  pinned, reroll the generated copy and preserve the pin.
- Temporary pins expire on schedule even when a Sales Cycle replaces that
  morning's normal task selection.
- A targeted task effect such as Build Script may reroll a Pinned Task when its
  own text permits it. Preserve the pin's source bonuses and expiration on the
  replacement.

### Approved Coding Common Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| README Update | 10 | 9 | Tomorrow, a non-Coding primary task gains 2 project progress. |
| Regression Tests | 10 | 10 | Generate 1 less base stress for every 2 printed-Common tasks completed this run. If the reduction exceeds this card's generated stress, recover the excess instead, up to 5 stress. |
| Bug Triage | 10 | 10 | If Chad has more project progress when selected, gain 2 project progress. |
| Production Hotfix | 10 | 12 | If 2 or fewer workdays remain, gain 4 project progress. |

- Count completed printed-Common tasks from all five families.
- Regression Tests uses the count from before its current play resolves. Its
  own completion increases the count only for later card plays.
- For Regression Tests, first total its printed base stress and every
  applicable card or trait increase, including Clean Code's 3 base stress.
  Apply Regression Tests' reduction to that total before floor-pressure
  scaling. Convert only reduction beyond the remaining positive stress into
  recovery, up to 5. Afterward, effects such as Automation may remove any
  positive stress that remains.

### Approved Coding Uncommon Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Version Control | 10 | 10 | Choose one unselected task and pin it for tomorrow. When that pinned task is played, gain 1 Commit before it resolves. |
| Build Script | 10 | 10 | Tomorrow, reroll one offered or pinned task into a different task of the same printed rarity. The replacement generates 2 less base stress if played that morning. |
| API Integration | 10 | 10 | Choose one unselected task from another family. This card grants its 1 family XP to that task's family instead of its printed family. If the next workday's primary task belongs to that family, it grants 1 additional family XP. |

- `Commit` has a maximum of 5. Each Commit permanently grants printed-Common
  Coding cards 1 additional base project progress.
- A Commit gained from Version Control applies to the preserved card that
  granted it if that card is a printed-Common Coding card.
- Version Control and Build Script may target every printed rarity, including
  Legendary. Build Script may change the task's family but preserves its
  printed rarity and cannot reroll into the same exact task.
- Build Script's stress reduction belongs only to the replacement generated by
  that effect and expires if it is not played that morning.
- API Integration remains a Coding play for Codebase, Polish, workday history,
  and other card triggers even though its ordinary family XP is redirected.
- When API Integration is resolved as a copied effect, redirect the Host's
  pending 1 family XP while retaining the Host's printed family for every
  other progression counter, history check, and card trigger.
- API Integration's next-workday bonus can stack with Debugging. If no
  different family is represented when its effect resolves, it grants XP to
  the resolving card's printed family and arms no follow-up.
- Commit is an explicit exception to the ordinary rule against permanent
  task-card buffs.

### Approved Coding Rare Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Repository Fork | 10 | 12 | Choose a non-Coding task completed this run and pin it for tomorrow. If selected, it counts as Coding for that play, grants Coding XP instead of its normal family XP, and grants 1 Commit before resolving. |
| Parallel Processing | 8 | 10 | Choose another offered task. After Parallel Processing resolves, play that task completely as an additional card. Its positive stress is increased by 10 percent before floor-pressure scaling. |

- Repository Fork preserves the original task's card identity, printed rarity,
  progress, stress, printed effect, and Polish.
- The Coding-family conversion lasts for that play only. Later effects that
  repeat the original task use its original family.
- A forked printed-Common task receives applicable Clean Code effects and may
  start Automation when selected as the primary task.
- The Repository Fork pin expires if it is not selected the following morning.
- If no non-Coding task has been completed this run, Repository Fork schedules
  no task. It still resolves its own progress, stress, Coding XP, Codebase, and
  Polish normally.
- Parallel Processing's additional card resolves its full project progress,
  stress, printed effect, family XP, counters, and card-play triggers. Negative
  printed effects remain active.
- The additional card is not a primary card. It cannot start Automation,
  satisfy primary-only rules, or advance a Brand Strategy Campaign step.
- Resolve Parallel Processing first and check for burnout. If it causes
  burnout, do not play the additional card.
- Apply the 10 percent increase only to positive stress generated by the
  additional card. Do not reduce its recovery or otherwise change its effects.

### Approved Coding Legendary Card

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Hackathon | 8 | 8 | Reveal one random task from each family. Choose exactly two and play them completely in either order. Those tasks generate 50 percent of their positive stress. |

- Generate each non-Coding revealed task using the normal initial-offer rarity
  rules. Every printed rarity, including Legendary, is eligible.
- If Hackathon's Coding-family reveal rolls Legendary, reroll that result among
  Common, Uncommon, and Rare Coding cards. Hackathon remains the only Coding
  card it cannot generate.
- The two chosen tasks resolve their full project progress, stress, printed
  effects, family XP, counters, and card-play triggers.
- The chosen tasks are additional cards rather than primary cards. They cannot
  start Automation, satisfy primary-only rules, or advance Brand Strategy
  Campaign steps.
- Resolve Hackathon first, then resolve the chosen tasks individually in the
  selected order, checking for burnout after each complete play. Burnout stops
  the remaining sequence.
- Apply the 50 percent multiplier only to positive stress generated by the two
  chosen tasks before floor-pressure scaling. Do not reduce their recovery or
  otherwise change their effects.
- Hackathon cannot generate another Hackathon.

### Coding Card Identity

Design Coding cards around three family pillars:

- **Build:** turn completed work, card history, or preserved task options into
  future value.
- **Automate:** sequence, filter, reroll, or process additional cards.
- **Integrate:** hand value or progression between Coding and other families.

Coding may remain the most internally synergistic family, but cards from all
three pillars still need standalone or cross-family reasons to be selected.

### Approved Management Common Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| One-on-One | 10 | 10 | The first coworker bonus triggered today grants 2 project progress. |
| Meeting Minutes | 10 | 10 | The first Team Meeting today grants 3 project progress. |
| Action Plan | 10 | 10 | The first Work on Task action today grants 2 additional project progress. |
| Capacity Planning | 9 | 10 | If at least six actions are scheduled today, gain 4 project progress. |

- One-on-One requires a successful activation. Chad and a blocked Standard
  opportunity do not consume its first-activation trigger.
- Capacity Planning checks the final locked number of Schedule Entries. Repeats,
  Triggered Schedule Entries, and Workday Events do not increase its count.

### Approved Management Uncommon Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Meeting Prep | 10 | 10 | Guarantee a Team Meeting today. If none are naturally scheduled, replace one random eligible ordinary action. |
| Staff Check-In | 9 | 10 | Choose a coworker. They make one bonus desk visit today and trigger their full relationship-scaled bonus. |
| Schedule Adjustment | 10 | 10 | Reroll one ordinary non-Lunch action into a different ordinary action. |

- Staff Check-In creates exactly one Forced Bonus Activation and does not
  consume the chosen coworker's Standard Bonus Opportunity.

### Management Card Identity

- Management observes coworkers, meetings, action order, and schedule size,
  then converts successful coordination into value.
- Management Commons reward those systems with bounded numerical effects.
  Higher rarities may guarantee, select, rearrange, or multiply the underlying
  people and workday actions.
- Management cards should remain useful outside Management traits while
  becoming more reliable or more powerful with Delegation, Agile, Leadership,
  and cross-family action generators.

### Approved Management Rare Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Cross-Functional Sync | 8 | 12 | Choose three coworkers. Add one bonus Team Meeting with them today. Each chosen coworker's relationship bonus triggers in that meeting even if it has already triggered today. |
| Executive Review | 9 | 11 | After revealing the schedule, choose Work on Task, Team Meeting, Water Cooler, or Office Chat. Add two bonus copies of that action to the beginning of the workday. |

- Cross-Functional Sync creates exactly one Forced Bonus Activation for each
  chosen coworker rather than a normal activation plus a forced one. An
  attending 10 XP Delegate receives exactly two activations total because
  Delegation sets the higher per-occurrence count.

### Approved Management Legendary Card

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| War Room | 8 | 10 | After revealing the schedule, add one bonus Work on Task, Team Meeting, Water Cooler, or Office Chat. That bonus action resolves twice. Every naturally scheduled ordinary non-Lunch action resolves one additional time today. Every Lunch, Office Chat, and Team Meeting outcome today is favorable. |

- War Room does not repeat Lunch, hostile actions, sabotage, special actions,
  or bonus actions from other sources.
- Slumped at Desk, sabotage, and hostile actions retain their normal harmful
  outcomes.
- Each play of War Room adds its own chosen bonus action, which resolves
  exactly twice, and adds one resolution to every eligible naturally scheduled
  action. Replaying War Room therefore rewards card-repetition effects without
  recursively repeating an added resolution.

### Approved Design Common Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Iteration Pass | 10 | 10 | After each complete play, Iteration Pass permanently gains 1 base project progress for the rest of the run. |
| Reference Study | 10 | 10 | If yesterday's primary task belonged to another family, gain 2 project progress. |
| Accessibility Review | 9 | 10 | If selected at 50 or more stress, recover 3 stress. |
| White Space | 10 | 10 | At Clock Out, if stress is no higher than after this card resolved, gain 3 project progress. |

- Iteration Pass gains its progress after the current play resolves, so its
  first complete play grants 10 base progress and later plays use the updated
  value.
- Every complete replay increments Iteration Pass once. Its accumulated
  increase is base progress rather than a positive numeric printed effect, so
  Refinement and Precision do not multiply that increase again. Their normal
  Polish-based base-progress bonuses still apply.
- Iteration Pass's entire printed effect is identity-bound. It cannot be chosen
  by Rapid Prototype or another copy effect and is rerolled from generated
  copy-source windows such as Design System.

### Approved Design Uncommon Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Prototype Test | 10 | 10 | Tomorrow, reveal two possible natural workday schedules before choosing the primary task. Choose which schedule to use. |
| Concept Selection | 9 | 10 | Tomorrow, preserve any number of ordinary offered tasks, then reroll every other ordinary slot once for free. |
| User Testing | 10 | 10 | Before workday playback, reveal three possible exact Lunch outcomes and choose one. |

- The first Prototype Test Effect Instance reveals two candidate schedules.
  Every additional instance applying to the same morning adds one candidate
  to the same combined schedule choice rather than opening another window.
- The first User Testing Effect Instance reveals three possible exact Lunch
  outcomes. Every additional instance applying to that workday adds one
  candidate to the same combined outcome choice.
- Each Concept Selection Effect Instance grants one complete selective-reroll
  pass. Apply multiple passes sequentially in the same interface, allowing the
  player to preserve tasks again before each pass.
- Every boss-floor candidate retains its required hostile action. Task, trait,
  Deal, and other post-selection schedule changes apply only after the player
  chooses a candidate and selects the primary task.

### Approved Design Rare Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Creative Breakthrough | 9 | 11 | For this workday and the next, stress recovery also grants equal project progress. Excess recovery still grants its project progress. |
| Rapid Prototype | 8 | 12 | Choose one other visible task. Resolve its entire printed effect as Rapid Prototype's effect today. |

- Creative Breakthrough applies to recovery from task resolution, scheduled
  workday actions, and Clock Out effects. It excludes Lights Out, automatic
  sleep, weekends, and promotion recovery.
- The effect follows the player across a promotion if its second workday has
  not occurred.
- Each complete play creates a separate two-workday instance. Overlapping
  instances stack their project-progress conversion rates.
- Excess recovery grants project progress but is not actual recovery and
  therefore does not generate Focus through Moodboard.
- Rapid Prototype may target a generated or Pinned Task of any printed rarity.
  The target is not consumed. Identity-bound cards and Sources already present
  in the current copy ancestry are visibly ineligible.
- Copy every positive and negative printed clause. Do not resolve the target's
  base progress, base stress, family XP, Polish, counters, card-play triggers,
  Campaign progress, or other effects that require the named card to be
  completed.
- Rapid Prototype's own Polish modifier applies to positive numeric values in
  the copied effect. It does not multiply nonnumeric guarantees, action counts,
  or choice counts.
- Every Rapid Prototype Effect Instance keeps its own copy-source choice. A
  replay or nested copy may choose the same visible task unless that Source is
  already present in its active copy ancestry.

### Approved Design Legendary Card

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Design System | 8 | 12 | Open a task window containing four new tasks with no rerolls. Choose one. For this workday and the next, each primary task also resolves that task's entire printed effect. |

- Generate four distinct candidates using normal initial-offer family and
  rarity rules. Every printed rarity is eligible.
- Reroll a candidate that duplicates another candidate, a task in the current
  ordinary offer, a Pinned Task, Design System, any Special card, an
  identity-bound card, or a Source already present in the active copy ancestry.
- The chosen task lends only its complete printed effect, including positive
  and negative clauses. It is not played and grants no base progress, base
  stress, family XP, Polish, counters, card-play triggers, Campaign progress,
  or named-card completion effects.
- Design System's own Polish modifier applies to positive numeric values in the
  borrowed effect. It does not multiply nonnumeric guarantees, action counts,
  or choice counts.
- The borrowed effect applies to Design System's current complete primary play
  and the following workday's primary task. A workday without a primary task
  consumes that day of duration without triggering it.
- Every Design System Effect Instance opens its own four-task window and
  creates a separate two-workday instance. Overlapping instances stack.

### Design Card Identity

Design cards use three pillars:

- **Observe:** reveal schedules, outcomes, or options before the player commits.
- **Iterate:** preserve and refine cards or choices through repeated work.
- **Transform:** copy printed effects or convert recovery and other existing
  value into project progress.

Design should provide splash value through information and flexible effect
access. It manipulates cards and their effects rather than repeating the
underlying workday schedule, which remains Management's territory. Iteration
Pass is an explicit card-local exception to the normally bounded Common
micro-effect rule.

### Approved Sales Common Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Expense Allowance | 9 | 10 | Gain $100 Expense Credit for tonight. Unspent credit expires at Lights Out. |
| Referral Fee | 10 | 10 | At Clock Out, gain $25 for each different coworker bonus triggered today, up to $75. |
| Sales Quota | 10 | 10 | At Clock Out, if you gained at least 20 project progress today, gain $100. |
| Cross-Sell | 10 | 10 | If you spend money on two of Home, Deals, or Outings tonight, receive a $100 rebate. |

- Expense Credit is temporary purchasing power for Home cards, Deals, and paid
  Outings. It is not ordinary cash, cannot earn interest, and expires at Lights
  Out.
- Referral Fee tracks coworker identities rather than activation quantity.
  Replayed or otherwise duplicated Effect Instances each pay separately.

### Approved Sales Uncommon Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Client Entertainment | 9 | 10 | Choose a coworker. Tonight, take them on any Outing for free; it grants 8 relationship instead of its normal amount. |
| Comparison Shopping | 9 | 10 | Tonight, after the Home and Deal catalogs are generated, choose one visible Home card or Deal. Reveal two random alternatives from the same catalog. Buy one of the three for 50 percent less. |
| Commission Advance | 9 | 11 | Gain $500 immediately. If the project is not completed by the end of tomorrow's workday, gain 20 flat stress. |

- Comparison Shopping's two alternatives are distinct, currently eligible
  options. Its compact comparison window shows only the original item and those
  two alternatives.
- Comparison Shopping's 50 percent discount has no cash-value cap and uses the
  chosen item's normal purchase limit.
- Commission Advance's failure penalty applies exactly 20 stress, ignoring
  floor scaling and every stress modifier. It can still cause burnout, and a
  Guardian Angel may respond to that burnout normally.

### Approved Sales Rare Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Corporate Expense Account | 8 | 12 | Gain $500 Expense Credit for tonight and one additional Home or Deal purchase tonight. Unspent credit expires at Lights Out. |
| Referral Network | 9 | 11 | Choose three coworkers; each gains 4 relationship. Tomorrow, the first time one of their bonuses triggers, trigger all three bonuses at doubled strength instead. |

- Corporate Expense Account uses the standard Expense Credit rules. Its
  additional purchase may be used on either a Home card or a Deal and expires
  if unused that night.
- Referral Network watches only Standard Bonus Opportunities. The first
  qualifying activation consumes the Network before generating its bonuses,
  marks all three selected coworkers' Standard opportunities as spent, and
  replaces the original with one doubled-strength Forced Bonus Activation from
  each selected coworker in selection order.
- Referral Network cannot replace a Forced Bonus Activation or recursively
  replace one of its own generated activations. With multiple pending
  Networks, use the oldest eligible Effect Instance; later instances remain
  armed for a later qualifying Standard activation and may expire unused.
- Its doubled-strength activations multiply each coworker's complete package,
  including Raj or Priya's stress drawback. The parent meeting or visit remains
  atomic for burnout.

### Approved Sales Legendary Card

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Net 30 Contract | 8 | 8 | Tonight, open the Deal Desk and finance one visible Home card or Deal without paying. At tomorrow's Clock Out, pay its final price. Gain 1 flat stress for every $25 of the unpaid balance. |

- Net 30 Contract shows the standard three distinct weighted Deal offers even
  if the player has no Negotiation milestone.
- Financing uses the relevant Home or Deal purchase limit rather than adding
  another purchase. A player without Negotiation receives exactly one
  temporary Deal purchase for this purpose.
- Net 30 Contract does not grant Negotiation's free Deal reroll, pay, interest,
  Client Call, or Deal-strength benefits. A player who already has those
  milestones applies them normally.
- Use the final purchase price after applicable discounts as the amount due.
  At the following Clock Out, automatically spend available cash toward the
  balance before converting the unpaid remainder into flat stress.

### Sales Card Identity

Sales cards use three pillars:

- **Earn:** turn performance and coworker activity into cash or Expense Credit.
- **Spend:** compare, discount, finance, or expand purchases.
- **Network:** convert relationships and coworker bonuses into economic value.

Sales money should buy tempo, options, or access rather than serving only as a
score. Its cards should remain useful without a Sales trait while becoming
stronger when Negotiation, Schmoozing, or Closing creates additional ways to
spend or exploit their resources.

### Approved Operations Common Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Process Audit | 9 | 10 | At Clock Out, gain 1 project progress for each different positive workday action type resolved today, up to 4. |
| Preventive Maintenance | 8 | 11 | The first Slumped at Desk today becomes a Water Cooler action. |
| Priority Requisition | 9 | 10 | Consume one Home reroll and gain two task rerolls. |
| Overnight Reserve | 10 | 9 | At Clock Out, reserve $250 if available. Return it the following morning and gain $100. |

- Process Audit counts each positive action type at most once. It uses the same
  positive-action definitions as Efficiency and includes beneficial special
  actions.
- Preventive Maintenance converts the complete action. The replacement Water
  Cooler grants its normal reroll and receives every applicable action and
  trait effect.
- Priority Requisition resolves only if a Home reroll is available. Its two
  task rerolls remain available for future standard morning offers.
- Overnight Reserve occurs after normal Clock Out pay and interest. Reserved
  cash cannot be spent that night and returns before the following morning's
  task choice and Reserve-Level calculation. If less than $250 is available,
  no cash is reserved and no profit is granted.

### Approved Operations Uncommon Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Contingency Plan | 9 | 10 | Reroll the first unfavorable Lunch, Office Chat, or Team Meeting today and accept the second result. If it remains unfavorable, gain one task reroll. |
| Shift Handoff | 8 | 11 | At Clock Out, copy the last naturally scheduled positive non-Lunch action into tomorrow's workday as a bonus action. |
| Accrual Accounting | 9 | 10 | Up to $500 spent tonight still counts toward tomorrow's Reserve Levels and interest-eligible cash. |

- Contingency Plan rerolls only the selected action's outcome. It does not
  repeat the action or affect Slumps, sabotage, hostile actions, passive
  manager effects, or task and trait costs.
- Shift Handoff records the last positive Action Resolution whose Schedule
  Entry has natural origin, including an entry converted at runtime. Tomorrow's
  bonus copy rolls a fresh Outcome, receives normal action and trait effects,
  and follows the player across a promotion.
- Accrual Accounting records ordinary cash actually spent after discounts. It
  excludes Expense Credit and financed amounts, grants no spendable cash, and
  remains subject to normal interest and Reserve-Level caps. Its accounting
  value expires after the following workday's interest calculation.

### Approved Operations Rare Cards

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Working Capital | 9 | 11 | When selected, choose a reserve cap of $500 or $1,000. At Clock Out, reserve the largest affordable $500 increment up to that cap until tomorrow's Clock Out. Add one bonus Work on Task action tomorrow for each $500 reserved. |
| Failover Protocol | 8 | 12 | The first two positive non-Lunch actions today become Backups. A later Slump or unfavorable Office Chat or Team Meeting is replaced by the oldest Backup. |

- Working Capital reserves only an amount the player can fully fund after
  normal pay and interest. Reserved cash is unavailable for night purchases
  and paid morning actions, but still counts toward the following workday's
  Accounted Cash snapshot and Reserve Levels. It returns at that workday's
  Clock Out before the locked interest payout and mandatory debt payments.
- Choosing the reserve cap is part of the morning card resolution. Clock Out
  never opens another decision: reserve $1,000 when allowed and affordable,
  otherwise $500 when allowed and affordable, otherwise reserve nothing.
- Each Working Capital bonus Work action receives every normal Work-action and
  trait effect. The reserved cash and scheduled actions follow the player
  across a promotion.
- A Failover Protocol Backup records the successful action and its favorable
  outcome, but not its participants or source-specific bonuses. When consumed,
  it uses fresh participants and resolves the recorded action and Outcome with
  currently applicable global action and trait effects.
- Each Backup can be consumed once. A replacement action cannot create another
  Backup. Lunch, sabotage, hostile actions, passive manager effects, and task
  or trait costs cannot consume a Backup.

### Approved Operations Legendary Card

| Card | Progress | Base stress | Locked effect |
|---|---:|---:|---|
| Perfect Execution | 8 | 12 | Every positive non-Work workday action today triggers one bonus Work on Task. Slumped at Desk becomes Work on Task. Every Work on Task grants 2 additional project progress today. |

- Positive non-Work actions use Efficiency's positive-action definitions and
  include favorable Lunch, Office Chat, and Team Meeting outcomes as well as
  beneficial special actions.
- Resolve each bonus Work on Task immediately after its triggering action. It
  receives every normal Work-action and trait effect but cannot trigger Perfect
  Execution because it is a Work action.
- If Preventive Maintenance and Perfect Execution are both active, Preventive
  Maintenance converts the first Slump into Water Cooler first. That positive
  Water Cooler then triggers Perfect Execution's bonus Work action. Perfect
  Execution converts any remaining Slumps directly into Work actions.
- Unfavorable outcomes, sabotage, hostile actions, passive manager effects, and
  task or trait costs remain unchanged.
- Each complete replay of Perfect Execution creates another trigger and adds
  another 2 project progress to every Work action. Treat this multiplicative
  replay scaling as a simulation watchpoint, not a proposed nerf.

### Operations Card Identity

Operations cards use three pillars:

- **Reserve:** hold cash, cards, or work for a later payoff.
- **Stabilize:** reroll, prevent, or replace unreliable outcomes.
- **Deliver:** hand off successful actions or convert them into dependable
  throughput.

Operations should make volatile systems reliable without guaranteeing every
outcome. It reacts to process and resource flow rather than directly commanding
people or schedules, which remains Management's territory.

### Balance Review Order

- The complete qualitative cross-family review of all 50 approved cards is
  finished. No card requires a further numeric redesign before full
  verification and simulation.
- Preserve the approved card roster and edge-rule clarifications. Treat the
  risks below as simulation targets rather than automatic nerfs.
- Do not perform final numeric tuning until full verification confirms the
  approved roster, traits, and structural baseline are implemented accurately.

### Legacy Resume Content Replacement

- The candidate removes the player's old stackable Resume skills, random
  rarity-based stack rewards, `R.resume`-style state, exact-skill stack
  forecasts, and stack-based Help and UI copy. Ordinary family tasks use the
  family-XP system instead.
- `Library` remains a $1,000 Tier 3 Home upgrade. Once per floor after Library
  is owned, the first ordinary primary task completed grants 1 additional XP
  to its family. Campaign tasks, Sales Cycle cards, Replays, and Complete
  Additional Plays neither trigger nor consume this once-per-floor bonus.
- Hackathon's `Stay home and study` Weekend outcome lets the player choose one
  family and grants it 1 family XP. This is a direct XP grant rather than a
  card play and grants no card counters or other completion triggers.
- Networking Brunch's successful `Work the room` outcome lets the player
  choose one non-Chad coworker to gain 5 relationship, then applies the
  existing 4 base stress before floor scaling. It retains the existing 70
  percent success and 30 percent 10-stress failure chances.
- Family XP gained during a Weekend follows the Locked transition and promotion
  claim order.
- Chad's separate rival stacks and accumulated-upgrade model are unrelated to
  the removed player Resume system and remain unchanged.

### Future Home Set Compatibility

- The candidate routes Home-upgrade behavior through one centralized,
  data-driven Home effect registry.
- Home-upgrade records can carry optional inert set metadata, and the
  Home card, inventory, tooltip, and sale-confirmation components render set
  progress and set-break consequences when an active set definition exists.
- No Home set bonus is active. The 15-upgrade roster, prices, and current 25
  percent list-price resale rule remain unchanged.
- Every standalone Home effect is preserved except where another Locked
  decision changes it, including Comfy Mattress and Library.
- Design and balance the actual Home sets only after the candidate passes full
  verification.

### Cross-Family Simulation Watchlist

These are risks to measure after full verification, not approved nerfs:

- action multiplication across War Room, Perfect Execution, Efficiency, Agile,
  Leadership, Deals, and other bonus-Work sources;
- Legendary replication through Pilot Approved, Hackathon, Design System, and
  other replay or copied-effect systems;
- Comparison Shopping's uncapped late-game Home and Deal discounts;
- persistent scaling from Clean Code, Commit, and Iteration Pass;
- Library's once-per-floor family-XP acceleration and milestone timing;
- economy compounding across Sales cards, Negotiation, Compound Interest,
  discounts, financing, Expense Credit, and Home purchases;
- Success Fee may create excessive late-run cash when its free Deal reroll and
  $1,500 or $3,000 payout align; and
- Productivity License plus Contractor Support may create excessive capstone
  burst progress with Work-action traits and Home upgrades.

### HUD Readability Direction

- Move the player portrait into a standalone HUD cluster in the bottom-left
  corner.
- Give the player cluster two persistent bars: project progress and stress.
- Do not place the HUD inside a full-width bottom background, frame, or border.
- Place Chad's portrait and project-progress bar in the top-right corner, with
  workdays remaining directly underneath.
- Keep the current project title prominent and larger than secondary HUD text.
- Keep a reduced right-hand sidebar dedicated to Resume information.
- Divide the Resume sidebar height across the five family summaries and use
  larger text for family XP, selected paths, and milestone status.
- Show family XP as ten discrete one-point segments without visible XP
  counters. Mark the 3/6/10 milestone gates and emphasize the next required
  gate. At 10, use an overflow marker rather than a number.
- Use a dark-mode Resume Book for complete trait details.
- Show exact uncapped family XP in the Resume Book and Promotion Review because
  Debugging and other effects can use XP above 10.
- Keep the capstone owner or pending reservation visible in the Resume rail and
  Resume Book.
- Favor larger text across the persistent HUD wherever space permits.
- Keep the top-left HUD and cash prominent, with the top-left and Chad clusters
  balanced around the center ticker.
- Show only spendable cash persistently in the top-left run cluster. Hover,
  keyboard focus, or activation opens a compact economy breakdown containing
  current Expense Credit, reserved cash, Working Capital, debt, and estimated
  interest when those values exist.
- Place a house-icon button beside cash. It opens a read-only Home inventory
  showing the current residence, slot usage, owned upgrades, and exact effects.
  Home purchases remain exclusive to the Night phase.
- Place Today's task directly under the Manager control in the top-left HUD.
  Show only `TODAY // FAMILY: TASK`, outline it with the task family's color,
  and reveal the complete daily effect on hover or keyboard focus.
- Give the Today control a neutral preselection state, distinct ordinary,
  Campaign, Sales Cycle, and Close states, and state-appropriate tooltip
  details. Retain the completed workday's state through Night, then clear it
  for Weekend and Promotion so a stale task is never shown.
- Format the Manager control on two lines, with `Manager:` above the manager's
  name.
- Center progress, stress, recovery, and rival values inside their bars in
  white.
- Emphasize the workdays-remaining number at twice the label size while keeping
  `WORKDAYS LEFT` stable and readable.
- Compact the Resume rail and player/Chad HUD clusters only during workday
  playback, then expand them in every other phase where the sidebar is
  available.
- Do not include a manual Resume minimize control.
- During workday playback, place Help, a `1x/2x/4x` speed selector, and Skip
  controls at the bottom-right immediately left of the Resume rail. Use a
  segmented speed control when space permits and one cycling button that shows
  the active speed on short or landscape-phone viewports. Expose compact
  controls through tooltips and accessible labels.
- Hide playback controls outside the workday. Changing speed or skipping alters
  presentation only; Skip visibly enters a disabled resolving state until the
  deterministic workday finishes.
- Preserve the selected playback speed between workdays for the remainder of
  the run.
- Place a compact active-effect strip beside the player bars for Focus,
  Guardian Angel, Escalation charges, and delayed effects with remaining
  durations. Use icons with exact tooltips during workday playback and expanded
  labels in other phases. Collapse overflow behind a visible count rather than
  extending across the office.
- Make Chad's HUD hoverable, focusable, and activatable to open his detailed
  forecast containing current stacks, accumulated upgrades, and the estimated
  next-workday progress range.
- Apply the larger-text and no-overlap requirements to task, Deal, Home,
  Promotion, Campaign, Closing-reward, and other decision surfaces in addition
  to the persistent HUD. Favor concise effect text over flavor when space is
  constrained.
- Keep reroll counts on the decision surfaces where they can be used and show
  exact coworker values inside relevant choice pickers or Night views rather
  than adding more persistent HUD counters.

### Office Layout Direction

- Use a cozy but professional office with warm windows, plants, wood accents,
  personal focus rooms, and a visible manager office and desk.
- Keep exactly eight indexed cubicles in two rows of four so the existing
  conversation reservation model remains compatible.
- Preserve the rule that a conversation reserves its host cubicle and blocks
  the immediately adjacent cubicles in the same row.
- Make every cubicle large enough for one seated host and three visiting Team
  Meeting participants.
- Let Team Meetings wait for existing conversations to finish, then show only
  one attached speech bubble at a time.
- Keep a broad central circulation spine and vertical aisles connecting every
  cubicle, the water cooler, lunch/coffee counter, copier, personal offices,
  and manager office.
- Keep active workers, action stations, meeting signals, and walking routes
  visible around the persistent workday HUD.
- Support phone play in landscape orientation and show a simple rotation screen
  in portrait.

### Trait System Structure

- Replace linear per-skill resume stacking with family XP milestone traits.
- Tasks advance their job family rather than an exact skill.
- Weight generated cards equally by family and allow multiple cards from the
  same family in one morning.
- At 3 family XP, choose one of the family's ordinary visible trait paths.
- Evolve the chosen path at 6 and 10 family XP.
- Closing is an exception after it is selected as a Sales path. It has no 6 or
  10 Sales XP milestones; the Sales Cycle and its persistent Close rewards are
  the path's progression system.
- Claim trait unlocks at promotions.
- Allow free hybrid investment across all five families.
- Show each full ordinary milestone path and its capstone before selection.
- Give every ordinary milestone path its own capstone. Closing instead uses its
  first successful actual Chain 9 Close as its non-XP capstone trigger.
- Allow only one capstone per run.
- The first selected ordinary milestone path to reach 10, Brand Strategy to
  finish its final Campaign, or Closing to complete its first successful actual
  Chain 9 Close claims the run's single capstone. Closing cannot claim the
  capstone through Sales XP.
- Use natural mechanical synergies rather than named pair-combination bonuses.
- Mix family-specific and global effects where the fiction supports them.
- Make normal traits pure upside.
- Make capstones run-defining but not automatic wins.
- Let capstones override directly conflicting manager rules.
- Keep Efficiency's locked extra Work action visible in workday playback.
- Make Efficiency Operations' dedicated reliability and process-control path.
  It should guarantee useful workday output and smooth schedule variance rather
  than rely on another uncapped scaling counter.
- Efficiency should also amplify positive workday actions and reward
  consistently favorable workday outcomes, so its upside is not limited to
  guaranteed actions. Positive-action bonuses replace their earlier milestone
  value and never lose accumulated value because of a later negative action.
- Make Brand Strategy reward switching families and hybrid play.
- Make Debugging primarily support other families rather than act as another
  self-contained scaling engine.
- Make Debugging's effects interact directly with other family traits or their
  progression rather than provide generic harmful-event prevention.
- Give Debugging a powerful, conditional capstone that supports hybrid play
  through cards, progression, actions, or resources without activating other
  traits or bypassing their family requirements.
- Build trait paths around conditional setup and payoff interactions that can
  become exceptionally strong when assembled correctly, rather than relying
  primarily on incremental efficiency bonuses.
- Use costs, card requirements, action order, or other build commitments to
  keep those high-ceiling engines from being automatic.
- For Clean Code, count every Coding task completed from the beginning of the
  run toward its Codebase, including tasks completed before selecting the path.
- Let Clean Code's Codebase continue growing beyond 10 family XP.
- Increase Codebase immediately after each Coding card play resolves. The
  resolving card uses the previous Codebase value, while later cards played
  during the same morning use the new value.
- Trait milestones are cumulative. Reaching 6 or 10 XP preserves every earlier
  active effect unless the new milestone explicitly replaces or upgrades that
  specific effect.
- Brand Strategy is the exception to the ordinary trait-path structure. It is
  hidden from Design's 3 XP choices, unlocks only through the Special card
  `Rebrand Initiative`, and progresses through named Campaign quests rather
  than 3/6/10 Design XP milestones.

### Promotion Claim Batch And Capstone Ownership

Capstone eligibility and reservation follow these rules:

- A selected ordinary path becomes a capstone candidate when its family XP
  first reaches 10. A family at 10 XP without a selected path is not eligible
  until the player chooses that path at promotion.
- Brand Strategy becomes a candidate when its final Campaign completes.
  Closing becomes a candidate on its first successful actual Chain 9 Close.
- If one atomic effect creates exactly one eligible candidate while the slot
  is open, reserve the capstone for it immediately. Ordinary capstones activate
  at the next promotion; Brand Strategy and Closing retain their immediate
  activation timing.
- If one atomic effect creates multiple candidates, finish that effect and
  pause at the next interactive boundary before workday playback or another
  qualifying event. The pending comparison reserves the slot for only those
  tied candidates.
- A previous reservation defeats every candidate created later, including a
  later promotion batch. A player cannot decline, bank, or release an owned or
  reserved capstone.
- If an atomic promotion batch creates multiple candidates while the slot is
  open, compare them after all path and non-capstone milestone choices are
  staged. Family order and interface click order never break the tie.
- An ordinary candidate that loses still receives its complete 10 XP
  milestone. Brand Strategy that loses cannot activate its final Campaign
  reward. Closing that loses, or qualifies after the slot is owned, cannot
  offer Anchor Account.
- Warn the player when an unselected family has reached 10 XP but remains
  ineligible, making the slot available to Brand Strategy, Closing, or another
  already-selected path.

Resolve each Promotion Claim Batch as one transaction:

1. Stage every required path selection for unselected families at 3 or more XP.
2. Stage every required non-capstone choice from reached 3, 6, and 10 XP
   milestones.
3. Apply milestone eligibility in order from 3 to 6 to 10 and determine every
   capstone candidate created by the complete promotion batch.
4. If necessary, present one dedicated capstone comparison and require the
   player to choose exactly one candidate.
5. Resolve any choice belonging specifically to the winning capstone.
6. Show the complete result and require one final confirmation. Only then make
   the staged paths, milestones, subchoices, and capstone active.

- The player may revise staged choices until final confirmation. Changing a
  path clears every dependent milestone and capstone choice for that path.
  After confirmation, path and permanent-team choices are irreversible.
- If a family is already at 10 XP when its path is selected, stage its 3, 6,
  and 10 XP milestones during that same promotion.
- A previous capstone reservation activates automatically after its ordinary
  path's 10 XP milestone is confirmed. If the slot is already owned, later
  ordinary paths still receive their 10 XP milestones without capstones.

Use one `Promotion Review` interface:

- Show a five-family rail with segmented XP bars, highlighted decisions, and
  checkmarks for completed claims.
- Use one central detail pane for the selected path's immediate effect, later
  milestones, and capstone rather than displaying every full path at once.
- Keep a visible count of unresolved decisions and disable Continue until all
  required choices and final confirmation are complete.
- Use a dedicated comparison view for simultaneous capstone candidates and
  show the consequence of each losing candidate.
- Keep the dark-mode Resume Book available for full wording.
- Display Brand Strategy as a separate questline beneath Design. After Closing
  is selected, replace Sales milestone presentation with its Deal Ladder.
- Show exact family XP, including values above 10, in Promotion Review while
  preserving the counter-free ten-segment persistent Resume rail.
- Keep the capstone owner or reservation permanently visible and mark every
  unavailable capstone accordingly.
- If a promotion creates no decisions, use a compact summary rather than the
  full choice interface.
- End with a summary of activated traits, the capstone owner, stress, cash, and
  carried effects before creating the next floor.

### Printed Common Coding Rule

- The four printed-Common Coding cards count as Common Coding cards for every
  Clean Code and Automation rule.
- A printed-Common non-Coding task converted by Repository Fork also receives
  Clean Code's scaling and may start Automation when selected as the primary
  task. It receives the Commit granted by Repository Fork before that play
  resolves.
- Automation's generated additional-card choices, offer weighting, and
  post-Combo-5 pool still contain only the four native printed-Common Coding
  cards. Repository Fork does not add the converted task to those pools.
- Printed-Uncommon, Rare, and Legendary Coding cards do not receive Clean
  Code's Common-card progress bonus and cannot start or continue an Automation
  Combo.
- Every Coding task still grants 1 Coding XP and increases Codebase and its own
  Polish after resolving, regardless of printed rarity.
- Additional Coding plays and Coding replays are Complete Plays under the
  global resolution rules. They resolve their printed effects, grant 1 Coding
  XP, increase Codebase and their own Polish, and receive applicable
  card-progress bonuses.
- Automation's no-stress rule is an explicit source modifier applied to its
  Complete Additional Plays. Outside Automation, an additional Coding play
  pays the stress specified by the effect that created it.

### Clean Code Trait Path

`Codebase` is the uncapped number of Coding tasks completed this run.

| Milestone | Locked effect |
|---|---|
| 3 XP | Printed-Common Coding cards gain +1 project progress per Codebase and add 3 base stress. |
| 6 XP | The Common-card bonus becomes +1.5 progress per Codebase. The stress cost remains 3. |
| 10 XP | The Common-card bonus becomes +2 progress per Codebase. The stress cost remains 3 unless Clean Code owns the capstone. |
| Capstone: Zero Technical Debt | Remove Clean Code's 3-base-stress penalty from printed-Common Coding cards and apply their Common-card scaling bonus twice. |

### Automation Trait Path

All Combo state, additional-card cost escalation, and paid-reroll cost
escalation reset at the start of each workday.

| Milestone | Locked effect |
|---|---|
| 3 XP | Gain one free global task-list reroll every morning. Selecting a Common Coding card as the primary task starts Combo 1. The player may pay $100 for the first additional Common Coding card, with each subsequent card costing $100 more. Additional cards gain an escalating +2, +4, +6, and so on project progress. |
| 6 XP | Additional-card cost escalation drops to +$50. Combo 5 grants +20 project progress. Global paid task-list rerolls begin at $100 each morning and cost $100 more per additional paid reroll. From Combo 2, Common Coding offer weight gains 20 percentage points. |
| 10 XP | Additional-card cost escalation drops to +$25. Paid rerolls begin at $50 and cost $50 more per additional paid reroll. Combo 10 grants +100 project progress. After Combo 5, subsequent Combo offers contain only Common Coding cards. |
| Capstone: Infinite Loop | After Combo 10, Combo 15, 20, 25, and every fifth Combo thereafter grants +100 project progress and resets the next additional-card and paid-reroll prices to $100 and $50. |

- The free reroll is global rather than Combo-dependent, remains available at
  later milestones, and can offer Legendary cards.
- Paid rerolls are also global morning actions rather than Combo-dependent, but
  cannot offer Legendary cards.
- Automation may use only printed-Common Coding cards as additional cards. Each
  is a Complete Additional Play, adds no stress, grants exactly 1 Coding XP,
  and receives Automation's escalating project-progress bonus.
- Automation may offer and play the same exact printed-Common Coding card more
  than once during one Combo. This is an explicit exception to the generated
  play-chain repeat restriction. A single simultaneous Combo offer still
  cannot contain duplicate copies of one task.
- Additional-card XP is granted immediately after each additional card
  resolves. Because milestone traits unlock only at promotions, XP earned
  during a Combo cannot change that Combo's active milestone effects.
- The 6 XP Common Coding offer bonus is additive, not a relative multiplier.

### Debugging Trait Path

| Milestone | Locked effect |
|---|---|
| 3 XP | After a Coding workday, selecting a non-Coding primary task grants 1 additional family XP to the selected task's family. |
| 6 XP | Selecting any non-Coding primary task grants 1 additional family XP to the selected task's family. This is cumulative with the 3 XP effect. |
| 10 XP | At the start of every workday, gain project progress equal to half of the total family XP earned across all five families. This 1:2 conversion has no cap, and family XP above 10 continues to count. |
| Capstone: Production Ready | On the workday immediately after a Coding workday, selecting a non-Coding primary card plays that card twice. Both plays resolve full base progress, base stress, printed effects, ordinary family XP, and card-play counters and triggers. |

- The 3 and 6 XP bonuses trigger from selecting the morning primary task, not
  from playing it. Each triggers at most once per workday, so Production Ready
  cannot duplicate those bonus-XP grants.

### Delegation Trait Path

| Milestone | Locked effect |
|---|---|
| 3 XP | When claimed, choose one persistent Delegate. Their future positive relationship gains are doubled without changing their current relationship. On every workday, the Delegate contributes their relationship-scaled bonus once at workday start. |
| 6 XP | Choose a second persistent Delegate, who receives the same relationship and contribution benefits. The normal daily desk visitor is guaranteed to be one of the two Delegates. |
| 10 XP | Each Work on Task action alternates which Delegate works in the player's place and triggers only that Delegate's bonus. In every Team Meeting, each attending Delegate triggers their bonus twice. |
| Capstone: All Hands | At workday start, every coworker contributes once and each Delegate contributes a second time. Later Work and Team Meeting triggers retain their normal 10 XP behavior rather than being doubled again. |

- Delegation-triggered Work actions visibly animate the applicable Delegate
  working instead of the player.
- Delegation's start contributions, Work triggers, and Team Meeting triggers
  are Forced Bonus Activations and do not consume Standard Bonus Opportunities.
- The Delegate Work alternation resets every morning and begins with the first
  Delegate chosen. Every Work Action Resolution, including repeats and
  triggered Work actions, advances it once.
- In a Team Meeting, an attending 10 XP Delegate receives two activations total
  for that resolution rather than a normal activation plus two more.
- All Hands consolidates the earlier start contribution into one Workday Event:
  every coworker contributes once in office-roster order, then each Delegate
  contributes once more in selection order. A Delegate therefore receives two
  start activations total rather than three.
- All Hands suppresses positive-stress components from every bonus it activates.
  Its complete contribution event is atomic and does not consume any Standard
  Bonus Opportunities.

### Agile Trait Path

`Velocity` is the uncapped number of favorable Team Meetings completed this
run, including meetings completed before the path is claimed. A favorable
meeting increases Velocity before using its new value for that meeting's
progress.

| Milestone | Locked effect |
|---|---|
| 3 XP | Meetings are 15 percent more likely to be favorable, raising the 50 percent base chance to 57.5 percent. Every Team Meeting grants project progress equal to Velocity; favorable meetings first add 1 Velocity. |
| 6 XP | Meetings are 30 percent more likely to be favorable instead of 15 percent, for a 65 percent total chance. Schedule one guaranteed Daily Stand-Up before the normal actions every workday, including during the final two deadline days. |
| 10 XP | Meetings are 45 percent more likely to be favorable instead of 30 percent, for a 72.5 percent total chance. Every Work on Task action grants its normal progress plus additional project progress equal to Velocity. |
| Capstone: Continuous Delivery | Meetings are 60 percent more likely to be favorable instead of 45 percent, for an 80 percent total chance. Every favorable Team Meeting immediately performs one free Work on Task action. The free Work receives the 10 XP Velocity bonus but cannot generate another meeting. |

- Agile's favorable-meeting increases are relative to the 50 percent base:
  `base chance * (1 + increase)`. The milestone values replace rather than
  stack with each other.
- Agile uses Velocity as its only path-specific counter.

### Leadership Trait Path

`Team Briefing` is a Leadership-specific scheduled action. When the schedule
locks, bind it to the next eligible non-Briefing action. When it resolves, that
bound action resolves again with its full effects and triggers. Team Briefing
has no separate progress, stress, or resource effect.

| Milestone | Locked effect |
|---|---|
| 3 XP | After choosing the primary task, reveal the workday schedule. The player may replace one ordinary non-Lunch action with Team Briefing. Bind it to the next eligible non-Briefing action; that target resolves one additional time. |
| 6 XP | The player may replace up to two ordinary non-Lunch actions with Team Briefings. Adjacent Briefings may target the same following action. |
| 10 XP | Each Team Briefing makes its target resolve two additional times instead of one. |
| Capstone: Executive Alignment | For each available Team Briefing, independently choose whether it replaces an eligible ordinary action or is inserted into the schedule as a bonus action. |

- Team Briefings are optional, so the player may preserve the original schedule.
- Replacement mode can remove an unwanted ordinary action. Bonus mode preserves
  the original action and increases the total schedule length.
- Lunch and hostile manager actions cannot be replaced by Team Briefing.
- Lunch and hostile actions are also skipped when finding a Team Briefing's
  target. A Triggered Schedule Entry inserted during playback cannot take or
  change that target.

### Eye For Detail Trait Path

Each task card tracks its own uncapped `Polish`, equal to the number of times
that exact task has been completed this run, including plays before the path is
claimed. Polish increases immediately after each play resolves. The current
play uses the previous Polish value, while later copies played during the same
morning use the new value.

| Milestone | Locked effect |
|---|---|
| 3 XP: Revision | Each morning, pin yesterday's selected task for that morning. When selected, a task gains 1 base project progress per existing Polish. |
| 6 XP: Refinement | The base-progress bonus becomes 1.5 per Polish. The task's positive numeric printed effects also increase by 5 percent per Polish. |
| 10 XP: Precision | The base-progress bonus becomes 2 per Polish. Positive numeric printed effects instead increase by 10 percent per Polish. |
| Capstone: Masterpiece | Permanently pin one previously completed task. Both of its Polish bonuses are applied twice when it is played. |

- Positive numeric printed effects include project progress, pay, recovery, and
  relationship gains. Polish does not multiply action counts, choice counts,
  guaranteed outcomes, or other nonnumeric clauses.
- Revision's pin expires when that morning's task choice closes. Masterpiece's
  pin is permanent.

### Moodboard Trait Path

`Focus` is a protective resource generated by actual stress recovery. Focus
absorbs final stress after floor-pressure scaling at a one-to-one rate.

| Milestone | Locked effect |
|---|---|
| 3 XP: Centered | Actual stress recovery also grants an equal amount of Focus, capped at 10. Focus lasts until consumed or through the end of the next workday. |
| 6 XP: Inspired | Increase the Focus cap to 20. Every point of Focus consumed also grants 1 project progress. |
| 10 XP: Creative Flow | Remove the Focus cap. Unused Focus carries between workdays instead of expiring. |
| Capstone: Flow State | Lights Out occurs automatically every night without consuming the Home choice. Focus spent during a workday refreshes at the start of the next workday instead of disappearing. |

- Only stress actually recovered generates Focus; attempted recovery while at
  zero stress does not.
- Moodboard is Design's broad support path. Its 3 XP milestone is intended to
  be an attractive survival investment for many builds, while deeper investment
  converts recovery into progress and eventually a renewable daily shield.

### Brand Strategy Campaign Structure

- Brand Strategy is a highly conditional, hidden trait path.
- The Special task `Rebrand Initiative` is the only way to unlock the
  path. It has 10 base project progress, generates 10 base stress, grants no
  family XP, and its first play unlocks Brand Strategy immediately.
- `Rebrand Initiative` has no effect beyond activating the questline. Later
  copies do not grant Campaign progress or another standalone benefit.
- Brand Strategy has no 3, 6, or 10 Design XP milestones.
- Track Brand Strategy with a `Campaigns Completed` stat rather than Brand
  Equity.
- Every Campaign has its own name and an ordered sequence of specific task
  cards chosen to reflect a plausible real-world workflow.
- Campaigns become progressively longer as the questline advances.
- The questline contains four Campaigns with 3, 4, 5, and 6 ordered tasks
  respectively, for 18 required tasks in total.
- The four Campaigns, in order, are `Brand Research`,
  `Identity Development`, `Rebrand Launch`, and `Market Expansion`.
- A Campaign may repeat job families or omit families; completing all five
  families is not a universal requirement.

| Campaign | Step | Required task | Family |
|---|---:|---|---|
| Brand Research | 1 | Brand Audit | Operations |
| Brand Research | 2 | Customer Interviews | Sales |
| Brand Research | 3 | Creative Brief | Design |
| Identity Development | 1 | Stakeholder Alignment | Management |
| Identity Development | 2 | Brand Positioning | Sales |
| Identity Development | 3 | Visual Identity | Design |
| Identity Development | 4 | Rollout Playbook | Operations |
| Rebrand Launch | 1 | Go-to-Market Plan | Management |
| Rebrand Launch | 2 | Campaign Creative | Design |
| Rebrand Launch | 3 | Website Refresh | Coding |
| Rebrand Launch | 4 | QA | Coding |
| Rebrand Launch | 5 | Press Launch | Sales |
| Market Expansion | 1 | Competitive Research | Sales |
| Market Expansion | 2 | Expansion Strategy | Management |
| Market Expansion | 3 | Campaign Localization | Design |
| Market Expansion | 4 | Regional Platform | Coding |
| Market Expansion | 5 | Rollout Logistics | Operations |
| Market Expansion | 6 | Partner Launch | Sales |

- Campaign tasks are not added to the ordinary roster or guaranteed as
  additional morning offers.
- While a Campaign is active, generate the ordinary candidate for each
  generated offer slot first. Guaranteed-family slots use their guaranteed
  family and can satisfy the current Campaign step.
- If one or more generated candidates belong to the required family, choose
  one matching slot uniformly at random and replace its card with the required
  Campaign task. The discarded card may be any rarity, including Legendary.
  Never show more than one copy of the required Campaign task.
- Protect the designated Campaign task from Special replacement. Check the
  remaining eligible generated slots for a Special in display order under the
  normal at-most-one rule.
- Apply this procedure to initial offers, ordinary generated extensions, and
  every free or paid full task-list reroll. Pinned Tasks are never replaced by
  Campaign generation.
- Balance each required Campaign task between ordinary Common and Uncommon
  power. It should provide enough immediate value to keep the player afloat on
  early floors without matching a true Uncommon card's upside.
- Every Campaign task has the `Campaign` label instead of Common, Uncommon,
  Rare, or Legendary. It does not inherit the rarity of the card it replaces.
  Campaign tasks receive family-wide and generic card-play effects but do not
  satisfy mechanics that explicitly require an ordinary printed rarity.
- Every Campaign task has 10 base project progress, generates 10 base stress,
  grants 1 XP to its displayed family, and receives its family's Campaign
  Bonus.

| Family | Locked Campaign Bonus |
|---|---|
| Coding | Gain 5 project progress. |
| Management | Gain 1 project progress per final locked Schedule Entry today. |
| Design | Gain 2 project progress and recover 2 stress. |
| Sales | Gain 2 project progress and $100 at Clock Out. |
| Operations | Gain 3 project progress and guarantee at least one Work on Task action today. If none is naturally scheduled, replace one eligible ordinary non-Lunch, non-hostile action rather than adding an entry. |

- Management counts the final locked schedule once. Repeats, Triggered
  Schedule Entries, and Workday Events do not increase its value.
- The current Campaign multiplier scales only flat numerical outputs belonging
  to the Campaign Bonus. It does not alter the card's original printed effect,
  base progress, base stress, family XP, costs, penalties, thresholds, caps,
  percentages, durations, probabilities, guarantees, or action, card, choice,
  replay, and resource counts.
- The 2x, 2.5x, 3x, and 4x values are successive total Campaign Bonus
  multipliers rather than bonuses that multiply each other.
- Preserve fractional project progress produced by the 2.5x multiplier and
  display it to one decimal place rather than rounding it.
- Only primary morning tasks can satisfy Campaign steps.
- Rerolling away a required Campaign task does not fail or complete its step.
  Selecting another task does not reset, regress, or fail the Campaign.
  Ordered progress persists across workdays, floors, Weekends, and promotions.
- An active Sales Cycle overrides the morning offer and pauses Campaign
  progress. The Campaign resumes unchanged after the Cycle ends.
- Outside an active Sales Cycle, the designated Campaign task remains eligible
  to become the Hot Lead. Selecting it both advances the Campaign and begins
  the Sales Cycle for the following morning.
- If the required primary task completes a Campaign, activate its reward before
  the workday. Brand Research's new free reroll becomes usable starting the
  following morning.
- Every completed Campaign grants a bonus, with later Campaign rewards becoming
  substantially more powerful.
- Completing `Brand Research` permanently grants one additional free task-list
  reroll every morning, sets Campaign Bonuses to 2x strength,
  and immediately grants 30 project progress.
- Completing `Identity Development` immediately grants $2,000, increases the
  Campaign Bonus multiplier to 2.5x, and immediately grants 40 project
  progress.
- Completing `Rebrand Launch` increases the Campaign Bonus multiplier to 3x,
  unlocks family-specific rewards for advancing Campaign steps, and
  immediately grants 50 project progress.
- After `Rebrand Launch`, completing the required primary task for the current
  Campaign step grants the following fixed reward for its family:
  - Coding: gain 15 project progress.
  - Management, `Department Coordination`: choose one of the other four
    families' Campaign-step rewards and gain it immediately.
  - Design: recover 10 stress at Clock Out.
  - Sales: gain $300 and choose one coworker to gain 5 relationship.
  - Operations: gain one additional free task-list reroll the following
    morning.
- Campaign-step rewards trigger only when the correct primary task advances the
  active Campaign. They trigger at most once per workday and are not increased
  by the Campaign Bonus multiplier.
- Completing `Market Expansion` gives every ordinary family task the Campaign
  tag while preserving its printed rarity and effect, increases Campaign
  Bonuses to 4x, allows the player to play up to two Campaign cards each
  workday, and immediately grants 50 project progress.
- The morning selection remains the primary Complete Play. The player may add
  one distinct Campaign card as a Complete Additional Play. Both cards resolve
  their normal base values, printed effects, family XP, counters, and triggers,
  then receive their 4x family Campaign Bonuses. Only the primary satisfies
  Selection and can advance the active Campaign.
- Choose and lock both cards before either resolves. Every distinct Campaign
  card visible in the generated offer or Pinned Task drawer is eligible.
  Resolve the primary and its complete generated Resolution Chain first, then
  resolve the Complete Additional Play and its chain.
- A Hot Lead used as the Complete Additional Play resolves normally but does
  not begin a Sales Cycle because it does not satisfy Selection.
- After `Market Expansion`, choose the next Campaign uniformly at random from
  all four named Campaigns. Immediate repeats are allowed. Repeat only its
  ordered task sequence, not its original milestone reward. Completing it
  grants 50 project progress and immediately rolls another Campaign.
- The first Campaign's free reroll generates another normal offer and does not
  guarantee the family required by the current Campaign step. It stacks with
  free rerolls from Automation and other sources.
- Completing the full questline should make the player heavily favored to win,
  comparable to a major high-risk cashout archetype.
- Brand Strategy provides no passive or quest benefit before the first Campaign
  is completed.
- Brand Strategy can coexist with Eye for Detail or Moodboard.
- The final Campaign reward is Brand Strategy's capstone and consumes the run's
  single capstone slot. It cannot activate if another path has already claimed
  that slot.
- If another path owns or reserves the capstone before Market Expansion begins,
  Market Expansion does not begin. If another path reserves the capstone while
  Market Expansion is active, stop that Campaign immediately. Previously
  earned Brand Strategy rewards remain active.
- If Market Expansion's final Complete Play creates Brand Strategy and another
  capstone candidate atomically, use the locked simultaneous-candidate
  comparison. Brand Strategy's final reward activates only if it wins.

### Negotiation Trait Path

- Build Negotiation around increased workday pay and powerful Sales-exclusive
  purchases offered during the night phase.
- Present these purchases through a dedicated Deal Desk rather than mixing them
  into or diluting the ordinary Home-card offer.
- Buying a Deal is an additional night action. It does not consume a Home
  choice, the outing, or Lights Out.
- Do not give Negotiation an additional ordinary night or Home choice. Reserve
  that effect for another Sales trait path.
- When a purchased Deal schedules a Client Call for the following workday, that
  Call grants 1 project progress per $25 of the Deal's listed price, capped at
  30 project progress.
- Show the calculated Client Call result directly on the Deal card, for example
  `$500 - Client Call tomorrow (+20 progress)`.
- Deal-strength multipliers, including Negotiation's capstone, do not
  increase Client Call progress.

| Milestone | Locked effect |
|---|---|
| 3 XP | Gain $100 workday pay. The Deal Desk offers three Deals every night; buy up to one. |
| 6 XP | The pay bonus becomes $200. Earn 20 percent more interest. Reroll the three Deal offers once per night for free. |
| 10 XP | The pay bonus becomes $300. Earn 50 percent more interest instead of 20 percent. Every purchased Deal schedules its Client Call for the following workday. |
| Capstone: Full Signing Authority | Deals are twice as strong. Buy up to two different Deals per night. Unlock Scope Renegotiation. |

- The pay bonuses replace rather than stack with the earlier milestone values.
- The interest bonuses multiply the final interest payout and replace rather
  than stack with each other.
- Purchasing Market Intelligence opens a picker containing all five task
  families. The selected family is guaranteed to occupy at least one random
  slot in the following morning's task offer.
- Success Fee costs $300. If the immediately following workday completes the
  current project, gain $1,500 at Clock Out; otherwise it pays nothing.
  Negotiation's capstone doubles the payout to $3,000. Its listed price still
  schedules a 12-project-progress Client Call at 10 XP.
- Escalation Coverage grants 1 persistent charge per normal purchase and 2
  charges when strengthened by Negotiation's capstone, to a maximum of 3.
- Escalation charges persist across workdays, floors, weekends, and promotions
  until consumed.
- An unfavorable Lunch, Office Chat, or Team Meeting; Slumped at Desk stress;
  sabotage; or a hostile manager action with a direct negative effect
  automatically consumes 1 charge and has its entire negative outcome
  neutralized. The event does not become favorable.
- Escalation Coverage does not trigger on base task stress, printed task or
  trait costs, passive daily manager stress, rival progress, or a Pointless
  Meeting with no direct numerical effect.
- A Deal that modifies a named workday action must also guarantee at least one
  instance of that action during the affected workday. Productivity License
  therefore guarantees at least one Work on Task action tomorrow.

#### Deal Catalog

- Make all eight standard Deals available as soon as Negotiation reaches 3 XP
  and use the individual relative weights shown below.
- Show three distinct Deals each night. Never show duplicate copies of one Deal
  in the same offer.
- At 6 Sales XP, the free Deal reroll replaces the entire three-Deal offer with
  a fresh weighted draw. Draw without replacement within the new offer, but
  Deals from the original offer may appear again.
- The reroll may be used before or after a purchase. Exclude every Deal already
  purchased that night from the new offer. It affects only the Deal Desk,
  expires at Lights Out, and cannot be banked.
- A Deal is a one-time purchase. It does not occupy a Home slot or permanently
  modify the player unless its text explicitly says otherwise.
- At the capstone, use each Deal's explicit doubled effect below. Do not double
  its price, duration, trigger count, or Client Call progress.
- The capstone's two nightly purchases must be different Deals.

| Deal | Weight | Initial offer | With free reroll |
|---|---:|---:|---:|
| Wellness Stipend | 1.10 | 51.5% | 76.5% |
| Conference Pass | 1.00 | 48.1% | 73.0% |
| Market Intelligence | 0.90 | 44.4% | 69.0% |
| Escalation Coverage | 0.85 | 42.4% | 66.8% |
| Productivity License | 0.75 | 38.3% | 61.9% |
| Facilitated Workshop | 0.65 | 34.0% | 56.4% |
| Contractor Support | 0.45 | 24.5% | 43.1% |
| Success Fee | 0.30 | 16.8% | 30.9% |

The offer percentages are approximate inclusion rates when drawing three
distinct Deals. The reroll column assumes the player keeps an initial hit and
uses the 6 XP free reroll after a miss.

| Deal | Price | Normal effect | Capstone effect | 10 XP Client Call |
|---|---:|---|---|---:|
| Wellness Stipend | $250 | Immediately recover 10 stress. | Recover 20 stress. | +10 progress |
| Conference Pass | $300 | Choose one coworker to gain 6 relationship. | That coworker gains 12 relationship. | +12 progress |
| Market Intelligence | $300 | Open the family picker and choose one. Guarantee one random task-offer slot from that family tomorrow morning. | Guarantee two random slots from that family. | +12 progress |
| Success Fee | $300 | If the next workday completes the current project, gain $1,500 at Clock Out. | Gain $3,000 instead. | +12 progress |
| Escalation Coverage | $350 | Gain 1 Escalation charge, up to 3. A charge automatically neutralizes the next qualifying harmful workday effect. | Gain 2 charges, still capped at 3. | +14 progress |
| Productivity License | $350 | Guarantee at least one Work on Task action tomorrow. Every Work action gains 3 project progress. | Keep the guarantee; each Work action gains 6 progress. | +14 progress |
| Contractor Support | $500 | Add two bonus Work on Task actions tomorrow. | Add four bonus Work on Task actions. | +20 progress |
| Facilitated Workshop | $500 | Add one guaranteed favorable Team Meeting tomorrow. | Add two guaranteed favorable Team Meetings. | +20 progress |

`Scope Renegotiation` costs $1,500, adds one workday to the current project, and
can be purchased only once per floor. It is not strengthened by the capstone.
At 10 XP it still schedules a Client Call for 30 project progress.

- Wellness Stipend uses actual stress recovery and therefore can generate Focus
  through Moodboard.
- Conference Pass is a positive relationship gain and therefore receives
  Delegation's relationship-gain multiplier for a chosen Delegate.
- Market Intelligence applies to randomly generated offer slots and can cause a
  matching Brand Strategy Campaign task to replace the guaranteed family card.
- Success Fee checks project completion during the immediately following
  workday and pays only once.
- Productivity License applies to ordinary and bonus Work on Task actions,
  including actions added by Contractor Support and traits.
- Scope Renegotiation's extra day is independent of the ordinary once-per-floor
  favorable-meeting deadline extension.

### Schmoozing Trait Path

- A non-rival coworker becomes a `Contact` at 20 relationship.
- Paid Outings grant 1 additional relationship per $50 spent.
- After choosing the primary task, Schmoozing may designate one other visible
  card as a secondary task. The player's permanent Contact team helps with it.
- Each unlocked Schmoozing team slot is filled by one eligible Contact. Once
  chosen, that Contact persists in the team for the rest of the run and can
  never be replaced or removed.
- If a team slot unlocks before an eligible Contact exists, it remains empty
  and pending. It never blocks Promotion Review or another phase transition.
- At any non-workday phase, the player may use the Resume Book to fill a
  pending slot with any currently eligible unassigned Contact. The player may
  leave a slot empty to wait for a different Contact. Once confirmed, the
  choice remains irreversible.
- Each team Contact contributes an Assist percentage equal to their current
  relationship. Their percentages and applicable Contact specialties are
  combined before applying the milestone's Assist cap.
- The secondary task grants only its calculated share of projected project
  progress. It applies no task stress, activates no printed non-progress
  effects, and ordinarily grants no family XP, Campaign progress, Polish,
  Codebase, Combo, or card-play triggers.
- Show the complete calculated secondary contribution before confirmation and
  visibly animate the assigned Contacts helping during workday playback.

| Milestone | Locked effect |
|---|---|
| 3 XP | Unlock the first permanent Contact-team slot. The team assists one secondary task. Combined Assist is capped at 100 percent. |
| 6 XP | Unlock a second permanent Contact-team slot. Combined Assist is capped at 200 percent. |
| 10 XP | Unlock a third permanent Contact-team slot. Remove the Assist cap. |
| Capstone: Inner Circle | After selecting the primary task, choose up to two other cards that a normal Schmoozing Assist could target. Every Contact on the permanent team applies their Assist percentage and specialty to each chosen secondary task. If only one legal target exists, assist only that card. |

Each Contact has a distinct Schmoozing specialty. These do not activate or
duplicate the coworker's ordinary relationship-scaled desk-visit bonus.

| Contact | Specialty | Locked effect |
|---|---|---|
| Karen | Coordination | Her Assist percentage doubles when the primary and secondary tasks share a family. |
| Dave | Cross-functional help | His Assist percentage doubles when the primary and secondary tasks belong to different families. |
| Bob | Practical work | His Assist percentage doubles for Common secondary cards. |
| Janet | Quality review | Her Assist percentage doubles for Rare or Legendary secondary cards. |
| Raj | Expense account | Pay $100 to add his Assist percentage a second time that workday. |
| Priya | Mentorship | If combined Assist reaches at least 100 percent, the secondary task grants 1 XP to its family despite the ordinary secondary-task XP restriction. |

### Closing Trait Path Foundation

- Build Closing around a self-contained, push-your-luck `Sales Cycle`.
- Outside a Sales Cycle, mark one random card in the ordinary morning offer as
  the `Hot Lead`. Selecting it plays that actual card normally for the current
  workday and enters the Sales Cycle beginning with the following morning.
- Selecting the Hot Lead begins the Sales Cycle at actual Chain 0. The first
  Sales Cycle card selected on a later morning reaches actual Chain 1.
- A Sales Cycle persists across multiple workdays rather than resolving as a
  same-morning loop.
- An active Sales Cycle persists through project completion and promotion to a
  later floor. It ends only through `Close`, burnout, or the end of the run.
- While the Sales Cycle is active, generate two underlying ordinary task cards
  each morning and replace each with a Sales Cycle card corresponding to that
  card's family. The third option is always `Close`.
- Sales Cycle cards have top offer priority and override every ordinary,
  guaranteed, fixed, Campaign, trait-added, or otherwise special task card.
- Selecting a Sales Cycle card makes it the current day's task, starts workday
  playback, and continues the Cycle into the following morning. It grants 10
  base project progress, generates no ordinary task stress, adds increasingly
  higher Sales Cycle stress as the chain grows, and grants no family XP.
- Apply each Sales Cycle card's floor-scaled stress immediately when it is
  selected. If the player's stress reaches 100 during the Cycle, the player
  burns out immediately before they can choose `Close`, gain its reward, bank
  pending Seasoned stacks, or receive Seasoned recovery.
- The Cycle card at actual Chain `N` generates `N + 1` base stress, producing
  the default per-card sequence `2, 3, 4, 5, 6, 7, 8, 9, 10...`. Apply the
  normal 20 percent floor stress scaling after all applicable Cycle modifiers.
- `Clean CRM` subtracts 1 base stress from each Cycle card before floor
  scaling. With `Seasoned Closer`, escalation increases after every second card
  instead, producing `2, 2, 3, 3, 4, 4, 5, 5...` before other modifiers.
  Acquiring Seasoned Closer does not retroactively reduce stress already paid
  during its acquisition Cycle.
- Closing ends the cycle and grants rewards based on how long the player kept
  the chain running.
- Selecting `Close` consumes that workday and does not return the player to an
  ordinary task offer that morning.
- The Close reward resolves immediately, then the normal AFK workday schedule
  plays without a primary task. The player receives no task base progress,
  task stress, printed task effect, or family XP from `Close`; ordinary
  scheduled actions and non-task daily systems still resolve.
- When the player cashes out through `Close`, automatically roll one random
  reward from the reward table corresponding to the final Chain. A normal
  cashout does not let the player select a reward.
- Use four Close reward tables: `Nurturing` at Chain 1-2, `Qualifying` at Chain
  3-4, `Presenting` at Chain 5-7, and `Enterprise` at Chain 8 or higher. Later
  tables contain substantially stronger and more unusual outcomes.
- `Portfolio Expansion` remains the exception: it rolls two random rewards
  from the earned table and lets the player choose one. The guaranteed
  one-time `Anchor Account` option at Chain 9 also remains an exception.
- Scale applicable Close reward values with the current floor so an outcome
  remains relevant throughout the run.
- Close rewards may grant persistent benefits. Add those benefits directly to
  the Closing trait for the remainder of the run.
- Every persistent Closing reward is unique. After it is acquired, remove it
  from every normal Close roll, Portfolio Expansion lower-tier roll, and
  roll-two choice in which it could appear, then renormalize the remaining
  eligible weights.
- One-time Close rewards remain in their eligible tables and may be gained
  repeatedly.
- When Portfolio Expansion is first acquired, choose Nurturing or Qualifying
  with equal probability, then roll from that tier's current eligible weighted
  pool. Apply normal unique-reward removal and weight renormalization before
  the roll.

The following persistent Close rewards are locked:

| Reward | Minimum Chain | Locked effect |
|---|---:|---|
| Clean CRM | 2 | Future Sales Cycle cards generate 1 less base stress. |
| Preferred Account | 4 | Future Sales Cycles count as starting at Chain 1 for reward eligibility but not for stress. The first Cycle-card selection therefore reaches Chain 2 rewards. |
| Seasoned Closer | 6 | Sales Cycle stress escalation increases after every second Cycle card instead of after every card. It also unlocks the permanent Seasoned stack engine defined below. |
| Portfolio Expansion | 6 | Immediately roll and gain one random reward from any lower-tier Close table. Future Closes reveal two rewards from the earned table; choose one. |
| Joint Venture | 8 | Immediately gain project progress equal to 50 percent of Chad's current progress. Whenever Chad gains project progress, gain progress equal to 50 percent of his final gain after all bonuses. |
| Master Services Agreement | 8 | Add one workday to the current project and every future project. Reduce the required size of the current project and every future project by 25 percent. |
| Executive Air Cover | 8 | The player is immune to every manager modifier and hostile manager action for the rest of the run. Chad and all manager effects that benefit him remain unchanged. Add one Executive Support bonus action every workday and convert harmful workday events into Executive Support. |
| Burnout Insurance | 8 | Permanently recover `10 + (5 * floor)` stress at every Clock Out. Also gain one Guardian Angel: the next time stress reaches 100 percent, resolve it before burnout, consume only the Guardian Angel, and set stress to 75 percent. The daily recovery remains active. |
| Key Account Status | 8 | Every future Sales Cycle starts at actual Chain 4. The player may Close immediately for a Qualifying reward, the first selected Cycle card resolves as Chain 5, and five selected Cycle cards reach actual Chain 9. |
| Anchor Account | 9 | Choose one family. Immediately gain family XP equal to the current floor. Future ordinary primary tasks from that family grant 1 additional family XP. |

- At Chain 9, `Anchor Account` becomes a guaranteed one-time Close option until
  it has been acquired, but only if Closing owns or can still claim the run's
  capstone.
- Closing's first successful Close at actual Chain 9 acts as the path's
  capstone trigger and claims the run's single capstone slot. Preferred
  Account's virtual reward-eligibility Chain cannot satisfy this trigger.
- If another path already owns the capstone, Closing can still reach actual
  Chain 9 for stress, Seasoned stacks, best-Chain tracking, and an Enterprise
  reward, but it cannot claim another capstone or offer `Anchor Account`.
- `Seasoned Closer` begins accumulating pending Seasoned stacks at actual Chain
  4. Each additional Cycle card adds another pending stack, so actual Chains
  4, 5, 6, and 7 offer 1, 2, 3, and 4 stacks respectively.
- Choosing `Close` at actual Chain 4 or higher banks all pending Seasoned stacks
  permanently. Newly banked stacks apply to that same Close. Acquiring
  `Seasoned Closer` at Chain 6 or higher retroactively counts the current Sales
  Cycle.
- After banking, a qualifying Close grants project progress equal to total
  Seasoned stacks multiplied by the actual Chain. After the Sales Cycle ends,
  recover 2 stress per total Seasoned stack.
- Seasoned calculations use actual Chain and its corresponding pending-stack
  count. `Preferred Account` affects reward eligibility only and does not
  provide free pending stacks or increase the Seasoned payout.
- `Key Account Status` starts at actual Chain 4. With Seasoned Closer, it
  creates the normal pending Chain 4 Seasoned stack, and an immediate Close
  banks that stack.
- Once Closing is selected, continue tracking Sales XP internally for
  cross-family effects but replace its visible segmented Sales XP bar with a
  dedicated `Deal Ladder`.
- The Deal Ladder has nine stable segments grouped by reward tier: Chains 1-2
  are `Nurturing`, 3-4 are `Qualifying`, 5-7 are `Presenting`, and 8-9 are
  `Enterprise`. Mark segment 9 with a star to communicate Closing's capstone
  threshold.
- Outside a Sales Cycle, the Deal Ladder shows the player's best actual Chain.
  During a Sales Cycle, it fills to the live actual Chain and shows both the
  exact final stress of the next Cycle card and the Close reward tier currently
  available. Preferred Account may raise the displayed reward tier without
  filling additional actual-Chain segments.
- Keep total permanent Seasoned stacks visible beside the Deal Ladder. Show
  acquired persistent Closing rewards as compact tags beneath it, with their
  full effects available in the Resume Book.

#### Close Resolution Order

- The Hot Lead's family counts as represented during its Sales Cycle, along
  with every family represented by a selected Sales Cycle card.
- A player may select `Close` at actual Chain 0 to abandon the Cycle. Unless
  Preferred Account or Key Account Status supplies reward eligibility, this
  grants no Close reward and still consumes the workday.
- Without Preferred Account, reward eligibility uses actual Chain. With
  Preferred Account, calculate reward Chain as the greater of actual Chain and
  `1 + the number of Sales Cycle cards selected during this Cycle`. Key Account
  Status's actual Chain 4 start and Preferred Account's virtual Chain 1 start
  do not add together.
- Selecting `Close` freezes actual Chain, reward Chain, represented families,
  and the current reward presentation. The player cannot continue the Cycle
  after seeing or rerolling the final reward presentation.
- On a successful actual Chain 9 Close, Closing claims the run's capstone if
  the slot is still available. If `Anchor Account` has not been acquired and
  Closing owns or can claim the capstone, add it as a guaranteed option beside
  the random Enterprise reward presentation.
- A normal Close reveals one eligible weighted reward from the earned table.
  With Portfolio Expansion, reveal two distinct eligible rewards from that
  table and choose one. If fewer than two distinct rewards remain, reveal every
  eligible reward that remains. Anchor Account is an additional option, and
  choosing it forfeits the random reward or Portfolio choices from that Close.
- Discovery Complete pre-rolls and reveals the entire random reward
  presentation behind `Close`, including both Portfolio Expansion choices.
  Selecting a Sales Cycle card instead of `Close` discards that presentation;
  the following morning rolls and reveals an entirely new presentation for the
  then-current reward tier.
- Champion tokens may be spent only after selecting `Close` and freezing the
  Cycle. The player may spend any number of banked tokens, one at a time. Each
  token replaces one chosen random top-level reward; the replaced result is
  permanently discarded. With Portfolio Expansion, the player chooses among
  the final displayed options after all desired rerolls.
- Champion tokens cannot reroll Anchor Account, Enterprise Dividend, or an
  immediate nested reward granted by Preferred Account or Portfolio Expansion.
- After rerolls, accept or choose one top-level reward and resolve it
  immediately, including any choices and nested reward it grants. A newly
  acquired persistent reward is removed from future pools at once.
- The current Cycle's previously paid stress is never recalculated. Clean CRM,
  Preferred Account, and Key Account Status affect future Cycles. Seasoned
  Closer is the exception: if acquired by this Close, it retroactively enables
  the current Cycle's pending Seasoned stacks.
- After the accepted reward and its nested reward finish resolving, bank all
  eligible pending Seasoned stacks. Then grant Seasoned project progress, then
  grant Seasoned stress recovery.
- End the Sales Cycle and begin the locked no-primary-task Close workday.

#### Closing Reward Rules

The tier assignments, weights, and exact values are Locked in the four tables
below. Apply these shared edge-case rules:

- `Anchor Account` remains a separate guaranteed one-time Chain 9 option rather
  than a weighted Enterprise-table entry.
- Executive Sponsor snapshots the awarding Close's actual Chain. Preferred
  Account's virtual reward-eligibility Chain does not increase its multiplier.
  Its two bonus visits do not replace the normal visitor or Delegation's
  guaranteed visitor.
- Each Executive Sponsor visit creates one Forced Bonus Activation using the
  coworker's relationship at that visit and multiplies the complete bonus
  package, including any stress drawback, by the snapshotted actual Chain.
  Resolve overlapping Sponsor visits from oldest to newest and preview the
  exact multiplied values when the coworker is chosen.
- Case Study provides the selected task independently on both mornings even if
  it was selected on the first. If the ordinary random offer naturally rolls
  that task, reroll the natural duplicate and preserve the Case Study pin.
- Pilot Approved suppresses only the paired Replay's duplicate of the primary
  card's own base and printed stress. Every separate Complete Play generated by
  either play, including cards generated by Hackathon or Parallel Processing,
  pays its normal modified stress.
- If another source such as Production Ready also adds a Replay, that Replay
  stacks additively and pays its normal stress. Pilot Approved's stress rule
  applies only to the one Replay created by Pilot Approved.

#### Locked Nurturing Values And Weights

| Reward | Weight | Locked value |
|---|---:|---|
| Follow-Up | 25 | Gain one free task reroll the following morning. |
| Account Notes | 25 | Choose a represented family and grant it 1 family XP. |
| Warm Introduction | 20 | Choose a non-Chad coworker and grant `2 + floor` relationship. |
| Post-Call Reset | 15 | Immediately recover `3 + floor` stress. |
| Clean CRM | 15 | Eligible at actual Chain 2 or higher; use its locked unique persistent effect. |

- At actual Chain 1, exclude Clean CRM and renormalize the other four weights.
  After Clean CRM is acquired, remove it and renormalize future Nurturing rolls
  as required by the global persistent-reward rule.

#### Locked Qualifying Values And Weights

| Reward | Weight | Locked value |
|---|---:|---|
| Qualified Referral | 25 | Choose a family represented during this Cycle. Tomorrow, guarantee that family in one offer slot and mark that card as the Hot Lead. |
| Internal Champion | 20 | Choose a coworker and gain `2 + floor` relationship. Gain one Champion token, to a maximum of two. After a future Close reward is rolled, spend a token to reroll it and accept the new result. |
| Discovery Complete | 25 | During the next Sales Cycle, reveal the exact reward currently behind Close. Continuing the chain replaces it with a newly rolled reward from the appropriate table. |
| Objection Handling | 20 | Gain two charges, to a maximum of four. Spend a charge before selecting a Cycle card to remove 3 base stress before floor scaling. |
| Preferred Account | 10 | Eligible at actual Chain 4 or higher; use its locked persistent effect and immediately grant one random repeatable Nurturing reward when first acquired. |

#### Locked Presenting Values And Weights

| Reward | Weight | Locked value |
|---|---:|---|
| Pilot Approved | 20 | Add one Replay to the next ordinary primary card. Pay that primary card's own base and printed stress only once across the original play and Pilot Replay; child card plays pay normally. |
| Executive Sponsor | 10 | Choose a coworker and gain `5 + floor` relationship. At the start of each of the next two workdays, they make a bonus desk visit and trigger their relationship-scaled bonus multiplied by the actual Chain of the awarding Close. |
| Case Study | 15 | Choose an ordinary task completed this run. It retains its rarity and full effects and is pinned independently on each of the next two mornings. |
| Launch Support | 25 | Add one bonus Work on Task action to each of the next two workdays. Each receives all normal Work-action and trait triggers. |
| Seasoned Closer | 20 | Eligible at actual Chain 6 or higher; use its locked unique persistent effect. |
| Portfolio Expansion | 10 | Eligible at actual Chain 6 or higher; use its locked unique persistent effect. |

- At actual Chain 5, exclude Seasoned Closer and Portfolio Expansion and
  renormalize the other four weights. Preferred Account's virtual reward Chain
  does not satisfy either reward's actual Chain 6 minimum.

#### Locked Enterprise Values And Weights

| Reward | Weight | Locked value |
|---|---:|---|
| Joint Venture | 20 | Immediately gain project progress equal to 50 percent of Chad's current progress. Whenever Chad gains project progress, after all of his bonuses are applied, gain project progress equal to 50 percent of that final amount. |
| Master Services Agreement | 20 | Add one workday to the current project and every future project. Reduce the required size of the current project and every future project by 25 percent. |
| Executive Air Cover | 20 | The player becomes immune to every manager modifier and hostile manager action for the rest of the run. Chad and manager effects that benefit him are unchanged. Add one automatic Executive Support bonus action every workday. A Slump, unfavorable Lunch, unfavorable Office Chat, unfavorable Team Meeting, sabotage, or hostile manager action becomes Executive Support instead. Executive Support randomly grants Strategic Push, Wellness Intervention, or Senior Sponsor. |
| Burnout Insurance | 20 | Permanently recover `10 + (5 * floor)` stress at every Clock Out. Also gain one Guardian Angel: the next time stress reaches 100 percent, resolve it before burnout, consume only the Guardian Angel, and set stress to 75 percent. The daily recovery remains active. |
| Key Account Status | 20 | Every future Sales Cycle starts at actual Chain 4. The player may Close immediately for a Qualifying reward, the first selected Cycle card resolves as Chain 5, and five selected Cycle cards reach actual Chain 9. With Seasoned Closer, the starting Chain 4 creates its normal pending stack and an immediate Close can bank it. |

- Executive Support outcomes are:
  - `Strategic Push`: gain `10 + (2 * floor)` project progress.
  - `Wellness Intervention`: recover `5 + (3 * floor)` stress.
  - `Senior Sponsor`: choose two distinct random non-Chad coworkers whose
    current bonus adds no stress and create one Forced Bonus Activation for
    each.
- Executive Air Cover does not convert base task stress, printed card costs,
  trait costs, or Sales Cycle stress.
- All five Enterprise rewards are equally weighted unique persistent rewards.
  Remove acquired rewards from the pool and renormalize the remaining rewards.
- After all five have been acquired, future Enterprise Closes grant
  `Enterprise Dividend`: gain project progress equal to 50 percent of the
  current project's remaining required progress and recover 50 percent of
  current stress, both rounded up.

### Efficiency Trait Path Foundation

`Standard Procedures` are guaranteed bonus actions appended to every workday.
They are selected only when their milestone is claimed, persist for the
remainder of the run, and remain visible during workday playback.

| Milestone | Locked effect |
|---|---|
| 3 XP: Daily Checklist | Work on Task becomes the first Standard Procedure. Add one guaranteed bonus Work action every workday. Every positive workday action grants 2 project progress. |
| 6 XP: Standard Operating Procedure | Choose Work on Task, Team Meeting, Water Cooler, or Office Chat as the second Standard Procedure. Duplicate choices are allowed. The positive-action bonus becomes 3 project progress. |
| 10 XP: Redundant Systems | Choose a third Standard Procedure from the same list. Standard Procedures cannot be removed, replaced, or cancelled by managers or other effects. The positive-action bonus becomes 5 project progress. |
| Capstone: Operational Excellence | Every Standard Procedure resolves twice with its full action and trait triggers. A repeated Procedure cannot recursively repeat itself. Each positive resolution retains the 5-project-progress bonus. |

- Lunch cannot be selected as a Standard Procedure because it is a fixed
  once-per-day special action with its own outcome rules.
- Positive workday actions include Work on Task, Water Cooler, favorable Lunch,
  favorable Office Chat, favorable Team Meeting, and beneficial special
  actions such as Client Call, Team Briefing, and Executive Support.
- Apply the Efficiency bonus once after each positive action resolution.
  Repeated and bonus actions can each trigger it when they resolve positively.
- Negative and neutral actions grant no Efficiency progress, but they do not
  reset a counter or remove progress earned by earlier positive actions.
- The 6 and 10 XP positive-action values replace rather than stack with the
  earlier milestone value.

### Logistics Trait Path Foundation

Logistics uses one committed stored-task slot rather than an expanding
multi-card inventory. After confirming the primary task, if the slot is empty,
the player may store one unselected ordinary task card.

| Milestone | Locked effect |
|---|---|
| 3 XP: Stockroom | A stored task can be selected as a future primary task. When played, it grants bonus project progress equal to `current floor * (2 + Turns Held) / 2`. |
| 6 XP: Consolidated Delivery | At 3 or more Turns Held, the stored task may be delivered alongside the primary task instead. It plays completely, including base progress, base stress, printed effects, family XP, counters, and triggers. |
| 10 XP: Bulk Fulfillment | The stored task may be delivered alongside the primary task at any age. Its complete printed effect resolves once normally plus one additional time for every 5 Turns Held. Base progress, base stress, family XP, counters, and card-play triggers still resolve once. |
| Capstone: Global Distribution | Replace Bulk Fulfillment's extra printed-effect resolutions with complete additional card plays. The stored card plays `1 + floor(Turns Held / 5)` times, and every play resolves base progress, base stress, printed effects, family XP, counters, and triggers. |

- A stored task persists across workdays and promotions. It cannot be
  discarded, replaced, or swapped, and the player cannot store another task
  until the current one is played.
- `Turns Held` starts at zero and increases by one at every Clock Out while the
  task is stored. Because storage occurs after confirming the current primary
  task, the earliest possible delivery on the following morning has one turn
  held.
- Use the current floor when the stored task is played. `Turns Held` has no
  cap.
- At 10 XP, every extra printed-effect resolution includes all positive and
  negative clauses printed on the card.
- Global Distribution's additional complete plays each apply their own card
  stress and progression. The separate Logistics delivery-progress bonus is
  granted only once per delivered stored task.

### Compound Interest Trait Path

One `Reserve Level` is granted for every $500 cash held. Calculate Reserve
Levels at workday start after all morning spending. Reserve benefits do not
consume cash.

| Milestone | Locked effect |
|---|---|
| 3 XP: Emergency Fund | Count up to 3 Reserve Levels. Each grants 2 project progress. Interest applies to up to $1,500. |
| 6 XP: Treasury Management | Count up to 5 Reserve Levels. Each grants 2 project progress and 1 stress recovery. Interest applies to up to $2,500. |
| 10 XP: Capital Allocation | Count up to 8 Reserve Levels. Each grants 3 project progress and 1 stress recovery. Interest applies to up to $4,000. |
| Capstone: Infinite Runway | Remove the Reserve-Level and interest-eligible-cash caps. Every Reserve Level grants 3 project progress and 1 stress recovery. |

- The 6 and 10 XP Reserve benefits and caps replace rather than stack with
  their earlier milestone values.
- Use the locked 15 percent base interest rate.
- Savings Account's additional $500 of interest-eligible cash stacks with the
  milestone caps before Infinite Runway removes the cap entirely.
- Negotiation's interest bonus multiplies the final interest payout after
  Compound Interest determines the eligible principal.
- Reserve recovery is actual stress recovery and can generate Focus through
  Moodboard.

## Historical Archive

Superseded designs and the complete pre-cleanup ledger are preserved through
`ARCHIVE_SUPERSEDED.md`.

## Open Questions

1. Define the remaining structural simulation matrix and tune F5 against the
   25-35 percent skilled-player win-rate target. Preserve the advanced suite's
   action-inflation result as a primary balance and readability watchpoint.
2. After the overhaul candidate passes full verification, design the Home set
   roster, thresholds, bonuses, prices, and resale tuning.
