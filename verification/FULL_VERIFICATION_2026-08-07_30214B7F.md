# OfficeWars Full Verification

Date: 2026-08-07

Implemented file: `officewarsautobattler.html`

Game SHA-256:
`30214B7FFF8FB4ED44690B90B64EE991E8F300ACE1A4E66E9100BBDAFCC81D12`

Overall result: **FAIL - player candidate passes, headless simulation parity
does not**

The player-facing game passes the current static, runtime, deterministic,
persistence, advanced-interaction, readability, sampled accessibility, and
distribution checks. Final signoff fails because automated Night resolution
breaks a Locked player rule: after buying a Home item, the skilled headless
policy also grants itself manual Lights Out.

## Verification Artifacts

| Artifact | SHA-256 |
|---|---|
| `.officewars-smoke.html` | `5DC59958D20B3A90FE71F4F5E3E840F3BEA941658E94798849474C9DF72E2644` |
| `.officewars-smoke-run.py` | `ADD032E1CC13C4715D8A9C58321684DC16E3981634DC63ECF138FD2B422E6A3C` |
| `.officewars-persistence-verify.py` | `7A3A7642DC6C7818DD34E9418DEF46659B36700D12D03DFD10EEECE65F398976` |
| `.officewars-advanced-verify.py` | `6A71969B1C6B562E6F462922BF13A745919874161BEDF17462B84C930AEC2295` |
| `.officewars-full-verify.py` | `2B44B8FB5C0FE9D9EF987114DCA87108B7CF682F80C464E6E0350FF7E30ADAA3` |
| `.officewars-visual-capture.py` | `03A0195D63DD1DC7C35D9D54DEB68BB913A371CCD9B045D65BB723E0A2EF466E` |
| `.officewars-skilled-telemetry.py` | `62378F333A4E783BB52DE6011DAF64F8F6FDCA2FD3267CEC680A82C8BBCCD8C2` |

## Requirement Matrix

| Requirement group | Status | Evidence |
|---|---|---|
| Standalone HTML, runtime load, IDs, and external dependencies | **Pass** | Full verifier; no page, console, or external-request errors |
| Core constants, managers, meetings, seven-floor curve, and Chad cap | **Pass** | Exact-value and deterministic runtime assertions |
| 50-card roster and 4/3/2/1 distribution in every family | **Pass** | 50 unique IDs and exact family counts |
| Ordinary rarity, Special generation, Campaign shape, and Sales Cycle shape | **Pass** | Generator and data-table assertions |
| All 50 cards: preview, markup, and primary Complete Play | **Pass** | Zero preview, markup, or play failures |
| All 50 cards: every delayed edge and UI expiration | **Not Run** | Basic and targeted coverage passed; exhaustive per-card lifecycle traversal did not run |
| Shared card, Replay, copy, Assist, and resolution rules | **Pass** | Smoke and advanced worst-case fixtures |
| Schedule, action, Clock Out, and transition ordering | **Pass** | Advanced schedule and economy groups |
| Coworker Standard and Forced activation ordering | **Pass** | Advanced coworker and repeated-meeting groups |
| All 14 ordinary trait paths | **Pass** | Advanced targeted timing group |
| Closing, Brand Strategy, Deals, Schmoozing, and Logistics | **Pass** | Advanced lifecycle group |
| Promotion batches and single-capstone ownership | **Pass** | Simultaneous-candidate fixtures |
| Deterministic 1x, 2x, 4x, and Skip playback | **Pass** | Current smoke suite |
| Active-run persistence, casino restoration, and orientation | **Pass** | 23 focused checks |
| Player Night purchase and Lights Out mutual exclusion | **Pass** | Both directions plus Moodboard exception |
| Headless Night policy uses player-legal choices | **Fail** | It recorded `homeUsed=1`, `lightsOut=true`, `exception=false` |
| Current balance simulation | **Blocked** | The policy failure gives automated runs illegal recovery |
| 17-case readability and responsive matrix | **Pass** | No sampled clipping, viewport overflow, or persistent-HUD overlap |
| Campaign Morning, Resume, Clock Out, and Night decision surfaces | **Pass** | Runtime assertions and current screenshots |
| Basic semantic names, focus return, and keyboard tooltip access | **Pass** | Full verifier sampled surfaces |
| Every modal and picker focus cycle | **Not Run** | Representative surfaces passed; every advanced picker was not traversed |
| Color independence and formal contrast in every state | **Not Run** | Human visual inspection only |
| Dynamic screen-reader announcements | **Blocked** | No screen-reader execution environment |
| Complete keyboard-only run | **Not Run** | Sampled controls passed |
| Every advanced decision surface at every viewport | **Not Run** | Ordinary phases and representative exceptional states passed |
| Save/restore at every phase and picker boundary | **Not Run** | Focused 23-check suite passed; exhaustive matrix did not run |
| New-run cleanup after every ending | **Not Run** | Result and replacement paths passed; all timer/listener combinations were not profiled |
| Rapid-input fuzzing for every control | **Not Run** | Repeated Skip and resolution locks passed |
| Worst-case chain termination | **Pass** | 16-play replay, 15-play storage, and 121-action fixtures terminate |
| Worst-case memory growth | **Not Run** | Termination passed; heap growth was not profiled |
| Active docs, references, UTF-8, and archive boundaries | **Pass** | QA cleanup and local reference audit |
| Public and rollout package integrity | **Pass** | Post-cleanup byte equality, local links, and ZIP inventory |
| Human balance evidence | **Not Run** | Human playtesting remains pending |
| Deferred Home set design | **Not Run** | Intentionally outside this candidate; metadata remains inert |

## Failed Check

The player UI uses `owLightsOutBlocksNightPurchases()` and
`owNightPurchasesBlockLightsOut()` correctly. The headless policy instead ends
with an unconditional `nightState.recPicked=true` after automated purchases.
The new verifier reproduced:

```text
purchaseUsed=true
homeUsed=1
dealUsed=0
lightsOut=true
exception=false
finalStress=31
```

This is not a player-facing Night defect. It is a simulation-model defect and
invalidates current win-rate evidence. The historical 58.4 percent
scripted-skilled result remains evidence only for its exact prior snapshot.

## Automated Results

- Smoke: **Pass**
- Persistence and orientation: **Pass**, 23 of 23 checks
- Advanced interactions: **Pass**, 8 of 8 groups
- Full runtime and surface audit: **Fail**, one headless-policy check
- Readability visual matrix: **Pass**, 17 of 17 cases
- Current balance batch: **Blocked**, deliberately not run

The advanced maximal fixture remains a tuning watchpoint: 121 action
resolutions produced 2,403 project progress while terminating correctly.

## Ship Decision

- **Player-facing relationship, Night, Campaign, readability, persistence, and
  playback update:** Pass.
- **Current implementation-verification candidate:** Fail until the headless
  Night policy follows player-legal choices.
- **Final balance release:** Blocked until a rules-faithful fixed-seed matrix is
  rerun and interpreted against the 25-35 percent target.
- **Exhaustive certification:** Incomplete. Every Not Run and Blocked row above
  remains explicitly unverified.

Gameplay code was not changed during this verification-only pass.
