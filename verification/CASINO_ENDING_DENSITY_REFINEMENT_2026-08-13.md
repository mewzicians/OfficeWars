# Casino Ending-Density Refinement Verification

Date: 2026-08-13

## Scope

This source-only music pass refined the active `Clean Return` and
`Groove-Carried Return` auditions. It did not change
`officewarsautobattler.html`, shipped gameplay, balance, or release packages.
The music remains exploratory and unapproved.

## Candidate Contract

- `Current Return` remains the exact reviewed 192-step control.
- All three candidates are identical through step 127 in foreground notes,
  lead envelopes, movement-ending accents, and treatment-dependent support.
- `Clean Return` changes only steps 128-191. Late False Confidence falls from
  16 to 10 attacks, and Compulsive Return falls from 48 to 31.
- `Groove-Carried Return` uses Clean's exact notes and articulation. It adds
  low bass replies only at steps 147, 163, and 179.
- No Groove reply occurs during False Confidence or the final turnaround.
- Every candidate retains the final `D` into Hook Payoff's opening `E`.

## Result

**Pass**

The focused Playwright runner verified:

- page parsing with no page or console errors;
- every full movement and focused direct start;
- audible late sections and continuous loop seams;
- pause, resume, and seeking;
- 45 rapid candidate switches;
- 66 seconds of uninterrupted Groove playback;
- a 50-source peak without source accumulation;
- cleanup to zero tracked sources; and
- responsive three-, two-, and one-column layouts without clipped controls or
  horizontal overflow.

Human musical preference remains **Not Run**. Technical stability does not
approve either candidate.

## Hashes

- `Music Locked/officewars-casino-motif-audition.html`:
  `7F078D0D346818CB989DC8DA2460A053D6A644CF24595381D057BAA67E613D1E`
- `.officewars-casino-motif-verify.py`:
  `64E463CD9535A73C49482FAC66E64FA70304C232BAFE9C97B38ED50C1F3AEA18`
- Shipped game, unchanged:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`
