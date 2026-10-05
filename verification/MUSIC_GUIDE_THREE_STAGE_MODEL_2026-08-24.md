# Music Guide Three-Stage Model Verification

Date: 2026-08-24

## Scope

This refinement implements only the first approved review step:

1. revise the guide into a progressive three-stage model; and
2. align the reusable approach-bundle template with that model.

The Boss A pilot bundle is intentionally unchanged. Aligning that existing
bundle is the separately approved next step.

## Verdict

Pass.

The guide now distinguishes:

1. **Musical Brief:** the minimum orientation required for every task;
2. **Approach Bundle:** conditional profile and method assembly; and
3. **Audition Contract:** only when listening must resolve a decision.

The model supports both brief-led and material-led work, allows a justified
tightly coupled method cluster, and defines when bundles become resolved or
archived.

## Guide Changes

`Build The Musical Brief` now:

- requires only scope, job or problem, listener context, existing identity,
  protected material, constraints, and the current question;
- treats duration, repetition, emotion, references, delivery, and masking as
  optional when decision-relevant; and
- allows a concrete musical objective instead of forcing an emotional story.

`Assemble An Approach Bundle` now:

- may be skipped for simple direction or diagnosis;
- supports brief-led composition from an open page;
- supports material-led composition around an existing sketch or accident;
- treats the bundle as provisional after the first meaningful sound;
- defaults to one primary method while allowing one justified coupled method
  cluster;
- defines a retrieval stopping rule; and
- requires answered bundles to become `resolved` or `archived`.

The Composer Review now records only answers that materially change the brief,
bundle, or experiment.

The final contract is split into three independently optional blocks rather
than one approximately 40-field form.

## Template Changes

The approach-bundle template now contains aligned fields for:

### Stage 1

- project scope and medium;
- working mode;
- musical job or problem;
- audience context;
- existing and protected material;
- constraints and open decisions;
- current question; and
- optional objective, reference, duration, and delivery context.

### Stage 2

- entry path;
- independent profile axes;
- primary method or coupled method cluster;
- supporting and excluded methods;
- prerequisites;
- compatibility and conflicts;
- evidence;
- audible success; and
- resolution condition.

### Stage 3

- audition question;
- control;
- held constants;
- changed hypothesis;
- audible criterion;
- repeated exposure;
- plausible consequences;
- technical verification;
- remaining gates; and
- next decision.

The template instructs authors to use `workflow: resolved` when the question is
answered and `workflow: archived` plus `superseded_by` when replaced.

## Current Hashes

- revised guide:
  `D87FD1412C864540AEEDBA4DAE21D958EB2A37BC6EDF5C2C5D3AEC9349766F6B`
- three-stage template:
  `CE1E439856C6CECF2A4B75246E77EFF26EC9DA36793507AA5F502A3F0F4CA782`
- coverage map:
  `07125B19931E38FFD1CB7E8971404E31BB4BCB82B5E3EFCE753F1D5EBDD46F05`
- verifier:
  `2B50666C7B236FA550E69D15BEE78E1674AC5505BC1576B2845377F452E1795C`

The guide remains shorter than the archived pre-second-brain guide:

- archived guide words: `3,859`;
- current guide words: `3,697`.

## Automated Verification

Command:

```powershell
python -B .officewars-music-guide-second-brain-verify.py
```

Result:

`175 passed, 0 failed`

New checks prove:

- all three stage headings exist;
- brief-led and material-led entry are documented;
- coupled method clusters are supported;
- the template contains the complete three-stage metadata contract;
- all second-brain links still resolve;
- the guide remains project-neutral; and
- the public fallback remains complete.

## Protected State

Unchanged:

- research library:
  `ADE4AEBACD525A76D01CD96F30712715B21BB94F9A246CF2448FF7CCFFAD7A1C`
- OfficeWars music brief:
  `B2DCC10C369E89BA5C5BEAC2DA49B682D1128F74B4D9736FBFC2BFBC3D4E1BF7`
- music catalog:
  `9D218055DD13E5D1E79F2F4213863641844D5499CB4F0A5010B95D11F4B29830`
- Boss A second-movement plan:
  `D2935E0FE950B852C2715335A896ED7DDEE09D0DF20BE2A822B1980A9EB93BC4`
- game:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`
- Approved Boss baseline:
  `0A6BC2BBF90C63761BD1BAA0743584CCD1444DC53E9DE845CFBBABDE273B636C`
- active Boss Test:
  `2441494767E9C39E2D810783D70C798727A48C9E33D6FD942857851D8D45DF63`

No audio artifact, lifecycle status, approval, or music-composer skill changed.

## Mirrors And Package

The revised guide is byte-equal across root, rollout, public mirror, and public
ZIP.

Public ZIP:

- files: `168`;
- bytes: `1,216,737`;
- SHA-256:
  `2878EF193C7C25F54E1C94EC8B0671D478067EDF463B0B0C857EB36FE779A5D9`;
- private vault entries: `0`; and
- packaged game hash unchanged.

## Intentionally Remaining

The read-only Boss A pilot still uses the pre-refinement field set. This is
intentional evidence for step 2 rather than an overlooked migration.

Step 2 should:

- populate the Stage 1 brief explicitly;
- use `entry_path: material-led`;
- rename its emotional-character profile field;
- state selected material and approval boundaries;
- state held constants and repeated exposure;
- record plausible results and the next decision; and
- preserve every existing musical conclusion and boundary.
