# Resume Skill Art Patch

Date: 2026-08-10

Implemented game SHA-256:
`ACF093447FFC8B51CBFB7281C577447EB23549A78A21492B5D3E1E3CC5F2BCFB`

## Resume Rail

- Added a distinct 8-bit office scene behind each Skill:
  Coding workstation, Management meeting space, Design desk, Sales storefront,
  and Operations storage rack.
- Kept the art low contrast beneath a fixed dark scrim so Skill names, XP
  segments, paths, and milestone markers remain primary.
- Dimmed and reframed the scenes in the collapsed Workday rail so the Skill
  initials remain readable.
- Marked every scene decorative and pointer-inert. Keyboard behavior and
  accessible Skill-button names are unchanged.
- Added a stronger visible focus outline and a high-contrast preference
  fallback.

## Verification

- `python .officewars-visual-capture.py`: **Pass**
- `python .officewars-smoke-run.py`: **Pass**
- `python .officewars-persistence-verify.py`: **Pass**, 23/23 checks
- `python .officewars-advanced-verify.py`: **Pass**, 8/8 groups
- `python .officewars-full-verify.py 0`: **Pass**
- Desktop, compact, landscape-phone, collapsed Workday, and 200 percent text
  samples: **Pass**
- Gameplay and balance changes: **None**
- Fresh structural balance simulation: **Not Run**, not required for this
  presentation-only patch

Detailed evidence is in
`../verification/RESUME_SKILL_ART_2026-08-10.md`.
