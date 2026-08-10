---
name: officewars-qa-cleanup
description: Audit, rewrite, and synchronize OfficeWars documentation, guidance, skills, handoffs, mirrors, manifests, and release packages without changing gameplay. Use when the user invokes QA cleanup or asks to remove stale material, reconcile project truth, repair documentation drift, or prepare consistent handoff and public-repository copies.
---

# OfficeWars QA Cleanup

## Locate The Workspace

1. Locate the active OfficeWars workspace root from the current working
   directory. Require `AGENTS.md`, `officewarsautobattler.html`,
   `docs/GAME_DESIGN.md`, and `docs/BALANCE_LEDGER.md`. Do not resolve project
   files relative to the installed skill directory.
2. Read `AGENTS.md` completely.
3. Read `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`, `docs/HANDOFF.md`,
   `docs/PROJECT_STATUS.md`, and `docs/WORKING_WITH_AGENTS.md`.
4. Treat `officewarsautobattler.html` as implemented truth,
   `docs/GAME_DESIGN.md` as stable product truth, and
   `docs/BALANCE_LEDGER.md` as decision-status truth.
5. Treat rollout and public folders as mirrors. Never let a mirror silently
   become an independent source.

## Build The Audit Inventory

Inventory every active:

- repository instruction and agent-guidance file;
- design, balance, status, handoff, patch-note, and verification document;
- project and user-facing OfficeWars skill;
- verification runner, checklist, screenshot, and evidence report;
- rollout handoff and public-repository mirror;
- manifest, hash table, launcher, repository metadata file, and ZIP package.

Read archives only when needed to classify useful history. Do not reactivate an
archived rule merely because it exists.

## Reconcile Project Truth

1. Compare every active implementation claim with the HTML or exact-hash test
   evidence.
2. Preserve the status meanings `Implemented Baseline`, `Locked`, `Draft`,
   `Open`, and `Superseded`.
3. Report HTML and documentation mismatches before changing either side. Never
   describe planned behavior as implemented.
4. Find stale dates, hashes, paths, status summaries, completed instructions,
   duplicated explanations, obsolete mechanics, and contradictory guidance.
5. Validate roster and system invariants documented by the active project,
   including card counts, rarity distribution, trait-path status, exceptional
   modes, and current open blockers.

## Clean Active Documents

- Rewrite, consolidate, move, or remove stale sections in place. Do not append
  verification notes beneath obsolete text.
- Make active documents shorter and clearer where possible.
- Keep factual former behavior only when it is still a useful labeled
  Implemented Baseline.
- Preserve only useful superseded reasoning in
  `docs/ARCHIVE_SUPERSEDED.md`; keep transient audit output out of active
  design documents.
- Record only decisions the user explicitly approved. Do not promote a Draft
  or answer an Open question during cleanup.
- Do not edit gameplay code unless the user separately requests an
  implementation change.

## Synchronize Mirrors And Packages

1. Synchronize every mapped root file to
   `officewars-rollout-handoff-2026-07-31/` when present.
2. Synchronize mapped game, guidance, documentation, verification, skill, and
   repository files to the current public-repository mirror when present.
3. Refresh manifest and documented hashes after all content changes.
4. Rebuild the public ZIP from the public folder, including hidden repository
   files, and compare every archived file byte-for-byte.
5. Preserve historical snapshot files unless they contain an active broken
   reference or falsely claim to be current.

## Validate The Cleanup

Check and report:

- active Markdown links and file references;
- valid UTF-8, no accidental binary or browser-profile debris, and no
  unintended trailing whitespace;
- decision-status consistency and current game hash;
- root-to-rollout and root-to-public mapped-file equality;
- skill metadata, skill-copy equality, and picker prompts;
- manifest completeness and hash accuracy;
- ZIP inventory and byte equality.

Treat an unexpected game-hash change as a failure. Do not run broad gameplay or
balance suites unless needed to resolve a documentation claim; exhaustive
implementation testing belongs to `$officewars-full-verification`.

## Report

Summarize:

1. files rewritten, moved, removed, or synchronized;
2. mismatches corrected and any mismatch intentionally left unresolved;
3. validation results with Pass, Fail, Not Run, or Blocked status;
4. current hashes and package names when they changed; and
5. remaining work that requires design approval, implementation, human
   testing, or another skill.

