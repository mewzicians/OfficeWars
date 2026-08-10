---
name: officewars-balance-lab
description: Analyze OfficeWars balance with rules-faithful fixed-seed simulations, policy audits, telemetry, ablations, and human evidence. Use when the user asks about win rates, difficulty, floor curves, stress, Chad, deadlines, economy, cards, traits, builds, Closing, tuning, simulations, or whether a mechanic is too strong or weak.
---

# OfficeWars Balance Lab

## Locate The Candidate

1. Locate the active OfficeWars root from the current working directory.
2. Read `AGENTS.md`, `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`,
   `docs/PROJECT_STATUS.md`, `docs/HANDOFF.md`, and relevant verification or
   playtest evidence.
3. Inspect the implemented HTML and record its exact hash.
4. Separate Implemented Baseline, Locked, Draft, Open, and Superseded values.
5. Do not simulate a proposed value as current unless the experiment labels it
   explicitly.

## Validate The Instrument

Before trusting telemetry, prove that each policy:

- uses only legal player actions, prices, limits, exclusions, and phase order;
- cannot see hidden offers, outcomes, future RNG, or unavailable information;
- obeys Lights Out, Home, Deal, outing, reroll, trait, and exceptional-mode
  rules;
- resolves cards, actions, stress, Clock Out, transitions, Chad, and deadlines
  through the same game rules as the player;
- handles persistence or checkpoint behavior consistently when it is part of
  the experiment;
- can actually select and use every build being compared.

Treat policy-rule mismatches as blockers, not balance results. State what each
policy can and cannot optimize.

## Design The Experiment

1. Define the question, hypothesis, population, metrics, and decision threshold.
2. Use fixed paired seeds for comparisons whenever possible.
3. Hold unrelated variables constant.
4. Include a baseline and one-variable ablations before recommending a broad
   change.
5. Use enough runs for the rarity and conditional event being measured; report
   sample size and uncertainty.
6. Keep human playtest evidence separate from scripted policy evidence, then
   compare where they agree or conflict.

## Measure The Whole Curve

Report more than final win rate:

- wins and failure causes by floor;
- project progress, Chad progress, deadline margin, and stress by day;
- burnout timing and recovery sources;
- cash, interest, purchases, debt, and unused resources;
- floor-clear timing and project overkill;
- card, family, trait, path, Home, manager, and coworker exposure;
- pick rate, availability, conditional conversion, and survivorship;
- Closing entry, chain length, Close timing, reward access, and post-Close
  conversion;
- action count, replay count, UI or time burden, and extreme outliers.

For successful runs, measure how early they win and what resources remain. For
failed runs, identify the first decisive deficit instead of only the final loss
label.

## Guard Against False Conclusions

- Do not rank options a policy rarely sees or cannot use intelligently.
- Separate selection strength from exposure and policy preference.
- Check survivorship, floor reach, build commitment, and conditional sample
  size.
- Investigate outliers and degenerate loops before averaging them away.
- Do not flatten exciting high-rolls merely because their ceiling is high.
- Protect standalone card value, splash value, family identity, trait
  breakpoint pressure, and conditional build fantasies together.
- Use the approximately 25-35 percent skilled-player win target as a structural
  guide, not permission for indiscriminate nerfs.

## Recommend Experiments, Not Unapproved Truth

Present findings in this order:

1. evidence and confidence;
2. critical structural problems;
3. tuning watchpoints;
4. plausible explanations and rejected explanations;
5. smallest useful experiments or ablations;
6. Draft recommendations with expected upside and risk.

Balance recommendations remain Draft until the user explicitly approves them.
Do not edit gameplay values during analysis unless implementation is separately
requested. When the user approves a decision, record only that decision in the
balance ledger; use `$officewars-implement` to ship it.

## Report

Include candidate hash, policy legality, seeds, sample sizes, metrics, failures,
biases, human-evidence gaps, and the next highest-information experiment.
