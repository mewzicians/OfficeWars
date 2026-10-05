# Workday Role Transfer Discovery

Date: 2026-08-17

## Scope

Human listening found Transition Repair Version B slightly better than Draft
02, but still short of the intended Workday cue. The full-scope review traced
the earliest remaining weakness to musical hierarchy: the organ was described
as a temporary protagonist while the lead remained continuously foregrounded.

This source-only diagnostic preserves Transition Repair Version B as exact
Version A. Version B keeps the same foreground pitches, harmony, `112 BPM`
tempo, `384-step` form, Ensemble C identity, and loop duration while changing
how the melody and band exchange ownership.

## Comparison

Version B tests one coordinated hierarchy hypothesis:

1. `Invitation` keeps the repaired organ `C`, adds an organ `D`, and lets the
   existing melody complete the parent rise on `E`.
2. `Role Transfer` gives the complete reversed phrase to an organ-lead voice.
   The lead rests for that phrase, then the organ carries the first half of
   the following phrase before handing it back.
3. `Recognition` preserves the parent foreground over a reduced groove and a
   low sustained organ halo so the return does not duplicate the opening
   arrangement.
4. `Teamwork` replaces the prior `4 / 4` lead-register anchors with two
   six-note lower-register replies. Every reply enters in a foreground gap
   and uses notes no higher than MIDI `55`.

The audition provides both complete forms plus direct A/B clips for all four
relationships.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-role-transfer-audition.html`
- Audition SHA-256:
  `F33F4E714D27109C4419A71A45C4577B11538151F47C3E5E6799B3BEC43EC55B`
- Verifier:
  `.officewars-workday-role-transfer-verify.py`
- Verifier SHA-256:
  `E2C91823B5B8E632BB2C819F74F31DAD041031396C2E8878BD19111B0A4C6439`
- Visual capture:
  `.visual-workday-role-transfer-audition.png`
- Visual-capture SHA-256:
  `F22AA796E64F474021E79CBF2D72ED762872E3EEB0C365A9B4A934467102A316`
- Protected Transition Repair control SHA-256:
  `F9D0B935D2D3A9A7DE8E3EC534362D2A39E5279FBF4355E5C05B9852010BFBE9`

## Verification

The focused Playwright run passes:

- exact Version A equality with Transition Repair Version B;
- identical foreground pitches, harmony, tempo, form, and selected ensemble
  in both versions;
- exact preservation of the reversed foreground phrase;
- one organ invitation note and three organ pickup notes in Version B;
- complete organ ownership of the reversed phrase and an organ-to-lead
  handoff inside the following phrase;
- a distinct reduced-groove and low-organ-halo Recognition arrangement;
- six lower reply attacks in each Teamwork phrase with no simultaneous
  foreground attacks;
- ten audible and comparison-safe playback modes at 50-percent volume;
- 100-percent output headroom;
- pause, resume, seek, timestamp, and mark clearing;
- 80 rapid A/B switches;
- one-shot relationship-clip completion;
- two uninterrupted wraps of both complete forms;
- bounded active and peak source counts;
- cleanup to zero active sources; and
- desktop, landscape, and portrait layout checks.

## Status

Technically verified and musically exploratory.

No role-transfer treatment, complete Workday cue, final production, mix,
gameplay integration, or shipped audio is selected by this evidence. Human
listening must determine whether Version B now creates a real second
protagonist, a convincing return, and cooperative Teamwork without weakening
the selected Workday identity.
