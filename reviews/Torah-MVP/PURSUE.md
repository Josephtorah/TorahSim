# Ideas worth pursuing — Torah-MVP

**Source:** `<old-home>/code/Torah-MVP`  
**From:** SCORECARD + AUDIT-2026-07-10  
**Confidence labels:** high = re-ran · medium = partial · low = hypothesis

| # | Idea | Why | Confidence |
|---|------|-----|------------|
| 1 | **Four-layer Unicode model** (C/V/cantillation/punct + transition grammar) | Reproduced counts; foundation for any parser | high |
| 2 | **פ/ס native block segmentation** (know 690 / 669 / 673) | Text’s own blocks beat heuristics | high |
| 3 | **Cantillation → verse trees / half-verse splits** (in-repo + LREC) | Machine-readable structure; legal A\|B patterns | high |
| 4 | **Structure-first compile** (torahc2 style) over keyword-first | Coverage and honesty improved when markers lead | high |
| 5 | **Epistemic discipline** (FINDINGS §7, fabrication notes; careful claim wording) | Separates fact / interpretation / intent | high |
| 6 | **Fix-then-use classification** only if needed (negation לא/אין) | Lev 11 currently untrustworthy for verdicts | medium |

**Do not pursue from this folder:** “1/106” claim, main-branch hash linker, Lev 12 timers here (not implemented), runtime-as-live-Torah-reader, intent-as-proven-program.
