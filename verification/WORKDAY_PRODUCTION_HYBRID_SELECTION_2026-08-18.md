# Workday Production Hybrid Selection Verification

Date: 2026-08-18
Status: Selected standalone Workday production foundation; not integrated into
the game

## Selection

Human listening selected `Hybrid D`.

Hybrid D preserves the complete selected Workday composition and combines:

- Production A's warmer lead;
- Production A's warmer connected lead;
- Production A's organ;
- Production B's tighter bass;
- Production B's tighter drums; and
- Production B's cleaner delay, feedback, and wet-space treatment.

The selection preserves the exact `256-step`, approximately `68.571-second`
form, Candidate C, Passage D, Ensemble C, `112 BPM`, Hybrid B motion arc,
development phrases, revised Corner Turn, parent return, and loop.

## Full Verification

Command:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
$env:PYTHONPATH="$env:TEMP\officewars-python"
python -B '.officewars-workday-production-hybrid-verify.py'
```

Result: `PASS: OfficeWars Workday production hybrid audition`

All four complete versions passed:

- exact selected composition and Passage D preservation;
- exact Production A and Production B references;
- intended Hybrid C and Hybrid D role ownership;
- all twelve Full, Backing, and Lead-plus-Organ modes;
- usable and comparison-safe output;
- 100-percent headroom;
- pause, resume, seeking, movement starts, and rapid switching;
- desktop, landscape, and portrait layouts;
- two uninterrupted complete loops; and
- zero active sources after stopping.

Hybrid D's long-run snapshot after two wraps reported:

- `wrapCount: 2`;
- `peakSources: 41`;
- `activeSources: 18` during live playback;
- `signalPeak: 0.037923`; and
- no clipping or scheduler accumulation.

## Artifacts

Selected reference:

`Music Locked/officewars-workday-production-hybrid-audition.html`

SHA-256:

`8BE0BB035799450ABED8FCA13A5F1BF40634FB54DE65EDD4F019F6DD17610D1B`

Verifier:

`.officewars-workday-production-hybrid-verify.py`

SHA-256:

`06FB2B2E374290064F0B324DC3FE0C71A5A513B131EA2715B238B5A697A623CD`

Retained screenshot:

`.visual-workday-production-hybrid-audition.png`

SHA-256:

`F2F9C5CA799B4EF1A99D488ABBA98891B9A49A28FFAFEE9F6DBA7DFBC60D37D8`

## Boundary

This selects the standalone Workday production foundation. It does not add
audio to `officewarsautobattler.html`, approve gameplay masking, prove
long-session fatigue resistance in the game, define adaptive states, or mark
the cue shipped.
