# Final web recovery prompt — paste into Grok web chat

Use this to pull **everything still missing** from the web sandbox/thread. We already have the Lev 12 kernel and full Mishnah extracts locally.

---

```markdown
# FINAL RECOVERY — paste every remaining artifact in full

I am reconstructing our entire Torah architecture project locally.  
I **already have** these (do NOT re-paste unless you have a longer/better version):

- leviticus_12_full_model.json
- lev12_2_model.json
- leviticus_12_analysis_process.md
- leviticus_12_2_word_by_word.md
- lev12_torah_model.py
- torah_test_scenarios.json
- lev12_mishnah_mapping.md
- hebrew_bible_architecture_summary.md
- starting_point_summary.md
- oral excerpts for Niddah 31a / Mishnah Niddah 3:7
- mishnah_niddah full + berakhot full (from my local Data)

## Rules
1. For each remaining file: `### FILE: exact_name` then a fenced code block with **full body**.
2. No “✅ Saved” without pasting content.
3. If a file never existed, say `MISSING: filename — never created`.
4. Representation only — not autonomous law generation.
5. Split across messages if needed (label Part 1/N).

## A. Workspace inventory (do first)
1. List **every** path under `/home/workdir/artifacts` (recursive `find` or `ls -laR`).
2. For each file: name, size, one-line description.
3. Flag which ones you can still read.

## B. Remaining models / docs (paste full contents)

### FILE: berakhot_ch1_model.json
(Full JSON if you created it — timing of Shema, Deut 6:4–9 links)

### FILE: berakhot_ch2_model.json
(Only if longer than the short version you already sent)

### FILE: berakhot_ch1_mapping.md (or similar)
Verse-by-verse Torah → Mishnah Berakhot mapping

### FILE: berakhot_ch2_mapping.md

### FILE: mishnah_niddah_ch1_bilingual.md
### FILE: mishnah_niddah_ch2_bilingual.md
### FILE: mishnah_niddah_ch3_bilingual.md
(Hebrew + English if they existed)

### FILE: mishnah_niddah_full.md
(Only if English or bilingual; I already have Hebrew from local Data)

### FILE: talmud_niddah_31a_full.md
Full Hebrew + English of the sugya we used (beyond the one remorse sentence)

### FILE: lev12_taamim_tree_diagram.md
Exact text diagrams for Lev 12:2 and full chapter as last refined

### FILE: any CFG / parser scripts beyond lev12_torah_model.py
(e.g. cantillation parser, treebank export, graph scripts)

### FILE: sefer_yetzirah* or 231_gates* or chagigah* models
(If any were created in the thread)

### FILE: searched_images or other non-text artifacts
Describe or re-export if possible

## C. Anything else
If the inventory shows files not listed above, paste **all of them** in full after section B.

## D. Completeness check
End with:
- PASTED: [list]
- MISSING_NEVER_CREATED: [list]
- UNREADABLE: [list]

Start with **A (inventory)** then **B**.
```

---

After the web replies, paste the whole message into Grok terminal; files will be written into `artifacts/`.
