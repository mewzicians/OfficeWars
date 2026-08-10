# Options And Night Policy Verification

Date: 2026-08-10

Game SHA-256:
`037A7BA364D0CAC4E40A4BAA78C8AF36022B0FF8D089D65AE6EE2F51F7AE9D0B`

Full verifier SHA-256:
`BD0687AFA64517ACFDCF391E0823BFA3531DC064E93F4CDC17C75678DA44D408`

## Results

| Requirement | Status | Evidence |
|---|---|---|
| Player purchase-versus-Lights-Out rule | **Pass** | Manual Lights Out blocks Home and Deal purchases; a purchase disables Lights Out; Moodboard remains the explicit exception |
| Headless Night-policy parity | **Pass** | Skilled policy purchased one Home item, ended with `recPicked=false`, and received only 4 stress recovery from 50 to 46 |
| Automatic Lights Out without a purchase | **Pass** | Advanced fixture finalized from 50 to 41 stress and advanced to Morning |
| Persistent volume preference | **Pass** | Legacy meta defaulted to 70; changing to 35 persisted and applied `audio.volume=0.35` |
| Tutorial reset in Options | **Pass** | Reset stored `completed=false`, `nextStep=0`, and `replayRequested=true` |
| Duplicate How to Play reset removed | **Pass** | No `orientation-replay-button` exists after opening How to Play |
| Meta-save compatibility | **Pass** | All 23 persistence and tutorial checks passed with the new `settings.volume` field |
| Options responsive layout | **Pass** | 1440x900 and 844x390 samples reported no clipping or viewport overflow |
| Runtime integrity | **Pass** | No sampled page errors, console errors, or external runtime requests |
| Structural balance telemetry | **Not Run** | The policy is legal again, but the fixed-seed balance matrix was not requested in this pass |

## Commands

```powershell
python .officewars-smoke-run.py
python .officewars-persistence-verify.py
python .officewars-advanced-verify.py
python .officewars-full-verify.py 0
```

All four commands passed on the named game hash.

## Remaining Scope

The preceding exhaustive report's broader every-picker,
assistive-technology, every-boundary save/restore, reset, rapid-input, and
memory-profile rows retain their recorded Not Run or Blocked status. The old
58.4 percent skilled-policy result remains historical until the corrected
policy is rerun.
