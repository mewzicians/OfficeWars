---
name: officewars-full-verification
description: Perform exhaustive, evidence-based verification of the complete OfficeWars release candidate across documentation, implementation, rules, deterministic behavior, UI, accessibility, persistence, packaging, edge cases, and legal simulations. Use when the user invokes full verification, requests ship readiness, or asks whether every approved feature is implemented and tested.
---

# OfficeWars Full Verification

## Locate And Freeze The Candidate

1. Locate the active OfficeWars workspace root from the current working
   directory. Require `AGENTS.md`, `officewarsautobattler.html`,
   `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`, and
   `verification/VERIFICATION_CHECKLIST.md`. Do not resolve project files
   relative to the installed skill directory.
2. Read `AGENTS.md` and every active source of truth, current status document,
   handoff, verification checklist, and current-hash report.
3. Calculate and record the exact SHA-256 of `officewarsautobattler.html`
   before testing.
4. Treat the HTML as implemented truth, the game design as stable product
   truth, the balance ledger as decision-status truth, and dated reports as
   evidence only for their named hash.
5. Do not trust a pre-existing checklist as complete. Reconstruct the
   requirement inventory from both documentation and code.

## Run The QA Consistency Phase

Perform the complete document, status, mirror, manifest, skill, and package
audit defined by `$officewars-qa-cleanup`. Rewrite stale active documentation
and synchronize mirrors, but do not modify gameplay during a
verification-only request.

## Build A Bidirectional Requirement Matrix

Trace requirements in both directions:

- For every Implemented or Locked card, trait, manager, coworker, Home effect,
  resource, action, phase transition, exceptional mode, save boundary, and UI
  state, locate its code, player-facing explanation, and test evidence.
- For every material gameplay branch found in the HTML, locate its active
  design status, UI exposure, and test coverage.
- Distinguish Locked-but-unimplemented work from implementation defects.
- Preserve every explicit Draft, Open question, deferred system, and historical
  exception without treating it as a release requirement.
- Record each requirement as `Pass`, `Fail`, `Not Run`, or `Blocked` with exact
  evidence.

## Run Verification Layers

Use existing project runners before writing new harnesses. Expand them only
when a requirement has no adequate evidence.

### Static And Structural

- Validate JavaScript syntax, standalone loading, required IDs, data-table
  integrity, and absence of required external dependencies.
- Verify exact constants, floor curve, roster counts, rarity distribution,
  unique IDs, trait paths, managers, exceptional card pools, and resource
  registries.
- Check every card's preview, markup, selectable state, primary Complete Play,
  and shared resolution compatibility.

### Behavioral And Edge Cases

- Test every shared card-play, Replay, copy, Assist, schedule, outcome,
  coworker, economy, Clock Out, Night, Weekend, promotion, and ending rule.
- Traverse exceptional systems including Brand Strategy, Closing, Deals,
  Schmoozing, Logistics, capstone ownership, and simultaneous decisions.
- Test additive multipliers, nested copies, repeated Legendaries, action
  inflation, burnout interruption, project completion mid-chain, and
  worst-case termination.
- Separate basic-path evidence from exhaustive per-card delayed-lifecycle
  evidence.

### Determinism And Persistence

- Compare 1x, 2x, 4x, and Skip from identical seeds and checkpoints.
- Verify gameplay and random-state equality, rollback after resolver errors,
  repeated input locks, and prepared-Workday restoration.
- Test valid, corrupt, and incompatible saves; Morning, Workday, Clock Out,
  Night, Weekend, Promotion, result, tutorial, and casino restoration.
- Mark every untraversed picker or transition boundary `Not Run`.

### UI, Readability, And Accessibility

- Exercise ordinary and exceptional decision surfaces at desktop, compact
  desktop, landscape phone, portrait rotation, text zoom, and reduced motion.
- Inspect clipping, overlap, viewport overflow, focus order, focus return,
  keyboard operation, semantic names, tooltip access, readable contrast, and
  non-color status communication.
- Capture representative screenshots and inspect them visually.
- Never claim screen-reader or complete keyboard certification unless those
  environments were actually exercised.

### Distribution And Release

- Verify root, rollout, and public-folder equality for every mapped file. The
  public mirror folder is the distribution surface; a release ZIP is built on
  demand only, so verify one only if the user asked for one to exist.
- Check hidden files, launchers, repository metadata, local links, UTF-8,
  manifests, hashes, and standalone operation.
- Confirm the packaged candidate is the exact tested HTML hash.

### Simulation And Balance Evidence

- Before simulation, prove every automated policy uses only player-legal
  choices, costs, exclusions, exceptions, and resolution order.
- Block balance conclusions when policy parity fails.
- Use fixed seeds and report policy capabilities, overall win rate, floor
  conversion, failure causes, stress and rival curves, economy, build
  selection, and conditional payoff conversion.
- Compare results with the 25-35 percent skilled-player target without turning
  one outlier directly into a nerf.
- Keep human playtesting distinct from automated evidence.

## Evidence Discipline

- A requirement passes only with evidence for the current game hash.
- A failed subrequirement makes its containing release gate fail.
- `Not Run` means no adequate execution occurred. `Blocked` means execution
  could not produce trustworthy evidence.
- Preserve previous reports as historical snapshots rather than silently
  rewriting their verdicts.
- Do not repair gameplay during verification unless the user separately asks
  for fixes. Report the exact defect and recommended next action instead.

## Deliverables

1. Write a dated report named
   `verification/FULL_VERIFICATION_<DATE>_<HASH8>.md`.
2. Include the candidate hash, test-artifact hashes, requirement matrix,
   failures, blocked and unrun scope, automated results, and ship decision.
3. Update current status and handoff documents to reference the report without
   converting unresolved items into design content.
4. Synchronize mapped reports and status documents to rollout and public
   mirrors and rebuild affected packages.
5. Give the user a concise verdict: player-facing readiness, implementation
   readiness, balance readiness, and the exact next blocker.

