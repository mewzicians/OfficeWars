# Workday Long-Cycle Discovery Verification

Date: 2026-08-18
Status: Technically verified exploratory endurance comparison; no long-cycle
strategy selected

## Question

Does the selected Hybrid D Workday cue remain strongest as an exact repeating
loop, or does subtle four-loop development improve endurance without making the
Workday demand more attention?

## Controlled Comparison

The source-only lab compares three anonymous `1024-step`, approximately
`4:34.286` supercycles at `112 BPM`.

Every candidate preserves:

- the exact selected `256-step`, approximately `68.571-second` Hybrid D loop;
- Candidate C, Passage D, Ensemble C, and Hybrid B's
  `0 / 0 / 0.55 / 1` motion arc;
- the selected melody, harmony, roots, form, production, and loop seam; and
- an exact first loop.

The exploratory strategies are:

1. Candidate A repeats exact Hybrid D for all four loops.
2. Candidate B adds below-conscious performance drift across loops 2-4:
   restrained organ breathing, slight lead and pocket variation, and a softer
   final reset.
3. Candidate C creates a clearer relationship arc across loops 2-4: organ
   response, rhythm-section response, ensemble reunion, and a prepared reset.

The retained page keeps those mechanisms anonymous until human listening
establishes a preference.

## Verification

Commands:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONPATH="$env:TEMP\officewars-python"
python -B '.officewars-workday-long-cycle-verify.py' --quick
python -B '.officewars-workday-long-cycle-verify.py'
```

Result: `PASS: OfficeWars Workday long-cycle audition`

The verifier proves:

- exact equality with the selected Hybrid D form, Passage D, Ensemble C, and
  production contract;
- all four note plans in every candidate remain exact selected Workday music;
- all three first loops use the exact Hybrid D performance;
- the intended loop 2-4 variation contracts;
- candidate anonymity and zero preselection;
- usable and comparison-safe first-loop output;
- direct Loop 1-4 starts with visible and accessible active-loop state;
- pause, resume, seeking, timestamps, and 48 rapid switches;
- 100-percent headroom;
- desktop, landscape, and portrait layouts;
- two uninterrupted complete supercycles for every candidate; and
- zero active sources after stopping.

Long-run snapshots after two supercycle wraps:

| Candidate | Wraps | Peak sources | Live signal peak |
|---|---:|---:|---:|
| A | 2 | 41 | `0.044581` |
| B | 2 | 41 | `0.079800` |
| C | 2 | 43 | `0.086330` |

No candidate clipped or accumulated sources.

## Artifacts

Audition:

`Music Legacy/officewars-workday-long-cycle-audition.html`

SHA-256:

`40C7103DEEFEB3E80A95C7D506356523A93D2C8D5E442D25DF93C4D00AAC8B02`

Verifier:

`.officewars-workday-long-cycle-verify.py`

SHA-256:

`ED7797524963237C8209C13BD85F4D8C3C867ECAC0017424BE2C4D2E244D2798`

Retained screenshot:

`.visual-workday-long-cycle-audition.png`

SHA-256:

`B8F05C01D8B8F40A88E86BA439ED171A801E0A7C7FD6AE99497DD93AA99B271D`

## Boundary

Technical verification makes the comparison reviewable; it does not establish
fatigue resistance or select a long-cycle strategy. Hybrid D remains selected
and unchanged. Gameplay masking, mix translation, adaptive behavior, game
integration, and shipping remain open. No music was added to
`officewarsautobattler.html`.
