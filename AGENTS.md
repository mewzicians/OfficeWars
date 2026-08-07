# OfficeWars Agent Guidance

## Sources Of Truth

- `officewarsautobattler.html` is the implemented game.
- `docs/GAME_DESIGN.md` describes the stable product and gameplay model.
- `docs/BALANCE_LEDGER.md` records implemented values, approved future
  decisions, active drafts, and open questions.
- `docs/HANDOFF.md` records the current implementation and verification phase.
- `docs/ARCHIVE_SUPERSEDED.md` indexes rejected and superseded history.
- `officewars-rollout-handoff-2026-07-31/` is a portable mirror, not an
  independent source. Keep its mapped files synchronized with the root.
- `officewars-public-repo-2026-08-07/`, when present in a larger source
  workspace, is the public-repository mirror; an exported public repository
  uses its own root for that role. Keep mapped game, guidance, documentation,
  verification, and repository files synchronized.
- Before OfficeWars design or balance work, read both documents under `docs/`.
- Inspect the HTML when a claim depends on current implementation.
- If the HTML and documentation disagree, report the mismatch. Do not silently
  treat a planned value as implemented.

## Planning Discipline

- Brainstormed or recommended values are drafts until the user explicitly
  selects, approves, or locks them.
- An unanswered or dismissed question remains open. Never apply its default.
- Record only the specific decision the user approved.
- A newer user decision supersedes an older one. Preserve only useful
  historical context in `docs/ARCHIVE_SUPERSEDED.md`; keep it out of the active
  ledger.
- During planning, do not edit gameplay code unless the user explicitly asks
  for implementation.
- When an approved decision should persist, update
  `docs/BALANCE_LEDGER.md` in the same task when edits are permitted.

## Collaboration Preferences

- Proactively flag mechanics or card text that are becoming bloated. Explain
  the specific readability or rules cost and recommend a leaner version.
- Speak up when planning moves to a new card, family, or system before material
  decisions in the current topic are finished.
- Tell the user when the pace is too fast to preserve design coherence, check
  interactions, or document decisions accurately. Invite a pause rather than
  silently following the topic change.
- Keep these interventions candid and concise. They should protect the design
  process without needlessly stopping useful momentum.
- Treat user proposals as ideas to evaluate together, not positions to endorse
  automatically. Before locking a design, proactively state any mechanical,
  balance, readability, implementation, or player-experience reservations.
- Distinguish critical objections from tuning watchpoints and matters of taste
  so the user can judge the severity. Offer stronger alternatives and original
  ideas whenever they would improve the game.
- Briefly correct actual misspellings and obvious typos in each response so the
  user can improve. Do not treat casual capitalization or intentional shorthand
  as spelling errors unless it makes the meaning unclear.

## Planning Shorthand

- Treat `qa cleanup` as a request to audit every active OfficeWars planning
  document, handoff, skill, and portable copy for stale status, contradictions,
  superseded mechanics, broken references, and synchronization drift.
- During `qa cleanup`, keep factual old behavior under clearly labeled
  Implemented Baseline sections. Remove obsolete planning instructions from
  active guidance and preserve only useful history in
  `docs/ARCHIVE_SUPERSEDED.md`.
- Rewrite, consolidate, move, or remove existing sections during `qa cleanup`
  instead of appending verification notes onto stale text. Active documents
  should become shorter and clearer wherever possible; report transient audit
  results in the response rather than preserving them as design content.
- Finish `qa cleanup` by validating decision statuses, roster counts, active
  file references, portable-copy equality, and documented hashes.
- Treat `full verification` as an exhaustive implementation and documentation
  audit. Reconstruct a bidirectional requirement matrix from the HTML and
  every active source of truth instead of assuming an existing checklist is
  complete.
- During `full verification`, run `qa cleanup` plus static integrity,
  behavioral and edge-case, deterministic playback, UI-state, accessibility,
  responsive-browser, distribution, and simulation checks. Trace every Locked
  card, trait, resource, phase transition, and exceptional mode to its code,
  player-facing UI, and test evidence.
- Report every requirement as Pass, Fail, Not Run, or Blocked with evidence.
  List all unverified items explicitly. Do not edit gameplay during a
  verification-only request unless the user separately asks for fixes.

## Product Constraints

- Keep the game in one standalone HTML file with no required server or build
  step.
- Preserve the office-friendly AFK workday: major choices belong in the
  morning, night, weekend, and promotion phases.
- Workday playback may be watched, accelerated, or skipped without changing
  outcomes.
- Add interaction at natural decision points rather than requiring constant
  attention.
- Keep mechanics readable in cards, forecasts, tooltips, legends, and help.
- Balance toward an approximately 25-35 percent win rate for a skilled player.

## Engineering Expectations

- Prefer existing helpers and data-driven tables in the HTML.
- Keep edits scoped to the approved behavior.
- When a mechanic changes, update every affected description, tooltip, legend,
  forecast, comment, and How to Play entry.
- Preserve unrelated user changes.
- Validate JavaScript syntax after gameplay edits.
- For user-facing or systemic changes, run focused browser smoke tests and
  simulations proportional to the risk.
