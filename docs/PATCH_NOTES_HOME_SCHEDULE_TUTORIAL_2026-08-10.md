# Home, Schedule, And Tutorial Readability Patch

Date: 2026-08-10

Implemented game SHA-256:
`0A8F74E5A47EDE063FE6100B053998601AD0B8D8BC4C521E644C3BE5BA9AB0AE`

## Schedule Decisions

- Replaced prose schedule previews with horizontal action-icon trackers.
- Stacked competing schedules for direct comparison and highlighted changed
  entries.
- Added visible source, replacement, bonus, procedure, hostile, and repeat
  states to schedule nodes.
- Applied the shared tracker to Prototype Test, Schedule Adjustment,
  Leadership, action guarantees, and the final Schedule Desk.

## Home Phase

- Replaced the office Night overlay with the player's full-screen living
  space.
- Added room controls for Home Shop, Relationships, Outings, unlocked Deals,
  Lights Out, and End Day.
- Added accessible visual Home-item slots. Occupied slots expose their effect
  and open a sale confirmation.
- Kept Cash, Expense Credit, current Stress, and projected post-sleep Stress
  prominent without duplicating the former Night footer.
- Added distinct Apartment, Townhouse, House, and Penthouse room layouts.
  Home-tier item restrictions remain deferred balance work.

## Transitions And Persistence

- Added sunset and door-opening entry, Outing fade and return, and sunrise
  exit presentations.
- Reduced-motion and automated play bypass presentation timing without
  changing outcomes.
- Sleep now writes a stable `nightResolved` checkpoint before sunrise.
  Refreshing during the transition advances once and cannot repeat recovery.

## Orientation

- Expanded the contextual orientation to thirteen steps.
- The first Workday pause opens the Action Guide and explains Work on Task,
  Lunch, Water Cooler, Office Chat, Slumped at Desk, and Team Meeting.
- The first Night spotlights Home Shop, Outings, Relationships, and End Day
  through the room itself.
- The first Capstone claim receives the final orientation callout. Deals remain
  an advanced discovery.

## Verification

- `python .officewars-smoke-run.py`: **Pass**
- `python .officewars-home-schedule-verify.py`: **Pass**
- `python .officewars-persistence-verify.py`: **Pass**, 24/24 checks
- `python .officewars-advanced-verify.py`: **Pass**, 8/8 groups
- `python .officewars-visual-capture.py --quiet`: **Pass**, 38 cases
- `python .officewars-full-verify.py 0`: **Pass**
- Fresh structural balance simulation: **Not Run**

Detailed evidence is in
`../verification/HOME_SCHEDULE_TUTORIAL_2026-08-10.md`.
