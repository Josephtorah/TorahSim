# Fetch log — re-fetchable Sefaria caches (gitignored 2026-07-30)

The caches below are NOT tracked in git (owner decision 2026-07-30: repo-size
discipline). The fetchers are committed and resumable; re-fetching restores
everything. The permanent record is never the cache — it is the citations,
verdicts, and quotes in logic/oral_triage/ and logic/units/.

| date | cache | command | scope | result |
|------|-------|---------|-------|--------|
| 2026-07-30 | Data/sefaria_links/ | `python3 fetch_oral_links.py Gen "1:1-31,2:1-3"` | creation week, 34 verses | 34 files · 13,940 links · 1.3 MB |
| 2026-07-30 | Data/sefaria_texts/ | `python3 fetch_oral_texts.py Gen.1.1 Gen.1.5` | day-1 tier-1 sources | 483 files · 0 failures · 3.2 MB |
| 2026-07-30 | (no cache — evidence queries) | `python3 logic/written_echo/verify_rarity.py …` | 5 search-wrapper queries (4 echo signatures + 1 probe) | rarity counts recorded in logic/written_echo/v1/edges.yaml |
| 2026-07-30 | (no cache — 4 single verses) | api/texts Jer 4:23, Isa 45:7, Ps 104:2, Prov 8:22 | echo-edge target texts | Hebrew recorded in edges.yaml; English is own literal gloss (API returned copyrighted JPS 2023) |
| 2026-07-30 | (no cache — 1 range) | api/texts Onkelos_Genesis.1.14-19 | gen_04 derivation Tier-A read (charter §4.1) | findings recorded in gen_04_lights_calendar.yaml (yehon plural; le-mimnei counting verb; le-mishlat; revi'a'i) |
| 2026-07-30 | Data/sefaria_texts/ | `python3 fetch_oral_texts.py Gen.1.14 Gen.1.19` | day-4 tier-1 sources | 130 new files · 35 already held · 0 failures |
| 2026-07-30 | (no cache — 1 range) | api/texts Onkelos_Genesis.1.20-23 | gen_05 derivation Tier-A read (charter §4.1) | findings recorded in gen_05_swarms_blessing.yaml (yirchashun — delegation + imperfect retained; NO receipt token added, matching MT; aphel archishu — waters as causer; ofa de-farach re-verbalizes kanaf, symmetric receipt; imperatives pushu/sgu/mlu retained, fowl 3ms yisgei) |
| 2026-07-30 | Data/sefaria_texts/ | `python3 fetch_oral_texts.py Gen.1.20 Gen.1.23` | day-5 tier-1 sources | 88 new files · 41 already held · 0 failures |
| 2026-07-30 | (no cache — 1 range) | api/texts Bava_Batra.74b.6-8 | §4.1 promotion fetch: the taninim sugya continues past the enumerated section (74b:5) into the mate tradition the [OPEN] ktiv dossier names | male-and-female created; male castrated, female slain and salted for the righteous (Isa 27:1); recorded in the day-5 ledger + ORAL_taninim_defective upgrade |
| 2026-07-31 | Data/sefaria_texts/ | api/texts Onkelos Leviticus 13:1-8 (8 sequential per-verse requests, 0.5s apart) | lev_13_intake_quarantine derivation (owner order "yes now derive it"): Tier-A translation read at derive time per charter section 4.1 — FIRST LAW UNIT | findings: tzara'at rendered SEGIRU/SEGIRUTA ("the shutting-disease" — the condition named by its own quarantine procedure, on the sagar root of Gen 2:21/7:16); amad be-einav ("stood in its eyes") resolved to kam kad havah ("stood as it was" — appearance reading); sapachat AND mispachat leveled to one word (adita, "the added one"); se'et (raised mark) rendered amka ("deep-spot") — Shevuot 6a-b shades dossier queued; declaratives retained (visa'ev/vidakkei) |
| 2026-07-31 | (no cache — metadata only) | api/name lookup x2 ("Erkhei Midrash" / its Hebrew title) | owner asked whether Bacher's exegetical-terminology lexicon can be read; checked whether Sefaria carries the Rabinovitz Hebrew translation | NOT on Sefaria; Bacher term-testing done against our existing local cache instead (logic/middot_scan/bacher_scan.py) — no text fetched |
| 2026-07-31 | Data/sefaria_texts/ | api/texts Onkelos Genesis 2:1-3 (3 sequential per-verse requests, 0.5s apart) | day-7 derivation (owner order "Lets finish the 7 days"): Tier-A translation read at derive time per charter section 4.1 | findings: ve-ishtakhlelu — the agentless passive completion RETAINED; the SEVENTH-day dating of the finishing act retained unharmonized; ve-NACH ("and He RESTED") glossing va-yishbot ("and He CEASED") both times — cessation rendered as rest; kadish yateh retained; the la'asot ("to make") tail retained (di vra le-me'bad) |
| 2026-07-31 | Data/sefaria_texts/ | api/texts Onkelos Genesis 1:24-31 (8 sequential per-verse requests, 0.5s apart) | day-6 derivation (owner order "Lets finish the 7 days"): Tier-A translation read at derive time per charter section 4.1 | 8 findings incl.: na'avid ("let us make") — the 1cp plural RETAINED by the anti-anthropomorphic translator (contrast day 4's number normalization); be-tzalma d-Adonai ("in the image of THE LORD") — the plural's referent resolved to the single God at 1:27; takin lachada ("exceedingly well-ordered") for tov me'od at 1:31 vs plain tav ("good") for the local tests — the global test read as an arrangement check; both receipts (1:24, 1:30) retained |
| 2026-07-31 | Data/sefaria_texts/ | api/texts Chullin 60a sections (6 sequential requests: 60a:7-8, 60a:3-5 probes, full 60a page) | middot-detector calibration: the grasses kal-va-chomer ("light and heavy" a-fortiori) passage cited by gen_03's ORAL_grasses note was verified-local earlier but never cached | located + cached Chullin 60a:10 (grasses draw the inference), 60a:11 (the argument spelled out with "how much more so"), 60a:13 (grafting two grasses); also cached 60a:7-8 (Adam's ox — probe overshoot, kept) |

Politeness contract (owner order): sequential requests, 0.5s delay, small
ranges per invocation — never a whole book at once.
- 2026-08-01 · `Onkelos Genesis 2:4` -> `Data/sefaria_texts/Onkelos_Genesis_2_4__715ea898.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:5` -> `Data/sefaria_texts/Onkelos_Genesis_2_5__84903187.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:6` -> `Data/sefaria_texts/Onkelos_Genesis_2_6__2ab65680.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:7` -> `Data/sefaria_texts/Onkelos_Genesis_2_7__7cf77abe.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:8` -> `Data/sefaria_texts/Onkelos_Genesis_2_8__1d311596.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:9` -> `Data/sefaria_texts/Onkelos_Genesis_2_9__e8f45b6b.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:10` -> `Data/sefaria_texts/Onkelos_Genesis_2_10__040b267a.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:11` -> `Data/sefaria_texts/Onkelos_Genesis_2_11__ff5b4a3b.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:12` -> `Data/sefaria_texts/Onkelos_Genesis_2_12__08777467.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:13` -> `Data/sefaria_texts/Onkelos_Genesis_2_13__33c98a05.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:14` -> `Data/sefaria_texts/Onkelos_Genesis_2_14__0492d31f.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:15` -> `Data/sefaria_texts/Onkelos_Genesis_2_15__07237f32.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:16` -> `Data/sefaria_texts/Onkelos_Genesis_2_16__6454b489.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:17` -> `Data/sefaria_texts/Onkelos_Genesis_2_17__0f431d11.json` · Tier-A gen_08 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:18` -> `Data/sefaria_texts/Onkelos_Genesis_2_18__83fd48ef.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:19` -> `Data/sefaria_texts/Onkelos_Genesis_2_19__49a71d58.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:20` -> `Data/sefaria_texts/Onkelos_Genesis_2_20__ec781def.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:21` -> `Data/sefaria_texts/Onkelos_Genesis_2_21__093f8815.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:22` -> `Data/sefaria_texts/Onkelos_Genesis_2_22__f7bd20cf.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:23` -> `Data/sefaria_texts/Onkelos_Genesis_2_23__6cdba96b.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:24` -> `Data/sefaria_texts/Onkelos_Genesis_2_24__38f9dc78.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 2:25` -> `Data/sefaria_texts/Onkelos_Genesis_2_25__924be7d2.json` · Tier-A gen_09 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:1` -> `Data/sefaria_texts/Onkelos_Genesis_3_1__9b9ae6cb.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:2` -> `Data/sefaria_texts/Onkelos_Genesis_3_2__73dba666.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:3` -> `Data/sefaria_texts/Onkelos_Genesis_3_3__e3cf0404.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:4` -> `Data/sefaria_texts/Onkelos_Genesis_3_4__31276e9b.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:5` -> `Data/sefaria_texts/Onkelos_Genesis_3_5__c81bd3a9.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:6` -> `Data/sefaria_texts/Onkelos_Genesis_3_6__fddd6eb3.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:7` -> `Data/sefaria_texts/Onkelos_Genesis_3_7__f47bfe6d.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:8` -> `Data/sefaria_texts/Onkelos_Genesis_3_8__df9a4ba7.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:9` -> `Data/sefaria_texts/Onkelos_Genesis_3_9__27f66a4b.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:10` -> `Data/sefaria_texts/Onkelos_Genesis_3_10__b3401672.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:11` -> `Data/sefaria_texts/Onkelos_Genesis_3_11__fa5f0a79.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:12` -> `Data/sefaria_texts/Onkelos_Genesis_3_12__4e789f3d.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:13` -> `Data/sefaria_texts/Onkelos_Genesis_3_13__90e438b8.json` · Tier-A gen_10 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:14` -> `Data/sefaria_texts/Onkelos_Genesis_3_14__5b539e52.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:15` -> `Data/sefaria_texts/Onkelos_Genesis_3_15__7ba9f9a8.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:16` -> `Data/sefaria_texts/Onkelos_Genesis_3_16__33cf7cc4.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:17` -> `Data/sefaria_texts/Onkelos_Genesis_3_17__170ece0a.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:18` -> `Data/sefaria_texts/Onkelos_Genesis_3_18__a6d3345c.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:19` -> `Data/sefaria_texts/Onkelos_Genesis_3_19__6037462f.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:20` -> `Data/sefaria_texts/Onkelos_Genesis_3_20__d7bcec76.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:21` -> `Data/sefaria_texts/Onkelos_Genesis_3_21__4db2caff.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:22` -> `Data/sefaria_texts/Onkelos_Genesis_3_22__28a55fcf.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:23` -> `Data/sefaria_texts/Onkelos_Genesis_3_23__5fca7f52.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 3:24` -> `Data/sefaria_texts/Onkelos_Genesis_3_24__6ead041f.json` · Tier-A gen_11 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:1` -> `Data/sefaria_texts/Onkelos_Genesis_4_1__a9e45d01.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:2` -> `Data/sefaria_texts/Onkelos_Genesis_4_2__05830b78.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:3` -> `Data/sefaria_texts/Onkelos_Genesis_4_3__65723d39.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:4` -> `Data/sefaria_texts/Onkelos_Genesis_4_4__da57071f.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:5` -> `Data/sefaria_texts/Onkelos_Genesis_4_5__226f3d03.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:6` -> `Data/sefaria_texts/Onkelos_Genesis_4_6__dcb54711.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:7` -> `Data/sefaria_texts/Onkelos_Genesis_4_7__708fd8a8.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:8` -> `Data/sefaria_texts/Onkelos_Genesis_4_8__e261c099.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:9` -> `Data/sefaria_texts/Onkelos_Genesis_4_9__646e18c9.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:10` -> `Data/sefaria_texts/Onkelos_Genesis_4_10__415783fd.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:11` -> `Data/sefaria_texts/Onkelos_Genesis_4_11__95d5e700.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:12` -> `Data/sefaria_texts/Onkelos_Genesis_4_12__55269a8d.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:13` -> `Data/sefaria_texts/Onkelos_Genesis_4_13__eb2e002d.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:14` -> `Data/sefaria_texts/Onkelos_Genesis_4_14__6deb330f.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:15` -> `Data/sefaria_texts/Onkelos_Genesis_4_15__e02dc4e8.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:16` -> `Data/sefaria_texts/Onkelos_Genesis_4_16__92bc4ec9.json` · Tier-A gen_12 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:17` -> `Data/sefaria_texts/Onkelos_Genesis_4_17__7a1baad9.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:18` -> `Data/sefaria_texts/Onkelos_Genesis_4_18__a34901a7.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:19` -> `Data/sefaria_texts/Onkelos_Genesis_4_19__438c4aa7.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:20` -> `Data/sefaria_texts/Onkelos_Genesis_4_20__1b3946ca.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:21` -> `Data/sefaria_texts/Onkelos_Genesis_4_21__c0f15fbc.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:22` -> `Data/sefaria_texts/Onkelos_Genesis_4_22__b491f742.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:23` -> `Data/sefaria_texts/Onkelos_Genesis_4_23__8ef5a8b4.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:24` -> `Data/sefaria_texts/Onkelos_Genesis_4_24__3367ba0f.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:25` -> `Data/sefaria_texts/Onkelos_Genesis_4_25__a973d7ba.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 4:26` -> `Data/sefaria_texts/Onkelos_Genesis_4_26__0c894d43.json` · Tier-A gen_13 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:1` -> `Data/sefaria_texts/Onkelos_Genesis_5_1__4659e0a3.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:2` -> `Data/sefaria_texts/Onkelos_Genesis_5_2__31d16464.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:3` -> `Data/sefaria_texts/Onkelos_Genesis_5_3__e0e81c33.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:4` -> `Data/sefaria_texts/Onkelos_Genesis_5_4__a495824d.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:5` -> `Data/sefaria_texts/Onkelos_Genesis_5_5__3a41bbce.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:6` -> `Data/sefaria_texts/Onkelos_Genesis_5_6__a00529bb.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:7` -> `Data/sefaria_texts/Onkelos_Genesis_5_7__a5b7d335.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:8` -> `Data/sefaria_texts/Onkelos_Genesis_5_8__f235ddaf.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:9` -> `Data/sefaria_texts/Onkelos_Genesis_5_9__68ceb0a2.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:10` -> `Data/sefaria_texts/Onkelos_Genesis_5_10__4a4840c3.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:11` -> `Data/sefaria_texts/Onkelos_Genesis_5_11__6e971976.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:12` -> `Data/sefaria_texts/Onkelos_Genesis_5_12__ccbb5dbb.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:13` -> `Data/sefaria_texts/Onkelos_Genesis_5_13__3c92548a.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:14` -> `Data/sefaria_texts/Onkelos_Genesis_5_14__5ffdaa01.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:15` -> `Data/sefaria_texts/Onkelos_Genesis_5_15__594d0585.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:16` -> `Data/sefaria_texts/Onkelos_Genesis_5_16__42322791.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:17` -> `Data/sefaria_texts/Onkelos_Genesis_5_17__0c74f27d.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:18` -> `Data/sefaria_texts/Onkelos_Genesis_5_18__fdf2d3d3.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:19` -> `Data/sefaria_texts/Onkelos_Genesis_5_19__995a5e4b.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:20` -> `Data/sefaria_texts/Onkelos_Genesis_5_20__a770fb5a.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:21` -> `Data/sefaria_texts/Onkelos_Genesis_5_21__5a5ca81d.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:22` -> `Data/sefaria_texts/Onkelos_Genesis_5_22__0013be86.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:23` -> `Data/sefaria_texts/Onkelos_Genesis_5_23__f0b203c7.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:24` -> `Data/sefaria_texts/Onkelos_Genesis_5_24__59705a12.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:25` -> `Data/sefaria_texts/Onkelos_Genesis_5_25__147a2d7f.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:26` -> `Data/sefaria_texts/Onkelos_Genesis_5_26__1c463e0b.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:27` -> `Data/sefaria_texts/Onkelos_Genesis_5_27__01ecf3f0.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:28` -> `Data/sefaria_texts/Onkelos_Genesis_5_28__1828ec72.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:29` -> `Data/sefaria_texts/Onkelos_Genesis_5_29__c8aad596.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:30` -> `Data/sefaria_texts/Onkelos_Genesis_5_30__8e40aa9b.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:31` -> `Data/sefaria_texts/Onkelos_Genesis_5_31__92768731.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 5:32` -> `Data/sefaria_texts/Onkelos_Genesis_5_32__4a5fc11d.json` · Tier-A gen_14 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:1` -> `Data/sefaria_texts/Onkelos_Genesis_6_1__732e6509.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:2` -> `Data/sefaria_texts/Onkelos_Genesis_6_2__0a86ea19.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:3` -> `Data/sefaria_texts/Onkelos_Genesis_6_3__5a50db26.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:4` -> `Data/sefaria_texts/Onkelos_Genesis_6_4__6077b3b4.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:5` -> `Data/sefaria_texts/Onkelos_Genesis_6_5__d26d5bcb.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:6` -> `Data/sefaria_texts/Onkelos_Genesis_6_6__29e9ac0b.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:7` -> `Data/sefaria_texts/Onkelos_Genesis_6_7__db867dde.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:8` -> `Data/sefaria_texts/Onkelos_Genesis_6_8__09c9037e.json` · Tier-A gen_15 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:9` -> `Data/sefaria_texts/Onkelos_Genesis_6_9__f3f60a1b.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:10` -> `Data/sefaria_texts/Onkelos_Genesis_6_10__734dadab.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:11` -> `Data/sefaria_texts/Onkelos_Genesis_6_11__8dd002fc.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:12` -> `Data/sefaria_texts/Onkelos_Genesis_6_12__876d4f6b.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:13` -> `Data/sefaria_texts/Onkelos_Genesis_6_13__02a08605.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:14` -> `Data/sefaria_texts/Onkelos_Genesis_6_14__0aea17f6.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:15` -> `Data/sefaria_texts/Onkelos_Genesis_6_15__f321c657.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:16` -> `Data/sefaria_texts/Onkelos_Genesis_6_16__01848cd1.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:17` -> `Data/sefaria_texts/Onkelos_Genesis_6_17__a57b6685.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:18` -> `Data/sefaria_texts/Onkelos_Genesis_6_18__505060a6.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:19` -> `Data/sefaria_texts/Onkelos_Genesis_6_19__a3b01b6f.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:20` -> `Data/sefaria_texts/Onkelos_Genesis_6_20__2c8167d9.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:21` -> `Data/sefaria_texts/Onkelos_Genesis_6_21__56656ad3.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 6:22` -> `Data/sefaria_texts/Onkelos_Genesis_6_22__cb636225.json` · Tier-A gen_16 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:1` -> `Data/sefaria_texts/Onkelos_Genesis_7_1__9706ca2c.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:2` -> `Data/sefaria_texts/Onkelos_Genesis_7_2__e473f867.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:3` -> `Data/sefaria_texts/Onkelos_Genesis_7_3__809d63bc.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:4` -> `Data/sefaria_texts/Onkelos_Genesis_7_4__9f9d671c.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:5` -> `Data/sefaria_texts/Onkelos_Genesis_7_5__1b384df4.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:6` -> `Data/sefaria_texts/Onkelos_Genesis_7_6__f28de5d8.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:7` -> `Data/sefaria_texts/Onkelos_Genesis_7_7__aa5a75d2.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:8` -> `Data/sefaria_texts/Onkelos_Genesis_7_8__4b214274.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:9` -> `Data/sefaria_texts/Onkelos_Genesis_7_9__896a11dd.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:10` -> `Data/sefaria_texts/Onkelos_Genesis_7_10__02ffcdde.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:11` -> `Data/sefaria_texts/Onkelos_Genesis_7_11__7198f89b.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:12` -> `Data/sefaria_texts/Onkelos_Genesis_7_12__be76a4ca.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:13` -> `Data/sefaria_texts/Onkelos_Genesis_7_13__74eb15a8.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:14` -> `Data/sefaria_texts/Onkelos_Genesis_7_14__9ffb2365.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:15` -> `Data/sefaria_texts/Onkelos_Genesis_7_15__02b20dd5.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:16` -> `Data/sefaria_texts/Onkelos_Genesis_7_16__50fb8927.json` · Tier-A gen_17 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:17` -> `Data/sefaria_texts/Onkelos_Genesis_7_17__0d6ee2e2.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:18` -> `Data/sefaria_texts/Onkelos_Genesis_7_18__a5fceabd.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:19` -> `Data/sefaria_texts/Onkelos_Genesis_7_19__edce0a05.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:20` -> `Data/sefaria_texts/Onkelos_Genesis_7_20__cded2c95.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:21` -> `Data/sefaria_texts/Onkelos_Genesis_7_21__190fa36f.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:22` -> `Data/sefaria_texts/Onkelos_Genesis_7_22__911ebb0a.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:23` -> `Data/sefaria_texts/Onkelos_Genesis_7_23__a06f5c09.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 7:24` -> `Data/sefaria_texts/Onkelos_Genesis_7_24__0d3a9b30.json` · Tier-A gen_18 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:1` -> `Data/sefaria_texts/Onkelos_Genesis_8_1__8e75f461.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:2` -> `Data/sefaria_texts/Onkelos_Genesis_8_2__ffd038f8.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:3` -> `Data/sefaria_texts/Onkelos_Genesis_8_3__e7fc4dd4.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:4` -> `Data/sefaria_texts/Onkelos_Genesis_8_4__fe2a6639.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:5` -> `Data/sefaria_texts/Onkelos_Genesis_8_5__70a06035.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:6` -> `Data/sefaria_texts/Onkelos_Genesis_8_6__e25c730f.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:7` -> `Data/sefaria_texts/Onkelos_Genesis_8_7__b1cb257b.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:8` -> `Data/sefaria_texts/Onkelos_Genesis_8_8__f61f2258.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:9` -> `Data/sefaria_texts/Onkelos_Genesis_8_9__8fb47a7e.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:10` -> `Data/sefaria_texts/Onkelos_Genesis_8_10__40f95451.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:11` -> `Data/sefaria_texts/Onkelos_Genesis_8_11__cf5875b3.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:12` -> `Data/sefaria_texts/Onkelos_Genesis_8_12__f279cd8a.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:13` -> `Data/sefaria_texts/Onkelos_Genesis_8_13__67b88b66.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:14` -> `Data/sefaria_texts/Onkelos_Genesis_8_14__2661d9a0.json` · Tier-A gen_19 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:15` -> `Data/sefaria_texts/Onkelos_Genesis_8_15__4f811ec8.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:16` -> `Data/sefaria_texts/Onkelos_Genesis_8_16__747dca64.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:17` -> `Data/sefaria_texts/Onkelos_Genesis_8_17__76e1e611.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:18` -> `Data/sefaria_texts/Onkelos_Genesis_8_18__cf661b02.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:19` -> `Data/sefaria_texts/Onkelos_Genesis_8_19__7b9cfb12.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:20` -> `Data/sefaria_texts/Onkelos_Genesis_8_20__e0b9f90e.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:21` -> `Data/sefaria_texts/Onkelos_Genesis_8_21__53a278e1.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-01 · `Onkelos Genesis 8:22` -> `Data/sefaria_texts/Onkelos_Genesis_8_22__a5ff7704.json` · Tier-A gen_20 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:1` -> `Data/sefaria_texts/Onkelos_Genesis_9_1__1545e67c.json` · Tier-A gen_21 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:2` -> `Data/sefaria_texts/Onkelos_Genesis_9_2__d1f9ca23.json` · Tier-A gen_21 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:3` -> `Data/sefaria_texts/Onkelos_Genesis_9_3__f5dbd097.json` · Tier-A gen_21 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:4` -> `Data/sefaria_texts/Onkelos_Genesis_9_4__dd9dca6d.json` · Tier-A gen_21 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:5` -> `Data/sefaria_texts/Onkelos_Genesis_9_5__6c936c83.json` · Tier-A gen_21 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:6` -> `Data/sefaria_texts/Onkelos_Genesis_9_6__849b0b42.json` · Tier-A gen_21 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:7` -> `Data/sefaria_texts/Onkelos_Genesis_9_7__26021242.json` · Tier-A gen_21 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:8` -> `Data/sefaria_texts/Onkelos_Genesis_9_8__66b5701d.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:9` -> `Data/sefaria_texts/Onkelos_Genesis_9_9__09653189.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:10` -> `Data/sefaria_texts/Onkelos_Genesis_9_10__604cef15.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:11` -> `Data/sefaria_texts/Onkelos_Genesis_9_11__591093e9.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:12` -> `Data/sefaria_texts/Onkelos_Genesis_9_12__0ebabeb0.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:13` -> `Data/sefaria_texts/Onkelos_Genesis_9_13__4e1fda43.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:14` -> `Data/sefaria_texts/Onkelos_Genesis_9_14__8ad6e212.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:15` -> `Data/sefaria_texts/Onkelos_Genesis_9_15__6329d19e.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:16` -> `Data/sefaria_texts/Onkelos_Genesis_9_16__1e78343d.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:17` -> `Data/sefaria_texts/Onkelos_Genesis_9_17__f161a940.json` · Tier-A gen_22 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:18` -> `Data/sefaria_texts/Onkelos_Genesis_9_18__7d75383c.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:19` -> `Data/sefaria_texts/Onkelos_Genesis_9_19__7123c317.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:20` -> `Data/sefaria_texts/Onkelos_Genesis_9_20__19becffc.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:21` -> `Data/sefaria_texts/Onkelos_Genesis_9_21__24945e8d.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:22` -> `Data/sefaria_texts/Onkelos_Genesis_9_22__01007629.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:23` -> `Data/sefaria_texts/Onkelos_Genesis_9_23__6d4ea8da.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:24` -> `Data/sefaria_texts/Onkelos_Genesis_9_24__7096acd4.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:25` -> `Data/sefaria_texts/Onkelos_Genesis_9_25__275e3f7a.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:26` -> `Data/sefaria_texts/Onkelos_Genesis_9_26__bf7a7fa0.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:27` -> `Data/sefaria_texts/Onkelos_Genesis_9_27__cf1dcd70.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:28` -> `Data/sefaria_texts/Onkelos_Genesis_9_28__735aef82.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 9:29` -> `Data/sefaria_texts/Onkelos_Genesis_9_29__d27059cd.json` · Tier-A gen_23 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:1` -> `Data/sefaria_texts/Onkelos_Genesis_10_1__7572b9dd.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:2` -> `Data/sefaria_texts/Onkelos_Genesis_10_2__17d52314.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:3` -> `Data/sefaria_texts/Onkelos_Genesis_10_3__d4b74310.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:4` -> `Data/sefaria_texts/Onkelos_Genesis_10_4__203c762b.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:5` -> `Data/sefaria_texts/Onkelos_Genesis_10_5__b0327622.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:6` -> `Data/sefaria_texts/Onkelos_Genesis_10_6__5a1f0803.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:7` -> `Data/sefaria_texts/Onkelos_Genesis_10_7__e00d3917.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:8` -> `Data/sefaria_texts/Onkelos_Genesis_10_8__8ca91618.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:9` -> `Data/sefaria_texts/Onkelos_Genesis_10_9__5f3fd6e1.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:10` -> `Data/sefaria_texts/Onkelos_Genesis_10_10__d6f6ebd9.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:11` -> `Data/sefaria_texts/Onkelos_Genesis_10_11__4aed7164.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:12` -> `Data/sefaria_texts/Onkelos_Genesis_10_12__4ae29f78.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:13` -> `Data/sefaria_texts/Onkelos_Genesis_10_13__3343dabd.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:14` -> `Data/sefaria_texts/Onkelos_Genesis_10_14__34b8e34a.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:15` -> `Data/sefaria_texts/Onkelos_Genesis_10_15__00dfa553.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:16` -> `Data/sefaria_texts/Onkelos_Genesis_10_16__0c76224d.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:17` -> `Data/sefaria_texts/Onkelos_Genesis_10_17__3cbece1e.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:18` -> `Data/sefaria_texts/Onkelos_Genesis_10_18__4030991e.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:19` -> `Data/sefaria_texts/Onkelos_Genesis_10_19__1e9c0593.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:20` -> `Data/sefaria_texts/Onkelos_Genesis_10_20__39885419.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:21` -> `Data/sefaria_texts/Onkelos_Genesis_10_21__1a49863b.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:22` -> `Data/sefaria_texts/Onkelos_Genesis_10_22__e8e2bf45.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:23` -> `Data/sefaria_texts/Onkelos_Genesis_10_23__d4edd3e8.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:24` -> `Data/sefaria_texts/Onkelos_Genesis_10_24__746d2753.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:25` -> `Data/sefaria_texts/Onkelos_Genesis_10_25__5d3dc4b4.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:26` -> `Data/sefaria_texts/Onkelos_Genesis_10_26__44622913.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:27` -> `Data/sefaria_texts/Onkelos_Genesis_10_27__a0025ebf.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:28` -> `Data/sefaria_texts/Onkelos_Genesis_10_28__5c27438d.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:29` -> `Data/sefaria_texts/Onkelos_Genesis_10_29__c70eea05.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:30` -> `Data/sefaria_texts/Onkelos_Genesis_10_30__7475ccd9.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:31` -> `Data/sefaria_texts/Onkelos_Genesis_10_31__0b441fe3.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 10:32` -> `Data/sefaria_texts/Onkelos_Genesis_10_32__bb6a5aab.json` · Tier-A gen_24 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:1` -> `Data/sefaria_texts/Onkelos_Genesis_11_1__e35402bb.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:2` -> `Data/sefaria_texts/Onkelos_Genesis_11_2__9a85b7b2.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:3` -> `Data/sefaria_texts/Onkelos_Genesis_11_3__9fc7cd67.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:4` -> `Data/sefaria_texts/Onkelos_Genesis_11_4__402e5b47.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:5` -> `Data/sefaria_texts/Onkelos_Genesis_11_5__8bdfad71.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:6` -> `Data/sefaria_texts/Onkelos_Genesis_11_6__349bbfeb.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:7` -> `Data/sefaria_texts/Onkelos_Genesis_11_7__5b08c402.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:8` -> `Data/sefaria_texts/Onkelos_Genesis_11_8__f23dc37b.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:9` -> `Data/sefaria_texts/Onkelos_Genesis_11_9__a8bf9110.json` · Tier-A gen_25 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:10` -> `Data/sefaria_texts/Onkelos_Genesis_11_10__d7759ac4.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:11` -> `Data/sefaria_texts/Onkelos_Genesis_11_11__b23b0bea.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:12` -> `Data/sefaria_texts/Onkelos_Genesis_11_12__f0983b58.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:13` -> `Data/sefaria_texts/Onkelos_Genesis_11_13__42474cd5.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:14` -> `Data/sefaria_texts/Onkelos_Genesis_11_14__e88ce8aa.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:15` -> `Data/sefaria_texts/Onkelos_Genesis_11_15__17667229.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:16` -> `Data/sefaria_texts/Onkelos_Genesis_11_16__4be82e1b.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:17` -> `Data/sefaria_texts/Onkelos_Genesis_11_17__67762f0c.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:18` -> `Data/sefaria_texts/Onkelos_Genesis_11_18__7647ab07.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:19` -> `Data/sefaria_texts/Onkelos_Genesis_11_19__187449a5.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:20` -> `Data/sefaria_texts/Onkelos_Genesis_11_20__24ec21af.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:21` -> `Data/sefaria_texts/Onkelos_Genesis_11_21__02f72fe6.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:22` -> `Data/sefaria_texts/Onkelos_Genesis_11_22__2ec67057.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:23` -> `Data/sefaria_texts/Onkelos_Genesis_11_23__36011758.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:24` -> `Data/sefaria_texts/Onkelos_Genesis_11_24__5b2931f5.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:25` -> `Data/sefaria_texts/Onkelos_Genesis_11_25__dc41e2a6.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:26` -> `Data/sefaria_texts/Onkelos_Genesis_11_26__e4431e14.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:27` -> `Data/sefaria_texts/Onkelos_Genesis_11_27__2381a038.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:28` -> `Data/sefaria_texts/Onkelos_Genesis_11_28__751379f2.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:29` -> `Data/sefaria_texts/Onkelos_Genesis_11_29__38b71146.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:30` -> `Data/sefaria_texts/Onkelos_Genesis_11_30__0ce5a95e.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:31` -> `Data/sefaria_texts/Onkelos_Genesis_11_31__144c485e.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 11:32` -> `Data/sefaria_texts/Onkelos_Genesis_11_32__a3299c40.json` · Tier-A gen_26 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:1` -> `Data/sefaria_texts/Onkelos_Genesis_12_1__893d79b8.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:2` -> `Data/sefaria_texts/Onkelos_Genesis_12_2__612dbd1c.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:3` -> `Data/sefaria_texts/Onkelos_Genesis_12_3__c2dcae16.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:4` -> `Data/sefaria_texts/Onkelos_Genesis_12_4__2d510356.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:5` -> `Data/sefaria_texts/Onkelos_Genesis_12_5__72bde099.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:6` -> `Data/sefaria_texts/Onkelos_Genesis_12_6__bc74f7bb.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:7` -> `Data/sefaria_texts/Onkelos_Genesis_12_7__dffaedea.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:8` -> `Data/sefaria_texts/Onkelos_Genesis_12_8__3ffaa65a.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:9` -> `Data/sefaria_texts/Onkelos_Genesis_12_9__4701ff45.json` · Tier-A gen_27 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:10` -> `Data/sefaria_texts/Onkelos_Genesis_12_10__2a1e0011.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:11` -> `Data/sefaria_texts/Onkelos_Genesis_12_11__dcb6cc83.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:12` -> `Data/sefaria_texts/Onkelos_Genesis_12_12__d0738f01.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:13` -> `Data/sefaria_texts/Onkelos_Genesis_12_13__78e4574f.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:14` -> `Data/sefaria_texts/Onkelos_Genesis_12_14__9bedab04.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:15` -> `Data/sefaria_texts/Onkelos_Genesis_12_15__e7893440.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:16` -> `Data/sefaria_texts/Onkelos_Genesis_12_16__a2bfa6d3.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:17` -> `Data/sefaria_texts/Onkelos_Genesis_12_17__217ac3cc.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:18` -> `Data/sefaria_texts/Onkelos_Genesis_12_18__caa296cc.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:19` -> `Data/sefaria_texts/Onkelos_Genesis_12_19__82331c45.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 12:20` -> `Data/sefaria_texts/Onkelos_Genesis_12_20__15f66234.json` · Tier-A gen_28 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:1` -> `Data/sefaria_texts/Onkelos_Genesis_13_1__22f9dbee.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:2` -> `Data/sefaria_texts/Onkelos_Genesis_13_2__2e0d9ab6.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:3` -> `Data/sefaria_texts/Onkelos_Genesis_13_3__7fc337db.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:4` -> `Data/sefaria_texts/Onkelos_Genesis_13_4__3d8e7068.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:5` -> `Data/sefaria_texts/Onkelos_Genesis_13_5__79ababf0.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:6` -> `Data/sefaria_texts/Onkelos_Genesis_13_6__0636ce94.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:7` -> `Data/sefaria_texts/Onkelos_Genesis_13_7__be647250.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:8` -> `Data/sefaria_texts/Onkelos_Genesis_13_8__6a2a88df.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:9` -> `Data/sefaria_texts/Onkelos_Genesis_13_9__fa6e3e80.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:10` -> `Data/sefaria_texts/Onkelos_Genesis_13_10__1fb3641f.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:11` -> `Data/sefaria_texts/Onkelos_Genesis_13_11__1da38e1f.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:12` -> `Data/sefaria_texts/Onkelos_Genesis_13_12__2ef19355.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:13` -> `Data/sefaria_texts/Onkelos_Genesis_13_13__8effd681.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:14` -> `Data/sefaria_texts/Onkelos_Genesis_13_14__fdfbbbc2.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:15` -> `Data/sefaria_texts/Onkelos_Genesis_13_15__2ed7200a.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:16` -> `Data/sefaria_texts/Onkelos_Genesis_13_16__fda6ca95.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:17` -> `Data/sefaria_texts/Onkelos_Genesis_13_17__e7b8797d.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 13:18` -> `Data/sefaria_texts/Onkelos_Genesis_13_18__209ca846.json` · Tier-A gen_29 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:1` -> `Data/sefaria_texts/Onkelos_Genesis_14_1__03bcfb9b.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:2` -> `Data/sefaria_texts/Onkelos_Genesis_14_2__b146b694.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:3` -> `Data/sefaria_texts/Onkelos_Genesis_14_3__d976e77e.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:4` -> `Data/sefaria_texts/Onkelos_Genesis_14_4__7e1574c5.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:5` -> `Data/sefaria_texts/Onkelos_Genesis_14_5__7b63352f.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:6` -> `Data/sefaria_texts/Onkelos_Genesis_14_6__3f1b3a6e.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:7` -> `Data/sefaria_texts/Onkelos_Genesis_14_7__3bf99273.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:8` -> `Data/sefaria_texts/Onkelos_Genesis_14_8__d0795762.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:9` -> `Data/sefaria_texts/Onkelos_Genesis_14_9__b20d2202.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:10` -> `Data/sefaria_texts/Onkelos_Genesis_14_10__47c317a2.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:11` -> `Data/sefaria_texts/Onkelos_Genesis_14_11__4f8568fe.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:12` -> `Data/sefaria_texts/Onkelos_Genesis_14_12__67fd2f14.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:13` -> `Data/sefaria_texts/Onkelos_Genesis_14_13__de2a8e4d.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:14` -> `Data/sefaria_texts/Onkelos_Genesis_14_14__8d8dcaba.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:15` -> `Data/sefaria_texts/Onkelos_Genesis_14_15__78876f31.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:16` -> `Data/sefaria_texts/Onkelos_Genesis_14_16__74569bfa.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:17` -> `Data/sefaria_texts/Onkelos_Genesis_14_17__3cafea6e.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:18` -> `Data/sefaria_texts/Onkelos_Genesis_14_18__508c4a46.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:19` -> `Data/sefaria_texts/Onkelos_Genesis_14_19__2c27a851.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:20` -> `Data/sefaria_texts/Onkelos_Genesis_14_20__717c88c6.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:21` -> `Data/sefaria_texts/Onkelos_Genesis_14_21__eca8d234.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:22` -> `Data/sefaria_texts/Onkelos_Genesis_14_22__9316acf1.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:23` -> `Data/sefaria_texts/Onkelos_Genesis_14_23__e7b9f4c0.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 14:24` -> `Data/sefaria_texts/Onkelos_Genesis_14_24__48ee161b.json` · Tier-A gen_30 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:1` -> `Data/sefaria_texts/Onkelos_Genesis_15_1__1608a5bd.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:2` -> `Data/sefaria_texts/Onkelos_Genesis_15_2__ab9b1f91.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:3` -> `Data/sefaria_texts/Onkelos_Genesis_15_3__d0a614c2.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:4` -> `Data/sefaria_texts/Onkelos_Genesis_15_4__63c381b3.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:5` -> `Data/sefaria_texts/Onkelos_Genesis_15_5__a29a6752.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:6` -> `Data/sefaria_texts/Onkelos_Genesis_15_6__5bc428c6.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:7` -> `Data/sefaria_texts/Onkelos_Genesis_15_7__d2821060.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:8` -> `Data/sefaria_texts/Onkelos_Genesis_15_8__7ae2d3f4.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:9` -> `Data/sefaria_texts/Onkelos_Genesis_15_9__543a3ec6.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:10` -> `Data/sefaria_texts/Onkelos_Genesis_15_10__a5f294b8.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:11` -> `Data/sefaria_texts/Onkelos_Genesis_15_11__4da25c30.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:12` -> `Data/sefaria_texts/Onkelos_Genesis_15_12__a6b27053.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:13` -> `Data/sefaria_texts/Onkelos_Genesis_15_13__4b24f84c.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:14` -> `Data/sefaria_texts/Onkelos_Genesis_15_14__b663d5b3.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:15` -> `Data/sefaria_texts/Onkelos_Genesis_15_15__413da4db.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:16` -> `Data/sefaria_texts/Onkelos_Genesis_15_16__dcbb018c.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:17` -> `Data/sefaria_texts/Onkelos_Genesis_15_17__f8097450.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:18` -> `Data/sefaria_texts/Onkelos_Genesis_15_18__4108e23f.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:19` -> `Data/sefaria_texts/Onkelos_Genesis_15_19__ac546ca5.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:20` -> `Data/sefaria_texts/Onkelos_Genesis_15_20__eecfee07.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-03 · `Onkelos Genesis 15:21` -> `Data/sefaria_texts/Onkelos_Genesis_15_21__400bfd87.json` · Tier-A gen_31 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:1` -> `Data/sefaria_texts/Onkelos_Genesis_16_1__1dda0e2a.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:2` -> `Data/sefaria_texts/Onkelos_Genesis_16_2__16007061.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:3` -> `Data/sefaria_texts/Onkelos_Genesis_16_3__5a63058a.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:4` -> `Data/sefaria_texts/Onkelos_Genesis_16_4__e0c54d8d.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:5` -> `Data/sefaria_texts/Onkelos_Genesis_16_5__4b6632d0.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:6` -> `Data/sefaria_texts/Onkelos_Genesis_16_6__5c372f62.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:7` -> `Data/sefaria_texts/Onkelos_Genesis_16_7__bfc2df34.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:8` -> `Data/sefaria_texts/Onkelos_Genesis_16_8__3c44b547.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:9` -> `Data/sefaria_texts/Onkelos_Genesis_16_9__d217300e.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:10` -> `Data/sefaria_texts/Onkelos_Genesis_16_10__118b4dc8.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:11` -> `Data/sefaria_texts/Onkelos_Genesis_16_11__8e492269.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:12` -> `Data/sefaria_texts/Onkelos_Genesis_16_12__2399609a.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:13` -> `Data/sefaria_texts/Onkelos_Genesis_16_13__59fbc47e.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:14` -> `Data/sefaria_texts/Onkelos_Genesis_16_14__8ae6db77.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:15` -> `Data/sefaria_texts/Onkelos_Genesis_16_15__6a60cb38.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 16:16` -> `Data/sefaria_texts/Onkelos_Genesis_16_16__83e56fe7.json` · Tier-A gen_32 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:1` -> `Data/sefaria_texts/Onkelos_Genesis_17_1__369a2738.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:2` -> `Data/sefaria_texts/Onkelos_Genesis_17_2__ddbcb29e.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:3` -> `Data/sefaria_texts/Onkelos_Genesis_17_3__b6a779d2.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:4` -> `Data/sefaria_texts/Onkelos_Genesis_17_4__ebd90b86.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:5` -> `Data/sefaria_texts/Onkelos_Genesis_17_5__365edf4f.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:6` -> `Data/sefaria_texts/Onkelos_Genesis_17_6__edae14b3.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:7` -> `Data/sefaria_texts/Onkelos_Genesis_17_7__dafaa174.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:8` -> `Data/sefaria_texts/Onkelos_Genesis_17_8__4a8e644f.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:9` -> `Data/sefaria_texts/Onkelos_Genesis_17_9__1293ecf9.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:10` -> `Data/sefaria_texts/Onkelos_Genesis_17_10__5bd17552.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:11` -> `Data/sefaria_texts/Onkelos_Genesis_17_11__2fac33ea.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:12` -> `Data/sefaria_texts/Onkelos_Genesis_17_12__8163e4c3.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:13` -> `Data/sefaria_texts/Onkelos_Genesis_17_13__0a6327f9.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:14` -> `Data/sefaria_texts/Onkelos_Genesis_17_14__2d9045e5.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:15` -> `Data/sefaria_texts/Onkelos_Genesis_17_15__420ea6b6.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:16` -> `Data/sefaria_texts/Onkelos_Genesis_17_16__a3e96e7f.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:17` -> `Data/sefaria_texts/Onkelos_Genesis_17_17__6bffe979.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:18` -> `Data/sefaria_texts/Onkelos_Genesis_17_18__311ea71e.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:19` -> `Data/sefaria_texts/Onkelos_Genesis_17_19__f8b9c8a7.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:20` -> `Data/sefaria_texts/Onkelos_Genesis_17_20__d545f4e5.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:21` -> `Data/sefaria_texts/Onkelos_Genesis_17_21__5b2a576c.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:22` -> `Data/sefaria_texts/Onkelos_Genesis_17_22__6497eacd.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:23` -> `Data/sefaria_texts/Onkelos_Genesis_17_23__2bab2317.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:24` -> `Data/sefaria_texts/Onkelos_Genesis_17_24__fd8e54b5.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:25` -> `Data/sefaria_texts/Onkelos_Genesis_17_25__148375df.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:26` -> `Data/sefaria_texts/Onkelos_Genesis_17_26__82e63a2a.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 17:27` -> `Data/sefaria_texts/Onkelos_Genesis_17_27__72c99a22.json` · Tier-A gen_33 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:1` -> `Data/sefaria_texts/Onkelos_Genesis_18_1__10d095c1.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:2` -> `Data/sefaria_texts/Onkelos_Genesis_18_2__05c84610.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:3` -> `Data/sefaria_texts/Onkelos_Genesis_18_3__47526339.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:4` -> `Data/sefaria_texts/Onkelos_Genesis_18_4__8f80b7c3.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:5` -> `Data/sefaria_texts/Onkelos_Genesis_18_5__28b3c824.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:6` -> `Data/sefaria_texts/Onkelos_Genesis_18_6__5ea18e91.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:7` -> `Data/sefaria_texts/Onkelos_Genesis_18_7__6aca0b40.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:8` -> `Data/sefaria_texts/Onkelos_Genesis_18_8__f5e99221.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:9` -> `Data/sefaria_texts/Onkelos_Genesis_18_9__54f956db.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:10` -> `Data/sefaria_texts/Onkelos_Genesis_18_10__16473848.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:11` -> `Data/sefaria_texts/Onkelos_Genesis_18_11__4ff646ab.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:12` -> `Data/sefaria_texts/Onkelos_Genesis_18_12__89209e86.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:13` -> `Data/sefaria_texts/Onkelos_Genesis_18_13__1de52a8b.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:14` -> `Data/sefaria_texts/Onkelos_Genesis_18_14__4a92f2c4.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:15` -> `Data/sefaria_texts/Onkelos_Genesis_18_15__460c2316.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:16` -> `Data/sefaria_texts/Onkelos_Genesis_18_16__134b33a5.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:17` -> `Data/sefaria_texts/Onkelos_Genesis_18_17__7ce3e3a4.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:18` -> `Data/sefaria_texts/Onkelos_Genesis_18_18__fa2bfd1b.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:19` -> `Data/sefaria_texts/Onkelos_Genesis_18_19__3c4dd7bd.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:20` -> `Data/sefaria_texts/Onkelos_Genesis_18_20__d02df3e2.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:21` -> `Data/sefaria_texts/Onkelos_Genesis_18_21__71d730ba.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:22` -> `Data/sefaria_texts/Onkelos_Genesis_18_22__29caac9a.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:23` -> `Data/sefaria_texts/Onkelos_Genesis_18_23__a38a8eea.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:24` -> `Data/sefaria_texts/Onkelos_Genesis_18_24__4bfd9427.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:25` -> `Data/sefaria_texts/Onkelos_Genesis_18_25__038fe3e6.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:26` -> `Data/sefaria_texts/Onkelos_Genesis_18_26__6a8a2ab3.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:27` -> `Data/sefaria_texts/Onkelos_Genesis_18_27__f14aff30.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:28` -> `Data/sefaria_texts/Onkelos_Genesis_18_28__d6d81b70.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:29` -> `Data/sefaria_texts/Onkelos_Genesis_18_29__df0738f4.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:30` -> `Data/sefaria_texts/Onkelos_Genesis_18_30__a302709f.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:31` -> `Data/sefaria_texts/Onkelos_Genesis_18_31__3c444cbf.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:32` -> `Data/sefaria_texts/Onkelos_Genesis_18_32__adf4e07a.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 18:33` -> `Data/sefaria_texts/Onkelos_Genesis_18_33__e3ce078f.json` · Tier-A gen_34 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:1` -> `Data/sefaria_texts/Onkelos_Genesis_19_1__406758f1.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:2` -> `Data/sefaria_texts/Onkelos_Genesis_19_2__753637e4.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:3` -> `Data/sefaria_texts/Onkelos_Genesis_19_3__71f28fc3.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:4` -> `Data/sefaria_texts/Onkelos_Genesis_19_4__b90a38da.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:5` -> `Data/sefaria_texts/Onkelos_Genesis_19_5__7f8f1b25.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:6` -> `Data/sefaria_texts/Onkelos_Genesis_19_6__9d994fbd.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:7` -> `Data/sefaria_texts/Onkelos_Genesis_19_7__bc3f60e9.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:8` -> `Data/sefaria_texts/Onkelos_Genesis_19_8__b0adbe30.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:9` -> `Data/sefaria_texts/Onkelos_Genesis_19_9__d0065f45.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:10` -> `Data/sefaria_texts/Onkelos_Genesis_19_10__b29ad1fc.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:11` -> `Data/sefaria_texts/Onkelos_Genesis_19_11__b0705c37.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:12` -> `Data/sefaria_texts/Onkelos_Genesis_19_12__1ec91624.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:13` -> `Data/sefaria_texts/Onkelos_Genesis_19_13__60ac1c1e.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:14` -> `Data/sefaria_texts/Onkelos_Genesis_19_14__70a6fad2.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:15` -> `Data/sefaria_texts/Onkelos_Genesis_19_15__e992174b.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:16` -> `Data/sefaria_texts/Onkelos_Genesis_19_16__30a5a724.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:17` -> `Data/sefaria_texts/Onkelos_Genesis_19_17__8ce183ea.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:18` -> `Data/sefaria_texts/Onkelos_Genesis_19_18__ef4f304f.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:19` -> `Data/sefaria_texts/Onkelos_Genesis_19_19__63140171.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:20` -> `Data/sefaria_texts/Onkelos_Genesis_19_20__fc65af06.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:21` -> `Data/sefaria_texts/Onkelos_Genesis_19_21__dae065af.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:22` -> `Data/sefaria_texts/Onkelos_Genesis_19_22__0d96ccc7.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:23` -> `Data/sefaria_texts/Onkelos_Genesis_19_23__a6934e0f.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:24` -> `Data/sefaria_texts/Onkelos_Genesis_19_24__38b02964.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:25` -> `Data/sefaria_texts/Onkelos_Genesis_19_25__bb4792ab.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:26` -> `Data/sefaria_texts/Onkelos_Genesis_19_26__edd13f0a.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:27` -> `Data/sefaria_texts/Onkelos_Genesis_19_27__953d7d7e.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:28` -> `Data/sefaria_texts/Onkelos_Genesis_19_28__45935ec9.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:29` -> `Data/sefaria_texts/Onkelos_Genesis_19_29__06261dbd.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:30` -> `Data/sefaria_texts/Onkelos_Genesis_19_30__4e69a0c5.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:31` -> `Data/sefaria_texts/Onkelos_Genesis_19_31__c616ea00.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:32` -> `Data/sefaria_texts/Onkelos_Genesis_19_32__8c7959a2.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:33` -> `Data/sefaria_texts/Onkelos_Genesis_19_33__1a062dad.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:34` -> `Data/sefaria_texts/Onkelos_Genesis_19_34__b1fd8afa.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:35` -> `Data/sefaria_texts/Onkelos_Genesis_19_35__336e8258.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:36` -> `Data/sefaria_texts/Onkelos_Genesis_19_36__aff2c989.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:37` -> `Data/sefaria_texts/Onkelos_Genesis_19_37__cc8785ef.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 19:38` -> `Data/sefaria_texts/Onkelos_Genesis_19_38__f05cbff1.json` · Tier-A gen_35 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:1` -> `Data/sefaria_texts/Onkelos_Genesis_20_1__8e2dbc93.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:2` -> `Data/sefaria_texts/Onkelos_Genesis_20_2__fd4f1e82.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:3` -> `Data/sefaria_texts/Onkelos_Genesis_20_3__874f86cc.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:4` -> `Data/sefaria_texts/Onkelos_Genesis_20_4__e95a6263.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:5` -> `Data/sefaria_texts/Onkelos_Genesis_20_5__03964c35.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:6` -> `Data/sefaria_texts/Onkelos_Genesis_20_6__1cb96256.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:7` -> `Data/sefaria_texts/Onkelos_Genesis_20_7__2553048e.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:8` -> `Data/sefaria_texts/Onkelos_Genesis_20_8__a7f56fad.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:9` -> `Data/sefaria_texts/Onkelos_Genesis_20_9__e098a673.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:10` -> `Data/sefaria_texts/Onkelos_Genesis_20_10__d17320da.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:11` -> `Data/sefaria_texts/Onkelos_Genesis_20_11__aab59be5.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:12` -> `Data/sefaria_texts/Onkelos_Genesis_20_12__69bb5564.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:13` -> `Data/sefaria_texts/Onkelos_Genesis_20_13__05e2d7ce.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:14` -> `Data/sefaria_texts/Onkelos_Genesis_20_14__ced642e2.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:15` -> `Data/sefaria_texts/Onkelos_Genesis_20_15__7c8ed9ea.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:16` -> `Data/sefaria_texts/Onkelos_Genesis_20_16__f39d4dff.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:17` -> `Data/sefaria_texts/Onkelos_Genesis_20_17__5ec9cb65.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 20:18` -> `Data/sefaria_texts/Onkelos_Genesis_20_18__60f4dd39.json` · Tier-A gen_36 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:1` -> `Data/sefaria_texts/Onkelos_Genesis_21_1__e9469712.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:2` -> `Data/sefaria_texts/Onkelos_Genesis_21_2__632bb90d.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:3` -> `Data/sefaria_texts/Onkelos_Genesis_21_3__3f1bd280.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:4` -> `Data/sefaria_texts/Onkelos_Genesis_21_4__031f0f3b.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:5` -> `Data/sefaria_texts/Onkelos_Genesis_21_5__5991a055.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:6` -> `Data/sefaria_texts/Onkelos_Genesis_21_6__49a1b8fe.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:7` -> `Data/sefaria_texts/Onkelos_Genesis_21_7__602b07e0.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:8` -> `Data/sefaria_texts/Onkelos_Genesis_21_8__0740e5e9.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:9` -> `Data/sefaria_texts/Onkelos_Genesis_21_9__a5bb54d5.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:10` -> `Data/sefaria_texts/Onkelos_Genesis_21_10__7c11bf07.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:11` -> `Data/sefaria_texts/Onkelos_Genesis_21_11__2d749fbf.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:12` -> `Data/sefaria_texts/Onkelos_Genesis_21_12__68fe9be0.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:13` -> `Data/sefaria_texts/Onkelos_Genesis_21_13__d739921f.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:14` -> `Data/sefaria_texts/Onkelos_Genesis_21_14__ad92288a.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:15` -> `Data/sefaria_texts/Onkelos_Genesis_21_15__67374f64.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:16` -> `Data/sefaria_texts/Onkelos_Genesis_21_16__40ce0ba1.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:17` -> `Data/sefaria_texts/Onkelos_Genesis_21_17__0249c72a.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:18` -> `Data/sefaria_texts/Onkelos_Genesis_21_18__ed905a04.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:19` -> `Data/sefaria_texts/Onkelos_Genesis_21_19__179e2aeb.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:20` -> `Data/sefaria_texts/Onkelos_Genesis_21_20__daa45d1e.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:21` -> `Data/sefaria_texts/Onkelos_Genesis_21_21__4adb9821.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:22` -> `Data/sefaria_texts/Onkelos_Genesis_21_22__4e3f40d8.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:23` -> `Data/sefaria_texts/Onkelos_Genesis_21_23__f1621ea2.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:24` -> `Data/sefaria_texts/Onkelos_Genesis_21_24__d38a51c7.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:25` -> `Data/sefaria_texts/Onkelos_Genesis_21_25__62a41fd0.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:26` -> `Data/sefaria_texts/Onkelos_Genesis_21_26__4ef8da52.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:27` -> `Data/sefaria_texts/Onkelos_Genesis_21_27__f7317f91.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:28` -> `Data/sefaria_texts/Onkelos_Genesis_21_28__208693b3.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:29` -> `Data/sefaria_texts/Onkelos_Genesis_21_29__02b2c549.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:30` -> `Data/sefaria_texts/Onkelos_Genesis_21_30__c2ae2170.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:31` -> `Data/sefaria_texts/Onkelos_Genesis_21_31__0cc752b8.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:32` -> `Data/sefaria_texts/Onkelos_Genesis_21_32__e9d5a1a1.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:33` -> `Data/sefaria_texts/Onkelos_Genesis_21_33__7ade559f.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 21:34` -> `Data/sefaria_texts/Onkelos_Genesis_21_34__dde50a3b.json` · Tier-A gen_37 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:1` -> `Data/sefaria_texts/Onkelos_Genesis_22_1__b90af9e4.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:2` -> `Data/sefaria_texts/Onkelos_Genesis_22_2__f89ad33c.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:3` -> `Data/sefaria_texts/Onkelos_Genesis_22_3__20e5c0fe.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:4` -> `Data/sefaria_texts/Onkelos_Genesis_22_4__a8daf2cb.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:5` -> `Data/sefaria_texts/Onkelos_Genesis_22_5__52e38758.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:6` -> `Data/sefaria_texts/Onkelos_Genesis_22_6__c52d5bd2.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:7` -> `Data/sefaria_texts/Onkelos_Genesis_22_7__866df2e1.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:8` -> `Data/sefaria_texts/Onkelos_Genesis_22_8__8e6f5260.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:9` -> `Data/sefaria_texts/Onkelos_Genesis_22_9__11a7d3ba.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:10` -> `Data/sefaria_texts/Onkelos_Genesis_22_10__e8dfa91f.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:11` -> `Data/sefaria_texts/Onkelos_Genesis_22_11__ba53696a.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:12` -> `Data/sefaria_texts/Onkelos_Genesis_22_12__ec577976.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:13` -> `Data/sefaria_texts/Onkelos_Genesis_22_13__9bd29834.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:14` -> `Data/sefaria_texts/Onkelos_Genesis_22_14__4cd41991.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:15` -> `Data/sefaria_texts/Onkelos_Genesis_22_15__661a4ec6.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:16` -> `Data/sefaria_texts/Onkelos_Genesis_22_16__d58bdbf3.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:17` -> `Data/sefaria_texts/Onkelos_Genesis_22_17__d51795a6.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:18` -> `Data/sefaria_texts/Onkelos_Genesis_22_18__73c8b6d8.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:19` -> `Data/sefaria_texts/Onkelos_Genesis_22_19__1bd1eb44.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:20` -> `Data/sefaria_texts/Onkelos_Genesis_22_20__1e969e5b.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:21` -> `Data/sefaria_texts/Onkelos_Genesis_22_21__000b9c33.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:22` -> `Data/sefaria_texts/Onkelos_Genesis_22_22__0427fd56.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:23` -> `Data/sefaria_texts/Onkelos_Genesis_22_23__6032c5dd.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 22:24` -> `Data/sefaria_texts/Onkelos_Genesis_22_24__f113c6df.json` · Tier-A gen_38 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:1` -> `Data/sefaria_texts/Onkelos_Genesis_23_1__48870707.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:2` -> `Data/sefaria_texts/Onkelos_Genesis_23_2__64e13a8d.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:3` -> `Data/sefaria_texts/Onkelos_Genesis_23_3__6c9d4714.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:4` -> `Data/sefaria_texts/Onkelos_Genesis_23_4__aa0e8fbe.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:5` -> `Data/sefaria_texts/Onkelos_Genesis_23_5__ea2f786e.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:6` -> `Data/sefaria_texts/Onkelos_Genesis_23_6__8a489b39.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:7` -> `Data/sefaria_texts/Onkelos_Genesis_23_7__0d2c6c8e.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:8` -> `Data/sefaria_texts/Onkelos_Genesis_23_8__4176d824.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:9` -> `Data/sefaria_texts/Onkelos_Genesis_23_9__f35ae205.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:10` -> `Data/sefaria_texts/Onkelos_Genesis_23_10__e5eb8a76.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:11` -> `Data/sefaria_texts/Onkelos_Genesis_23_11__dd1736dd.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:12` -> `Data/sefaria_texts/Onkelos_Genesis_23_12__5dd4f93d.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:13` -> `Data/sefaria_texts/Onkelos_Genesis_23_13__13dd5176.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:14` -> `Data/sefaria_texts/Onkelos_Genesis_23_14__ae0162bb.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:15` -> `Data/sefaria_texts/Onkelos_Genesis_23_15__74a3af90.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:16` -> `Data/sefaria_texts/Onkelos_Genesis_23_16__7de45f3b.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:17` -> `Data/sefaria_texts/Onkelos_Genesis_23_17__9da161d8.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:18` -> `Data/sefaria_texts/Onkelos_Genesis_23_18__f2117587.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:19` -> `Data/sefaria_texts/Onkelos_Genesis_23_19__42242803.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-05 · `Onkelos Genesis 23:20` -> `Data/sefaria_texts/Onkelos_Genesis_23_20__2ea16adc.json` · Tier-A gen_39 derive-time read (sequential, 0.5s)
- 2026-08-08 · ORAL AUDIT gen_08 (oral-first era pilot; WebFetch summaries, not cached to disk — claims DB-verified via verify_claims.py, summaries advisory only):
  `api/texts/Rashi_on_Genesis.2.4-2.9` · `api/texts/Rashi_on_Genesis.2.10-2.17` ·
  `api/texts/Bereshit_Rabbah.12` · `api/texts/Bereshit_Rabbah.13` · `api/texts/Bereshit_Rabbah.14` ·
  `api/texts/Bereshit_Rabbah.15` · `api/texts/Bereshit_Rabbah.16` ·
  `api/texts/Berakhot.61a` · `api/texts/Sanhedrin.56b` · `api/texts/Avot_DeRabbi_Natan.1` ·
  `api/texts/Pesachim.54a` · `api/related/Genesis.2.4` ·
  `api/texts/Kitzur_Baal_HaTurim_on_Genesis.2.4-2.17` · `api/texts/Minchat_Shai_on_Torah,_Genesis.2.4-2.17`
  (dead ends logged: `Baal_HaTurim_on_Genesis` = empty index; chapter-level fetch returns first segment only — use verse ranges)
- 2026-08-08 · SEFARIA-EXPORT CURATED MIRROR (owner order: local search) — one-time bulk
  download from the public GCS bucket (the sanctioned bulk path) via
  logic/solo_tools/fetch_sefaria_export.py: 91 files, 0 failures, ~700MB ->
  Data/sefaria_export/ (full list: Data/sefaria_export/MIRROR_MANIFEST.txt).
  Works: Rashi ×5 · Kitzur Baal HaTurim ×5 · Baal HaTurim (Gen) · Minchat Shai on Torah ·
  Midrash Rabbah ×5 · Tanchuma + Buber · Sifra · Sifrei ×2 · Mekhilta ×2 · Pirkei DeRabbi
  Eliezer · Avot DeRabbi Natan · Aggadat Bereshit · Onkelos ×5 · Targum Jonathan ×5 ·
  links0-16.csv (full citation graph). Indexed by logic/solo_tools/index_sefaria_export.py
  -> derivation.sqlite: export_texts FTS5 (41,114 segments He+En) + export_links
  (668,695 Torah-anchored citations). Oral scans are now LOCAL-FIRST (PROCESS.md);
  web = gap-filler only.
- 2026-08-08 · ORAL AUDIT gen_09 (Gen 2:18-25): ZERO web fetches — first fully local-first
  audit; all sources read verbatim from Data/sefaria_export/ via export_texts/export_links
  (Kitzur Baal HaTurim, Minchat Shai, Rashi, citation-graph span map). Oral layer ~22 min.
- 2026-08-08 · ORAL AUDIT gen_10 (Gen 3:1-13): ZERO web fetches; oral layer ~14 min; first
  audit under the external-checker hold (mechanical gates: diff/green/verifier/gloss_lint).

## 2026-08-08 — gen_11_sentences_exile retro audit (Gen 3:14-24)
ZERO web fetches. All sources local: export_links span census +
export_texts raw reads (Kitzur Baal HaTurim 6 notes, Minchat Shai 11
notes, Rashi 23 notes, Bereshit Rabbah 20:12). First audit under the
Hebrew-script display convention.

## 2026-08-08 — five-block timed run: gen_12 through gen_16 (Gen 4:1-6:22)
ZERO web fetches across all five blocks. Local reads only; the Gen 4
and Gen 6 chapter-wide queries were banked across adjacent blocks.
Run total 20m00s; 45 verified / 0 failed / 3 uncheckable.

## 2026-08-08 — second five-block run: gen_17 through gen_21 (Gen 7:1-9:7)
ZERO web fetches. Run total 16m31s (13:38:26-13:54:57); 40 verified /
0 failed / 1 uncheckable; 5 discrepancy observations; 12 inheritance
edges recorded (first run under the edge layer); ktiv/qere dual-token
instrument discovery at Gen 8:17.

## 2026-08-08 — third five-block run: gen_22 through gen_26 (Gen 9:8-11:32)
ZERO web fetches. Run total 15m08s (13:59:09-14:14:17); 37 verified /
0 failed / 3 uncheckable; the 9:29 Noah death-total manuscript war
arbitrated (SNAPSHOT = Jericho-chumash camp, closing gen_14's held
anomaly); 11 inheritance edges (Chronicles mirror-list, Jonah's
Nineveh, Jeremiah 51 anti-Babel oracle, Zephaniah pure-speech
reversal); meteg-precedes-vowel codepoint lesson; letter-form
(inverted nun) = fifth uninstrumented layer.

## 2026-08-08 — retro-audit run 4 (gen_27..gen_36, Gen 12:1-20:18)
Zero web fetches. All sources from the local mirror (export_texts /
export_links in derivation.sqlite); all probes against
source-snapshot.sqlite. 156 verifier rows: 153
VERIFIED / 0 FAILED / 3 UNCHECKABLE. 63m29s wall.

## 2026-08-08 — retro-audit run 5 (gen_37..gen_46, Gen 21:1-27:40)
Zero web fetches. All sources from the local mirror (export_texts /
export_links in derivation.sqlite); all probes against
source-snapshot.sqlite. 211 verifier rows: 205
VERIFIED / 0 FAILED / 6 UNCHECKABLE (builder-asserted manual rows).
66m22s wall.

## 2026-08-08 — RUN 6 (retro oral audits gen_47-gen_51, Gen 27:41-30:24)
ZERO web fetches — all sources read locally (export_texts /
export_links in derivation.sqlite; Minchat Shai, Kitzur Baal
HaTurim, Bereshit Rabbah span maps, Rashi scan). 69 verifier rows:
64 VERIFIED / 0 FAILED / 5 UNCHECKABLE. 29m41s wall
(18:07:25-18:37:06 CDT). Index 44 of 62 audited; Gen 2:4-30:24
oral layer gapless (creation week deferred).

## 2026-08-08 — RUN 7 (retro oral audits, gen_52-59 + gen_01-02)

ZERO web fetches — full run served from the local mirror
(export_texts/export_links: Minchat Shai, Kitzur Baal HaTurim,
Bereshit Rabbah span maps, Rashi scans). TEN blocks: gen_52-59
(Gen 30:25-36:43) then creation week begins (gen_01-02, Gen
1:1-8). 107 verifier rows: 101 VERIFIED / 0 FAILED / 6
UNCHECKABLE. 58m17s wall (18:47:08-19:45:25 CDT, incl. a
mid-run owner pause and the switch to lean-record mode at block
4). Index 54 of 62 audited; Gen 1:1-8 + 2:4-36:43 oral layer
done — remaining: gen_03-07 (creation week) + lev_04, lev_13,
lev_19.

## 2026-08-08 — RUN 8 (retro oral audits, gen_03-07 + lev_04/13/19) — RETRO PROGRAM COMPLETE

ZERO web fetches — full run served from the local mirror
(export_texts: Minchat Shai, Kitzur Baal HaTurim, Rashi; span
maps via export_links). EIGHT blocks: gen_03-07 (creation week,
Gen 1:9-2:3) then the three Leviticus units (Lev 4:1-35, Lev
13:1-8, Lev 19:1-37 — the corpus's first Leviticus oral audits).
73 verifier rows: 67 VERIFIED / 0 FAILED / 6 UNCHECKABLE. 41m08s
wall (~5m08s/block; blocks 351/227/402/252/182/592/117/345s).
INDEX 62 of 62 AUDITED — the retro oral-audit program is
COMPLETE: every frozen unit carries a chain-attested, DB-verified
oral layer.

## 2026-08-08 — RUN FWD-1 (forward era, first derivation run: gen_60-64, Gen 37-41)

ZERO web fetches — oral scans in-pipeline from the local mirror
(Minchat Shai ×105 notes, Kitzur Baal HaTurim ×75 across the five
chapters). FIVE new units DERIVED + FROZEN (review waived by owner
2026-08-08 — mechanical gates only): gen_60 (Gen 37, 13/0/0), gen_61
(Gen 38, 12/0/0), gen_62 (Gen 39, 11/0/1), gen_63 (Gen 40, 12/0/0),
gen_64 (Gen 41, 13/0/0). Manifest totals: 61 VERIFIED / 0 FAILED / 1
UNCHECKABLE. All freeze rituals complete (verify_text + interpreter +
corpus regression + py layer + indexes + ALL_UNITS proof green each
time; 67 frozen units, regression 67/67 at close). 60m44s wall
(~12m09s/block incl. the one-time generator build; blocks
1256/1786*/492/479/750s — *block-2 timer misread, actual ~25m).
Joseph cycle now frozen Gen 37:1-41:57.

## RUN FWD-2 (2026-08-09) — gen_65-69 (Gen 42-46, the reunion arc)
Five chapters derived + frozen in-pipeline (owner: "do the next 5
blocks"): gen_65_first_descent (42, 13 rows), gen_66_second_descent
(43, 13), gen_67_cup_and_surety (44, 13), gen_68_i_am_yosef (45, 13),
gen_69_descent_seventy (46, 13) — 65 claims, 65 VERIFIED / 0 FAILED /
0 UNCHECKABLE, zero web fetches (local mirror only). 72 frozen units;
regression 72/72; ALL_UNITS + CORPUS_TRUTH green (world at 1,283
facts, 164 open demands, 8 authored settlement links). Marquees: the
dageshed ALEF (43:26); Ben Asher-era mark-splits (paseq/munach 46:2;
Puvah's dagesh with Radak vs the Hilleli 46:13); the 27 Egypt-ward
descents exact; the two-comings stress pair (46:26/27); the three
bindings closed (Simeon soft / chariot hard); הורדהו pair (39:1/44:21);
the harvest-pair invariant collision (8:22/45:6); the healed speech
(37:4→45:15).

## 2026-08-09 — RUN FWD-3 (forward era, run 3: Gen 47-50 — GENESIS COMPLETE)

In-pipeline oral audits for the run's four blocks (owner order "do the
next 4 blocks and finish genesis"): gen_70_goshen_and_the_fifth (47,
13 rows), gen_71_crossed_hands (48, 13), gen_72_testament_twelve (49,
13), gen_73_coffin_in_egypt (50, 13) — 52 claims, 52 VERIFIED / 0
FAILED / 0 UNCHECKABLE, zero web fetches (local mirror only). 76
frozen units; regression 76/76; ALL_UNITS + CORPUS_TRUTH green (world
at 1,367 facts, 165 open demands, 12 authored settlement links, hash
2c281ba6a39b7ed5). GENESIS COMPLETE: 1:1-50:26 gapless. Marquees: the
full-of-full "our fathers" at the performance verse (47:3, script
lean at 46:34); Rameses' vowel splitting two cities (47:11 sheva vs
Exod 1:11 patach); the Sura/Nehardea split "until Ezra comes" (47:19);
the Torah's one full "saying" opening the living blessing-formula
(48:20, lean twin in-verse); the Shiloh word carried whole (49:10);
the LAST four-letter Name of Genesis at the salvation cry (49:18); two
galgal-vs-munach mark-splits (47:26, 49:9); zero full giver-forms in
the Torah (the Ramah's rule verified, 49:21); the two lean deaths —
Aaron's and Moses' alone (50:16 rule); the paqod-yifqod password ×3
ending at Exod 13:19 (the bones-demand's receipt pre-armed); MS's
colophon carried ("Complete and finished is the book of Genesis").

## 2026-08-09 — RUN FWD-4 (exo_01-05, Exod 1-5): EXODUS OPENS
In-pipeline oral audits for the run's five blocks (owner order "do the
first 5 blocks of exodus"): exo_01_names_and_midwives (Exod 1, 13
rows), exo_02_drawn_from_the_water (2, 13), exo_03_bush_and_name (3,
13), exo_04_signs_and_firstborn (4, 13), exo_05_bricks_without_straw
(5, 13) — 65 claims, 65 VERIFIED / 0 FAILED / 0 UNCHECKABLE, zero web
fetches (local mirror only). 81 frozen units; regression 81/81;
ALL_UNITS + CORPUS_TRUTH green (world at 1,451 facts, 174 open
demands, 14 authored settlement links — 2 new: elders-script →
Exod 4:29, court-script → Exod 5:3 — hash e4e113a6e3b4a92c).
Marquees: the lean midwives (the printed Masorah's "unique" ruled an
error — full-form census EMPTY, nine lean stations); the TWO ARKS
(תבת "ark of" — Noah's gopher-ark Gen 6:14 and the reed-basket Exod
2:3, the Torah's only pair of the lean construct); the Name in the
FINALS of the name-question (3:13, לי מה שמו מה) and in the INITIALS
of the brother's appointment (4:14, ידבר הוא וגם הנה) — twin
mechanical crowns; the password's past tense (פקד פקדתי 3:16
completing the four-station stream file from Gen 50:24-25 to Exod
13:19); the holy ground's two unique-full words (רגליך/עומד, 3:5);
the strike-word all-full with two Masorot ruled corruptions (והכיתי
×3); Moses-Moses without the pause-line (the four doubled names);
the double-stroke's five-station census (5:15, the Torah's rarest
accent); the BABEL DOUBLE (bricks-pair Gen 11:3/Exod 5:18 +
scatter-pair Gen 11:8/Exod 5:12); Abel's cry-word at the quota (Gen
4:10/Exod 5:8); the three ill-dealings in three spellings (5:22);
a genuine stream-vs-chain split carried named (the second throw-word
of 4:3 — the Ramah's eight-lean list vs the stream's full letter).
Blocks ran ~11-14 minutes each (run start 13:49, block 5 frozen
~15:00).

## 2026-08-09 — RUN FWD-5 (exo_06-10, Exod 6-10): THE PLAGUE CYCLE

ZERO WEB FETCHES. All five blocks ran wholly on the local mirror
(export_texts: Minchat Shai on Torah + Kitzur Baal HaTurim on
Exodus, chapters 6-10 — 70 MS notes + 58 KB notes read) and the
SNAPSHOT databases. Five units derived + frozen in one run:
exo_06_i_am_the_lord (Exod 6, 30 vv) · exo_07_staff_and_blood
(Exod 7, 29 vv) · exo_08_frogs_lice_swarms (Exod 8, 28 vv) ·
exo_09_pestilence_boils_hail (Exod 9, 35 vv) ·
exo_10_locusts_and_darkness (Exod 10, 29 vv) — 151 verses, the
whole plague-cycle through the severed audience. Oral manifests:
66 claims, 66 VERIFIED / 0 FAILED / 0 UNCHECKABLE. Corpus: 86
frozen units, regression 86/86; world refolded VERIFY GREEN
(1,561 facts / 308 demands / 181 open / 16 authored links, hash
dee671001e8fa3b8). Marquee: the dageshed-lamed rule censused
whole (93 stations, two-sided, with a discrepancy observation
against Or Torah's except-one); the magician-word FRONT-RANK
discrepancy (the stream splits the Masorah's two-lean pair —
full with the Hilleli at 8:15, lean with the ruling at 9:11);
the frogs' soft-tzadi passage-rule whole across the block-seam
(ten soft plurals, the one hard singular); the thunder-word
file with Sinai's lean bonus (19:16 in the same census); the
Babel cease-pair (bond three: bricks, scatter, cease); the
light-in-the-dwellings pair (10:23 + Num 31:10); the one full
going-word (Joseph's caravan, Gen 37:25); the jussive eat- and
remove-threes isolated by the vav's half-vowel; the curse that
circles back (10:28 + Deut 3:26) and the double never-again
(10:29 + Gen 8:21); the kingless locust-verse (the Masorah:
"the locust has no king"); the majority-principle applied by
the Ramah to the text's own letters (10:4); FIVE printed-
authority corrections; TWO binder-divergences dual-tracked.
Blocks ran ~13-20 minutes each (run start 15:45, block 5 frozen
17:02; block 1 carried the run setup).

## 2026-08-09 — RUN FWD-6 (exo_11-15, Exod 11-15): MIDNIGHT TO MARAH
## (bookkeeping written post-transfer; block 5 REDONE after the crash)

ZERO WEB FETCHES. All five blocks ran wholly on the local mirror
(export_texts: Minchat Shai on Torah + Kitzur Baal HaTurim on
Exodus, chapters 11-15) and the SNAPSHOT databases. Five units
derived + frozen: exo_11_one_more_plague (Exod 11, 10 vv) ·
exo_12_passover_and_exodus (Exod 12, 51 vv) ·
exo_13_consecration_and_pillars (Exod 13, 22 vv) ·
exo_14_the_sea_splits (Exod 14, 31 vv) ·
exo_15_the_song_and_marah (Exod 15, 27 vv) — 141 verses:
midnight, the exodus, the sea, the Song, Marah. RUN HISTORY: the
session died 2026-08-09 18:27:53 with blocks 1-4 frozen and
exo_15's manifest verified but no unit built; the machine then
moved (old Mac retired); exo_15 was rebuilt from the verified
manifest inheritance on owner order ("redo exodus 15") the same
evening on the new machine — redo wall time 19m06s (t0 20:50:58,
ritual complete 21:10:04; first-session spend on the block ~7m).
Oral manifests this run: 65 claims (13+13+13+13+13), 65 VERIFIED
/ 0 FAILED / 0 UNCHECKABLE. Corpus: 91 frozen units, regression
91/91; world refolded VERIFY GREEN (1,681 facts / 324 demands /
188 open / 18 authored links, hash 1db42dfddc0d2f64). Run-6
bookkeeping (this entry, the state-doc section, the registry and
settlement appends) was owed from the crash and written at the
exo_15 redo: registry gained MIRYAM (the 2:4 sister signed at
15:20); settlement links gained TWO (exo_06's joint charge →
Exod.12.51; gen_73's bones-oath → Exod.13.19 — both pre-queued
by the prior runs' own notes; the open-count holds at 188: two
new perpetual/unnarrated opens exactly offset by the two
settlements). Marquee (exo_15): the guard-dageshim (Micah barred
from the Song by one dot); the two lean like-You's in one verse
(the mute-reading); the ten songs on a yod; the people formed
twice; the dwelling-cipher (752=752); the anagram-pharmacy
(disease = the bread = the salt, 83 on the gall); the
reign-cutoff chain-vs-stream divergence (dual-tracked); the
once-vocalization of the cover-word; the nostril-pair (Adam's
sweat / the Name's blast); the five sendings (the Akeda's stayed
hand to the mother-bird); the three refoundings on statute-and-
ordinance (Marah, Shechem, Ezra); the butchered choice; the
Song-layout law CLOSED (one column, five lines before and
after). Machine firsts: the corpus's first song-event, first
repair-miracle (the sweetening), first statute-station, first
conditional covenant (the if-clause), first woman titled
prophetess; the murmur-form's Torah-three asserted (Marah, the
spies, after Korah); the refrain verbatim (15:1 = 15:21, seven
tokens); the could-not-drink clause returned (7:21 → 15:23,
full vs lean).

## 2026-08-09 — RUN FWD-7 (exo_16, Exod 16): THE MANNA

ZERO WEB FETCHES. One block on owner order ("do one more block"),
wholly on the local mirror (Minchat Shai on Exod 16, 20 notes +
Kitzur Baal HaTurim on Exod 16, 21 notes) and the SNAPSHOT
databases. exo_16_manna_and_sabbath (Exod 16, 36 vv) derived +
frozen — the manna, the murmurings, the test's first verdict, the
first human Sabbath. TWO ketiv/qere pairs in-span, both on the
murmur-verb. Oral manifest: 13 claims, 13 VERIFIED / 0 FAILED /
0 UNCHECKABLE first run (the initial_letters check type's first
use — the Elijah acrostic machine-verified). Machine: 7D/6R/2E/
1N/1 TEST-FAIL — five cards pop on narrated compliance-formulas;
leave-none-over stands perpetual (breached once — the worms);
the boundary-card pops on va-yishbetu (Torah-unique: THE FIRST
HUMAN SABBATH); the glory's first public appearance (16:10);
Marah's armed test pays at 16:4 and FAILS at 16:28 on Pharaoh's
own refuse-verb (מאנתם "you refuse" — Torah-unique, asserted);
the house names the manna (first collective naming, REGISTRY 1).
Corpus: 92 frozen units, regression 92/92; world refolded VERIFY
GREEN (1,703 facts / 331 demands / 189 open / 18 authored links,
hash c8cc330a578d5d49; +1 open = the perpetual daily rule).
Marquee: the unique murmurings spelling (printed Masorah
corrected); the Ramah's THREE LEAN SEVENTHS census-exact (12:15,
16:30, Lev 25:9 — the three great cessations); the quail-pair
(the gift and the grave); the alphabet-verse (all 22 letters in
the omer-law); the Elijah initials on the keepsake-clause; the
fence-order (rest-word before Sabbath uniquely here); the
boundary-adjacency unique (rest as geometry); Sin = the bush
(120=120); the 248-limb hapax; the wormless Sabbath; the
three-dot lifting vowel (worm-rise pointed apart from
glory-rise). TIMING (owner-requested): block wall 21:30:38 →
~21:46:25 CDT ≈ 15m50s to ritual-complete (+~2m fold and
records); manifest verified first-run.

## RUN FWD-8 (2026-08-10) — exo_17..exo_21 (Exod 17-21, five blocks)

ZERO WEB FETCHES. All oral scans from the local mirror
(derivation.sqlite export_texts): Minchat Shai + Kitzur Baal HaTurim
per chapter (17: 10+13 notes; 18: 18+18; 19: 16+16 + targeted Rashi
pulls 19:1-2, 19:20-25; 20: 30+22 incl. the double-cantillation
essay; 21: 19+34). Five manifests, 65 rows, all VERIFIED first run
(one row self-sharpened at EX17-05: the pausal or-not pair). Two
tradition-vs-SNAPSHOT divergences filed openly at exo_19 (19:11's
second third-word; 19:19's shofar) — dual-tracked, stream standing.

## TALMUD-SHELF MIRROR EXTENSION (2026-08-10) — owner order "fetch it"

Cause: owner audit question ("how are we doing oral torah checks when
we don't even have the talmud") exposed the coverage hole — the
2026-08-08 mirror carried the verse-anchored shelf (Rashi, Kitzur,
Minchat Shai, targums, midrash) and 53,391 Talmud links, but the
Talmud TEXT was absent; zero-fetch discipline meant named Bavli loci
were never read. Fixed before Exod 22 (the ordinances continue into
Bava Kamma territory) rather than repeat the gap knowingly.

FETCHED (sanctioned bulk bucket, storage.googleapis.com/sefaria-export,
via logic/solo_tools/fetch_sefaria_export_talmud.py — listing-API
discovery, He+En merged.json, resumable, 0.4s pacing):
- Talmud Bavli — all 37 tractates (six Seder dirs; TEXT only, no
  Steinsaltz/Rishonim/Acharonim layers)
- Mishnah — all 63 tractates (incl. Pirkei Avot)
- Tosefta — both editions (Vilna "Tosefta X" + Lieberman
  "Tosefta X (Lieberman)")
498 files, 0 failures. 132 stray commentary dirs (Tosefta editions'
Brief Commentary / Variants subtrees, swept by a loose pattern)
PRUNED same day — prune list appended to MIRROR_MANIFEST.txt.
Mirror: 794 MB, 231 work dirs.

INDEXED: index_sefaria_export.py gained a daf-aware ref formatter
(sectionNames[0]=="Daf" -> 1-based section n maps to folio (n+1)//2,
side a/b by parity; verified: Berakhot section 3 = folio 2a, the
tractate's famous first words "From when do we recite the Shema").
Rebuild: export_texts 41,114 -> 134,746 segments (231 works);
export_links unchanged (668,695). derivation.sqlite 362 -> 525 MB.

VERIFIED (Exod 1-21 span, the frozen corpus): all 1,620 Bavli-text
links resolve to local segments across 37 tractates (the only 7
non-resolving Bavli refs are coarse ranges like "Niddah 45b-46a" —
text present, prefix-query reachable); Exod 21:24 links land on the
actual eye-for-eye pages (Bava Kamma 83b-84a); Mishnah/Tosefta text
links resolve (263 + 140). Unresolved remainder is by-design absent
commentary/reference (Steinsaltz 2,433, Jerusalem Talmud 816, Rif/
Introductions/minor tractates 412). Optional future adds noted:
Jerusalem Talmud; Tractate Soferim (the scribal-law minor tractate —
letter-fact material). Zero-fetch discipline RESUMES from here with
the Talmud inside it.

## CHAIN-OF-TRANSMISSION SHELF COMPLETION (2026-08-10) — PHASE 1 of the
## re-derivation program (owner: "phase 1 go"; scope ruling: "Only use
## oral torah in the chain of transmission")

FETCHED (fetch_sefaria_export_chain.py, 538 files + pass-2 sweep 605
files, 0 failures across both): Jerusalem Talmud all 39 text
tractates; all 15 Bavli minor tractates (incl. Soferim); chain
midrash completions (Yalkut Shimoni Torah+Nach, Lekach Tov, Sekhel
Tov, both Pesiktas, Tanna DeBei Eliyahu x2, Seder Olam x2, Midrash
Tehillim/Mishlei/Shmuel/Aggadah, Bereshit Rabbati, Mishnat Rabbi
Eliezer, Sefer HaYashar, Yelamdenu, five Megillot Rabbahs; Sifrei
Zuta + Midrash Tannaim); the rishonim on Torah (Ibn Ezra + HaKatzar,
Ramban, Rashbam, Chizkuni, Bekhor Shor, Rabbeinu Bahya, Rabbeinu
Chananel, Saadia Gaon, Sforno, Radak-Genesis, Da'at/Hadar Zekenim,
Paaneach Raza, Riva, Rosh, Toledot Yitzchak, Tzror HaMor, Tur
HaArokh, Ralbag, Abarbanel, Bartenura-on-Torah, Gevia Kesef, Ateret
Zekeinim); the classical acharonim on Torah (Torah Temimah, Or
HaChaim, Kli Yakar, Malbim + Ayelet HaShachar, Gur Aryeh x5,
Mizrachi, Siftei Chakhamim, Levush HaOrah, Divrei David, Maskil
LeDavid, Nachalat Ya'akov, HaKtav VeHaKabalah, Haamek+Harchev Davar,
Meshekh Chokhmah, both Aderet Eliyahus (Gra; Ben Ish Chai), Chatam
Sofer, Beit HaLevi, Meshech-era anthologies Pardes Yosef, Chida set,
Chanukat HaTorah, Avi Ezer, Em LaMikra, Netinah LaGer, Tevat Gome,
Alshekh...); the codes: Halakhot Gedolot (geonic), Mishneh Torah
complete (61 books incl. Transmission of the Oral Law), Tur,
Shulchan Arukh (4 sections), six mitzvot-codes (Chinukh, Rambam +
Rasag Sefer HaMitzvot, SMAG, SMAK, Yereim). Pass 2 also carried the
two categories' Nach-book chain commentaries (kept: chain-authored,
Tanakh-side program will use them; prune-on-word possible via
manifest). EXCLUDED + SURFACED (script header): Reggio, Shadal, Ohev
Ger (haskalah-method); Ein Yaakov + Rif (duplicative of Bavli);
Otzar Midrashim, Legends of the Jews, Ruth Rabbah Lerner (modern
compilations); Tze'enah Ure'enah; Minchat Chinukh, Sefer Charedim,
Arukh HaShulchan, Kitzur Shulchan Arukh, Chayyei/Chokhmat Adam, Ben
Ish Hai, Shulchan Arukh HaRav (later digests/comment layers — owner
may rule in). OPEN SCOPE SEAM for owner: Talmud/Mishnah-side chain
commentaries (Rashi on Bavli, Tosafot, Bartenura on Mishnah,
Maharal's Derekh Chayyim, Abarbanel's Nachalat Avot) — chain works,
not yet fetched.

MIRROR: 794 MB -> 1.3 GB, 231 -> 896 works. INDEXED with the
generalized Sefaria-citation ref formatter (named sections ", ",
numeric tail " N:N", empty complex-nodes skipped, daf folios;
unit-tested + 12-ref convention spot-check, old refs byte-identical):
export_texts 134,746 -> 594,636 segments; derivation.sqlite 525 MB ->
1.4 GB. ACCEPTANCE (Exod 1-21): 91,579 anchored links, 46,550 resolve
locally (51%); held-but-unjoined residue 75 (coarse/range cites —
prefix-resolvable); ALL remaining non-resolution is works outside the
chain ruling (Chasidut/Kabbalah/Musar/Jewish Thought/Reference/
Steinsaltz/modern) or the surfaced seam above. Midrash 91%, Tanakh
72% resolution. Zero-fetch discipline RESUMES.

## CHAIN PASSES 3-5 + PHASE 2 INSTRUMENTATION (2026-08-10)

PASS 3 (owner: "yes fetch talmud side chain commentariries"): 2,661
files, 0 failures — Bavli Rishonim on Talmud complete (Rashi, Tosafot,
Ramban/Rashba/Ritva/Ran chiddushim, Meiri, Rosh, Mordechai, Rabbeinu
Chananel/Gershom, Tosafot variants...), Bavli Acharonim (Maharsha x2,
Maharam, Penei Yehoshua, Rabbi Akiva Eiger, Rashash, Ben Yehoyada...),
minor-tractate commentary, Yerushalmi chain commentary (Penei Moshe,
Korban HaEdah, Sheyarei Korban, Beur HaGra, Sirilio, Ridbaz...),
Mishnah-side rishonim+acharonim (Rambam, Bartenura, Rash MiShantz,
Tosafot Yom Tov, Melekhet Shelomoh, Derekh Chayyim, Nachalat Avot...).
Excluded: Guggenheimer notes, Yein Levanon, Rif (standing rulings).
PASS 4 (census-driven): 135 files — Tafsir Rasag (579 Exod-1-21
listings!), Targum Jerusalem, Halakhah-rishonim shelf (Ohr Zarua,
Machzor Vitry, Kol Bo, Abudarham, Sefer Chasidim, Siddur Rashi...),
midrash chain commentaries (Radal), Sefer HaMitzvot HaKatzar. Targum
Neofiti EXCLUDED (rediscovered 1949, not transmitted — chain
criterion fails; surfaced). PASS 5a-e: Ben Ish Hai, Perla on Rasag's
Sefer HaMitzvot (18.4 MB), Sheiltot d'Rav Achai Gaon (geonic — found
via its Netziv commentary in the census) + Haamek Sheilah. Chibbah
Yeteirah fetched on mistaken chain identification, PRUNED same hour
(Sefaria-classified Modern; surfaced).

MIRROR: 1.9 GB, ~3,345 works. INDEX: 1,512,045 segments; DB 2.3 GB.
chain_scope.yaml grew census-driven OUT rulings (modern academic,
contemporary, apparatus — each named, owner-overridable). Exod 21
final classification: 7,529 listings = 4,804 READABLE + 63
TANAKH-VERSE + 2,595 OUT (rulings named) + 67 UNRULED, of which the
mass is the NOSEI-KELIM SEAM awaiting owner ruling (Beit Yosef, Bach,
Sma, Taz, Ketzot, Peri Megadim, Mishneh LaMelech, Minchat Chinukh...;
~450 MB to close) + a handful of contemporary works.

PHASE 2 INSTRUMENTATION BUILT same day: chain_scope.yaml (rulings,
machine-readable), chain_scan.py (full-inversion scanner; incremental
DISK read-ledger at logic/oral_audit/ledgers/; daf/range/prefix
resolution; Tanakh cross-refs via elijah_docket/tanakh.sqlite),
oral_coverage.py (the freeze-blocking coverage gate), freeze_ritual.py
step-0 wiring (red gate = no freeze flip), PROCESS.md pipeline steps
rewritten (inversion FIRST, logic notes BEFORE machine derivation,
two-gate verify; drift-era text retired to git history).

## PASS 6 + SHELF CLOSURE (2026-08-10, owner: "yes fetch" — nosei kelim)

PASS 6: 1,979 files, 0 failures — the codes' commentary layer whole:
Shulchan Arukh nosei kelim (Sma, Shach, Taz, Magen Avraham, Ketzot,
Netivot, Eliyah Rabbah, Peri Megadim incl. both components...), Tur
layer (Beit Yosef, Bach, Darkhei Moshe, Prisha...), Mishneh Torah
layer (Kessef/Maggid/Lechem Mishneh, Mishneh LaMelech, Radbaz, Kiryat
Sefer, Tzafnat Pa'neach...), Halakhah acharonim (Shev Shmateta...),
Minchat Chinukh (owner-ruled in), Marganita Tava, pass-6b stragglers.
Excluded: contemporary (Gray Matter, Rabbinic Authority...), devotional
(Sefer Charedim — surfaced). Meiri on Shevuot/Ketubot/Bava Kamma:
cited by links but ABSENT FROM THE EXPORT BUCKET — bucket gap recorded
in chain_scope.yaml, web gap-filler if ever needed.

FINAL SHELF: 2.3 GB, ~5,230 works; export_texts 1,952,179 segments;
derivation.sqlite ~3 GB-class. PILOT CHAPTER GATE-CLEAN: Exod 21 =
7,529 listings -> 4,842 READABLE + 63 TANAKH-VERSE (4,905 required
readings) + 2,624 OUT (rulings named) + 0 UNRULED. Exod 1-21 overall:
42,439 readable; 166 unruled remain across the other 20 chapters —
cleaned per-block during the campaign by the same census procedure.
Zero-fetch discipline resumes; the chain of transmission is CLOSED
LOCAL.
