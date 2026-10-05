---
name: officewars-plan
description: Continue OfficeWars game-design and balance planning from the repository's durable design document and balance ledger. Use when the user asks to resume, brainstorm, critique, compare, balance, or plan OfficeWars mechanics, tasks, traits, managers, progression, economy, stress, pacing, simulation targets, or the gameplay loop.
---

# OfficeWars Planning

## Load Context

1. Locate the active OfficeWars workspace root from the current working
   directory. Require `AGENTS.md`, `officewarsautobattler.html`,
   `docs/GAME_DESIGN.md`, and `docs/BALANCE_LEDGER.md`. Do not resolve project
   files relative to the installed skill directory.
2. Read `AGENTS.md`.
3. Read `docs/GAME_DESIGN.md` and `docs/BALANCE_LEDGER.md` completely.
4. Treat `officewarsautobattler.html` as the implemented truth. Inspect only
   the relevant sections when a question depends on current code.
5. Treat the ledger as the decision-status truth. Do not infer that a draft is
   approved because it appears in a prior plan.

## Continue Planning

1. Identify the user's requested topic.
2. Briefly summarize the locked decisions and open questions relevant to that
   topic. Do not repeat the whole ledger unless requested.
3. Resolve discoverable implementation facts from the HTML before asking the
   user.
4. Offer a concrete recommendation with its balance or design rationale.
5. Ask no more than three material questions at once. Prefer structured choices
   when the current client supports them.
6. If the user pauses, dismisses, or leaves a question unanswered, stop and
   leave it open. Never apply a recommended default silently.

## Maintain Decision Status

- Mark a choice `Locked` only after the user explicitly selects, approves, or
  locks that specific choice.
- Treat a direct answer to a focused decision question as approval of that
  choice unless the user says the discussion is exploratory.
- Do not lock adjacent recommendations that the user did not address.
- When a newer decision replaces an older one, keep the active ledger concise
  and add only useful historical context to
  `docs/ARCHIVE_SUPERSEDED.md`.
- When the user approves a decision and file edits are permitted, update
  `docs/BALANCE_LEDGER.md` in the same task.
- If the active collaboration mode forbids edits, report the exact ledger update
  that remains pending.
- Update `docs/GAME_DESIGN.md` only for stable system-level changes, not every
  numeric experiment.

## Boundaries

- Keep planning separate from implementation.
- Use `$officewars-qa-cleanup` for active-document and package cleanup. Use
  `$officewars-full-verification` for exhaustive release verification. Do not
  absorb either workflow into this planning skill.
- Do not edit the game HTML during brainstorming or balance discussion.
- Implement gameplay only when the user explicitly requests implementation and
  the active collaboration mode permits it.
- Preserve the standalone-HTML and office-friendly AFK constraints.
- Check every recommendation for interactions with stress scaling, deadlines,
  rarity, rival pacing, manager rules, Home choices, and existing traits.
- Do not resurrect rejected ideas without explaining why new information makes
  reconsideration worthwhile.

## Current Repository Phase

- The active HTML implements Workday and Office Politics Phases 1-5 at
  SHA-256
  `4BBE884285DF98DB6F7D0C98FC92B9A44464280C86D5A7BBECFE56F2316F2EA9`.
- Implemented systems include the fixed calendar, Overdelivery, transparent
  Chad, deterministic manager packages, cinematic chronological politics,
  dynamic rosters, Relationship, standing, invitations, loyalty, Alumni,
  campaigns, Favors, path-aware progression, fifty cards, rewards, Deals,
  Closing, Brand Strategy, Weekends, and deterministic restoration.
- The seven-Home, 29-item, nine-set, and 24-cell Cash Jar redesign is Locked
  and canonically recorded but unimplemented.
- The deterministic twelve-event Galactic Weekend replacement table is
  Locked and canonically recorded. Galactic Investment and Galactic Gambler
  exact values remain Draft; Galactic Property Rights is Locked and uses a
  frozen active-item morning snapshot.
- Guided Intern is Locked and unimplemented. It follows the Home gate so it
  teaches the final catalog and Night model.
- House deposits, deposit caps, rarity odds, and floor salary remain Draft
  simulation inputs.
- Home, Cash Jar, Guided Intern, accessibility, simulation, tuning, and human
  evidence are Not Run.
- Read `docs/HANDOFF.md` for current phase and
  `docs/BALANCE_LEDGER.md` for exact mechanics and status.

## Useful Invocations

- `$officewars-plan Continue the Coding traits.`
- `$officewars-plan Review the task-card balance proposals.`
- `$officewars-plan Summarize what is locked and what still needs decisions.`
