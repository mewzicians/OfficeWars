# Home Side-View And Celestial Arcs

Date: 2026-08-10

Implemented game SHA-256:
`C68FF6FF42BFC19DB334BD72F1A13C1DABA6196C76E7E347BB7AB11E50ABBA5B`

## Home Composition

- Rebuilt Apartment, Townhouse, House, and Penthouse as flat side-view room
  elevations with one unambiguous floor line.
- Ordered the interactive furniture from left to right as End Day bed,
  Relationships phone, Home Shop PC, Deal laptop, and Outings door.
- Enlarged the window and retained the moon inside its frame.
- Removed the perspective rug and sofa treatment that made furniture appear
  layered or detached from the floor.
- Moved Home item capacity to a wall storage shelf. Apartment through
  Penthouse retain their exact 3, 6, 9, and 12 accessible slots.
- Preserved the top Cash, Expense Credit, Stress, and projected-sleep display,
  room-wide Lights Out dimming, keyboard access, tooltips, and sale prompts.

## Transitions

- Sunset now carries the sun from the left edge to the right edge while the
  moon crosses from right to left.
- Sunrise reverses those directions.
- Each body uses a five-stage arch with its apex near the center of the
  transition window rather than a short diagonal path.
- Reduced-motion and automated paths retain their deterministic bypasses.

## Verification

- Updated the focused Home runner to require the shared floor order and
  wall-mounted slot region across all four Homes at desktop and landscape
  sizes.
- Added full-viewport distance and direction checks for all four celestial
  keyframes.
- Re-ran smoke, persistence, advanced interactions, the readability visual
  matrix, and the no-simulation full verifier.

Detailed evidence is in
`../verification/HOME_SIDE_VIEW_ARCS_2026-08-10.md`.
