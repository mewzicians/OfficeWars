# Casino Answer Chase Density Verification

Date: 2026-08-13

## Scope

This source-only music pass reduces the excessive beeping in Answer Chase. It
does not change `officewarsautobattler.html`, shipped gameplay, balance, or
audio. Every audition remains exploratory and musically unapproved.

## Candidate Contract

- `Previous Clean` preserves the reviewed loop with 41 Answer Chase foreground
  attacks and 24 bright offbeat replies.
- `Chase Breathing` uses 30 foreground attacks and no reply voice.
- `Chase Echoes` uses the same 30 foreground attacks plus five lower, softer
  echoes at steps 53, 62, 69, 76, and 85.
- The echoes occupy existing rests and leave the final Answer Chase bar clear.
- Hook Payoff and steps 96-191 are exact across all candidates.
- The cleaned 10-attack False Confidence ending, 31-attack Compulsive Return,
  and final `D -> E` loop return remain unchanged.

## Result

**Pass**

The focused Playwright runner verified:

- page parsing with no page or console errors;
- exact candidate notes, treatments, reply counts, and reply positions;
- every full movement and the Answer Chase-to-False Confidence handoff;
- pause, resume, seeking, and 45 rapid candidate switches;
- 66 seconds of uninterrupted Chase Echoes playback;
- a 43-source peak without source accumulation;
- cleanup to zero tracked sources; and
- responsive three-, two-, and one-column layouts without clipped controls or
  horizontal overflow.

Human musical preference remains **Not Run**. Technical stability does not
approve either quieter treatment.

## Hashes

- `Music Locked/officewars-casino-motif-audition.html`:
  `3A4F629EFC8FF4F0AE4B1D7D1F2FBC9604A8397CED09E961EC1DBC32861FCC4D`
- `.officewars-casino-motif-verify.py`:
  `7A2B1B494E6D15390968B420EFB2D08B7D102C47F6E9802B1F20D2F0F013CB75`
- Shipped game, unchanged:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`
