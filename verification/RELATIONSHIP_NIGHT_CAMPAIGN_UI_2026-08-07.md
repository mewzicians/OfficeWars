# Relationship, Night, And Campaign UI Verification

Date: 2026-08-07

Game SHA-256:
`30214B7FFF8FB4ED44690B90B64EE991E8F300ACE1A4E66E9100BBDAFCC81D12`

Result: **PASS for player-facing scope**

## Verified Behavior

| Requirement | Status | Evidence |
|---|---|---|
| Relationship copy is concise | **Pass** | Runtime surface audit shows the actual bonus without the removed scaling labels |
| Outings explain Workday bonuses | **Pass** | Runtime surface audit finds the new footer sentence |
| Lights Out blocks Home and Deal purchases | **Pass** | Runtime assertion disables both purchase categories and their cards |
| A purchase blocks manual Lights Out | **Pass** | Runtime assertion disables the toggle and rejects direct activation |
| Moodboard exception remains legal | **Pass** | Runtime assertion permits purchases while automatic Lights Out is active |
| Legacy inconsistent Night saves normalize | **Pass** | Restore code preserves purchases and clears manual Lights Out |
| Lights Out suppresses illegal purchase warnings | **Pass** | Finalization warns only for still-legal unused actions and resources |
| Campaign status band | **Pass** | Runtime and visual checks show name, requested card and family, `2 OF 3 STEPS`, and Campaigns completed |
| Rebrand Initiative copy | **Pass** | The implemented Special card matches the approved sentence exactly |

## Regression Evidence

- `python .officewars-smoke-run.py`: `PASS:OVERHAUL`.
- `python .officewars-persistence-verify.py`: all 23 checks passed.
- `python .officewars-advanced-verify.py`: all eight high-risk groups passed.
- `python .officewars-full-verify.py 0`: all player-facing checks passed; the
  separate simulation-policy parity check failed as documented below.
- `python .officewars-visual-capture.py`: all 17 cases passed with no sampled
  clipped text, viewport overflow, persistent-HUD overlap, or incoherent visual
  overlap.

Representative desktop, compact desktop, landscape phone, portrait rotation,
Campaign, Resume, Workday, Clock Out, ordinary Night, Lights-Out Night, and
200-percent text cases were exercised. Direct screenshot inspection found no
unreadable or overlapping primary decision surface.

## Out-Of-Scope Finding

The headless Night policy does not use the same choice restriction as the
player. It can purchase a Home item and then set manual Lights Out. Current
balance simulation is therefore Blocked, not part of this focused UI Pass.
Exact evidence is in
`FULL_VERIFICATION_2026-08-07_30214B7F.md`.
