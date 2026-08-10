---
name: officewars-github-package
description: Synchronize, rebuild, and verify the GitHub-ready OfficeWars public repository ZIP. Use when the user asks to update, refresh, prepare, validate, or hand off the public GitHub package, public-repository mirror, release ZIP, or upload bundle.
---

# OfficeWars GitHub Package

## Establish Release Truth

1. Locate the active OfficeWars root. Require `AGENTS.md`,
   `officewarsautobattler.html`, `docs/GAME_DESIGN.md`,
   `docs/BALANCE_LEDGER.md`, `docs/PROJECT_STATUS.md`, and
   `docs/HANDOFF.md`.
2. Read those files and identify the active `officewars-public-repo-*`
   mirror and its sibling ZIP. Treat the root as source and the public folder
   as a mirror.
3. Record the root game SHA-256 before changing package files.
4. Inspect current workspace changes. Preserve unrelated user work and do not
   package an unexplained implementation or documentation mismatch.
5. If multiple public mirrors exist, use the one explicitly named by the user.
   Otherwise use the mirror named by active guidance; do not merge mirrors.

## Build The Public Inventory

Keep the upload usable as a repository root rather than wrapping it in another
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

## Synchronize Before Packaging

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

## Build The ZIP

Run the bundled deterministic builder:

```powershell
python "<skill-dir>\scripts\build_public_zip.py" `
  "<workspace>\officewars-public-repo-YYYY-MM-DD" `
  "<workspace>\officewars-public-repo-YYYY-MM-DD.zip"
```

The script includes dotfiles, sorts archive paths, removes the old ZIP only
after the replacement is complete, and verifies every archived byte against
the public folder. Do not use a wildcard-only `Compress-Archive` command
because it can omit hidden repository files.

## Verify The Upload Bundle

Confirm all of the following:

- the ZIP opens and has no duplicate or unsafe paths;
- archive paths begin at repository-root contents, not an outer folder;
- ZIP inventory exactly equals the public-folder inventory;
- every archived file is byte-identical to its public source;
- `.github/`, `.agents/skills/`, `.gitignore`, and `.nojekyll` are present;
- the packaged game hash equals the root game hash;
- the public README links to existing packaged paths;
- no excluded private or temporary artifacts entered the ZIP; and
- the final ZIP SHA-256, file count, filename, and size are recorded.

## Report

State the public mirror and ZIP paths, synchronized files, tests and package
checks as Pass, Fail, Not Run, or Blocked, root and packaged game hashes, ZIP
hash and size, and any remaining release blocker. Never say the ZIP is ready
for GitHub when a required check failed or was not performed.
