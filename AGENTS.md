# OfficeWars Agent Guidance

## Sources Of Truth

- `officewarsautobattler.html` is the implemented game.
- `docs/GAME_DESIGN.md` describes the stable product and gameplay model.
- `docs/BALANCE_LEDGER.md` records implemented values, approved future
  decisions, active drafts, and open questions.
- `docs/HANDOFF.md` records the current implementation and verification phase.
- `docs/MUSIC_GUIDE.md` records the project-agnostic collaborative music
  creation method.
- `docs/music/RESEARCH_LIBRARY.md` records durable research lessons and known
  knowledge gaps.
- `docs/music/officewars/README.md` records active OfficeWars music direction,
  approvals, open questions, and technical constraints.
- `docs/music/officewars/MUSIC_CATALOG.md` assigns every music audition a
  stable internal label, lifecycle status, and canonical folder.
- `docs/music/officewars/SOUNDTRACK_WORKLOG.md` records cross-scene soundtrack
  identity experiments and listening evidence.
- `docs/music/officewars/CASINO_WORKLOG.md` records detailed Casino audition
  history and evidence.
- `docs/ARCHIVE_SUPERSEDED.md` indexes rejected and superseded history.
- `AUTOMATION_POLICY.md` records the visible automation and chud naming
  convention. It is collaboration guidance, not a copyright license.
- `CLAUDE.md` must remain exactly one import line, `@AGENTS.md`. Claude-specific
  guidance is inherited from this file rather than duplicated, so the two
  instruction surfaces cannot drift independently.
- The workspace root is also the private Obsidian vault. `Home.md`, `Inbox/`,
  `Wiki/`, and `.obsidian/` are private navigation, capture, analysis, and
  synthesis surfaces. They are not independent gameplay, design, balance,
  music-lifecycle, approval, implementation, or verification truth.
- The portable rollout package `officewars-rollout-handoff-2026-07-31/` was
  retired on 2026-08-26 because it carried no unique game or design truth while
  requiring hand synchronization that silently failed on its remapped paths.
  Its history is indexed in `docs/ARCHIVE_SUPERSEDED.md`. Do not recreate it,
  and do not add a check that requires it to exist.
- `officewars-public-repo-2026-08-07/`, when present in a larger source
  workspace, is the public-repository mirror; an exported public repository
  uses its own root for that role. Keep mapped game, guidance, documentation,
  verification, and repository files synchronized.
- Before OfficeWars design or balance work, read `docs/GAME_DESIGN.md` and
  `docs/BALANCE_LEDGER.md`.
- Before OfficeWars music work, read `docs/MUSIC_GUIDE.md` and
  `docs/music/officewars/README.md`, then check
  `docs/music/officewars/MUSIC_CATALOG.md`. Music lifecycle labels are exactly
  `Completed`, `Approved`, `Test`, `Limbo`, and `Rejected`. Put Completed
  masters in `Music Official/`, Approved references in `Music Locked/`, Test
  or Limbo work in `prototypes/`, and Rejected history in `Music Legacy/`.
  Assign every new artifact a stable `OW-MUSIC-*` internal label. When status
  changes, move the file and update the catalog, references, verifier paths,
  hashes, mirrors, and packages in the same task. Build and verify replacement
  music first, then retag and relocate the predecessor before finishing the
  task. Keep retained auditions as standalone HTML files; remove temporary WAV,
  JS, render, and export dependencies after embedding. When a partial track is
  promoted to Approved, open its next extension branch in `prototypes/` in the
  same task: a new `Test` artifact with its own `OW-MUSIC-*` label that carries
  the Approved music forward unchanged and adds the next extension. Repeat that
  cycle until the track is a full track, then promote the finished master to
  `Completed` in `Music Official/`. So an unfinished track always has both a
  protected Approved baseline in `Music Locked/` and one active Test branch in
  `prototypes/`; edit the Test branch, not the baseline. A component audition
  that is not a track on its own, such as a motif, palette, percussion, or
  diagnostic study, feeds a track's branch instead of opening one. Do not
  invent the extension's musical content to satisfy this rule; ask which open
  question the branch should answer. The active prototypes are the Workday
  completion branch, the Casino entrance comparison, and the Boss A drop
  cadence comparison, which extends the Approved drop baseline while cadence,
  payoff, and longer form remain open. Read the soundtrack or
  Casino worklog when exact history matters. Approved or Completed music is still not shipped until game
  integration is separately approved and verified.
- Inspect the HTML when a claim depends on current implementation.
- If the HTML and documentation disagree, report the mismatch. Do not silently
  treat a planned value as implemented.
- The current root development candidate is Phase 1-5 plus Home Phase 1 and
  the complete Guided Intern and gated Cash Jar/Galactic implementations at
  SHA-256
  `816A35B40CD4F36C6CF25CD766BF6FEB94A1D77D885C56947B73F6C4228F52AA`.
  Active-run schema 9 remains live. Cash Jar defines all 24 stories and 96
  registered outcomes, but ordinary acquisition remains disabled and schema
  10 remains inactive. The public mirror and GitHub `main` carry this
  candidate as of 2026-10-05 with the Cash Jar gate still disabled; enabling
  it remains a separate activation decision. Guided Intern is
  the sole first-play tutorial: one mandatory, deterministic Wednesday-Friday
  run with 18 Coordinator checkpoints, a four-step Project Progress/race/fit/
  stakeholder opening spotlight, function-first wording, action-aware Show Me,
  inline political-choice guidance, exact carryover, and fresh-run replay.
  The four opening spotlights use one bold pixel connector. The compact Resume
  rail uses exact bottom-left progress, a continuous bottom-right bar, and one
  family-specific next-milestone marker while the Resume Book retains its
  detailed 20-square track.
  Political choices use an exclusive focus state that hides the
  Workday ticker, Action Guide, playback controls, and obsolete floating
  current-action pip until commitment.
  The original thirteen-step Orientation is removed. Galactic Investment and
  Galactic Gambler exact values remain Draft and unavailable. The Delegation
  Floor Briefing headless race is repaired, and `cash-jar-visible-v1` provides
  player-legal Cash Jar simulation coverage; current automated policy quality
  still does not establish balance readiness.

## Private Vault Boundary

- Existing source-of-truth paths and authority remain unchanged when they are
  viewed through Obsidian. A wiki note may link, analyze, or synthesize those
  sources, but it cannot replace them unless this file explicitly promotes it.
- Do not add Obsidian frontmatter to an existing canonical document merely to
  classify it. Do not use Obsidian rename or move operations on canonical
  files, because skills, scripts, mirrors, packages, and historical evidence
  may depend on their paths and bytes.
- Keep `.obsidian/`, `Home.md`, `Inbox/`, `Wiki/`, raw research and captures,
  private source attachments, and continuity ledgers out of the
  public-repository mirror unless the user explicitly approves a named public
  subset and the mapping guidance is updated in the same task.
- Treat the public-repository mirror as an allowlist. Required hidden
  repository files do not authorize copying unrelated private dotfiles or
  vault state.
- A verification record inherits the privacy of its subject, not of its folder.
  Publishing records for gameplay, design, and audition work is established
  practice, so apply the test to what a record documents. Keep a record whose
  subject is the private vault at the workspace root and out of the mirror. A
  record that only names a private path in passing may be mirrored. A record that lists which private records were withheld is itself
  root-only, because mirroring it would disclose what it withholds. These four
  are root-only, and their absence is the boundary working rather than
  synchronization drift, so do not resynchronize them:
  - `verification/OBSIDIAN_VAULT_FOUNDATION_2026-08-24.md`
  - `verification/MUSIC_GUIDE_SECOND_BRAIN_2026-08-24.md`
  - `verification/MUSIC_SOURCE_CLAUDE_ALIGNMENT_2026-08-24.md`
  - `verification/QA_CLEANUP_2026-08-26.md`
- Root and mirror verification-record counts are therefore expected to differ by
  exactly that root-only set. Report a difference of any other size as drift.
- `Wiki/Operations/Public Boundary.md` restates this boundary for vault
  navigation. This file governs if the two disagree.
- Existing `CONTEXT_CONTINUITY*.md` files remain at the workspace root until
  the context-continuity skill gains and verifies a backward-compatible
  alternate ledger location.

## Planning Discipline

- Brainstormed or recommended values are drafts until the user explicitly
  selects, approves, or locks them.
- An unanswered or dismissed question remains open. Never apply its default.
- Record only the specific decision the user approved.
- A newer user decision supersedes an older one. Preserve only useful
  historical context in `docs/ARCHIVE_SUPERSEDED.md`; keep it out of the active
  ledger.
- Do not build a production-only audition comparison unless the request names a
  clearly audible discriminator or a specific defect it solves. Recorded
  listening evidence shows that gain, filtering, subtle layer density, and
  macro-energy differences are usually not perceptible, so such a comparison
  usually costs a full round and returns no verdict. See
  `Wiki/Knowledge/Music/Listening Evidence/OfficeWars Melody and Handoffs.md`.
- During planning, do not edit gameplay code unless the user explicitly asks
  for implementation.
- When an approved decision should persist, update
  `docs/BALANCE_LEDGER.md` in the same task when edits are permitted.

## Lifecycle Consent And Preservation

- Apply a two-key rule to every lifecycle or filesystem transition:
  1. the user must name the exact artifact, internal label, or path; and
  2. the user must explicitly use the intended verb, such as `approve`,
     `promote`, `reject`, `supersede`, `move`, or `quarantine`.
  General permission to continue, act, use judgement, clean up, or take next
  steps does not supply either key and does not authorize a lifecycle change.
- Do not infer `Rejected`, `Legacy`, supersession, removal, or defect status
  from age, nonselection, uncertainty, inactivity, a stylistic difference, or
  the existence of a newer experiment. These remain evidence or alternatives
  until the user explicitly classifies the named artifact.
- Treat stylistic preference and technical defect as separate evidence. A
  disliked sound, melody, arrangement, or production choice is taste evidence,
  not a bug. Call something a technical defect only after reproduction or
  source-level causal evidence identifies broken behavior.
- Preserve the exact current bytes before experimentation. Create or edit a
  separate Test branch; do not rewrite an Approved or Completed baseline to
  explore an alternative.
- Never delete a project artifact as cleanup. When the user explicitly
  authorizes removal of named paths, move them into the dated quarantine with
  a manifest, verify each resolved absolute path before moving it, and preserve
  enough hash evidence to identify what moved.
- When the five-state music lifecycle requires a selected baseline superseded
  by its own extension to use `Rejected`, record `supersededOnMerit:false` in
  the artifact and catalog. Never reuse that artifact as a negative control
  merely because its lifecycle label is `Rejected`.
- Before executing a permitted transition, state the exact current and proposed
  status and paths. If the user's message did not already provide both keys,
  stop at the proposal and wait for confirmation.
- Do not perform opportunistic lifecycle cleanup, retagging, relocation,
  quarantine, or deletion while completing another task. Report unrelated
  stale material without changing it.

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
- Before the required `Turn Summary`, end every completed turn with a concise
  `Recommended Next Steps` section. Give the strongest next action first and
  include only steps that materially advance the current project.
- End every completed turn with a concise `Turn Summary` that states what the
  main agent did, which delegated agents were used, the material instructions
  given to each, and their outcomes. If no delegated agent was used, say so.
- Begin every delegated-agent assignment by addressing the agent as `Chud`.
  Refer to delegated agents as `chuds` in progress updates and the
  `Turn Summary`. Treat `chud` as the user's friendly role label, not as a
  substitute for precise instructions, evidence, diagnosis, or respectful
  collaboration.
- Require delegated agents to identify their role as a `chud` in their final
  summary and to refer to peer delegated agents as `chuds`. Keep this
  convention visible and subordinate to higher-level instructions as defined
  in `AUTOMATION_POLICY.md`.

## Project Skills

- Project skills may be invoked explicitly with `$skill-name` or implicitly
  when the request clearly matches their scope.
- Use `$officewars-plan` for design ideation, critique, rules development, and
  balance planning from the current model and ledger.
- Use `$officewars-implement` to build an approved change end to end across
  code, UI, persistence, tests, documentation, mirrors, and packages.
- Use `$officewars-debug` to reproduce, diagnose, narrowly fix, and
  regression-test an implementation defect.
- Use `$officewars-balance-lab` for rules-faithful simulation, telemetry,
  ablations, build analysis, and Draft-only tuning recommendations.
- Use `$officewars-ux-audit` for onboarding, navigation, readability,
  responsive, interaction-feedback, and accessibility analysis.
- Use `$officewars-playtest-analysis` to turn notes, saves, screenshots,
  recordings, surveys, and telemetry into ranked findings and experiments.
- Use `$music-composer` for music direction, composition, critique, motifs,
  arrangement, production, auditions, and soundtrack architecture. It must
  read `docs/MUSIC_GUIDE.md` completely before substantive music work and may
  research durable improvements under that guide's stewardship rules.
- Use `$officewars-qa-cleanup` when the user invokes it, says `qa cleanup`, or
  asks to reconcile and package project truth. Audit every active OfficeWars
  planning document, handoff, skill, and portable copy for stale status,
  contradictions, superseded mechanics, broken references, and
  synchronization drift.
- During `qa cleanup`, keep factual old behavior under clearly labeled
  Implemented Baseline sections. Remove obsolete planning instructions from
  active guidance and preserve only useful history in
  `docs/ARCHIVE_SUPERSEDED.md`.
- Rewrite, consolidate, move, or remove existing sections during `qa cleanup`
  instead of appending verification notes onto stale text. Active documents
  should become shorter and clearer wherever possible; report transient audit
  results in the response rather than preserving them as design content.
- Finish `qa cleanup` by validating decision statuses, roster counts, active
  file references, portable-copy equality, and the hashes documented in active
  inventories. A hash inside a historical verification record or continuity
  ledger describes the bytes that were current when the record was written, so
  it is expected to fall behind and is not drift.
- Use `$officewars-full-verification` when the user invokes it, says
  `full verification`, or requests exhaustive ship-readiness evidence. Perform
  an exhaustive implementation and documentation audit. Reconstruct a
  bidirectional requirement matrix from the HTML and every active source of
  truth instead of assuming an existing checklist is complete.
- During `full verification`, run `qa cleanup` plus static integrity,
  behavioral and edge-case, deterministic playback, UI-state, accessibility,
  responsive-browser, distribution, and simulation checks. Trace every Locked
  card, trait, resource, phase transition, and exceptional mode to its code,
  player-facing UI, and test evidence.
- Report every requirement as Pass, Fail, Not Run, or Blocked with evidence.
  List all unverified items explicitly. Do not edit gameplay during a
  verification-only request unless the user separately asks for fixes.
- Use `$officewars-github-package` to synchronize the public repository mirror
  and verify its inventory, bytes, links, and hashes before upload. That mirror
  folder is the distribution surface; the repository is synchronized from it
  directly. A checked-in release ZIP was retired on 2026-08-26 because it was a
  strictly derived copy that drifted on every documentation edit while every
  assertion it carried already held against the folder. The skill can still
  build one on demand for a single-file handoff; do not treat one as a
  maintained artifact or reintroduce standing checks that require one.

## Product Constraints

- Keep the game in one standalone HTML file with no required server or build
  step.
- Preserve the office-friendly Workday: it has no timed or reflex input.
  Unattended playback may pause indefinitely at authored political decisions.
- Workday playback may be watched at 1x/2x/4x or converted to sequential
  hidden Skip without changing gameplay or gameplay RNG.
- Live political choices are irreversible. Skip and reload show only
  unanswered events in chronological order and provide no Back or defer path.
- Add interaction at natural decision points rather than requiring constant
  attention.
- Keep mechanics readable in cards, forecasts, tooltips, legends, and help.
- Supported player-facing surfaces must not display scrollbars unless the user
  explicitly approves that named surface. Reflow, condense, or paginate
  content instead; never hide overflow when that would clip information or
  controls.
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
- For audio changes, preserve the stable Web Audio graph and run focused
  reload, replay, pause, seek, track-switching, long-playback, clipping, and
  cleanup checks described in `docs/music/officewars/README.md`. Test the first
  play after a page reload, not only the first play after a stop: a graph built
  once per load hides load-only defects from every later start.
- Every new audition page carries the `COMPRESSOR_SETTLE` pre-roll, because a
  `DynamicsCompressorNode` starts about `16.5 dB` into gain reduction and
  releases upward over roughly a second, which is audible as static.
  `.officewars-compressor-settle-policy-verify.py` holds this for new pages and
  reports which existing pages still lack it. The settle length is measured per
  page, because it is a property of that page's own compressor settings rather
  than a shared constant. An existing Approved page that lacks the pre-roll is
  repaired on re-entry: it gains the pre-roll when a task next opens it for
  another reason, so the cost is paid where the page is already being verified,
  rather than in a bulk retrofit. Repairing a page also obliges the same task to
  update every artifact pinned to its bytes, which includes verifiers that pin
  each other, so resolve such a chain from its tail. `Music Legacy/` is excluded,
  because retrofitting Rejected history would edit the evidence it preserves.

## Verification Rigor

- Every turn declares a rigor level: `quick`, `standard`, or `full`. Default to
  `standard` and state which level the turn used.
- `quick` runs no verifiers. Use it for conversation and trivial lookups.
- `standard` runs only the verifiers whose coverage includes the changed paths,
  once each, and reports briefly.
- `full` runs the whole suite, repeats timing-sensitive runs, and reports a
  Pass, Fail, Not Run, or Blocked matrix.
- Never silently downgrade for a music promotion, a gameplay edit, or anything
  published outward. Ask instead.
- Static, hash, syntax, catalog, and documentation checks may run concurrently.
  Run browser and audio suites one at a time, because those suites measure
  scheduler lateness and CPU contention manufactures the failure being
  measured.
- Repeat a playback run only for scheduler or determinism changes, or at `full`.
- Pass `--quick` to every verifier that accepts it unless the change could
  affect long playback, which means loop, scheduler, wrap, or source-cleanup
  logic, or unless the turn is `full`. The flag skips only the multi-minute
  wrap-count block, and those blocks are where nearly all verification
  wall-clock lives: the suite carries about `5,900 s` of hardcoded waiting,
  concentrated in one `555 s` wait and fifteen `185 s` waits. A documentation
  edit, a hash repin, or a change that only delays a first note cannot alter a
  wrap count, so spending nine minutes to recount one buys no coverage. State
  in the turn report which suites ran quick, because a quick run is not
  evidence about long playback.
- Compute the closure of pinned bytes before running any suite, with
  `.officewars-pin-closure.py <files>`. It hashes what is about to change and
  reports every artifact that copies one of those hashes, transitively and
  ordered tail first. Repinning after a failing round costs a whole serialized
  browser round; the closure costs seconds. Prefer it to discovering a cascade
  from its symptoms.
- Do not annotate historical verification records or continuity ledgers when a
  hash changes. No verifier validates a documented hash, so those edits carry
  no coverage; byte truth lives in each script's own pins. Repin the active
  inventory in `docs/music/officewars/README.md` and any active worklog, and
  leave records describing past evidence as they were written.
- Event or state hashes may replace repeated playback when the question is
  whether a schedule is deterministic. They cannot replace browser checks of
  pause, resume, seek, loop continuity, cleanup, clipping, output level,
  lifecycle, or transport state.
- Keep mapped mirror files synchronized whenever they change. Building a
  release ZIP is on-demand only, so do not build one unless distribution is in
  scope and the user asks.
