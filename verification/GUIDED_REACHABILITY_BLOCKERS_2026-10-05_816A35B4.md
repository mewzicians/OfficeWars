# Guided Reachability Blockers

Date: 2026-10-05  
Rigor: standard  
Candidate SHA-256:
`816A35B40CD4F36C6CF25CD766BF6FEB94A1D77D885C56947B73F6C4228F52AA`  
Candidate size: `1,730,955` bytes  
Predecessor: `0B220B29C569B218B3A0038DACF81CACF3A7265186FC31335C3703C4E26BC288`

## Defects

1. Guided step 8 (`GI-THU-POLITICS`) required Office Politics during Morning,
   but the only entry was the HUD button under the Morning overlay. A real
   click landed on the Morning page.
2. The fixed Coordinator dock covered overlay controls. At 1366x768 it hid
   CONFIRM PROMOTION in step 18 (`GI-FRI-PATH`), and Show Me never targeted
   that button.

## Repair

- Morning renders its own OFFICE POLITICS button in the panel header for
  every player; the HUD-state wrapper keeps both copies enabled together.
- Step 8 targets the Morning button.
- After a path is chosen, step 18 instructs and Show Me targets CONFIRM
  PROMOTION.
- The dock stays full-size at the bottom when it covers no live control.
  Otherwise it collapses to one line, and moves to the top only when that
  covers fewer controls. Refit runs on overlay, scene, modal, scroll, and
  resize changes, coalesced to one frame.
- The Show Me marker tries above, below, right, and left, each left- and
  right-aligned, rejecting placements that leave the viewport or meet the
  target or the dock. It takes the first that covers no visible control,
  enabled or disabled, and otherwise the one covering fewest.
- The full-dock checklist is unchanged; only the one-line dock hides it.

No gameplay state, RNG, schema, or balance value changed.

## Evidence

| Suite | Result |
|---|---|
| `.officewars-guided-reachability-verify.py` (new) | Pass 364/364, 52 checks each, across 1366x768, 1024x768, 844x390, 1440x900, 1280x650, 1536x800, and 1440x900 at 200% text |
| Same suite against the predecessor | Fail 196/329; no Morning entry, CONFIRM PROMOTION real click times out at 5 of 6 viewports |
| `.officewars-guided-intern-verify.py` | Pass 47/47 twice on the final bytes; 4 of 5 earlier runs; see watchpoint |
| `.officewars-no-scroll-verify.py` | Pass |
| `.officewars-persistence-verify.py` | Pass |
| `.officewars-smoke-run.py` | Pass |
| Inline script parse and page errors | Pass; none |
| Fit cost, 8 s animated Workday at 1366x768 | 8 fits, 30 ms total, 18.5 ms longest |

## Pinned Residuals

Both residuals existed in the predecessor. The new suite pins them exactly, so
a fix or a new overlap fails until its table is updated.

- 844x390 Mornings: the one-line dock still covers VIEW OFFICE. Panel, toggle,
  and dock need 393px of 390px, and the toggle must stay outside the panel it
  hides.
- 1440x900 at 200% text: the Promotion Review panel overflows after a path is
  chosen. After Show Me scrolls it, the top dock covers one path card and the
  marker covers the disabled previous-page arrow.

## Watchpoint

`guided-political-focus-reload` failed once in five runs. The game focuses the
first political choice in a `requestAnimationFrame` after render, and the
suite reads `document.activeElement` without waiting for it. The dock fit
never moves focus.

## Boundaries

Not Run: the remaining focused suites, simulations, formal screen-reader
execution, and human playtesting. The mirror was synchronized afterward for
the 2026-10-05 publish. No release ZIP was built.
