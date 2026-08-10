# Celestial Opposing Arcs Patch

Date: 2026-08-10

Implemented game SHA-256:
`F51AD51327F63AE55214D0A73D1BA55A46964950A291D6AE6E48E307898DF9EE`

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

## Verification

Both transitions were sampled at eleven points across their full duration at
1280x800, measuring each body's centre as a percentage of viewport width:

- sunset minimum horizontal separation: 48.1 percent of viewport width;
- sunrise minimum horizontal separation: 48.0 percent of viewport width;
- no page or console errors.

The Home room geometry suite was rerun and is unchanged: all four tiers ground
within 0.01px of the floor line on desktop and landscape.

## Not Changed

Durations, sky and curtain timing, the door-opening step, the Outing fade, moon
phase selection, and every reduced-motion and automated bypass are untouched.
No gameplay, balance, or persistence behaviour changes.
