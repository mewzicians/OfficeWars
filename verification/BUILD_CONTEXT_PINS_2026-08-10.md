# Build Context And Pinned Tasks Verification

Date: 2026-08-10

Game SHA-256:
`2C15A37A71AFA22626B742EF4D88ACC0209DB5AB3FB763ED25549E7050D0CC9C`

Visual-capture runner SHA-256:
`5CFA8D96AF2F10CD720E5F9CC97C62BAFF3FB916C7A71B161DEA3F2F6B77CBB0`

## Results

| Requirement | Status | Evidence |
|---|---|---|
| Targeted effects remain inspectable | **Pass** | A deterministic API Follow-Up fixture visibly names Design in Morning Build Context and exposes its complete timing rule |
| Delegates remain inspectable | **Pass** | Karen and Dave appear by name in Morning Build Context, the active-effect model, and the Resume |
| Contacts remain inspectable | **Pass** | Bob and Priya appear by name; their individual specialties remain available in the Resume |
| Compact pinned-task identity | **Pass** | Two simultaneous pins render only Skill, name, and rarity with no nested full task card |
| Full pinned-task inspection | **Pass** | Activating Version Control opens a standard full task card with two metrics, printed effect, pin source, Select Task, and Back |
| Pinned-task selection | **Pass** | Selecting through the dialog arms the ordinary Morning confirmation with the pin as its source |
| Keyboard modal behavior | **Pass** | Open focuses the close control; Escape closes the dialog and restores focus to the originating pin |
| Milestone tooltip content | **Pass** | Automation's 3, 6, and 10 XP squares expose their exact effects; an unchosen Management path gives the approved unchosen-specialization message |
| Pointer, keyboard, and touch access | **Pass** | Milestone tooltips passed hover, focus, and touch pointer fixtures |
| Resume art visibility | **Pass** | Five decorative scenes compute at 0.86 opacity in the expanded rail, remain pointer-inert, and keep a foreground scrim |
| Desktop layout | **Pass** | 1440x900 keeps three Build Context entries on one row and two compact pins side by side without sampled clipping or overflow |
| Landscape layout | **Pass** | 844x390 keeps Build Context, compact pins, expanded pin dialog, and milestone tooltips usable without sampled viewport overflow |
| 200 percent text | **Pass** | The context and pin fixture grows vertically without horizontal overflow or text overlap; full rules remain available through tooltips |
| Runtime integrity | **Pass** | Smoke, persistence, advanced interactions, and the no-simulation full verifier all passed |
| Structural balance telemetry | **Not Run** | No gameplay values, RNG, or resolution paths changed |

## Commands

```powershell
python .officewars-visual-capture.py --quiet
python .officewars-smoke-run.py
python .officewars-persistence-verify.py
python .officewars-advanced-verify.py
python .officewars-full-verify.py 0
```

## Remaining Scope

The preceding exhaustive report's broader assistive-technology,
every-boundary save/restore, rapid-input, and memory-profile rows retain their
recorded Not Run or Blocked status.
