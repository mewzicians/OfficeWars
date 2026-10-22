# OfficeWars Game Design

Last updated: 2026-10-22

## Purpose

OfficeWars is a single-file office autobattler about climbing seven corporate
floors before Stress, the fixed workweek, or Chad ends the run.

This document contains durable player-facing behavior and mental models.
Exact values, content tables, decision status, and replacement text belong in
`BALANCE_LEDGER.md`. Implemented runtime truth remains
`officewarsautobattler.html`.

## Product Goals

- Keep one standalone HTML file with no required server or build step.
- Support brief attention without timed or reflex input.
- Let Workday playback run at 1x, 2x, 4x, or hidden Skip without changing
  gameplay or gameplay RNG.
- Pause unattended playback only at authored irreversible political choices.
- Make project pressure, managers, Chad, coworkers, politics, economy, and
  Home builds readable.
- Fit supported player-facing layouts without visible scrollbars. Long content
  must reflow, condense, or paginate unless a named scrollable surface is
  explicitly approved.
- Preserve deterministic reload and headless parity.
- Target approximately 25-35 percent wins for a skilled player after tuning.

## Implemented Baseline

The current root HTML implements Workday and Office Politics Phases 1-5, Home
Phase 1, Guided Intern, and the complete gated Cash Jar/Galactic runtime at
SHA-256
`1DA11A1FEC21B8AED383B1BDD53F2AAB0DAB55ADA8E2F1B188F26407DEFEC149`.
The public mirror and GitHub `main` carry this candidate as of 2026-10-22.
The balance ledger and some agent guidance on GitHub are older versions; the
ledger there still names `816A35B4`.

Implemented systems include:

- Wednesday-Friday Intern and Monday-Friday later floors;
- fixed project records, Friday locks, two earned overtime days, promotion,
  Weekend routing, and immediate CEO victory;
- task cards, fixed Comply/Resist/Negotiate manager packages, deterministic
  Today's Directive completion, five-state Approval, and Night objectives;
- pixel-cinematic Workday actions, chronological Project, Relationship, Chad,
  source-created, and Boss political events;
- irreversible choices, resource reservation, hidden Skip, results reel, and
  deterministic restoration;
- transparent Chad pace, supporter snapshots, direct political subtraction,
  conversations, and forecast decomposition;
- seven Project Briefs, favored and adversarial Skills, stakeholders,
  dilemmas, Overdelivery, expectations, and role rewards;
- forty-two authored coworker identities, dynamic floor rosters, 0-10
  Relationship, player/Chad standing, 168 scenes, invitations, traps, loyalty,
  role votes, and Alumni;
- Delegation campaigns, Favors, Schmoozing, All Hands, and direct social
  consumers;
- path-aware ordinary 3/10/20 progression, exceptional Closing and Brand
  Strategy progression, the fifty-card roster, Deals, rewards, and Weekends;
  and
- seven Homes, 28 available Home items, nine sets, Morning salary, deposits,
  shop rerolls, Cash-basis sales, held items, Active Buffs, Prepare Tomorrow,
  Remote Task, and Home/social integrations; and
- active-run schema 9 plus stable checkpoints for political choices, hidden
  queues, results, role votes, payouts, Night, Floor Briefing, and tutorial
  state; and
- Guided Intern as the sole first-play tutorial: one mandatory deterministic
  Wednesday-Friday run with 18 Coordinator checkpoints and real carryover.

Cash Jar acquisition remains disabled for ordinary players, but the gated
runtime implements its lifecycle, all 24 Weekend stories and 96 outcomes,
Galactic acquisition/events, Timeline, Hivemind, Reality, UI, and persistence.
Schema 9 remains live and schema 10 remains inactive. Guided Intern is not
part of the Cash Jar gate.

Headless promotion now awaits Delegation Floor Briefing before Morning. The
`cash-jar-visible-v1` simulation policy can legally acquire, Keep, Open, and
settle Cash Jar outcomes using visible information only. It is an evidence
instrument, not a tuned skilled-player model.

## Run Calendar And Promotion

Intern is the first floor. Every later floor uses a Monday-Friday workweek.
Completing the project locks promotion after the current atomic resolution
survives. Chad completing first causes defeat; a same-Clock-Out tie favors the
player. Earned overtime may extend an unfinished floor through Sunday.

A successful non-final floor resolves:

`Final Clock Out -> Overdelivery payout -> final Night -> pending Night
directive -> promotion recovery -> Weekend -> Promotion Review -> next floor`

The outgoing manager does not modify Weekend outcomes.

## Morning And Progression

Every ordinary task belongs to Coding, Management, Design, Sales, or
Operations. A primary is distinct from a Replay, Complete Additional Play,
copied Printed-Effect Resolution, or Automated Task Resolution.

Only the primary receives primary-only project and manager treatment. Skill XP
is uncapped. Ordinary paths advance through the active threshold authority.
Closing advances through Sales Cycles and Chain, while Brand Strategy advances
through Campaigns. Only one career-path capstone may be owned.

## Workday And Politics

The Workday order is:

1. Reveal the manager directive.
2. Assign fixed package responses to visible primary packages.
3. Pay the selected response cost.
4. Resolve the primary and its immediate chain.
5. Lock schedule entries, participants, political records, dialogue, and
   conditional branches.
6. Save the prepared Workday.
7. Play ordinary actions and pause at political choices.
8. Reveal results chronologically.
9. Continue to Clock Out.

Watching, Skip, reload, and headless execution must preserve gameplay state and
RNG. Political choices have no timer, Back, edit, or defer path. Costs reserve
at commitment. Terminal outcomes release later reservations and end the run.

A live political choice owns the central Workday presentation. The day ticker,
Action Guide, playback controls, and floating current-action card are hidden
until commitment. The saved event anchor appears inside the decision as a
before/after action breadcrumb. Normal HUD information remains visible.

The Office Politics wrap-up owns the screen as Clock Out does: the day
ticker, Action Guide, playback controls, and HUD stay hidden while the
results reel is open, live or restored.

## Projects, Chad, Managers, And Coworkers

Every floor owns a Project Brief, favored/adversarial Skill pair, two
stakeholders, a dilemma deck, and a role contest. Overdelivery rewards excess
completion but temporarily raises next-floor expectations.

Chad remains throughout the run. His forecast itemizes pace, project size,
supporters, role rewards, manager effects, bosses, expectations, and direct
subtraction.

Every manager combines a passive, directive tendencies, fixed task-package
responses, Approval, and Favorite/Vindictive riders. Directives are
deterministic office quests rather than manager-odds rolls.

Every floor roster contains Gatekeeper, Wildcard, Pragmatist, Achiever,
Networker, and Idealist identities. Relationship controls personal scenes and
loyalty; standing controls political alignment. Loyal coworkers become Alumni
after retirement and preserve identity, gifts, Network ranks, and permanent
archetype perks.

## Implemented Home System

Status: **Implemented in schema 9; Cash Jar gated**

Home becomes a supportive build shaper with a deterministic seven-level
housing ladder:

`Apartment -> Condo -> Townhouse -> Duplex -> House -> Estate -> Penthouse`

### Housing And Shop

- The player deposits Cash toward the next Home during Night.
- Deposits persist, cannot be withdrawn, and share one move per Night with
  automatic equity sources.
- A move immediately changes capacity and comfort; the current catalog keeps
  its generated rarity until rerolled or replaced.
- Home level controls active item slots, nightly recovery, and shop rarity
  odds.
- The base shop shows three unique-item offers at every Home.
- Free Home rerolls bank. Paid rerolls escalate each Night and reset the next
  Night.
- Items are unique. Selling uses acquisition Cash basis and immediately
  recomputes sets.
- Final-charge items disappear. A player-controlled final charge warns which
  sets will break.
- The same side-view room evolves through all seven Homes.

Exact deposits, salary, and rarity odds remain Draft tuning values.

### Item And Set Model

The catalog defines 29 ordinary items. Twenty-eight are available; Cash Jar is
implemented behind its release gate and remains unavailable in ordinary
schema-9 play.

- 11 Common;
- 7 Uncommon;
- 6 Rare; and
- 5 Legendary.

Items have literal tags and useful standalone effects. Nine simultaneous sets
shape builds:

- Energy;
- Financial Foundation;
- Appliance Suite;
- Wellness;
- Connected Home;
- Hospitality;
- Networking;
- Workspace; and
- Planning.

Flexible sets count tags. Workspace and Planning require four specific
non-Legendary pieces; Home Office and Personal Assistant are their fifth-piece
supers. Connected Home passively upgrades every other completed set.

Set completion is derived from currently active items and changes immediately
after buying, selling, exhausting, destroying, or receiving an item.

### Exceptional Resolution

Automation's purchased Combo cards become `Automated Task Resolution`.
Automated resolutions keep base PP, printed effects, card-local conditional
PP, and Automation Combo PP, but grant no Stress, Skill XP, completion
identity, Codebase, Polish, counters, or Complete Play triggers.

Home Office Remote Task, Planning day plans, set-created actions, cloned
effects, and other exceptional sources must preserve ancestry, exactly-once
settlement, and watched/Skip/reload/headless parity.

### Player-Facing Home Language

The player-facing action is `Work`; prose calls it a `Work action`.
`Work on Task` remains only an internal compatibility alias.

Home cards use a compact three-part model:

1. item name;
2. `GOOD FOR` set tags; and
3. one short mechanical effect.

Named buffs and reusable keywords use a dotted underline with the same short
tooltip on hover, keyboard focus, and tap. Routine UI never exposes internal
snapshots, settlement markers, ancestry, schemas, or calculation precedence.

The existing HUD effect strip remains the quick view. Selecting a chip or its
overflow opens the Resume's categorized Active Buffs page. Build Context shows
only Morning-relevant effects; permanent Home items and sets are grouped.

The compact Resume rail uses one bottom progress footer per Skill: exact
uncapped XP or Closing Chain on the left, the next gate beside it, and one
continuous family-colored bar on the right. A 16px family icon marks the next
milestone and disappears at final completion. Completed Skills use a brighter
static frame; an active capstone adds a gold star and a one-time,
reduced-motion-safe acquisition treatment. Detailed 20-square XP tracks and
milestone tooltips remain in the Resume Book.

## Locked Cash Jar

Status: **Locked; gated implementation verified, release disabled**

`Cash Jar Marked "DO NOT SPEND"` is a unique Financial Foundation Common.

- It appears only in an eligible Home catalog generated while ordinary Cash is
  `$500` or less.
- Buying it consumes all ordinary Cash, ignores discounts, credit, financing,
  and free-purchase effects, and counts as a Home purchase and Cash spend for
  other systems.
- Its own purchase cannot break it.
- It cannot be sold. Only spending ordinary Cash, Weekend Open, or another
  authored terminal effect removes it.
- While intact it grants `$25` after Workday salary and before task selection.
- Any later gross ordinary-Cash outflow breaks and destroys it immediately;
  Expense Credit and canceled transactions do not.
- A declined offer may return while still eligible. A purchased, broken, or
  opened Jar never returns.

### Weekend Cashout

At every eligible Weekend an intact Jar offers:

- `Keep`: gain one Tier, receive no reward, and continue the no-spend
  challenge; or
- `Open`: freeze and consume the current ordinary-Cash wallet, destroy the
  Jar, select the current Tier/band story, and make one irreversible authored
  choice.

The six Tiers use four Cash bands:

- `$0-499`;
- `$500-999`;
- `$1,000-4,999`; and
- `$5,000+`.

This creates 24 unique story cells. Cash band controls power; Tier primarily
controls weirdness. Tier 6 / `$5,000+` is the unique Cash Jar capstone.

The Jar event replaces the ordinary mystery Weekend. Floor 3's guaranteed
Casino follows it. Keep is unavailable when no later non-final Weekend exists.
Choices reveal labels only; probabilities and outcomes remain hidden until
commitment.

Stable checkpoints cover Keep/Open, post-Open story choice, and settled
result. Exact story tables belong in the ledger.

### Planetary Constitution

One Declared-a-Planet outcome grants permanent Galactic laws and replaces
future mystery Weekends with a beneficial Galactic event deck.

- Twelve stable event identities use a Locked deterministic replacement table.
- Every event shows two fully described beneficial choices.
- Draw without replacement, reshuffle after all twelve, and exclude the
  immediately previous event.
- Repeated outcomes use event-specific upgrades and Encores.
- Hostage events resolve after Clock Out and before Night; a real Weekend
  consumes a due Hostage trigger.
- Mid-floor rewards begin at their next authored legal boundary.
- Presentation compresses after twelve actions without changing mechanics,
  politics, RNG, or Skip parity.

Property Rights turns the active Home portfolio into Workday productivity and
pay. It snapshots active items before salary, freezes that portfolio through
the Workday, and applies productivity only to the original selected primary;
derived task resolutions do not inherit it. Orbital Warehouse counts every
owned item because those items are active. Exact values and settlement order
belong in the ledger. Galactic Investment and Galactic Gambler numeric values
remain Draft.

## Guided Intern

Status: **Implemented**

Every profile must complete one mandatory authored Wednesday-Friday Guided
Intern before ordinary play. `GI-OPEN` remains one checkpoint but contains
four automatic Back/Next spotlight steps: the actual Project Progress HUD, the
Chad race and three-workday calendar, Favored/Adversarial Project Fit, and
named project stakeholders. Only its final step exposes Clock In. Later
lessons use a larger dock, short dialogue, a persistent checklist, one-time
attention cues, and accessible required-action targeting.

One bold, decorative pixel connector links the Coordinator card to the active
opening target. It refits after step changes, reload, resizing, and text
scaling, never accepts input, and consumes no gameplay state or RNG.

The deterministic scenario teaches the project race, favored/adversarial
Skills, manager packages, cinematic Workday choices, Office Politics, Chad
Openings, Night tradeoffs, completion lock, one Overdelivery tier, Weekend,
and Promotion Review. Real state carries into Associate.

The Coordinator assumes player competence and explains hidden interactions,
not obvious labels or generic reassurance. Eighteen checkpoints teach only
the approved content: three Coding tasks, one Home item, one social target,
one Home deposit, and the core run loop. The player reviews all three Coding
paths individually and freely chooses one at graduation.

Opening and lesson copy follows function-first progressive disclosure.
Project Progress is defined before PP is used. Favored and Adversarial explain
their purpose in the spotlight, retain exact accessible tooltips, and repeat
exact consequences only when a relevant Morning task is being confirmed.
Gatekeeper and Pragmatist appear as work-style descriptors rather than
guaranteed response rules.

Intern social state follows the floor-local model: Priya can retire as Alumni,
and Coordinator Approval becomes manager reputation. It is not copied onto the
new Associate roster.

Guided Intern replaces the removed contextual Orientation. Options can start
a fresh real Guided replay after the normal active-run replacement warning.
Completion is committed only after a recoverable Associate Floor Intro exists;
the Coordinator does not interrupt the first Associate Morning.

The opening walkthrough replaces opening Show Me with Back, Next, `1/4`
progress, and one final Clock In. Its optional persisted `openingStep` defaults
to the first step for older saves and changes no gameplay RNG. Later Show Me
resolves the next legal action, including the next incomplete step in
multi-action Night and Promotion lessons. It scrolls, focuses, and labels that
target without changing gameplay or RNG. Repeat is not part of the interface.
The Guided Floor Intro keeps the compact Coordinator card away from the
highlighted target and has no internal scrollbar at supported desktop,
scaled-text, or short-landscape layouts.

During Guided political choices, the full Coordinator dock is replaced by a
compact instruction and Show Me strip inside the decision pane. Wrong-choice
feedback remains inline. The ordinary dock returns after commitment while the
Action Guide remains closed.

Elsewhere the dock stays full-size at the bottom unless it would cover a live
control; then it collapses to one line, at the top when that covers fewer
controls. The Show Me marker avoids the dock and other controls. Morning
carries its own Office Politics button because the HUD copy sits under the
Morning overlay.

## Persistence, UI, And Accessibility

Home and Cash Jar records are serializable before presentation. Reload preserves generated
offers, transactions, held items, mastery, plans, Remote Task, Home Setup,
active buffs, Cash Jar choices/outcomes, Galactic events, and exactly-once
settlement.

Home and Cash Jar UI support desktop and short landscape, keyboard-focusable/touch
tooltips, reduced-motion-compatible transitions, and 200-percent text without
horizontal overflow in the verified surfaces. Formal screen-reader execution
and broad human evidence remain Not Run. Routine effects stay concise; exact
formulas and precedence remain in the ledger or optional accessible details.

The supported interface uses authored pages instead of visible scrollbars for
long content. Morning separates tasks from context and pins; Resume pages paths
and categorized buffs; Clock Out separates summary, carryover, and source log;
and Help, schedules, politics, inventories, Action Guide, and result reels page
their long-form content. Responsive refit state is presentation-only and
consumes no gameplay RNG.

## Documentation Boundary

- `GAME_DESIGN.md`: stable behavior and player mental models.
- `BALANCE_LEDGER.md`: exact values, tables, status, and recovery gaps.
- `HANDOFF.md` and `PROJECT_STATUS.md`: current implementation and evidence.
- `ARCHIVE_SUPERSEDED.md`: discarded directions only.
- Dated patch notes and verification reports: evidence for their named
  snapshots, never current design authority.
