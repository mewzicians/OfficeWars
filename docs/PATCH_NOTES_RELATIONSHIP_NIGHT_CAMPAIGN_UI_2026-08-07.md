# Relationship, Night, And Campaign UI Patch Notes

Release date: 2026-08-07

Implemented game SHA-256:
`30214B7FFF8FB4ED44690B90B64EE991E8F300ACE1A4E66E9100BBDAFCC81D12`

## Player-Facing Changes

### Relationships

- Relationship views and tooltips show the coworker's actual bonus without the
  redundant `Day Bonus` or `improves with relationship` labels.
- The Outings footer now explains that coworkers grant their bonus when met
  during the Workday.

### Night

- Manual Lights Out and Home or Deal purchases are mutually exclusive in both
  directions.
- Selecting manual Lights Out disables Home and Deal purchases. Outings remain
  available.
- Making a Home or Deal purchase disables manual Lights Out.
- Moodboard's automatic Lights Out is the explicit exception and may coexist
  with purchases.
- Restoring an older Night save that contains both a purchase and manual
  Lights Out preserves the purchase and clears manual Lights Out.
- Choosing Lights Out suppresses unused Home and Deal purchase warnings because
  those actions are no longer legal. Other valid warnings, such as an unused
  Outing or unspent Expense Credit, may still appear.

### Brand Strategy

- An active Campaign adds a dedicated Morning status band with Campaign name,
  requested card and family, completed steps, and Campaigns completed.
- `Rebrand Initiative` now reads:
  `Unlock Brand Strategy. Some task offers become Campaign cards. Play the
  requested Campaign cards in order to complete Campaigns and earn powerful
  rewards.`

## Verification

Focused player-facing evidence is recorded in
`../verification/RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md`.

The current full verification found a separate headless-policy defect:
automated Night resolution can buy a Home item and then grant itself manual
Lights Out. This does not affect player-controlled Night, but it blocks current
balance simulation until repaired and rerun. See
`../verification/FULL_VERIFICATION_2026-08-07_30214B7F.md`.
