# Public GitHub Repository Setup

This folder is ready to become the root of a public repository.

## Before Uploading

1. Read `LICENSE_GUIDE.md` and choose a license.
2. Replace this snapshot's date in `docs/PROJECT_STATUS.md` if newer gameplay
   work has happened.
3. Open `officewarsautobattler.html` locally and confirm the title screen loads.
4. Confirm no personal files, browser profiles, generated screenshots, or
   editor settings were added to this folder.

## Browser-Only Upload

1. Sign in to GitHub and select **New repository**.
2. Use `officewars` or another short public name.
3. Suggested description:
   `A single-file office autobattler about projects, stress, coworkers, and corporate survival.`
4. Select **Public**.
5. Do not initialize the repository with a README, `.gitignore`, or license;
   this folder already provides the first two.
6. Create the repository.
7. Choose **uploading an existing file**.
8. Drag the contents of this folder into the upload area. Upload the contents,
   not the outer dated folder.
9. Verify that `.github`, `.agents`, `docs`, and `verification` appear in the
   upload list.
10. Commit with `Publish current OfficeWars development snapshot`.

Large browser uploads can be split into two commits: upload the root files
first, then `docs`, `verification`, `.github`, and `.agents`.

## Enable GitHub Pages

1. Open **Settings**, then **Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the default branch, usually `main`, and the `/ (root)` folder.
4. Save and wait for the deployment link.
5. Open the published URL. `index.html` should forward directly to the game.

## Repository Presentation

Suggested topics:

`autobattler`, `roguelike`, `card-game`, `browser-game`, `indie-game`,
`javascript`, `single-file`, `office`

Use `docs/assets/officewars-workday.png` as the social preview image under
**Settings**, **General**, **Social preview**.

Pin these links near the top of the README:

- the GitHub Pages play URL;
- the project status;
- the contribution guide;
- the agent collaboration guide.

## First Public Milestone

Create a milestone named `Balance and Human Playtest Pass`. Good initial issues:

- collect human Closing Chain 8 and Chain 9 outcomes;
- compare all trait paths under policies that can actually choose them;
- tune Floors 4-7 without making Floor 3 harsher;
- complete remaining UI, accessibility, save/restore, and lifecycle checks;
- design Home item sets only after the current verification gate closes.

## Releases

Do not call the current snapshot `1.0`. A suitable first tag is
`playtest-2026-08-06` or `0.1.0-playtest`.

Attach the standalone `officewarsautobattler.html` to releases so players can
download one file without cloning the repository.
