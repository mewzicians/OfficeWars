# Home And Manager Visual Pass Verification

Date: 2026-08-10

Game SHA-256:
`DD5BFD100A3E4B270587F62346DF7AF456484DF6AB7DA72A5C4EBBE13BA98488`

| Artifact | SHA-256 |
|---|---|
| `.officewars-smoke-run.py` | `ADD032E1CC13C4715D8A9C58321684DC16E3981634DC63ECF138FD2B422E6A3C` |
| `.officewars-home-schedule-verify.py` | `EA9E2BAF7A61C7E015652C7BE760D932D3EAD02F5B46928484C9CE49C7159E2B` |
| `.officewars-persistence-verify.py` | `88BC1A7D906A4A56CE1EA67E77C88925265C048F1E94A765A729170EE97D73DB` |
| `.officewars-advanced-verify.py` | `DC32B71569A9377F77B3A800D4CB0BDAAAD94C8D67BC7A79273D8483360699F2` |
| `.officewars-visual-capture.py` | `E94C43B0B61AF8D18D18A5ADCD1BB2A453ED0DEAA40E56A544C5C216F6BFF718` |
| `.officewars-full-verify.py` | `816D35CBE01639747776A9B10923B7B5A2B670D86A15807BDF6146FACB622EC1` |

## Results

| Requirement | Status | Evidence |
|---|---|---|
| Four-tier Home geometry | **Pass** | Apartment, Townhouse, House, and Penthouse each render exact 3/6/9/12 slots at desktop and landscape-phone sizes |
| Grounded room objects | **Pass** | PC, phone table, Deal table, bed, door, and every item slot remain in the room floor region |
| Bed readability | **Pass** | Bed is at least 2.4 times the phone control width and includes a frame, mattress, pillow, blanket, and legs |
| Home Shop PC | **Pass** | Monitor, neck, base, tower, keyboard, and mouse are present at both tested viewports |
| Relationships phone | **Pass** | Phone control is visible, the old book control is absent, and the orientation targets the phone |
| Window moon | **Pass** | Moon bounds remain fully inside the room-window bounds for all eight Home fixtures |
| Home title and Stress | **Pass** | Lower-left title is the Home name only; the top Stress bar matches the tested 42 percent state |
| Lights Out presentation | **Pass** | Switch activates, room dimming opacity exceeds 0.5, purchases lock normally, and controls remain visible |
| Curved celestial paths | **Pass** | Sunset sun, sunset moon, sunrise sun, and sunrise moon each use five-stage arc keyframes |
| Manager variants | **Pass** | All eight managers render distinct portrait glyphs and colors with accessible names |
| Ordinary-floor manager | **Pass** | Current manager is seated behind the manager desk and no patrol sprite exists |
| Boss-floor manager | **Pass** | Seated portrait hides, visible patrol uses `manager-office-patrol`, and `CAST` contains no manager member |
| Deterministic gameplay | **Pass** | Smoke and advanced suites pass; manager presentation does not consume gameplay state or RNG |
| Persistence and tutorial | **Pass** | All 24 persistence, casino, and thirteen-step orientation checks pass |
| Responsive visual matrix | **Pass** | Full readability matrix passes with no sampled clipping, viewport overflow, or persistent-HUD overlap |
| Full automated audit | **Pass** | Current no-simulation full verifier reports every executed check passing |
| Structural balance simulation | **Not Run** | This pass changes presentation only and has no approved numeric balance changes |

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
