# Workday Ensemble Discovery Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday ensemble-identity
audition. It follows human listening that found the earlier sustained-glue and
sparse-reply treatments too subtle to make the melody feel supported or to
communicate recognizable instrumental intent.

## Decision Status

**Ensemble C selected as the Workday ensemble foundation**

The selected parent melody, office-funk palette, `112 BPM` pace, harmony,
bass, drums, and Hybrid B `0 / 0 / 55% / 100%` development arc remain
protected. Human listening selected Ensemble C because its accompaniment and
melody work together and uplift one another. Ensembles A and B sounded present
without creating the same reciprocal relationship and do not carry forward
for this role.

This selects the accompaniment identity and ensemble relationship only.
Complete Workday form, long-exposure development, final production, gameplay
masking, and game integration remain open.

## Artifacts

- Audition:
  `Music Locked/officewars-workday-ensemble-audition.html`
- Audition SHA-256:
  `29283F405A18DE320361BD91500626B494B8008A44921C368CC742DD9D4E9A9D`
- Verifier:
  `.officewars-workday-ensemble-verify.py`
- Verifier SHA-256:
  `D3384349C9114F5C9BFEAAEB3AF9521AD033A1A2988BAEF5ED6A1315AC64A954`
- Desktop capture:
  `.visual-workday-ensemble-audition.png`
- Capture SHA-256:
  `EA613777618A09BCA6A63A1CB12DA4C3B0E3CDBBB369B8F6FBBD06893E83A394`

## Controlled Musical Contract

All three candidates are `128` steps, approximately `34.286` seconds, and
`112 BPM`. They share the exact selected foreground, chord roots, bass, drums,
four phrase functions, and gradual Hybrid B motion arc.

Only the harmonic backing identity and resulting mix hierarchy differ:

1. Ensemble A uses a rounded, ringing electric-piano behavior with sustained
   chord body and short phrase replies.
2. Ensemble B uses percussive clavinet-like interlocks over a restrained
   two-voice bed.
3. Ensemble C uses sustained organ-like voicings and measured rhythmic
   swells.

Each candidate provides:

- **Full Mix** for the intended ensemble relationship;
- **Backing Only** for rhythm, bass, and harmony without the melody; and
- **Harmony Only** for direct instrumental identification.

The isolated monitor gains are normalized independently from the unchanged
full-mix relationships so timbre can be compared without loudness bias.

## Browser Evidence

After selection, the focused Playwright runner passes:

- page parsing with no page or console errors;
- exact selected-melody equality with Hybrid B across all nine playback modes;
- exact harmony roots and the `0 / 0 / 55% / 100%` motion arc;
- three distinct accompaniment profiles and correct Full, Backing, and
  Harmony layer contracts;
- audible 50-percent playback for every isolated and combined layer;
- the explicit Ensemble C selection scope without implying complete-cue
  approval or shipping;
- full-mix averages of `0.029399`, `0.027451`, and `0.031185`;
- harmony-only averages of `0.013769`, `0.011897`, and `0.012871`;
- retained 100-percent headroom with a maximum sampled peak of `0.294967`;
- pause, resume, seeking, timestamp marking, and timestamp clearing;
- 72 rapid switches across all nine playback modes;
- two uninterrupted complete loops of all three full mixes;
- long-play peak live-source counts of `27`, `21`, and `39`;
- stop cleanup to zero tracked sources;
- desktop, landscape, and portrait layouts without horizontal overflow or
  clipped controls; and
- visual inspection of the retained desktop capture.

## Not Run

- Long-exposure listening beyond the verified repeated loops.
- Complete Workday form, final production, gameplay masking, or game
  integration.
