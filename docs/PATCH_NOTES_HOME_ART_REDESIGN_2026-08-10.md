# Home Art Redesign Patch

Date: 2026-08-10

Implemented game SHA-256:
`286D494DCD9DFE1A237D702B0E1BDEA203099F48A7E65525DBF285EDEC1B2B52`

## Why

Home rooms read as misaligned and visually unfinished. Furniture bounding boxes
were already pinned to the shared feet line, so the automated grounding check
passed, but the art *inside* each box floated above its own bottom edge by fixed
`rem` offsets and percentage-of-own-height legs. Every piece therefore stopped at
a slightly different height and nothing appeared to rest on the floor.

The palette had also drifted away from the office scene, which uses hard dark
outlines, flat fills, and offset shadows.

## Alignment

- Introduced explicit `home-room-wall` and `home-room-floor` layers. The floor
  element's top edge now *is* the feet line, so wall, baseboard, and floor cannot
  drift apart.
- Every furniture piece now draws from `bottom:0` of its own hotspot box. Legs,
  pedestals, and the plant pot end exactly on the shared boundary instead of
  being offset by `rem` insets.
- Measured result: bed, phone table, Home Shop desk, Deal desk, door, and plant
  all land within 0.01px of the floor line on desktop and landscape.
- The PC tower now stands on the floor beside the desk rather than floating
  against the desk edge.

## Office Art Language

- Adopted the office scene's tokens: `#17272d` outlines, `#845d3d` / `#4c3526`
  wood, `#26353b` / `#71868b` metal, `#6b9fb0` glass, and `#e8c36e` gold.
- Replaced the washed grey-green wall with the office's dark teal family and
  added the same faint 32px grid and top-light gradient.
- Replaced blurred shadows with the office's flat offset shadow.
- Removed the rounded and skewed shapes that fought the pixel treatment: the
  mouse, pillow, phone, keyboard, and laptop are now axis-aligned.
- Window now uses the office window's heavier bottom border and inner light.

## Composition

- Enlarged all furniture so the room reads as furnished rather than as a thin
  strip along the floor.
- Item slots now rest on the wall shelf instead of floating above it.
- Added a wall clock in the previously empty wall between the window and the
  side table, reusing the unused decorative span.
- Moved the light switch clear of the item slots; its label no longer overlaps
  them.
- Moved the wall art clear of the window. The wider House and Penthouse windows
  previously overlapped it, including in landscape, where the tier rules
  out-specify the landscape overrides.
- Retired the floating rug, which read as a bar rather than a floor covering.

## Tiers

Apartment, Townhouse, House, and Penthouse now differ by material quality rather
than only by a tint: Townhouse adds a wainscot rail, House adds a chair rail and
a wider window, and Penthouse adds panelled walls, gold trim, a dark stone floor,
and the largest window.

## Lights Out

Furniture now sits below the room dim layer, so the room dims uniformly. The
redundant per-hotspot dim was disabled because it drew visible dark rectangles
around each piece. Controls and labels stay legible, and `SHOP LOCKED` /
`DEALS LOCKED` remain the purchase-lock signal.

## Not Changed

No gameplay, balance, state, or persistence behaviour. This patch is presentation
only; every class name the verification suites assert on is preserved.
