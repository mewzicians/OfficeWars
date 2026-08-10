# Home, Schedule, And Tutorial Verification

Date: 2026-08-10

Game SHA-256:
`0A8F74E5A47EDE063FE6100B053998601AD0B8D8BC4C521E644C3BE5BA9AB0AE`

| Artifact | SHA-256 |
|---|---|
| `.officewars-smoke-run.py` | `ADD032E1CC13C4715D8A9C58321684DC16E3981634DC63ECF138FD2B422E6A3C` |
| `.officewars-home-schedule-verify.py` | `434566D60267BB07FF5B3BCC3D564FB8738F5AB2E3BC15205596FD89A01C7B8E` |
| `.officewars-persistence-verify.py` | `A9BA5FB90485D24FB9AC8D37050B7F7DD079205BD8A96366784E909E023DAED3` |
| `.officewars-advanced-verify.py` | `DC32B71569A9377F77B3A800D4CB0BDAAAD94C8D67BC7A79273D8483360699F2` |
| `.officewars-visual-capture.py` | `2287BB319FDC91BAE8907B72F160B74024985A3AD1FA24E4D5F6115B7E93EEE8` |
| `.officewars-full-verify.py` | `BAAF0B81040C3A5EF01BF5F05F1420D54D1C6224CE007792E2B2016428755D00` |

## Results

| Requirement | Status | Evidence |
|---|---|---|
| Shared schedule language | **Pass** | Prototype Test, Schedule Adjustment, Leadership, guarantees, and Schedule Desk use action-icon timelines with source states and highlighted differences |
| Schedule comparison layout | **Pass** | Desktop and landscape fixtures show two stacked five-entry schedules, six highlighted differences, and no horizontal overflow |
| Dedicated Home scene | **Pass** | Night hides the office HUD and exposes Home Shop, Relationships, Outings, unlocked Deals, Lights Out, End Day, and item slots through room objects |
| Home status readability | **Pass** | Cash, Expense Credit, current Stress, and projected post-sleep Stress remain visible at desktop and landscape-phone sizes |
| Home inventory interaction | **Pass** | Occupied slots expose their item effect and an accessible sale confirmation; empty capacity remains visible |
| Lights Out policy | **Pass** | Manual Lights Out locks Home and Deal purchases; a purchase blocks automatic Lights Out unless an explicit exception applies |
| Home transitions | **Pass** | Sunset, door opening, Outing fade and return, and sunrise are implemented with reduced-motion and automated bypasses |
| Exactly-once Night restore | **Pass** | Restoring `nightResolved` advances to Morning with the settled Stress value and does not repeat recovery |
| Thirteen-step orientation | **Pass** | Persistence fixture traverses all thirteen named steps and confirms Home targets, boss-floor timing, and the Capstone finish |
| Workday action tutorial | **Pass** | The first Workday tutorial opens the live Action Guide and names all six ordinary actions without starting playback |
| Persistence and casino restoration | **Pass** | All 24 focused save, continuation, tutorial, and casino checks pass |
| High-risk interactions | **Pass** | All eight advanced groups pass, including schedule ordering, Night policy, promotion, traits, and worst-case chains |
| Responsive visual matrix | **Pass** | Thirty-eight desktop, compact, landscape, portrait, exceptional-mode, Home, tutorial, and 200-percent-text cases pass without sampled clipping or viewport overflow |
| Browser integrity | **Pass** | Focused and broad runners report no page errors, console errors, or required external requests |
| Structural balance telemetry | **Not Run** | This release changes presentation, onboarding, and transition persistence rather than approved balance values |

## Commands

```powershell
python .officewars-smoke-run.py
python .officewars-home-schedule-verify.py
python .officewars-persistence-verify.py
python .officewars-advanced-verify.py
python .officewars-visual-capture.py --quiet
python .officewars-full-verify.py 0
```

All six commands passed on the named game hash.

## Remaining Scope

- Fresh structural balance simulation is **Not Run**.
- Exhaustive screen-reader testing, every task picker, every save/restore
  boundary, reset stress, rapid-input fuzzing, and long-session memory
  profiling retain the statuses recorded in the preceding exhaustive report.
- Home-set definitions and Home-tier item restrictions remain deferred design
  work, not missing implementation from this patch.
