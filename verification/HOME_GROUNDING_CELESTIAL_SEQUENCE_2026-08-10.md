# Home Grounding And Celestial Sequence Verification

Date: 2026-08-10

Game SHA-256:
`470F4146FBA177FD6B7062A0093DDCF7C2826B797FE9AE74317BD1D146050FF7`

| Artifact | SHA-256 |
|---|---|
| `.officewars-smoke-run.py` | `ADD032E1CC13C4715D8A9C58321684DC16E3981634DC63ECF138FD2B422E6A3C` |
| `.officewars-home-schedule-verify.py` | `331116736A5117C365A54847976DCA2F61111191BD71988166ED05FB5917CCE6` |
| `.officewars-persistence-verify.py` | `88BC1A7D906A4A56CE1EA67E77C88925265C048F1E94A765A729170EE97D73DB` |
| `.officewars-advanced-verify.py` | `DC32B71569A9377F77B3A800D4CB0BDAAAD94C8D67BC7A79273D8483360699F2` |
| `.officewars-visual-capture.py` | `E94C43B0B61AF8D18D18A5ADCD1BB2A453ED0DEAA40E56A544C5C216F6BFF718` |
| `.officewars-full-verify.py` | `816D35CBE01639747776A9B10923B7B5A2B670D86A15807BDF6146FACB622EC1` |

## Results

| Requirement | Status | Evidence |
|---|---|---|
| Four-tier room composition | **Pass** | Apartment, Townhouse, House, and Penthouse retain the same left-to-right interactive layout |
| Shallow floor plane | **Pass** | Every furniture control and the plant meet the measured 90-percent room-height floor boundary at desktop and landscape sizes |
| Furniture readability | **Pass** | Furniture bodies remain above the baseboard; feet extend into the shallow floor strip instead of the objects appearing embedded |
| Home-name placement | **Pass** | The Home name remains inside the room below the shared furniture boundary |
| Wall storage and moon | **Pass** | Exact 3/6/9/12 slot counts stay on the wall and the moon remains inside the window |
| Responsive geometry | **Pass** | All four tiers pass at 1440x900 and 844x390 with no viewport overflow |
| Shared celestial path | **Pass** | All four five-stage keyframes use identical full-width east-to-west transforms |
| Sunset sequence | **Pass** | Sun and moon use equal duration and linear timing; the sun's negative delay keeps it ahead |
| Sunrise sequence | **Pass** | Moon and sun use equal duration and linear timing; the moon's negative delay keeps it ahead |
| Deterministic gameplay | **Pass** | Smoke and all eight advanced interaction groups pass on the named hash |
| Persistence and tutorial | **Pass** | All 24 persistence, casino, and orientation checks pass |
| Readability matrix | **Pass** | The complete visual matrix passes without sampled clipping, persistent-HUD overlap, or viewport overflow |
| Full automated audit | **Pass** | The no-simulation full verifier reports every executed check passing |
| Structural balance simulation | **Not Run** | This presentation-only pass changes no gameplay values or resolution behavior |

## Commands

```powershell
python .officewars-home-schedule-verify.py
python .officewars-smoke-run.py
python .officewars-persistence-verify.py
python .officewars-advanced-verify.py
python .officewars-visual-capture.py --quiet
python .officewars-full-verify.py 0
```

All six commands passed on the named game hash.

## Remaining Scope

- Fresh structural balance simulation is **Not Run**.
- Formal screen-reader execution, exhaustive every-picker traversal,
  exhaustive save-boundary traversal, rapid-input fuzzing, and long-session
  memory profiling retain the statuses from the preceding exhaustive report.
- Home set definitions and Home-tier item restrictions remain deferred design
  work.
