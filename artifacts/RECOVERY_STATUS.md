# Recovery status — COMPLETE (inventory ground truth)

Last updated from web sandbox inventory: **2026-07-10**.

## Ground truth: what actually existed on web

`ls -laR /home/workdir/artifacts` returned only:

| Path | Size | Notes |
|------|------|--------|
| `hebrew_bible_architecture_summary.md` | 2941 B | Present on disk |
| `leviticus_12_analysis_process.md` | 3023 B | Present on disk |
| `leviticus_12_full_model.json` | 2459 B | Present on disk |
| `searched_images/6sXg7.jpg` | ~105 KB | Present; **not downloadable to us without base64/URL** |
| `searched_images/UaBWq.jpg` | ~147 KB | Present; **not downloadable to us without base64/URL** |

**Everything else the web chat claimed to “save” never persisted** (or was only regenerated in chat). Confirmed by the inventory: 3 markdown/json files + 2 images.

### Explicitly never created (web completeness check)

- `berakhot_ch1_model.json`
- Full bilingual Mishnah Niddah files

---

## What we have locally in `artifacts/` (fuller than web sandbox)

### Lev 12 kernel
- [x] `leviticus_12_full_model.json` (web + local merge)
- [x] `lev12_2_model.json`
- [x] `leviticus_12_analysis_process.md` (local expansion > web 3 KB stub)
- [x] `leviticus_12_2_word_by_word.md`
- [x] `lev12_torah_model.py` (**local improved** female path; do not replace with web male-only)
- [x] `torah_test_scenarios.json`
- [x] `lev12_mishnah_mapping.md`
- [x] `oral_excerpts_niddah.md`
- [x] `talmud_niddah_doubled_period_he.md` (from local `Data/bavli_niddah_he.json`)

### Architecture / process
- [x] `hebrew_bible_architecture_summary.md`
- [x] `starting_point_summary.md`
- [x] `THREAD_SUMMARY.md`
- [x] `README.md`
- [x] `WEB_RECOVERY_PROMPT_FINAL.md`

### Mishnah / Berakhot from local `Data/` (read-only extract)
- [x] `mishnah_niddah_full.md` (10 chapters)
- [x] `mishnah_niddah_ch1.md` … `ch3.md`
- [x] `mishnah_berakhot_full.md` (9 chapters)
- [x] `mishnah_berakhot_ch1.md`, `ch2.md`
- [x] `berakhot_ch1_model.json` (local reconstruction)
- [x] `berakhot_ch2_model.json`

### Not recoverable without further web action
- [ ] `searched_images/6sXg7.jpg`
- [ ] `searched_images/UaBWq.jpg`  
  (Need web to paste base64, data URLs, or describe contents)

---

## Conclusion

**Text recovery is complete.** Local `artifacts/` is the canonical project store and is **richer** than the web sandbox ever retained.

Optional only: ask web for the two JPEGs as base64 if they matter.

**Principle:** Representation only. `Data/` never modified.
