# LAW ERA — the ten showcase blocks (owner-approved reference list)

Owner order 2026-08-10: narrative analysis paused; law focus. All ten blocks
to be scanned under the oral-torah scan process (full link inversion per the
FULL ORAL TORAH LAW — scope narrowing only by explicit owner ruling; the
Core Shelf proposal remains PENDING, not adopted). Scans feed the ordered
re-derivation of the covering units.

| # | Block | Span | Code concept | Chain decompiler | Status |
|---|-------|------|--------------|------------------|--------|
| 1 | Slave-term laws | Exod 21:1-11 | first case-law cascade: כי ("when/if") conditionals, 6-yr timer, ear-rite opt-out flag | Kiddushin ch.1, Mekhilta Nezikin | **SCAN COMPLETE**; draft machine `exo_21_v2_block1_DRAFT.py`; **scene catalog** `logic/gork/scene_catalog_exo_21_block1_2026-08-11.json` (48 fixtures for later tests / Pass B) |
| 2 | Homicide & injury | Exod 21:12-27 | mens-rea fork, refuge commutation, עין תחת עין ("eye for eye") -> damages semantics | Bava Kamma 83b-84a, Sanhedrin, Makkot | **SCAN COMPLETE** 2026-08-11: 36 bites, 1,639 rows, census satisfied; chapter ledger at 3,601; notes mirror `scratch_mirror/law02_scan_notes.md`; **MACHINE CODED** 2026-08-12: `exo_21_v2_block2_DRAFT.py` asserts green + 24-edge dependency proof (12 resolved incl. Judah's surety-תחת "in place of" and Jacob's אסון "calamity" / 12 forward incl. 1 Kgs 2:28 Joab); claims `manifests/law02_exo_21_12_27_claims.json` (43); gloss_lint clean — **ALL THREE EXOD-21 BLOCKS NOW CODED** |
| 3 | Goring ox | Exod 21:28-36 (+21:37 tail) | state machine: תם ("innocent") -> מועד ("forewarned"), liability escalation; tail adds the 4/5 theft tariff of 21:37 | Bava Kamma ch.1-4, ch.7 | **SCAN COMPLETE** 2026-08-12 + **21:37 TAIL COMPLETE** same day: 23 clips block proper (1,130 rows) + 4 tail clips (bites 24-27 + tanakh close, 172 rows); chapter ledger 4,903 = census EXACT — **EXOD 21 CHAPTER GATE GREEN, coverage continuous 21:1-37** (full exo_21_the_ordinances span); notes mirror `scratch_mirror/law03_scan_notes.md`; **MACHINE CODED** 2026-08-12: `exo_21_v2_block3_DRAFT.py` asserts green + 14-edge dependency proof; claims `manifests/law03_exo_21_28_37_claims.json` (28) |
| 4 | Theft & four guardians | Exod 22:1-14 | liability lookup table (4 custody classes × fates) reconstructed by the chain | Bava Kamma ch.7, Bava Metzia ch.3+7, Shevuot | queued |
| 5 | Skin-affliction protocol | Lev 13-14 | decision tree with 7-day timers, re-inspection loops, טמא/טהור ("impure/pure") states | Negaim (Mishnah), Sifra Tazria | queued |
| 6 | Kashrut classifier | Lev 11 | type system: boolean feature predicates (hooves AND cud; fins AND scales), blacklist | Chullin ch.3, Sifra Shemini | queued |
| 7 | Shemittah & Yovel | Lev 25 | nested schedulers: 7-yr loop in 7×7->50 cycle; land/debt/person resets | Arakhin, Kiddushin, Sifra Behar | queued |
| 8 | Zelophehad daughters | Num 27 + 36 | the amendment cycle: hard case -> escalation -> patch -> constraining patch | Bava Batra ch.8, Sifrei Pinchas | queued |
| 9 | Vows & annulment | Num 30 | speech-act transactions with same-day rollback windows | Nedarim, Sifrei Matot | queued |
| 10 | Refuge cities | Num 35 | deployed commutation system; release on unrelated event (high priest's death) | Makkot ch.2, Sifrei Masei | queued |

Honorable mentions (not in the ten, on record): Exod 12 (calendar
instantiation + timed protocol; frozen, law-lens re-scan candidate),
Exod 20 Decalogue (constitutional layer vs. case law), Lev 27 (valuation
lookup table), Num 19 (red heifer — flagship underivable constant).

Unit mapping note: blocks 1-3 subdivide frozen unit exo_21_the_ordinances
(span 21:1-37, FWD-8); block 4 falls in exo_22_property_social territory.
**CHAPTER ASSEMBLED 2026-08-12: `exo_21_v2_DRAFT.py`** — blocks 1-3
imported unchanged under one World (statute-0 runtime, persistent state,
verdicts as state-writes) + 7 cross-block seam laws asserted + the merged
60-edge chapter dependency proof (2 internal / 31 resolved / 27 forward);
all green, gloss_lint clean. v2 freeze awaits owner word.
The July-24 exo_2x files (slave_person, ox_pit, decalogue_altar) are
drift-era drafts, not the current frozen layer.

Origin: gen_08 read-only check (2026-08-10) proved the scan method — 0
contradictions, ~150 operator-grade additions, ~1 in 4 findings
multi-witness. Reports: Desktop epub + gen08_v1_vs_v2_code_comparison.md.
