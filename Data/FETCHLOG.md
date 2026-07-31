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
| 2026-07-31 | (no cache — metadata only) | api/name lookup x2 ("Erkhei Midrash" / its Hebrew title) | owner asked whether Bacher's exegetical-terminology lexicon can be read; checked whether Sefaria carries the Rabinovitz Hebrew translation | NOT on Sefaria; Bacher term-testing done against our existing local cache instead (logic/middot_scan/bacher_scan.py) — no text fetched |
| 2026-07-31 | Data/sefaria_texts/ | api/texts Onkelos Genesis 2:1-3 (3 sequential per-verse requests, 0.5s apart) | day-7 derivation (owner order "Lets finish the 7 days"): Tier-A translation read at derive time per charter section 4.1 | findings: ve-ishtakhlelu — the agentless passive completion RETAINED; the SEVENTH-day dating of the finishing act retained unharmonized; ve-NACH ("and He RESTED") glossing va-yishbot ("and He CEASED") both times — cessation rendered as rest; kadish yateh retained; the la'asot ("to make") tail retained (di vra le-me'bad) |
| 2026-07-31 | Data/sefaria_texts/ | api/texts Onkelos Genesis 1:24-31 (8 sequential per-verse requests, 0.5s apart) | day-6 derivation (owner order "Lets finish the 7 days"): Tier-A translation read at derive time per charter section 4.1 | 8 findings incl.: na'avid ("let us make") — the 1cp plural RETAINED by the anti-anthropomorphic translator (contrast day 4's number normalization); be-tzalma d-Adonai ("in the image of THE LORD") — the plural's referent resolved to the single God at 1:27; takin lachada ("exceedingly well-ordered") for tov me'od at 1:31 vs plain tav ("good") for the local tests — the global test read as an arrangement check; both receipts (1:24, 1:30) retained |
| 2026-07-31 | Data/sefaria_texts/ | api/texts Chullin 60a sections (6 sequential requests: 60a:7-8, 60a:3-5 probes, full 60a page) | middot-detector calibration: the grasses kal-va-chomer ("light and heavy" a-fortiori) passage cited by gen_03's ORAL_grasses note was verified-local earlier but never cached | located + cached Chullin 60a:10 (grasses draw the inference), 60a:11 (the argument spelled out with "how much more so"), 60a:13 (grafting two grasses); also cached 60a:7-8 (Adam's ox — probe overshoot, kept) |

Politeness contract (owner order): sequential requests, 0.5s delay, small
ranges per invocation — never a whole book at once.
