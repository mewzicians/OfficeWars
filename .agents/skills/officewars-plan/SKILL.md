---
name: officewars-plan
description: Continue OfficeWars game-design and balance planning from the repository's durable design document and balance ledger. Use when the user asks to resume, brainstorm, critique, compare, balance, or plan OfficeWars mechanics, tasks, traits, managers, progression, economy, stress, pacing, simulation targets, or the gameplay loop.
---

# OfficeWars Planning

## Load Context

1. Read `/AGENTS.md`.
2. Read `/docs/GAME_DESIGN.md` and `/docs/BALANCE_LEDGER.md` completely.
3. Treat `/officewarsautobattler.html` as the implemented truth. Inspect only
   the relevant sections when a question depends on current code.
4. Treat the ledger as the decision-status truth. Do not infer that a draft is
   approved because it appears in a prior plan.

Resolve paths relative to the repository root containing this skill.

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
  contextual first-day orientation. Its relationship copy, two-way manual
  Lights Out purchase rule, active Campaign status band, consolidated player
  project HUD, and synchronized Workday ticker are current at SHA-256
  `30214B7FFF8FB4ED44690B90B64EE991E8F300ACE1A4E66E9100BBDAFCC81D12`.
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
- The current hash passes focused smoke, persistence, automated, advanced, and
  17-case visual checks. Read
  `/verification/RELATIONSHIP_NIGHT_CAMPAIGN_UI_2026-08-07.md` for current-hash
  presentation and regression evidence,
  `/verification/WORKDAY_TICKER_SYNC_2026-08-07.md` for the preceding ticker
  snapshot,
  `/verification/PROJECT_HUD_CONSOLIDATION_2026-08-07.md` for the preceding
  HUD snapshot,
  `/verification/PERSISTENCE_TUTORIAL_2026-08-07.md` for the preceding
  persistence and orientation snapshot,
  `/verification/PLAYBACK_SPEED_CONTROL_2026-08-07.md` for the preceding speed
  snapshot, and
  `/verification/FULL_VERIFICATION_2026-08-07_30214B7F.md` for the current
  Pass, Fail, Not Run, and Blocked matrix.
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

## Planning Shorthand

- Treat `<family> review` as a request for a preliminary review of that
  family's complete card roster before the final all-card simulation.
- Test every card against standalone value, family identity, conditional
  synergy, floor pacing, stress, deadlines, rival pressure, managers, Home
  upgrades, all locked trait paths, additional-card rules, and card-repeat or
  multiplier systems.
- Lead with candid, prioritized findings in a senior autobattler set-designer
  voice. Separate numeric concerns from rules contradictions and implementation
  dependencies.
- Do not reopen or change a locked card merely because it appears on a
  watchlist. Recommend a change only when the preliminary review finds a
  concrete failure, and wait for explicit approval before recording it.
- All five ordinary family rosters and their qualitative cross-family review
  are complete. Preserve the Locked roster and simulation watchlist. Defer
  final numeric tuning until implementation is accurate and structural values
  are settled.
- Treat `qa cleanup` as a full active-document verification pass:
  1. Read every active OfficeWars design document, handoff, decision-gate file,
     implementation plan, verification checklist, repository instruction, and
     portable copy.
  2. Compare planning status with `GAME_DESIGN.md`, `BALANCE_LEDGER.md`, and the
     implemented HTML. Keep old behavior only when clearly labeled as the
     current Implemented Baseline.
  3. Rewrite, consolidate, move, or remove completed planning steps,
     superseded mechanics, duplicated explanations, and contradictory
     instructions. Do not append audit notes onto stale sections. Active
     documents should become shorter and clearer wherever possible.
  4. Add only concise, useful historical context to
     `ARCHIVE_SUPERSEDED.md`. Keep transient verification output in the final
     response instead of turning it into design documentation.
  5. Verify Locked, Draft, and Open labels; the 50-card family and rarity
     counts; active file references; portable-copy equality; and documented
     hashes.
  6. Do not edit gameplay code during this cleanup unless the user separately
     requests implementation.
- Treat `full verification` as the exhaustive implementation audit defined in
  `AGENTS.md`. Rebuild traceability from all active sources instead of trusting
  a pre-existing checklist, run every applicable verification layer, and
  report Pass, Fail, Not Run, or Blocked with evidence for every requirement.
