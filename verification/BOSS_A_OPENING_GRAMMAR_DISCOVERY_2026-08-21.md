# Boss A Opening Grammar Discovery

Date: 2026-08-21

## Decision Boundary

`OW-MUSIC-BOSS-A-OPENING-GRAMMAR-DISCOVERY` is Rejected at
`Music Legacy/officewars-boss-a-opening-grammar-audition.html`.

Continuous Tune is the direct `Rejected` listening control at
`Music Legacy/officewars-boss-a-continuous-tune-audition.html`.

The Approved static-free rollback remains unchanged at
`Music Locked/officewars-boss-a-windowed-percussion-audition.html`.

## Listening Hypothesis

Human listening rejected Continuous Tune after the opening. Its larger
ensemble did not preserve the opening's foreground grammar because one
triangle-and-sine instrument carried nearly every later melodic attack.

This diagnostic preserves the exact `128-step` Challenge Issued source
contract, then holds one `96-step` continuation melody, harmony, roots,
galloping rhythm, backbeat, arrival accents, and loudness target constant.
Only foreground ownership changes:

- Candidate A is saw-led with triangle completions.
- Candidate B interlocks saw and triangle within each phrase.
- Candidate C uses short triangle sparks while saw carries structural notes.

The opening's final triangle `C5` supplies the inherited boundary note. The
first new attack is `D5` two steps later, so the handoff is part of the phrase
rather than a repeated section start. The continuation contains three neutral
`32-step` phrases and does not claim a complete Boss form.

## Render Evidence

- Candidate A WAV SHA-256:
  `9D5138F5BF59AEEB3E7F208ED91FE9FD34BC001BAA3223016EE0A3695B746DED`
- Candidate B WAV SHA-256:
  `7071813DEAC22D60A028B240FEECA54FE7D8727ED980E6D197883D30721BBAB6`
- Candidate C WAV SHA-256:
  `32E1199C726EBB1BD7B5D0F523E8CDFDA191132909CA016B3525600F36420705`
- Continuation RMS:
  `0.006799 / 0.007048 / 0.007043`
- Maximum adjacent-sample delta: `0.009399`
- Seam delta: `0.000092`
- Maximum source peak: `0.051758`
- Maximum projected peak at the `1.30` playback multiplier: `0.067285`

All three renders are stereo `24kHz`, have distinct hashes, and preserve the
opening after the new ending's bounded circular-render tail decays. Source
verification separately proves the exact opening notes, harmony, roots,
rhythm profile, undercurrent, timbres, and lead behavior.

## Browser Evidence

The standalone desktop audition passes:

- exact embedded hashes and byte lengths;
- dark-mode default and persistent theme switching;
- play, pause, resume, stop/restart, seek, and four direct bookmarks;
- live waveform rendering;
- thirty rapid A/B/C switches with one reusable media-source graph;
- the exact `1.30` effective full-volume gain; and
- two uninterrupted normal-speed loops of each complete candidate.

Wrapper SHA-256:
`FB3117394C4D79AEC73ACC5F86FD732FBFE5FC4DC74DA0FCF668190A38AA9DF2`

Continuous Tune's retained Full Ensemble and Melody + Pulse WAV hashes remain
`14EA8BCF84636D427709151ABC8069B5910F3D077DB3324ABD613B67CB44FF2B`
and
`AFC65207C608B656FBF165D2A80988BDD2989482DD337E0314C70B02A00F98D1`.

Human listening found all three versions closer, but rejected their tunes and
handoffs as still too far from Challenge Issued. Next Movement superseded this
artifact and was itself rejected; the active Boss A Test is now
`OW-MUSIC-BOSS-A-SECOND-MOVEMENT-SKETCHES`.
