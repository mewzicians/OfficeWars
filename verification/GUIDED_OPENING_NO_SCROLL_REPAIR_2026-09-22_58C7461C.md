# Guided Opening No-Scrollbar Repair

Date: 2026-09-22

## Candidate

- Root HTML SHA-256:
  `58C7461CA6574AA56709559F251290ED7ACC36BD0942D99B46E8637B49030EF5`
- Size: `1,590,228` bytes
- Active-run schema: 9
- Cash Jar public gate: disabled
- Schema 10: inactive
- Public mirror: unchanged
- Release ZIP: not built

## Reported Defect

The Guided Floor Intro displayed an internal vertical scrollbar at the
player's desktop scaling. The generic Floor Intro body plus the new
Coordinator briefing exceeded the overlay's `88vh` maximum.

The same implementation reproduced:

- `229px` vertical overflow at 200% text; and
- `116px` vertical overflow at `844x390`.

Hiding overflow on that content would have clipped the action buttons and was
not an acceptable repair.

## Repair

Guided Intern now replaces the generic Floor Intro body with a compact
Guided-specific layout:

- the approved Coordinator objective/action briefing;
- Floor and project identity;
- three compact race facts: player target, Friday deadline, and Chad progress;
- one-line favored/adversarial/stakeholder context; and
- equal-width Show Me and Clock In controls.

The Guided panel uses `overflow:hidden` only after the layout itself proves
that its content height fits. The class is removed immediately after Clock In
and during presentation reset, so ordinary overlays retain their existing
behavior.

## Verification

| Viewport | Text scale | Vertical overflow | Actions visible |
|---|---:|---:|---|
| `1440x900` | 100% | `0px` | Yes |
| `1536x800` | 125% approximation | `0px` | Yes |
| `1440x900` | 200% | `0px` | Yes |
| `844x390` | 100% | `0px` | Yes |

Passing suites:

- Guided Intern focused verifier: `37/37`;
- persistence and Guided replay: `30/30`;
- full UI/accessibility/responsive audit: Pass; and
- smoke: Pass.

Fresh desktop and short-landscape screenshots were visually inspected:

- `Wiki/Projects/OfficeWars/Visual Reference/visual-guided-intern-desktop.png`
- `Wiki/Projects/OfficeWars/Visual Reference/visual-guided-intern-landscape.png`

## New Product Constraint

Supported player-facing surfaces must not display scrollbars unless the user
explicitly approves the named surface. Implementations must reflow, condense,
or paginate content. They must not hide overflow if that clips information or
controls.

## Remaining Global Gap

The reported Guided opening now complies. The full layout audit still records
actual overflow in ordinary Morning:

- compact Morning: `10px`; and
- short-landscape Morning: `67px`.

The broad ordinary visual-capture suite also reports existing non-Guided
readability mismatches. Those surfaces require a separate game-wide no-scroll
pass before claiming global compliance.

## Verdict

Reported Guided opening scrollbar: **Fixed**

Global no-scrollbar compliance: **Not yet complete**
