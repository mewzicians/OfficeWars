# Boss A Percussion Repair

Date: 2026-08-19

## Scope

This source-only diagnostic preserves the liked Boss A undercurrent-repair
tune and changes only the remaining high-frequency percussion that human
listening described as a constant metronome.

No music was added to `officewarsautobattler.html`.

## Diagnosis

The sustained On the Clock undercurrent was no longer the metronome source.
The complete mix still used:

- a pitched square-wave hat on every offbeat; and
- a smaller square-wave snare edge.

Those regular tonal attacks remained perceptually separate from the tune.

## Protected Sources

- Selected Boss A identity:
  `Music Locked/officewars-boss-identity-audition.html`
  - SHA-256:
    `94475C64CE37353EAAB68741A844429EDE3C6D9D709084BE3363112018C8F941`
- Liked undercurrent-repair control:
  `Music Legacy/officewars-boss-a-undercurrent-repair-audition.html`
  - SHA-256:
    `75A89448B43A14CB02E9A02B931B4C57D536B63D0001B3522BB724294A59051D`
- Selected Workday parent, **On the Clock**:
  `Music Locked/officewars-workday-long-cycle-tribrid-audition.html`
  - SHA-256:
    `FF677CC9F4F85501BCE6979D614FAE90DC293A308BCE31E7DC9EA4867F91F4B2`
    (as of this record; repinned to `60DDDF21` by the 2026-08-27 settle repair, which changed no music)
- Game:
  `officewarsautobattler.html`
  - SHA-256:
    `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`

The protected audition and game hashes remained unchanged.

## Candidate

- Audition:
  `Music Legacy/officewars-boss-a-percussion-repair-audition.html`
  - SHA-256:
    `86A19FDE1BD0EEF44F35C797F76E7DB0A05AC6878A256B4E306E1A4F79CE1A0F`
- Verifier:
  `.officewars-boss-a-percussion-repair-verify.py`
  - SHA-256:
    `DEB2AFF1B45F1F8076A28AF1E8BAD241B1578A01BCC022CEC33212D6537107AA`
- Retained visual:
  `.visual-officewars-boss-a-percussion-repair-audition.png`
  - SHA-256:
    `30464702F04080A1FE17C46BB7E7E883C2046DDE68AFEFDB13416D352A699AD7`

The candidate replaces only the tonal high percussion with deterministic,
non-tonal paper-brush noise. Its bar patterns alternate instead of striking
every offbeat identically. Melody, harmony, bass, sustained ancestry,
four-movement form, duration, and mix architecture remain exact.

The audition provides:

- `Current Full Repair`, the exact liked control;
- `Integrated Paper Brush`, the replacement candidate; and
- `Paper Brush Only`, an isolated monitor.

## Verification

The final retained verifier passed:

- exact control equality;
- selected Boss A and On the Clock protected hashes;
- unchanged melody, harmony, bass, form, undercurrent, and movement map;
- absence of the rejected tonal high-percussion oscillators in the candidate;
- deterministic paper-brush generation and alternating syncopated patterns;
- all three listening modes and direct movement starts;
- comparison-safe full-mix levels;
- audible isolated brush monitoring;
- pause, resume, seeking, rapid switching, and live movement highlighting;
- `100%` page-volume headroom;
- desktop, landscape, and portrait layouts;
- two uninterrupted loops of all three modes;
- maximum `22` concurrent tracked sources;
- no clipping; and
- cleanup to zero tracked sources after stopping.

Observed average signal levels at `50%` page volume:

- Current Full Repair: `0.014936`
- Integrated Paper Brush: `0.015207`
- Paper Brush Only: `0.000536`

The first post-move run correctly rejected stale protected-verifier hashes.
Those hashes were updated after confirming the only verifier-byte changes were
the new `Music Locked/` and `Music Legacy/` source paths. The exact final
verifier bytes then passed the complete lifecycle gate.

## Decision Boundary

Boss A remains the selected boss identity foundation. The undercurrent-repair
tune remains liked but not selected as a complete boss cue.

Human listening liked the integrated paper-brush treatment but reported an
occasional static pop. The artifact therefore moved through Limbo and is now
labeled Rejected in `docs/music/officewars/MUSIC_CATALOG.md`.

Its liked musical material is preserved in the active Test
`OW-MUSIC-BOSS-A-POP-REPAIR`. Complete form approval, production master,
adaptive behavior, game integration, shipping, and final delivery remain open.
