# Workday Motion Diagnostic Verification

Date: 2026-08-17

## Scope

This report verifies the source-only OfficeWars Workday motion diagnostic. It
compares the restrained office-funk treatment at its original pace, with added
groove motion at that pace, and with the original arrangement accelerated.

## Decision Status

**Palette and pace foundations selected; motion amount unresolved**

The user found the restrained office-funk palette the most fun and the most
likely to remain enjoyable over long listening, while noting that it could
feel slow or become sleepy. In the focused diagnostic, the user preferred
Revision B but also liked an unidentified quality in Revision A.

The selected scope is:

- restrained office funk is the Workday palette foundation;
- Revision B's `112 BPM` pace is the Workday pace foundation; and
- Revision A's extra syncopated motion remains useful vocabulary whose exact
  amount and placement require another listening test.

This does not select a complete arrangement, production master, or shipped
Workday cue.

## Artifacts

- Audition:
  `Music Legacy/officewars-workday-motion-audition.html`
- Audition SHA-256:
  `6850D23E628DDA76D427A80CAC94ECDAFC176B5BA5A4FD0F7D642A60A49E8A49`
- Verifier:
  `.officewars-workday-motion-verify.py`
- Verifier SHA-256:
  `485DC9195F9A2766F2C4CF991D3195E97C01EBB84DE228A8C131E6C79DC76B54`
- Desktop capture:
  `.visual-workday-motion-audition.png`
- Capture SHA-256:
  `49529619AAC81E22B54B74C0B173B52535002D7DBCD9B303C3B921A16C0554BE`

## Controlled Musical Contract

All three samples preserve the selected Sketch B melody, chord plan, bass
roots, four-phrase form, and office-funk sound world.

The diagnostic changes only:

1. no lift at `104 BPM`;
2. added syncopated bass, chord, kick, and snare motion at `104 BPM`; or
3. the exact original arrangement accelerated to `112 BPM`.

## Browser Evidence

The focused Playwright runner passes:

- exact melodic, harmonic, form, and sound-world equality;
- the intended `104`, `104`, and `112 BPM` plans;
- comparison-safe average signals of `0.039429`, `0.032567`, and `0.034276`;
- maximum sampled 50-percent peaks of `0.197224`, `0.137532`, and `0.149829`;
- retained 100-percent headroom with a maximum sampled peak of `0.228905`;
- pause, resume, seeking, timestamp controls, and rapid switching;
- two complete uninterrupted wraps for every sample;
- cleanup to zero tracked sources; and
- desktop, landscape, and portrait layouts without overflow or clipped
  controls.

## Not Run

- Long-exposure fatigue testing beyond two loops.
- Final phrase-development selection.
- Final Workday form, production, or game integration.
- UI-sound and gameplay-sound masking tests inside the shipped game.
