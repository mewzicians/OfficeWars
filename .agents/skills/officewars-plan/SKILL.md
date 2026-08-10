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
  `/docs/ARCHIVE_SUPERSEDED.md`.
- When the user approves a decision and file edits are permitted, update
  `/docs/BALANCE_LEDGER.md` in the same task.
- If the active collaboration mode forbids edits, report the exact ledger update
  that remains pending.
- Update `/docs/GAME_DESIGN.md` only for stable system-level changes, not every
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

- The active HTML contains the approved rollout, readability candidate,
  cycling playback-speed update, versioned active-run persistence, and
  thirteen-step contextual orientation. Its relationship copy, two-way manual
  Lights Out purchase rule, active Campaign status band, consolidated player
  project HUD, synchronized Workday ticker, reusable task-picker cards, and
  Automation Skill-XP exception, grounded Home scene, and no-crossing
  celestial sequence are current at SHA-256
  `470F4146FBA177FD6B7062A0093DDCF7C2826B797FE9AE74317BD1D146050FF7`.
- Do not restart or reimplement the overhaul from the rollout plan unless a
  verified finding requires a fix.
- The first full bidirectional verification ran on 2026-08-06 and failed ship
  signoff. Read `/verification/FULL_VERIFICATION_2026-08-06.md` before fixing
  or tuning the candidate.
- Findings F1-F4 are resolved and passed the focused retest in
  `/verification/BLOCKERS_1_4_RETEST_2026-08-06.md`.
- All eight targeted high-risk interaction groups passed the deterministic
  suite recorded in
  `/verification/ADVANCED_INTERACTION_VERIFICATION_2026-08-06.md`.
- The deterministic Skip repair and expanded browser suite passed local
  validation on 2026-08-07. Read
  `/verification/SKIP_FIX_LOCAL_VALIDATION_2026-08-07.md` for that snapshot's
  evidence and cross-version simulation comparison.
- The current hash passes smoke, persistence, automated, advanced, and 29-case
  visual checks. Read
  `/verification/FULL_VERIFICATION_2026-08-10_55D9A6ED.md` for the current
  Pass, Fail, Not Run, and Blocked matrix. Earlier dated reports remain
  evidence only for their named hashes.
- The player-facing Night rule passes, but the headless Night policy grants
  manual Lights Out after purchasing. Current balance simulation is therefore
  Blocked. The prior 58.4 percent scripted-skilled result is historical
  snapshot telemetry, not current balance evidence.
- Balance finding F5, structural tuning, explicitly unverified rows, human
  evidence, and the deferred Home set design remain unfinished.
- Read `/docs/HANDOFF.md` for current implementation status and
  `/docs/BALANCE_LEDGER.md` for exact mechanics and decision status.

## Useful Invocations

- `$officewars-plan Continue the Coding traits.`
- `$officewars-plan Review the task-card balance proposals.`
- `$officewars-plan Summarize what is locked and what still needs decisions.`
