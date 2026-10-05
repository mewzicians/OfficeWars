# Boss A Active Development Branch

Date: 2026-08-19

## Decision

Boss A remains under active development even though its current static-free
version is Approved.

- Protected rollback baseline:
  `Music Locked/officewars-boss-a-windowed-percussion-audition.html`
- Active editable Test branch:
  `prototypes/officewars-boss-a-development-audition.html`

The files use different internal labels. The Approved reference must remain
unchanged while further composition, arrangement, production, and completion
work occurs in the Test branch.

## Initial Branch State

The Test branch was derived from the exact Approved page and changed only:

- visible development labels;
- lifecycle status from `Approved` to `Test`;
- internal label to `OW-MUSIC-BOSS-A-DEVELOPMENT`;
- API name and scope; and
- the optional download filename.

Its embedded audio remains byte-identical to the Approved baseline:

- asset SHA-256:
  `D6DD6B1EBAF50F95F4B0DEAA8860A9D9B667D2FF27C6ED5A549A977876D1C554`
- asset byte length: `8777188`

## Artifact Hashes

- Approved baseline HTML:
  `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`
- Active Test HTML:
  `10236A5CA94FDE562E5A138135E7950D851B424A6048835D84E71833AB36CA6D`
- Focused Test verifier:
  `284C1D0DD043F8120ECE7FD707C9E013A4211963E55D60A7C801162B31428518`
- Game HTML:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`

## Verification

Pass:

- catalog placement and unique lifecycle labels;
- exact embedded-audio equality with the Approved baseline;
- standalone playback;
- Test status, internal label, and scope;
- pause, resume, seeking, movement starts, and rapid source replacement;
- one-source runtime behavior, headroom, responsive layout, and cleanup;
- protected Approved baseline hash; and
- no game integration.

The full two-loop audio evidence belongs to the identical Approved baseline.
The new focused regression is sufficient for this metadata-only branch
creation because its embedded audio asset is exact.

## Status

The active Boss branch remains `Test`. It is not Completed, integrated, or
shipped.
