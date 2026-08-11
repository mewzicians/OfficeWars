# Full Verification 2026-08-10 — F51F2F7C

Candidate SHA-256:
`F51F2F7C7A11098FA7DABF5692767D14D14B75F45AFA9CADC6EB3DA96A141A46`

Hashes in this project are taken over LF content, matching the repository blob
and the public package. A CRLF working copy of the same file produces a
different value. See Finding V1.

Scope: verification and QA-consistency pass following the Home room art redesign
and the celestial opposing-arc change. This report supersedes no earlier report;
previous dated reports remain exact evidence for their own named hashes.

## Environment Constraint

No Python interpreter is installed on the machine used for this pass, and
installing one was declined. Every shipped runner under `.officewars-*.py`
requires Python and Playwright and therefore **could not be executed**.

Rows that depend on those runners are recorded as `Blocked`, not as passing and
not as failing. Where a requirement could be exercised independently, it was
verified with Node 22 driving headless Chrome over the DevTools Protocol, and
the row records that method explicitly.

Test artifacts (SHA-256, first 16 hex):

| Harness | Hash | Purpose |
|---|---|---|
| `audit.js` | `31e1450a9ec50480` | structural invariants read from loaded tables |
| `surfaces.js` | `f5bded120703fac9` | player-surface sweep, overflow, names, errors |
| `homeshot.js` | `e8dddc8d73785c49` | Home room geometry contract, four tiers |
| `arcs.js` | `9cd395fcd4092041` | celestial separation sampling |
| `verifyarcs.js` | `19fed4ef87c7d8fd` | replicates the shipped suite's arc assertions |

## Requirement Matrix

### Static and structural

| Requirement | Status | Evidence |
|---|---|---|
| JavaScript syntax valid | Pass | single inline script parsed with `node:vm`, 0 errors |
| Stylesheet braces balanced | Pass | brace depth 0 |
| Standalone load, ready flag set | Pass | `data-officewarsReady === 'true'` |
| Required element IDs present | Pass | `overlay`, `run-hud`, `home-scene`, `phase-transition` |
| No external dependencies | Pass | 0 non-`file:`/`data:` network requests observed |
| 50 ordinary cards, 10 per Skill | Pass | read from `TASKS` |
| Rarity split 4/3/2/1 per Skill | Pass | verified for all five Skills |
| No duplicate task IDs | Pass | 0 duplicates across 50 IDs |
| Special pool | Pass | `rebrandInitiative` only |
| Homes 3/6/9/12 slots | Pass | read from `HOMES` |
| Managers / cast / floors | Pass | 8 / 8 / 7 |
| Floor curve | Pass | `110/10, 130/8, 165/7, 210/6, 250/6, 285/6, 300/5` |
| Brand campaigns present | Pass | 4 |
| Meeting dialogue bank self-check | Pass | `MEETING_DIALOGUE_ISSUES` empty |

### UI, readability, responsive

| Requirement | Status | Evidence |
|---|---|---|
| No page or console errors | Pass | menu, Morning, Resume Book, Night at 3 viewports |
| No horizontal overflow | Pass | 12 surface × viewport combinations |
| No interactive element off-viewport | Pass | 12 combinations, 0 offenders |
| Every interactive element has an accessible name | Pass | 12 combinations, 0 unnamed |
| Home room geometry, four tiers | Pass | desktop and landscape; see below |
| Reduced motion bypasses transitions | Pass | layer never activates, Home scene entered directly |
| Formal screen-reader certification | Not Run | no assistive-technology environment exercised |
| Text zoom to 200 percent | Not Run | not sampled in this pass |
| Portrait rotation gate | Not Run | not sampled in this pass |

Home room geometry, all four tiers at 1440x900 and 844x390: floor line at 10
percent of room height, every measured piece (bed, phone table, Home Shop desk,
Deal desk, door, plant) grounded within **0.01px** of that line, item slots above
the 86.5 percent wall boundary, left-to-right order bed → phone → shop → deals →
door, moon inside the window, Home name below the furniture, and no element
outside the viewport.

### Phase transitions

| Requirement | Status | Evidence |
|---|---|---|
| Sun and moon never share a stretch of sky | Pass | min separation 48.1% (sunset), 48.0% (sunrise) of viewport width across 11 samples each |
| Arc halves cut from one path | Pass | `ascend[-1] == descend[0]` = `translate(50vw, -46vh)` |
| No delay-offset chase | Pass | all four animation delays `0s` |
| Bodies run opposite halves, swapped per transition | Pass | sunset sun=descend/moon=ascend; sunrise reversed |
| Transition moon never renders a fully masked disc | Pass | day-0 true phase `phase-new` resolves to `phase-crescent` in transitions; Home window keeps `phase-new` |

### Determinism, persistence, behaviour, simulation

| Requirement | Status | Reason |
|---|---|---|
| 1x/2x/4x/Skip state and RNG equality | Blocked | requires `.officewars-smoke-run.py` |
| 24-check persistence suite | Blocked | requires `.officewars-persistence-verify.py` |
| Eight advanced interaction groups | Blocked | requires `.officewars-advanced-verify.py` |
| Full automated runtime audit | Blocked | requires `.officewars-full-verify.py` |
| Home/schedule contract suite | Blocked | requires `.officewars-home-schedule-verify.py` |
| Per-card behaviour, Replay, copy, Assist traversal | Blocked | same runners |
| Save corruption and every-boundary restore | Blocked | same runners |
| Structural simulation and all balance measurement | Blocked | same runners; also gated behind policy-parity proof |
| Exhaustive per-picker traversal, rapid-input fuzzing, memory profiling | Not Run | outside this pass, as in the preceding report |

### Distribution and release

| Requirement | Status | Reason |
|---|---|---|
| Root-to-rollout mirror equality | Blocked | `officewars-rollout-handoff-2026-07-31/` is not present in this clone |
| Root-to-public mirror equality | Not Applicable | this repository *is* the public mirror |
| Public ZIP rebuild and byte equality | Blocked | canonical builder `build_public_zip.py` requires Python |
| Active Markdown links resolve | Pass | 0 broken relative links |
| Valid UTF-8, no trailing whitespace | Pass | 0 offenders across tracked Markdown |

## Findings

**V1 — Documented hashes were computed over CRLF, not LF. Fixed.**
The two patch notes added earlier today recorded `286D494D…` and `1735BF27…`,
which are `sha256sum` values of a CRLF working copy. The project convention is
LF content: the ledger's prototype hash `1E4D168C…` matches the LF blob exactly,
and the previous candidate's documented `470F4146…` matches the LF blob at
commit `24cc761`. Both patch notes were corrected to their LF values
(`2105696E…` and `F51F2F7C…`), and `PROJECT_STATUS.md`, `HANDOFF.md`, and
`BALANCE_LEDGER.md` now state the convention explicitly so it cannot recur.

**V2 — Active status documents claimed a superseded hash. Fixed.**
`PROJECT_STATUS.md`, `HANDOFF.md`, and `BALANCE_LEDGER.md` still presented
`470F4146…` as the implemented hash and carried its suite results as current.
All three now name `F51F2F7C…`, and the verification sections separate what was
verified on this hash from what is Blocked and from historical evidence that
does not transfer.

**V3 — Verification checklist is entirely unchecked.** `VERIFICATION_CHECKLIST.md`
holds 182 unchecked items and 0 checked. This is by design: the handoff states
that the checklist is a requirement inventory and that unchecked boxes must not
be read as passes. No change made.

**V4 — Dangling references, left unresolved deliberately.**
`.agents/skills/officewars-plan/SKILL.md` refers to `/docs/…` and
`/verification/…` with a leading slash, which does not resolve from the
repository root. `docs/ARCHIVE_SUPERSEDED.md` refers to `archive/*.md`, and two
historical reports refer to `START_HERE.md`; neither target ships in the public
package, which `SNAPSHOT_PROVENANCE.md` documents as an intentional exclusion.
These were **not** edited here because the skill and archive files are mirrored
from the source workspace, and repairing them only in the mirror would let the
mirror diverge from its source. They belong to the source workspace.

**V5 — No new gameplay defect found.** No page errors, console errors, external
requests, layout overflow, or unnamed interactive controls were observed on any
sampled surface.

## Ship Decision

- **Player-facing readiness:** Pass on everything sampled. The Home room and
  both transitions are visually coherent and correctly grounded, and no sampled
  surface produced an error, overflow, or unnamed control.
- **Implementation readiness:** Not established on this hash. The static,
  structural, and surface layers pass, but every determinism, persistence, and
  behavioural suite is Blocked. Absence of evidence here is not evidence of
  correctness.
- **Balance readiness:** Unchanged and still open. No simulation ran. The
  historical 58.4 percent scripted-skilled result predates the corrected Night
  policy and remains invalid as current evidence.
- **Exact next blocker:** install Python and Playwright, then rerun the five
  shipped runners against `F51F2F7C` to convert the Blocked rows. Until that
  happens this candidate must not be described as verified, and no balance
  conclusion may be drawn.
