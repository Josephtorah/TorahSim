# THE RULE CATALOG — the rule book's master index
Opened 2026-09-01 on the owner's question ("how do we catalog them").
ONE catalog for every rule the machine knows or is owed: the compiled
modules of engine.py first, then the 206 Talmud-law candidates from the
triage (TALMUD_LAW_HARVEST.md), grouped by tractate — the Mishnah's own
organization, so the catalog's table of contents grows into the
tradition's.

Every entry: a stable ID, the source, the Genesis anchor, one line of
what the rule says, and a STATUS. IDs never change; status moves.

STATUS ladder:
  CANDIDATE  — surfaced by the triage, not yet examined
  EXAMINED   — case rows quoted, classified A/B/C against the machine
  COMPILED   — a working rule function in engine.py, exam green
  (a rule's claims seat in units via the findings loop as usual)

## PART I — COMPILED (the working rule book, 41 rules, 129/129 green)

| id | module | tractate | oracle | Genesis anchor |
|---|---|---|---|---|
| R-001 | life_override | Yoma | Mishnah Yoma 8:7 | Gen 7:22 (G18-05, G18-10) |
| R-002 | procreation_measure | Yevamot | Mishnah Yevamot 6:6 | Gen 1:28, 5:2, 16:3 (G06-03/12, G14-15, G32-16/22) |
| R-003 | judgment_durations | Eduyot | Mishnah Eduyot 2:10 | Gen 7:11-8:14 (G17-11, computed) |
| R-004 | sciatic_nerve | Chullin | Mishnah Chullin 7:1+7:6 | Gen 32:33 (G55-31, G55-35) |
| R-005 | day_boundary | Chullin | Mishnah Chullin 5:5 | Gen 1:5 (operator order) |
| R-006 | seas_as_mikveh | Mikvaot | Mishnah Mikvaot 5:4 | Gen 1:10 (G03-12) |
| R-007 | forgiveness_after_injury | Bava Kamma | Mishnah Bava Kamma 8:7 | Gen 20:7+20:17 (G36-18) |
| R-008 | seed_categories | Nedarim | Mishnah Nedarim 3:11 | Gen 21:12 + Gen 17 (G37-25, G33-30, computed) |
| R-009 | world_to_come | Sanhedrin | Mishnah Sanhedrin 10:3 | Gen 6:3, 11:8-9, 13:13 (G15-10, G25-16, G29-23/25) |
| R-010 | circumcision_third_day | Shabbat | Mishnah Shabbat 19:3 | Gen 34:25 (G57-23) |
| R-217 | noahide_seven_laws | Sanhedrin | Sanhedrin 56a:24 + 56b:4-8 + 57a:1-7 (TALMUD-ONLY) | Gen 2:16 (G08-28; F-012 the token-assignment dispute) |
| R-218 | noahide_execution_scope | Sanhedrin | Sanhedrin 57a:8-13 (TALMUD-ONLY) | Gen 9:6 (G21-11 — the all-seven paradigm) |
| R-219 | noahide_procedure | Sanhedrin | Sanhedrin 57b:2-9 (TALMUD-ONLY) | Gen 9:5-6 (G21-11, G36-14; F-013 three legs) |
| R-220 | noahide_relations | Sanhedrin | Sanhedrin 58a:7-8 + 57b:10 + 58b:5-14 (TALMUD-ONLY) | Gen 2:24, 20:12 (G09-19; F-016 the sister leg) |
| R-221 | gentile_sabbath_torah | Sanhedrin | Sanhedrin 58b:25 + 59a:2-5 (TALMUD-ONLY) | Gen 8:22 (UNSEATED — F-014) |
| R-222 | repeated_at_sinai | Sanhedrin | Sanhedrin 59a:10-12 + 59b:1-12 (TALMUD-ONLY) | Gen 32:33, 21:12, 17:9/14 (G55-35, G37-25; F-015 framework + two legs) |
| R-223 | meat_timeline | Sanhedrin | Sanhedrin 59b:13-21 + 57a:4-5 + 59a:6-9 (TALMUD-ONLY) | Gen 1:29-30 vs 9:3-4 (G21-08/09, gen_06 rev 2) |
| R-224 | noahide_offerings | Avodah Zarah | Avodah Zarah 51a:15-18 + Sanhedrin 57a:7 (TALMUD-ONLY) | Gen 6:19-20, 7:3, 6:9 (G16-15) |
| R-225 | circumcision_agent | Avodah Zarah | Avodah Zarah 26b:12 + 27a:6 (TALMUD-ONLY) | Gen 17:9-13 (G33-24, G33-22) |
| R-226 | court_of_shem | Avodah Zarah | Avodah Zarah 36b:7 (TALMUD-ONLY) | Gen 38:24 (G61-16) |
| R-227 | pursuer | Sanhedrin | Sanhedrin 72b:15 + 72b:17 (TALMUD-ONLY) | Gen 9:6 (G21-13) |
| R-228 | four_avot_damages | Bava Kamma | Mishnah Bava Kamma 1:1/2:2/5:7/6:2; Gittin 5:1 | Exod 22:4-5 (EX22-02/03/08) |
| R-229 | fire_liability | Bava Kamma | Mishnah Bava Kamma 6:4 + 6:5 | Exod 22:5 (EX22-03) |
| R-230 | theft_and_confession | Bava Kamma | Mishnah Bava Kamma 7:1/7:4/9:8; Shevuot 8:3-4; Ketubot 3:9 | Exod 22:3-8 (EX22-04, EX22-09) |
| R-231 | four_keepers | Bava Metzia | Mishnah Bava Metzia 7:8/3:12/6:6/8:1 | Exod 22:6-14 (EX22-04, EX22-06) |
| R-232 | oath_mechanics | Shevuot | Mishnah Shevuot 6:3/6:4/7:1 | Exod 22:7-10 (EX22-04, EX22-05) |
| R-233 | verbal_wronging | Bava Metzia | Mishnah Bava Metzia 4:10 | Exod 22:20 (ledger-held) |
| R-234 | interest_parties | Bava Metzia | Mishnah Bava Metzia 5:11 | Exod 22:24 (EX22-09) |
| R-235 | unloading_duty | Bava Metzia | Mishnah Bava Metzia 2:10 | Exod 23:5 (EX23-03) |
| R-236 | court_architecture | Sanhedrin | Mishnah Sanhedrin 1:1/1:6/4:2; Rosh Hashanah 2:9 | Exod 22:8 + 23:2 + 24:9 (EX22-04, EX23-02, EX24-07) |
| R-237 | witness_fitness | Sanhedrin | Mishnah Sanhedrin 3:3; Shevuot 4:1 | Exod 23:1 (EX23-01) |
| R-238 | tunneler | Sanhedrin | Mishnah Sanhedrin 8:6 | Exod 22:1-2 (EX22-01) |
| R-239 | sorcerer_mode | Sanhedrin | Mishnah Sanhedrin 7:4 | Exod 22:17 (ledger-held dispute, decided by the case table) |
| R-240 | idolatry_service | Sanhedrin | Mishnah Sanhedrin 7:6 | Exod 22:19 + 23:13 (EX22-09) |
| R-241 | bribe_consequences | Peah | Mishnah Peah 8:9 | Exod 23:8 (EX23-04) |
| R-242 | appearance_duty | Chagigah | Mishnah Chagigah 1:1 + 1:2 | Exod 23:14-17 (EX23-07) |
| R-243 | meat_milk_scope | Chullin | Mishnah Chullin 8:4; Kiddushin 2:9; Avodah Zarah 5:9 | Exod 23:19 (EX23-08) |
| R-244 | pesach_over_chametz | Pesachim | Mishnah Pesachim 5:4 | Exod 23:18 (EX23-08) |
| R-245 | gift_order | Terumot | Mishnah Terumot 3:6 + 3:7 | Exod 22:28 (EX22-10) |
| R-246 | bikkurim_duty | Bikkurim | Mishnah Bikkurim 1:2/1:3/1:9; Shekalim 8:8 | Exod 23:16 + 23:19 (EX23-08, EX23-09) |
| R-247 | shemitah_model | Eduyot | Mishnah Eduyot 4:3 | Exod 23:11 (EX23-05) |

### The Exodus 1-21 backfill exam (2026-09-01, owner: 'lets run step
### 9 on exodus 1 - 21 again') — R-248..R-280, 33 modules, 100/100.
### Part II (R-273..R-280) compiled ON the law-era claims: 34 of 38
### material chapter-21 rows were already held by manifests
### law01/law02/law03 — the machine answered Mishnah it never saw.
| R-248 | passover_offering | Pesachim | Mishnah Pesachim 5:2/5:3/5:5/7:4; Kiddushin 2:1 | Exod 12:4-6 + 12:27 (EX12-17) |
| R-249 | passover_eating | Pesachim | Mishnah Pesachim 2:8/7:1/10:9; Beitzah 2:7; Makkot 3:3 | Exod 12:8-10 + 12:46 (EX12-18) |
| R-250 | leaven_ban | Pesachim | Mishnah Pesachim 1:1/2:2/3:3/9:3; Beitzah 1:1; Makkot 3:2 | Exod 12:15 + 12:19 (EX12-19 — the frontier debt paid) |
| R-251 | seder_duties | Pesachim | Mishnah Pesachim 10:5 + 2:5 | Exod 12:27 + 12:39 + 1:14 (EX12-20, EX01-14) |
| R-252 | egypt_vs_generations | Pesachim | Mishnah Pesachim 9:5 | Exod 12:3 + 12:11 + 12:22 (EX12-21) |
| R-253 | calendar_court | Rosh Hashanah | Mishnah Rosh Hashanah 1:7 + 3:1; Pesachim 4:9 | Exod 12:1-2 (EX12-22) |
| R-254 | firstborn_animal | Bekhorot | Mishnah Bekhorot 1:2/1:7/2:6/2:9; Avodah Zarah 5:9 | Exod 13:12-13 (EX13-14) |
| R-255 | firstborn_human | Bekhorot | Mishnah Bekhorot 8:1 | Exod 13:2 (EX13-14) |
| R-256 | tefillin_form | Megillah | Mishnah Megillah 4:8; Sanhedrin 11:3 | Exod 13:9 + 13:16 (EX13-15, beside the EX13-04 crown) |
| R-257 | sabbath_boundary | Eruvin | Mishnah Eruvin 4:5; Shabbat 1:1 + 24:1; Horayot 1:3 | Exod 16:29 + 20:10 (EX16-14 beside the EX16-10 crown; EX20-16) |
| R-258 | challah_measure | Eduyot | Mishnah Eduyot 1:2 | Exod 16:16 (EX16-15) |
| R-259 | court_tiers | Sanhedrin | Mishnah Sanhedrin 1:5 + 4:1 + 4:2 | Exod 18:22 (EX18-14 beside the EX18-13 routing) |
| R-260 | plotting_witnesses | Makkot | Mishnah Makkot 1:2 + 1:3 + 1:6 | Exod 20:13 + 21:23 (EX20-14, EX21-14) |
| R-261 | equal_weight | Keritot | Mishnah Keritot 6:9 | Exod 20:12 (EX20-15) |
| R-262 | altar_stones | Middot | Mishnah Middot 3:4; Chagigah 3:8 | Exod 20:21-22 (EX20-12 held before the exam; EX20-16) |
| R-263 | sinai_purity | Shabbat | Mishnah Shabbat 9:3 | Exod 19:15 (EX19-14) |
| R-264 | song_performance | Sotah | Mishnah Sotah 5:4 | Exod 15:1 (EX15-14) |
| R-265 | incantation_ban | Sanhedrin | Mishnah Sanhedrin 10:1 | Exod 15:26 (EX15-15) |
| R-266 | public_discharge | Rosh Hashanah | Mishnah Rosh Hashanah 3:8 | Exod 17:11 (EX17-14) |
| R-267 | census_tables | Pirkei Avot | Pirkei Avot 5:4 + 5:6 | Exod 11:1 + 16:4 (EX11-14 — the plague-chronology slot paid; EX16-15) |
| R-268 | decalogue_standing | Tamid | Mishnah Tamid 5:1; Pirkei Avot 3:6 | Exod 20:2 + 20:21 (EX20-16) |
| R-269 | document_precedent | Yadayim | Mishnah Yadayim 4:8 | Exod 5:2 + 9:27 (EX05-14) |
| R-270 | circumcision_priority | Nedarim | Mishnah Nedarim 3:11 | Exod 4:24-26 (EX04-14) |
| R-271 | good_measure | Sotah | Mishnah Sotah 1:9 | Exod 2:4 + 13:19 (EX02-14, riding EX13-01) |
| R-272 | maror_reason | Pesachim | Mishnah Pesachim 10:5 | Exod 1:14 (EX01-14) |
| R-273 | slave_acquisition | Kiddushin | Mishnah Kiddushin 1:2 + 3:12; Yevamot 2:5; Bekhorot 1:7 | Exod 21:2-11 (law-era L2/L4/L5/L6/L8/L11) |
| R-274 | onah_duty | Ketubot | Mishnah Ketubot 5:6; Eduyot 4:10 | Exod 21:10 (L10-01/02) |
| R-275 | goring_liability | Bava Kamma | Mishnah Bava Kamma 1:4/3:8/3:9/4:3/4:9/5:7 | Exod 21:35-36 (L29/L35/L36) |
| R-276 | stoned_ox_process | Sanhedrin | Mishnah Sanhedrin 1:4; Bava Kamma 4:4-4:8; Keritot 6:2; Kiddushin 2:9; Arakhin 3:3; Eduyot 6:1 | Exod 21:28-32 (L28/L30/L31/L32 + EX21-14) |
| R-277 | pit_liability | Bava Kamma | Mishnah Bava Kamma 5:5 + 5:6 + 3:1 | Exod 21:33-34 (L33) |
| R-278 | five_payments | Bava Kamma | Mishnah Bava Kamma 8:1/8:2/3:10; Ketubot 3:2 | Exod 21:18-27 (L19/L22/L26/L12-05) |
| R-279 | theft_tariff | Bava Kamma | Mishnah Bava Kamma 7:1 + 7:5; Sanhedrin 1:1 | Exod 21:37 (L37) |
| R-280 | capital_modes | Sanhedrin | Mishnah Sanhedrin 11:1 + 7:3 | Exod 21:12-21 (L12/L15/L16/L17/L20) |

## PART II — CANDIDATES from the Talmud triage (206), by tractate

Each: id | source passage | Genesis anchor | the rule in one line.
Status: all CANDIDATE unless marked.

### Arakhin (1)
- **R-011** · Arakhin 16b:17 (Gen 13:3) — do not change your lodging: 'to the place where his tent had been at first' (13:3)

### Avodah Zarah (8)
- **R-012** · Avodah Zarah 25b:8 (Gen 33:14) — traveler's ruse with a dangerous escort: widen the road as Jacob did to Esau ('until I come to Seir', 33:14)
- **R-013** · Avodah Zarah 26b:12 (Gen 17:9) — circumcision by a gentile invalid: 'and YOU shall keep My covenant' (Gen 17:9) — **COMPILED → R-225 (2026-09-01, the Noahide block)**
- **R-014** · Avodah Zarah 27a:6 (Gen 17:13) — the two derivations: la-H' himol vs himol yimol (17:13) — **COMPILED → R-225 (2026-09-01, the Noahide block)**
- **R-015** · Avodah Zarah 36b:7 (Gen 38:24) — harlotry banned by the court of Shem - 'take her out and be burned' (38:24): jurisdiction history from our verse — **COMPILED → R-226 (2026-09-01, the Noahide block)**
- **R-016** · Avodah Zarah 51a:15 (Gen 6:19) — MISSING-LIMB ban for Noahide offerings: 'of all the living' (Gen 6:19) - bring animals whose limbs live; ark-spec ink as sacrificial law — **COMPILED → R-224 (2026-09-01, the Noahide block)**
- **R-017** · Avodah Zarah 51a:16 (Gen 7:3) — terefah excluded: 'to keep seed alive' (7:3) — **COMPILED → R-224 (2026-09-01, the Noahide block)**
- **R-018** · Avodah Zarah 51a:18 (Gen 6:19, 6:9) — 'with YOU - like you' (6:18): the animals like Noach; and Noach himself tamim (6:9) — **COMPILED → R-224 (2026-09-01, the Noahide block)**
- **R-019** · Avodah Zarah 53b:13 (Gen 11:1-9) — idol-annulment: the house of Nimrod abandoned in peacetime (the dispersion, 11:1-9) - annulled idolatry precedent

### Bava Batra (9)
- **R-020** · Bava Batra 100a:7 (Gen 13:17) — acquisition by walking: R. Eliezer from 'arise, walk the land... for to you I give it' (13:17)
- **R-021** · Bava Batra 110b:9 (Gen 42:13) — paternal-brother inheritance: brotherhood-brotherhood analogy from the sons of Jacob (42:13)
- **R-022** · Bava Batra 113a:4 (Gen 2:24) — the cleave-word doubled (yidbeku) in the husband-inheritance derivation (2:24 family)
- **R-023** · Bava Batra 123a:10 (Gen 48:5) — 'Ephraim and Manasseh shall be to me like Reuben and Simeon' (48:5) - tribal double-portion law
- **R-024** · Bava Batra 143b:6 (Gen 46:23) — 'the sons of Dan: Chushim' (46:23) - one child written plural: the bnei-canon for inheritance
- **R-025** · Bava Batra 173b:10 (Gen 42:37) — the unconditional-guarantor category from Reuben's 'give him into my hand and I will return him' (42:37)
- **R-026** · Bava Batra 173b:9 (Gen 43:9) — THE GUARANTOR BECOMES OBLIGATED: 'I will be surety for him, from my hand you shall require him' (43:9) - surety law's root
- **R-027** · Bava Batra 56a:9 (Gen 15:18) — Kenite, Kenizzite, Kadmonite excluded from the conquest - the covenant's land list (15:18-19) as boundary law
- **R-028** · Bava Batra 69b:1 (Gen 23:17) — deed law: boundary clauses from 'the field of Ephron... in all its border round about' (23:17) - our Machpelah purchase as the drafting template

### Bava Kamma (7)
- **R-029** · Bava Kamma 49a:5 (Gen 22:5) — ox goring a slave-woman - fetus damages as animal loss: am ha-domeh la-chamor (22:5)
- **R-030** · Bava Kamma 55a:12 (Gen 1:21, 1:25) — breeding two SEA species banned: le-mino at sea learned from le-mino on land (1:21/1:25) - creation ink as kilayim law
- **R-031** · Bava Kamma 60b:6 (Gen 12:10) — famine in the city, scatter your feet - 'Abram went down to Egypt' (12:10)
- **R-032** · Bava Kamma 65b:18 (Gen 31:38) — a day-old ram is a 'ram': 'your rams I have not eaten' (31:38) - sacrificial-age definition
- **R-033** · Bava Kamma 91b:8 (Gen 9:5) — SELF-INJURY FORBIDDEN: 'your own blood I will require' (9:5)
- **R-034** · Bava Kamma 92a:16 (Gen 20:17, 21:1) — pray for your fellow first and be answered first: Abraham for Abimelech, then Sarah remembered (20:17 to 21:1)
- **R-035** · Bava Kamma 93a:3 (Gen 16:5, 23:2) — invoking Heaven's judgment on a fellow - the invoker is punished first: Sarai's cry, Sarah's death (16:5, 23:2)

### Bava Metzia (5)
- **R-036** · Bava Metzia 106b:5 (Gen 8:22) — the six agricultural seasons of the sharecropper law - built on 'seedtime and harvest, cold and heat' (8:22)
- **R-037** · Bava Metzia 59a:11 (Gen 12:15, 12:16) — honor your wife, for blessing comes through her: 'he did good to Abram for her sake' (12:16)
- **R-038** · Bava Metzia 87a:1 (Gen 19:3) — one refuses a lesser host, never a greater: 'he urged them greatly' (19:3)
- **R-039** · Bava Metzia 87a:2 (Gen 18:5, 18:7) — the righteous say little and do much: bread promised, cattle run for (18:5, 18:7) - the source behind the Pirkei Avot 1:15 link
- **R-040** · Bava Metzia 93b:3 (Gen 31:40) — the paid keeper's standard of care measured by Jacob's 'heat by day, frost by night' (31:40)

### Bekhorot (3)
- **R-041** · Bekhorot 46b:2 (Gen 7:22) — THE NOSE-PREDICATE'S THIRD LAW: the emerging head counts when 'the breath of life is in its nostrils' (7:22) - firstborn law; add to the scan's career list
- **R-042** · Bekhorot 50a:8 (Gen 23:16) — all plain Torah silver = sela, EXCEPT Ephron's: centenaria, 'current with the merchant' (23:16)
- **R-043** · Bekhorot 55a:22 (Gen 2:11-14) — vow-scope geography: all rivers are beneath the Euphrates (2:10-14) - 'the fourth river is Perat'

### Berakhot (17)
- **R-044** · Berakhot 13a:8 (Gen 17:5) — calling Abraham 'Abram' breaches a positive command - 'your name SHALL BE Abraham' (Gen 17:5); R. Eliezer adds a negative
- **R-045** · Berakhot 18a:3 (Gen 23:3, 23:4) — the mourner-before-burial exemption: 'Abraham rose from before his dead... I will bury my dead from BEFORE ME' (Gen 23:3-4)
- **R-046** · Berakhot 25b:11 (Gen 9:23) — a gentile's nakedness bars the Shema: 'their father's nakedness they saw not' (Gen 9:23)
- **R-047** · Berakhot 26a:17 (Gen 1:5) — missed-evening-prayer makeup rides the day boundary: 'evening and morning, ONE DAY' (Gen 1:5) - a new call site of our day_boundary predicate
- **R-048** · Berakhot 26b:5 (Gen 19:27) — ABRAHAM INSTITUTED MORNING PRAYER - 'Abraham rose early to the place where he had STOOD' (Gen 19:27), standing = prayer
- **R-049** · Berakhot 26b:6 (Gen 24:63) — ISAAC INSTITUTED AFTERNOON PRAYER - 'Isaac went out to MEDITATE in the field toward evening' (Gen 24:63)
- **R-050** · Berakhot 26b:7 (Gen 28:11) — JACOB INSTITUTED EVENING PRAYER - 'he ENCOUNTERED the place and lodged' (Gen 28:11), encounter = prayer
- **R-051** · Berakhot 27a:10 (Gen 18:1) — prayer-hours defined from 'the HEAT OF THE DAY' (Gen 18:1) = six hours
- **R-052** · Berakhot 2a:9 (Gen 1:5) — night precedes day for the Shema - learned from the world's creation, 'evening and morning one day' (Gen 1:5)
- **R-053** · Berakhot 34b:3 (Gen 37:10) — bowing taxonomy: full prostration = spread arms and legs, from 'to bow to you to the GROUND' (Gen 37:10)
- **R-054** · Berakhot 54b:10 (Gen 19:29) — the blessing rows on Lot and his wife: 'the true Judge' and 'who remembers the righteous' (Gen 19:29)
- **R-055** · Berakhot 54b:8 (Gen 19:26) — the pillar of salt as a standing blessing-object (Gen 19:26)
- **R-056** · Berakhot 55b:17 (Gen 41:12, 41:13) — DREAMS FOLLOW THE MOUTH - 'as he interpreted for us, so it was' (Gen 41:13); Rava's rider: when the reading fits the dream
- **R-057** · Berakhot 61a:19 (Gen 2:22) — escort duty (shoshvin): 'He BROUGHT her to the man' (Gen 2:22) - the Torah taught conduct, the greater escorts the lesser
- **R-058** · Berakhot 61a:24 (Gen 24:61) — riding behind, not before: 'Rebekah and her maidens rode AFTER the man' (Gen 24:61)
- **R-059** · Berakhot 64a:10 (Gen 15:15) — parting from the dead: say 'go IN peace' - 'you shall come to your fathers IN peace' (Gen 15:15)
- **R-060** · Berakhot 6b:8 (Gen 19:27) — a fixed place for prayer, from Abraham's returning 'to the PLACE where he had stood' (Gen 19:27)

### Chullin (12)
- **R-061** · Chullin 113a:20 (Gen 38:20) — meat-milk 'kid' defined from 'Judah sent the kid of the GOATS' (Gen 38:20)
- **R-062** · Chullin 113b:2 (Gen 27:16) — 'skins of the kids of goats' (Gen 27:16): where Scripture specifies vs plain gedi - the definition's second leg
- **R-063** · Chullin 139b:19 (Gen 7:14) — 'every bird every wing' (Gen 7:14) - tzippor/kanaf distinction in the bird-law sugya
- **R-064** · Chullin 16a:5 (Gen 22:10) — slaughter valid with a detached blade: 'he took the KNIFE to slay' (Gen 22:10) - shechitah rule from the binding
- **R-065** · Chullin 49a:18 (Gen 12:3) — the priests' return-blessing: 'I will bless those who bless you' (Gen 12:3) - R. Akiva's source
- **R-066** · Chullin 60b:12 (Gen 21:23) — Abimelech's oath (Gen 21:23) as standing legal bar - the Caphtorim conquest workaround
- **R-067** · Chullin 65a:2 (Gen 14:4) — SCRIBAL LAW: Kedorlaomer written as two words but never on two lines (Gen 14:4)
- **R-068** · Chullin 85a:12 (Gen 43:16) — fitting-slaughter analogy: 'slaughter a slaughtering and PREPARE' (Gen 43:16)
- **R-069** · Chullin 89a:4 (Gen 14:23-24, 14:24) — consumed robbery cannot be restored - 'save what the lads have eaten' (Gen 14:24)
- **R-070** · Chullin 90b:4 (Gen 32:33) — sinew of a burnt-offering: 'the CHILDREN OF ISRAEL shall not eat' - not 'the altar' (Gen 32:33 subject-scope)
- **R-071** · Chullin 95b:14 (Gen 42:36) — the THREE-TIME pattern rule (chazakah): 'Joseph is gone, Simeon is gone, and Benjamin you will take' (Gen 42:36)
- **R-072** · Chullin 95b:8 (Gen 24:14) — divination defined by Eliezer's test (Gen 24:14) - the paradigm case of the nichush ban

### Eruvin (2)
- **R-073** · Eruvin 18b:13 (Gen 7:1) — partial praise to the face, full behind it: 'YOU I have seen righteous' (7:1)
- **R-074** · Eruvin 18b:14 (Gen 6:9) — against the narrator's fuller 'righteous and WHOLE' (6:9) - the conduct rule from the ink delta

### Horayot (2)
- **R-075** · Horayot 5b:15 (Gen 48:4) — KAHAL defined at 'I will make you a congregation of peoples' (48:4)
- **R-076** · Horayot 6b:2 (Gen 48:4) — a tribe with a holding is a kahal; Levi excluded - same verse (48:4)

### Ketubot (8)
- **R-077** · Ketubot 30a:6 (Gen 42:38) — ason by Heaven's hand exempts like ason by man's: 'lest a calamity befall him' (42:38)
- **R-078** · Ketubot 50a:3 (Gen 28:22) — the CHARITY CAP - a fifth: 'all You give me I will DOUBLY TITHE' (28:22, the doubled verb = two tenths)
- **R-079** · Ketubot 57b:2 (Gen 24:25, 24:55) — the bride's preparation time: 'let the maiden remain days or ten' (24:55)
- **R-080** · Ketubot 57b:3 (Gen 24:55) — 'days' read as a year - the leg's resolution
- **R-081** · Ketubot 61a:3 (Gen 20:3, 3:20) — she rises with him and does not descend: be'ulat BA'AL (20:3) + 'mother of all LIVING - for life, not pain' (3:20)
- **R-082** · Ketubot 67b:2 (Gen 2:18) — provisioning the orphan groom: house, bed, then the wife - 'a helper for him' (2:18)
- **R-083** · Ketubot 8a:3 (Gen 2:22) — the wedding blessing's 'building forever' - the rib BUILT (2:22) in the liturgy
- **R-084** · Ketubot 8b:10 (Gen 18:19, 21:33) — the mourners' consolation formula: 'holders of Abraham's covenant... he will command his children' (18:19)

### Kiddushin (7)
- **R-085** · Kiddushin 11b:5 (Gen 23:13) — money betrothal: taking-taking from the field of Ephron (23:13) - our Kiddushin 1:1 bridge verbatim
- **R-086** · Kiddushin 29a:11 (Gen 17:10, 17:14, 21:4) — the circumcision cascade: father ('Abraham circumcised Isaac', 21:4), court ('every male', 17:10), self ('the uncircumcised male', 17:14)
- **R-087** · Kiddushin 29a:12 (Gen 21:4) — the mother exempt: 'as God commanded HIM' - not her (21:4)
- **R-088** · Kiddushin 2a:4 (Gen 23:13) — the same kichah-kichah derivation at the tractate's opening (23:13)
- **R-089** · Kiddushin 2a:5 (Gen 25:10) — and taking is called ACQUISITION: 'the field Abraham BOUGHT' (25:10)
- **R-090** · Kiddushin 4b:3 (Gen 23:13) — the baraita's version: 'I have given the silver of the field, TAKE from me' (23:13)
- **R-091** · Kiddushin 61b:9 (Gen 4:7) — the doubled condition (tenai kaful): R. Meir from 'if you do well... and if you do not' (4:7)

### Makkot (2)
- **R-092** · Makkot 11b:1 (Gen 43:9) — a conditional ban needs release: Judah's self-ban and his rolling bones (43:9)
- **R-093** · Makkot 9a:10 (Gen 20:6) — 'from sinning TO ME' (20:6) - Heaven's jurisdiction vs man's in the killer sugya

### Megillah (1)
- **R-094** · Megillah 20b:2 (Gen 1:5) — dawn-performed rites valid: 'God called the LIGHT day' (Gen 1:5) - the brightening is day; the naming operator in rite-timing law

### Menachot (2)
- **R-095** · Menachot 26b:11 (Gen 19:28) — kitor defined: no kiln smokes until the fire grips its majority - 'the smoke of the land like the kiln's' (19:28)
- **R-096** · Menachot 37a:1 (Gen 48:17) — the right hand called YAD: 'he saw his father set his right hand' (48:17) - tefillin-hand leg

### Moed Katan (1)
- **R-097** · Moed Katan 18a:4 (Gen 22:5) — A COVENANT IS CUT TO THE LIPS: 'we will bow and RETURN to you' - and both returned (22:5)

### Nedarim (3)
- **R-098** · Nedarim 32b:6 (Gen 14:18) — the priesthood passes from Shem to Abraham - 'he was priest to God Most High' (14:18) and the blessing order
- **R-099** · Nedarim 32b:8 (Gen 14:18) — 'HE a priest' - he and not his seed (14:18)
- **R-100** · Nedarim 37b:8 (Gen 18:5, 24:55) — ITTUR SOFERIM - the scribes' adornment readings: 'AFTER you shall pass' (18:5), 'AFTER she shall go' (24:55) - ink canon

### Niddah (6)
- **R-101** · Niddah 22b:13 (Gen 2:19, 2:7) — the miscarriage-form question rides 'formation like man' (2:7, 2:19)
- **R-102** · Niddah 25a:9 (Gen 3:21) — skin is made only for the formed: 'garments of skin He made them' (3:21)
- **R-103** · Niddah 28a:9 (Gen 38:28, 38:28-29) — the hand that emerged and returned - the mother impure: 'he put out a hand' (38:28)
- **R-104** · Niddah 31a:24 (Gen 46:15) — the sex-determination rule proven from the ledger's ink: sons hung on the daughters (46:15)
- **R-105** · Niddah 70b:7 (Gen 19:26) — does Lot's wife's pillar defile? a corpse defiles, a pillar of salt does not (19:26) - a posed case answered on our verse's object
- **R-106** · Niddah 8b:17 (Gen 38:24) — pregnancy recognized at three months: 'about three months later' (38:24) - the Tamar presumption

### Pesachim (7)
- **R-107** · Pesachim 117b:11 (Gen 12:2) — the Amidah's three-patriarch opening mapped to the call's clauses (12:2): liturgical structure from our verse
- **R-108** · Pesachim 2a:3 (Gen 1:4, 44:3) — enter and leave a city by daylight (ki tov) - the travel rule riding day one's good-light token (1:4, 44:3)
- **R-109** · Pesachim 3a:10 (Gen 7:8) — THE CLEAN-LANGUAGE CANON: the Torah curved EIGHT LETTERS to avoid 'impure' (7:8) - numeric ink claim, checkable
- **R-110** · Pesachim 4a:6 (Gen 22:3) — THE ZEALOUS DO COMMANDMENTS EARLY - source: 'Abraham rose early in the morning' (22:3)
- **R-111** · Pesachim 56a:7 (Gen 49:1) — the silent 'blessed be the Name' - born at Jacob's deathbed Shema scene (49:1)
- **R-112** · Pesachim 7b:14 (Gen 44:12) — the leaven-search analogy: found-found from 'he SEARCHED... it was FOUND' (44:12) - the bridge our sweep row predicted, verbatim
- **R-113** · Pesachim 93b:13 (Gen 19:15, 19:23) — dawn-to-sunrise = five mils, computed from Lot's dawn departure reaching Zoar at sunrise (19:15, 19:23) - a legal constant from our verses

### Rosh Hashanah (4)
- **R-114** · Rosh Hashanah 10b:6 (Gen 8:13) — ONE DAY IN A YEAR COUNTS AS A YEAR: 'in the six hundred and first year, on the first of the month' (8:13) - computed from our flood date rows
- **R-115** · Rosh Hashanah 16b:4 (Gen 21:17) — JUDGED BY THIS HOUR'S DEEDS: 'God heard the lad WHERE HE IS' (21:17)
- **R-116** · Rosh Hashanah 16b:6 (Gen 17:15, 17:16) — name-change tears the decree: 'Sarai... for Sarah is her name, and I will bless her' (17:15-16)
- **R-117** · Rosh Hashanah 32b:5 (Gen 21:1) — is 'the LORD remembered Sarah' (21:1) a remembrance-verse for the liturgy? R. Yosei vs R. Yehudah

### Sanhedrin (45)
- **R-118** · Sanhedrin 108b:14 (Gen 6:18, 8:16) — ark cohabitation ban: entry verse separates couples (Gen 6:18), exit verse rejoins (8:16) - law from operand ORDER
- **R-119** · Sanhedrin 29a:34 (Gen 2:17, 3:3) — WHOEVER ADDS SUBTRACTS - the hermeneutic law derived from Gen 3:3's added 'nor touch it'
- **R-120** · Sanhedrin 37b:12 (Gen 4:14, 4:16) — exile atones half: Gen 4:14 'wanderer' vs 4:16 'dwelt in Nod' - the ink delta IS the derivation (our gen_11 sentences-exile territory)
- **R-121** · Sanhedrin 46b:21 (Gen 23:2) — eulogy law: honor of the living or the dead? proof from Gen 23:2 Abraham eulogizing Sarah (our Machpelah unit)
- **R-122** · Sanhedrin 56a:15 (Gen 2:16) — Noahide sugya opener: blasphemy leg of Gen 2:16 derivation — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-123** · Sanhedrin 56b:23 (Gen 2:16) — dispute how many laws Adam got: R. Yehudah idolatry only; +blasphemy; +dinim — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-124** · Sanhedrin 56b:4 (Gen 2:16) — THE ROOT: all seven laws hung on Gen 2:16 va-yetzav ('and He commanded') word by word — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-125** · Sanhedrin 56b:5 (Gen 18:19) — dinim (courts) from va-yetzav via Gen 18:19 'he will command his children' — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-126** · Sanhedrin 56b:6 (Gen 9:6) — blasphemy/idolatry/bloodshed legs; bloodshed cites Gen 9:6 — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-127** · Sanhedrin 57a:1 (Gen 6:11, 6:12) — hashchatah = sexual sin + idolatry, from Gen 6:11-12 (flood indictment as legal category) — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-128** · Sanhedrin 57a:3 (Gen 9:6) — bloodshed leg restated on Gen 9:6 — **COMPILED → R-218 (2026-09-01, the Noahide block)**
- **R-129** · Sanhedrin 57a:4 (Gen 9:3) — ROBBERY from Gen 9:3 'as the green herb' (of the field, not the garden) — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-130** · Sanhedrin 57a:5 (Gen 9:4) — LIMB FROM THE LIVING from Gen 9:4 'flesh with its life-blood you shall not eat' — **COMPILED → R-223 (2026-09-01, the Noahide block)**
- **R-131** · Sanhedrin 57a:6 (Gen 9:7) — castration ban from Gen 9:7 'swarm and multiply' — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-132** · Sanhedrin 57a:7 (Gen 6:20) — mixed-kinds ban from Gen 6:20 'of the fowl by its kind' (ark spec as law source) — **COMPILED → R-224 (2026-09-01, the Noahide block)**
- **R-133** · Sanhedrin 57a:9 (Gen 9:6) — Rav Sheshet's challenge: bloodshed explicit at Gen 9:6, whence the rest — **COMPILED → R-218 (2026-09-01, the Noahide block)**
- **R-134** · Sanhedrin 57b:1 (Gen 9:6) — Noahide executed for bloodshed (Gen 9:6 continuation) — **COMPILED → R-218 (2026-09-01, the Noahide block)**
- **R-135** · Sanhedrin 57b:10 (Gen 2:24) — woman's liability: Gen 2:24 'a MAN shall leave' vs 'they shall be one flesh' — **COMPILED → R-220 (2026-09-01, the Noahide block)**
- **R-136** · Sanhedrin 57b:12 (Gen 2:16) — 'saying' (lemor, Gen 2:16) = sexual prohibitions leg — **COMPILED → R-217 (2026-09-01, the Noahide block)**
- **R-137** · Sanhedrin 57b:3 (Gen 9:5) — ONE JUDGE suffices for a Noahide: Gen 9:5 'I will require it' singular — **COMPILED → R-219 (2026-09-01, the Noahide block)**
- **R-138** · Sanhedrin 57b:4 (Gen 9:5) — Gen 9:5 word-by-word: no warning needed, one witness, man not woman, even a relative — **COMPILED → R-219 (2026-09-01, the Noahide block)**
- **R-139** · Sanhedrin 57b:5 (Gen 9:6) — R. Yishmael: FETUS included - Gen 9:6 'blood of man IN man' = the embryo (abortion law from our ink) — **COMPILED → R-219 (2026-09-01, the Noahide block)**
- **R-140** · Sanhedrin 57b:7 (Gen 18:19) — objection from Gen 18:19 'he will command' re women in dinim — **EXAMINED 2026-09-01 — read in full; the women-in-courts split (sons to judgment, household to charity, 57b:8) not yet a case row**
- **R-141** · Sanhedrin 58a:7 (Gen 2:24) — Gen 2:24 dissected: 'his father'/'his mother' - R. Eliezer vs R. Akiva on which relatives banned — **COMPILED → R-220 (2026-09-01, the Noahide block)**
- **R-142** · Sanhedrin 58a:8 (Gen 2:24) — Gen 2:24 word-by-word: ve-davak not male; b-ishto not the neighbor's; one-flesh excludes beast — **COMPILED → R-220 (2026-09-01, the Noahide block)**
- **R-143** · Sanhedrin 58b:14 (Gen 2:24) — unnatural relations with one's wife: ve-davak (Gen 2:24) — **EXAMINED 2026-09-01 — held at G09-19 (the manner of cleaving actionable); classified B in the held_rows table, case row not posed**
- **R-144** · Sanhedrin 58b:25 (Gen 8:22) — a gentile who keeps a full Sabbath: Gen 8:22 'day and night shall not cease' — **COMPILED → R-221 (2026-09-01, the Noahide block)**
- **R-145** · Sanhedrin 58b:5 (Gen 20:12) — sister law: Gen 20:12 'my father's daughter, not my mother's' proves maternal sister banned — **COMPILED → R-220 (2026-09-01, the Noahide block)**
- **R-146** · Sanhedrin 59a:12 (Gen 32:32) — the SINEW: given to the sons of Jacob, not repeated at Sinai - the framework our G55-35 seat carries — **COMPILED → R-222 (2026-09-01, the Noahide block)**
- **R-147** · Sanhedrin 59a:6 (Gen 9:4) — blood from the living, R. Chanina b. Gamliel's extra law from Gen 9:4 — **COMPILED → R-223 (2026-09-01, the Noahide block)**
- **R-148** · Sanhedrin 59b:1 (Gen 17:9) — circumcision: commanded to Noahides? Gen 17:9 'you and your seed' - repeated at Sinai for Israel alone — **COMPILED → R-222 (2026-09-01, the Noahide block)**
- **R-149** · Sanhedrin 59b:10 (Gen 21:12) — sons of Ishmael exempt: Gen 21:12 'in Isaac shall seed be called' (same statute as our G37-25) — **COMPILED → R-222 (2026-09-01, the Noahide block)**
- **R-150** · Sanhedrin 59b:12 (Gen 17:14) — sons of Keturah obligated: Gen 17:14 'et briti hefar' the inclusion — **COMPILED → R-222 (2026-09-01, the Noahide block)**
- **R-151** · Sanhedrin 59b:13 (Gen 1:29) — Adam not permitted meat: Gen 1:29 read as grant of herbs only — **COMPILED → R-223 (2026-09-01, the Noahide block)**
- **R-152** · Sanhedrin 59b:14 (Gen 9:3, 9:4) — meat permitted to Noach: Gen 9:3, limb-from-living carved out by Gen 9:4 'akh' — **COMPILED → R-223 (2026-09-01, the Noahide block)**
- **R-153** · Sanhedrin 59b:16 (Gen 1:26, 1:28) — 'dominion over fish' (Gen 1:26) = labor not eating (matches our day-6 dominion-as-labor seat) — **COMPILED → R-223 (2026-09-01, the Noahide block)**
- **R-154** · Sanhedrin 59b:18 (Gen 1:26) — 'fowl of the sky' (Gen 1:26) likewise labor — **COMPILED → R-223 (2026-09-01, the Noahide block)**
- **R-155** · Sanhedrin 59b:20 (Gen 1:28) — 'every creeping beast' (Gen 1:28) brings in the serpent (for labor) — **COMPILED → R-223 (2026-09-01, the Noahide block)**
- **R-156** · Sanhedrin 59b:3 (Gen 9:7) — procreation: said to the sons of Noach (Gen 9:7), repeated at Sinai for Israel — **COMPILED → R-222 (2026-09-01, the Noahide block)**
- **R-157** · Sanhedrin 59b:9 (Gen 17:9) — circumcision restricted: 'you and your seed' (Gen 17:9), no one else — **COMPILED → R-222 (2026-09-01, the Noahide block)**
- **R-158** · Sanhedrin 5a:6 (Gen 49:10) — judicial AUTHORITY: 'the scepter shall not depart' (Gen 49:10) = the exilarchs' license to judge
- **R-159** · Sanhedrin 72b:15 (Gen 9:6) — the PURSUER: 'who sheds man's blood by man shall his blood be shed' (Gen 9:6) - save the pursued by the pursuer's blood — **COMPILED → R-227 (2026-09-01, the Noahide block)**
- **R-160** · Sanhedrin 72b:17 (Gen 9:6) — pursuer warning formula quoting Gen 9:6 — **COMPILED → R-227 (2026-09-01, the Noahide block)**
- **R-161** · Sanhedrin 91a:16 (Gen 25:5) — gift-deed law: Gen 25:5-6 'gave all to Isaac; gifts to concubines' sons' - lifetime deeds settle inheritance
- **R-162** · Sanhedrin 91a:8 (Gen 9:25) — slave-property doctrine from Gen 9:25 'slave of slaves': what a slave acquires his master owns

### Shabbat (16)
- **R-163** · Shabbat 105a:2 (Gen 17:5) — NOTARIKON licensed from the Torah: av hamon goyim unpacked letter by letter (17:5) - in the writing-liability sugya
- **R-164** · Shabbat 108a:10 (Gen 17:14) — WHERE circumcision is done: foreskin-foreskin analogy; the fruit-making place (17:14 family)
- **R-165** · Shabbat 127a:13 (Gen 18:3) — hospitality greater than receiving the Presence: 'my Lord, do not pass by' (18:3)
- **R-166** · Shabbat 132a:10 (Gen 17:7) — the generations-generations analogy (17:7)
- **R-167** · Shabbat 132a:15 (Gen 17:12) — 'on the day' - by day and not by night, from 'eight days old' (17:12)
- **R-168** · Shabbat 132a:20 (Gen 17:12) — 'eighth' excludes the seventh - from the same clause (17:12)
- **R-169** · Shabbat 132a:6 (Gen 17:11) — circumcision overrides Shabbat: the sign-sign analogy (17:11)
- **R-170** · Shabbat 132a:8 (Gen 17:11) — the covenant-covenant analogy (17:11)
- **R-171** · Shabbat 132a:9 (Gen 17:14) — an adult, of whom 'covenant' is written - should he override? (17:14)
- **R-172** · Shabbat 132b:10 (Gen 17:10, 17:14) — adult/minor/in-between: where 'flesh' is written (17:10, 17:14)
- **R-173** · Shabbat 133b:13 (Gen 17:14) — the overconfident circumciser on Shabbat dusk - liability shape (17:14 frame)
- **R-174** · Shabbat 137a:3 (Gen 17:10) — 'himol lakhem kol zakhar' - why circumcision differs (17:10)
- **R-175** · Shabbat 151b:9 (Gen 9:2) — the dread-of-man grant read as a live-only condition: day-old alive needs no guard, dead Og does (9:2)
- **R-176** · Shabbat 152a:15 (Gen 50:10) — SEVEN-DAY MOURNING from 'he made for his father a mourning of seven days' (50:10)
- **R-177** · Shabbat 32a:4 (Gen 32:11) — never stand in danger counting on a miracle - merit is deducted: 'I am diminished by all the kindnesses' (32:11)
- **R-178** · Shabbat 95a:1 (Gen 2:22) — hair-plaiting on Shabbat = BUILDING: 'He BUILT the rib' - He braided Eve's hair (2:22); a labor-definition from our verse

### Shevuot (6)
- **R-179** · Shevuot 35b:11 (Gen 19:18) — every name in the Lot passage profane except 19:18 - the same classification
- **R-180** · Shevuot 35b:9 (Gen 18:3) — name-sanctity ON OUR INK: every 'Lord' of Abraham sacred except 18:3 - erasure law
- **R-181** · Shevuot 36a:13 (Gen 9:15) — NO is an oath: 'the waters shall NO more become a flood' (9:15) with Isaiah's 'I swore'
- **R-182** · Shevuot 36a:14 (Gen 9:11, 9:15) — doubled no, doubled yes: the covenant's two negations (9:11, 9:15)
- **R-183** · Shevuot 38b:20 (Gen 24:3) — the oath administered 'by the LORD': Abraham's adjuration (24:3)
- **R-184** · Shevuot 38b:22 (Gen 24:2) — grasping an object at the oath: the thigh-grasp scene (24:2)

### Sotah (3)
- **R-185** · Sotah 10b:6 (Gen 38:25) — BETTER THE FURNACE THAN SHAMING ANOTHER IN PUBLIC - derived from Tamar (Gen 38:25)
- **R-186** · Sotah 14a:4 (Gen 18:1, 25:11, 3:21) — IMITATIO DEI: clothe the naked (Gen 3:21), visit the sick (18:1), comfort mourners (25:11) - the kindness obligations rooted verse by verse
- **R-187** · Sotah 45b:17 (Gen 7:22) — THE NOSE-PREDICATE'S SECOND LAW: corpse measured FROM THE NOSE for the nearest-city rite - 'all in whose nostrils was the breath of life' (Gen 7:22); a new call site for the scan's career list

### Sukkah (1)
- **R-188** · Sukkah 11b:14 (Gen 2:6) — SUKKAH ROOFING defined from the mist: not impurity-susceptible, earth-grown (2:6)

### Taanit (4)
- **R-189** · Taanit 10b:6 (Gen 42:1) — do not display satiety in famine: 'why do you show yourselves' (42:1)
- **R-190** · Taanit 10b:7 (Gen 45:24) — no halakhic engrossment on the road: 'do not quarrel on the way' (45:24)
- **R-191** · Taanit 11a:4 (Gen 41:50) — marital relations forbidden in famine years: 'born BEFORE the famine came' (41:50), the childless excepted
- **R-192** · Taanit 22b:11 (Gen 2:7) — the self-affliction limit: 'the man became a LIVING soul - keep it alive' (2:7)

### Yevamot (15)
- **R-193** · Yevamot 100b:9 (Gen 17:7) — 'to be God to you and your seed after you' (17:7): the ban on gentile and slave unions
- **R-194** · Yevamot 17b:6 (Gen 13:8) — why the brotherhood analogy takes the sons of Jacob and not Lot's 'men brothers' (13:8) - the free-term analysis
- **R-195** · Yevamot 24a:6 (Gen 48:6) — LEVIRATE 'NAME' MEANS INHERITANCE: name-name analogy to 'on the name of their brothers in their inheritance' (48:6)
- **R-196** · Yevamot 34b:3 (Gen 38:9) — the acts of Er and Onan defined (38:9)
- **R-197** · Yevamot 34b:4 (Gen 38:10, 38:9) — Er's act inferred from the matched deaths (38:10)
- **R-198** · Yevamot 42a:6 (Gen 17:7) — the wait between husbands: distinguish the first's seed - 'to your seed AFTER you' (17:7)
- **R-199** · Yevamot 61b:13 (Gen 24:16) — betulah = maiden, from 'the maiden, very fair, a virgin' (24:16)
- **R-200** · Yevamot 61b:16 (Gen 2:18) — one must not stand without a wife even with children: 'not good that the man be alone' (2:18)
- **R-201** · Yevamot 62a:14 (Gen 22:5) — a slave has no lineage: 'sit here WITH the donkey' (22:5)
- **R-202** · Yevamot 62b:17 (Gen 3:16) — conjugal duty before a journey - the longing clause of the curse (3:16)
- **R-203** · Yevamot 63b:16 (Gen 9:6, 9:7) — neglecting procreation = shedding blood: the juxtaposition at Gen 9:6-7
- **R-204** · Yevamot 63b:17 (Gen 9:6, 9:7) — or diminishing the image - the same juxtaposition's second reading
- **R-205** · Yevamot 65b:9 (Gen 18:12, 18:13) — PEACE PERMITS THE ALTERED REPORT: God Himself changed Sarah's words (18:12-13)
- **R-206** · Yevamot 72a:7 (Gen 17:13, 17:14) — the drawn foreskin re-circumcised: himol yimol + 'my covenant he broke' (17:13-14)
- **R-207** · Yevamot 88a:13 (Gen 42:8) — identity evidence: 'Joseph recognized his brothers and they did not recognize him' (42:8) - the beard rule

### Yoma (2)
- **R-208** · Yoma 77a:14 (Gen 31:50) — marital deprivation is called AFFLICTION: 'if you afflict my daughters' (31:50) - the Yom Kippur innuy roster's source
- **R-209** · Yoma 87a:13 (Gen 50:17) — ASK FORGIVENESS AT MOST THREE TIMES: the brothers' triple plea (50:17) - a rider on our forgiveness module

### Zevachim (7)
- **R-210** · Zevachim 108b:15 (Gen 8:20) — R. Yosei's outside-slaughter source: 'Noach built an altar' (8:20)
- **R-211** · Zevachim 115b:18 (Gen 8:20) — all species valid on a private altar: 'of every clean beast and every clean fowl' (8:20)
- **R-212** · Zevachim 116a:11 (Gen 7:16) — the self-presenting animals: 'those that CAME, male and female' (7:16) - ark ink in altar law
- **R-213** · Zevachim 116a:14 (Gen 4:4) — did the sons of Noach offer peace-offerings? Abel's FATS prove it (4:4)
- **R-214** · Zevachim 53b:8 (Gen 49:27) — the altar's strip in the portion of 'Benjamin the wolf' (49:27) - Temple geography from the testament
- **R-215** · Zevachim 88b:6 (Gen 37:31) — the tunic atones for bloodshed: 'they dipped the tunic in the blood' (37:31)
- **R-216** · Zevachim 97b:9 (Gen 22:10, 22:13) — the knife and the burnt-offering from the binding (22:10, 22:13)

## HOW A CANDIDATE BECOMES A RULE (the standing path)
1. The owner picks a batch from Part II.
2. Exam first: the passage's case rows quoted into a spec (with its
   Mishnah row if one exists nearby, else the Talmud passage itself is
   the oracle), classified A/B/C via the three-strata holdings search.
3. Gaps filed to logic/findings/FINDINGS_QUEUE.md; owner rules
   seat / import-only / reject.
4. Compile into engine.py under its tractate module; exams re-run green.
5. The catalog row's status moves; the ID never changes.

INTAKE RULE (standing): a candidate qualifies only if a derived unit
already anchors its Genesis verse - true for all 206 by construction
(the triage enumerated only passages citing derived Genesis).
R-281 | MODULE temple_funds (Terumah exam 2026-09-01)
R-282 | MODULE sanctuary_extension (Terumah exam 2026-09-01)
R-283 | MODULE showbread_form (Terumah exam 2026-09-01)
R-284 | MODULE showbread_tamid (Terumah exam 2026-09-01)
R-285 | MODULE menorah_integrity (Terumah exam 2026-09-01)
R-286 | MODULE sanctuary_partition (Terumah exam 2026-09-01)
R-287 | MODULE mitzvah_orientation (Terumah exam 2026-09-01; TALMUD-ONLY — Babylonian Talmud Sukkah 45b)
R-288 | MODULE sheretz_removal (Terumah exam 2026-09-01)
R-289 | MODULE karpef_carrying (Terumah exam 2026-09-01)
R-290 | MODULE curtain_boundary (Terumah exam 2026-09-01; Makkot 3:3 backfill credit)
R-291 | MODULE oil_grades (Terumah exam 2026-09-01)
