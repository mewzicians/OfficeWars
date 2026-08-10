# Home Grounding And Celestial Sequence

Date: 2026-08-10

Implemented game SHA-256:
`470F4146FBA177FD6B7062A0093DDCF7C2826B797FE9AE74317BD1D146050FF7`

## Home Composition

- Replaced the deep brown floor band with a shallow plank floor and a clear
  baseboard across Apartment, Townhouse, House, and Penthouse.
- Grounded the bed, Relationships phone table, Home Shop PC desk, Deal desk,
  plant, and Outings door on one shared boundary.
- Kept furniture bodies above the baseboard while allowing their feet to
  extend naturally into the floor strip.
- Kept the Home name below the furniture and preserved the wall shelf, item
  slots, window moon, status bar, Lights Out dimming, and room controls.

## Celestial Motion

- The sun and moon now use the same full-width east-to-west arc.
- At sunset, the sun leads and the moon follows.
- At sunrise, the moon leads and the sun follows.
- Identical paths, durations, and linear timing preserve their spacing so the
  two bodies never cross.
- Reduced-motion and automated paths retain their deterministic bypasses.

## Verification

- Updated the focused Home runner to check the rendered furniture baseline,
  Home-name placement, shared celestial path, matching timing, and lead delays.
- Re-ran Home, smoke, persistence, advanced-interaction, readability, and
  no-simulation full verification.

Detailed evidence is in
`../verification/HOME_GROUNDING_CELESTIAL_SEQUENCE_2026-08-10.md`.
