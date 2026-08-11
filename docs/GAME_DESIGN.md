# OfficeWars Game Design

## Purpose

OfficeWars is a single-file office-themed autobattler about climbing seven
corporate floors before stress, deadlines, or a rival end the run.

This document describes the stable game model. Current numeric implementation
lives in `officewarsautobattler.html`; approved and proposed balance changes live
in `BALANCE_LEDGER.md`.

## Design Goals

- Support short bursts of player attention in an office environment.
- Put meaningful decisions at the morning, night, weekend, and promotion.
- Let the workday play autonomously with one cycling 1x, 2x, and 4x speed
  button plus Skip.
- Make builds legible through task Skills, permanent progression, homes, and
  relationships.
- Create varied runs without allowing a single unlucky roll to decide one.
- Target an approximately 25-35 percent win rate for a skilled player.
- Keep the complete game usable as one standalone HTML file.

## Run Continuity And Onboarding

OfficeWars keeps one versioned active-run save in browser storage. The main
menu offers Continue Run when that save is valid and requires confirmation
before a new run replaces it. Committed choices and stable phase transitions
autosave without allowing a refresh to reroll an offer or undo a cost.

A first-play contextual orientation teaches the basic journey through thirteen
short callouts. It covers the project race and stress, morning task anatomy,
the Resume, autonomous Workday controls, Clock Out, four focused Night Planner
lessons, the first three-path Promotion choice, the 6 and 10 XP milestones,
the first boss floor, and the first claimed Capstone. The Night sequence
separately teaches Home Shop, Outings, Relationships and coworker bonus timing,
then recovery, finalization, and the optional room interface. Conditional
Deals remain a discovery. Each callout spotlights its relevant existing
interface while darkening the rest of the screen. The first Workday pauses
once before playback and opens the live Action Guide, which explains Work on
Task, Lunch, Water Cooler, Office Chat, Slumped at Desk, and Team Meeting using
current values. Playback is not interrupted after it begins. Players can skip
the orientation at any step or reset it through Options for the next New Run.
The tutorial does not rig cards or outcomes, and advanced traits and card
interactions remain discoveries.

Options stores meta preferences separately from the active run. The current
screen provides a persistent master-volume setting for future audio and the
tutorial reset command.

If the page closes during a prepared Workday, continuing the run restores its
deterministic checkpoint and automatically skips the remaining playback to
Clock Out. Victory and defeat summaries persist across refreshes and return
cleanly to the main menu. Casino checkpoints preserve chips and active game
state; a pending Slots result settles exactly once after restoration. Sleep
settles before the sunrise presentation and writes a `nightResolved`
checkpoint, so refreshing during the transition advances the run without
applying recovery twice.

## Run Structure

The player climbs from Intern through the CEO's Office. Each floor assigns a
project with a required size and deadline. The player loses by:

- reaching 100 percent stress;
- missing the project deadline; or
- allowing the rival to complete the project first.

Completing a project promotes the player to the next floor. Beating the final
floor wins the run.

## Daily Loop

1. Morning: choose one task card from a generated set. Apply that task's
   immediate gains and losses when the selection is confirmed.
2. Workday: watch scheduled actions resolve automatically.
3. Clock Out: settle workday-triggered effects, ordinary pay, interest, and
   effects explicitly assigned to Clock Out.
4. Night: use available Outing, Home, and Deal actions in any legal order.
   Unless an effect explicitly provides an exception, manually selecting
   Lights Out forfeits Home and Deal purchases, while making either purchase
   makes manual Lights Out unavailable. Then explicitly finalize the night.
   If Lights Out is still legal and was not selected manually, finalization
   selects it automatically before applying sleep.
5. Weekend: after every fifth run-wide workday, resolve a mystery event or
   casino visit.
6. Promotion: carry the build forward and enter the next floor.

A surviving non-final project-completion day still proceeds through Night
before promotion. Completing the project does not discard effects or resources
that apply that night. Beating the final floor proceeds directly to victory.

After an ordinary surviving day, Night is followed by a Weekend when due and
then the next morning. After a non-final project completion, resolve Night,
promotion recovery, any due Weekend, promotion trait claims, and finally the
next floor. Promotion recovery occurs before the Weekend, while trait claims
occur afterward.

## Task Cards

Every ordinary task belongs to one of five job Skills:

- Coding;
- Management;
- Design;
- Sales; and
- Operations.

A task provides base project progress and stress plus a daily effect. Each
Skill contains ten reusable task cards: four Common, three Uncommon, two Rare,
and one Legendary, for 50 ordinary Skill cards total. Rarity belongs to the
card rather than being rolled separately. Cards have no universal rarity
multiplier or stress tax; each card is balanced around its explicit effect and
rarity.

Special cards sit outside the Skill roster and ordinary rarity distribution.
They can be generated only as slots in the standard morning task window,
including ordinary additional slots and standard task-list rerolls. Card-created
task windows, guarantees, and other effects cannot newly generate a Special
card. Each eligible generated slot has a 0.2 percent Special chance. Check slots
in display order and stop after the first success, allowing at most one Special
per generated window. Choose uniformly among currently eligible Specials. A
visible Special may be preserved during its current morning but cannot be
pinned into a future morning unless its own text allows it. `Rebrand
Initiative` is the first Special card and leaves the eligible pool after it
unlocks Brand Strategy.

For clarity, a selected task's direct gains and losses resolve when the player
confirms it rather than remaining projected until Clock Out. Effects explicitly
tied to a workday action, Clock Out, or a future day still resolve at their
stated trigger. Resolve the task's complete immediate package atomically, then
check for burnout. After that play resolves, immediately update its Skill XP
and card-progression counters; the resolving card cannot improve itself, but
later cards played during the same morning use the updated values.

Selecting a primary task is a separate event from playing a card. Every card
play is complete by default: it resolves base progress, base stress, the
printed effect, Skill XP, card-progression counters, and card-play triggers.
Replays and additional plays use that complete procedure but do not repeat the
morning selection or any primary-only trigger. Resolving only a copied printed
effect and calculating a Schmoozing Assist are not card plays. An effect may
explicitly suppress one component of a Complete Play; Automation's additional
Combo cards are the current exception and grant no Skill XP.

Each independent effect that says to play a card twice adds one Replay.
Multiple such effects add their Replays rather than multiplying the total play
count.

Copied effects may contain another copy effect, but every copy branch tracks
its active Source cards and cannot use the same Source twice. An effect whose
entire value is explicitly bound to its own card identity cannot be selected
as a copy Source. `Iteration Pass` is the only current identity-bound ordinary
effect; `API Integration` instead redirects the Host card's pending Skill XP.

A selection and everything it generates form one ordered resolution chain.
Finish each card play before starting the next. Reaching the required project
progress marks the project complete but does not interrupt that chain; remaining
plays still resolve for their effects and progression, and promotion waits
until after the workday. Burnout ends the chain and discards everything in it
that has not begun resolving.

Morning offerings weight all five Skills equally at 20 percent and may show
more than one card from the same Skill, but never duplicate the same task in
one offer. A task card can appear again on later workdays. Every completed
ordinary task grants one XP to its Skill regardless of rarity,
immediately after that play resolves unless its source explicitly suppresses
Skill XP.

Every separate window that asks the player to choose a task uses the Morning
task-card visual language. A Complete Play or future primary choice shows
stats and effect text. A copied-effect source shows effect text without stats,
a Schmoozing Assist target shows only the stats used by the Assist, and a
category-only choice shows only Skill, rarity, and name.

When active run state can change the value of a Morning decision, a compact
Build Context strip appears above the task offer. It names active delayed
effects, their selected targets, Delegates, Contacts, and other relevant
resources before commitment. Concise summaries may use progressive disclosure,
but complete timing and effect text remains available through hover, keyboard
focus, tap, the Resume, or the active-effect strip.

Rules-loaded terms in trait text and task-card effects use a consistent
high-contrast keyword treatment. Hover, keyboard focus, and tap reveal one
short shared-glossary definition; the same term always uses the same
definition in the Resume, Promotion, Morning offer, Pinned Task details, and
separate task pickers.

Pinned Tasks remain separate from the generated offer. Morning shows each pin
as a compact Skill, name, and rarity row; activating it opens the standard full
task card before the player selects it. Eye for Detail does not create a new
Revision pin from a primary task selected through Pinned Tasks. The same task
can create Revision normally when selected later from the generated offer.

Common cards are simple and dependable, with one short, automatic micro-effect
that can make each card preferable in a specific situation. Keep that effect
bounded unless the ledger explicitly approves card-local progression.
Uncommon cards are stronger or more specialized and may use two short clauses.
Rare cards offer build-shaping daily effects with a condition, tradeoff, or
synergy. Legendary cards deliver a dramatic Skill-defining workday without
guaranteeing a win. Higher rarity raises a card's potential rather than making
it the automatic choice.

Every card should provide useful standalone value, express its job Skill, and
offer a higher conditional synergy ceiling. Coding remains the most internally
synergistic Skill, reflecting its comparatively solitary work fantasy, but
its effect cards must still offer enough standalone or cross-Skill value to
create real splash decisions.

The implementation uses Skill-based milestone traits rather than the
superseded stackable Resume-skill system. See the ledger for exact path effects
and values.

## Skill Card Identities

- **Coding - Build, Automate, Integrate:** turn prior work into future value,
  sequence or process additional cards, and hand value between Skills.
- **Management - Coordinate, Schedule, Amplify:** observe people and the
  workday schedule, guarantee or rearrange actions, and multiply successful
  coordination.
- **Design - Observe, Iterate, Transform:** reveal information before
  commitment, refine cards or preserved options through repeated work, and
  copy or convert existing effects into flexible value. Design manipulates
  card effects and information rather than repeating the underlying schedule.
- **Sales - Earn, Spend, Network:** generate cash or temporary purchasing
  power, turn spending into discounts or financing, and convert relationships
  into economic leverage. Sales money should create choices and tempo rather
  than function only as a score.
- **Operations - Reserve, Stabilize, Deliver:** hold resources or work for a
  later payoff, reroll or replace unreliable outcomes, and convert successful
  actions into dependable throughput. Operations responds to process
  reliability and resource flow rather than directly commanding people.

## Workday Actions

The standard day contains five actions, with Lunch fixed in the third slot.
Espresso can add another action.

A Schedule Entry is an action placed on the workday timeline. Resolving that
entry once is one Action Resolution, which produces one Outcome and applies
the relevant action triggers. Repeating an action adds resolutions without
adding more Schedule Entries. A Coworker Bonus Activation is tracked
separately from the action or visit that caused it: triggering a bonus twice
creates two activations, while doubling its strength creates one activation
with doubled numerical values.

The game generates and tags a Natural Schedule before the primary task is
resolved. Task, trait, Deal, and other effects then modify it through automatic
changes and one consolidated Schedule Desk before the entries lock. Schedule
count effects use that locked timeline. Repeats do not add entries, and actions
created dynamically during playback do not retroactively change its count.
Any decision that previews or compares schedules uses the same horizontal
tracker language as the live Workday: one icon tile per action, source badges,
and highlighted differences. When multiple schedules are available, stack
their trackers and let the player select one directly.

Adding an action creates a bonus entry. Replacing one creates a non-natural
entry in the same position. A runtime conversion preserves the original
entry's natural origin, while a repeat reuses that entry and its participants
with a fresh Outcome. Opening actions play first, ordinary bonus additions
follow the core schedule, and Standard Procedures play last. Actions triggered
during playback resolve immediately after their parent.

Desk visits, sabotage, passive manager ticks, and similar Workday Events are
not Schedule Entries or Action Resolutions. They use fixed timeline positions
so normal, double-speed, and skipped playback always resolve the same order and
outcomes. An event counts as an action only when an effect explicitly converts
it into one. The normal daily desk visit resolves after the midpoint Schedule
Entry, and armed sabotage resolves immediately after that visit.

- Work on Task grants project progress.
- Lunch resolves a hidden favorable or unfavorable result.
- Water Cooler grants a task or Home reroll.
- Office Chat can relieve stress or sour a relationship and cause sabotage.
- Slumped at Desk adds stress.
- Team Meeting affects the deadline, progress, or stress and includes coworker
  participant bonuses.
- Boss floors inject hostile manager actions.

Playback controls change presentation speed, never game outcomes. One button
shows the current speed and cycles `1x -> 2x -> 4x`; player-facing 1x uses
twice the original presentation baseline.

## Stress And Recovery

Stress is the player's health. Positive stress gains are multiplied by floor
pressure; ordinary recovery is not. Recovery can come from tasks, chats,
coworkers, Home upgrades, sleep, Lights Out, weekends, and promotions.

Flat stress ignores floor scaling and numerical stress modifiers. Focus may
still absorb it, and Guardian Angel may still prevent the resulting burnout.

Moodboard generates Focus from actual automatic-sleep, Lights Out, promotion,
and Weekend recovery. Harmful Weekend outcomes resolve atomically, then Focus
and Guardian Angel apply before burnout. Traits claimed after that Weekend do
not affect earlier transition events.

Stress should create route and build pressure without making defensive choices
mandatory every day.

## Home And Economy

Workdays pay cash and may earn interest. Cash buys permanent Home upgrades,
larger homes, and outings. Homes increase upgrade capacity and provide
cumulative bonuses. The night phase deliberately makes recovery, investment,
and relationship spending compete for attention and resources.

After the morning task chain and all morning spending finish, snapshot the
cash used for that workday's Reserve Levels and interest. Cash earned later in
the workday begins earning interest on the following workday. At Clock Out,
resolve performance effects before conditional rewards, settle income and
interest before mandatory debts, and pay those debts before creating new
reserves. On a project-completion night, purchases that can affect only the
already-completed project are unavailable.

Night is one flexible decision phase presented as the player's current living
space rather than the office. Each Home uses a flat side-view room composition
with a shallow patterned floor, a clear baseboard boundary, and furniture
grounded on that boundary. Clock Out transitions through a sunset and door
opening into the room; ending the day transitions through sunrise back to the
office. The sun and moon share one east-to-west arc but never occupy the same
stretch of it. Screen-right is east and screen-left is west. At each
transition the departing body completes the western half of the arc and drops
below the left edge, while the arriving body enters from the right/eastern
edge and climbs to the resting position the departing body held. The sun sets
in the west and the moon rises in the east at sunset; the moon sets in the
west and the sun rises in the east at sunrise. Reduced-motion and automated
runs bypass presentation timing without changing outcomes.

Generate Home and Deal catalogs at Night start, then open the consolidated
iPad-style Night Planner unless the player most recently ended Night from the
room. Its Home Shop, Outings, and Relationships tabs share persistent Stress,
Lights Out, Finalize Night, and Hide Planner controls. Deal Desk appears as a
fourth tab only while Sales or another active effect provides a legal Deal
purchase. Home Shop offers expand across the usable Planner width; three
offers use three equal columns and an additional visible offer uses a fourth
column without hiding the purchase controls. The room remains a complete
optional interface: the iPad opens the full Planner, the computer opens Home
Shop, the door opens Social tabs for Outings and Relationships, the laptop
opens Deal Desk when available, the switch selects Lights Out, and the bed
finalizes Night. Ending Night through the Planner makes the next Night open
there; using the bed preserves the room preference.

Outings remain independent of the recovery choice. Manual Lights Out and Home
or Deal purchases are mutually exclusive unless an effect explicitly permits
both; Moodboard's automatic Lights Out is the current exception. Purchases do
not end Night automatically. An explicit finalization applies sleep and any
available Lights Out recovery, expires night-only resources, and advances the
run. Newly purchased Home effects apply immediately. Repeated effects remain
separate but do not bypass normal Night limits unless they explicitly add an
action, purchase, or Outing.

The Planner and room keep Cash, Expense Credit, current Stress, and projected
post-sleep Stress prominent, including a top Stress bar. Interactive furniture
follows a stable left-to-right elevation: End Day bed, Night Planner iPad,
Home Shop computer, Deal laptop, and Social door. Every furniture body stays
above the baseboard while its feet meet the shared floor edge; the Home name
remains below that edge. The wall switch selects Lights Out. The moon appears
through the room window, and Lights Out visibly dims the room without hiding
its controls. Home capacity appears as accessible visual item slots on a wall
storage shelf. Occupied slots expose their effect and open a sell confirmation
through pointer, keyboard, or tap activation. Outing stories briefly fade the
room to black, then return the player to the same living space.

## Coworkers And Relationships

Coworkers move through the office, talk, join meetings, visit the player, and
grant relationship-scaled bonuses. Outings improve relationships and unlock
biography sections. Social systems should create useful build choices while
remaining character-driven.

Coworker bonuses trigger when the player meets that coworker during the
Workday, including eligible meetings and visits.

Each non-rival coworker normally has one Standard Bonus Opportunity per
workday, spent by ordinary Team Meeting participation or the normal daily desk
visit. Explicit card, trait, and reward effects may create Forced Bonus
Activations that ignore and do not consume that opportunity. For one meeting
or visit, overlapping rules set one total activation count rather than adding
duplicate normal and forced triggers unless an effect explicitly says
`additional`.

Calculate each complete bonus from current relationship when it activates.
Strength multipliers affect every numerical component before floor stress
scaling. Resolve all activations produced by one action or Workday Event
atomically so playback order cannot create hidden survival differences.

## Managers And Rival

Each floor has a manager modifier. Boss floors also support the rival and inject
hostile actions. The rival develops a simulated build and progresses every
workday. Manager rules should change priorities without creating unavoidable
losses. Delayed effects use the floor and manager active when they resolve
unless their source explicitly snapshots another value. The completed-floor
manager remains active through its completion Night, while Weekend events
ignore manager modifiers unless explicitly stated.

The current manager is visibly represented in the manager office with a
distinct portrait and color. They remain seated on ordinary floors and use a
cosmetic office patrol only on boss floors. This patrol is presentation-only:
it never joins the gameplay cast, reserves space, consumes RNG, or changes
1x, 2x, 4x, or Skip outcomes.

## Trait Progression

The progression system uses Skill XP rather than random per-skill stacks:

- task offerings use equal Skill weighting while allowing Skill repeats;
- every completed task grants one Skill XP regardless of rarity;
- at 3 Skill XP, choose one of the Skill's ordinary visible career paths;
- the selected ordinary path evolves at 6 and 10 XP;
- Closing is an exception after it is chosen as a Sales path: it has no 6 or
  10 XP milestones and develops entirely through its Sales Cycle, Close reward
  tables, and persistent Closing rewards;
- later milestones preserve earlier trait effects unless their text explicitly
  replaces or upgrades a specific effect;
- ordinary XP milestones and path choices are claimed at promotions;
- hybrid investment across Skills remains open;
- each ordinary milestone path has a distinct capstone, while Closing uses its
  first successful actual Chain 9 Close as its non-XP capstone trigger;
- only one capstone can be claimed per run across ordinary paths reaching 10
  XP, Brand Strategy finishing its final Campaign, and Closing completing its
  first actual Chain 9 Close;
- Brand Strategy is a hidden exception unlocked only by the Special card
  `Rebrand Initiative`; it can coexist with an ordinary Design path and
  advances through named, ordered task Campaigns rather than Design XP;
- while Brand Strategy is active, the Morning Task Desk shows its Campaign
  name, requested task and Skill, completed steps, and Campaigns completed;
- traits create natural cross-system synergies instead of named pair bonuses;
- trait paths use setup, payoff, and capstone interactions that can become
  exceptionally strong in the right build without being automatic.

Promotion claims are one staged transaction. The player configures every new
path and reached milestone, resolves any capstone comparison, and confirms the
whole batch before any new trait becomes active. Path selection shows only the
3 XP effect; each later milestone reveals its own description when claimed.
The final Promotion Review presents one paginated page per Skill, shows only
milestones earned in that promotion, uses visual milestone cards, and gives a
new capstone its own prominent card before the player confirms or revises the
staged batch.
The first sole capstone candidate reserves the run's capstone provisionally.
Before confirming Promotion, the player may revise that ordinary reservation
among every ordinary path newly eligible in the same review. Candidates
created by one atomic event are compared without using Skill order or
interface order as a tiebreaker. A confirmed or immediately activated
capstone remains permanent.

On the compact Resume rail, milestone boxes keep a green outline before they
are reached, use a highlighted `!` while awaiting Promotion Review, and retain
a green checkmark after the claim is confirmed. Hovering, focusing, or tapping
a 3, 6, or 10 XP box reveals the selected path's exact effect at that
milestone. Before specialization, the box states that no specialization has
been chosen for that Skill.

Exact approved and implemented-candidate trait effects live in the balance
ledger.

## Documentation Rule

Use this file for stable gameplay concepts. Use `BALANCE_LEDGER.md` for changing
numbers, active proposals, decisions, and unresolved questions. Use
`ARCHIVE_SUPERSEDED.md` only for historical directions that no longer belong in
active planning.
