# OfficeWars Balance Ledger

Last updated: 2026-09-23

## Status Rules

- **Implemented Baseline**: behavior currently present in
  `officewarsautobattler.html`.
- **Locked**: explicitly approved design, whether implemented or not.
- **Draft**: exact tuning input awaiting simulation or approval.
- **Open**: unresolved design choice.
- **Recovery Required**: an approved decision whose exact prior text is not
  currently recoverable; do not silently redesign it.
- **Superseded**: inactive direction indexed in `ARCHIVE_SUPERSEDED.md`.

## Implemented Baseline

The current root standalone HTML has:

- SHA-256
  `816A35B40CD4F36C6CF25CD766BF6FEB94A1D77D885C56947B73F6C4228F52AA`;
- size `1,730,955` bytes;
- active-run schema 9; and
- tutorial-meta schema 6.

Phases 1-5 are implemented. This includes the fixed calendar, Overtime Bank,
completion lock, Overdelivery, expectations, transparent Chad pace, fixed
manager packages, deterministic Today's Directive, pixel-cinematic Workday,
chronological politics, hidden Skip/reload, dynamic rosters, Relationship,
standing, scenes, invitations, loyalty, Alumni, campaigns, Favors, 3/10/20
progression, fifty cards, rewards, Deals, Closing, Brand Strategy, Weekends,
deterministic persistence, and Home Phase 1. Home Phase 1 includes seven
Homes, 28 available items, nine sets, Morning salary, the Home planner,
Active Buffs, deposits, rerolls, Cash-basis sales, Automation replacement,
Remote Task, Planning, and direct social integrations.

Current core values:

| Value | Implemented |
|---|---:|
| Project sizes | `45 / 80 / 115 / 155 / 205 / 265 / 330` |
| Floor Stress scaling | `20%` |
| Home automatic Night recovery | `0 / 1 / 2 / 3 / 4 / 5 / 6` |
| Lights Out recovery | `5` |
| Promotion recovery | `25` |
| Base interest | `15%` |
| Natural Workday entries | `5` |
| Overtime Bank cap | `2` |
| Ordinary Skill thresholds | `3 / 10 / 20` |

Cash Jar remains gated and unobtainable in ordinary runs. Its lifecycle,
Weekend flow, 24 story cells, 96 outcomes, Galactic dependencies, Timeline,
Hivemind, and Reality packages are implemented behind the gate. Schema 10 is
not active.

## Implemented Home Phase 1

Status: **Implemented; Draft economy inputs remain Draft; Cash Jar gated**

### Housing Ladder

| Home | Active slots | Automatic Night recovery |
|---|---:|---:|
| Apartment | 3 | 0 |
| Condo | 5 | 1 |
| Townhouse | 7 | 2 |
| Duplex | 9 | 3 |
| House | 11 | 4 |
| Estate | 13 | 5 |
| Penthouse | 15 | 6 |

- One irreversible manual deposit is allowed per Night in `$50` increments.
- Quick controls are `$50`, half remaining cap, maximum, and custom.
- Deposits are ordinary Home-category Cash spending. They cannot use Expense
  Credit, do not consume a Home purchase, and cannot be withdrawn.
- At most one move settles per Night across manual deposits and automatic
  equity.
- A move applies slots and comfort immediately. The already-generated catalog
  retains its old rarity odds until replaced.
- Equity beyond the current requirement carries to the next meter.
- The base Home Shop has three offers at every Home.
- Free Home rerolls bank. Paid rerolls cost `$50`, `$100`, `$150`, and so on
  each Night, then reset.
- Items are unique. Empty rarity pools fall back to any eligible unowned item.

### Draft Housing And Salary Inputs

These values are simulation inputs, not final tuning.

| Current Home | Next requirement | Night deposit cap | Common / Uncommon / Rare / Legendary |
|---|---:|---:|---|
| Apartment | $600 | $200 | 85 / 15 / 0 / 0 |
| Condo | $1,000 | $300 | 70 / 25 / 5 / 0 |
| Townhouse | $1,600 | $450 | 55 / 35 / 10 / 0 |
| Duplex | $2,500 | $700 | 40 / 40 / 18 / 2 |
| House | $4,000 | $1,100 | 28 / 38 / 28 / 6 |
| Estate | $6,500 | $1,800 | 18 / 32 / 35 / 15 |
| Penthouse | - | - | 10 / 20 / 40 / 30 |

Draft Workday salary by floor:

`$200 / $250 / $325 / $425 / $550 / $700 / $900`

### Ownership, State, And Resale

- Home state is a per-item ledger, not an ID-only owned list.
- Persist acquisition Cash basis, charges, counters, lifetime progression,
  once-per-day/floor use, sold generations, and inactive state.
- Selling returns `25%` of ordinary Cash actually paid for that copy.
- Expense Credit, free portions, and financing principal create zero basis.
- Net 30 Cash paid later adds basis when paid.
- Financial Foundation raises resale to `50%`, including the sale that breaks
  the set.
- Neglected Houseplant Growth adds after percentage resale.
- Item progression survives sale but remains inactive until reacquired.
- A final-charge item disappears. A player-controlled final charge warns the
  exact sets that will break.

### Set Definitions

| Set | Requirement | Locked effect | Connected Home upgrade |
|---|---|---|---|
| Energy | 2 tags | Add one fully Natural random ordinary non-Lunch Schedule Entry every Workday. | Roll two candidate entries and choose one. |
| Financial Foundation | 2 tags | After interest, add equity equal to `50%` of earned interest. At Penthouse pay it as Cash. | Match becomes `75%`. |
| Appliance Suite | 3 tags | Gain one additional Home-item purchase each Night. | The first Appliance-granted extra purchase does not block Lights Out. |
| Wellness | 3 tags | Excess Night recovery becomes Well Rested, cap `5`, for the next Workday. | Cap becomes `8`. |
| Hospitality | 3 tags | Unlock Host a Gathering once per Night; it consumes the sole Outing. | Guests may be chosen from the full current roster. |
| Networking | 3 tags | Unlock one Make the Follow-Up per floor after a successful social event: `+5` player standing or a basic Favor for an existing supporter. | Standing becomes `+8`. |
| Connected Home | 3 tags | Passively apply every completed set's Connected upgrade. It does not upgrade itself. | - |
| Workspace | Standing Desk + Ergonomic Chair + Second Monitor + Cloud Workstation | Every ordinary Complete Play gains `+3 base PP / -1 base Stress`. | Stress reduction becomes `-2`; PP is unchanged. |
| Workspace Super | Workspace 4 + Home Office | Deep Work becomes `+4 base PP / -1 base Stress`. | Stress reduction becomes `-2`. |
| Planning | Receipts Shoebox + Wall of Sticky Notes + Notebook Marked "NOT WORK" + Library | At Night roll two Plans from different categories and choose one for the next Workday. | See one Plan per category. |
| Planning Super | Planning 4 + Personal Assistant | See one Plan per category and choose two from different categories. | See all six Plans and choose two. |

Set effects apply only to unresolved future triggers. Committed serialized
records retain frozen values when a set breaks.

Well Rested:

- At Night finalization, Wellness converts excess recovery into up to 5 Well
  Rested for the following Workday; Connected Wellness raises the cap to 8.
- Comfy Mattress grants a separate 5 guaranteed Well Rested after Lights Out;
  Zoning raises that grant to 10.
- Well Rested absorbs scaled Stress before Focus, does not reduce raw-Stress
  directive tracking, cannot convert into PP, and expires at Clock Out.

### Hospitality Approaches

Host a Gathering chooses three legal guests and resolves one saved result per
guest.

| Approach | Price | Per-guest odds | Success | Failure |
|---|---:|---:|---|---|
| Host Dinner | $100 | 100% | `+1 Relationship` | None |
| Rally the Room | $50 | 80% | `+2 player standing` | `+2 Chad standing` |
| Talk Office Politics | Free | 50% | `+4 player standing` | `+4 Chad standing`, `+1 Stress` per failed guest, cap 3 |

Expense Credit pays before Cash. The gathering counts once for Outing and
spending objectives; participant effects see all three guests.

### Planning Deck

Category order is Pace, People, Control.

| Category | Plan | Benefit | Cost |
|---|---|---|---|
| Pace | Delivery Sprint | Primary `+4 base PP`; every Work action `+1 base PP` | `+4` flat Stress at Clock Out |
| Pace | Sustainable Pace | Primary `-4 base Stress`; first Slump becomes Water Cooler | Primary `-3 base PP` |
| People | Collaboration Block | Add one Office Chat; first successful coworker political decision gives participants `+2 player standing` | Primary `-2 base PP` |
| People | Visibility Push | Directive Success non-Approval numeric reward `+50%` | Directive Failure adds `+2 Stress` |
| Control | Risk Buffer | Reroll first unfavorable ordinary action | Primary `-2 base PP` |
| Control | Flexible Calendar | Replace one ordinary non-Lunch entry with a chosen different action | Primary `+3 base Stress` |

No Plan is offered when no next Workday exists.

### Item Catalog

#### Common - 11

| Item | Tags | Price | Standalone effect | Galactic Zoning |
|---|---|---:|---|---|
| Questionably Acquired Coffee Maker | Energy, Appliance | $450 | At Workday start with at least 60% Stress, primary gets `-2 base Stress` and gain 1 Brew. Cash out at Brew targets `3/4/5...` for `1/2/3...` bonus Work entries next Workday, or choose New Roast to raise future cashout permanently. | `-4 base Stress`, `+2 Brew`, double cashout Work entries |
| Blackout Curtains | Energy, Wellness | $200 | Automatic Night recovery `+1` | Recovery `+2` |
| Neglected Houseplant | Wellness | $250 | Each Outing adds 1 Growth. Sale adds `Growth * current Growth value`; value starts `$50` and rises `$50` after a sale at 5+ Growth. | `+2 Growth` per Outing |
| Standing Desk | Workspace | $350 | Work actions gain `+1 base PP` | `+2 base PP` |
| Emergency Snack Drawer | Wellness | $300 | Three Snacks; automatically reroll an unfavorable Lunch once and accept the second result; disappear at zero | No Zoning upgrade |
| Router With One Good Antenna | Connected Home | $250 | Each Home Shop reroll adds one persistent temporary eligible offer for that Night | Add two offers per reroll |
| Receipts Shoebox | Planning, Financial Foundation | $250 | Manager modifier Cash cost `-$25`, minimum 0 | `-$50`, minimum 0 |
| Wall of Sticky Notes | Planning | $500 | Three charges. During ordinary generated task selection, arm and replace one generated target with a chosen one of three random other Skills at normal rarity; preserve package slot; disappear at zero. | No Zoning upgrade |
| Folding Dining Table | Hospitality | $200 | First paid Outing after acquisition each floor costs `$25` less | `$50` less |
| Cash Jar Marked "DO NOT SPEND" | Financial Foundation | All ordinary Cash | Unique no-spend challenge and six-tier Weekend cashout described below | No Zoning upgrade |
| Notebook Marked "NOT WORK" | Planning, Wellness | $500 | If net Stress at Clock Out is `+15` over morning, gain a free Journal action. Goals are `3/4/5...` entries; each completion permanently reduces every Complete Task Play's base Stress by 1 while owned. | `-2 base Stress` per completed rank |

#### Uncommon - 7

| Item | Tags | Price | Standalone effect | Galactic Zoning |
|---|---|---:|---|---|
| Comfy Mattress | Wellness | $600 | Lights Out grants 5 guaranteed Well Rested next Workday, in addition to the set cap | 10 Well Rested |
| Ergonomic Chair | Workspace | $550 | First task play each day whose original base Stress is at least 10 gets `-3 base Stress` | `-6` |
| Savings Account | Financial Foundation | $700 | Up to `$250` of house deposit each Night counts toward next morning Accounted Cash and interest without counting the same dollars twice | `$500` |
| Game Console | Appliance, Connected Home | $800 | Refund the first task or Home reroll spent each run-wide day after resolution; gross spending and paid-Home price escalation still occur | Refund first task and first Home reroll |
| Robot Vacuum | Appliance | $550 | First Home item purchase each Night recovers 4 Stress | Recover 8 |
| Guest Towels | Hospitality | $650 | First successful Build Rapport with each coworker per floor gains `+1 Relationship` | `+2 Relationship` |
| Framed Conference Badge | Networking | $750 | First successful social event with each coworker per floor introduces a different non-supporter for `+2 standing`; empty pool grants source archetype basic Favor | `+4 standing` |

#### Rare - 6

| Item | Tags | Price | Standalone effect | Galactic Zoning |
|---|---|---:|---|---|
| Second Monitor | Workspace | $1,400 | After primary choice, select a different visible ordinary generated/Pinned/stored task without consuming it. Every ordinary Complete Play that day gains half its printed base PP. Copies and Automation are excluded. | Gain full target base PP |
| Cloud Workstation | Workspace, Connected Home | $1,350 | Initial generated offer marks one eligible ordinary card. If primary, gain `+5 base PP` and total native XP 2. Any task-offer reroll or targeted replacement clears the mark for the day. | `+10 base PP`, total native XP 4 |
| Library | Planning | $1,450 | Catalogue five different ordinary task identities completed while owned. One Study Session per Night grants `+3 XP` to one of three random eligible Skills, then clears the catalogue; overflow identities carry. | `+6 XP` |
| Home Gym | Wellness | $1,100 | Once per day when actual Stress after shields reaches threshold, recover 10; threshold starts 60 and rises 5 per trigger, cap 95 | Recover 20 |
| Jacuzzi | Hospitality, Wellness | $1,250 | First three distinct successful social participants per floor form Party Crew. Crew members join future Chats/Meetings involving a member; first crew action each day is favorable unless an earlier guarantee handles it. | First two crew actions favorable |
| Business Card Corkboard | Networking | $1,300 | Successful social participants link once to the lowest-standing eligible coworker. Future positive Relationship or player-standing movement propagates half, minimum 1, nonrecursively. | Full-strength propagation |

#### Legendary - 5

| Item | Tags | Price | Standalone effect | Galactic Zoning |
|---|---|---:|---|---|
| Home Office | Workspace | $2,800 | After primary, choose a different visible ordinary task and precommit its choices. At Clock Out resolve Remote Task: base PP plus complete printed effect and legal child plays, with no own Stress, XP, counters, selection, or Complete Play triggers. | Resolve Remote Task twice |
| Personal Assistant | Planning | $2,600 | At Night choose one of three random Skills and one ordinary action; next legal ordinary Workday guarantees a generated Skill slot and Natural action. Carry through exceptional mornings. | Two Skills and two actions |
| Espresso Machine | Energy, Appliance | $2,100 | First positive ordinary action each day immediately repeats with same participants, fresh outcome, normal modifiers, and no recursion | First two positive actions repeat |
| Guest Suite | Hospitality, Networking | $2,200 | Unsanctioned Guest Pass: after first successful Night social event, first successful participant gains `+1 Relationship` or `+3 standing` if loyal, joins tomorrow's first Chat/Meeting, and blocks Chad movement until next Night | First two successful participants |
| Smart Home Hub | Appliance, Connected Home | $2,400 | First eligible authored limited Home trigger each day applies its effect package twice while its marker advances once; excludes state creators and recursive triggers | First two eligible triggers |

Notebook Marked "NOT WORK":

- If net Stress at Clock Out is at least 15 above the Workday's morning value,
  automatically record one Journal entry.
- Journal consumes no Night action, purchase, or choice.
- Goals require `3/4/5...` entries. Completing a goal immediately grants one
  permanent rank; each rank reduces every Complete Play's base Stress by 1
  while the Notebook is active.
- Completed ranks and current goal progress are lifetime mastery and survive
  sale/reacquisition.

Smart Home Hub's numeric allowlist is:

- Questionably Acquired Coffee Maker;
- Folding Dining Table;
- Comfy Mattress;
- Ergonomic Chair;
- Robot Vacuum;
- Guest Towels;
- Cloud Workstation;
- Library; and
- Home Gym.

It never duplicates choices, rerolls, refunds, offers, schedules,
participants, links, guarantees, repeats, or itself.

### Locked Player-Facing Home Copy

`GOOD FOR` uses literal set tags. Named terms are underlined buff/keyword
tooltips.

| Item | Short effect |
|---|---|
| Questionably Acquired Coffee Maker | At 60%+ Stress, your primary gets -2 Stress and gains 1 Brew. |
| Blackout Curtains | Automatic Night recovery +1. |
| Neglected Houseplant | Outings grant 1 Growth. Selling cashes out its Growth. |
| Standing Desk | Work actions grant +1 PP. |
| Emergency Snack Drawer | 3 Snacks. Automatically rerolls an unfavorable Lunch. |
| Router With One Good Antenna | Home Rerolls add 1 extra offer for that Night. |
| Receipts Shoebox | Manager modifiers cost $25 less. |
| Wall of Sticky Notes | 3 charges. Replace 1 generated task with a choice of 3 other Skills. |
| Folding Dining Table | Your first paid Outing each floor costs $25 less. |
| Cash Jar Marked "DO NOT SPEND" | Costs all Cash. Breaks when you spend Cash. Non-sellable. Open it on a Weekend. |
| Notebook Marked "NOT WORK" | After a +15 Stress Workday, record 1 Journal entry. Complete 3/4/5... entries to reduce task Stress by 1. |
| Comfy Mattress | Lights Out grants 5 Well Rested for tomorrow. |
| Ergonomic Chair | Your first task each day with 10+ base Stress gets -3 Stress. |
| Savings Account | Up to $250 of tonight's Home deposit still counts toward tomorrow's Accounted Cash. |
| Game Console | Refund your first Task or Home Reroll each day. |
| Robot Vacuum | Your first Home purchase each Night recovers 4 Stress. |
| Guest Towels | Your first successful Build Rapport with each coworker each floor grants +1 Relationship. |
| Framed Conference Badge | Each coworker's first successful social event triggers an Introduction. |
| Second Monitor | Choose another visible task. Your Complete Plays today gain half its base PP. |
| Cloud Workstation | One generated task is Marked. Play it for +5 PP and 2 XP. |
| Library | Complete 5 different tasks to unlock a Study Session for +3 XP. |
| Home Gym | At your Training Threshold, recover 10 Stress once per day. |
| Jacuzzi | Your first 3 successful social participants each floor join Party Crew. |
| Business Card Corkboard | Successful social participants create a Link to a low-standing coworker. |
| Home Office | After choosing your primary, queue another visible task as a Remote Task for Clock Out. |
| Personal Assistant | At Night, Prepare 1 of 3 Skills and 1 action for your next Workday. |
| Espresso Machine | Your first positive action each day Repeats. |
| Guest Suite | Your first successful Night social event grants Guest Pass to its first participant. |
| Smart Home Hub | Your first Hub-Compatible Home trigger each day activates twice. |

### Automation Replacement

Purchased Automation Combo cards resolve as `Automated Task Resolution`:

- resolve base PP, printed effect, card-local conditional PP, and Combo PP;
- grant no Stress, Skill XP, Codebase, Polish, completion identity, counters,
  selection, Complete Play, Replay, Campaign, Sales Cycle, or political
  triggers;
- do not receive Workspace; and
- preserve source ancestry and exactly-once delayed effects.

## Locked Cash Jar

Status: **Locked; gated implementation verified, release disabled**

### Purchase And Break Rules

- Eligible only in a Home catalog generated while ordinary Cash is `$500` or
  less.
- Unique once per run. If declined, it may reappear while eligible.
- Buying consumes the full ordinary-Cash wallet, ignores discounts, Expense
  Credit, financing, and free-purchase effects, and creates zero resale basis.
- The purchase counts as a Home purchase and ordinary Cash spend for other
  systems, but is exempt from breaking itself.
- It grants `$25` after salary and before task selection as a separate Cash
  gain. It counts for Accounted Cash and interest, not salary modifiers.
- Any later gross ordinary-Cash outflow breaks it immediately, including
  manager/political costs, rerolls, purchases, deposits, Net 30 payments, and
  Casino chips. Refunds do not restore it.
- Expense Credit and canceled transactions do not break it.
- Breaking destroys it with no salvage, frees its slot, stops income, and
  permanently retires the offer.

### Weekend Rules

- A new Jar begins at Tier 1.
- It may Keep/Open at the immediately following Weekend, including when bought
  on the final Night.
- Keep increases Tier by one and grants no reward.
- Open freezes the current ordinary-Cash wallet, shows the exact forfeiture,
  consumes it, destroys the Jar, and opens the current Tier/band story.
- Keep is unavailable when no later non-final Weekend exists.
- Jar Weekend replaces the ordinary mystery event. Floor 3 Casino follows.
- Story choices show labels only. Outcome probabilities and effects remain
  hidden until commitment.
- Outcome roll occurs at choice commitment and is saved before settlement.
- Stable checkpoints: `cashJarWeekend`, `cashJarStory`, `cashJarResult`.

Cash bands:

1. `$0-499`
2. `$500-999`
3. `$1,000-4,999`
4. `$5,000+`

### Tier 1

#### $0-499 - Rainy-Day Test

| Choice | Odds | Result |
|---|---:|---|
| Use the Jar | 70% | Patch: recover 15 Stress and gain two banked Home rerolls |
| Use the Jar | 30% | Insurance: recover 25 Stress and gain one free unowned Common Home item; if full, use one temporary holding slot |
| Call the Landlord | 65% | Rent Abatement: regain the full frozen stake and gain `$200 Expense Credit` through the next floor |
| Call the Landlord | 35% | Code Violation: permanently gain `+1 active Home slot` |

#### $500-999 - Coin Counter

| Choice | Odds | Result |
|---|---:|---|
| Use the Machine | 70% | Return `125%` of the stake, rounded to the next `$25` |
| Use the Machine | 30% | Return `200%` of the stake |
| Open an Account | 65% | Business Account: interest cap `+$1,000` and `$500 Expense Credit` through next floor; if interest is already uncapped, gain `+5 percentage points` interest instead |
| Open an Account | 35% | Preferred Customer: base interest `+5 percentage points`; first paid Home reroll each Night costs `$0`, and the next paid reroll starts at `$50`; Game Console remains unused |

#### $1,000-4,999 - Trillionaire Adoption

| Choice | Odds | Result |
|---|---:|---|
| Accept Adoption | 65% | Family Office: permanent `+$250 Workday pay` and `+$250` Night manual-deposit cap |
| Accept Adoption | 35% | Adjusted Expectations: future player completion target is `ceil(90% of final shared size)` while Chad remains at 100%; Overdelivery uses the player target |
| Ask for a Modest Favor | 70% | Board Recommendation: every future manager begins at maximum Approval/Favorite |
| Ask for a Modest Favor | 30% | Family Health Plan: future promotion recovery `+15`; each new floor grants Guardian Angel if none exists |

#### $5,000+ - Declared a Planet

| Choice | Odds | Result |
|---|---:|---|
| Declare Independence | 65% | Planetary Citizenship: at future floor creation shift every coworker `+5 player / -5 Chad`; exact role-ballot ties favor player |
| Declare Independence | 35% | Planetary Constitution: choose one of three random unowned Galactic laws now, another at next Floor Briefing, then one per later Floor Briefing; future mystery Weekends use the Galactic deck |
| Monetize the Nation | 70% | Reserve Currency: eligible net-new Cash grants `x1.5`, round once; interest uncapped; `+2 Home purchases` per Night |
| Monetize the Nation | 30% | Universal Basic Luxury: each Night roll one eligible Home item using current Home odds and one legal ordinary Deal; choose one free. If neither exists, recover 10 and gain `$250 Expense Credit` |

Reserve Currency excludes refunds, returned stakes, financing principal, resale
basis, and transfers. Universal Basic Luxury has independent ordinary-Deal
access and does not unlock the complete Deal Desk.

### Tier 2

#### $0-499 - The Jar Gets Promoted

| Choice | Odds | Result |
|---|---:|---|
| Negotiate Compensation | 70% | Merit Increase: permanent `+$50 Workday pay` |
| Negotiate Compensation | 30% | Corporate Housing: `+$300` equity now and permanent `+$50` manual-deposit cap; at Penthouse gain `$300 Cash` |
| Put It in Management | 65% | Management Material: next manager begins `+1 Approval`; if already capped, gain `$100 Expense Credit` |
| Put It in Management | 35% | Golden Parachute: one run-wide charge suppresses one directive's printed Failure package and grants `$250 Cash`; status remains Failed |

Permanent `+$50` pay is an explicit low-band exception and balance watchpoint.

#### $500-999 - The Jar Becomes a Thought Leader

| Choice | Odds | Result |
|---|---:|---|
| Post Corporate Wisdom | 70% | Engagement Farming: first coworker each Workday to gain Relationship also gains `+3 player standing` |
| Post Corporate Wisdom | 30% | Viral Post: first supporter crossing each Workday gives every other undecided coworker `+2 player standing`; no recursion |
| Build the Network | 65% | Featured Connection: one seeded random coworker per future Floor Briefing gains `+2 Relationship / +5 standing` |
| Build the Network | 35% | Endorsement Deal: first supporter per future floor grants their archetype basic Favor as a capacity-free Reward Favor |

#### $1,000-4,999 - The Jar Gets an MBA

| Choice | Odds | Result |
|---|---:|---|
| Do the Coursework | 70% | Transfer Credits: choose one of three random Skills, gain 5 XP now; first eligible primary in that Skill each future floor gains `+1 XP` |
| Do the Coursework | 30% | Accelerated Program: every future eligible ordinary primary grants `+1` additional XP |
| Declare a Concentration | 65% | Study Group: once per Workday the eligible primary grants `+1 XP` to the lowest-XP different Skill |
| Declare a Concentration | 35% | Double Major: choose one of three random Skills and pair it with the lowest-XP different Skill; every XP grant to either mirrors once to the other |

Reward/effect Skill pickers show up to three seeded random eligible Skills.
Promotion Review and fixed tutorial choices remain fully available. Double
Major mirrored XP cannot mirror again and does not advance Closing Chain or
Brand Campaign progression.

#### $5,000+ - The Jar Goes Public

| Choice | Odds | Result |
|---|---:|---|
| Ring the Opening Bell | 70% | IPO Pop: gain Cash equal to `150%` of the frozen stake |
| Ring the Opening Bell | 30% | Beat the Street: regain 100% of stake; future Overdelivery payout choice is `50%` stronger without raising expectations |
| Keep Voting Control | 65% | Voting Shares: add one player Board ballot to every future Role Vote |
| Keep Voting Control | 35% | Founder Control: add two player Board ballots; exact final vote ties favor player |

Stake returns are settlement amounts and are not amplified by Cash-gain
multipliers.

### Tier 3

#### $0-499 - The Jar Becomes Essential Infrastructure

| Choice | Odds | Result |
|---|---:|---|
| Connect It to the Grid | 70% | Priority Service: first eligible task/action Stress package each Workday is `1 raw Stress` lower |
| Connect It to the Grid | 30% | Load Balancing: every eligible task/action package is `1 raw Stress` lower, cap `5` total per Workday |
| Apply for Public Funding | 65% | Infrastructure Match: match 25% of the next cumulative `$500` net Home Cash spending, maximum `$125`; at Penthouse pay Cash |
| Apply for Public Funding | 35% | Capital Improvement Plan: after the next Home move add `$500` toward the following Home; at/already Penthouse gain `$500 Cash` |

Stress reductions apply after other reductions and before floor scaling.

#### $500-999 - The Jar Enters Witness Protection

| Choice | Odds | Result |
|---|---:|---|
| Accept a New Identity | 70% | Sealed Record: reduce each involuntary Workday Relationship loss by 1, maximum 3 prevented per Workday |
| Accept a New Identity | 30% | Safe House: once per floor suppress the first hostile invitation trap that would apply |
| Testify Against Chad | 65% | Protective Detail: halve the first remaining Chad-conversation movement toward Chad each Workday, rounding down |
| Testify Against Chad | 35% | State's Evidence: every Chad conversation creates a trap-suppressed Opening with `+20 percentage points` and a 10-standing transfer on success |

#### $1,000-4,999 - The Jar Gets a Patent

| Choice | Odds | Result |
|---|---:|---|
| License the Patent | 70% | Licensing Revenue: choose one of three eligible completed tasks; its printed-effect resolutions pay `$100`, cap `$300/Workday` |
| License the Patent | 30% | Patent Portfolio: primary printed effect and first three recognized non-primary resolutions pay `$75` each, cap `$300/Workday` |
| Keep It Proprietary | 65% | Trade Secret: chosen patented task's first Complete Play each Workday resolves its full printed effect again |
| Keep It Proprietary | 35% | Monopoly Rights: first eligible ordinary primary each Workday resolves its full printed effect again |

Patent duplication reuses prepared choices, repeats positive and negative
printed clauses, delayed instances, and legal child plays, but grants no base
PP, task Stress, XP, counters, selection, or card-play trigger. Identity-bound,
Special, Closing, and non-task sources are ineligible. Automation migration
must precede Patent implementation.

#### $5,000+ - The Jar Becomes the President

| Choice | Odds | Result |
|---|---:|---|
| Pass Laws for Yourself | 70% | Cabinet Appointment Act: current manager grants their presidential floor rule |
| Pass Laws for Yourself | 30% | Executive Loyalty Act: same rule; suppress harmful manager-passive clauses, begin Favorite, and never fall below Pleased |
| Outlaw the Opposition | 65% | Chad Sanctions Act: multiply Chad's final gross daily PP by `0.75` |
| Outlaw the Opposition | 35% | Compulsory Endorsement Act: every future coworker Role Vote ballot is player |

Presidential manager rules:

| Manager | Floor rule |
|---|---|
| Micromanager | Every eligible ordinary primary gains one stress-free Replay |
| Slave Driver | Add two guaranteed Work entries every Workday |
| Penny Pincher | First Home item, Deal, and Outing each Night are each free; Home/Deal do not block Lights Out |
| Chaos Agent | Every rolled ordinary action and non-manager political check uses best-of-two; other reroll sources are preserved but unavailable on that check |
| Deadline Hawk | Meeting quota grants PP equal to `50%` of all player PP gained that Workday |
| Toxic Positivity | Double positive Relationship and player-standing movement; prevent Relationship loss |
| Absentee | Completing the directive resolves all three stance Success packages in Comply/Resist/Negotiate order; only selected cost is paid |
| Bean Counter | Interest is uncapped and final interest is `4x` normal, replacing ordinary doubling |

### Tier 4

#### $0-499 - The Jar Is Declared Sentient

| Choice | Odds | Result |
|---|---:|---|
| Give It a Job | 70% | Clerical Assistance: one seeded random eligible task-package slot each Workday gets `+1 base PP` if selected |
| Give It a Job | 30% | Performance Coaching: one seeded slot gets `+1 base PP / -1 base Stress` |
| Recognize Its Rights | 65% | Right to Disconnect: once per floor one Home or Deal purchase does not block Lights Out |
| Recognize Its Rights | 35% | Legal Personhood: permanent `+1 normal Favor capacity` |

#### $500-999 - The Jar Gets a Reality Show

| Choice | Odds | Result |
|---|---:|---|
| Play to the Cameras | 70% | Ratings Bump: first directive completed each floor grants `+1 additional Approval` |
| Play to the Cameras | 30% | Breakout Star: every Directive Success non-Approval numeric reward is `25%` stronger |
| Control the Edit | 65% | Sympathetic Edit: first failed directive each floor grants `+1 Approval` instead of its normal Approval change; other Failure clauses remain |
| Control the Edit | 35% | Final Cut: first failed directive each floor suppresses the complete printed Failure package and grants `+1 Approval`; status remains Failed |

Reward scaling stacks additively and never scales Approval, Relationship,
standing, odds, votes, duration, or counts.

#### $1,000-4,999 - The Jar Joins the Supreme Court

| Choice | Odds | Result |
|---|---:|---|
| Write the Majority Opinion | 70% | Rational Basis Review: qualifying non-manager political odds cannot finish below 50% |
| Write the Majority Opinion | 30% | Strict Scrutiny: raise qualifying odds one locked ladder step, then apply the 50% minimum |
| Issue an Injunction | 65% | Preliminary Injunction: once per floor suppress negative clauses from first failed qualifying political event |
| Issue an Injunction | 35% | Permanent Injunction: once per calendar day suppress negative clauses from first failed qualifying political event |

Costs remain consumed and Failure status remains. Terminal effects, deterministic
manager directives, ordinary action outcomes, Casino, and Weekend stories are
excluded.

#### $5,000+ - The Jar Is Now in the Systems

| Choice | Odds | Result |
|---|---:|---|
| Give It Admin Access | 70% | Administrator Privileges: current plus cached task/catalog candidates; selected primary also Automated-resolves itself; best-of-two action/politics; first Home item, Deal, and Outing each Night free and Home/Deal do not block Lights Out |
| Give It Admin Access | 30% | Root Access: manager costs 0; political required costs 0 and attached Favors/charges return; all Home items, Deals, and Outings cost 0 and never block Lights Out; one free reroll per catalog |
| Let It Run in the Background | 65% | Background Process: stress-free primary Replay; every successful non-terminal political positive package resolves twice; automatic Night recovery doubles; first Deal or Outing positive numeric package doubles |
| Let It Run in the Background | 35% | System Restore: first two unfavorable actions become favorable; one Workday burnout per floor sets Stress to 50; first two political failures per day become Success; Lights Out always legal and Night Stress caps at 50 |

These are intentional late-run win engines.

### Tier 5

#### $0-499 - The Jar Becomes an Urban Legend

| Choice | Odds | Result |
|---|---:|---|
| Feed the Rumor | 70% | Word Gets Around: first eligible Office Chat each floor gains one odds-ladder step |
| Feed the Rumor | 30% | Local Celebrity: one seeded random non-stakeholder per future floor gains `+1 Relationship / +2 standing` |
| Deny Everything | 65% | Plausible Deniability: reveal the first hostile invitation trap each floor, not its secret roll |
| Deny Everything | 35% | Haunted Break Room: reduce first remaining Chad-conversation movement toward Chad each floor by 2 |

#### $500-999 - The Jar Is Retroactively Made a Founder

| Choice | Odds | Result |
|---|---:|---|
| Take the Founder Package | 70% | Founder Salary: permanent `+$100 Workday pay` |
| Take the Founder Package | 30% | Founder Equity: `$500` house equity at every future promotion; at Penthouse gain `$500 Cash` |
| Rewrite the Org Chart | 65% | Executive Deference: every future manager starts `+1 Approval` |
| Rewrite the Org Chart | 35% | Founder Override: manager-package Cash costs `-$50`, minimum 0 |

#### $1,000-4,999 - The Jar Is Declared a Natural Law

| Choice | Odds | Result |
|---|---:|---|
| Bend Time | 70% | Time Dilation: add one seeded guaranteed-favorable non-Lunch Natural Schedule Entry every Workday |
| Bend Time | 30% | Causal Loop: repeat first positive ordinary action with same favorable outcome and participants |
| Change the Constants | 65% | Conservation of Space: permanent `+3 active Home slots` |
| Change the Constants | 35% | Accelerated Development: ordinary path thresholds become `1 / 8 / 18 XP` |

Accelerated Development includes Delegation and Schmoozing, excludes Closing
and Brand Strategy, and uses the existing single-capstone authority.

#### $5,000+ - The Jar Exists in Every Timeline

| Choice | Odds | Result |
|---|---:|---|
| Find the Best Timeline | 70% | Many Worlds: current plus one alternate per task/Night slot; one stress-free primary Replay; best-of-two actions/politics; first Home item, Deal, and Outing each Night free and Home/Deal do not block Lights Out |
| Find the Best Timeline | 30% | The Only Winning Timeline: three candidates per task/Night slot; two stress-free primary Replays; best-of-three actions/politics; every Home item, Deal, and Outing costs 0 and Home/Deal do not block Lights Out |
| Merge the Timelines | 65% | Timeline Convergence: stress-free primary Replay; first positive action repeats; first political success per day doubles; automatic Night recovery doubles |
| Merge the Timelines | 35% | Quantum Immortality: gain Convergence plus one run-wide start-of-floor rewind after non-victory defeat; retry uses new deterministic branch seed and best-of-two action/politics |

The rewind preserves manager, project, roster, Jar outcome, and a consumed
marker outside the restored snapshot. Doomed-floor gains and spending are
undone.

### Tier 6

#### $0-499 - The Jar Is Missing from the Final Report

| Choice | Odds | Result |
|---|---:|---|
| Let the Omission Stand | 70% | Omitted Incident: once per floor omit first unfavorable ordinary action that would worsen active manager objective from manager tracking only |
| Let the Omission Stand | 30% | Missing Chad Appendix: omit one Chad supporter from each morning pace snapshot |
| Blame Formatting | 65% | Creative Accounting: first cumulative `$100` Cash spent each floor still counts toward Accounted Cash and does not violate maximum/no-spend directives |
| Blame Formatting | 35% | Redacted Review: once per floor prevent first manager-authored Approval loss from failed directive |

#### $500-999 - The Jar Is Classified Above Top Secret

| Choice | Odds | Result |
|---|---:|---|
| Use the Black Budget | 70% | Untraceable Funds: gain `$200 Expense Credit` every Workday morning |
| Use the Black Budget | 30% | Black Budget Authority: gain `$350 Expense Credit` every morning; it may pay manager-package and required political Cash costs |
| Deny the Program Exists | 65% | Compartmentalized Assets: once per floor return first Favor or political charge consumed |
| Deny the Program Exists | 35% | Covert Extraction: once per floor first failed non-manager political event refunds committed Cash, Expense Credit, Favors, and charges and suppresses its Stress; other consequences remain |

#### $1,000-4,999 - The Jar Becomes the Alumni Hivemind

Active voices initially equal represented Alumni archetypes. If none exist,
synthesize one. Natural missing archetypes unlock immediately; one missing
voice is synthesized after each Night and becomes active next Workday.

| Choice | Odds | Result |
|---|---:|---|
| Merge Their Memories | 70% | Collective Memory: active voices grant base perks, rank at least 2, `+2 primary base PP / +$50 pay` per voice |
| Merge Their Memories | 30% | Shared Consciousness: active voices grant upgraded perks, rank at least 2, `+3 primary base PP / +$75 pay` per voice |
| Absorb the Network | 65% | Network Endowment: base perks, rank 3, `+2 primary base PP / +$50 pay` per voice, one guaranteed rank-3 gift each Night |
| Absorb the Network | 35% | Alumni Singularity: upgraded perks, rank 3, `+4 primary base PP / +$100 pay` per voice, one guaranteed rank-3 gift each Night; at six voices rates double |

Hivemind upgrades:

- Gatekeeper: prevent first two Approval losses per floor.
- Wildcard: reroll first two failed project dilemmas per floor.
- Pragmatist: first two Work actions each day gain `+2 PP`.
- Achiever: Stretch Goal raises one reward by two tiers without expectation.
- Networker: two non-stakeholders begin each floor `+5 standing / +1 Relationship`.
- Idealist: prevent first two Relationship losses per floor.

Per-voice PP modifies only the original primary's base PP before task
multipliers and Overdelivery. Guaranteed gifts replace the ordinary Alumni roll
and use normal Favor overflow.

#### $5,000+ - The Jar Acquires Reality

This is the unique Cash Jar capstone and does not consume the career capstone.

| Choice | Odds | Result |
|---|---:|---|
| Acquire the Assets | 70% | Controlling Interest: future project starts at 25% player progress; all Skills favored; adversarial penalties disabled; player PP `x1.5`; Chad gross daily PP `x0.5` |
| Acquire the Assets | 30% | Universal Ownership: immediately move to Penthouse; every Home set complete and Connected-upgraded; Home items/Deals/Outings cost 0 and Home/Deal never block Lights Out; interest uncapped at `4x` |
| Restructure Reality | 65% | Mandatory Consensus: completed and future rosters Relationship 10 and `100/0` standing; managers locked Favorite with harmful clauses suppressed; non-manager political choices 100% |
| Restructure Reality | 35% | Reality, Inc.: combine the complete Controlling Interest, Universal Ownership, and Mandatory Consensus packages |

Reality, Inc. does not immediately award victory. The final project and genuine
terminal rules still resolve.

## Locked Galactic Laws

Status: **Mixed Locked / Draft; ten Locked laws implemented behind the gate**

| Law | Status | Exact rule |
|---|---|---|
| Galactic Overtime | Locked | Add two random ordinary actions every Workday. |
| Group Project | Locked | After an eligible ordinary primary, choose a different visible generated, Pinned, or stored ordinary task. Consume its Pin/storage source and resolve a stressless Complete Additional Play with full XP, counters, printed effects, and child plays. Repeat no Selection, favored/adversarial consequence, Campaign, Sales Cycle, Close, or Automation start. Empty pool generates one seeded Common ordinary task from a different Skill. |
| Galactic Zoning | Locked | Apply every owned Home item's exact Zoning upgrade from the 29-item table. |
| Time Loop | Locked | Repeat the first positive ordinary action. Repeat sources are additive and nonrecursive: each distinct source adds one Action Resolution to the original; child repeats trigger no repeat source. |
| Investment | Draft values | Approved mechanic: eligible spending converts to PP. Draft value: every `$25` grants `1 PP`. |
| Galactic Gambler | Draft values | Approved mechanic: rerolls grant recovery and periodic PP. Draft values: recover 5 per reroll; every third reroll grants 10 PP. |
| Galactic Hostage | Locked | Trigger one Galactic event every two Workdays after Clock Out and before Night. If a real Weekend is due, its Galactic event consumes and resets the due Hostage trigger so only one event occurs. |
| Property Rights | Locked | Before Workday salary, snapshot every active Home item. Each grants the original selected primary `+1 base PP` and `+$50 Workday pay` for that Workday. There is no count cap. |
| Subsidiary | Locked | Mirror Chad's gains. With Joint Venture, replace both mirrors with Hostile Merger: from Chad's final calculated gain, player gains 100% and Chad retains 50%. |
| Groveling | Locked | Managers remain positive and all manager-package benefits favor the player. |
| Foresight | Locked | Pre-save one shared percentile roll per political event and reveal which choices succeed. A legal attached reroll pre-saves and reveals its second result. |
| One-Party State | Locked | Future coworkers begin Relationship 7 and `60/40` player standing. |

### Property Rights Ordering

- Use the same active-item authority as item effects and set completion.
  Orbital Warehouse counts every owned item because it makes those items
  active. Inactive, sold, destroyed, exhausted, and merely stored item records
  do not count.
- Freeze the active item IDs and count before salary. Buying, selling,
  exhausting, destroying, or otherwise changing an item later affects the
  following Workday's snapshot only.
- Add the PP to the original selected primary's base PP before task
  multipliers and Overdelivery. It applies exactly once and does not apply to
  Replays, Complete Additional Plays, copied Printed-Effect Resolutions,
  Remote Tasks, Automated Task Resolutions, or child resolutions.
- Add the pay to other additive Workday-pay bonuses before one final salary
  multiplier. Mercury Payroll percentages combine for that multiplier.
  Reserve Currency then applies to the resulting eligible Cash.
- Persist active item IDs, count, PP bonus, pay bonus, salary-settled state,
  and primary-applied state before presentation. Reload restores the snapshot
  without recounting items or repeating either benefit. Property Rights uses
  no RNG.
- Build Context, salary results, the primary modifier list, and Home inventory
  details show the concise item count and resulting PP/pay contributions.

## Galactic Weekend Deck

Status: **Locked replacement table; gated implementation verified**

This deterministic table explicitly supersedes the unavailable original event
tables.

Global rules:

- Every event shows two fully described beneficial choices.
- Draw without replacement through all twelve events.
- After exhaustion, reshuffle and exclude the immediately previous event.
- Galactic events replace future ordinary mystery Weekends after Planetary
  Constitution. Floor 3 Casino still follows.
- Hostage events resolve after Clock Out and before Night.
- A real Weekend event consumes and resets a due Hostage trigger.
- Repeated outcomes use event-specific upgrades. Maxed outcomes grant their
  event Encore.
- Mid-floor rewards begin at their next authored legal boundary and never
  recalculate settled state.
- Workdays exceeding twelve actions compress presentation without changing
  mechanics, politics, RNG, or Skip parity.

### 1. Moon PTO

Setup: The Moon approves PTO that predates the player's employment.

- **Take the Backdated PTO**
  - Next floor, Lights Out is automatic and Home/Deal purchases do not block
    it.
  - Flow State or a duplicate upgrades next floor's automatic sleep and Lights
    Out recovery to resolve twice.
- **Work the Lunar Shift**
  - Next floor, add one seeded guaranteed-favorable non-Lunch Natural action
    each Workday.
  - Duplicate upgrades this to two actions.
- Routes coexist.
- Encore: recover 15 Stress and gain 5 Well Rested.

### 2. Mercury Payroll Error

Setup: Mercury retrograde duplicates the player's payroll record.

- **Report the Error**
  - Permanent `+50%` final Workday pay.
  - Duplicate upgrades it to `+100%`.
- **Keep the Overpayment**
  - Permanent `+10 percentage points` interest and `+$1,000` interest cap.
  - Duplicate upgrades it to `+20 points / +$2,000`.
  - Each unusable `$1,000` cap increase under uncapped interest converts to
    `+5 percentage points`.
- Routes coexist. Pay percentage modifiers combine additively before one final
  multiplier.
- Encore: `$1,000 Cash + $500 Expense Credit` through the next Night.

### 3. Venus Replied All

Setup: A private message about everyone has been sent to everyone.

- **Own the Thread - Nothing Is Private Now**
  - Next roster starts Relationship 7 and `60/40` player standing.
  - Duplicate or One-Party State upgrades it to Relationship 10 and `70/30`.
- **Let It Go Viral - Public Profile**
  - Next floor, each coworker's first positive Relationship gain also grants
    `+5 player standing`.
  - Duplicate upgrades it to `+10`.
- Routes coexist.
- Encore: capacity-free Vouch for You and Bring Them In Reward Favors.

### 4. Mars Team Building

Setup: The mandatory offsite is on Mars, and Chad volunteers to lead.

- **Join the Trust Fall - Team Cohesion**
  - Each player supporter subtracts 2 additional percentage points from Chad's
    pace.
  - Duplicate raises the additional subtraction to 4 points.
- **Take Command - Command Authority**
  - Halve Chad's positive role, manager, and boss pace modifiers.
  - Duplicate removes those positive modifiers.
- Owning both adds **Controlling Authority**: Chad's final gross daily gain is
  another `10%` lower.
- Every component is separately itemized in Chad's forecast.
- Encore: player gains `5 * floor PP`; Chad loses the same amount, minimum
  zero.

### 5. Jupiter's Memo

Setup: Jupiter circulates a policy memo large enough to create weather.

- **File Under Risk - Jupiter Risk Policy**
  - After limited card/item protections, reroll the next eligible unfavorable
    ordinary action each Workday.
  - Duplicate protects the first two.
- **File Under Visibility - Jupiter Visibility Policy**
  - Add one shared directive-preview step each Night.
  - Duplicate adds two.
  - Shared ladder: category, exact directive, then choose one legal template.
  - Excess preview sources grant `+1 Approval` once per floor.
- Owning both unlocks **Innovation Addendum**.
  - First copied Printed-Effect Resolution each Workday gets `+50%` positive
    numeric values.
  - If no copy resolves, grant `+5 PP` after the primary chain.
  - With both components upgraded, affect the first two copies or grant
    `+10 PP`.
  - Source ancestry prevents recursion.
- Encore: `+1 Approval` and one capacity-free Do-Over Reward Favor.

### 6. Saturn's Org Chart

Setup: Saturn provides an org chart made entirely of rings and dotted lines.

- **Archive the Org Chart - Archived Authority**
  - Retain the outgoing project's full player role reward regardless of role
    owner.
  - One archived reward remains active alongside the current role.
  - Duplicate raises archive capacity to two.
- **Draw the Dotted Lines - Matrix Authority**
  - Future role rewards actually won by the player persist after promotion.
  - Keep the two most recent archived rewards.
  - Duplicate raises capacity to three.
- Owning both creates **Executive Archive**.
  - Archive outgoing player-role rewards regardless of owner.
  - Keep the three most recent at full authored strength alongside the current
    role.
- Hostage acquisition waits for the next legal role-resolution or retirement
  boundary.
- Encore: `+1` player Board ballot on the next unresolved Role Vote; if none
  remains, gain `+10 PP and $500 Cash`.

### 7. Comet Delivery

Setup: A comet reaches the loading dock, and Shipping says the player signed
for it.

Both choices advance shared Galactic Logistics:

- Rank 1: **Cargo Bay**, `+3 active Home slots`.
- Rank 2: **Orbital Warehouse**, all owned Home items remain active and count
  toward sets regardless of Home capacity.

Choices:

- **Open the Crate**
  - Gain one seeded free unowned Home item using current Home rarity odds and
    one banked Home reroll.
  - If every item is owned, convert the item to `$1,000 Cash`.
  - An unusable reroll converts to `$250 Cash`.
- **Sell Shipping Rights**
  - Gain `$1,000 Cash + $500 house equity`.
  - Penthouse converts equity to Cash.

After Rank 2, each selected delivery package becomes that choice's repeat
Encore. Home level still controls comfort, deposits, and rarity odds.

### 8. Pluto's Appeal

Setup: Pluto appeals its classification and offers to add the player's
expectations claim.

- **Grandfather the Scope**
  - Remove up to three project-size expectation tiers.
  - Duplicate grants complete project-size expectation immunity.
- **Protect the Rating**
  - Remove up to three Chad-pace expectation tiers.
  - Duplicate grants complete Chad-pace expectation immunity.
- Owning both creates **Protected Status**.
- Resolution order:
  1. calculate raw expectation;
  2. apply Pluto protection;
  3. apply other expectation-reduction sources;
  4. each external reduction tier left unused becomes one expectation-free
     payout tier.
- Pluto's own removed tiers never create payout tiers.
- Encore: `$1,000 Cash` and recover 20 Stress.

### 9. The Sun's PIP

Setup: The Sun places the player on a performance plan for insufficient output.

- **Request Accommodations - Solar Shield**
  - Prevent the first 5 positive task base-Stress points each Workday.
  - Duplicate raises the shield to 10.
- **Sign the PIP - Solar Output**
  - Apply all task base-Stress reducers first.
  - Rank 1: each prevented point grants 2 base PP; each remaining point grants
    1 base PP; remove the remaining base Stress.
  - Duplicate raises the conversion to 3 PP and 2 PP.
- Solar PP belongs to the resolving Complete Play and receives normal task and
  Overdelivery scaling.
- Printed, flat, trait, political, and other non-base Stress are excluded.
- Encore: next eligible primary gains `+10 base PP / -10 base Stress`.

### 10. Black Hole 401(k)

Setup: Benefits opens a retirement account with an event horizon.

- **Max the Match - Event Horizon Match**
  - Count one independent Black Hole Reserve Level per `$500 Cash`.
  - Rank 1: cap 5; each grants `+1 PP / +1 recovery`.
  - Duplicate: cap 10; each grants `+2 PP / +1 recovery`.
  - Compound Interest benefits stack separately.
- **Roll It Over - Singularity Interest**
  - Rank 1: final interest `x1.5`, cap `+$2,000`.
  - Duplicate: final interest `x2`, cap `+$4,000`.
  - Each unusable `$2,000` cap component under uncapped interest converts to
    `+10 percentage points`.
- Encore: `$2,000 Cash` and recover 20 Stress.

### 11. Galactic All-Hands

Setup: Every current and former coworker joins one call; nobody can locate
Mute.

- **Recognize the Room - Loyalty Resolution**
  - Rank 1: choose up to three current coworkers to become loyal.
  - Duplicate: make the complete current roster loyal.
  - Every already-loyal target grants its archetype's capacity-free Reward
    Favor.
- **Fund the Network - Alumni Endowment**
  - Rank 1: every represented archetype gains `+1 Network rank`.
  - Duplicate: every represented archetype gains `+2 ranks`.
  - Missing archetypes and capped/excess increases grant their mapped Reward
    Favor.
- Weekend acquisition resolves before outgoing-roster retirement.
- Encore after both routes are maxed: grant all six capacity-free basic Reward
  Favors.

### 12. Alien Recruiter

Setup: An alien recruiter says the player's experience is transferable, though
not necessarily to Earth.

- On the first Alien event, choose one persistent placement Skill from three
  seeded random Skills.
- **Take the Specialist Offer**
  - Rank 1: placement Skill gains 10 XP.
  - Duplicate: placement Skill gains another 15 XP.
- **Join the Rotation**
  - Rank 1: the two lowest-XP non-placement Skills gain 5 XP.
  - Duplicate: all four non-placement Skills gain 5 XP.
- Every 5 Alien-granted XP above 20 in a Skill creates one permanent Alien
  Seniority rank: tasks of that Skill gain `+1 base PP`.
- Remainders persist.
- Seniority applies to ordinary Complete Plays and Automated Task Resolutions,
  not copied effects.
- Encore: one Seniority rank for all five Skills.

### Data, Persistence, And UI

Implemented records:

- `GalacticEventDefinition`: ID, title, setup, two choices, component ranks,
  combined upgrade, Encore, legal boundary, and fallbacks.
- `GalacticDeckState`: draw bag, discard order, previous event, Hostage
  counter, pending event, choice, result, and settled marker.
- `GalacticRewardState`: component ranks, permanent effects, deferred
  boundaries, Alien placement/Seniority, Saturn archive, and Comet logistics.

Stable checkpoints:

- `galacticEvent`
- `galacticEventResult`

Save choice, targets, generated item/task/Skill candidates, ranks, deferred
effects, focus, and pending Night/Weekend route before presentation. Reload
never redraws event, reward, item, target, or Skill state.

UI requirements:

- show setup and two complete deterministic beneficial choices;
- concise result plus accessible Details;
- Orbital Warehouse inventory supports every owned item without rendering all
  items in the room;
- Mars modifiers appear separately in Chad's forecast;
- presentation compresses after twelve actions without changing state; and
- keyboard, touch, screen reader, reduced motion, short landscape, and 200%
  text remain required.

## Implemented Guided Intern

Status: **Implemented**

- Mandatory once per profile; no opt-out after start.
- Wednesday-Friday authored scenario with Onboarding Coordinator.
- Fixed tasks: Bug Triage, Regression Tests, Production Hotfix.
- Final project result: `52 / 45`, exactly one Overdelivery tier.
- Chad ends at `36 / 45`.
- Teaches one Comply, Negotiate, and Resist package; Safe/Balanced/Risky
  project choices; Office Politics; Chad Opening; Night; Weekend; payout; and
  Promotion Review.
- Wednesday: Bug Triage, `DIR-COLL-01` Comply, Delivery Safe, one Work action,
  player `18 / 45`, Chad `15 / 45`, Role Vote, and Blackout Curtains.
- Thursday: Regression Tests, `DIR-COLL-02` Negotiate for `$50`, Leverage
  Balanced, Priya Chad Opening, Build Rapport to Relationship 10, player
  `28 / 45`, and Chad `26 / 45`.
- Friday: Production Hotfix, `DIR-PROC-02` Resist, Quality Risky fixed success,
  player `52 / 45`, Chad `36 / 45`, one Overdelivery tier, `$150` Cash payout,
  `$50` Condo deposit, Side Gig `Decline Politely`, and Promotion Review.
- Carry approximately `$762`, Blackout Curtains, `$50` Home equity, 3 Coding
  XP, one expectation tier, Priya as Idealist Alumni, and `+1` manager
  reputation into Associate.
- Eighteen high-trust checkpoints use short dialogue, a day-local checklist,
  spotlight, Continue, action-aware Show Me, and conditional Why. Repeat is
  removed. Instructions never auto-advance and do not explain obvious labels.
- `GI-OPEN` remains one checkpoint with four mandatory presentation steps:
  Project Progress, Chad and `3 WORKDAYS · WED–FRI`, Project Fit, and Karen/Bob
  stakeholder context. Back/Next advances `1/4` through `4/4`; only the final
  step exposes Clock In.
- Opening Show Me is removed. The actual Project Progress HUD is highlighted,
  a bold pixel connector points from the compact Coordinator card to each
  target without overlap, and
  `tutorialLessonState.openingStep` reloads without gameplay or RNG changes.
- Favored and Adversarial use function-first opening copy, exact accessible
  tooltips, and exact Morning confirmation disclosure for relevant tasks.
- Exactly four optional Why explanations remain: manager settlement,
  Relationship versus standing, Lights Out blocking, and Overdelivery
  expectations.
- The Guided opening has zero vertical overflow at desktop, scaled desktop,
  200% text, and short landscape.
- Clean Code, Automation, and Debugging are reviewed one at a time. After all
  three are viewed, the player freely chooses the only genuine Guided branch.
- Deals, Casino, Cash Jar, unrelated Skills/cards/items, random generation,
  bosses, Favors, Campaigns, Sales Cycles, and exceptional plays are excluded.
- The old thirteen-step Orientation is removed. `REPLAY GUIDED INTERN` starts
  a fresh real Guided run after the normal active-run replacement warning.
- Existing active ordinary runs are never interrupted. Later ordinary New Runs
  use the normal Intern floor unless replay was explicitly requested.

## Implemented Resume Rail Footer

Status: **Implemented**

- Expanded desktop width is `clamp(180px, 13vw, 230px)`; Workday remains 70px.
- Each compact Skill row shows exact XP or Closing Chain on the bottom left and
  one continuous progress bar on the bottom right.
- Secondary states are `PATH n`, `PATH READY`, and `NEXT n`.
- Ordinary paths fill toward 20 XP, Accelerated Development toward 18 XP, and
  Closing toward Chain 9. Exact XP remains uncapped after the bar fills.
- One family-specific 16px pixel marker identifies the next milestone:
  monitor, clipboard, paintbrush, briefcase, or box.
- Final milestones remove next text and the marker, fill the bar, and add a
  brighter frame with pixel corners.
- Active capstones add a gold star and double frame. Their acquisition shimmer
  runs once, does not survive reload, and is static under reduced motion.
- The Resume Book retains its detailed 20-square track and milestone tooltips.
- The presentation model, marker movement, resizing, and shimmer consume no
  gameplay state or gameplay RNG.

## Validation Status

| Area | Status |
|---|---|
| Current HTML, Phases 1-5, and Home Phase 1 | Implemented; focused/browser/persistence evidence Pass |
| Seven Homes, 28 available items, and nine sets | Implemented; Cash Jar remains gated |
| Locked Cash Jar 24-cell matrix | Gated implementation verified: 24 stories, 48 choices, 96 outcomes and handlers |
| Galactic laws | Ten Locked laws and acquisition verified behind the gate; Investment and Galactic Gambler remain Draft and unavailable |
| Galactic deterministic replacement event table | Gated implementation verified: 12 events, 24 choices, upgrades, Encores, persistence |
| Guided Intern | Implemented; focused 47/47, four-step opening with pixel connector, exact wording, carryover, mode parity, opening/political reload, action-aware Show Me, accessibility, and requested regressions Pass |
| Resume rail footer and family markers | Implemented; Phase 5 state matrix, 20-square Resume Book preservation, five icons, capstone shimmer/reload, reduced motion, responsive clipping, and RNG inertness Pass |
| Political decision focus | Implemented; live/restored decisions hide competing Workday chrome, use saved inline context, and embed Guided instruction without changing gameplay or RNG |
| Complete no-scrollbar UI | Implemented; 354/354 desktop, short-landscape, portrait, and 200-percent-text surface checks plus broad visual matrix Pass |
| Whole-run simulation phase integrity | 750/750 complete with zero errors after Delegation Floor Briefing promise repair |
| Automated skilled simulation | 1,000 seeds complete: 0 wins, 640 Chad losses, 343 burnouts, 17 firings; policy/balance evidence only |
| Cash Jar player-legal policy | 300 runs: 90 natural acquisitions, 29 Opens/outcomes, 0 breaks, 0 errors; Tier 3 target produced no Opens |
| Home browser/accessibility automation | Pass for focused UI, keyboard/touch tooltips, short landscape, and 200% text |
| Formal screen-reader and Home human playtest | Not Run |

Historical snapshots and discarded alternatives are indexed in
`ARCHIVE_SUPERSEDED.md` and are not active guidance.
