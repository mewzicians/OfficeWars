# Guided Coordinator Attention And Show Me Repair

Date: 2026-09-22

## Candidate

- Root HTML SHA-256:
  `1ADB8AA7D7ED25BA769DE9B24AE8AFD8CC643505395484972F331AAB00B7E776`
- Size: `1,588,617` bytes
- Active-run schema: 9
- Tutorial-meta schema: 6
- Cash Jar public gate: disabled
- Schema 10: inactive
- Public mirror: intentionally unchanged
- Release ZIP: not built

## Implemented UX

- The first Guided checkpoint is integrated into the central Floor Intro.
- The separate dock is hidden during that opening.
- The approved copy appears once:

  `Beat Chad to 45 project progress by Friday. Clock In to choose Wednesday's
  task and see what your manager expects today.`

- One visible and accessibility-exposed Clock In control remains.
- The later Coordinator dock is wider, higher contrast, and uses a one-time
  lesson-arrival cue.
- Repeat and `owGuidedRepeat` are removed.
- Show Me now resolves the next legal action, scrolls and focuses it, applies a
  strong temporary outline, and displays a temporary `NEXT` marker.
- Multi-action Night and Promotion lessons advance the Show Me target after
  each completed requirement.
- Automatic lesson attention never focuses the target or changes gameplay.
- Reduced motion suppresses movement animation.

## Defects Repaired

1. The original opening targeted the project HUD behind the active Floor Intro,
   so Show Me appeared inert. It now targets the visible Clock In action.
2. Task targeting used a retired card ID while the current Morning surface uses
   dynamic IDs such as `mcard-offer-0`. The resolver now uses the live Guided
   task marker and compact SELECT control.
3. Schedule, Role Vote, payout, Weekend, and path surfaces mounted after their
   lesson state changed, leaving Show Me hidden. Each surface now refreshes the
   Coordinator after mounting.
4. `guided-live-status` used an undefined `sr-only` class. Its accessibility
   announcement therefore rendered as duplicate visible text—the reported
   Repeat symptom. A standard visually-hidden utility now protects the live
   region.
5. The hidden dock retained a second button labelled Clock In during the
   opening. Its label is now suppressed with the dock, leaving one Clock In in
   the opening interface.

## Verification

| Suite | Result |
|---|---|
| Focused Guided Intern | Pass 37/37 |
| Persistence and Guided replay | Pass 30/30 |
| Full UI/accessibility/responsive audit | Pass |
| Smoke | Pass |
| Guided desktop capture | Pass visual inspection |
| Guided short-landscape capture | Pass visual inspection |
| Ordinary broad visual-capture suite | Fail on pre-existing readability expectations outside Guided |

Focused evidence includes:

- approved copy exactly once;
- central opening, one Clock In, no opening dock, and no Repeat;
- visible, focusable, state/RNG-inert Show Me for Clock In and Morning task;
- Show Me progression through Wednesday, Thursday, and Friday Night actions;
- Weekend Decline and path-review targeting;
- exact Guided gameplay and 1x/2x/4x/Skip/headless parity;
- all 18 lesson identities across reload;
- desktop, compact, short landscape, 200% text, reduced motion, and keyboard
  order; and
- no page or console errors.

The broad visual script contained retired fixture assumptions for milestone
counts, capstone thresholds, Clock Out political pauses, and legacy coworker
IDs. Those drivers were aligned with current rules so the suite could complete.
It then reported unrelated existing readability mismatches in Context Pins,
Resume tooltips, Campaign, Automation Combo, and several overlap checks. No
Guided Coordinator failure appears in that list.

## Visual Evidence

- `Wiki/Projects/OfficeWars/Visual Reference/visual-guided-intern-desktop.png`
- `Wiki/Projects/OfficeWars/Visual Reference/visual-guided-intern-landscape.png`

## Verdict

Coordinator attention and Show Me repair: **Pass**

The requested Guided UX is implemented and verified. The unrelated ordinary
visual-readability backlog remains a separate QA task.
