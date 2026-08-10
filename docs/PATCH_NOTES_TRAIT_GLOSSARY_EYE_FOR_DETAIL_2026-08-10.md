# Trait Glossary And Eye For Detail Patch

Date: 2026-08-10

Implemented game SHA-256:
`CF59C4A593E3B4E7BB41A591959306FE8214CA869A2D0FF2251DBB11F4E581A9`

## Eye For Detail

- Revision now records whether the previous primary task came from the
  generated offer, Pinned Tasks, or storage.
- A primary task selected from Pinned Tasks does not create another Revision
  pin the next morning.
- The same task can create Revision normally after a later generated-offer
  play.
- Masterpiece and every other independent pin source remain unchanged.

## Trait Rules

- Named mechanics such as Codebase, Polish, Scope Renegotiation, and Reserve
  Levels use one high-contrast cyan treatment.
- One data-driven glossary provides short definitions through hover, keyboard
  focus, and tap in path choices, Promotion Review, and the Resume.
- Choice cards expose the same glossary to keyboard users without nesting
  focusable controls inside their buttons.

## Orientation

- Removed the conditional Deals lesson from the basic tutorial.
- Added a first-Capstone lesson explaining the run-wide one-Capstone rule.
- Updated Relationships to explain that coworker bonuses trigger when the
  player meets coworkers during the Workday.
- Existing schema-1 tutorial preferences migrate to schema 2 without clearing
  volume or completed-tutorial state.

## Verification

- `python .officewars-smoke-run.py`: **Pass**
- `python .officewars-persistence-verify.py`: **Pass**, 23/23 checks
- `python .officewars-advanced-verify.py`: **Pass**, including the new pin,
  glossary, and tutorial contract group
- `python .officewars-visual-capture.py --quiet`: **Pass**
- `python .officewars-full-verify.py 0`: **Pass**

Detailed focused evidence is in
`../verification/TRAIT_GLOSSARY_EYE_FOR_DETAIL_2026-08-10.md`.
