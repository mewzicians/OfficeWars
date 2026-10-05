# Guided Intern Spotlight And Wording Pass

Date: 2026-09-23

Candidate:

- SHA-256:
  `5181B41F5175B0F84CE6C886638B646A16C9DC5032AEE6C1ED6D8B2101BB3AB8`
- size: `1,699,513` bytes
- active-run schema: 9
- Cash Jar target schema: 10, inactive
- Cash Jar public gate: disabled

## Implemented Opening

`GI-OPEN` remains one of exactly 18 Guided checkpoints but now contains four
mandatory presentation steps:

1. the actual Project Progress HUD explains the floor project and defines PP;
2. the race card identifies Chad and shows `3 WORKDAYS · WED–FRI`;
3. Project Fit explains Favored, Adversarial, Approval, and their function; and
4. Karen and Bob appear as named stakeholders with Gatekeeper and Pragmatist
   work-style descriptors.

The compact Coordinator card stays separate from every highlighted target.
Back and Next move through `1/4` to `4/4`; only the final step exposes Clock
In. Opening Show Me is removed because the walkthrough itself supplies the
spotlight. The disabled Back control has a distinct visual state.

## Wording And Progressive Detail

- All 18 Coordinator instructions use the approved concise copy.
- Exactly four optional Why explanations remain: manager settlement,
  Relationship versus standing, Lights Out blocking, and Overdelivery
  expectations.
- Repeated label narration and the authored-result prose were removed.
- Friday's fixed result is disclosed as `GUIDED RESULT · SUCCESS`.
- Favored and Adversarial terms have persistent keyboard, pointer, and touch
  tooltips with exact effects.
- Relevant Morning task confirmation shows exact project-fit consequences;
  neutral tasks add no disclosure.
- Wrong-action feedback names the required Guided action without repeatedly
  saying “for this assignment.”

## Persistence And Determinism

- `R.tutorialLessonState.openingStep` stores the current presentation step.
- Missing `openingStep` defaults to the first step; no migration or schema
  change is required.
- Every opening step survives reload with the same gameplay RNG and state.
- Intentional Guided replay starts again at step one.
- Back, Next, focus, tooltips, resizing, reduced motion, and responsive refit
  consume no gameplay state or gameplay RNG.
- Headless execution completes the presentation boundary without changing the
  Associate continuation.

## Verification

| Suite | Result |
|---|---|
| Guided Intern | Pass 47/47 |
| Persistence and tutorial | Pass |
| No-scroll/collision matrix | Pass 354/354 |
| Broad visual-capture matrix | Pass |
| Cinematic Workday | Pass 33/33 |
| Advanced interaction chains | Pass |
| Integrated full UI audit | Pass |
| Smoke | Pass |
| Formal screen-reader execution | Not Run |
| Broad human playtest | Not Run |

Verifier hashes:

- Guided Intern:
  `847F01E7CE942A314EFE1914557877498D6067A8D145DCBE3525678603C7C813`
- persistence:
  `D3C60168C75BA8E1C4257A46FB0A2DF4DC53D045DCA7BFF26D433DBACC62031E`
- advanced:
  `D6B3659131E930CE82F7B54A73BC6D52561D4AC3486E6F4D6BAA8F45C9A0F036`
- no-scroll:
  `0A94830B6DACBE82850AB0AE19669665669ECE5E061516D86DF701E13E75A9B8`
- visual capture:
  `CD4B17B46689E544B51D105C72ABE12C5B77481EC0F387EE4BB99A81A7941422`
- cinematic:
  `D97F2C608B9229D0471ACE8E11C23BB55BA1636479D9B0C65343FCDA97D1B04B`
- smoke page:
  `F80C6517555CFCA10A252EC9114E54922576FD8E45BFDEEC7B916B90B27F9FFF`
- smoke runner:
  `5B62FD0B577E033A79D498CB0301934CBB4980EED92182763A7B24C384BA2950`

## Preserved Boundaries

- Guided gameplay values, exact traces, and the 18-checkpoint count are
  unchanged.
- Watched 1x/2x/4x, Skip, reload, replay, and headless outcomes remain equal.
- Cash Jar remains gated and schema 10 remains inactive.
- Galactic Investment and Galactic Gambler are unchanged.
- The public mirror remains on `360CC6C0...`.
- No release ZIP was built.

## Verdict

The Guided Intern spotlight and wording pass is implemented and ready for
human first-session review.
