# OfficeWars Cash Jar Full Verification

Date: 2026-09-22

## Candidate

- Root HTML SHA-256:
  `FB2B6DE27C3032D520501A78E6E7651C7367C25BB65C019FD5DA1763DEF83859`
- Size: `1,538,306` bytes
- Active-run schema: 9
- Cash Jar target schema: 10, inactive
- `OW_CASH_JAR_RELEASE_ENABLED`: `false`
- Public mirror HTML:
  `360CC6C08F3040D92EF8764350CCC4D3A110BEF3B5AE8CD0CDED269E7C29E82B`

This report verifies the complete gated Cash Jar implementation. It does not
activate Cash Jar, schema 10, canonical public release, mirror synchronization,
or a release ZIP.

## Executive Verdict

| Gate | Verdict |
|---|---|
| Cash Jar story and handler completeness | Pass |
| Cash Jar lifecycle, UI, and persistence | Pass |
| Locked Galactic dependency implementation | Pass |
| Timeline, Hivemind, and Reality composition | Pass |
| Existing gameplay regression stability | Pass |
| Focused deterministic playback | Pass |
| Whole-candidate headless simulation | Fail |
| Cash Jar balance readiness | Not Ready |
| Formal accessibility certification | Not Run |
| Distribution readiness | Fail |
| Gated implementation readiness | Pass |
| Player-facing activation readiness | Fail |
| Overall Cash Jar release readiness | Not Ready |

The root contains a complete gated implementation, but it is not ready for
activation or publication.

## Critical Release Blocker

The general simulator has an asynchronous phase race when a promoted run owns
Delegation:

1. `nextFloor()` calls the wrapped `floorIntro()`.
2. `floorIntro()` starts `owPhase4RunFloorBriefing()` and returns before its
   promise completes.
3. The simulator starts the next Morning.
4. The late briefing callback calls the original floor intro and overwrites
   the phase from `morning` back to `floorIntro`.
5. The next simulator loop fails with
   `Simulation expected morning, received floorIntro.`

The 750-run full audit reproduced 20 baseline and 3 random failures. Focused
diagnostics reproduced seeds `910001` and `1010027` at Floor 3, run day 9.
Cash Jar was `unoffered`, its feature flag was false, Galactic laws were empty,
and Timeline was inactive in both failing states. This is a pre-existing
headless promotion dependency defect, not a Cash Jar outcome defect, but it
violates the release requirement for deterministic headless execution.

No gameplay repair was made during this verification-only task.

## Bidirectional Requirement Matrix

### Foundation And Lifecycle

| Requirement | Code/UI/evidence | Verdict |
|---|---|---|
| Eligible catalog only at ordinary Cash <=$500 | Catalog eligibility and core verifier | Pass |
| Purchase consumes all ordinary Cash and bypasses discounts/credit/financing/free effects | Home purchase authority and core verifier | Pass |
| Unique, nonsellable, no reacquisition after terminal state | Home generation and lifecycle state | Pass |
| $25 morning income after salary/before task | Cash transaction and core verifier | Pass |
| Positive ordinary-Cash outflow breaks before downstream benefit | Central Cash authority and core verifier | Pass |
| Expense Credit, refunds, returns, transfers, and zero outflow do not break it | Cash classification suites | Pass |
| Weekend Keep/Open replaces ordinary mystery Weekend | Weekend routing and core verifier | Pass |
| Keep raises Tier once with no reward | Core and release UI verifier | Pass |
| Keep unavailable at Tier 6 or without a later Weekend | Core and release UI verifier | Pass |
| Open freezes and consumes exact stake, band, Tier, and story | Core and release UI verifier | Pass |
| Choice labels reveal no probabilities or outcomes | All 24 story pages in release UI verifier | Pass |
| One saved roll and exactly-once settlement | Core and focused outcome suites | Pass |
| Floor 3 Casino routing survives | Core and Galactic routing evidence | Pass |
| Weekend, story, and result checkpoints restore without redraw | Release UI verifier | Pass |

### Story Inventory And Outcome Families

Every story contains two choices and four stable outcome IDs.

| Story cells | Outcomes | Focused authority | Verdict |
|---|---:|---|---|
| T1/B1-B3 | 12 | Simple economy/Home | Pass |
| T1/B4 | 4 | Social, planet economy, Planetary Constitution | Pass |
| T2/B1 | 4 | Simple economy/Home | Pass |
| T2/B2 | 4 | Social/political/manager | Pass |
| T2/B3 | 4 | Progression/task/Patent | Pass |
| T2/B4 | 4 | Public-market and voting | Pass |
| T3/B1 | 4 | Infrastructure/stress/Home funding | Pass |
| T3/B2 | 4 | Social/political/manager | Pass |
| T3/B3 | 4 | Progression/task/Patent | Pass |
| T3/B4 | 4 | Presidential manager rules | Pass |
| T4/B1 | 4 | Sentient task and rights | Pass |
| T4/B2-B3 | 8 | Directive and political authorities | Pass |
| T4/B4 | 4 | Systems/Admin Access | Pass |
| T5/B1 | 4 | Social/political/manager | Pass |
| T5/B2 | 4 | Founder/simple authorities | Pass |
| T5/B3 | 4 | Natural Law | Pass |
| T5/B4 | 4 | Timeline | Pass |
| T6/B1-B2 | 8 | Report/black-budget/social authorities | Pass |
| T6/B3 | 4 | Alumni Hivemind | Pass |
| T6/B4 | 4 | Reality | Pass |
| Total | 96 | Inventory: 96 known handlers, 0 remaining | Pass |

### Shared Composition

| Requirement | Evidence | Verdict |
|---|---|---|
| Candidate expansion and legal empty-pool fallback | Timeline | Pass |
| Shared best-of-N rolls | Systems, Timeline, Galactic Foresight | Pass |
| Primary Replay source ancestry and stress exclusions | Systems, Timeline, advanced chains | Pass |
| Causal Loop, Espresso, Time Loop, Timeline repeat additivity | Natural Law, Timeline, advanced chains | Pass |
| Political-success and recovery doubling without duplicate settlement | Systems, Timeline | Pass |
| Quantum start-of-floor rewind, branch seed, reload, CEO exclusion | Timeline | Pass |
| Hivemind voice synthesis, ranks, upgraded perks, gifts, PP/pay ordering | Hivemind | Pass |
| Administrator/Hivemind/Timeline/Reality primary and derived-play ordering | Reality | Pass |
| Universal Ownership free purchases without phantom Cash transactions | Reality | Pass |
| Mandatory Consensus current/completed/future roster and manager rules | Reality | Pass |
| Reality, Inc. preserves genuine terminal outcomes | Reality | Pass |

### Galactic Laws And Events

| Requirement | Evidence | Verdict |
|---|---|---|
| Planetary Constitution acquisition and later Floor Briefings | Galactic | Pass |
| Ten Locked laws available; two Draft laws excluded | Galactic | Pass |
| Overtime, Group Project, Zoning, Time Loop | Galactic and Home Matrix | Pass |
| Hostage, Property Rights, Subsidiary, Groveling, Foresight, One-Party State | Galactic | Pass |
| Twelve-event no-replacement deck and reshuffle exclusion | Galactic | Pass |
| All 24 event choices settle | Galactic | Pass |
| Duplicate upgrades, combined routes, and Encores | Galactic | Pass |
| Deferred boundaries and exactly-once persistence | Galactic | Pass |
| Responsive event UI and result reload | Galactic | Pass |
| Investment and Galactic Gambler | Draft and unavailable | Pass boundary |

### Existing Gameplay Dependencies

| Area | Evidence | Verdict |
|---|---|---|
| Phase 1 calendar, lock, Overdelivery, Chad pace | 25/25 | Pass |
| Phase 2 resources and frozen politics transaction | 20/20 | Pass |
| Phase 3 projects, managers, directives, bosses | 21/21 | Pass |
| Phase 4 rosters, loyalty, invitations, votes | 18/18 | Pass |
| Phase 4 dependency repair | 15/15 | Pass |
| Phase 5 progression and all fifty cards | 21/21 | Pass |
| Today's Directive | 13/13 | Pass |
| Home items, sets, and lifecycle | 39/39 | Pass |
| Advanced interactions and worst-case termination | All groups | Pass |
| Night Planner and Home layouts | Desktop/landscape | Pass |
| Task keyword and tooltip contract | Desktop/landscape | Pass |
| Persistence and tutorial | 26/26 | Pass |
| Smoke | `PASS:OVERHAUL` | Pass |

## Determinism And Persistence

- Timeline, Hivemind, and Reality each passed watched
  1x/2x/4x/Skip/headless equality and were repeated under full rigor.
- Cinematic Workday passed 32/32 twice, including hard political pauses,
  no Back/defer, reload to the same unanswered event, reduced motion, and
  results order.
- Cash Jar Weekend, story staging, and settled result each restored identical
  records, rewards, and RNG.
- Quantum rewind reload and exactly-once consumption passed.
- General whole-run simulation fails the Delegation Floor Briefing race
  described above.

## UI And Accessibility

The current-hash Cash Jar release verifier passed 10/10:

- all 24 story pages show exactly two named choice buttons;
- no probability or outcome text leaks before commitment;
- keyboard activation reaches Open, story choice, Details, and Continue;
- Tier, band, stake, Keep reward, and exact Open forfeiture are visible;
- desktop, compact, short landscape, 200-percent text, and reduced motion have
  no horizontal overflow;
- portrait correctly shows the rotation gate; and
- browser, console, and external-request errors are empty.

Fresh captures were inspected:

- `.officewars-screenshots/cash-jar-release-desktop-FB2B6DE2.png`
- `.officewars-screenshots/cash-jar-release-landscape-FB2B6DE2.png`

Both captures are readable, unclipped, and preserve clear Keep/Open hierarchy.

Not Run:

- formal screen-reader execution;
- certification across a physical touch device; and
- broad current-hash human playtesting.

## Simulation And Balance Evidence

### Full Audit: 250 Runs Per Policy

| Policy | Completed | Errors | Wins |
|---|---:|---:|---:|
| Baseline | 230/250 | 20 | 0 |
| Random | 247/250 | 3 | 0 |
| Skilled | 250/250 | 0 | 0 |

The errors are the Delegation Floor Briefing race. Because policy parity
fails, these runs do not support a balance verdict.

### Independent Skilled Telemetry

Seeds `1110000-1110999` completed without browser or console errors:

- wins: 0;
- Chad/rival losses: 640;
- burnouts: 343;
- firings: 17;
- Floor 2 reached: 859;
- Floor 3 reached: 234;
- Floor 4 reached: 17;
- Floor 5 reached: 1;
- Floors 6-7 reached: 0.

This is far below the 25-35% skilled-player target. The policy is not adequate
evidence for tuning or for active Cash Jar balance because ordinary Cash Jar
acquisition is disabled and high-tier outcomes are never exercised.

Cash Jar balance readiness is therefore **Not Ready / active-policy simulation
Not Run**. No values were changed.

## Distribution And QA Consistency

- Root gameplay hash remained unchanged throughout verification.
- The final public-mirror verifier passed 10 checks and failed 3:
  mapped-byte equality, the exact four-record root-only difference, and record
  count difference.
- Nine mapped files are intentionally stale pending release:
  the HTML, Home Matrix verifier, AGENTS, five active status/design documents,
  and the verification checklist.
- The new full-verification report is the fifth root-only verification record
  until publication is approved; the four private-vault records remain the
  exact protected private set.
- `CLAUDE.md` and automation-policy structure passed. The final guidance
  verifier passed 16 checks and failed only root/public AGENTS byte equality,
  because the root guidance now describes the gated candidate.
- Active root Game Design, Balance Ledger, Handoff, Project Status, Working
  With Agents, and Verification Checklist were corrected to distinguish:
  complete gated implementation, disabled activation, and old public mirror.
- Home Matrix was repaired to report the actual tested file hash instead of a
  stale literal.
- The public mirror was not synchronized because activation/publication was
  not approved and the release verdict is Not Ready.
- No release ZIP was built.

## Test Artifact Hashes

| Artifact | SHA-256 |
|---|---|
| Cash Jar core | `0A50EFFD46E33937DFD5B50BEA99A78B21C420E1BD5FF712CA3F51A07A004936` |
| Simple outcomes | `0A599EB954B3BB3B17D2D56F193A17FDE1E356A4C08DA4B1585CA5D5527A8F9A` |
| Social/manager | `BEA409059499DB01177947901367F30803A34958C07FB2C83C067B0EB9410141` |
| Progression/Patent | `AD2095604B7C511DB528129A986BFA7A5D649BD85439591D057FD865FED2C17F` |
| Infrastructure | `FD3E0FB39A645641E8096A71D6A95CD13CCE7A974948E5786B5032BD3DAAB2E1` |
| Sentient | `A59572490783A73BADEA74D2FBDC1DD14B254D23AB09E5E1D1C41AD9E274FD57` |
| Systems | `D3B05DB0B07368F9F485DFFCE49B3EA54DC04FE2476604A15FFCE41CCAEF1E2F` |
| Natural Law | `8E6858FA791CBC37B76D3CB87F58EE500021C26FF415073EDC0E36B3DF2134F5` |
| Timeline | `9D9BE59C04AC7FE32DA44F8E051538DFEA166D1EF67A923A90AECA732466ACE8` |
| Public outcomes | `9DE063C31A0B40B279F6B099F493F4D3DDA8714FD5F6B61E4587EAF9503CA05C` |
| Planet economy | `8BB7233A78995B0AEA68336BBFE3CB9D689B03F4D215D62A7E868AB6A6234002` |
| Galactic | `2AC4D660AF88DB83612DEA3F3688115128AC84DF7C1A99E6E143F3F2264AA04F` |
| Hivemind | `9388630A7DEA41709BF2E5CF34BE987DBE0D3375EC0F8D9063B4C582EC20096C` |
| Reality | `910149B66D75171A5B6FA77C921EA2AD46D4EE54104CF43290C789F955FD514F` |
| Inventory | `84DA6B9382D3566331F6B52D612CD94A094D7D3E2C7F2DF986E59F8DF0C25DF1` |
| Cash Jar release UI | `1415113C457D8949390621F5B2F24DDBFE2E2433F9F6764FE0DD4855124B6467` |
| Simulation diagnostic | `22C8E4F78D9DAB160000306DA57C05AF68144D479C7AE6182473422C0708A407` |
| Full audit | `75CB0F74B4799879AA296492F685C180DEFF2B67AFE8472723FC9E9C4CCCB769` |
| Skilled telemetry | `62378F333A4E783BB52DE6011DAF64F8F6FDCA2FD3267CEC680A82C8BBCCD8C2` |
| Home Matrix | `B009A3E904723C4C9BB805E235928B268EA839F0BB81F15388F6971063CE4363` |
| Cinematic Workday | `23AA1EE9CBB81C0BDB45AD99E7A8E3B866B8DAE3289F2AD0C49BBEC68001063A` |
| Persistence/tutorial | `C8A7025F873FAE9CF7483A8C17146D4283BC29C2378A97D3AFEC81A572A187B1` |

## Ship Decision

**Do not activate or publish Cash Jar yet.**

The 96-outcome gated implementation and its player-facing surfaces are
implementation-ready. Release readiness fails because whole-candidate
headless simulation is not deterministic at the Delegation Floor Briefing
boundary, the current automated policy provides no credible balance evidence,
active Cash Jar balance is untested, and the public mirror remains the old
candidate.

The next engineering action is a narrow Delegation Floor Briefing headless
race repair followed by repeated full simulation and Cash Jar release
verification.
