# OfficeWars Agent Guidance

## Read First

Before planning, balancing, reviewing, or implementing OfficeWars:

1. Read `docs/GAME_DESIGN.md`.
2. Read `docs/BALANCE_LEDGER.md`.
3. Read `docs/PROJECT_STATUS.md` and `docs/HANDOFF.md`.
4. Read `docs/WORKING_WITH_AGENTS.md`.
5. Inspect `officewarsautobattler.html` whenever a claim depends on runtime
   behavior.

`officewarsautobattler.html` is implementation truth. The balance ledger is
decision-status truth. If they disagree, report the mismatch instead of
silently choosing one.

## Decision Discipline

- Brainstorms, recommendations, simulations, and playtest observations remain
  Draft evidence until the project owner explicitly approves a decision.
- Never treat silence, a skipped question, or a topic change as approval.
- Record only what was explicitly approved. A newer decision supersedes an
  older one.
- Keep active documents concise. Preserve only useful history in
  `docs/ARCHIVE_SUPERSEDED.md`.
- Keep planning separate from implementation unless implementation is
  explicitly requested.

## Collaboration

- Be candid. Evaluate proposals rather than automatically agreeing with them.
- Label critical objections, tuning watchpoints, and matters of taste
  separately.
- Flag bloated card text, excessive mechanics, unclear interactions, and
  planning that is moving too quickly to verify accurately.
- Ask no more than three focused questions at once.
- Briefly correct genuine spelling mistakes without policing casual shorthand.
- Give concrete alternatives when objecting.

## Product Guardrails

- Preserve one standalone gameplay HTML file with no required server, build
  step, account, or network request.
- Preserve the office-friendly AFK workday. Major decisions belong in Morning,
  Night, Weekend, and Promotion phases.
- Playback speed and Skip must never change outcomes.
- Keep mechanics inspectable through cards, forecasts, tooltips, legends,
  logs, and Help.
- Keep mobile gameplay landscape-first.
- Balance toward approximately 25-35 percent wins for a genuinely skilled
  policy or player.

## Engineering

- Prefer existing helpers and data tables over parallel systems.
- Keep edits scoped to approved behavior and preserve unrelated changes.
- Update every affected card description, tooltip, forecast, legend, Help
  entry, and document when mechanics change.
- Validate JavaScript and run tests proportional to the change.
- Treat the dated verification reports as evidence, not permanent proof after
  the HTML changes.

## Planning Shorthand

- `qa cleanup`: rewrite and consolidate all active sources so current status,
  decision labels, references, portable copies, and hashes agree. Do not append
  audit notes onto stale prose.
- `full verification`: reconstruct the requirement matrix from current sources
  and run applicable static, behavioral, browser, accessibility, distribution,
  and simulation checks. Report Pass, Fail, Not Run, or Blocked.
- `<family> review`: review that complete card family against standalone value,
  identity, trait synergy, floors, stress, economy, managers, and multiplier
  systems.
- `<rarity> <family> card next`: continue the established card-design review
  for that rarity and family.
- `$officewars-plan <topic>`: resume planning from the project skill when the
  receiving agent supports repository skills.
