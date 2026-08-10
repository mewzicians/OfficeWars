# Night, Resume, And Automation UI Patch

Date: 2026-08-10

Implemented game SHA-256:
`90A06E921AF33D6F7BE8D5F3EC4A12FE8FFD72419AA13A299720809FEB0685EC`

## Implemented

- Night shows prominent green Cash and yellow Expense Credit.
- Home capacity is represented by visual item slots. Occupied slots expose
  their description to hover, focus, and tap and open a sell confirmation.
- The Night footer forecasts final Stress with a bar and exact values. Routine
  action-availability prose was removed; existing warnings still catch skipped
  legal actions.
- Resume family dividers were removed. Milestones use a green outline before
  reaching them, a highlighted `!` while awaiting Promotion Review, and a green
  checkmark after being claimed.
- Automation Combo separates task cards from commands. End Combo and daily,
  banked, and paid rerolls appear before the cards in landscape layouts.
- Combo rerolls replace all three slots without advancing Combo. Paid rerolls
  remain a 6 XP unlock and cannot show Legendary cards.

No save migration was required. The game remains one standalone HTML file.
