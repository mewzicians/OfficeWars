# OfficeWars Full Verification

Date: 2026-08-20

## Frozen Candidate

- Game: `officewarsautobattler.html`
- SHA-256:
  `D2E44F34D21CF9A9303311ED5377A9910BB7D2D5C9FEE36BC0F98FCA5647498A`
- Scope: verification, documentation cleanup, music lifecycle QA, mirror
  synchronization, and package validation only.
- Gameplay changes: none.

## Verdict

| Readiness area | Status | Evidence |
|---|---|---|
| Implementation | Pass | Full structural and behavior runner, smoke, advanced systems, persistence/tutorial, keyword, Home/schedule, and Night Planner suites pass. |
| Player-facing UI | Pass with unrun assistive-technology scope | Desktop, compact desktop, landscape phone, portrait rotation, reduced motion, and 200-percent text scaling pass. Formal screen-reader execution is Not Run. |
| Persistence and determinism | Pass | 1x/2x/4x/Skip equality, random-state equality, corrupt and incompatible saves, prepared Workday, Night, Casino, results, and tutorial lifecycle pass. |
| Music lifecycle and technical playback | Pass | Catalog placement, Casino scene, Workday branch, Approved Boss baseline, and active Boss elastic-story Test pass current checks; the active Boss Test also passes its complete two-loop gate. |
| Distribution | Pass | Root truth, rollout mirror, public mirror, manifests, and rebuilt ZIP were synchronized and byte-verified after cleanup. |
| Balance | Fail | The current 250-run fixed-seed scripted-skilled policy wins 18.0 percent, below the documented 25-35 percent target. |
| Human readiness | Not Run | Human balance playtesting, formal screen-reader testing, and device-level music translation remain open. |

**Ship decision: Hold.** The frozen implementation candidate is technically
stable, but the current automated balance evidence misses the target and
several explicitly human or specialized verification rows remain unrun.

## Automated Evidence

### Core Verification

Pass:

- one standalone game HTML with no required runtime dependency;
- JavaScript, required IDs, registries, unique IDs, roster, rarity, floor
  curve, managers, resources, and Home effects;
- all 50 ordinary cards through preview, markup, and primary Complete Play;
- all ordinary paths and exceptional systems, including Brand Strategy,
  Closing, Deals, Logistics, Automation, promotion, and capstone priority;
- shared Complete Play, Replay, additional play, copied effect, Assist,
  schedule, coworker, Clock Out, Night, Weekend, promotion, and ending
  boundaries;
- worst-case resolution-chain termination and rollback after resolver errors.

### Determinism And Persistence

Pass:

- identical-state 1x, 2x, 4x, and Skip resolution;
- gameplay and random-state equality;
- valid, corrupt, and incompatible save behavior;
- Morning, prepared Workday, Clock Out, Night, Casino, result, and tutorial
  restoration;
- exactly-once Night settlement and casino continuation.

### UI And Readability

Pass:

- desktop, compact desktop, landscape phone, portrait rotation gate;
- reduced motion and 200-percent text scaling;
- Home geometry, Night Planner, Home Shop grid, schedule trackers, Resume,
  glossary keywords, task pickers, focus/tap keyword access, and visual
  overflow checks;
- representative screenshot inspection with no sampled clipping or overlap.

Not Run:

- formal screen-reader execution;
- exhaustive keyboard traversal of every picker and transition;
- exhaustive every-picker and every-transition save/restore traversal;
- rapid-input fuzzing;
- long-session memory profiling.

### Music

Pass:

- `docs/music/officewars/MUSIC_CATALOG.md` covers every audition with unique
  lifecycle labels and canonical folder placement:
  `0 Completed / 13 Approved / 3 Test / 0 Limbo / 27 Rejected`;
- Casino entrance scene completes its full focused playback gate;
- the On the Clock Approved baseline retains exact-hash two-supercycle
  evidence and its active completion branch passes current regression;
- the Approved Boss static-free baseline retains exact-hash two-loop evidence;
- the active Boss elastic-story Test passes its complete current two-loop,
  movement, waveform, transport, responsive, and cleanup gate;
- no audition is integrated into `officewarsautobattler.html`.

Open:

- Workday and Boss completion/translation checks;
- Casino entrance selection;
- device and gameplay-masking evidence;
- final music integration and shipping approval.

## Simulation Evidence

The current full runner executed 250 fixed-seed runs for each automated policy:

| Policy | Win rate |
|---|---:|
| Baseline | 0.0 percent |
| Random | 8.8 percent |
| Scripted skilled | 18.0 percent |

The policy uses the corrected Night legality gate and completes without runtime
failure. The scripted-skilled result is below the documented 25-35 percent
target, so balance readiness fails.

The policy still overrepresents a subset of trait paths. The result is evidence
of a current structural difficulty problem, not sufficient evidence for a
specific nerf or buff.

An attempted 1,000-run extended telemetry job exceeded 20 minutes and timed
out without a trustworthy result. It is recorded as Blocked and does not
replace the completed 250-run matrix.

## QA Cleanup

Corrected:

- stale current candidate hash and verification summaries;
- broken historical report paths in current status documentation;
- stale music Test summaries and Approved-versus-Completed wording;
- contradictory Casino composition/production status;
- stale current music-verifier hashes;
- active Boss verifier paths after music lifecycle moves;
- root-to-mirror drift in the general music guide and soundtrack worklog.

Removed as verified generated or abandoned artifacts:

- temporary downloaded reference audio, video, transcripts, and frame sheets;
- Python caches, empty test-temp directory, and debug log;
- obsolete Boss WAV and render-source intermediates;
- completed one-time Boss lifecycle migration scripts.

Preserved:

- the paused Boss Player-voice WAV, render source, builders, verifier, and
  continuity ledger;
- reusable verification and generation scripts;
- all Approved, Test, and Rejected standalone music HTML artifacts.

## Test Artifact Hashes

| Artifact | SHA-256 |
|---|---|
| `.officewars-full-verify.py` | `64B3F9A280FAA6F424BD306E957CCB8CD31DD010C91782ECEC0080B6E8BED682` |
| `.officewars-smoke-run.py` | `ADD032E1CC13C4715D8A9C58321684DC16E3981634DC63ECF138FD2B422E6A3C` |
| `.officewars-advanced-verify.py` | `60AC438D658455BF5FAFE08CAD42A7C2F0D44671166446A6D811FC1EC2FACCDB` |
| `.officewars-persistence-verify.py` | `3474CF05512EF62913ED6FAE43CE19A55828315B50E835B34220764F75BCE757` |
| `.officewars-task-keyword-verify.py` | `067064323EF6011AF2FC46CB824C597EFCAE142DAD749DC6873D45D69A18A4F9` |
| `.officewars-home-schedule-verify.py` | `8F4EB3921FAD48B13A08EF2AD8B774FC25847F6DB0E55B73FAA5E5DD3DF94B87` |
| `.officewars-night-planner-verify.py` | `1A73379F28E3DC764195D13B623778D202C16D964DE5903C245B66A6BF8E0A95` |
| `.officewars-visual-capture.py` | `4A22DFF2B4458D87A3932BA05D947FCD39B4C72CC2F5E28F52C98659B89BC0E5` |
| `.officewars-music-catalog-verify.py` | `EF813377D1493655A7FC2509D952591B2E377DB0506A13A4DCF411AE01B8AFCB` |
| `.officewars-casino-scene-verify.py` | `EB7B912E347CB3AC64AFF76E9FCC8B979984F3D27A79C7CCAF5C7955A91C00ED` |
| `.officewars-music-development-verify.py` | `86B6BACCA5DC35AF7E3D48A0BE14483F5F1270F04137EF7ED7BA486A677F180D` |
| `.officewars-boss-a-elastic-story-verify.py` | `A15C36952E7186AE45A676C5D74A740EFD6FB857EA1BF2F37580A1F054B2F27A` |
| `.officewars-boss-a-approved-verify.py` | `C3F279FE03CB3D64AE5209999C3D2228EB3DC1A4EFB0FEAB496EF27CDB2751A4` |
| `.officewars-workday-long-cycle-tribrid-verify.py` | `D5637C9D549AC5DCBA3366501D8C6443E422205119087E6482520ED085BB656C` |

## Distribution Evidence

- rollout manifest: `155 / 155` package files match their documented
  SHA-256 values;
- public mirror: `161` files;
- public ZIP: `161` files, extracted and compared byte-for-byte against the
  public mirror.

## Explicit Status Matrix

| Requirement group | Status |
|---|---|
| Static and standalone integrity | Pass |
| Cards, Skills, managers, Home, resources, and registries | Pass |
| Shared resolution, schedules, coworkers, economy, and endings | Pass |
| Exceptional Sales, Operations, Automation, Campaign, and Closing systems | Pass |
| Deterministic playback and Skip | Pass |
| Persistence and tutorial lifecycle | Pass |
| Desktop and responsive readability | Pass |
| Keyboard/focus/tap checks covered by automated suites | Pass |
| Formal screen-reader certification | Not Run |
| Exhaustive picker/transition restoration | Not Run |
| Rapid-input fuzzing | Not Run |
| Long-session memory profiling | Not Run |
| Music lifecycle and focused technical playback | Pass |
| Distribution mirrors, manifests, and ZIP | Pass |
| Automated balance target | Fail |
| Human balance and accessibility evidence | Not Run |
| Extended 1,000-run telemetry | Blocked |

## Next Blocker

Use a balance-specific policy and ablation pass, followed by human playtesting,
to explain the 18.0 percent skilled result before approving tuning. Do not
convert the missing screen-reader, exhaustive restoration, fuzzing, memory, or
human rows into passes without direct evidence.
