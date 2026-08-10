# Celestial Opposing Arcs Patch

Date: 2026-08-10

Implemented game SHA-256:
`1735BF27F06FC1273C7A58043791BA64CF4F33A5B03A81529E936D8F559341DF`

## Why

Both phase transitions were physically wrong. The sun and moon started from the
same point off the eastern edge and ran the *same* five-stage keyframe path
across the sky, separated only by a negative `animation-delay` of about two
tenths of a second. The trailing body therefore chased the leading body across
the screen and both left by the same western edge together.

Superseded decision: the previous rule was that the two bodies share one arc
with the sun leading at sunset and the moon leading at sunrise. That is replaced
by the rule below.

## Behaviour

The sun and moon still share one east-to-west arc, but they never occupy the
same stretch of it. At each transition:

- the departing body starts at the apex resting position, completes the western
  half of the arc, and drops below that edge;
- the arriving body enters from the opposite eastern edge and climbs the eastern
  half to the apex resting position the departing body just vacated.

Sunset therefore sets the sun in the west while the moon rises in the east.
Sunrise sets the moon in the west while the sun rises in the east. The two are
always on opposite sides of the sky.

## Implementation

- Replaced the four full-path keyframes `ow-sun-set`, `ow-moon-rise`,
  `ow-sun-rise`, and `ow-moon-set` with two half-arc keyframes, `ow-arc-ascend`
  and `ow-arc-descend`, cut from the same underlying path so the halves join
  exactly at the apex.
- Removed the negative `animation-delay` offsets that produced the chase.
- Sunset now plays `ow-arc-descend` on the sun and `ow-arc-ascend` on the moon;
  sunrise plays the reverse.

## Transition Moon Phase

A new moon is drawn as a fully masked disc. That is correct for the static Home
window, but while the moon is arcing across the sky it reads as a hole rather
than a moon. `owTransitionMoonPhaseClass` now promotes `phase-new` to
`phase-crescent` for transitions only. The Home window moon still shows the true
phase, and no other phase is altered.

## Verification Suite

`.officewars-home-schedule-verify.py` asserted the superseded rule in three
places and would have failed on the new behaviour:

- it required the four deleted keyframes `ow-sun-set`, `ow-moon-rise`,
  `ow-sun-rise`, and `ow-moon-set`, each with at least five steps;
- `transition-paths` required all four arc paths to be *identical*, which was
  the shared-arc rule itself;
- `transition-phasing` required the exact `-0.22s` and `-0.2s` delays that
  produced the chase.

Those assertions now check the current rule instead: the two half-arc keyframes
exist, the descending half exits past `100vw`, the halves join exactly at the
apex (`ascend[-1] == descend[0]`), every animation delay is `0s`, and the sun
and moon always run opposite halves, swapped between sunset and sunrise.

## Verification

Both transitions were sampled at eleven points across their full duration at
1280x800, measuring each body's centre as a percentage of viewport width:

- sunset minimum horizontal separation: 48.1 percent of viewport width;
- sunrise minimum horizontal separation: 48.0 percent of viewport width;
- no page or console errors.

The updated suite assertions were evaluated directly in the browser against the
shipped stylesheet and all pass. The transition moon resolves to
`phase-crescent` on a day-0 run whose true phase is `phase-new`, while the Home
window moon still resolves to `phase-new`.

Note: no Python interpreter is available on the machine used for this change, so
`.officewars-home-schedule-verify.py` was not executed end to end. Its celestial
assertions were reproduced exactly and checked in the same browser engine; the
remaining rows in that suite are unverified for this hash.

The Home room geometry suite was rerun and is unchanged: all four tiers ground
within 0.01px of the floor line on desktop and landscape.

## Not Changed

Durations, sky and curtain timing, the door-opening step, the Outing fade, moon
phase selection, and every reduced-motion and automated bypass are untouched.
No gameplay, balance, or persistence behaviour changes.
