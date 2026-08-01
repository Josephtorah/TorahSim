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
