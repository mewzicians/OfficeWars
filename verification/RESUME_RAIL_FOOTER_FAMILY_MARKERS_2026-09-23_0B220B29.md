# Resume Rail Footer And Family Markers

Date: 2026-09-23  
Rigor: standard  
Candidate SHA-256:
`0B220B29C569B218B3A0038DACF81CACF3A7265186FC31335C3703C4E26BC288`  
Candidate size: `1,719,028` bytes

## Outcome

The compact Resume rail now uses a bottom footer with exact progress on the
left and one uninterrupted bar on the right. The five Skill families use
distinct 16px pixel markers for their next milestone. The full Resume Book
retains its detailed 20-square track and milestone tooltips.

Completed Skills use a full family-colored bar, brighter frame, and pixel
corner accents without next-milestone text. Active capstones add a gold star,
double frame, and one ephemeral acquisition shimmer. The shimmer does not
replay after reload and is absent under reduced motion.

The four Guided opening steps share one fixed decorative SVG connector with a
7px dark stroke, 3px gold stroke, square joins, and a block arrowhead. It
rebuilds after each step and refits after viewport changes without changing
state or gameplay RNG.

## Implementation

- Desktop Resume rail width is `clamp(180px, 13vw, 230px)`; Workday remains
  collapsed to 70px.
- Compact rows expose `PATH n`, `PATH READY`, and `NEXT n` states through a
  shared presentation model.
- Ordinary paths fill toward 20 XP, Accelerated Development toward 18 XP, and
  Closing toward Chain 9 while exact uncapped XP remains visible.
- Coding, Management, Design, Sales, and Operations use monitor, clipboard,
  paintbrush, briefcase, and box markers.
- Marker placement clamps inside both ends of the bar and disappears after
  the final milestone.
- Rail buttons retain complete accessible labels; markers and the Guided
  connector are decorative and pointer-inert.

## Verification

| Suite | Result |
|---|---|
| `.officewars-phase5-verify.py` | Pass; compact/detail split, all rail states, five markers, clipping, shimmer, reduced motion, reload, and inertness |
| `.officewars-guided-intern-verify.py` | Pass 47/47; all four connector routes, reload, responsive geometry, accessibility, and parity |
| `.officewars-visual-capture.py` | Pass; broad desktop/compact/landscape/200%-text readability matrix |
| `.officewars-no-scroll-verify.py` | Pass 354/354 surface checks |
| `.officewars-persistence-verify.py` | Pass |
| `.officewars-smoke-run.py` | Pass |
| `.officewars-full-verify.py 0` | Pass core and UI audit; simulations intentionally disabled for this presentation-only change |

No page errors, console errors, clipping, required-content collisions, state
mutation, or gameplay-RNG changes were observed.

## Boundaries

Cash Jar remains gated, active-run schema remains 9, schema 10 remains
inactive, Galactic Investment and Galactic Gambler are unchanged, the public
mirror was not synchronized, and no release ZIP was built.

Formal screen-reader execution and broad human playtesting remain Not Run.
