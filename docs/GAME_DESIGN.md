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
- Let the workday play autonomously with 1x, 2x, 4x, and skip controls.
- Make builds legible through task families, permanent progression, homes, and
  relationships.
- Create varied runs without allowing a single unlucky roll to decide one.
- Target an approximately 25-35 percent win rate for a skilled player.
- Keep the complete game usable as one standalone HTML file.

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
4. Night: use available Outing, Home, and Deal actions in any legal order,
   then explicitly finalize the night with automatic sleep and optional
   Lights Out.
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

Every ordinary family task belongs to one of five job families:

- Coding;
- Management;
- Design;
- Sales; and
- Operations.

A task provides base project progress and stress plus a daily effect. Each
family contains ten reusable task cards: four Common, three Uncommon, two Rare,
and one Legendary, for 50 ordinary family cards total. Rarity belongs to the
card rather than being rolled separately. Cards have no universal rarity
multiplier or stress tax; each card is balanced around its explicit effect and
rarity.

Special cards sit outside the family roster and ordinary rarity distribution.
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
check for burnout. After that play resolves, immediately update its family XP
and card-progression counters; the resolving card cannot improve itself, but
later cards played during the same morning use the updated values.

Selecting a primary task is a separate event from playing a card. Every card
play is complete by default: it resolves base progress, base stress, the
printed effect, family XP, card-progression counters, and card-play triggers.
Replays and additional plays use that complete procedure but do not repeat the
morning selection or any primary-only trigger. Resolving only a copied printed
effect and calculating a Schmoozing Assist are not card plays.

Each independent effect that says to play a card twice adds one Replay.
Multiple such effects add their Replays rather than multiplying the total play
count.

Copied effects may contain another copy effect, but every copy branch tracks
its active Source cards and cannot use the same Source twice. An effect whose
entire value is explicitly bound to its own card identity cannot be selected
as a copy Source. `Iteration Pass` is the only current identity-bound ordinary
effect; `API Integration` instead redirects the Host card's pending family XP.

A selection and everything it generates form one ordered resolution chain.
Finish each card play before starting the next. Reaching the required project
progress marks the project complete but does not interrupt that chain; remaining
plays still resolve for their effects and progression, and promotion waits
until after the workday. Burnout ends the chain and discards everything in it
that has not begun resolving.

Morning offerings weight all five families equally at 20 percent and may show
more than one card from the same family, but never duplicate the same task in
one offer. A task card can appear again on later workdays. Every completed
ordinary family task grants one XP to its family regardless of rarity,
immediately after that play resolves.

Common cards are simple and dependable, with one short, automatic micro-effect
that can make each card preferable in a specific situation. Keep that effect
bounded unless the ledger explicitly approves card-local progression.
Uncommon cards are stronger or more specialized and may use two short clauses.
Rare cards offer build-shaping daily effects with a condition, tradeoff, or
synergy. Legendary cards deliver a dramatic family-defining workday without
guaranteeing a win. Higher rarity raises a card's potential rather than making
it the automatic choice.

Every card should provide useful standalone value, express its job family, and
offer a higher conditional synergy ceiling. Coding remains the most internally
synergistic family, reflecting its comparatively solitary work fantasy, but
its effect cards must still offer enough standalone or cross-family value to
create real splash decisions.

The implementation uses family-based milestone traits rather than the
superseded stackable Resume-skill system. See the ledger for exact path effects
and values.

## Family Card Identities

- **Coding - Build, Automate, Integrate:** turn prior work into future value,
  sequence or process additional cards, and hand value between families.
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

Playback controls change presentation speed, never game outcomes.

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

Night is one flexible decision phase. Generate its Home and Deal catalogs at
the start, then let the player use available Outing, Home, and Deal actions in
any order. Purchases do not end Night automatically. An explicit finalization
applies sleep and Lights Out, expires night-only resources, and advances the
run. Newly purchased Home effects apply immediately. Repeated effects remain
separate but do not bypass normal Night limits unless they explicitly add an
action, purchase, or Outing.

## Coworkers And Relationships

Coworkers move through the office, talk, join meetings, visit the player, and
grant relationship-scaled bonuses. Outings improve relationships and unlock
biography sections. Social systems should create useful build choices while
remaining character-driven.

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

## Trait Progression

The progression system uses family XP rather than random per-skill stacks:

- task offerings use equal family weighting while allowing family repeats;
- every completed task grants one family XP regardless of rarity;
- at 3 family XP, choose one of the family's ordinary visible trait paths;
- the selected ordinary path evolves at 6 and 10 XP;
- Closing is an exception after it is chosen as a Sales path: it has no 6 or
  10 XP milestones and develops entirely through its Sales Cycle, Close reward
  tables, and persistent Closing rewards;
- later milestones preserve earlier trait effects unless their text explicitly
  replaces or upgrades a specific effect;
- ordinary XP milestones and path choices are claimed at promotions;
- hybrid investment across families remains open;
- each ordinary milestone path has a distinct capstone, while Closing uses its
  first successful actual Chain 9 Close as its non-XP capstone trigger;
- only one capstone can be claimed per run across ordinary paths reaching 10
  XP, Brand Strategy finishing its final Campaign, and Closing completing its
  first actual Chain 9 Close;
- Brand Strategy is a hidden exception unlocked only by the Special card
  `Rebrand Initiative`; it can coexist with an ordinary Design path and
  advances through named, ordered task Campaigns rather than Design XP;
- traits create natural cross-system synergies instead of named pair bonuses;
- trait paths use setup, payoff, and capstone interactions that can become
  exceptionally strong in the right build without being automatic.

Promotion claims are one staged transaction. The player configures every new
path and reached milestone, resolves any capstone comparison, and confirms the
whole batch before any new trait becomes active. The first sole capstone
candidate reserves the run's capstone immediately; candidates created by one
atomic event are compared without using family order or interface order as a
tiebreaker.

Exact approved and implemented-candidate trait effects live in the balance
ledger.

## Documentation Rule

Use this file for stable gameplay concepts. Use `BALANCE_LEDGER.md` for changing
numbers, active proposals, decisions, and unresolved questions. Use
`ARCHIVE_SUPERSEDED.md` only for historical directions that no longer belong in
active planning.
