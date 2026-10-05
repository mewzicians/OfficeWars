# OfficeWars Full No-Scrollbar Verification

Date: 2026-09-22

Candidate:

- SHA-256:
  `BBBD39F7E46FADC451F3F0CF69A811A72DD04F32F861A85D517BE738A2CFA17E`
- size: `1,680,694` bytes
- active-run schema: 9
- Cash Jar target schema: 10, inactive
- Cash Jar public gate: disabled

## Verdict

The complete supported player-facing interface passes the no-scrollbar release
gate. Long surfaces now reflow, condense, or paginate instead of exposing a
scrollbar or clipping controls. The focused browser verifier completed 354
surface/page checks across desktop, short landscape, portrait rotation, and
200-percent text with zero overflow failures.

The broad ordinary visual-capture matrix also passes. Guided Intern,
persistence, deterministic cinematic playback, progression, Home/Night,
Cash Jar release UI, and smoke regressions pass on this candidate.

This does not authorize Cash Jar activation, schema 10, public synchronization,
or release packaging.

## Implemented Surface Authorities

- Morning uses `TASKS` and `CONTEXT & PINS` pages, responsive compact cards,
  and a resize/text-scale refit authority.
- Resume shows one career path at a time. Active Buffs use category and entry
  pages. Large Home inventories use bounded pages.
- Clock Out separates Summary, People & Carryover, and paged Source Log.
- Schedule comparisons retain every option in the DOM while presenting one
  complete schedule page at a time.
- Office Politics pages large-text rosters and coworker detail groups.
- Politics Review pages review sources, choices, and large result batches.
- The Workday Action Guide and cinematic wrap-up page long result sets.
- How to Play pages long topics by paragraph while retaining thirteen topics.
- Promotion, Automation, pinned-task detail, Floor Intro, Casino, Weekend,
  Cash Jar, Galactic, and game-over surfaces use responsive fit rules.
- Large-text HUD layout prevents run, project, and player panels from
  colliding.
- Poker now chooses coworkers from the current floor roster instead of retired
  legacy IDs, allowing the current Casino table to render.

Presentation-only page state consumes no gameplay RNG and does not alter
settlement, replay, schedule, or save authorities.

## Focused No-Scrollbar Matrix

| Area | Coverage | Verdict |
|---|---|---|
| Menu, Options, all Help topics and sections | desktop, landscape, 200% text | Pass |
| Ordinary and Guided Floor Intro | desktop, compact, landscape, 200% text | Pass |
| Morning tasks, Build Context, pins, Campaign | all responsive modes and both pages | Pass |
| Resume, paths, buffs, tooltips, pinned detail | every page/category | Pass |
| Home inventory and Chad forecast | up to twenty inventory items | Pass |
| Schedule rows and slot pickers | every schedule page | Pass |
| Workday ticker and Action Guide | every guide page | Pass |
| Live politics, Politics Review, result batches | every choice/result page | Pass |
| Cinematic political choice and twelve-result reel | every result page | Pass |
| Clock Out | all three pages and every log page | Pass |
| Night Home, Outings, Deals, Relationships | desktop, landscape, 200% text | Pass |
| Weekend and Casino | lobby, buy-ins, Poker, Slots, Blackjack | Pass |
| Cash Jar and Galactic | route, story, result, Galactic event | Pass |
| Promotion, Automation, game over | desktop, landscape, 200% text | Pass |
| Portrait | rotation gate | Pass |

Focused verifier:

- `.officewars-no-scroll-verify.py`
- SHA-256:
  `A3C9B7C204A32D57FCD7D4A440AFE187C98FC048B36086B9A271D224A4A07243`
- result: `NO_SCROLL_PASS`, 354/354 surface checks

## Regression Evidence

| Suite | Result |
|---|---|
| `.officewars-visual-capture.py --quiet` | Pass |
| `.officewars-full-verify.py 0` | Pass |
| Phase 1 | Pass 25/25 |
| Phase 2 | Pass 20/20 |
| Phase 3 | Pass 21/21 |
| Phase 4 | Pass 18/18 |
| Phase 5 | Pass 21/21 |
| Guided Intern | Pass 37/37 |
| Persistence | Pass 30/30 |
| Cinematic Workday | Pass 32/32 |
| Home Schedule | Pass |
| Night Planner | Pass |
| Advanced interaction chains | Pass |
| Cash Jar release | Pass 10/10 |
| Cash Jar inventory | Pass 6/6, 96/96 handlers |
| Casino scene | Pass |
| Smoke | Pass |
| Agent guidance/public mirror equality | Fail: root `AGENTS.md` differs from the intentionally unsynchronized public mirror |

Material updated verifier hashes:

- visual capture:
  `CD4B17B46689E544B51D105C72ABE12C5B77481EC0F387EE4BB99A81A7941422`
- Phase 3:
  `189410BC3BDBA351A8C7A8571D76F10A999038509777A44F5315B29F5A0A1A37`
- Phase 5:
  `72EE24BBA928EECEA70EC17E683B3A7DDD06ED36B42CD079416671E9933B4878`
- Guided Intern:
  `F234C9B0E44052A9332E6A076CF8D074BA02C870259A9F65DE2521665C0FD9AE`

## Requirement Status

| Requirement | Status |
|---|---|
| No visible scrollbars on supported surfaces | Pass |
| No clipped required controls or information | Pass in automated matrix |
| Keyboard-operable page controls and modal focus | Pass |
| Reduced motion | Pass |
| 200-percent text | Pass |
| Portrait rotation gate | Pass |
| 1x/2x/4x, Skip, reload, and headless parity | Pass in Guided/Cinematic/Persistence suites |
| Formal screen-reader execution | Not Run |
| Broad current-hash human playtest | Not Run |
| Public mirror synchronization | Not Run; explicitly out of scope |
| Release ZIP | Not Run; not requested |

## Preserved Boundaries

- Cash Jar remains gated and unobtainable in ordinary play.
- Schema 10 remains inactive.
- Canonical status is not changed to a public Implemented release.
- Galactic Investment and Galactic Gambler are unchanged.
- The public mirror remains on `360CC6C0...`.
- No release ZIP was built.

## Readiness

The no-scrollbar implementation is ready for human review. The overall Cash
Jar/public release remains Not Ready for the previously documented balance,
activation, and distribution reasons; none are caused by this UI pass.
