# Home Side-View And Celestial Arcs Verification

Date: 2026-08-10

Game SHA-256:
`C68FF6FF42BFC19DB334BD72F1A13C1DABA6196C76E7E347BB7AB11E50ABBA5B`

| Artifact | SHA-256 |
|---|---|
| `.officewars-smoke-run.py` | `ADD032E1CC13C4715D8A9C58321684DC16E3981634DC63ECF138FD2B422E6A3C` |
| `.officewars-home-schedule-verify.py` | `BF03A9BA61F6814C9771738D0EAD0D8012C34388363FDDF0938FD93D4FE2E527` |
| `.officewars-persistence-verify.py` | `88BC1A7D906A4A56CE1EA67E77C88925265C048F1E94A765A729170EE97D73DB` |
| `.officewars-advanced-verify.py` | `DC32B71569A9377F77B3A800D4CB0BDAAAD94C8D67BC7A79273D8483360699F2` |
| `.officewars-visual-capture.py` | `E94C43B0B61AF8D18D18A5ADCD1BB2A453ED0DEAA40E56A544C5C216F6BFF718` |
| `.officewars-full-verify.py` | `816D35CBE01639747776A9B10923B7B5A2B670D86A15807BDF6146FACB622EC1` |

## Results

| Requirement | Status | Evidence |
|---|---|---|
| Four-tier side-view layout | **Pass** | Apartment, Townhouse, House, and Penthouse render the bed, phone, PC, Deal desk, and door in the same left-to-right order |
| Shared floor line | **Pass** | Every interactive furniture control ends within eight percent of the room floor across desktop and landscape fixtures |
| Wall storage | **Pass** | Exact 3/6/9/12 slot counts stay above the floor line and within the wall region |
| Responsive geometry | **Pass** | All four tiers pass at 1440x900 and 844x390 with no viewport overflow |
| Bed readability | **Pass** | The bed remains larger than the bedside phone and includes its headboard, frame, mattress, pillow, blanket, and legs |
| PC, phone, and Deal desk | **Pass** | The full PC assembly, phone table, and laptop table remain distinct and selectable |
| Window moon | **Pass** | Moon bounds stay fully inside the window in every tested Home fixture |
| Lights Out | **Pass** | The switch remains selectable and room dimming preserves readable controls |
| Full-width sunset arcs | **Pass** | Sun travels left-to-right and moon right-to-left using five keyframe stages and 100-viewport-width endpoints |
| Full-width sunrise arcs | **Pass** | Sun travels right-to-left and moon left-to-right using five keyframe stages and 100-viewport-width endpoints |
| Deterministic gameplay | **Pass** | Smoke and all eight advanced interaction groups pass on the named hash |
| Persistence and tutorial | **Pass** | All 24 persistence, casino, and orientation checks pass |
| Readability matrix | **Pass** | Desktop, compact, landscape, Night, and 200-percent text samples pass without sampled clipping or persistent-HUD overlap |
| Full automated audit | **Pass** | The current no-simulation full verifier reports every executed check passing |
| Structural balance simulation | **Not Run** | This pass changes presentation only and contains no approved numeric balance changes |

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
