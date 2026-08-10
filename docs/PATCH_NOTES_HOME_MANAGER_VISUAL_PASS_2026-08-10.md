# Home And Manager Visual Pass

Date: 2026-08-10

Implemented game SHA-256:
`DD5BFD100A3E4B270587F62346DF7AF456484DF6AB7DA72A5C4EBBE13BA98488`

## Home Scene

- Grounded the Home Shop desk, Relationships phone table, Deal laptop, item
  slots, bed, and exit door across Apartment, Townhouse, House, and Penthouse.
- Rebuilt Home Shop as a monitor, stand, tower, keyboard, mouse, and desk.
- Replaced the Relationships book with a phone.
- Enlarged the bed and gave it a frame, mattress, pillow, blanket, and legs.
- Moved the moon inside the room window and reduced the lower-left room label
  to the Home name.
- Restored a top Stress bar beside Cash, Expense Credit, and projected sleep.
- Replaced the lamp control with a wall light switch. Selecting Lights Out
  changes the switch state and visibly dims the room while controls remain
  readable.
- Placed all visual item slots on the central floor rug. Penthouse uses a
  stable four-column layout for its twelve slots.

## Transitions

- Replaced diagonal sunset and sunrise paths with five-stage curved arcs.
- Sunset carries the sun west and down while the moon rises from the east.
- Sunrise carries the sun up from the east while the moon arcs west and down.
- Reduced-motion and automated paths retain their existing deterministic
  bypasses.

## Manager Presence

- Added a distinct portrait and color for each of the eight managers.
- The current manager sits behind the manager desk on ordinary floors.
- Boss floors replace the seated portrait with a cosmetic office patrol.
- The patrol is not part of `CAST`, consumes no RNG, reserves no cubicles, and
  cannot change Workday resolution, playback speed outcomes, or Skip.

## Verification

- Expanded the focused Home runner from two Apartment samples to all four Home
  tiers at desktop and landscape-phone sizes.
- Added checks for floor anchoring, window-contained moon geometry, Stress-bar
  fill, PC and phone parts, bed scale, room dimming, all manager variants,
  boss-floor patrol isolation, and curved transition keyframes.
- Updated orientation, visual-matrix, persistence, and full-verifier contracts
  from the Relationships book to the phone.

Detailed evidence is in
`../verification/HOME_MANAGER_VISUAL_PASS_2026-08-10.md`.
