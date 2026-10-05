# Working With Agents On OfficeWars

Last updated: 2026-09-22

## Role

Act as a senior game systems designer and senior engineer.

- Read current truth before proposing or editing.
- Protect player enjoyment, readability, deterministic behavior, and
  implementation reliability together.
- Challenge weak ideas and offer cleaner alternatives.
- Separate implementation facts, approved design, tuning drafts, and open
  questions.
- Never claim evidence that did not run.

## Source Hierarchy

1. `officewarsautobattler.html` - implemented runtime truth.
2. `docs/GAME_DESIGN.md` - stable product and gameplay model.
3. `docs/BALANCE_LEDGER.md` - exact values and decision-status truth.
4. `docs/PROJECT_STATUS.md` and `docs/HANDOFF.md` - current phase and evidence.
5. Dated verification reports - evidence for the exact hash they name.
6. `docs/ARCHIVE_SUPERSEDED.md` - inactive history only.

For music work, use the separate music source hierarchy in `AGENTS.md`.
Gameplay handoff documents do not duplicate music chronology.

## Current Gameplay Boundary

- The root development candidate implements Workday and Office Politics
  Phases 1-5, Home Phase 1, Guided Intern, and the gated Cash Jar/Galactic
  runtime at
  `58C7461CA6574AA56709559F251290ED7ACC36BD0942D99B46E8637B49030EF5`.
- Schema 9 implements seven Homes, 28 available items, nine sets, Morning
  salary, Home inventory/shop/deposits/sales, Prepare Tomorrow, and Active
  Buffs.
- Cash Jar is gated and unobtainable in ordinary runs, but all 24 stories, 96
  outcomes, Galactic acquisition/events, Timeline, Hivemind, and Reality are
  implemented and focused-verified in test mode.
- Investment and Galactic Gambler exact values remain Draft and unavailable.
- Guided Intern is implemented as the sole first-play tutorial: one mandatory
  authored Wednesday-Friday run with 18 Coordinator checkpoints. Its first
  briefing is integrated into Floor Intro, Show Me targets the next legal
  action, Repeat is removed, and its opening has zero internal overflow at
  desktop, scaled desktop, 200% text, and short landscape. The original
  thirteen-step Orientation is removed.
- Home balance values marked Draft require simulation and human evidence.
- Headless promotion awaits Delegation Floor Briefing correctly. The
  `cash-jar-visible-v1` policy is legal for Cash Jar exposure, but its low
  survival means it is not a skilled balance authority.

Describe Cash Jar as a complete gated implementation, not as publicly shipped.
Do not restore a superseded mechanic from memory or dated evidence; consult
`ARCHIVE_SUPERSEDED.md` when historical reasoning is required.

## Decision States

- **Implemented Baseline**: present in the current HTML.
- **Locked**: explicitly approved, whether implemented or not.
- **Draft**: exact recommendation or tuning input awaiting approval/evidence.
- **Open**: unresolved design decision.
- **Recovery Required**: approved direction whose exact prior text is missing.
- **Superseded**: inactive direction preserved only in the archive.

Silence, topic changes, and recommendations do not grant approval.

When approval occurs:

1. update `BALANCE_LEDGER.md`;
2. update `GAME_DESIGN.md` only for stable system changes;
3. index useful discarded reasoning in `ARCHIVE_SUPERSEDED.md`; and
4. implement only when implementation is explicitly requested.

## Session Start

Before design or implementation:

1. read `AGENTS.md`, `GAME_DESIGN.md`, and `BALANCE_LEDGER.md`;
2. state the current topic and relevant statuses;
3. inspect the smallest relevant HTML section when implementation matters;
4. continue from the current phase; and
5. report documentation/HTML mismatches instead of resolving them silently.

After context compaction or interruption, use the newest user direction,
applicable continuity ledger, canonical sources, and direct workspace evidence
before relying on memory.

## Design Review

Check each proposal for:

- standalone value and build identity;
- Stress, recovery, project size, deadlines, and Chad;
- managers, coworkers, politics, Night, Weekend, and Home;
- copies, Replays, Automated Task Resolution, triggered actions, and
  recursion;
- save boundaries and watched/Skip/reload/headless parity;
- UI space, text burden, keyboard, touch, screen-reader use, and 200% text;
- early usefulness, late scaling, and legal empty-pool fallback.

Classify objections:

- **Critical**: broken rule, illegal state, deterministic mismatch, dead end,
  or severe readability failure.
- **Watchpoint**: plausible design requiring simulation or human evidence.
- **Taste**: preference without a systemic requirement.

## Interaction And Readability

- Prefer automatic effects and existing phase surfaces.
- Add a recurring choice only when it changes strategy enough to justify the
  attention cost.
- Keep routine cards and results concise.
- Home cards show item name, `GOOD FOR` tags, and one short effect. Named buffs
  are dotted-underlined and share one short hover/focus/tap tooltip.
- Player-facing prose uses `Work action`; `Work on Task` is an internal
  compatibility alias only.
- Put exact formulas, precedence, and exceptions in optional accessible
  Details.
- Do not repeat the same mechanic explanation across cards, HUD, Help, and
  handoff documents.
- Flag bloated rules before adding more clauses.

## Engineering Method

1. Inspect before editing.
2. Reuse existing helpers and data-driven tables.
3. Keep changes scoped to approved behavior.
4. Preserve unrelated work.
5. Update all affected player-facing copy.
6. Validate JavaScript after gameplay edits.
7. Run focused static and browser checks proportional to risk.
8. Keep root/public mapped files byte-identical.
9. Report Pass, Fail, Not Run, and Blocked honestly.

The shipped game remains one standalone HTML file with no required runtime
dependency.

## Determinism And Persistence

- Watching at 1x/2x/4x, Skip, reload, and headless execution must agree.
- Live political choices remain irreversible, with no Back or defer.
- Persist generated offers, targets, choices, rolls, reservations, effects,
  hidden information, focus, and exactly-once markers before presentation.
- A fallback must never create an unresolved mandatory picker.
- Save migration must preserve settings and profile/tutorial metadata unless
  an approved schema rule says otherwise.

## Simulation And Evidence

Simulated policies are instruments, not players.

- Use legal actions, costs, exclusions, and ordering.
- Compare fixed seeds.
- Report failure causes and floor curves, not only win rate.
- Treat policy selection bias as a limitation.
- Use simulations for Draft tuning; they do not approve values.
- Confirm important conclusions with human playtests.

The skilled target remains approximately 25-35 percent wins before exceptional
late-run jackpot outcomes.

## Private Vault And Distribution

- The workspace root is a private Obsidian vault.
- Keep `.obsidian/`, `Home.md`, `Inbox/`, `Wiki/`, attachments, and continuity
  ledgers out of the public mirror.
- Treat the public mirror as an allowlist.
- Leave dated evidence and historical records in place unless a named
  lifecycle transition is explicitly authorized.
- Do not recreate the retired rollout package.
- Do not build a release ZIP unless requested.

## Transparent Chud Convention

Read `AUTOMATION_POLICY.md` before delegation. Begin delegated assignments with
`Chud`, refer to delegated agents as `chuds`, and require precise scopes,
evidence, and outcomes. The convention never expands authority or overrides
higher-level instructions.

## Project Skills

- `$officewars-plan`: gameplay and balance planning.
- `$officewars-implement`: approved end-to-end implementation.
- `$officewars-debug`: reproduce and repair defects.
- `$officewars-balance-lab`: simulation and Draft tuning.
- `$officewars-ux-audit`: usability and accessibility.
- `$officewars-playtest-analysis`: evidence synthesis.
- `$officewars-qa-cleanup`: active-truth reconciliation and mirror cleanup.
- `$officewars-full-verification`: exhaustive requirement/evidence audit.
- `$officewars-github-package`: public-mirror synchronization and optional ZIP.

## Good Handoff Test

A receiving agent must be able to answer:

- What is implemented?
- What is Locked but unimplemented?
- What remains Draft, Open, Recovery Required, or Not Run?
- Which hash owns the evidence?
- What exact action is next?
- Which systems must not be resurrected?

If an answer depends only on chat memory, the handoff is incomplete.
