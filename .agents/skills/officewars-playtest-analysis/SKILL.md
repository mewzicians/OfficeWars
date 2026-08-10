---
name: officewars-playtest-analysis
description: Turn OfficeWars playtest notes, saves, screenshots, recordings, surveys, and telemetry into prioritized evidence and experiments. Use when the user shares player feedback or asks what playtests mean, which problems matter, why players won or lost, or what should be tested next.
---

# OfficeWars Playtest Analysis

## Locate The Tested Build

1. Locate the active OfficeWars root from the current working directory.
2. Read `AGENTS.md`, `docs/GAME_DESIGN.md`, `docs/BALANCE_LEDGER.md`,
   `docs/PROJECT_STATUS.md`, `docs/HANDOFF.md`, and `docs/PLAYTEST_GUIDE.md`.
3. Identify the exact tested hash or version. Do not merge evidence from
   different builds without labeling it.
4. Inspect the relevant HTML and current rules before interpreting behavior.
5. Separate Implemented Baseline, Locked, Draft, and Open design.

## Normalize The Evidence

For each session, capture when available:

- player experience, goals, and familiarity with card games or roguelikes;
- build, path choices, Homes, coworkers, managers, and floor reached;
- seed, save, platform, browser, viewport, and input method;
- session length, decision time, tutorial status, and use of speed or Skip;
- win or loss cause, stress curve, Chad curve, deadline margin, cash, and
  progress;
- exact quote or observed behavior;
- screenshot, recording timestamp, save, or telemetry row supporting it.

Keep observation separate from player explanation and analyst hypothesis.

## Classify Findings

Assign every meaningful item to one primary class:

- **Bug**: implementation violates intended rules or state.
- **Comprehension**: the player cannot find, predict, or explain a rule.
- **Decision quality**: information exists but does not support a useful choice.
- **Balance**: legal understood play produces an unhealthy power or difficulty
  pattern.
- **Pacing**: time, repetition, waiting, or decision cadence harms the run.
- **Feedback**: the result occurs but is not visible, timely, or satisfying.
- **Accessibility**: input, perception, motion, text, or semantics exclude use.
- **Taste**: preference without evidence of a systemic problem.

Do not turn taste into a defect or confusion into a balance nerf.

## Assess Strength Of Evidence

For each finding, estimate:

- frequency across sessions;
- severity and consequence;
- reproducibility;
- affected player profile and game phase;
- whether the issue improved with learning;
- whether telemetry supports the report;
- confidence and plausible competing explanations.

One severe reproducible bug can outrank frequent polish feedback. One unusual
high-roll is not automatically a balance problem.

## Analyze Runs

Look for:

- where stress, deadline, or Chad first became unrecoverable;
- early dead choices and automatic picks;
- trait breakpoint sacrifices and splash-card decisions;
- unused resources and misunderstood systems;
- floor-clear timing, overkill, and late-run acceleration;
- build availability versus build execution;
- Closing entry, chain risk, cash-out decisions, and reward conversion;
- action inflation, long resolution chains, and Workday readability;
- tutorial drop-off, menu confusion, save trust, and exceptional-mode clarity.

Compare human evidence with legal fixed-seed simulation only when the tested
rules and candidate hash align.

## Recommend The Next Learning Step

Prioritize findings by player harm, evidence strength, reach, and cost to test.
For each important item, propose the smallest discriminating experiment:

- a focused reproduction;
- copy or layout prototype;
- instrumentation event;
- controlled rules ablation;
- targeted seed set;
- novice-versus-expert comparison;
- follow-up interview question.

State what result would support or reject the hypothesis. Avoid bundling
multiple uncertain changes into one experiment.

## Protect Decision Status

Playtest conclusions and tuning proposals remain Draft until the user approves
them. Do not edit gameplay during analysis unless implementation is separately
requested. Record approved decisions in the ledger, send defects to
`$officewars-debug`, balance questions to `$officewars-balance-lab`, UX
problems to `$officewars-ux-audit`, and approved changes to
`$officewars-implement`.

## Report

Lead with ranked findings, evidence, confidence, and affected players. Then
summarize run patterns, disagreements between feedback and telemetry, and the
next highest-information experiments.
