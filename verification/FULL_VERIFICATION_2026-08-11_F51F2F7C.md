# Full Verification 2026-08-11 - F51F2F7C

Candidate SHA-256:
`F51F2F7C7A11098FA7DABF5692767D14D14B75F45AFA9CADC6EB3DA96A141A46`

Scope: local verification after synchronizing GitHub commit
`040b9277e58373abf85a6a0768d350831c55aedc` into the source workspace.
Hashes use LF content, matching the repository blob and public package.

## Environment

- Windows PowerShell workspace
- Python 3.13 with the project Playwright environment
- Standalone `file:` launch; no server or build step
- Desktop, compact desktop, landscape phone, portrait rotation, reduced
  motion, and 200-percent text-scale fixtures

## Test Artifacts

| Runner | SHA-256 |
|---|---|
| `.officewars-home-schedule-verify.py` | `832BB7DD900AE514057FF575C89424E1A825C2274A79A3E6ED17DC4844C3043C` |
| `.officewars-smoke-run.py` | `ADD032E1CC13C4715D8A9C58321684DC16E3981634DC63ECF138FD2B422E6A3C` |
| `.officewars-persistence-verify.py` | `88BC1A7D906A4A56CE1EA67E77C88925265C048F1E94A765A729170EE97D73DB` |
| `.officewars-advanced-verify.py` | `DC32B71569A9377F77B3A800D4CB0BDAAAD94C8D67BC7A79273D8483360699F2` |
| `.officewars-visual-capture.py` | `E94C43B0B61AF8D18D18A5ADCD1BB2A453ED0DEAA40E56A544C5C216F6BFF718` |
| `.officewars-full-verify.py` | `816D35CBE01639747776A9B10923B7B5A2B670D86A15807BDF6146FACB622EC1` |

The Home verifier hash differs from the GitHub import because its new
celestial probe listed four retired keyframe names in the discovery set while
asserting the two current names. The one-line harness repair changed the set to
`ow-arc-ascend` and `ow-arc-descend`. It did not modify the game.

## Automated Results

| Layer | Status | Evidence |
|---|---|---|
| Home and schedule contract | Pass | `PASS:HOME_SCHEDULE` at desktop and landscape |
| Smoke and playback determinism | Pass | `PASS:OVERHAUL` |
| Persistence and tutorial | Pass | 24 of 24 checks, `PASS:PERSISTENCE_AND_TUTORIAL` |
| Advanced interactions | Pass | eight of eight groups, no browser errors or external requests |
| Readability visual matrix | Pass | `PASS:READABILITY_VISUAL_MATRIX` |
| Full no-simulation verifier | Pass | all audit and sampled layout checks true |
| Structural balance simulation | Not Run | intentionally deferred; a fresh rules-faithful run is still required |

## Requirement Matrix

### Static And Structural

| Requirement | Status | Evidence |
|---|---|---|
| JavaScript syntax and standalone load | Pass | full verifier loaded the exact candidate and set the ready flag |
| No required external dependency | Pass | zero external runtime requests |
| Required IDs and unique runtime IDs | Pass | full verifier |
| Floor curve and core constants | Pass | full verifier |
| 50 ordinary cards and 4/3/2/1 rarity split per Skill | Pass | full verifier |
| Card preview, markup, and primary Complete Play | Pass | all 50 cards traversed |
| Special, Campaign, Sales Cycle, Home, Deal, and Closing registries | Pass | full verifier |
| All 14 ordinary paths and hidden Brand Strategy | Pass | advanced path fixtures |

### Behavior And Edge Cases

| Requirement | Status | Evidence |
|---|---|---|
| Shared schedule ordering and conflict resolution | Pass | maximal 27-entry fixture |
| Clock Out economy, debt, Focus, and Guardian Angel order | Pass | advanced fixture |
| Coworker standard and forced activation order | Pass | advanced fixture |
| Repeated meetings and complete-package strength | Pass | advanced fixture |
| Promotion staging, revision, and capstone priority | Pass | advanced fixture |
| Closing, Brand Strategy, Deals, Schmoozing, and Logistics lifecycles | Pass | advanced fixture |
| Replay, copied-effect ancestry, and generated child plays terminate | Pass | advanced worst-case fixtures |
| Maximum sampled action chain terminates | Pass | 121 resolutions and 2,403 progress |
| Lights Out and purchase mutual exclusion | Pass | player and headless paths |
| Home scene, schedule picker, and manager contracts | Pass | focused Home/schedule runner |

The 121-action fixture is a balance and readability watchpoint, not an
implementation failure.

### Determinism And Persistence

| Requirement | Status | Evidence |
|---|---|---|
| 1x, 2x, 4x, and Skip parity | Pass | smoke suite |
| Corrupt and incompatible saves | Pass | persistence suite |
| Morning and prepared-Workday restoration | Pass | identical cards, state, and gameplay RNG |
| Night and `nightResolved` exactly-once restoration | Pass | persistence suite |
| Result, menu, and replacement-run lifecycle | Pass | persistence suite |
| Slots, Blackjack, and Poker continuation | Pass | persistence suite |
| Tutorial completion, skip, and reset persistence | Pass | persistence suite |
| Every picker at every save boundary | Not Run | broader exhaustive matrix remains open |

### UI, Readability, And Accessibility

| Requirement | Status | Evidence |
|---|---|---|
| Desktop, compact desktop, and landscape layouts | Pass | no sampled overflow or clipped text |
| Portrait rotation gate | Pass | visual matrix |
| Reduced motion | Pass | visual and focused transition checks |
| 200-percent text scaling | Pass | visual matrix |
| Home art at all four tiers | Pass | desktop and landscape screenshots visually inspected |
| Home furniture grounding and slot placement | Pass | measured geometry within 0.01px |
| Opposing celestial arc halves | Pass | current keyframes, zero delays, shared apex |
| Accessible names on sampled controls | Pass | full verifier |
| Keyboard and tap tooltips on sampled surfaces | Pass | full and advanced verifiers |
| Formal screen-reader certification | Not Run | no assistive-technology environment exercised |
| Exhaustive keyboard-only traversal | Not Run | sampled controls passed; full traversal remains open |

### Distribution And Documentation

| Requirement | Status | Evidence |
|---|---|---|
| Root active documents match current candidate | Pass | QA cleanup |
| Leading-slash project-skill references | Pass | repaired in source skill |
| Root-to-rollout mapped equality | Pass | synchronized after this report |
| Root-to-public mapped equality | Pass | synchronized after this report |
| Public ZIP inventory and byte equality | Pass | deterministic package builder |
| GitHub historical report preserved | Pass | August 10 blocked report retained unchanged |

## Findings

**V1 - Imported Home verifier had a stale discovery set. Fixed.**
The runner searched for deleted animation names, returned an empty keyframe
map, and failed before checking the current arc rules. The discovery set now
uses the same two names as the assertions. The repaired runner passes on both
viewports.

**V2 - GitHub's blocked runtime rows are now resolved locally.**
Smoke, persistence, advanced interactions, Home/schedule, visual capture, and
the full no-simulation verifier all pass on `F51F2F7C`. The August 10 report
remains valid history for the environment where Python was unavailable.

**V3 - No gameplay defect was found.**
The game file remains byte-identical to GitHub commit `040b9277e583` and keeps
the same candidate hash.

## Open Verification Scope

- fresh structural balance simulation under the corrected Night policy;
- formal screen-reader execution;
- exhaustive every-picker and every-transition save/restore traversal;
- rapid-input fuzzing; and
- long-session memory profiling.

## Ship Decision

- **Player-facing readiness:** Pass for the sampled release surfaces.
- **Implementation readiness:** Pass for the shipped automated suites.
- **Distribution readiness:** Pass after mirror and ZIP verification.
- **Balance readiness:** Not established; the structural simulation rerun is
  still required before making current win-rate claims.
