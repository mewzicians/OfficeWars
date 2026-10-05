# Workday Transition Repair Discovery

Date: 2026-08-17

## Scope

This source-only experiment tests three reported transition problems in
Workday Relational Form Draft 02 without changing its selected melody,
`112 BPM` pace, six-movement form, or Ensemble C identity.

Human listening identified:

- an awkward beginning to `Band Invites`;
- an awkward start to `Roles Reverse`, while finding its reversed notes
  interesting; and
- a strange moment in `Teamwork`.

The music-guide diagnosis is abrupt role transfer rather than weak core
material.

## Comparison

Version A preserves Draft 02 exactly.

Version B changes only three handoffs:

1. `Band Invites` resolves the preceding `B` to an organ `C`, begins on the
   parent harmony, and leaves the foreground entrance unchanged.
2. `Roles Reverse` preserves every reversed foreground note, foreshadows the
   organ takeover in the preceding phrase, and ramps organ leadership across
   four bars.
3. `Teamwork` replaces the close-shadowing `8 / 6` counterline attacks with
   complementary `4 / 4` harmonic anchors.

The audition provides both complete forms and six one-shot boundary clips.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-transition-repair-audition.html`
- Audition SHA-256:
  `F9D0B935D2D3A9A7DE8E3EC534362D2A39E5279FBF4355E5C05B9852010BFBE9`
- Verifier:
  `.officewars-workday-transition-repair-verify.py`
- Verifier SHA-256:
  `9028E4935CE1825F0660636538B57CA59129041BE515CB23E0B5D8E3A97305C9`
- Visual capture:
  `.visual-workday-transition-repair-audition.png`
- Visual-capture SHA-256:
  `E1833C6907FD43A15FD807E92F35ED69835B1F506D45EC8B4C465ACA2D3E903D`
- Protected Draft 02 control SHA-256:
  `AA0DDF1A9F1EFE629CE4E0BC108902533760F14339294C91BB82AF9463270DEB`

## Verification

The focused Playwright run passes:

- exact Version A equality with protected Draft 02;
- identical foreground notes in Versions A and B;
- exact preservation of the reversed `Roles Reverse` melody;
- repair-only harmony, organ-leadership, and counterline changes;
- eight audible and comparison-safe playback modes at 50 percent volume;
- 100 percent output headroom;
- pause, resume, seek, timestamp, and mark clearing;
- 64 rapid A/B switches;
- one-shot boundary completion;
- two uninterrupted wraps of both complete forms;
- bounded active and peak source counts;
- cleanup to zero active sources; and
- desktop, landscape, and portrait layout checks.

## Status

Technically verified and musically exploratory.

No transition repair, complete Workday cue, final production, mix, gameplay
integration, or shipped audio is selected by this evidence. Human listening
must determine whether Version B improves each boundary without damaging the
interesting material.
