---
name: officewars-github-package
description: Synchronize and verify the GitHub-ready OfficeWars public repository mirror, and build a release ZIP only when one is explicitly asked for. Use when the user asks to update, refresh, prepare, validate, or hand off the public GitHub package, public-repository mirror, or upload bundle.
---

# OfficeWars GitHub Package

The public-repository mirror folder is the deliverable. The repository is
synchronized from that folder directly, so the folder is what must be correct,
complete, and free of private material. A checked-in release ZIP was retired on
2026-08-26 because it was a strictly derived copy that drifted on every
documentation edit while every assertion it carried already held against the
folder. Build a ZIP only when the user asks for a single-file handoff, and never
leave standing checks that require one to exist.

## Establish Release Truth

1. Locate the active OfficeWars root. Require `AGENTS.md`,
   `officewarsautobattler.html`, `docs/GAME_DESIGN.md`,
   `docs/BALANCE_LEDGER.md`, `docs/PROJECT_STATUS.md`, and
   `docs/HANDOFF.md`.
2. Read those files and identify the active `officewars-public-repo-*`
   mirror. Treat the root as source and the public folder as a mirror.
3. Record the root game SHA-256 before changing package files.
4. Inspect current workspace changes. Preserve unrelated user work and do not
   package an unexplained implementation or documentation mismatch.
5. If multiple public mirrors exist, use the one explicitly named by the user.
   Otherwise use the mirror named by active guidance; do not merge mirrors.

## Build The Public Inventory

Keep the mirror usable as a repository root rather than wrapping it in another
directory. Include every current public artifact:

- the standalone game, GitHub Pages launcher, README, contribution guidance,
  agent guidance, requirements, `.gitignore`, and `.nojekyll`;
- `.github/`, including issue and pull-request templates;
- `.agents/skills/`, including every current OfficeWars project skill and its
  picker metadata;
- active public documentation, selected public assets, verification runners,
  checklists, and current evidence referenced by the public handoff or status.

Exclude private archives, rollout-only handoffs, credentials, `.git/`, browser
profiles, temporary screenshots, caches, editor state, old ZIPs, and files
containing personal absolute paths that are not intentional documentation.

Use the existing public mirror as the packaging allowlist, then add a newly
active root file only when current public guidance or the release change
requires it. Never delete historical verification evidence merely because it
is old.

## Synchronize

1. Copy mapped root files byte-for-byte into the public mirror.
2. Update public status, handoff, patch notes, skill lists, and current hashes
   when the release changed them.
3. Keep `index.html` as a launcher; do not duplicate gameplay logic into it.
4. Preserve the one-file game architecture and all hidden repository files.
5. Run the QA-cleanup checks for stale dates, broken local links, invalid
   UTF-8, trailing whitespace, private paths, contradictory status, and
   root-to-public drift.
6. If gameplay changed, require JavaScript syntax validation and the focused
   tests appropriate to that change before calling the package ready. Do not
   turn an unrun broad suite into a pass.

Stop and report rather than packaging when active sources contradict one
another, a required test fails, or the public folder contains unexplained
files.

## Verify The Mirror

Confirm all of the following against the public folder:

- every mapped file is byte-identical to its root source;
- the packaged game hash equals the root game hash;
- `.github/`, `.agents/skills/`, `.gitignore`, and `.nojekyll` are present;
- the public README links to existing packaged paths;
- intentionally divergent public files, such as a play-only README or
  contribution guidance, are left divergent rather than overwritten from root;
- no private path is present: `.obsidian/`, `Home.md`, `Inbox/`, `Wiki/`, raw
  research and captures, private source attachments, and continuity ledgers;
- no excluded temporary artifact entered the mirror; and
- the mirror file count and the root game hash are recorded.

## Build A ZIP Only On Demand

Skip this section unless the user asked for a ZIP. When they do, run the
bundled deterministic builder:

```powershell
python "<skill-dir>\scripts\build_public_zip.py" `
  "<workspace>\officewars-public-repo-YYYY-MM-DD" `
  "<workspace>\officewars-public-repo-YYYY-MM-DD.zip"
```

The script includes dotfiles, sorts archive paths, removes the old ZIP only
after the replacement is complete, and verifies every archived byte against
the public folder. Do not use a wildcard-only `Compress-Archive` command
because it can omit hidden repository files.

Then confirm the ZIP opens with no duplicate or unsafe paths, that its paths
begin at repository-root contents rather than an outer folder, that its
inventory exactly equals the verified mirror inventory, and record its SHA-256,
file count, filename, and size. Treat the result as a one-off handoff artifact:
say when it was built and from which mirror bytes, and do not add a check
elsewhere that requires it to keep existing.

## Report

State the public mirror path, the synchronized files, the tests and mirror
checks as Pass, Fail, Not Run, or Blocked, the root and packaged game hashes,
and any remaining release blocker. If a ZIP was built, add its path, hash, and
size, and state that it is a point-in-time copy. Never say the package is ready
for GitHub when a required check failed or was not performed.
