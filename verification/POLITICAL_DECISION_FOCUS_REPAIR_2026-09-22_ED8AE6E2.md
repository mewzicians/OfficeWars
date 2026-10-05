# Political Decision Focus Repair

Date: 2026-09-22

Candidate:

- SHA-256:
  `ED8AE6E2F8620A8567D8FDEEEE74A8130A5865E884B2352497770F1B20BDDEEF`
- size: `1,685,721` bytes
- active-run schema: 9
- Cash Jar target schema: 10, inactive
- Cash Jar public gate: disabled

## Reproduced Defect

During a live Guided project decision, the political choice pane competed with
four fixed surfaces:

- the large day ticker;
- the open Action Guide;
- playback controls; and
- the floating current-action cinematic pip beneath the top-left HUD.

The full Guided Coordinator dock added a fifth attention surface. Required
choices remained operable but were visually obscured and lacked exclusive
decision ownership.

## Repair

- Every live or restored political choice enters a shared
  `ow-political-decision-focus` presentation state.
- Entering focus closes the Action Guide and hides the ticker, guide, playback
  controls, and floating cinematic pip.
- The saved event anchor now supplies an inline breadcrumb such as
  `WORKDAY CONTEXT · BEFORE WORK`; unattached events fall back to
  `WORKDAY CONTEXT · OFFICE POLITICS`.
- Committing, interrupting, or closing the cinematic stage exits focus and
  restores the correct watched or Skip presentation. The Action Guide stays
  closed until manually reopened.
- Guided project choices hide the full Coordinator dock and render a compact
  accessible Coordinator strip inside the decision pane.
- Inline Guided feedback and Show Me use the existing lesson and target
  authorities. Wrong choices and Show Me remain state- and RNG-inert.
- The normal dock is restored immediately after the political choice closes.
- No new saved fields or schema changes were added; focus state is derived
  entirely from the active event.

## Focused Evidence

| Requirement | Result |
|---|---|
| Screenshot-state reproduction with Guide previously open | Pass |
| Ticker, Guide, controls, and pip hidden during choice | Pass |
| Inline context matches saved action and anchor | Pass |
| Ordinary desktop/short-landscape/200% text | Pass |
| Guided inline instruction and unique accessible labels | Pass |
| Guided desktop/short-landscape/200% text/reduced motion | Pass |
| Wrong choice updates inline feedback without commitment | Pass |
| Show Me focuses the required option without state/RNG mutation | Pass |
| Correct choice restores ticker/dock and leaves Guide closed | Pass |
| `workdayPoliticalChoice` reload | Pass |
| `workdayPoliticalQueue` reload/Skip continuation | Pass |
| Watched 1x/2x/4x, Skip, and partial-Skip parity | Pass |
| Collision and overflow scan | Pass |

Focused verifier hashes:

- cinematic Workday:
  `D97F2C608B9229D0471ACE8E11C23BB55BA1636479D9B0C65343FCDA97D1B04B`
- Guided Intern:
  `2818DB2E4493900CAD2CA285CC4BAAC079250AE600DAEF24B8C8F4BFF34CC80C`
- no-scroll/collision:
  `0A94830B6DACBE82850AB0AE19669665669ECE5E061516D86DF701E13E75A9B8`

## Regression Results

| Suite | Result |
|---|---|
| Guided Intern | Pass 40/40 |
| Cinematic Workday | Pass 33/33 |
| No-scroll/collision matrix | Pass 354/354 |
| Broad visual-capture matrix | Pass |
| Persistence | Pass 30/30 |
| Advanced interaction chains | Pass |
| Full audit | Pass |
| Smoke | Pass |

## Preserved Boundaries

- Gameplay values, resolution order, and RNG consumption are unchanged.
- Political decisions remain irreversible, untimed, and without Back/defer.
- Cash Jar remains gated.
- Schema 10 remains inactive.
- Galactic Investment and Galactic Gambler are unchanged.
- The public mirror remains on `360CC6C0...`.
- No release ZIP was built.

## Verdict

The political decision focus repair is implemented and ready for human review.
Formal screen-reader execution and broad human playtesting remain outside this
automated repair evidence.
