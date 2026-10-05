# Workday Candidate C Form Discovery

Date: 2026-08-18

## Scope

The source-only `OfficeWars Workday Candidate C Form Lab` tests whether the
selected Candidate C middle can support a coherent Workday form while
preserving:

- selected Ensemble C;
- `112 BPM`;
- Hybrid B's `0 / 0 / 55% / 100%` macro-motion arc; and
- the selected parent melody as the foreground protagonist.

The exploratory cue is `256` eighth-note steps, approximately `68.571`
seconds, with eight phrase-level turns:

1. `Settle In`;
2. `Desk Banter`;
3. `Detour Opens`;
4. `Detour Deepens`;
5. `Thread Returns`;
6. `Corner Turn`;
7. `Parent Returns`; and
8. `Full Groove`.

The first two and final two phrases preserve the four parent phrases exactly.
Phrases three and four preserve Candidate C's selected `64-step` melody,
harmony, and roots exactly. Only phrases five and six are new C-derived
development material.

## Protected References

- Selected middle reference:
  `Music Locked/officewars-workday-middle-melody-audition.html`
  - SHA-256:
    `021B8B9742D6AA8BFC958AA41D6E3D7504E969F1A3328769EF6F3188784D146E`
- Selected ensemble reference:
  `Music Locked/officewars-workday-ensemble-audition.html`
  - SHA-256:
    `29283F405A18DE320361BD91500626B494B8008A44921C368CC742DD9D4E9A9D`
- Selected motion reference:
  `Music Locked/officewars-workday-hybrid-audition.html`
  - SHA-256:
    `7F777F7F20B455EFE170CEF983704B409F71DF98AFD82DE22FE1E02983762E67`

All three references remained byte-unchanged.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-candidate-c-form-audition.html`
  - SHA-256:
    `17952E8F87A6630D39FB2F0867D0DF977BB7AD96F19789A81464797020253ADF`
- Focused verifier:
  `.officewars-workday-candidate-c-form-verify.py`
  - SHA-256:
    `F6813716469667D5B7355B23E4FAA6AC3E854083C6A8E34C101E652D6C594CBF`
- Retained visual:
  `.visual-workday-candidate-c-form-audition.png`
  - SHA-256:
    `F3C18A2D5476EB0E6A6EDEBB666A3B3F09782EAF3056A857738BED3C806BF502`

## Verification

The focused browser verifier passed:

- exact Candidate C notes, harmony, and roots;
- exact Ensemble C timbre, effects, and output identity;
- exact Hybrid B macro-motion values;
- exact parent phrases at the opening and return;
- distinct C-derived development material;
- smooth melodic arrivals into development, return, and loop restart;
- all eight movement starts;
- Full Cue and Melody Only audibility;
- default 50-percent output and 100-percent headroom;
- pause, resume, seeking, issue marking, and mark clearing;
- 60 rapid switches;
- desktop, landscape, and portrait layouts without overflow or clipped
  controls;
- two uninterrupted loops of both listening modes;
- bounded active and peak source counts;
- no page or console errors; and
- cleanup to zero tracked sources.

Commands:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONPATH="$env:TEMP\officewars-python"
python -B .officewars-workday-candidate-c-form-verify.py --quick
python -B .officewars-workday-candidate-c-form-verify.py
```

## Decision Boundary

Technical verification establishes that the audition preserves its selected
foundations and has a stable audio lifecycle. It does not select the complete
form, the two new development phrases, duration, transitions, production, or
game integration. Those remain exploratory until human listening.
