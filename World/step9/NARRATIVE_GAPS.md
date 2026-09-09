# NARRATIVE_GAPS.md — O8 THE NARRATIVE GAPS ON THE ENGINE (2026-09-08)

The owner's ruling (the state doc, compaction point #90, "I want to finish all of them"; #97's tail; this sitting "08 go"):
FIRST the census by script — every frozen Genesis and Exodus unit whose verses no engine scene submits — THEN the
uncovered stretches as scenes in the sequential conventions (SEQUENTIAL_RUN.md section 9), sized into sittings by the
census, each with its daemon declared first, the tape re-stitched after each, the gaps line of the sequence runner
shrinking to the ink's own silences. This file is the design: section 1 the census as computed, section 2 the sizing,
section 3 the conventions this campaign adds, section 4 the FIRST sitting's declaration (Exodus 1-19), section 5 the
later sittings sketched. Declared BEFORE the code; every citation below was resolved on the local shelf by script
(scratchpad shelf_find.py and the Mishnah/Mekhilta/Bavli file readers, nikud stripped) at this sitting.

## 1. THE CENSUS (scratchpad o8_census.py; its print o8_census.txt — computed, never recited)

The instrument: every unit file logic/units/gen_*.yaml and exo_*.yaml (164 files: 98 Genesis, 66 Exodus) read for its
meta.refs, genre and status; the range expanded to verses over the Tanakh DB's own verse counts; the sequential tape
(cold_run_sequence.py's sentinel section) parsed for every literal submit's case_source verses and every marker's
verse; the corpus world's events table (corpus_world.sqlite, read-only; 557 events on 436 verses of 79 units) and its
demands table joined by unit; the entity registry's step9-scenes members counted.

- The files are 114 FROZEN + 50 DRAFT. The drafts are the old tree-derived v1 duplicates of frozen units (exo_01_israel_
  egypt_oppression beside exo_01_names_and_midwives, and the like); they are counted apart and take no scene.
- THE TAPE: 139 events, 69 markers (the O5-O7 state).
- GENESIS: 73 frozen units; 54 carry NO tape event (all narrative-register); 13 of those carry MARKERS ONLY (the clock
  stamps ride, no act): gen_14 (19 markers), gen_17 (1), gen_19 (4), gen_23 (1), gen_26 (10), gen_27 (1), gen_32 (1),
  gen_42 (2), gen_43 (2), gen_45 (1), gen_58 (1), gen_64 (1), gen_70 (2). The contiguous stretches of the 54:
    Gen 2:4-8:22     13 units  172 verses  corpus events 149  demands 11  markers 24
    Gen 9:18-16:16   10 units  175 verses  corpus events 146  demands 29  markers 13
    Gen 18:1-20:18    3 units   89 verses  corpus events  42  demands 26  markers 0
    Gen 22:1-24       1 unit    24 verses  corpus events   8  demands  4  markers 0
    Gen 25:1-31:54   13 units  269 verses  corpus events  76  demands 49  markers 5
    Gen 33:1-37:36    5 units  159 verses  corpus events   5  demands 37  markers 1
    Gen 39:1-47:31    9 units  302 verses  corpus events  17  demands 37  markers 3
  TOTAL 54 units, 1,190 verses, 443 corpus events, 193 demands.
- EXODUS: 41 frozen units; 30 carry no tape event = 20 narrative-register + 10 law/spec-register (exo_20-23, 25-30 —
  the law engines' spans: the decalogue, the ordinances, the guardians, the Mishpatim runners, the calendar, the
  sanctuary spec, the vestments, the investiture, the incense and shekel — compiled as LAW, not narrative). The 20:
    Exod 1:1-19:25   19 units  519 verses  corpus events 21  demands 81  markers 5 (7:7, 12:2, 12:41, 16:1, 19:1)
    Exod 23:20-33     1 unit    14 verses  corpus events  0  demands  0  markers 0 — exo_23_escort_land: the angel's
                     escort and the land's promise, a SPEECH inside the ordinances runner's declared span
                     ([Exod 23:20-33] is compiled there: nations_driven_out, covenant_barred, demolished on
                     entered_the_land); its genre label reads narrative, its ink is a law promise. NOT A GAP.
  Markers-only in Exodus: exo_07 (7:7), exo_12 (12:2, 12:41), exo_16 (16:1), exo_19 (19:1).
- THE COVERED units and their kinds are listed in o8_census.txt (section "COVERED units"). The verse-grain gaps inside
  a covered unit (Gen 50:24-26 Joseph's oath; the inside of Gen 6-9's flood beyond 9:1-17) are the reading's business
  at each sitting, not the census's: the census is at the unit grain, as the plan asked.

## 2. THE SIZING — four sittings, by the census

The plan expected two to four. The census's stretches fall into FOUR sittings, each one daemon, in this order (the
plan's own: Exodus first):

- S1 EXODUS 1-19 THE STORY — 19 frozen units, 519 verses, 81 demands: the names and the midwives, the birth and the
  flight, the bush, the signs, the bricks, "I am the LORD", the ten plagues, the night and the going out (the acts of
  12:29-42 and 12:50-51; the LAW of 12:1-28, 12:43-49, 13:1-16 stays the Passover engine's), the pillars and the bones,
  the sea, the song and Marah, the manna and the first Sabbath, Massah and Amalek, Jethro and the judges, Sinai's acts.
  Runner cold_run_exodus_story.py, daemon law_exodus_story. THIS SITTING (section 4).
- S2 GENESIS 2:4-16:16 FROM EDEN TO HAGAR — 23 frozen units, 347 verses, 295 corpus events, 40 demands: the garden and
  the sentences, Cain, the lines, the flood's inside (the prologue, the ark's spec, the boarding, the rise, the
  remembering, the exit), the vineyard, the nations, Babel, Shem's line, the call, the descent to Egypt, the
  separation, the war of the kings, the pieces, Hagar. Runner cold_run_primeval.py (a working name — the sitting
  declares), daemon law_primeval.
- S3 GENESIS 18:1-31:54 FROM MAMRE TO THE HEAP — 17 frozen units, 382 verses, 126 corpus events, 79 demands: Mamre and
  the plea, Sodom, Gerar, the binding, Abraham's end and Ishmael's line, the twins and the birthright, Isaac at
  Gerar, the wells, the blessing, the flight, Bethel, the well and Rachel, the wage and the switched bride, the
  womb and the names, the speckled wage, the flight over the river, the pursuit and the heap.
- S4 GENESIS 33:1-47:31 AND 50:15-26 FROM THE RETURN TO GOSHEN — 14 frozen units + gen_73's uncovered verses, ~470
  verses, 22 corpus events, 74 demands: the return and the first altar, the gate, Bethel and the three deaths,
  Edom's ledger, the dreamer sold, Potiphar's house, the two dreams, Pharaoh's dreams and the rise, the two descents,
  the cup, "I am Joseph", the seventy, Goshen and the fifth; and Joseph's forgiveness, his OATH (50:25 — the bones
  Exodus 13:19 carries) and his death.
Each sitting: the declaration (in this file, its own section), the types and effects registered first by script, the
daemon declared and the gate run to fail, the span on a stub and the census run with --emit, the predictions printed
by script, the code, the run, the tape re-stitched, the sequence runner's literals re-predicted, the gates, the sweep,
the records. After S4 the sequence runner's gaps line should read the ink's own silences only (Genesis 50 to Exodus 1's
193 years is not a gap the tape can fill: the ink narrates nothing there beyond 1:6-8 and 2:23's "many days").

## 3. THE CONVENTIONS THIS CAMPAIGN ADDS (for THE_STEPS' sequential-run paragraph, after S1 proves them)

13. A narrative runner's OWN scene is a bare-world unit test with scene days (the pre_sinai and family shape); THE TAPE
    carries the ink's markers, kept in the stitcher's one table (section 4 of SEQUENTIAL_RUN.md) and verified against
    the ink parse there — no second copy of the parser, no marker typed twice. The stitcher's CLOCK_DAY_RUNNERS list
    names the runner so its scene days are dropped on the tape.
14. ONE ACT, ONE WRITER PER EFFECT holds across the story and the law: when the story's scene submits a kind an older
    daemon consumes without a seat check (married, people_answered), that daemon GAINS the seat check its own span
    implies (rule 11's enforcement, not a new rule), and the story's daemon writes the story's status; the registry's
    tape line declares the two layers. A statute's own recorded RUN (the eighth-day timer on every `born` — Gen 17:12
    "throughout your generations") is not seat-scoped: the covenant's law runs on Moses' and Gershom's births.
15. A PROMISE is a HEAVEN entry OPEN until the ink's own fulfillment statement closes it (the four expressions of
    6:6-8; the firstborn's death decreed at 4:23; Amalek's blotting at 17:14). A close that finds nothing open because
    the opening verse is a LATER sitting's write (Gen 15:14's substance closed at Exod 12:36; Gen 50:25's oath closed
    at Exod 13:19) is expected, printed, and counted again when that sitting lands.
16. A PLAGUE or a DECREE is a HEAVEN or DEBIT entry on the struck or bound party, closed by the narrated removal or
    refusal only; where the ink narrates no removal the entry stays open — the ink's own shape (four of the ten
    plagues are removed by an act; six are not).
17. THE TRADITION'S DAY-TABLES ARE DATA ROWS WITH THEIR ARMS (Sivan's days by Rabbi Yose and by the rabbis; Moses'
    birthday on the seventh of Adar; the ark's day by two amoraim); the engine's WEEKDAY from the creation count (day
    0 = "day one", day 6 = the first Sabbath) is an engine derivation printed AGAINST the shelf's weekday rows as
    checkpoints — a DIVERGE on the anchor is the modeled calendar's (OPEN-2/OPEN-4), a MATCH on the spacing is the
    shelf's own month lengths reproduced.
18. THE MODELED PLACEMENT OF AN UNDATED STRETCH: an age-at-event marker inside an undated stretch walks the clock to
    that year's FIRST DAY and says so (7:7's "Moses eighty at the speaking" opens the plagues at the first day of his
    eightieth year); the ink's relative stamps ("tomorrow", "seven days", "three days") then walk from there; the
    tradition's bound on the stretch (Mishnah Eduyot 2:10, the Egyptians' judgment twelve months) is graded as a bound.

## 4. S1 — EXODUS 1-19 THE STORY: THE DECLARATION

### 4a. The span, the runner, the daemon
- Span `exodus_story` (dependency_dispositions.yaml): [[Exod,1,1,22],[Exod,2,1,25],[Exod,3,1,22],[Exod,4,1,31],
  [Exod,5,1,23],[Exod,6,1,30],[Exod,7,1,29],[Exod,8,1,28],[Exod,9,1,35],[Exod,10,1,29],[Exod,11,1,10],
  [Exod,12,29,42],[Exod,12,50,51],[Exod,13,17,22],[Exod,14,1,31],[Exod,15,1,27],[Exod,16,1,36],[Exod,17,1,16],
  [Exod,18,1,27],[Exod,19,1,25]] — the Passover engine's verses (12:1-28, 12:43-49, 13:1-16) excluded: their acts
  on the tape are the Passover engine's own (12:28 "and the sons of Israel went and did" is its run; the exam's rows
  stay off the tape).
- Runner cold_run_exodus_story.py (no module of that name exists — the collision guard); daemon `law_exodus_story`,
  `wraps: exodus_story`; every cell function WRAPPED by it.
- The census run with --emit on the stub before a cell; the expected edges: REFERENCE edges where the ink names an
  institution compiled elsewhere (the Sabbath at 16:23-30, the burnt offering and sacrifices at 18:12, the covenant at
  19:5, the firstborn at 4:22-23 and 12:29, the Passover night at 12:29-42); FALSE where a homograph (the omer as a
  measure at 16:16-36 against the sheaf; the pledge-word); each dispositioned before a cell with its link class.

### 4b. The types (event_vocabulary.yaml; NEW unless marked; witnesses cut from the verses' consonants by script and
verified by the lint against the Tanakh DB; the form by the register test — every act on a verse with a narrative verb)
Acts: king_arose (1:8) · taskmasters_set (1:11) · made_to_serve (1:13) · lives_embittered (1:14) · decree_refused
(1:17) · houses_made (1:21) · married [REUSE, +2:1 and 2:21 witnesses; link reference] · born [REUSE, +2:2, 2:22] ·
hidden (2:2) · placed_in_the_ark (2:3) · drawn_from_the_water (2:5-6, 2:10) · named (2:10, 2:22, 15:23, 16:31, 17:7,
17:15 — the ink's "called its name"; fields name) · egyptian_struck (2:12) · fled (2:15) · king_died (2:23) ·
cry_went_up (2:23) · appeared_in_the_bush (3:2) · signs_shown (4:3-7, 4:30 — fields count) · returned_to_egypt (4:20)
· circumcised [REUSE, +4:25 witness] · believed (4:31; 14:31) · release_refused (5:2) · straw_withheld (5:7-10) ·
officers_beaten (5:14) · not_heard (6:9) · staff_swallowed (7:12) · plague_struck (7:20 blood, 8:2 frogs, 8:13 lice,
8:20 swarms, 9:6 pestilence, 9:10 boils, 9:23 hail, 10:13 locusts, 10:22 darkness, 12:29 the firstborn — fields
plague, by) · heart_hardened (the fifteen seats of the ink census: 7:13, 7:22, 8:11, 8:15, 8:28, 9:7, 9:12, 9:34,
9:35, 10:20, 10:27, 11:10, 14:4, 14:8, 14:17 — fields agent: pharaoh / the_lord, verb: strong / heavy) ·
plague_removed (8:9 frogs, 8:27 swarms, 9:33 hail, 10:19 locusts — the four Pharaoh entreated for) · driven_from_court
(10:11) · face_barred (10:28) · sent_out (12:31-33) · vessels_asked (12:35-36) · journeyed (12:37 Rameses to Succoth,
13:20 Etham, 14:2 Pi-hahiroth, 15:22 the wilderness of Shur, 15:23 Marah, 15:27 Elim, 16:1 Sin, 17:1 Rephidim, 19:2
Sinai — fields to) · brought_out (12:51) · bones_taken (13:19) · pillar_set (13:21) · pursued (14:8-9) · sea_split
(14:21) · sea_returned (14:27-28) · saved_at_the_sea (14:30) · sang (15:1; 15:21) · waters_sweetened (15:25) ·
statute_set (15:25 — the narrator's clause) · murmured (15:24 Marah, 16:2-3 the fleshpot, 17:2-3 Rephidim; 14:11 the
sea; 16:20 left till morning; 16:27 went out on the seventh — fields trial) · manna_fell (16:13-15) · double_gathered
(16:22) · rested_on_the_seventh (16:30) · omer_kept (16:33-34) · rock_struck (17:6) · amalek_came (17:8) ·
hands_raised (17:11-12) · amalek_weakened (17:13) · jethro_came (18:5) · jethro_sacrificed (18:12) ·
judges_appointed (18:25) · moses_went_up (19:3, 19:8, 19:20 — fields ascent) · people_answered [REUSE, +19:8
witness; link reference; the erection daemon seat-checked to Exod 24] · people_sanctified (19:14) · bounds_set (19:12,
19:23) · thunder_and_horn (19:16) · lord_descended (19:20).
Speech: decree_issued (1:16 the midwives; 1:22 all his people — fields decree) · holy_ground_declared (3:5) ·
sent_to_pharaoh (3:10) · name_declared (3:14-15) · mouth_appointed (4:14-16) · firstborn_death_decreed (4:22-23) ·
redemption_promised (6:6-8 — fields expressions) · now_you_will_see (6:1) · wealth_promised (3:21-22; 11:2) ·
covenant_offered (19:5-6) · healer_promised (15:26) · blotting_sworn (17:14-16).
The `tape:` line of every reused kind declares the two layers; `link: reference` with the shared content lemma named.

### 4c. The effects (effect_vocabulary.yaml; NEW unless marked; each ink claim machine-verified before the append; the
ledger op in brackets — the registry's own classes: status, debit, heaven, body, block, transfer, timer, destroy)
- enslaved [status, israel_people] 1:13 וַיַּעֲבִדוּ מִצְרַיִם אֶת בְּנֵי יִשְׂרָאֵל בְּפָרֶךְ (and Egypt made the sons of Israel serve
  with rigor); the tradition's word: Mishnah Pesachim 10:5 מֵעַבְדוּת לְחֵרוּת (from slavery to freedom), מִשִּׁעְבּוּד לִגְאֻלָּה (from
  bondage to redemption); Pesachim 116a:11 Shmuel's opening עֲבָדִים הָיִינוּ (we were slaves). Closed at 12:51.
- embittered [status, israel_people] 1:14 וַיְמָרְרוּ אֶת חַיֵּיהֶם (and they embittered their lives) — Mishnah Pesachim 10:5's
  maror reason in the ink's own verb; Sotah 11b:1 on "with rigor" (soft speech / crushing).
- decree_issued [debit on the addressee, cp the king] 1:16, 1:22 — Sotah 12a:8 (Rabbi Yose son of Rabbi Chanina: three
  decrees: 1:16, 1:22, and 1:22 read "even on his own people") — the value the decree's text; the midwives' entry
  closed by the refusal (decree_refused), the people's stays open (the ink narrates no execution).
- feared_god [status, the midwives] 1:17, 1:21 · houses_made [status, the midwives] 1:21 וַיַּעַשׂ לָהֶם בָּתִּים (and He made
  them houses) — Sotah 11b:22: houses of priesthood and Levites (Rav) / of kingship (Shmuel): the value the two arms.
- wife_taken [REUSE, status] 2:1, 2:21 — the same formula (the family engine's word); Sotah 12a:10-13 the retaking.
- hidden_three_months [timer, moses] 2:2 וַתִּצְפְּנֵהוּ שְׁלֹשָׁה יְרָחִים (and she hid him three months) — the due by the
  Calendar (three months); Sotah 12a:18 (the Egyptians counted from the retaking) and 12b:15-17 (the ark's day: the
  twenty-first of Nisan, Rabbi Chanina bar Papa; the sixth of Sivan, Rabbi Acha bar Chanina — "from the seventh of
  Adar to the sixth of Sivan is three months").
- drawn_out [status, moses] 2:10 (the naming's reason: מִן הַמַּיִם מְשִׁיתִהוּ (from the water I drew him)).
- name_given [status on the named] 2:10, 2:22, 15:23, 16:31, 17:7, 17:15 — the value the name (English with the
  Hebrew).
- sought_to_kill [body, moses, cp the king] 2:15 וַיְבַקֵּשׁ לַהֲרֹג אֶת מֹשֶׁה (and he sought to kill Moses) — closed at 2:23 by
  the king's death with 4:19's note ("all the men who sought your life are dead").
- cry_heard [REUSE, heaven, israel_people] 2:24 וַיִּשְׁמַע אֱלֹהִים אֶת נַאֲקָתָם (and God heard their groaning), 3:7 — the
  ordinances' word (22:22) at its narrative seat: a REFERENCE (hear + cry).
- covenant_remembered [REUSE, status] 2:24 וַיִּזְכֹּר אֱלֹהִים אֶת בְּרִיתוֹ (and God remembered His covenant) — Lev 26:42's
  own words at their run: a REFERENCE.
- holy_ground [status, the place] 3:5 · sent_to_pharaoh [debit, moses, cp Heaven] 3:10 וְאֶשְׁלָחֲךָ אֶל פַּרְעֹה וְהוֹצֵא אֶת
  עַמִּי (and I will send you to Pharaoh, and bring out My people) — closed at 12:51.
- name_declared [status, god] 3:14-15 — Berakhot 9b:6 ("I was with you in this bondage and will be with you in the
  bondage of the kingdoms" — the value's gloss).
- signs_in_hand [status, moses] 4:2-9 (value 3: the staff, the hand, the water) · staff_of_god [status, the staff]
  4:20 מַטֵּה הָאֱלֹהִים (the staff of God) — Mishnah Avot 5:6 (the staff among the ten things created at twilight: the
  answer-sheet row).
- mouth_appointed [status, aaron, cp moses] 4:16 וְהָיָה הוּא לְךָ לְפֶה (and he shall be to you a mouth) · mark_of_anger
  [status, moses] 4:14 — Zevachim 102a:6-8: Rabbi Yehoshua ben Korcha (no mark here), Rabbi Shimon ben Yochai ("I
  said you would be priest and he Levite; now he is priest and you Levite" — the priesthood's transfer), the sages
  (Moses served as priest only the seven days of installation): the value the three arms.
- firstborn_death_decreed [heaven, paro_exodus_era] 4:23 הִנֵּה אָנֹכִי הֹרֵג אֶת בִּנְךָ בְּכֹרֶךָ (behold I kill your son,
  your firstborn) — closed at 12:29.
- circumcision_due [REUSE, timer] — the pre-Sinai daemon's own run on `born` (2:2 Moses, 2:22 Gershom); Nedarim
  31b:13-32a:3 (was Moses lax about the circumcision — Rabbi Yehoshua ben Korcha yes, Rabbi no: "I will circumcise and
  go out — a danger"; he busied himself with the lodging first; Rabban Shimon ben Gamliel: the infant was sought, not
  Moses); Sotah 12a:17 (Moses born circumcised — "others say"; the timer fires at his eighth day and no act closes it:
  the ink's silence, the shelf's row beside it).
- believed [status, israel_people] 4:31 וַיַּאֲמֵן הָעָם (and the people believed), 14:31 וַיַּאֲמִינוּ בַּיהוָה וּבְמֹשֶׁה עַבְדּוֹ
  (and they believed in the LORD and in Moses His servant) — Mekhilta Shirata 1:1 (the song in the merit of faith).
- release_demanded [debit, paro_exodus_era, cp israel_people] 5:1 שַׁלַּח אֶת עַמִּי (let My people go) — refused 5:2,
  closed at 12:31 by sent_out; the Mekhilta on 13:17 ("the mouth that said 'I will not send' said 'I will send you'").
- straw_withheld [status, israel_people] 5:7 · beaten [body, the officers] 5:14 וַיֻּכּוּ שֹׁטְרֵי בְּנֵי יִשְׂרָאֵל (and the
  officers of the sons of Israel were beaten).
- now_you_will_see [heaven, moses] 6:1 עַתָּה תִרְאֶה (now you will see) — Sanhedrin 111a:10: what I do to Pharaoh you will
  see, the war of the thirty-one kings you will not — OPEN to Deuteronomy 34 (book-bound; the prediction the ledger
  holds).
- to_be_brought_out / to_be_delivered / to_be_redeemed / to_be_taken_as_a_people / to_be_brought_to_the_land [heaven,
  israel_people] 6:6-8 — the five expressions in the ink's own verbs: וְהוֹצֵאתִי (I will bring out), וְהִצַּלְתִּי (I will deliver),
  וְגָאַלְתִּי (I will redeem), וְלָקַחְתִּי (I will take), וְהֵבֵאתִי (I will bring in); closed at 12:51 (out), 14:30 (delivered — the ink's וַיּוֹשַׁע, saved),
  15:13 (redeemed — the song's גָּאָלְתָּ), 19:8 (taken — the acceptance of 19:5-6's "you shall be to Me"); the fifth OPEN
  (Joshua — book-bound).
- not_heard [status, israel_people] 6:9 · shortness_of_spirit is its value.
- plague_struck [REUSE, heaven, egypt_people] the ten — the calf's registered verb (32:35 וַיִּגֹּף, and He plagued) at
  12:23, 12:27 (לִנְגֹּף, בְּנָגְפּוֹ — to plague, when He plagued Egypt), 9:14 (מַגֵּפֹתַי, My plagues), 11:1 (נֶגַע, a plague): a
  REFERENCE by lemma; the value the plague's name; Mishnah Avot 5:4 (ten plagues in Egypt — the count graded on the
  ledger); Mekhilta Beshalach ch.31 row 2 (Rabbi Yose HaGelili: ten in Egypt, fifty at the sea — the finger and the
  hand; Avot's ten at the sea beside it: the sea's plagues are derived, not narrated — one act on the tape).
- heart_hardened [status, paro_exodus_era] the fifteen seats — the value (agent, verb) per seat from the ink census:
  the first divine agent at 9:12 (וַיְחַזֵּק יְהוָה — and the LORD strengthened) after five of Pharaoh's own; the
  tradition's "five times" not found on the local shelf under the searched forms (labeled a remark).
- plague_removed [status, egypt_people] 8:9, 8:27, 9:33, 10:19 — the four entreated (8:4, 8:24, 9:28, 10:17: the corpus
  world's four "entreat" demands, settled in-unit); the heaven entry closed by the scene at each.
- barred_from_the_face [block, moses] 10:28 אַל תֹּסֶף רְאוֹת פָּנַי (do not again see my face); Zevachim 102a:10 (the
  anger's mark at 11:8 — Reish Lakish: he slapped him and went out).
- sent_out [transfer, israel_people] 12:31-33 קוּמוּ צְּאוּ (rise, go out) — closes release_demanded.
- egypt_emptied [transfer, egypt_people → israel_people] 12:36 וַיְנַצְּלוּ אֶת מִצְרָיִם (and they emptied Egypt) — Sanhedrin
  91a:10-12 (Gebiha ben Pesisa before Alexander: the wage of six hundred thousand who served four hundred and thirty
  years — 12:40's own number as the wage's term); Berakhot 9a:29-9b:2 ("please" — so that the righteous one will not
  say: 'and they shall serve them and afflict them' He fulfilled, 'afterwards they go out with great substance' He did
  not — Gen 15:14's promise, S2's write, closed here); the Mekhilta Pischa ch.35 row 1 (the garments dearer than the
  silver and gold).
- brought_out [transfer, israel_people] 12:51 — closes enslaved, sent_to_pharaoh, to_be_brought_out; Mishnah Pesachim
  10:5's five transitions as the answer-sheet row on the close.
- encamped_at [status, israel_people] the nine stations — the value the place; Numbers 33's list the RUN's citation
  (book-bound).
- bones_carried [status, moses] 13:19 וַיִּקַּח מֹשֶׁה אֶת עַצְמוֹת יוֹסֵף עִמּוֹ (and Moses took the bones of Joseph with him) —
  Mishnah Sotah 1:9 (Moses merited the bones of Joseph); Sotah 13a:13-13b:5 (Serach bat Asher; the two verses — Moses
  took, the sons of Israel brought up; Joshua 24:32 buries — book-bound); the Mekhilta Pischa-b ch.19 rows 1-9; closes
  Gen 50:25's oath (S4's write).
- pillar_leads [status, israel_people] 13:21-22 · pursued_by_egypt [body, israel_people] 14:8-9 · sea_split [status,
  the sea] 14:21 · egypt_drowned [destroy, egypt_people] 14:28 לֹא נִשְׁאַר בָּהֶם עַד אֶחָד (not one of them remained) ·
  saved [status, israel_people] 14:30 וַיּוֹשַׁע יְהוָה (and the LORD saved) — closes to_be_delivered and
  pursued_by_egypt.
- song_sung [status, israel_people] 15:1 — Mishnah Sotah 5:4 (Rabbi Akiva: they answered after Moses word by word as
  the Hallel is read; Rabbi Nechemya: as the Shema); Sotah 30b:11-13 (three arms: as the adult reading the Hallel, as
  the minor, as the scribe who begins); the value the arms.
- waters_sweetened [status, the waters] 15:25 · statute_set_at_marah [status, israel_people] 15:25 שָׁם שָׂם לוֹ חֹק
  וּמִשְׁפָּט (there He set for him a statute and an ordinance) — Sanhedrin 56b:15-16 (ten commandments at Marah: the seven
  of Noah's sons, and courts, the Sabbath, honoring father and mother — the value); Shabbat 87b:1 (the Sabbath
  commanded at Marah); Mekhilta Shirata ch.25 row 2 (the tree's four readings).
- healer_promised [heaven, israel_people] 15:26 (conditional — the value the condition).
- tested_the_lord [status counter, israel_people] the trials — Arakhin 15a:14-15b:2 (Rabbi Yehuda's ten: two at the
  sea, two at the water, two at the manna, two at the quail, one at the calf, one at Paran); the tape's own by Exodus
  19: the sea's descent (14:11), Marah (15:24), the fleshpot (16:3 — the first quail), the manna twice (16:20, 16:27),
  Rephidim (17:2-3) = SIX; the sea's ascent is Psalm 106:7's (off the three books), the calf is the erection daemon's
  span, the second quail and Paran are Numbers'.
- manna_provided [status, israel_people] 16:4-5, 16:35 (the value: a day's portion each day, double on the sixth, none
  on the seventh; forty years) — Kiddushin 38a:3-4 (forty years less thirty days; the cakes tasted of manna); Mekhilta
  Vayassa ch.35 row 1; Mishnah Avot 5:6 (the manna created at twilight — the row); no period timer on the tape (the
  forty years run past the three books; the daily re-arm would be fourteen thousand fires with no ink at each).
- omer_kept [status, the jar] 16:33-34 (before the Testimony — the ink's own anachronism, named).
- water_from_the_rock [status, israel_people] 17:6 · amalek_weakened [body, amaleq] 17:13 וַיַּחֲלֹשׁ (and he weakened) ·
  prevailed [status, israel_people] 17:11 — Mishnah Rosh Hashanah 3:8 (do Moses' hands make war? when Israel looked
  upward and subjected their heart to their Father in heaven they prevailed — the value) · amalek_to_be_blotted
  [heaven, amaleq] 17:14 מָחֹה אֶמְחֶה אֶת זֵכֶר עֲמָלֵק (I will surely blot out the memory of Amalek) — OPEN (Deuteronomy
  25:19, 1 Samuel 15 — book-bound).
- offered_burnt_and_sacrifices [status, reuel_yitro] 18:12 — Zevachim 116a:19-21 (Jethro before or after the giving of
  the Torah — the sons of Rabbi Chiya and Rabbi Yehoshua ben Levi; Rabbi Yehoshua: he heard of Amalek's war; Rabbi
  Elazar HaModai: of the giving; Rabbi Eliezer: of the sea) — the value the fork; the placement stays the ink's order
  (section 4h, OPEN-9).
- courts_established [status, israel_people] 18:25 — the value the four denominations and the computed total 78,600
  from 12:37's six hundred thousand (Sanhedrin 18a:3) · hard_cases_to_moses [status] 18:26.
- treasured_people [heaven, israel_people, conditional] 19:5-6 · undertook_to_do [status, israel_people] 19:8 כֹּל
  אֲשֶׁר דִּבֶּר יְהוָה נַעֲשֶׂה (all that the LORD has spoken we will do) — Shabbat 88a:5 (the mountain held over them; Rava:
  they accepted it again in the days of Ahasuerus); Mekhilta Bachodesh ch.8 row 1 (with one heart) — closes
  to_be_taken_as_a_people.
- sanctified_for_the_third_day [timer, israel_people] 19:10-11 (due today + 2 by the ink; Shabbat 87a:2-3 Rabbi Yose:
  Moses added a day of his own accord — the giving on the seventh; the rabbis: the sixth) · mountain_barred [block,
  israel_people] 19:12-13, 19:21-24 (released "when the horn sounds long" — never narrated on the tape: OPEN) ·
  descended_on_the_mountain [status, the mountain] 19:18-20.

### 4d. The daemon's watches (daemon_dispositions.yaml — declared BEFORE the code; the gate run to fail)
law_exodus_story: king_arose → [] (the ink's act, no state: 1:8's king "who did not know Joseph" writes nothing the
tradition names — the coverage line will show a watched kind with no effect; declared so) — no: the registry demands
a written effect per fired kind; the act is folded into taskmasters_set's row. The watches:
  taskmasters_set → [enslaved]; made_to_serve → [enslaved]; lives_embittered → [embittered]; decree_issued →
  [decree_issued]; decree_refused → [feared_god]; houses_made → [houses_made]; married → [wife_taken] (the seat Exod
  2 only); hidden → [hidden_three_months]; placed_in_the_ark → []; drawn_from_the_water → [drawn_out]; named →
  [name_given]; egyptian_struck → []; fled → [sought_to_kill]; king_died → []; cry_went_up → [cry_heard,
  covenant_remembered]; appeared_in_the_bush → []; holy_ground_declared → [holy_ground]; sent_to_pharaoh →
  [sent_to_pharaoh]; name_declared → [name_declared]; signs_shown → [signs_in_hand]; mouth_appointed →
  [mouth_appointed, mark_of_anger]; firstborn_death_decreed → [firstborn_death_decreed]; returned_to_egypt →
  [staff_of_god]; believed → [believed]; release_refused → [release_demanded]; straw_withheld → [straw_withheld];
  officers_beaten → [beaten]; now_you_will_see → [now_you_will_see]; redemption_promised → [to_be_brought_out,
  to_be_delivered, to_be_redeemed, to_be_taken_as_a_people, to_be_brought_to_the_land]; not_heard → [not_heard];
  staff_swallowed → []; plague_struck → [plague_struck]; heart_hardened → [heart_hardened]; plague_removed →
  [plague_removed]; driven_from_court → []; face_barred → [barred_from_the_face]; wealth_promised → []; sent_out →
  [sent_out]; vessels_asked → [egypt_emptied]; journeyed → [encamped_at]; brought_out → [brought_out]; bones_taken →
  [bones_carried]; pillar_set → [pillar_leads]; pursued → [pursued_by_egypt]; sea_split → [sea_split]; sea_returned
  → [egypt_drowned]; saved_at_the_sea → [saved]; sang → [song_sung]; waters_sweetened → [waters_sweetened];
  statute_set → [statute_set_at_marah]; healer_promised → [healer_promised]; murmured → [tested_the_lord];
  manna_fell → [manna_provided]; double_gathered → []; rested_on_the_seventh → []; omer_kept → [omer_kept];
  rock_struck → [water_from_the_rock]; amalek_came → []; hands_raised → [prevailed]; amalek_weakened →
  [amalek_weakened]; blotting_sworn → [amalek_to_be_blotted]; jethro_came → []; jethro_sacrificed →
  [offered_burnt_and_sacrifices]; judges_appointed → [courts_established, hard_cases_to_moses]; moses_went_up → [];
  covenant_offered → [treasured_people]; people_answered → [undertook_to_do] (the seat Exod 19 only);
  people_sanctified → [sanctified_for_the_third_day]; bounds_set → [mountain_barred]; thunder_and_horn → [];
  lord_descended → [descended_on_the_mountain].
A kind watched with an empty list is an act the ink narrates whose ledger state the tradition names nowhere on the
shelf at this sitting; the daemon returns nothing and the coverage line shows it — kept on the tape for the record
(the narrative-verb test, the 'and he did' form, admits it), declared under the watches with its empty list as the gate reads it. [AS RUN: the gate
refuses a watched kind with no effect? — measured at the gate run; if refused, the kinds move to the tape as unconsumed
with a why, or gain the status the ink itself states.]

### 4e. The registry (logic/corpus/entity_registry.yaml — members with units [step9-scenes])
Existing entities gain the scene tokens: moses ← 'moses'; aaron ← 'aaron'; miryam ← 'miriam'; yehoshua ← 'joshua';
chur ← 'hur'; amram ← 'amram'; yokheved ← 'jochebed'; reuel_yitro ← 'jethro'; paro_oppression_era ← 'the-oppression-
king'; paro_exodus_era ← 'pharaoh'; amaleq ← 'amalek'; israel_people ← 'israel' (exists); levi ← 'levi'; joseph ←
'joseph'. NEW entities (units [step9-scenes]): zipporah, gershom (Exod 2:22, 18:3), the_midwives (1:15-21, Shiphrah
and Puah), pharaohs_daughter (2:5-10), egypt_people (the Egyptians as a body), the_magicians, the_elders_of_israel,
the_officers (5:14-21), the_son_at_the_lodging (4:25 "her son" — UNCERTAIN: Nedarim 32a:2 "the infant"; the ink names
one son by 2:22 and two by 4:20; the tradition's Eliezer not on the local shelf — resolved to its own singleton, the
identity filed for the fold's sitting O10), kohath (6:18), the_staff, the_sea, the_rock, the_mountain, the_jar.

### 4f. The calendar rows (calendar_parameters.yaml)
- moses_birth_date {month 12, day 7} — Kiddushin 38a:5-7 (on the seventh of Adar Moses died and on the seventh of Adar
  he was born — "He fills the years of the righteous from day to day"); the birth's day within its year by the shelf's
  row (convention 9); the year from 7:7 (eighty at the speaking).
- sinai_days {r_yose: {second_ascent 2, boundary 3, separation 4, giving 7}, rabbis: {second_ascent 3, boundary 4,
  separation 5, giving 6}} — Shabbat 86b:5-87a:6; the running setting r_yose (the tape's ascent marker stands at the
  seventh, Taanit 28b); 87a:2-3 the added day.
- exodus_weekday {shelf: 5 (Thursday), Shabbat 87b:2-3} and iyar_length {rabbis 30 (87b:3 "Iyar of that year was
  full"), r_yose 29} — data for the weekday checkpoints only; the engine's weekday is the creation count's.
- ark_day {r_chanina_bar_papa: {1, 21}, r_acha_bar_chanina: {3, 6}} — Sotah 12b:15-17 — graded against the ink's three
  months from the birth (the checkpoint CS0).
- jethro_timing {before (Rabbi Yehoshua, the war of Amalek heard), after (Rabbi Elazar HaModai, the giving heard)} —
  Zevachim 116a:20-21, Mekhilta Yitro ch.1 row 1; the running setting before (the ink's order); OPEN-9.

### 4g. The markers (the stitcher's table; every number parsed from the ink and re-verified at run time)
  Exod 2:2   F  born:moses = the seventh of Adar of (exodus_year − 80) — the number 80 from 7:7 (assert_ink at 7:7),
             the day from the row moses_birth_date; the era life:moses set HERE (7:7's marker no longer sets it);
             position 2:2, the number's verse 7:7 (the 21:5/21:2 form).
  Exod 2:3   F  the ark = born:moses + 3 months (the ink's 3 at 2:2; the Calendar's month key).
  Exod 7:7   F  the speaking = the first day of Moses' eightieth year (modeled, said so — convention 18); 83 for Aaron
             verified; life:aaron set at exodus − 83 years (as before).
  Exod 7:25  F  +7 days (the river) · 8:6 F +1 (the frogs' morrow — the ink's "tomorrow") · 8:19 F +1 (the swarms) ·
  9:5-6 F +1 (the pestilence "on the morrow") · 9:18 F +1 (the hail "tomorrow") · 10:4 F +1 (the locusts) · 10:22 F
  +3 (the darkness's three days).
  Exod 12:2  F  the epoch (as before) · 12:3 F the tenth (the lamb taken) · 12:6 F the fourteenth · 12:29 F the
             fifteenth (the night's midnight — the day boundary is the evening: the night belongs to the fifteenth;
             = the exodus day, 12:41's marker at the same day) · 12:41 F (as before).
  Exod 15:22 F +3 days (Shur) · 16:1 F (as before) · 16:13 F +1 (the manna's first morning).
  Exod 19:1  F (as before) · 19:3 F the second of Sivan (sinai_days) · 19:12 F the third · 19:14 F the fourth · 19:16
             F the giving day (the seventh under r_yose).
  The bound for Exodus 1-2:22's undated acts: [Jacob's deathbed, born:moses]; for 2:23-6:30: [the ark, the speaking];
  the plagues walk by their own stamps; 12:37-15:21 sit between the exodus day and Shur; 16:2-16:12 between 16:1 and
  16:13; 17-18 between 16:13 and 19:1.

### 4h. The checkpoints (the sequence runner; declared by the text or the shelf, computed by the engine)
  CS0 the ark's day = born:moses + 3 months vs Sotah 12b:16-17's sixth of Sivan — MATCH expected only if the Calendar's
      three months from the seventh of Adar land on the sixth (Adar 29 + Nisan 30 + Iyar 29 = 88 days → the sixth;
      the Calendar's month key keeps the day of month → the seventh): DIVERGE expected by one day under add(3,
      'month'); the 88-day reading printed beside it.
  CS1 the exodus day's weekday by the creation count vs Shabbat 87b:2 (Thursday) — DIVERGE expected (computed at the
      design from the standing DAYS: day 894328 % 7 = 1, the second day of the week; the modeled intercalations over
      two thousand four hundred years are not the tradition's — OPEN-2/OPEN-4).
  CS2 the spacing 15 Nisan → 15 Iyar → 1 Sivan = +2, +1 weekdays (Nisan full, Iyar deficient — Shabbat 87b:3-4, Rabbi
      Yose's arm; the Mekhilta Vayassa ch.1 row 1) — MATCH expected (the modeled alternation is the shelf's own).
  CS3 the giving day under r_yose = the seventh of Sivan = the tape's standing ascent marker (Taanit 28b) — MATCH.
  CS4 the manna's first morning = the sixteenth of Iyar; the shelf's Sunday (Shabbat 87b:5, Rav Pappa) vs the engine's
      weekday — DIVERGE expected (the anchor).
  CS5 C3c's bound PARSED: 133 + 137 + 80 from 6:18, 6:20, 7:7 by ink_numbers, no literal — MATCH as before.
  CS6 the judges: 600,000 (12:37) over the four denominations (18:21) = 78,600 (Sanhedrin 18a:3) — MATCH.
  CS7 the trials on the ledger by Exodus 19 = 6 of Arakhin 15a-b's ten (the accounting above) — MATCH.
  CS8 the plagues on Egypt's ledger = 10 (Mishnah Avot 5:4), 4 closed by a narrated removal — MATCH.
  CS9 Eduyot 2:10's twelve months as a BOUND on the plague stretch (the speaking to the exodus) — within: MATCH.
  The sojourn fork's worlds carry the same (the checkpoints run on every world).

### 4i. The scene (the runner's own bare world; the rows in the text's order; the tuple predicted by a hand-model
written FIRST — scratchpad o8_s1_predict.py — and printed before the runner is typed)
The slots (subject, effect) in order: israel enslaved (2), embittered (1); the-midwives decree_issued (1),
feared_god (1), houses_made (1); egypt_people decree_issued (1); jochebed wife_taken (1); moses hidden_three_months
(1), circumcision_due (1 — fired: the timer from `born`, the pre-Sinai daemon registered on the scene's world too),
drawn_out (1), name_given (1), sought_to_kill (1, closed 0 open); gershom name_given (1), circumcision_due (1, open
after 4:25? — by the registry the lodging's son is its own singleton: gershom's stays OPEN 1); zipporah wife_taken
(1); israel cry_heard (1), covenant_remembered (1); the-place holy_ground (1); moses sent_to_pharaoh (1, closed at
12:51); god name_declared (1); moses signs_in_hand (1), mark_of_anger (1); aaron mouth_appointed (1); pharaoh
firstborn_death_decreed (1, closed at 12:29), release_demanded (1, closed at 12:31), heart_hardened (15),
barred_from_the_face (0 — the block is on moses: moses barred_from_the_face 1); the-staff staff_of_god (1); israel
believed (2), straw_withheld (1), not_heard (1), to_be_* (5; open at the end: 1 — the land); the-officers beaten (1);
moses now_you_will_see (1, open 1); egypt_people plague_struck (10; open 6), plague_removed (4), egypt_emptied (1),
egypt_drowned (1); israel sent_out (1), brought_out (1), encamped_at (9), pillar_leads (1), pursued_by_egypt (1,
closed), saved (1), song_sung (1), statute_set_at_marah (1), healer_promised (1), tested_the_lord (6),
manna_provided (1), water_from_the_rock (1), prevailed (1), courts_established (1), hard_cases_to_moses (1),
treasured_people (1), undertook_to_do (1), sanctified_for_the_third_day (1 — fired), mountain_barred (1, open);
moses bones_carried (1); the-sea sea_split (1); the-waters waters_sweetened (1); the-jar omer_kept (1); amalek
amalek_weakened (1), amalek_to_be_blotted (1, open); jethro offered_burnt_and_sacrifices (1); the-mountain
descended_on_the_mountain (1); the timers set and fired; the clock. The literal is typed from the predictor's print.

### 4j. The answer sheet and the shelf the cells read
Mishnah rows verified by their own tokens: Pesachim 10:4 (מתחיל בגנות — begins with disgrace), 10:5 (פסח מצה ומרור;
מעבדות לחרות); Avot 5:4 (עשר מכות — ten plagues), 5:6 (והמן והמטה — the manna and the staff); Sotah 1:9 (מרים המתינה;
משה זכה בעצמות יוסף); Sotah 5:4 (כקורין את ההלל); Rosh Hashanah 3:8 (ידיו של משה); Eduyot 2:10 (משפט המצריים);
Sanhedrin 1:6 (the courts' sizes — the denominations' institution by name); Megillah 4:10 is Genesis's (S4).
Bavli and Mekhilta rows (all read at this sitting by script, cited above): Sotah 11a:6, 11a:15, 11b:1, 11b:11-13,
11b:22, 12a:8, 12a:10-18, 12b:10, 12b:13, 12b:15-17, 13a:13-17, 13b:5; Nedarim 31b:13-14, 32a:1-3; Sanhedrin 111a:10,
91a:10-12, 18a:3, 56b:15-16, 67b:15; Shabbat 86b:5, 87a:1-3, 87a:6, 87b:1-5, 88a:3, 88a:5; Zevachim 116a:19-21, 102a:6-8,
102a:10; Arakhin 15a:14-15b:2; Kiddushin 38a:3-7; Sotah 30b:11-13; Berakhot 9a:29-9b:2, 9b:6; Megillah 9a:16; Pesachim
116a:11-12, 116b:1-3; Mekhilta Pischa ch.35 row 1, ch.40 row 1, Pischa-b ch.17 row 1, ch.19 rows 1-9, Beshalach ch.16
row 1, ch.31 row 2, Shirata ch.1 rows 1-2, ch.25 row 2, Vayassa ch.1 row 1, ch.4 row 2, ch.35 row 1, Yitro ch.1 row
1, Bachodesh ch.1 rows 1-3, ch.8 row 1, ch.11 row 1, ch.16 row 1.

### 4k. The edits to standing files (each with its check)
- cold_run_family.py: `married` gains the seat check (Gen 24 → wife_taken + comforted; else nothing) — its scene and
  tuple unchanged; the guard re-measured.
- cold_run_erection.py: `people_answered` gains the seat check (Exod 24 only) — its scene and tuple unchanged.
- cold_run_sequence.py: the import and DAEMON_ORDER (+ law_exodus_story after law_family); c3's bound parsed from the
  ink (CS5); the CS checkpoints; PARAMS + sinai_days, jethro_timing (the settings printed); the literals CENSUS, DAYS,
  VERDICTS re-predicted by the stitcher, RUN typed from the first run after reading; the tape section regenerated.
- world_engine.py: Clock.weekday (day % 7 under the creation epoch — day 0 the first day, 6 the Sabbath; None
  otherwise) — a fire-probe written first (clock_probes.py +1).
- scratchpad seq_record.py / seq_stitch.py: SPAN_ORDER and CLOCK_DAY_RUNNERS gain 'exodus_story'; the MK table gains
  4g's rows; the 7:7 row changed from P to F; the registry's tape lines appended for the new kinds.
- event_vocabulary.yaml (+~65 types; 3 amended), effect_vocabulary.yaml (+~60), daemon_dispositions.yaml,
  dependency_dispositions.yaml (the span, the edges, the pointers), calendar_parameters.yaml (+5 rows),
  entity_registry.yaml (+15 members, +16 entities), COMPILE_DEBT (O8 S1 DONE), DAEMON_INDEX / DEPENDENCY_INDEX
  regenerated, THE_STEPS (conventions 13-18 after S1 proves them), THE_BRIEFING, the state doc, memory.

### 4l. The order of work (the wrap's rhythm)
1. This declaration. 2. The effects appended by script (each ink claim verified). 3. The types appended by script (the
witnesses cut and verified; the lint 0). 4. The calendar rows and the registry members. 5. The daemon declared; the
gate run → FAIL (no def, no functions). 6. The span on a stub runner; the census --emit; the dispositions filed; the
gate run. 7. The hand-model prediction printed. 8. The runner typed (fix_percent first); run; misses read. 9. The two
seat checks; those runners rerun. 10. The engine's weekday + its probe; the probe sets rerun. 11. The recorder and the
stitcher (the MK rows); the sequence runner's literals; the sequence run; the CS verdicts read. 12. The gates, the
sweep, the corpus regression. 13. The records; the compaction point.

### 4m. OPEN at this sitting
OPEN-9 Jethro's placement (Zevachim 116a:20): the after-arm would move 18's acts past the covenant — recorded as a
setting, not run as a world (a placement with no day). The son at the lodging UNCERTAIN (4e). The tradition's "five
times Pharaoh hardened his own heart" not on the local shelf under the searched forms. The plague stretch's placement
MODELED (convention 18). The weekday anchor DIVERGE (CS1, CS4) filed under the calendar's modeled grounds. Moses'
flight age (the forty of Sifrei Devarim 357 — not found on the local Sifrei under the searched forms): 2:11-2:22 stay
inside the open bound. The trials' count and Amalek's blotting owed forward to Numbers and the Prophets' RUN.

### 4n. AS RUN (2026-09-08; the account: REPORT_NARRATIVE_GAPS.md)
The order held: the effects (251 → 311; two typed claims refuted by the scan and corrected before the literal), the
types (271 → 341; the lint 0 on 797 witness runs), the calendar rows and the registry members, the daemon declared and
the gate run to fail (the missing def), the span on a stub and the census run with --emit (ten edges, twenty pointers,
all dispositioned; the four CALLs failing until the code made them live), the hand-model printed (77 slots), the runner
typed: 111/113 FIRST RUN — the naming scanner's verb set (the literal stood) and the model's open count (cry_heard's
HEAVEN op; 16 → 17 corrected beside the recorded miss); 113/113 second run. The recorder's and the stitcher's close
wrappers extended for the engine's close(value=); the parser's table extended with the construct numerals (7:25, 10:22,
15:22 — and 34:28's "the ten words" read into a standing row). The tape 260 events / 88 markers / 23 closes; the sequence
runner 7/7 with nine new checkpoints exactly as 4h expected (CS0, CS1, CS4 DIVERGE; CS2, CS3, CS6-CS9 MATCH; C3c parsed).
The two seat checks held: the double writes on the tape are still the two mornings of 36:3 alone. The gaps line: the
four Genesis stretches and the ink's own silences inside Exodus 2-7. The engine: Clock.weekday and close(value=), probes
18/18. Conventions 13-18 entered in THE_STEPS. The sweep and the corpus regression: the report's closing section.

## 5. S2-S4 (each sitting declares its own section here before its code)
S2 FROM EDEN TO HAGAR: the garden's command and breach (the pre-Sinai engine holds 2:16-17 and 2:24 already — its
span; the story's acts around them), Cain's sentence (the first court on the ledger: Sanhedrin's rows), the flood's
inside (the 120 years of 6:3 a heaven timer; 7:4's seven days and forty days; 7:24/8:3's 150 — the markers exist;
the ark's spec a build_spec; Sanhedrin 108a-b the generation of the flood — Mishnah Sanhedrin 10:3's verdict table
on the flood generation, the dispersion, Sodom: no share in the world to come — the answer sheet), the vineyard's
curse, the nations' ledger, Babel's dispersion (10:3's second row), the call (12:1-3's promises as heaven entries),
the descent to Egypt (the endangerment — Bava Kamma 8:7's Abimelech row is S3's), the separation, the war and Lot's
rescue (Nedarim 32a:17 the 318 = Eliezer), the pieces (15:13-14's three promises OPEN — closed by S1's Exodus acts;
Megillah 9a:16 the elders' 430), Hagar (16:16's marker exists).
S3 FROM MAMRE TO THE HEAP: the plea for Sodom (the count's descent), Sodom's overthrow (10:3's third row), Gerar
(Bava Kamma 8:7 — "he must pray for him"; the prayer for Abimelech), the binding (Avot 5:3's ten trials of Abraham —
the answer sheet's count over S2-S3), Abraham's end, the twins' birthright sale (Bekhorot's firstborn rows), Isaac at
Gerar and the wells, the blessing's deception, Bethel's vow (a debit on Jacob closed at 35:7 — S4), the wage of seven
years (the timers), the switched bride, the twelve names, the speckled wage, the flight and the pursuit (the heap's
oath).
S4 FROM THE RETURN TO GOSHEN: Esau met, the gate's deceit (Megillah 4:10 Reuben's act — read and not translated),
Bethel's vow paid, the three deaths (35:28's marker exists), Edom's kings' ledger, the dreamer sold (Sotah 13b:10),
Potiphar's house, the dreams, the rise (41:46's marker exists), the two descents and the cup, the seventy, Goshen and
the fifth (47:24-26 — a land statute on Egypt's ledger), Joseph's oath (50:25 — closed by S1's 13:19) and death.

## 6. S2 — GENESIS 2:4-16:16 FROM EDEN TO HAGAR: THE DECLARATION (2026-09-08, the first sitting after compaction #98;
the owner: "Continue" — read as the word; #98's rereads done first)

### 6a. The span, the runner, the daemon
- Span `primeval` (dependency_dispositions.yaml): [[Gen,2,4,15],[Gen,2,18,23],[Gen,2,25,25],[Gen,3,1,24],[Gen,4,1,26],
  [Gen,5,1,32],[Gen,6,1,22],[Gen,7,1,24],[Gen,8,1,22],[Gen,9,18,29],[Gen,10,1,32],[Gen,11,1,32],[Gen,12,1,20],
  [Gen,13,1,18],[Gen,14,1,24],[Gen,15,1,21],[Gen,16,1,16]] — the pre-Sinai engine's verses (2:16-17 the first rule,
  2:24 the unions' root, 9:1-17 the Noahide charter and the bow) EXCLUDED: their law is that engine's, and the story's
  scene submits the ACTS around them (the breach of 3:6 is an act against 2:16-17's rule, fetched by call).
- Runner cold_run_primeval.py (no module of that name exists — the collision guard, measured); daemon `law_primeval`,
  `wraps: primeval`; every cell function WRAPPED by it. The scene on a BARE world with w.laws = [law_primeval] alone:
  no birth of this stretch is under the covenant of Gen 17 (the eighth-day timer is the pre-Sinai daemon's run on
  `born`, from 17:12 forward), so the ledger births here are the ink's own verbs `begot` / `bore` (6b) and the
  pre-Sinai daemon is not registered on the scene (on the tape it watches and does not fire on them).
- The census run with --emit on the stub before a cell; the expected edges: CALL where the ink names an institution
  compiled elsewhere — the burnt offering at 8:20 (the offering engine), the minchah of 4:3 and the firstlings and
  their fat of 4:4 (the meal-offering engine; the firstling's law seat Lev 27:26 in the temurah engine; the fat
  inventory of the offering engine), the clean beasts of 7:2 and 8:20 (the species classifier of the Shemini
  engine), the tithe of 14:20 (the temurah engine's tithe cells), the priest of 14:18 (the priesthood engine), the
  marriage formula's token 'as a wife' at 4:19, 11:29, 16:3 (the family engine), the heir of 15:3-4 (the family
  engine's inheritance cells), the walking of 13:17 as an acquisition (the family engine's three modes — a TRANSFER
  taught by Bava Batra 100a:7), the covenant of 6:18 and 15:18 (the pre-Sinai engine's covenant cells), the first
  rule cited back at 3:11 and 3:17 ('which I commanded you' — a RUN_CITATION into the pre-Sinai engine's 2:16-17),
  Cain's bloods against 9:6's bloodshed cells (the pre-Sinai engine), 'childless' at 15:2 (the sanctions engine's
  word at Lev 20:20-21); PARAMETER for 12:17's plagues (the affliction engine's datum — Bereshit Rabbah 41:2 reads
  ra'atan); FALSE for the homographs — the servant of 9:25-27 (the slave engines), 'shall not cease' at 8:22 (the
  Sabbath root), the stranger of 15:13 (the holiness engine's sojourner), the sister of 12:13 and 12:19 (the
  sanctions engine's sister), the 'king' tokens of Gen 14 (Molech's consonants). Each dispositioned before a cell.

### 6b. The types (event_vocabulary.yaml; NEW unless marked; witnesses cut from the verses' consonants by script and
verified by the lint against the Tanakh DB; the form by the register test — an act on a verse with the narrative
verb, the 'and he did' form, within the chapter window; a speech at a narrated speaking)
Acts: formed_from_dust (2:7) · placed_in_the_garden (2:8, 2:15) · named [REUSE, +2:20 'called names', 2:23, 3:20,
4:17, 4:25, 4:26, 5:2, 5:3, 5:29, 11:9, 16:13, 16:14, 16:15 — the naming formula's own lemmas at every seat; link
reference] · woman_built (2:21-22) · ate_of_the_tree (3:6 — the four verbs took, ate, gave, ate) · eyes_opened (3:7)
· hid_from_the_voice (3:8) · clothed_in_skins (3:21) · expelled (3:23-24) · bore (4:1 Cain, 4:2 Abel, 4:17 Enoch,
4:20 Jabal, 4:22 Tubal-cain, 4:25 Seth, 16:15 Ishmael — the mother's verb 'and she bore'; fields child) · begot (5:3
Seth ... 5:32 the three, 10:8 Nimrod, 10:25 Peleg and Joktan, 11:10 Arpachshad ... 11:26 the three — the father's
verb 'and he begot'; fields children) · first_offerings_brought (4:3 Cain's minchah, 4:4 Abel's firstlings; fields
what) · anger_burned (4:5) · killed (4:8; fields victim) · went_out_from_the_presence (4:16) · city_built (4:17) ·
married [REUSE, +4:19 two wives, 6:2 the sons of God, 11:29 Abram and Nahor, 16:3 Hagar 'as a wife'; link
reference] · profanation_begun (4:26 'then it was begun to call on the name') · enoch_taken (5:24) · multiplied (6:1)
· wickedness_seen (6:5, 6:12) · regretted (6:6) · favor_found (6:8) · ark_made (6:22) · entered_the_ark (7:7, 7:13,
7:15-16) · flood_came (7:11, 7:17-18) · all_flesh_expired (7:21-23) · waters_prevailed (7:24) · remembered (8:1) ·
waters_receded (8:1-3) · ark_rested (8:4) · bird_sent (8:7 the raven, 8:8, 8:10, 8:12 the dove; fields bird,
sending) · cover_removed (8:13) · exited_the_ark (8:18-19) · altar_erected (8:20 Noah, 12:7 Shechem, 12:8 Bethel,
13:18 Hebron; fields at — AS RUN: the name altar_built was the ordinances engine's case kind) · olah_offered (8:20) · savor_smelled (8:21) · vineyard_planted (9:20) ·
drunk_and_uncovered (9:21) · nakedness_seen_and_told (9:22) · covered_backward (9:23) · awoke_and_knew (9:24) ·
kingdom_begun (10:10) · cities_built (10:11-12) · journeyed [REUSE, +11:2 Shinar, 11:31 Haran, 12:5 Canaan, 12:6
Shechem, 12:8 Bethel, 12:9 the Negev, 12:10 Egypt, 13:1-3 back to Bethel, 13:11-12 Lot to the plain, 13:18
Hebron; the itinerary's own verbs; link reference] · lord_descended [REUSE, +11:5 'came down to see'; link
reference — the descent verb; Bereshit Rabbah 38:9 one of the ten descents] · confounded_and_scattered (11:7-9) ·
died [REUSE, +11:28 Haran 'died in the presence of his father'; link reference — the death verb] · barren (11:30) ·
went (12:4-5 'and Abram went as the LORD had spoken') · appeared (12:7) · called_on_the_name (12:8, 13:4) ·
famine_came (12:10) · woman_taken (12:15) · dealt_well (12:16) · plagued (12:17) · sent_away (12:20) · strife_arose
(13:7) · lot_chose (13:10-11) · separated (13:11) · sodom_wicked (13:13 — the narrator's verdict clause, the Mishnah's
own proof-text; the form act by the register test, said so) · war_waged (14:1-2, 14:5-11) · lot_taken (14:12) ·
escapee_told (14:13) · mustered_and_pursued (14:14-15) · brought_back (14:16) · bread_and_wine_brought (14:18) ·
tithe_given (14:20) · believed [REUSE, +15:6 'and he believed in the LORD'; link reference — the faith verb;
Mekhilta Shirata ch.1 row 1 joins the seats itself] · pieces_cut (15:10-11) · deep_sleep_fell (2:21, 15:12 — the
same noun, Bereshit Rabbah 17:5 and 44:17 the same three kinds; fields kind) · passed_between_the_pieces (15:17) ·
covenant_cut_with_abram (15:18) · conceived_and_despised (16:4) · afflicted (16:6) · fled [REUSE, +16:6 Hagar; link
reference — the flight verb; the Exodus daemon seat-checked to Exod 2] · angel_found (16:7).
Speech: serpent_spoke (3:1, 3:4-5) · interrogated (3:9-13) · sentenced (3:14-15 the serpent, 3:16 the woman, 3:17-19
the man, 4:11-12 Cain; fields sentence) · counsel_given (4:6-7 the first IF) · mark_promised (4:15) · lamech_sang
(4:23-24) · decree_of_the_reprieve (6:3) · wipe_resolved (6:7) · end_decreed (6:13) · ark_commanded (6:14-21) ·
boarding_commanded (7:1-4) · exit_commanded (8:15-17) · never_again_resolved (8:21-22) · cursed_canaan (9:25) ·
blessed_shem_and_japheth (9:26-27) · tower_proposed (11:3-4) · call_given (12:1-3) · land_promised (12:7, 13:14-17,
15:7; fields seat) · sister_asked (12:11-13) · pharaoh_protested (12:18-19) · separation_proposed (13:8-9) ·
kings_demand_refused (14:21-24) · word_came (15:1) · heir_questioned (15:2-3) · heir_declared (15:4) · stars_shown
(15:5) · sign_asked (15:8) · pieces_commanded (15:9) · decree_of_the_sojourn (15:13-16) · hagar_offered (16:2) ·
wrong_claimed (16:5) · maid_released (16:6) · return_commanded (16:9) · seed_promised_to_hagar (16:10) ·
ishmael_announced (16:11-12).
The `tape:` line of every reused kind declares the two layers (the Exodus daemon's named, journeyed, fled, believed
and lord_descended branches, and the family daemon's died, GAIN the seat check their span implies — convention 14);
`link: reference` with the shared lemma named.

### 6c. The effects (effect_vocabulary.yaml; NEW unless marked; each ink claim verified by script before the append;
the ledger op in brackets)
- living_soul [status, adam] 2:7 וַיְהִי הָאָדָם לְנֶפֶשׁ חַיָּה (and the man became a living soul) — Bereshit Rabbah
  14:9 (the five soul-names — the frozen unit's read); to_work_and_keep [status, adam] 2:15 לְעָבְדָהּ וּלְשָׁמְרָהּ (to work it and to keep it) —
  Bereshit Rabbah 16:5 (R. Yehuda: He elevated him; R. Nechemya: He persuaded him — the taking verb).
- helper_made [status, adam] 2:22 — Bereshit Rabbah 17:2-3 ('if he merits, a help; if not, against him'); Mishnah
  Yevamot 6:6 (Beit Hillel's male-and-female from 5:2 — the answer-sheet row on the couple).
- name_given [REUSE, status] at the twelve seats above; deep_sleep_fell [status] 2:21, 15:12 — Bereshit Rabbah 17:5
  and 44:17 (the three deep sleeps: of sleep, of prophecy, of stupor — the value the kind at each seat).
- breached_the_first_rule [status, eve; adam] 3:6 — the rule fetched from the pre-Sinai engine (the first LET-NOT,
  2:17); Bereshit Rabbah 19:5 (three things said of that tree); Berakhot 40a:14 and Sanhedrin 70a:21-22 (the tree's
  identity: the vine — R. Meir; wheat — R. Yehuda; the fig — R. Nechemya: the value's arms); eyes_opened [status]
  3:7 — Bereshit Rabbah 19:6; girdles_made [status] 3:7.
- deceived [status, eve] 3:13 הַנָּחָשׁ הִשִּׁיאַנִי (the serpent deceived me) — the woman's own admission.
- serpent_cursed [status, the serpent] 3:14 — Bereshit Rabbah 20:4-5 (judged by a full Sanhedrin — the seventy-one
  mentions of the Name to this point; the angels cut off its hands and feet); enmity_set [status, the serpent, cp eve]
  3:15; pain_multiplied [status, eve] 3:16 — Bereshit Rabbah 20:6; ruled_by_the_husband [status, eve] 3:16 — 20:7
  (the four desires); ground_cursed [status, the ground] 3:17 — 20:9 (livelihood harder than birth); sweat_bread
  [status, adam] 3:19; return_to_dust [heaven, adam] 3:19 — OPEN on the tape (the death is a proleptic marker, not
  an event); Bereshit Rabbah 19:8 ('in the day you eat': one of My days, a thousand years — he lived 930 and left 70
  to his sons): the checkpoint CG9.
- clothed_in_skins [status, adam and eve] 3:21 — Sotah 14a:4-6 (walk after His attributes: He clothes the naked;
  the Torah begins and ends with kindness); Bereshit Rabbah 20:12 (R. Meir's Torah read 'garments of light').
- expelled [status, adam and eve] 3:23-24 — Bereshit Rabbah 21:7-8 (sent from Eden in this world, and in the world
  to come? — R. Yehuda and R. Nechemya; driven out like a priest's daughter divorced who cannot return — R. Yochanan;
  like an Israelite's daughter who can — Reish Lakish); way_guarded [block, the garden] 3:24 — the cherubim and the
  flaming sword.
- begotten [status, the child, cp the parent] every `bore` / `begot` — the value the parent; Mishnah Avot 5:2's ten
  generations counted on the tape's own life eras (CG0).
- regarded [heaven, abel] 4:4 וַיִּשַׁע יְהוָה אֶל הֶבֶל וְאֶל מִנְחָתוֹ (and the LORD regarded Abel and his offering);
  not_regarded [status, cain] 4:5 — Bereshit Rabbah 22:5 (from the refuse — Cain; the firstlings and their fat — Abel;
  R. Elazar: the first minchah), 22:4 (Abel in the world no more than fifty days — the two arms on 'at the end of
  days': from Sukkot to Chanukah, from Passover to Shavuot); the minchah engine and the firstling's seat by call.
- sin_at_the_door [status, cain] 4:7 — Kiddushin 30b:5 ('if you wish, you rule over it'); Bereshit Rabbah 22:6.
- slain [destroy, abel, cp cain] 4:8 — Sanhedrin 37b:10 (wounds upon wounds: he did not know where the soul goes
  out); bloods_cry [heaven, cain] 4:10 קוֹל דְּמֵי אָחִיךָ צֹעֲקִים (the voice of your brother's bloods cries) — Mishnah
  Sanhedrin 4:5 (not 'blood' but 'bloods': his blood and the blood of his descendants; whoever destroys one soul
  destroys a whole world); Sanhedrin 37b:11 (the earth's mouth opened for Abel's blood and never again) — OPEN.
- cursed_from_the_ground [status, cain] 4:11; fugitive_and_wanderer [status, cain] 4:12 — Sanhedrin 37b:12 (exile
  atones half: 'a fugitive and a wanderer', and at the end 'he dwelt in the land of Nod'); Bereshit Rabbah 22:11
  ('my iniquity is greater than my father's — he transgressed a light command and was banished'); mark_set [status,
  cain] 4:15 — Bereshit Rabbah 22:12 (a dog / a horn / leprosy — the arms); sevenfold_vengeance [heaven, cain, cp
  HEAVEN] 4:15 — OPEN; 4:24's seventy-sevenfold the quote-diff (Lamech).
- settled_in_nod [status, cain] 4:16 — Bereshit Rabbah 21:9, 22:13 (the east receives — Adam, Cain, the manslayer:
  the refuge's direction).
- city_built [status, the city of Enoch, cp cain] 4:17 — Bereshit Rabbah 23:1 (their inward thought: their houses
  forever — they called lands by their names); wife_taken [REUSE, status] 4:19 (two wives — Bereshit Rabbah 23:2:
  one for offspring, one for pleasure), 6:2 ('from all they chose' — 26:5: R. Shimon ben Yochai calls them the sons
  of judges), 11:29 (Sarai; Milcah — Megillah 14a:13 Iscah is Sarah: the registry holds Iscah UNCERTAIN), 16:3
  ('as a wife' — Bereshit Rabbah 45:3: as a wife, not a concubine).
- seventy_sevenfold_claimed [status, lamech] 4:23-24 — Bereshit Rabbah 23:4 (his wives refused him: tomorrow the
  flood comes; 'I killed a man for my wound').
- idolatry_begun [status, the generation of Enosh] 4:26 — Bereshit Rabbah 23:7 (a language of rebellion at three
  places: 'then it was begun', 6:1 'when man began', 10:8 'he began to be a mighty one'); the frozen unit's export
  (the agentless 'it was begun' — the fork the unit recorded).
- taken_by_god [status, enoch] 5:24 — Bereshit Rabbah 25:1 (Enoch a hypocrite: taken while righteous — R. Aivu).
- comfort_named [status, noah] 5:29 — Bereshit Rabbah 25:2 (R. Yochanan: the name is not the exposition — Nachman
  or Yanach); 25:3 (the ten famines: Adam's, Lamech's, Abraham's ... — the curse of the ground quoted in the name).
- multiplied_on_the_earth [status, humankind] 6:1 — Bereshit Rabbah 26:4.
- reprieve_of_a_hundred_and_twenty [timer, the generation of the flood] 6:3 וְהָיוּ יָמָיו מֵאָה וְעֶשְׂרִים שָׁנָה (and his days shall be a
  hundred and twenty years) — the due = the speaking + 120 years; on the tape the speaking is RETROGRADE-dated at
  the flood − 120 (6g), so the timer fires at the flood's own marker (CG2); Bereshit Rabbah 30:7 (all hundred and
  twenty years Noah planted cedars and cut them — 'the Master of the world brings a flood'); Onkelos 6:3 (the frozen
  unit's read: אַרְכָא יְהִיבַת לְהוֹן (an extension is given them) — if they repent); 26:6 (the other arm: 'My spirit shall
  not judge' — the row gen6_3_reading, the lifespan reading UNEXERCISED).
- wickedness_great [status, humankind] 6:5 — Sanhedrin 108a:10 (with 'great' they sinned, with 'great' they were
  judged — 'the great deep'); regretted_making_man [status, god] 6:6 — Sanhedrin 108a:15-16 (Rav Dimi: 'well did I
  do that I prepared graves for them' / 'not well'); Bereshit Rabbah 27:4.
- to_be_wiped [heaven, the generation of the flood] 6:7 אֶמְחֶה אֶת הָאָדָם (I will wipe out man) — closed at 7:23 by
  the narrated wiping; no_share_in_the_world_to_come [heaven, the generation of the flood] 7:23 — Mishnah Sanhedrin
  10:3 (three rows of this stretch: the flood generation — 'He wiped' this world, 'they were wiped' the world to
  come, R. Akiva; R. Yehuda ben Beteira: neither live nor are judged, from 6:3's 'shall not judge'; the dispersion
  generation from 11:8-9's two scatterings; the men of Sodom from 13:13's 'wicked' and 'sinners'); Sanhedrin
  107b:18-108a:5, 109a:4-9 — the three entries OPEN forever (CG7).
- found_favor [status, noah] 6:8 — Sanhedrin 108a:14 (even on Noah the decree was sealed, but he found favor);
  Bereshit Rabbah 29:1-5 (in the merit of his descendants).
- earth_corrupted [status, the earth] 6:11-12 — Sanhedrin 108a:11 (they mated kind with kind); sealed_for_violence
  [status, the generation of the flood] 6:13 — Sanhedrin 108a:12 (R. Yochanan: their decree was sealed only when they
  stretched their hands to robbery); Bereshit Rabbah 31:5 (violence less than a perutah, robbery a perutah).
- ark_owed [debit, noah, cp HEAVEN] 6:14 — closed 6:22; ark_spec [status, the ark] 6:14-16 (300 by 50 by 30 cubits;
  the light; the three decks — Sanhedrin 108b:8-11: gopher, the window or the gem, the lower for dung, the middle
  for beasts, the upper for man); covenant_promised [heaven, noah] 6:18 וַהֲקִמֹתִי אֶת בְּרִיתִי אִתָּךְ (and I will
  establish My covenant with you) — closed at 9:11 by the pre-Sinai engine's act (the close line the scene issues at
  that verse; the covenant word's first token — the unit's export); ark_built [status, the ark] 6:22.
- boarding_owed [debit, noah] 7:1 — closed 7:7; seven_days_reprieve [timer, the generation of the flood] 7:4 —
  Sanhedrin 108b:4-5 (Rav: the seven days of mourning for Methuselah; the sun reversed; a taste of the world to
  come); Bereshit Rabbah 32:5 (the forty days: they transgressed the Torah given in forty days; the embryo's forty),
  32:7; fires at the flood (CG3).
- in_the_ark [status, noah and his sons] 7:7; ark_intercourse_barred [block, noah and his sons] 7:7 — Sanhedrin
  108b:14-15 (from 6:18's order 'you and your sons, your wife and your sons' wives': forbidden in the ark; three
  cohabited and were smitten — the dog, the raven, Ham); Bereshit Rabbah 34:7; shut_in [status, noah] 7:16.
- fountains_split [status, the earth] 7:11 — Sanhedrin 108a:9 (judged by water like the eyeball with which they
  sinned); wiped_out [destroy, the generation of the flood] 7:23; only_noah_remained [status, noah] 7:23 — Sanhedrin
  108a:19-21 (if man sinned, what did the beast sin? — the wedding canopy; 'all on the dry land died, not the fish');
  waters_prevailed_a_hundred_and_fifty [status, the earth] 7:24 (the marker C1).
- remembered_by_god [status, noah] 8:1 — Bereshit Rabbah 33:1-3 (and every living thing: His mercies on all His
  works); waters_receding [status, the earth] 8:1-3 — Sanhedrin 108b:3 (Rav Chisda: in boiling water they sinned, in
  boiling water they were judged — 'subsided' as the king's wrath subsided); Bereshit Rabbah 33:4 (three fountains
  stayed open); rested_on_ararat [status, the ark] 8:4.
- raven_sent [status, the raven] 8:7 — Sanhedrin 108b:12-13 (the raven's retort: your Master hates me — seven of the
  clean, two of the unclean; 'wicked one, what is permitted me is forbidden me'); dove_returned [status, the dove]
  8:9, 8:11, 8:12 (the value: returned / the olive leaf / did not return) — Sanhedrin 108b:16-17 (the dwelling of
  clean birds with the righteous; 'let my food be bitter as the olive from Your hand'); the sendings' days (CG4).
- ground_seen_dry [status, noah] 8:13; exit_owed [debit, noah] 8:16 — closed 8:18; intercourse_permitted [status,
  noah and his sons] 8:16 — Sanhedrin 108b:14 ('you and your wife'); out_of_the_ark [status] 8:18.
- altar_built [status, the altar, cp the builder] 8:20, 12:7, 12:8, 13:18 — Bereshit Rabbah 34:9 (Noah on the great
  altar of Jerusalem — R. Elazar ben Yaakov), 39:16 (Abram's three altars: the tidings of the land, its acquisition,
  that his sons not fall at Ai); olah_offered [status, noah] 8:20 — the offering engine's burnt offering by call;
  the clean beasts by the species classifier (Sanhedrin 108b:6-7: 'a man and his wife' — those never mated across
  kinds; how did he know — the ark accepted them, or those that came of themselves); savor_smelled [status, god] 8:21.
- ground_not_cursed_again [status, the ground] 8:21 — Bereshit Rabbah 34:10 (the righteous rule their heart);
  seasons_pledged [status, the earth] 8:22 — 34:11 (as long as heaven and earth stand).
- vineyard_planted [status, noah] 9:20 — Bereshit Rabbah 36:3 (he was profaned — chullin); Sanhedrin 70a:21 (Rav
  Chisda: could you not learn from the first man, whom wine alone undid — as the one who says his tree was a vine);
  drunk [status, noah] 9:21 — 36:4 (the same day he planted, drank, was disgraced); uncovered [status, noah] 9:21;
  saw_and_told [status, ham] 9:22 — Sanhedrin 70a:18-20 (Rav and Shmuel: he castrated him / he lay with him — the
  value; 'therefore he cursed him by the fourth'); covered_the_father [status, shem and japheth] 9:23 — Bereshit
  Rabbah 36:6 (Shem began, Japheth joined: Shem merited the tallit, Japheth the burial).
- canaan_cursed [status, canaan] 9:25 עֶבֶד עֲבָדִים יִהְיֶה לְאֶחָיו (a slave of slaves he shall be to his brothers) —
  the slave word's first four tokens inside the curse (the unit's export); Sanhedrin 70a:19 (cursed by the fourth);
  Bereshit Rabbah 36:7 (Ham sinned and Canaan is cursed?!); shem_blessed [status, shem] 9:26; japheth_enlarged
  [heaven, japheth] 9:27 יַפְתְּ אֱלֹהִים לְיֶפֶת וְיִשְׁכֹּן בְּאָהֳלֵי שֵׁם (God enlarge Japheth, and he shall dwell in the tents of
  Shem) — Megillah 9b:4-5 (Rabban Shimon ben Gamliel: only Greek — 'the beauty of Japheth shall be in the tents of
  Shem'; Mishnah Megillah 1:8 the answer-sheet row); Bereshit Rabbah 36:8 (Cyrus; no Presence but in the tents of
  Shem) — OPEN (book-bound).
- kingdom_founded [status, nimrod] 10:10 — Chullin 89a:7 (I gave greatness to Nimrod and he said 'let us build');
  Eruvin 53a:7 (Amraphel is Nimrod — the furnace); Bereshit Rabbah 37:4 (Shinar: where the flood's dead were shaken
  out); cities_built [status, asshur] 10:11-12; peleg_named_for_the_division [status, peleg] 10:25 — Bereshit Rabbah
  37:7 (Eber a great prophet: named for the event); the dispersion's year not on the local shelf — Babel stays at
  the tape's counter (6g).
- encamped_at [REUSE, status] 11:2 (Shinar — Bereshit Rabbah 38:7: they removed themselves from the Ancient One),
  11:31 (Haran), 12:5, 12:6, 12:8, 12:9, 12:10, 13:1-3, 13:12 (Lot), 13:18 — the value the place.
- tower_undertaken [status, the builders] 11:3-4 — Sanhedrin 109a:4-6 (the three parties: to dwell, to serve
  idols, to make war — R. Yirmeya bar Elazar; R. Natan: all for idolatry, 'a name' here and 'the name of other gods'
  there); Bereshit Rabbah 38:6, 38:8 (who said to whom: Mitzrayim to Cush).
- descended_to_see [status, the city and tower] 11:5 — Bereshit Rabbah 38:9 (one of the ten descents written in the
  Torah — R. Shimon bar Chalafta: the same list the Mekhilta counts at Exod 19:11, S1's row).
- language_confounded [status, the builders] 11:7-9 — 38:10 (one of the things changed for King Ptolemy: 'let ME go
  down'); scattered [status, the builders] 11:8; building_ceased [status, the city and tower] 11:8 — Sanhedrin
  109a:7 (a third burned, a third swallowed, a third stands); no_share_in_the_world_to_come [the second entry, the
  generation of the dispersion] 11:8-9 — Mishnah Sanhedrin 10:3.
- died_before_his_father [status, haran] 11:28 — Bereshit Rabbah 38:13 (Terah the idol-maker; the furnace: 'if your
  God saves you...' — Haran burned); barren [status, sarai] 11:30 — 38:14, 45:1-2; Yevamot 64a:5 (the ten years of
  16:3 — dwelling abroad does not count).
- go_owed [debit, abram, cp HEAVEN] 12:1 — closed 12:4 'and Abram went as the LORD had spoken'; great_nation_promised
  [heaven, abram] 12:2 — OPEN (Deut 26:5 — book-bound); Bereshit Rabbah 39:11; blessing_promised [heaven, abram]
  12:2-3 (the ladder: I will bless you, make your name great, be a blessing; bless your blessers, curse your curser;
  all the families blessed in you — 39:12) — OPEN here (24:1 'blessed Abraham in all' is S3's close at the family
  engine's verse).
- land_promised [heaven, abram] 12:7 לְזַרְעֲךָ אֶתֵּן אֶת הָאָרֶץ הַזֹּאת (to your seed I will give this land), 13:15 ('to
  you and to your seed forever'), 15:7 ('to give you this land to inherit it') — three entries, all CLOSED at 15:18
  by the ink's own perfect: לְזַרְעֲךָ נָתַתִּי (to your seed I HAVE GIVEN) — the give-arc's receipt (the frozen unit's
  export); land_granted [status, the seed of Abraham] 15:18-21 (the value the ten nations — Bereshit Rabbah 44:23: ten
  named, seven given; the Kenite, Kenizzite and Kadmonite for the future).
- called_on_the_name [status, abram] 12:8, 13:4; famine [status, the land] 12:10 — Bereshit Rabbah 25:3, 40:3 (the
  ten famines — the third in Abraham's days); presented_as_sister [status, sarai] 12:13 — 40:4-5 (hidden in a chest at
  the customs); taken_to_pharaohs_house [body, sarai, cp paro] 12:15 — closed 12:20; enriched_for_her_sake [transfer,
  abram, cp paro] 12:16 — 40:6 (whatever is written of Abraham is written of his sons — the Egypt pattern);
  plague_struck [REUSE, heaven] 12:17 (the plague noun shared with Exod 11:1 — a REFERENCE by lemma; Bereshit Rabbah
  41:2: with ra'atan he was struck — the affliction engine's datum, PARAMETER) — OPEN (no removal narrated);
  sent_out [REUSE, transfer] 12:20 — the sending verb; a TRANSFER taught by Bereshit Rabbah 40:6 (the pattern:
  'and Pharaoh commanded men' here, 'commanded all his people' at Exod 1:22).
- very_rich [status, abram] 13:2 — Bereshit Rabbah 41:3 (Ps 105:37 — the pattern again); strife_between_herdsmen
  [status, the herdsmen] 13:7 — 41:5 (Abram's beasts muzzled, Lot's not); chose_the_plain [status, lot] 13:10-11 —
  41:7 (the whole verse a language of lewdness; 'journeyed east' — from the Ancient One); parted [status, abram; lot]
  13:11; no_share_in_the_world_to_come [the third entry, the men of Sodom] 13:13 — Mishnah Sanhedrin 10:3; Sanhedrin
  109a:8-9 (Rav Yehuda: wicked in their bodies, sinners with their money; the baraita reversed — the value).
- seed_as_dust [heaven, abram] 13:16 — OPEN; land_walk_commanded [debit, abram, cp HEAVEN] 13:17 — Bava Batra 100a:7
  (R. Eliezer: walking acquires — 'for to you I will give it'; the sages: out of affection, that it be easy for his
  sons to conquer) — OPEN (the walk is never narrated; the family engine's modes by call); Bereshit Rabbah 41:10.
- rebelled [status, the five kings] 14:4 (the ink's twelve, thirteen, fourteen — CG5); defeated [status, the five
  kings] 14:10-11; taken_captive [body, lot, cp the four kings] 14:12 — closed 14:16; called_the_hebrew [status,
  abram] 14:13 — Bereshit Rabbah 42:8 (from Eber / from beyond the river / the language; the escapee is Og);
  muster_of_three_hundred_and_eighteen [status, abram] 14:14 — Nedarim 32a:16-17 (Rav: he emptied them of Torah; Shmuel: of gold; R. Ami bar
  Abba: Eliezer alone — the sum of his letters is 318); night_divided [status, abram] 14:15 — Bereshit Rabbah 43:3
  (the night divided of itself, or its Maker divided it: half for Abraham, half for his sons in Egypt — Exod 12:29,
  S1's midnight); kings_smitten [status, the four kings] 14:15; goods_brought_back [transfer, the king of Sodom, cp
  abram] 14:16 — 43:4 (the men and women he returned, the children he did not).
- blessed_by_the_priest [status, abram, cp melchizedek] 14:19 — Nedarim 32b:6 (the priesthood was to go out from
  Shem; because he set Abraham's blessing before the Place's, it went to Abraham — the value); priesthood_removed
  [status, melchizedek] 14:19-20 — the same row; Bereshit Rabbah 43:6 (Salem is Jerusalem; the priest's office by
  call into the priesthood engine); bread_and_wine [status, abram] 14:18; tithe_given [transfer, abram, cp
  melchizedek] 14:20 וַיִּתֶּן לוֹ מַעֲשֵׂר מִכֹּל (and he gave him a tenth of all) — the tithe's institution by call
  (the temurah engine's Lev 27:30); Bereshit Rabbah 43:8.
- sworn_to_take_nothing [status, abram] 14:22-24 הֲרִמֹתִי יָדִי אֶל יְהוָה (I have lifted my hand to the LORD) —
  Bereshit Rabbah 43:9 (R. Yehuda: he made it terumah; R. Nechemya: a vow); Nedarim 32a:15 (R. Yochanan: punished
  for 'give me the persons' — he kept people from entering under the wings of the Presence); portion_reserved
  [status, the allies] 14:24.
- shield_promised [heaven, abram] 15:1 — Bereshit Rabbah 44:4 (the two fears: a righteous man among the slain; the
  reward consumed); childless [REUSE, heaven, abram] 15:2 עֲרִירִי (childless — Lev 20:20-21's own word at its narrative
  seat, a REFERENCE by lemma) — closed at 16:15 by the son born; heir_from_the_loins [heaven, abram] 15:4 — the
  inheritance institution by call (the family engine) — OPEN (Isaac, S3); seed_as_stars [heaven, abram] 15:5 —
  Nedarim 32a:9 (go out of your astrology: no constellation for Israel); Bereshit Rabbah 44:12.
- believed [REUSE, status] 15:6; reckoned_righteousness [status, abram] 15:6 — the Mekhilta Shirata ch.1 row 1 (S1's
  row: Abraham inherited this world and the world to come only in the merit of faith — 'and he believed in the LORD');
  the frozen unit's 'staged both ways' (who reckoned to whom) kept as the value's note.
- brought_out_of_ur [status, abram] 15:7 — Bereshit Rabbah 44:13 (Michael went down and saved him from the furnace —
  R. Eliezer ben Yaakov; the Holy One Himself — the rabbis); Pesachim 118a:20 (Gabriel: I will go down and cool the
  furnace); Eruvin 53a:7.
- pieces_owed [debit, abram] 15:9 — closed 15:10; pieces_cut [status, the pieces] 15:10 — Bereshit Rabbah 44:14-15
  (three kinds of bulls, goats, rams — the atonements; the kingdoms: Babylon, Media, Greece; the bird Israel), 44:16
  (the vulture driven off — his merit); dread_and_darkness [status, abram] 15:12.
- seed_to_serve_four_hundred [heaven, the seed of Abraham] 15:13 כִּי גֵר יִהְיֶה זַרְעֲךָ (for your seed shall be a stranger) and אַרְבַּע מֵאוֹת שָׁנָה (four
  hundred years) — the value 400 parsed; Bereshit Rabbah 44:18 ('from when you have
  seed' — the running setting seed_isaac's teacher on the shelf); the CAUSE the tradition names: Nedarim 32a:14-15
  (R. Abahu: 210 years of servitude for pressing scholars into service, 14:14; Shmuel: for 'whereby shall I know',
  15:8; R. Yochanan: for 'give me the persons', 14:21) — closed by S1's Exodus scene at 12:41 (the close line added
  there this sitting; the S1 bare scene finds nothing, its tuple unmoved); nation_to_be_judged [heaven, the seed of
  Abraham] 15:14 — closed at Exod 12:29 (S1's scene; Eduyot 2:10's twelve months of judgment, S1's CS9);
  to_go_out_with_substance [heaven, the seed of Abraham] 15:14 — closed at Exod 12:36 (Berakhot 9a:29-9b:1 'so that
  the righteous one will not say' — S1's own row); Bereshit Rabbah 44:19-20 ('also that nation': the four exiles;
  'afterward' — after ten plagues); buried_in_peace [heaven, abram] 15:15 — closed at 25:8-9 (S3's write);
  fourth_generation_return [heaven, the seed of Abraham] 15:16 — OPEN (Joshua — book-bound); amorite_not_full
  [status, the amorite] 15:16.
- passed_between_the_pieces [status, the pieces] 15:17 — Bereshit Rabbah 44:21 (four things shown: Gehenna, the
  kingdoms, the giving of the Torah, the Temple); covenant_cut [REUSE, status] 15:18 (the cutting verb with the
  covenant noun — Exod 34's word at Genesis' first cutting: a REFERENCE by lemma; 44:22: this world revealed to him,
  and the world to come? — the arms; the pre-Sinai engine's covenant cells by call).
- ten_years_childless [status, sarai] 16:3 מִקֵּץ עֶשֶׂר שָׁנִים לְשֶׁבֶת אַבְרָם בְּאֶרֶץ כְּנָעַן (at the end of ten years of
  Abram's dwelling in the land of Canaan) — Mishnah Yevamot 6:6 (married ten years without children: he may not
  neglect procreation — the answer-sheet rule with this verse as its source), Yevamot 64a:5 (the years abroad do not
  count — from this verse); Bereshit Rabbah 45:3; the marker at Abram's 85 (CG6).
- conceived [status, hagar] 16:4 — Bereshit Rabbah 45:4 (from the first union — R. Levi; never from the first — R.
  Elazar); mistress_despised [status, hagar, cp sarai] 16:4; judgment_invoked [heaven, sarai, cp abram] 16:5 יִשְׁפֹּט
  יְהוָה בֵּינִי וּבֵינֶיךָ (the LORD judge between me and you) — Bereshit Rabbah 45:5 (you wrong me with words — hearing
  my disgrace and silent) — OPEN (the tradition's 'she was punished first' searched on the local shelf and not found:
  a remark, no checkpoint); afflicted [body, hagar, cp sarai] 16:6 — 45:6 (Abram: I am not obliged for her good or
  ill — Deut 21:14's 'after you have afflicted her'); fled_from_the_mistress [status, hagar] 16:6.
- return_owed [debit, hagar, cp the angel] 16:9 שׁוּבִי אֶל גְּבִרְתֵּךְ (return to your mistress) — OPEN (the ink narrates
  the son born, never the return: the corpus's demand OPEN); seed_multiplied [heaven, hagar] 16:10 — OPEN;
  ishmael_announced [heaven, hagar] 16:11 — closed at 16:15 (the son born and named — by Abram, where 16:11 said
  'you shall call': the ink's own delta; Bereshit Rabbah 45:8: three named before they were formed — Isaac, Solomon,
  Josiah — Ishmael beside them by the verse); wild_ass_of_a_man [status, ishmael] 16:12 — 45:9 (R. Yochanan: grows in
  the wilderness; Reish Lakish: plunders souls); name_given on god (16:13 'You are a God of seeing' — 45:10: God
  never conversed with a woman but that righteous one, through an angel), on the well (16:14).

### 6d. The daemon's watches (daemon_dispositions.yaml — declared BEFORE the code; the gate run to fail)
law_primeval: formed_from_dust → [living_soul]; placed_in_the_garden → [to_work_and_keep]; named → [name_given] (the
Gen seats; the Exodus daemon seat-checked); woman_built → [helper_made]; deep_sleep_fell → [deep_sleep_fell, dread_and_darkness] (the 15:12 seat);
serpent_spoke → []; ate_of_the_tree → [breached_the_first_rule]; eyes_opened → [eyes_opened, girdles_made];
hid_from_the_voice → []; interrogated → [deceived]; sentenced → [serpent_cursed, enmity_set, pain_multiplied,
ruled_by_the_husband, ground_cursed, sweat_bread, return_to_dust, cursed_from_the_ground, fugitive_and_wanderer]
(by the sentence field); clothed_in_skins → [clothed_in_skins]; expelled → [expelled, way_guarded]; bore →
[begotten]; begot → [begotten, peleg_named_for_the_division] (the 10:25 seat); first_offerings_brought → [regarded, not_regarded]; anger_burned → [];
counsel_given → [sin_at_the_door]; killed → [slain, bloods_cry]; mark_promised → [mark_set, sevenfold_vengeance];
went_out_from_the_presence → [settled_in_nod]; city_built → [city_built]; married → [wife_taken, ten_years_childless] (the Gen 4, 6,
11, 16 seats — the ten years at 16:3); lamech_sang → [seventy_sevenfold_claimed]; profanation_begun → [idolatry_begun]; enoch_taken →
[taken_by_god]; multiplied → [multiplied_on_the_earth]; decree_of_the_reprieve → [reprieve_of_a_hundred_and_twenty]; wickedness_seen →
[wickedness_great, earth_corrupted]; regretted → [regretted_making_man]; wipe_resolved → [to_be_wiped];
favor_found → [found_favor]; end_decreed → [sealed_for_violence]; ark_commanded → [ark_owed, ark_spec,
covenant_promised]; ark_made → [ark_built]; boarding_commanded → [boarding_owed, seven_days_reprieve];
entered_the_ark → [in_the_ark, ark_intercourse_barred, shut_in]; flood_came → [fountains_split];
all_flesh_expired → [wiped_out, only_noah_remained, no_share_in_the_world_to_come]; waters_prevailed →
[waters_prevailed_a_hundred_and_fifty]; remembered → [remembered_by_god]; waters_receded → [waters_receding]; ark_rested →
[rested_on_ararat]; bird_sent → [raven_sent, dove_returned] (by the bird field); cover_removed → [ground_seen_dry];
exit_commanded → [exit_owed, intercourse_permitted]; exited_the_ark → [out_of_the_ark]; altar_erected →
[altar_built]; olah_offered → [olah_offered]; savor_smelled → [savor_smelled]; never_again_resolved →
[ground_not_cursed_again, seasons_pledged]; vineyard_planted → [vineyard_planted]; drunk_and_uncovered → [drunk,
uncovered]; nakedness_seen_and_told → [saw_and_told]; covered_backward → [covered_the_father]; awoke_and_knew →
[]; cursed_canaan → [canaan_cursed]; blessed_shem_and_japheth → [shem_blessed, japheth_enlarged]; kingdom_begun →
[kingdom_founded]; cities_built → [cities_built]; journeyed → [encamped_at] (the Gen seats); tower_proposed →
[tower_undertaken]; lord_descended → [descended_to_see] (the Gen 11 seat); confounded_and_scattered →
[language_confounded, scattered, building_ceased, no_share_in_the_world_to_come]; died →
[died_before_his_father] (the Gen 11 seat; the family daemon seat-checked to Gen 23); barren → [barren];
call_given → [go_owed, great_nation_promised, blessing_promised]; went → []; appeared → []; land_promised →
[land_promised]; called_on_the_name → [called_on_the_name]; famine_came → [famine]; sister_asked →
[presented_as_sister]; woman_taken → [taken_to_pharaohs_house]; dealt_well → [enriched_for_her_sake]; plagued →
[plague_struck]; pharaoh_protested → []; sent_away → [sent_out]; strife_arose → [strife_between_herdsmen];
separation_proposed → []; lot_chose → [chose_the_plain]; separated → [parted]; sodom_wicked →
[no_share_in_the_world_to_come]; war_waged → [rebelled, defeated]; lot_taken → [taken_captive]; escapee_told →
[called_the_hebrew]; mustered_and_pursued → [muster_of_three_hundred_and_eighteen, night_divided, kings_smitten]; brought_back →
[goods_brought_back]; bread_and_wine_brought → [bread_and_wine, blessed_by_the_priest, priesthood_removed];
tithe_given → [tithe_given]; kings_demand_refused → [sworn_to_take_nothing, portion_reserved]; word_came →
[shield_promised]; heir_questioned → [childless]; heir_declared → [heir_from_the_loins]; stars_shown →
[seed_as_stars]; believed → [believed, reckoned_righteousness] (the Gen seat); sign_asked → []; pieces_commanded →
[pieces_owed]; pieces_cut → [pieces_cut]; passed_between_the_pieces → [passed_between_the_pieces]; decree_of_the_sojourn →
[seed_to_serve_four_hundred, nation_to_be_judged, to_go_out_with_substance, buried_in_peace, fourth_generation_return,
amorite_not_full]; covenant_cut_with_abram → [covenant_cut, land_granted]; hagar_offered → []; conceived_and_despised
→ [conceived, mistress_despised]; wrong_claimed → [judgment_invoked]; maid_released → []; afflicted → [afflicted];
fled → [fled_from_the_mistress] (the Gen seat); angel_found → []; return_commanded → [return_owed];
seed_promised_to_hagar → [seed_multiplied]; ishmael_announced → [ishmael_announced, wild_ass_of_a_man]; and the
15:7 seat of land_promised writes brought_out_of_ur beside it (the seat field).
A kind with an empty list is the ink's act kept on the tape for the record (S1's precedent, 4d).

### 6e. The registry (logic/corpus/entity_registry.yaml — members with units [step9-scenes])
Existing entities gain the scene tokens: the_human ← 'adam' (exists); eve ← 'eve'; adam_and_eve ← 'adam-and-eve';
noach ← 'noah' (exists); noah_and_sons ← 'noah-and-sons'; abraham ← 'abram'; sarah ← 'sarai'; lot ← 'lot'; hagar ←
'hagar'; ishmael ← 'ishmael'; melchizedek ← 'melchizedek'; paro_abram_era ← 'pharaoh-of-abram'; bnei_ha_elohim ←
'the-sons-of-god'; servant_of_abraham ← 'eliezer-of-damascus' (UNCERTAIN, as its note already says);
mitzrayim_son_of_ham ← (none); israel_people ← 'the-seed-of-abraham' (a people-token, convention 6); god ← 'god'
(exists). NEW entities: the primeval line (cain, abel, seth, enosh, kenan, mahalalel, jared, enoch, methuselah,
lamech), the line of Cain (enoch_son_of_cain, irad, mehujael, methushael, lamech_son_of_methushael, adah, zillah,
jabal, jubal, tubal_cain, naamah, cains_wife — the wife UNCERTAIN, the ink names her by her husband), shem, ham,
japheth, canaan, cush, nimrod, asshur, arpachshad, shelah, eber, peleg, joktan, reu, serug, nahor_son_of_serug,
terah, haran, nahor_son_of_terah, milcah, iscah (UNCERTAIN — Megillah 14a:13 reads her as Sarah: named, not made),
the_serpent, the_generation_of_the_flood, the_generation_of_enosh, the_builders (the generation of the dispersion),
the_men_of_sodom, the_four_kings, the_five_kings, the_king_of_sodom, the_escapee, the_allies (Aner, Eshcol, Mamre),
the_herdsmen, the_amorite, humankind (the human race as a body — 6:1, 6:5), the_angel_at_the_well (16:7 — the
angel_of_the_lord entity exists: its member 'the-angel-of-the-lord' joins it instead); objects and places:
the_garden, the_ground, the_earth (the pre-Sinai scene's 'the-earth' token joins here), the_cherubim,
the_city_of_enoch, the_ark, the_raven, the_dove, the_altar_of_noah, the_vineyard, the_city_and_tower,
the_land_of_canaan, the_altar_at_shechem, the_altar_at_bethel, the_altar_at_hebron, the_pieces, the_well_lachai_roi.

### 6f. The calendar rows (calendar_parameters.yaml)
- gen6_3_reading {reprieve: 120 years before the flood (the running setting); lifespan: the human span capped at
  120 (UNEXERCISED)} — Bereshit Rabbah 30:7 (all hundred and twenty years Noah planted and cut), 26:6 (the verse's
  other readings); Onkelos (the frozen unit's read: 'an extension is given them'). The row licenses the marker of 6g.
- abel_days_bound 50 — Bereshit Rabbah 22:4 (both arms: Abel was in the world no more than fifty days) — recorded,
  UNEXERCISED (the stretch carries no stamp; graded as a remark, not a checkpoint).
- window_count_from 'the tenth month's first' (8:5) — the antecedent of 8:6's 'at the end of forty days' is the
  nearest date the ink states: channel ink, said so.

### 6g. The markers (the stitcher's table; every number parsed from the ink and re-verified at run time)
  Gen 6:3   R  [120]  the decree of the hundred and twenty years — RETROGRADE: M['decree_of_the_reprieve'] = the flood − 120
            years (the flood computed from Noah's 600th year, 2/17, as 7:11's row does); the counter stands at 5:32's
            Noah-500, so the stated day is EARLIER — the engine dates 6:1-7:4's events by the text (Pesachim 6b:7,
            the tape's standing principle at Lev 8:2 and Num 9:1); the reprieve's timer then fires at the flood (CG2).
            The teacher: Bereshit Rabbah 30:7 (the 120 years ran before the flood); the arithmetic the ink's own
            (600 − 120 = 480 < 500).
  Gen 7:4   F  [7, 40, 40]  the boarding call: M['boarding_call'] = M['flood'] − 7 — 'yet seven days'; 7:10 'after
            the seven days' = the flood.
  Gen 7:11  F  (exists — the flood).
  Gen 7:12  F  [40, 40] at 7:17 (the numbers' verse 7:12, the position 7:17 where the ink says the forty days were
            on the earth and the ark was lifted): M['rain_end'] = M['flood'] + 40 — 7:13-16's 'on that very day'
            stays at the flood's day.
  Gen 8:4, 8:5, 8:13, 8:14  F  (exist — the rest, the tops, the drying, the dry earth).
  Gen 8:6   F  [40]  M['window'] = M['mountains'] + 40 (the row window_count_from).
  Gen 8:10  F  [7]   M['dove_2'] = M['window'] + 7 (the first dove at the window's day, modeled at the same day as the
            raven, said so); Gen 8:12 F [7] M['dove_3'] = M['dove_2'] + 7 — the sendings inside the tenth month's
            stretch (CG4).
  Gen 16:3  F  [10]  M['hagar_given'] = the first day of Abram's year 85 (12:4's 75 + the ten years of dwelling —
            the arrival 12:5 in the year of the going out) — the marker's year the ink's, the day modeled (convention
            4); Ishmael's 16:16 at 86 (exists) — CG6.
  Babel (11:1-9), Cain (4:1-16), the garden (2:4-3:24), the vineyard (9:18-27), the nations (10), the war (14) and
  the pieces (15) carry NO stamp: the events sit at the counter inside the bound the neighboring markers open — the
  ink's own silences, printed by the gaps line.

### 6h. The checkpoints (the sequence runner; declared by the text or the shelf, computed by the engine)
  CG0 Mishnah Avot 5:2's ten generations from Adam to Noah and ten from Noah to Abraham — the tape's life eras
      counted (the_human .. noach = 10; shem .. abraham = 10) — MATCH.
  CG1 Mishnah Eduyot 2:10's twelve months for the flood generation's judgment — the ink's stretch 7:11 → 8:14 by the
      Calendar = twelve months + N days, N within [10, 11] (Bereshit Rabbah 33:7's own arithmetic: 'the eleven days by
      which the solar year exceeds the lunar') — MATCH expected (the modeled months give 10 at the stitcher's print).
  CG2 the reprieve's timer (6:3 + 120 years, retrograde-dated) fires ON the flood's day — MATCH expected.
  CG3 the seven days' timer (7:4) fires on the flood's day — MATCH expected.
  CG4 the dove's last sending (8:12) before the drying (8:13) — MATCH expected (the window at 11/11, the third
      sending at 11/25, the drying at 1/1).
  CG5 the war's years: 14:4-5's twelve, thirteen, fourteen chain by the ink's numbers (12 + 1 + 1 = 14) — MATCH; the
      tradition's two sums beside it (Bereshit Rabbah 42:6: R. Yose twenty-five, Rabban Shimon ben Gamliel thirteen).
  CG6 Hagar given at Abram's 85 (16:3) and Ishmael born at 86 (16:16): one year — MATCH expected.
  CG7 Mishnah Sanhedrin 10:3's three rows of this stretch = three open entries of no_share_in_the_world_to_come on
      the flood generation, the dispersion generation, the men of Sodom — MATCH expected.
  CG8 Terah's death 60 years after Abram's departure (11:26's 70 + 12:4's 75 = 145; 11:32's 205) — the P marker
      against the age marker — MATCH expected; Bereshit Rabbah 39:7's own number (sixty-five) printed beside it.
  CG9 Adam's 930 (5:5) within the thousand-year 'day' of 2:17 (Bereshit Rabbah 19:8) — the proleptic marker against
      the creation day: MATCH expected.

### 6i. The scene (the runner's own bare world; the rows in the text's order; the tuple predicted by a hand-model
written FIRST — scratchpad o8_s2_predict.py — and printed before the runner is typed; the model consulting the OP
CLASS and the WRITE TIME of every effect, reused ones included — S1's lesson)
The slots (subject, effect) in the order of 6c; then the open entries, the timers set and fired, the closes
performed, the clock. The bare scene's timers: reprieve_of_a_hundred_and_twenty (due beyond the scene's end: set, not fired),
seven_days_reprieve (due inside: set and fired — the boarding at scene day d, the flood at d + 7). The literal is
typed from the predictor's print.

### 6j. The answer sheet and the shelf the cells read
Mishnah rows verified by their own tokens: Sanhedrin 10:3 (דור המבול, דור הפלגה, אנשי סדום — the three rows), 4:5
(דמי אחיך — the bloods), Avot 5:2 (עשרה דורות — twice), 5:3 (עשרה נסיונות — the trials' count owed to S3), Eduyot 2:10
(דור המבול — the twelve months), Yevamot 6:6 (עשר שנים; זכר ונקבה בראם), Megillah 1:8, יונית (Greek).
Babylonian rows (all read at this sitting by script; the file index 2*daf−2, +1 for b — every file checked to carry
its 1a/1b at index 0-1): Sanhedrin 107b:18-108a:5, 108a:9-23, 108b:2-19, 109a:4-9, 37b:10-12, 70a:18-22; Nedarim
32a:9, 32a:14-18, 32b:6; Sotah 14a:4-6; Megillah 9b:4-5, 14a:13; Berakhot 40a:14; Kiddushin 30b:5; Bava Batra 100a:7;
Yevamot 64a:5; Chullin 89a:7; Eruvin 53a:7; Pesachim 118a:20; Rosh Hashanah 11b:6-7 (the flood's month by R. Yehoshua
and R. Eliezer — located by script under the runner's own index formula; the ordinal reading the runner already prints beside C2); Shabbat 55b:3-4 (four died by the
serpent's counsel — the value of return_to_dust's arm). Bereshit Rabbah (the Genesis spine) 16:5, 17:2-5, 19:5-8,
20:4-12, 21:7-9, 22:4-13, 23:1-7, 25:1-3, 26:4-6, 27:4, 28:9, 29:1-5, 30:7, 31:5, 32:5-7, 33:1-7, 34:7-11, 36:3-8,
37:4-7, 38:6-14, 39:7-16, 40:3-6, 41:2-10, 42:6-8, 43:3-9, 44:4-23, 45:1-10. The Mekhilta Shirata ch.1 row 1 (S1's
row, read again at 15:6).

### 6k. The edits to standing files (each with its check)
- cold_run_exodus_story.py: the branches named, journeyed, fled, believed, lord_descended gain the seat check
  (Exod only — WE.seat(src)[0] == 'Exod'); the scene gains three close lines at 12:29, 12:36, 12:41/12:51 for the
  Gen 15 entries (they find nothing on the bare scene: the tuple UNCHANGED, the guard re-measured).
- cold_run_family.py: `died` gains the seat check (Gen 23) — its scene unchanged.
- cold_run_sequence.py: the import and DAEMON_ORDER (+ law_primeval after law_pre_sinai — the 41st); the CG
  checkpoints after CS9; the literals CENSUS, DAYS (+7 keys), VERDICTS re-predicted by the stitcher, RUN typed from the
  first run after reading; the tape section regenerated.
- scratchpad seq_record.py / seq_stitch.py: SPAN_ORDER and CLOCK_DAY_RUNNERS gain 'primeval' (after 'pre_sinai');
  the MK table gains 6g's rows; the DAYS key list the new keys; the registry's tape lines appended for the new kinds.
- event_vocabulary.yaml (+~110 types; 7 amended), effect_vocabulary.yaml (+~120; 6 reused with their ink lines
  extended), daemon_dispositions.yaml, dependency_dispositions.yaml (the span, the edges, the pointers),
  calendar_parameters.yaml (+3 rows), entity_registry.yaml (+~70 entities and members), COMPILE_DEBT (O8 S2 DONE),
  DAEMON_INDEX / DEPENDENCY_INDEX regenerated, THE_STEPS (the retrograde-dated timer as a convention if S2 proves
  it), THE_BRIEFING, the state doc, memory.

### 6l. The order of work (the wrap's rhythm, as 4l)
1. This declaration. 2. The effects appended by script (each ink claim through the CLAIMS list). 3. The types
appended by script (the witnesses cut and verified; the lint 0). 4. The calendar rows and the registry entities. 5.
The daemon declared; the gate run → FAIL. 6. The span on a stub runner; the census --emit; the dispositions filed;
the gate run. 7. The hand-model prediction printed. 8. The runner typed (fix_percent first); run; misses read. 9. The
seat checks on the two older daemons and the three closes in S1's scene; those runners rerun. 10. The recorder and
the stitcher (the MK rows); the sequence runner's literals; the sequence run; the CG verdicts read. 11. The gates, the
probes, the sweep, the corpus regression. 12. The records; the compaction point.

### 6m. OPEN at this sitting
The dispersion's year (Peleg's days, 10:25) not on the local shelf — Babel undated. Cain's wife and Iscah UNCERTAIN
in the registry. The tradition's 'she was punished first' (16:5) not found under the searched forms. The trials of
Abraham (Avot 5:3) counted at S3 over both stretches. The tree's identity, the 120's two readings, the ark's window
or gem, the raven's and the dove's arms — recorded as values, none run as a world. The retrograde-dated timer (6:3)
is the sitting's engine question: proved or refuted at CG2.

### 6n. AS RUN (2026-09-08; the account: REPORT_NARRATIVE_GAPS.md, the second sitting)
The order held: the effects (311 → 454 — 143 new, eight reused with their ink lines extended; fifty count claims through
the CLAIMS list and verified by script before a line was appended; the appender refused two glosses carrying semicolons;
two shelf claims not on the local shelf replaced before the write — Onkelos on 2:7 and 4:26 are not in the units' notes,
so Bereshit Rabbah 14:9 and the unit's own export stand — and the flood rows of Rosh Hashanah located by script at
11b:6-7, the design's 10b corrected), the types (341 → 445 — 103 new and altar_erected; eight standing kinds extended
with their new witnesses), three calendar rows with their arms, the registry (93 → 168 entities, fifteen members added;
four UNCERTAIN), the daemon declared and the gate run to FAIL. The gate's parser reads `[a-z_]` names only: six names
with digits refused and renamed everywhere (the two decrees; the reprieve, the waters, the muster, the seed's four
hundred), and the build() cell listed as a function removed, as at S1. The span on a stub and the census --emit: twelve
edges, five pointers and the registration edge dispositioned. The hand-model printed (214 slots) and MATCHED on the first
run. The runner 202/206 FIRST RUN — four INK-census literals had been typed from memory or from book-wide counts (the
namings 14 → 12, the begettings 39 → 37, the bearings 7 → 5, the covenant seats) and were corrected beside the recorded
misses; 206/206 second run (pure ink 60 / recorded moves 117 / answer-sheet 10 / data 4 / imports 15 / hypotheses 0).
Two kind names clashed SILENTLY with standing kinds — the appender skips a name it already holds — altar_built (the
ordinances' case kind: a new kind altar_erected registered and the watches renamed) and sentenced (the family's speech
kind: its witnesses, ink and link extended; law_family seat-checked to Genesis 38). The recorder: 183 history events. The
stitcher: 95 markers (78 forward / 15 proleptic / 2 retrograde), 443 events on the tape, 40 closes, 265 kinds, 136
subjects, the tape 645 lines; two register-offs of the primeval's, both the test's backward window inside the chapter,
cited at the answering verse (10:8's perfect "begot" at 10:10; 15:1's "the word came" at 15:2). The sequence runner 6/7
on its first run — CG0-CG9 ALL MATCH as 6h expected, the CS verdicts unchanged; before that run could grade, the tape
stopped on law_primeval's OWN shared branches: `sentenced` read Judah's Gen 38 event (a missing field), and `married`
would have answered Rebekah's and Moses' — seat-checked to Genesis 3-4 and Genesis 2-16 (convention 14 runs both ways:
the new daemon's branches carry the check too). The RUN tuple READ by script before it was typed: the tape's events
attributed to their runners by the tape's own comments — the rest reproduces S1's tuple exactly (260 / 298 / 12 / 8);
the primeval's share 183 events, 224 writes (the bare scene's 223 plus the reprieve's one fire, which only the tape
reaches), two timers set and fired, seventy entities new to the ledger, seventeen closes (its fourteen and S1's three
lines on the pieces' entries); typed (443, 14, 10, 0, 0, 522, 10, 166, the two mornings, 39); 7/7 second run. THE
RETROGRADE-DATED TIMER PROVED at CG2 (6m's question): the decree's entry dated at Noah's 480, its timer's due computed
from the dated day through the Calendar, the counter unmoved, the fire on the flood's day. The census after: Genesis 31
units / 843 verses still uncovered, in five stretches (18-20, 22, 25-31, 33-37, 39-47) — S3 and S4 as sized. The gates,
the probes, the sweep and the corpus regression: the report's closing section.

## 7. S3 — GENESIS 18-20, 22, 25-31 FROM MAMRE TO THE HEAP: THE DECLARATION (2026-09-08, the sitting after O8 S2 in
## the same window; the owner: "now continue"; declared whole BEFORE its code, as sections 4 and 6 were)

### 7a. The span, the runner, the daemon
The span `mamre`: Genesis 18:1-20:18, 22:1-24, 25:1-31:54 — the seventeen frozen units the census lists as the second
and third Genesis stretches (gen_34 mamre, gen_35 sodom, gen_36 gerar, gen_38 moriah, gen_42 abraham_end, gen_43
twins, gen_44 isaac_gerar, gen_45 wells, gen_46 blessing, gen_47 grudge, gen_48 bethel, gen_49 well_stone, gen_50 wage,
gen_51 twelve_names, gen_52 speckled, gen_53 flight, gen_54 heap): 17 units, 382 verses. Cut out, as S2 cut the
pre-Sinai spans: Genesis 21 (the pre-Sinai engine's birth and eighth day, its Beersheba oath), 23 (the family engine's
purchase), 24 (its commission) — the story scene submits the acts around them and closes on their events where the ink
states a fulfillment (7d). The runner cold_run_primeval.py's shape: cold_run_mamre.py, seventeen cells in the text's
order (mamre, sodom, gerar, moriah, abraham_end, twins, isaac_gerar, wells, blessing, grudge, bethel, well_stone, wage,
twelve_names, speckled, flight, heap), each a bare-world unit; the callee imports where the text reaches: the pre-Sinai
code (the covenant's eighth day on every male birth of the stretch; the oath of 26:3 upheld), the offerings (22:13's ram
as a burnt offering in place of the son; 31:54's sacrifice; the altars of 22:9 and 26:25 as at 8:20), the substitution
engine (28:22's tithe vow as 14:20's tithe — the tithe's own status), the family engine (25:9-10's use of the purchased
field; 25:5's all-that-he-had against the inheritance order; 25:25's firstborn by the head), the ordinances engine (THE
PAID KEEPER: Jacob's account of 31:38-40 graded by the four guardians' rows — the torn, the stolen by day and night —
Bava Metzia 93b:3 the shelf's own reading of the keeper's ceiling); the sanctions engine only by S2's standing Sodom
entry (13:13), which 19:24-25 executes in this world and leaves open for the next. The daemon law_mamre, the
FORTY-SECOND. The scene on a bare world with w.laws = [law_mamre, law_pre_sinai] — as S1's, not S2's: this stretch's
births are UNDER THE COVENANT of Genesis 17, so the eighth-day timer runs on every male `born` (Esau, Jacob, the eleven
sons — thirteen), and NOT on Dinah (17:12 says "every male": the daemon reads the field the statute names — 7k) and not
on Lot's daughters' sons or Nahor's (their births are `bore`/`begot`, the households outside the covenant — the price
of missing installation, named as such: the state doc's THE TIME CONSENSUS (T1)).

### 7b. The types (event_vocabulary.yaml; NEW unless marked; witnesses cut from the verses' consonants by script and
### checked against the Tanakh DB before the append; the form by the register test; digits never in a name)
REUSED kinds, their witness lines extended (the seat and the witness): appeared (18:1, 26:2, 26:24 night); named
(19:37 Moab, 19:38 Ben-ammi, 22:14 the place, 25:25 Esau, 25:26 Jacob, 25:30 Edom, 26:18 the wells, 26:20 Esek, 26:21
Sitnah, 26:22 Rehoboth, 26:33 Shibah, 28:19 Bethel, 29:32-30:24 the twelve, 31:47 the two tongues, 31:48 Galeed, 31:49
Mizpah — twenty-nine seats); married (25:1, 26:34 twice, 28:9, 29:23, 29:28, 30:4, 30:9); born (25:24-26 the twins,
29:32-30:24 the twelve — fourteen, Dinah with sex f); bore (19:37, 19:38, 25:2); begot (22:20-24 Nahor's house and
Bethuel, 25:3-4 the rosters); died (25:8, 25:17); buried (25:9); journeyed (20:1, 22:19, 25:11, 26:1, 26:17, 26:23,
28:10, 29:1, 31:21); remembered (19:29, 30:22); sent_away (19:29 Lot by God, 25:6, 26:16, 26:31, 28:5); expelled? no —
sent_away carries 26:16; fled (31:21); pursued (31:23); decree_issued (26:11); return_commanded (31:3); famine_came
(26:1); sister_asked (20:2, 26:7); woman_taken (20:2); altar_erected (22:9, 26:25); called_on_the_name (26:25);
olah_offered (22:13); conceived? — the S2 kind is conceived_and_despised (Hagar's); the conceptions here ride `born`;
barren (25:21, 29:31); word_came? no — the appearances are `appeared`; covenant_cut_with_abram? no — a new
covenant_cut_between_men (26:28-31, 31:44-54) beside it; anger_burned (30:2, 31:36); tithe_given? no — the vow is new.
NEW kinds (form act unless speech): ran_and_bowed (18:2; 19:1 Lot), hospitality_offered [speech] (18:3-5), cakes_ordered
[speech] (18:6), calf_prepared (18:7), meal_served (18:8), son_promised [speech] (18:10; 18:14), laughed_within (18:12;
17:17 is the pre-Sinai's), laugh_denied [speech] (18:15), escorted (18:16), house_charged [speech] (18:19), outcry_declared
[speech] (18:20-21), stood_before_the_lord (18:22), pleaded_for_the_righteous [speech] (18:23-32, the six counts as the
value), lord_departed (18:33), lodging_urged (19:3), matzot_baked (19:3), house_surrounded (19:4), men_demanded [speech]
(19:5), daughters_offered [speech] (19:8), pressed_at_the_door (19:9), pulled_in (19:10), struck_blind (19:11),
evacuation_commanded [speech] (19:12), mocked_by_sons_in_law (19:14), lingered (19:16), led_out (19:16), escape_commanded
[speech] (19:17), little_city_pleaded [speech] (19:18-20), city_spared [speech] (19:21-22), fire_rained (19:24),
overturned (19:25), looked_back (19:26), rose_to_the_place (19:27), looked_down (19:28), dwelt_in_the_cave (19:30),
made_the_father_drink (19:33; 19:35), came_in_a_dream [speech] (20:3; 31:24), king_pleaded [speech] (20:4-5),
prophet_declared [speech] (20:6-7), servants_told (20:8), rebuked [speech] (20:9-10; 26:9-10 Isaac), answered_the_king
[speech] (20:11-13), restored (20:14), dwelling_granted [speech] (20:15), silver_given [speech] (20:16), prayed (20:17
the first "and he prayed"; 25:21 "and he entreated"), healed (20:17), wombs_shut (20:18 — the narrator's flashback, its
window's own verbs), tested (22:1), offering_commanded [speech] (22:2), rose_early_and_went (22:3), place_seen_on_the_third_day
(22:4), lads_left [speech] (22:5), wood_laid (22:6), lamb_asked [speech] (22:7-8), bound (22:9), knife_taken (22:10),
called_from_heaven [speech] (22:11-12; 22:15), ram_seen (22:13), sworn_by_himself [speech] (22:16-18), births_told
[speech] (22:20-23), all_given (25:5), gifts_given (25:6 — the family's kind, its witness extended), blessed_after_the_death
(25:11), princes_counted (25:16), fell_before_his_brothers (25:18), struggled_in_the_womb (25:22), inquired (25:22),
oracle_given [speech] (25:23), grew_up (25:27), loved_apart (25:28), stew_boiled (25:29), gulp_demanded [speech] (25:30),
sale_demanded [speech] (25:31), birthright_dismissed [speech] (25:32), sworn (25:33; 26:31; 31:53), birthright_sold
(25:33), bread_and_lentils_given (25:34), birthright_despised (25:34), descent_barred [speech] (26:2), oath_upheld
[speech] (26:3-5), dwelt (26:6), seen_sporting (26:8), hundredfold_found (26:12), grew_great (26:13), envied (26:14),
wells_stopped (26:15), wells_redug (26:18), well_found (26:19; 26:32), quarreled (26:20; 26:21), room_made (26:22),
tent_pitched (26:25), well_dug (26:25), visited (26:26), covenant_proposed [speech] (26:28-29; 31:44), feast_made (26:30;
29:22), bitterness_of_spirit (26:35), eyes_dimmed (27:1), hunt_commanded [speech] (27:2-4), overheard (27:5),
counsel_given? — the S2 kind (4:6-7's) is God's counsel; here: mother_counselled [speech] (27:6-10; 27:42-45), objected
[speech] (27:11-12), curse_taken_on [speech] (27:13), kids_fetched (27:14), disguised (27:15-16), delicacies_brought
(27:17-18; 27:31 Esau), identity_claimed [speech] (27:19; 27:24; 27:32 the true one), felt (27:21-23), ate_and_drank
(27:25), kissed (27:26-27; 29:11; 29:13), blessed [speech] (27:27-29 Jacob; 27:39-40 Esau; 28:1-4 the send-off),
trembled (27:33), cried_out (27:34), supplanted_charged [speech] (27:35-36), wept (27:38; 29:11), grudge_held (27:41),
words_told (27:42), loathing_stated [speech] (27:46), sent_to_paddan_aram (28:5), took_a_wife_from_ishmael? — married
carries 28:9; lodged_at_the_place (28:11), dreamed (28:12; 31:10), promised_at_bethel [speech] (28:13-15), awoke_and_feared
(28:16-17), pillar_set_and_anointed (28:18; 31:45 raised), vowed [speech] (28:20-22), well_seen (29:2-3), shepherds_questioned
[speech] (29:4-6), shepherds_rebuked [speech] (29:7-8), stone_rolled (29:10), flock_watered (29:10), kin_told (29:12),
embraced (29:13), month_dwelt (29:14), wage_asked [speech] (29:15; 30:28), wage_named [speech] (29:18; 30:31-33),
contract_accepted [speech] (29:19; 30:34), served (29:20; 29:30), wife_demanded [speech] (29:21), bride_switched (29:23),
maid_given (29:24; 29:29), deceit_charged [speech] (29:25), custom_stated [speech] (29:26), week_demanded [speech] (29:27),
week_fulfilled (29:28), womb_opened (29:31; 30:22), ceased_bearing (29:35), envied_her_sister (30:1), children_demanded
[speech] (30:1), maid_offered [speech] (30:3), mandrakes_found (30:14), mandrakes_traded [speech] (30:14-16), god_heard
(30:17; 30:22 with the remembering), release_demanded [speech] (30:25-26), divination_confessed [speech] (30:27),
service_audited [speech] (30:29-30), flock_removed (30:35-36), rods_peeled (30:37-38), flock_bore_striped (30:39),
flocks_separated (30:40-42), broke_out (30:43), sons_words_heard (31:1), face_changed (31:2), wives_summoned (31:4),
account_given [speech] (31:5-13; 31:36-42 the twenty years), wives_answered [speech] (31:14-16), rose_and_loaded (31:17),
livestock_driven (31:18), teraphim_stolen (31:19), heart_stolen (31:20), river_crossed (31:21), told_on_the_third_day
(31:22), overtaken (31:25), charges_laid [speech] (31:26-30), fear_answered [speech] (31:31), death_oath_sworn [speech]
(31:32), tents_searched (31:33-35), quarreled_with_laban (31:36), tribunal_demanded [speech] (31:37), all_is_mine_claimed
[speech] (31:43), heap_made (31:46), witness_declared [speech] (31:48-50), boundary_sworn [speech] (31:51-53), sacrificed
(31:54), ate_and_lodged (31:54). The count is the script's (about a hundred and fifty new; the appender's NEW list is
CHECKED AGAINST THE REGISTRY before the append — S2's lesson: a clashing name is skipped in silence).

### 7c. The effects (effect_vocabulary.yaml; NEW unless marked; each ink claim verified by script before the append;
### the `he` quoted from the verse by the run's own index; the op class named for the hand-model)
REUSED, their ink lines extended: name_given [st] (the twenty-nine seats), wife_taken [st] (25:1, 26:34, 28:9, 29:23,
29:28, 30:4, 30:9), encamped_at [st] (20:1 Gerar, 22:19 Beersheba, 25:11 Beer-lahai-roi, 26:6, 26:17 the wadi, 26:23,
28:11 the place, 31:25 Gilead), famine [st] (26:1 the second), presented_as_sister [st] (20:2, 26:7), remembered_by_god
[st] (19:29, 30:22), sent_out [tr] (19:29, 25:6, 26:31, 28:5), begotten [st] (19:37-38, 22:20-24, 25:2-4), altar_built
[st] (22:9, 26:25), olah_offered [st] (22:13 the ram in place of the son), called_on_the_name [st] (26:25), land_promised
[he] (26:3-4 Isaac, 28:13 Jacob), seed_as_stars [he] (22:17, 26:4), seed_as_dust [he] (28:14 — its line already names
the seat), blessing_promised [he] (22:18, 26:4, 28:14 the nations and the families), great_nation_promised [he] (18:18),
return_owed [de] (20:7 the wife; 31:3 the return to the land), decree_issued [de] (26:11 the touch ban), expelled [st]
(26:16), barren [st] (25:21, 29:31), conceived [st] (25:21, 29:32-30:23), gathered_to_his_people [st] (25:8, 25:17),
buried [st] (25:9), gifts_given [tr] (25:6), firstborn_by_the_head [st] (25:25 — Mishnah Bekhorot 8:1's row),
birthright_transferred [tr] (25:33 — beside the family's 48-49 seats), release_demanded [de] (30:25), circumcision_due
[de] — written by law_pre_sinai, not by law_mamre, on the thirteen male births; seed_multiplied [he] (16:10) CLOSED at
25:16 by the ink's own twelve princes; buried_in_peace [he] (15:15) CLOSED at 25:8 by the ink's own "in a good old
age"; nation_to_be_judged and its siblings untouched.
NEW effects, by cell (op in brackets; subject; the seat): mamre — visitors_received [st abraham 18:2-8; Shabbat 127a:13
the hospitality rule, Bava Metzia 86b:3 the three calves], son_promised_at_the_season [he sarah 18:10, 18:14 — CLOSED
on the tape at 21:2 by the pre-Sinai engine's born:isaac (the daemon closes on that event by seat; on the bare scene the
entry stays open and the model counts it so)], laughed_within [st sarah 18:12], laugh_denied [st sarah 18:15],
house_charged [st abraham 18:19 — righteousness and justice], outcry_to_be_seen [he sodom 18:20-21 — CLOSED at 19:25 by
the overthrow], stood_before_the_lord [st abraham 18:22], righteous_count_pleaded [st abraham 18:24-32 — the value
[50, 45, 40, 30, 20, 10], each number parsed from its verse; Bereshit Rabbah 49:9 and 49:12], spared_for_the_ten [he
sodom 18:32 — CLOSED at 19:24: not found]. sodom — angels_lodged [st lot 19:1-3; Bereshit Rabbah 50:4], matzot_made [st
lot 19:3 — the token is bread for guests, not the leaven law: Bereshit Rabbah 48:12 reads the visit's cakes as Passover's,
a dating the calendar row of 7f carries], house_surrounded [st lot 19:4], daughters_offered [st lot 19:8],
struck_with_blindness [bo the-men-of-sodom 19:11], evacuation_owed [de lot 19:12 — CLOSED 19:16], mocked [st lot
19:14], lingered [st lot 19:16], led_out_of_sodom [tr lot_and_his_house 19:16], looking_back_barred [bl
lot_and_his_house 19:17 — breached 19:26], zoar_spared [st zoar 19:21], overthrown [de the-cities-of-the-plain
19:24-25 — this world's execution of S2's no_share entry, which stays open for the next], pillar_of_salt [st lots-wife
19:26; Bereshit Rabbah 51:5], morning_prayer_founded [st abraham 19:27 — Berakhot 26b:5 "Abraham instituted the morning
prayer", Berakhot 6b:8 the fixed place; the transfer taught], cave_dwelt [st lot 19:30], made_drunk [st lot 19:33,
19:35], daughters_conceived [st the-two-daughters 19:36]. gerar — taken_by_the_king [bo sarah 20:2],
death_decreed_over_the_woman [he abimelech 20:3 — CLOSED 20:17 by the healing], integrity_pleaded [st abimelech
20:4-5], withheld_from_sin [st abimelech 20:6], prophet_declared [st abraham 20:7 — the Torah's first "prophet"],
servants_feared [st the_house_of_abimelech 20:8], great_sin_charged [st abraham 20:9], fear_of_god_doubted [st abraham
20:11], half_sister_claimed [st sarah 20:12], restored_with_gifts [tr abraham 20:14], dwelling_granted [st abraham
20:15], thousand_silver_covering [tr sarah 20:16 — the value a thousand, parsed], prayed_for_abimelech [st abraham 20:17
— Mishnah Bava Kamma 8:7's row: payment does not forgive until the injured asks, and the forgiver must not be cruel,
from this verse; Bava Kamma 92a:4, 92a:16], healed [st the_house_of_abimelech 20:17], wombs_shut [st
the_house_of_abimelech 20:18]. moriah — tried [he abraham 22:1 — Bereshit Rabbah 55:1, 56:11 the tenth; CLOSED 22:12
"now I know"], offering_of_the_son_owed [de abraham 22:2 — CLOSED 22:12 by the countermand], went_to_moriah [st abraham
22:3], place_seen_on_the_third_day [st abraham 22:4], lads_left [st the-two-lads 22:5], wood_laid [st isaac 22:6],
lamb_asked [st isaac 22:7-8], bound_on_the_altar [bo isaac 22:9 — Rosh Hashanah 16a:16 the ram's horn recalls it],
knife_taken [st abraham 22:10], hand_stayed [st abraham 22:12], god_fearing_known [st abraham 22:12], ram_caught [st
the-ram 22:13 — Bereshit Rabbah 56:9], gate_of_enemies_promised [he abraham 22:17], sworn_by_himself [st abraham
22:16], births_told [st abraham 22:20 — the eight of Milcah (parsed: eight) and the four of Reumah, thirteen begotten
with Rebekah]. abraham_end — all_given_to_isaac [tr isaac 25:5 — Sanhedrin 91a:16: deeds of gift in his lifetime],
died_in_good_old_age [st abraham 25:8 — Bereshit Rabbah 62:1; closes 15:15's entry], blessed_by_the_lord [st isaac 25:11;
26:12], twelve_princes [st ishmael 25:16 — parsed twelve; the twelve names of 25:13-15 counted by the runner],
fell_before_his_brothers [st ishmael 25:18 — 16:12's polarity]. twins — prayed_for_the_wife [st isaac 25:21 — Yevamot
64a:6: "Isaac was barren", forty to sixty], struggled_in_the_womb [st rebekah 25:22], inquired_of_the_lord [st rebekah
25:22], two_nations_in_the_womb [he rebekah 25:23 — OPEN], elder_to_serve_the_younger [he esau 25:23 — OPEN, off the
three books], heel_held [st jacob 25:26], hunter_of_the_field [st esau 25:27], dweller_in_tents [st jacob 25:27],
loved_by_the_father [st esau 25:28], loved_by_the_mother [st jacob 25:28], stew_boiled [st jacob 25:29], came_in_weary
[st esau 25:29 — Bava Batra 16b:11: that day Abraham died, the lentils the mourner's meal — the reading-placed day of
7g], gulp_demanded [st esau 25:30], sale_demanded [st jacob 25:31], birthright_dismissed [st esau 25:32], oath_sworn [st
esau 25:33; isaac_and_abimelech 26:31; jacob 31:53], bread_and_lentils_given [tr esau 25:34; Bava Batra 16b:12],
birthright_despised [st esau 25:34]. isaac_gerar — descent_to_egypt_barred [bl isaac 26:2 — Bereshit Rabbah 64:3: an
unblemished burnt offering leaves not the enclosure, the transfer taught], sojourn_commanded [st isaac 26:3],
oath_to_abraham_upheld [st isaac 26:3], charge_kept [st abraham 26:5 — "My charge, My commandments, My statutes, My
teachings": Yoma 28b:10, Kiddushin 82a:10 — the whole Torah kept before it was given; THE TIME CONSENSUS's (T1) fork
will read these two rows], seen_sporting [st isaac 26:8], wife_acknowledged [st isaac 26:9 — the "guilt" of 26:10 is a
homograph of the guilt offering: FALSE at the census], hundredfold_found [st isaac 26:12 — the value a hundred, parsed;
Bereshit Rabbah 64:6: measured for the tithes], grew_very_great [st isaac 26:13], envied [st the-philistines 26:14],
wells_stopped [st the-wells-of-abraham 26:15 — CLOSED 26:18]. wells — living_water_found [st isaac 26:19],
quarreled_over [st the-herdsmen-of-gerar 26:20, 26:21], room_made [st isaac 26:22], fear_not_promised [he isaac 26:24 —
"I am with you"], well_dug [st isaac 26:25 — found 26:32], covenant_proposed [st abimelech 26:28; laban 31:44],
feast_made [st isaac 26:30; laban 29:22], covenant_between_men [st isaac 26:31 with abimelech; jacob 31:53 with laban],
bitterness_of_spirit [st isaac_and_rebekah 26:35]. blessing — eyes_dim [st isaac 27:1], death_day_unknown [st isaac
27:2], hunt_owed [de esau 27:3-4 — CLOSED 27:31 brought, the blessing gone], overheard [st rebekah 27:5],
two_kids_counselled [st rebekah 27:9 — Bereshit Rabbah 65:14: the contract's two kids daily], objection_hairy_smooth [st
jacob 27:11], curse_taken_upon_herself [st rebekah 27:13], disguised_in_esaus_garments [st jacob 27:15-16],
delicacies_brought [st jacob 27:17; esau 27:31], identity_falsely_claimed [st jacob 27:19, 27:24], not_recognized [st
isaac 27:23 — "the voice is Jacob's voice"], blessed_with_dew_and_fat [he jacob 27:28 — OPEN], peoples_to_serve [he
jacob 27:29 — OPEN], blessing_ratified [st jacob 27:33 — "indeed he shall be blessed"], trembled [st isaac 27:33],
great_and_bitter_cry [st esau 27:34], supplanted_twice [st esau 27:36 — the value two: the ledger's two transfers on
Jacob from Esau, the birthright (25:33) and the blessing (27:27), counted by the runner as a checkpoint], master_made
[st jacob 27:37], wept [st esau 27:38; jacob 29:11], blessed_by_the_sword [he esau 27:39-40 — OPEN, the yoke's breaking
off the three books]. grudge — grudge_held [st esau 27:41], kill_intent_after_the_mourning [he esau 27:41 — OPEN, never
executed], words_told_to_rebekah [st rebekah 27:42], flight_owed [de jacob 27:43 — CLOSED 28:10 the departure],
few_days_promised [he rebekah 27:44-45 — OPEN forever: she never sends], loathing_stated [st rebekah 27:46],
canaanite_wife_barred [bl jacob 28:1], wife_from_paddan_owed [de jacob 28:2 — CLOSED 29:28], blessing_of_abraham_given
[he jacob 28:3-4 — OPEN], esau_saw_the_command [st esau 28:6-8]. bethel — sun_set_at_the_place [st the-place 28:11 —
Bereshit Rabbah 68:10], stone_pillow [st jacob 28:11 — Chullin 91b:8 the stones gathered into one], ladder_dreamed [st
jacob 28:12], with_you_promised [he jacob 28:15 — CLOSED 31:5 "the God of my father has been with me"], return_promised
[he jacob 28:15 — OPEN: S4's 35:6 closes it], house_of_god_recognized [st jacob 28:16-17], pillar_anointed [st
the_pillar_of_bethel 28:18 — the first oil poured in the Torah], vow_of_bethel [de jacob 28:20-22 — the four conditions
and the two commitments as the value; OPEN: S4's 35:7 and 35:14 close it; Bereshit Rabbah 70:7], tithe_vowed [de jacob
28:22 — Ketubot 50a:3 the doubled verb, the charity cap's verse; the substitution engine's tithe status by CALL as at
14:20]. well_stone — well_with_the_stone [st the-well-of-haran 29:2-3 — the protocol], shepherds_questioned [st jacob
29:4-6], shepherds_rebuked [st jacob 29:7 — the labor-duty read], stone_rolled_alone [st jacob 29:10],
kissed_and_wept [st jacob 29:11], kin_told [st rachel 29:12], embraced_and_housed [st laban 29:13], bone_and_flesh [st
jacob 29:14], month_dwelt [st jacob 29:14 — the marker of 7g]. wage — wage_asked [st laban 29:15], two_daughters [st
laban 29:16-17], loved_rachel [st jacob 29:18], seven_years_owed [de jacob 29:18 — with laban; CLOSED 29:21 by the
timer], seven_years_service [ti jacob 29:18 — the timer, due seven years on, fires at 29:21 "my days are fulfilled"],
contract_accepted [st laban 29:19; 30:34], served_as_few_days [st jacob 29:20], wife_demanded [st jacob 29:21],
bride_switched [st jacob 29:23 — measure for measure, the unit's read], maid_given [tr leah 29:24; rachel 29:29],
deceit_charged [st laban 29:25], custom_of_the_place [st laban 29:26], week_of_the_feast [ti jacob 29:27 — the timer
of seven days; Bereshit Rabbah 70:19 "from here: one does not mix a joy with a joy", Mishnah Moed Katan 1:7 the row it
grounds, Moed Katan 8b:9 and 9a:4 the Babylonian arm from Solomon], second_seven_owed [de jacob 29:27 — CLOSED 30:26 by
the timer], second_seven_service [ti jacob 29:30 — due seven years on, fires at 30:25-26], loved_more [st rachel
29:30]. twelve_names — hated_seen [st leah 29:31], womb_opened [st leah 29:31; rachel 30:22], son_named_for [st each
son — folded into name_given's value: the naming clause], ceased_bearing [st leah 29:35], envied_her_sister [st rachel
30:1], children_demanded [st rachel 30:1], in_gods_place_refused [st jacob 30:2], maid_offered_as_wife [st rachel 30:3;
leah 30:9], mandrakes_found [st reuben 30:14], night_hired_for_mandrakes [tr leah 30:15-16 with rachel — Bereshit Rabbah
72:3 the ledger of the trade], heard_by_god [st leah 30:17; rachel 30:22], daughter_born [st leah 30:21 — no eighth
day: 7k], reproach_gathered [st rachel 30:23], another_son_asked [he rachel 30:24 — OPEN: S4's 35:17-18], remembered on
Rosh Hashanah — Rosh Hashanah 11a:16 by verbal analogy from Leviticus 23:24, Bereshit Rabbah 73:1: a calendar row (7f),
not a marker. speckled — wives_and_children_claimed [st jacob 30:26], divined_blessing [st laban 30:27],
wage_designation_offered [st laban 30:28], service_audited [st jacob 30:29-30], speckled_wage_agreed [de laban 30:31-34
with jacob], righteousness_to_answer [st jacob 30:33], flock_removed [st laban 30:35-36 — three days' distance, parsed
three], rods_peeled [st jacob 30:37-38], flock_bore_striped [st the-flock 30:39], flocks_separated [st jacob 30:40],
strong_ones_bred [st jacob 30:41-42], broke_out_exceedingly [st jacob 30:43]. flight — sons_words_heard [st jacob 31:1],
face_changed [st laban 31:2], wives_summoned_to_the_field [st jacob 31:4], god_with_me [st jacob 31:5 — closes 28:15's
entry], strength_served [st jacob 31:6], wages_changed_ten_times [st laban 31:7, 31:41 — the value ten, parsed twice;
Bereshit Rabbah 74:3 and 74:11 the rabbis' hundred, "no counting fewer than ten"], wage_flip [st the-flock 31:8],
livestock_rescued [tr jacob 31:9], he_goats_dreamed [st jacob 31:10-12], god_of_bethel_recalled [st jacob 31:13 — the
vow's own mention], inheritance_questioned [st rachel_and_leah 31:14-15], do_all_god_said [st rachel_and_leah 31:16],
rose_and_loaded [st jacob 31:17], livestock_driven_to_canaan [st jacob 31:18], teraphim_stolen [tr rachel 31:19 with
laban — Bereshit Rabbah 74:5 her intent; 74:4 and 74:9 the curse's chain], heart_stolen [st laban 31:20],
fled_from_laban [st jacob 31:21], river_crossed [st jacob 31:21]. heap — told_on_the_third_day [st laban 31:22 — the
marker], pursued_seven_days [st laban 31:23 — parsed seven; Bereshit Rabbah 74:6], speech_restrained [de laban 31:24 —
"neither good nor bad"; CLOSED 31:29 he keeps it], overtaken_at_gilead [st jacob 31:25], charges_laid [st laban
31:26-30], fear_answered [st jacob 31:31], death_oath_on_the_thief [he rachel 31:32 — the machine knows the thief from
31:19 though Jacob does not; OPEN: S4's 35:19 closes it by Bereshit Rabbah 74:9's transfer, named there], tents_searched
[st laban 31:33-35], quarreled_with_laban [st jacob 31:36], tribunal_demanded [st jacob 31:37], keeper_account [st jacob
31:38-40 — THE PAID KEEPER by CALL to the ordinances engine: the theft by day and night sought from his hand is the
paid keeper's own liability; the torn he bore is BEYOND it (Exodus 22:12 exempts a witnessed tearing) — Bava Metzia 93b:3
"did Jacob watch as the city's watchmen?", Mishnah Bava Metzia 7:8 the four keepers' row], torn_borne_beyond_duty [st
jacob 31:39], twenty_years_served [st jacob 31:38, 31:41 — the value twenty, parsed twice; fourteen and six parsed
beside it], adjudicated_last_night [st laban 31:42], all_is_mine_claimed [st laban 31:43], pillar_raised [st
the_pillar_of_gilead 31:45], heap_made [st the-heap 31:46], witness_declared [st the-heap 31:48], watch_between_us [he
laban 31:49 — OPEN], covenant_terms [st jacob 31:50 — no affliction of the daughters, no wives over them],
boundary_witnessed [st the_heap_and_pillar 31:52], sacrifice_offered [st jacob 31:54 — the offerings engine by CALL: a
sacrifice eaten by the kin on the mount, the peace offering's shape before its law; the unit's own export],
ate_and_lodged [st jacob_and_his_kin 31:54]. About a hundred and sixty new; the appender's count is the record.

### 7d. The daemon's watches (daemon_dispositions.yaml — declared BEFORE the code; the gate run to fail)
law_mamre watches every kind of 7b and writes the effects of 7c per cell; the REUSED kinds shared with other daemons
carry seat checks BOTH WAYS from the declaration (S2's lesson): law_mamre answers appeared, named, married, born, bore,
begot, died, buried, journeyed, remembered, sent_away, fled, pursued, decree_issued, return_commanded, famine_came,
sister_asked, woman_taken, altar_erected, called_on_the_name, olah_offered, barren, anger_burned, gifts_given ONLY at
seats in Genesis 18-20, 22, 25-31; law_primeval's branches on named, journeyed, lord_descended, believed, fled, married,
begot, bore, died (Gen 11), remembered, sent_away, famine_came, sister_asked, woman_taken, altar_erected,
called_on_the_name, olah_offered, barren, anger_burned, return_commanded, appeared — every one now reads `if gen`, i.e.
any Genesis seat — are narrowed to Genesis 2-16 (7k: the double-writes census of the sequence tape is the proof);
law_family's died (23), married (24), buried, gifts_given (24:53) keep their seats; law_exodus_story's are Exodus's;
law_pre_sinai's `born` gains the male check (7k) and keeps its whole-tape run. The CLOSES on other engines' events:
son_promised_at_the_season closes on `born` isaac at Gen 21:2 (the pre-Sinai engine's); seed_multiplied (16:10) closes
on princes_counted 25:16; buried_in_peace (15:15) on died 25:8. The functions block: the seventeen cells WRAPPED by
law_mamre; no build() entry (S1's and S2's lesson).

### 7e. The registry (logic/corpus/entity_registry.yaml — members with units [step9-scenes])
Scene tokens joined to EXISTING entities by script: abraham, sarah, isaac, rebekah, jacob, esau, laban, leah, rachel,
lot, ishmael, hagar (25:12), god, angel_of_the_lord, three_visitors, two_angels_sodom, the_men_of_sodom, shtei_ha_banot,
eshet_lot, ha_bekhirah, moav, ben_ammi, avimelekh_abraham_era, avimelekh_isaac_era, fikhol_isaac_era, achuzat, qetura,
reuben, simeon, levi, judah, dan_son, naphtali, gad, asher, issachar, zebulun, dinah, joseph, pelishtim, ha_gal, ha_matzeva,
ha_maqom_luz, beer_sheva_place, the wells (beer_eseq, beer_sitna, beer_rechovot), bethuel, nahor, milkah, israel_people
where 22:17's seed is addressed. NEW entities: bilhah, zilpah, mahalath, the-ram, the-two-lads, the_house_of_abimelech,
the-people-of-gerar, the-wells-of-abraham, the-herdsmen-of-gerar, the-philistines (if absent), the-sons-of-the-concubines,
lot_and_his_house, the-two-daughters, the-cities-of-the-plain, zoar (if absent), the-place (Bethel before its name),
the_pillar_of_bethel, the_pillar_of_gilead, the-heap, the_heap_and_pillar, the-well-of-haran, the-flock,
jacob_and_his_kin, rachel_and_leah, isaac_and_rebekah, the-sons-of-nahor (uz, buz, kemuel, chesed, hazo, pildash,
jidlaph, bethuel; tebah, gaham, tahash, maacah), keturah's six (zimran, jokshan, medan, midian, ishbak, shuah) and the
rosters' names (sheba, dedan; ephah, epher, hanoch, abida, eldaah; the Asshurim, Letushim, Leummim as peoples),
ishmael's twelve (nebaioth, kedar, adbeel, mibsam, mishma, dumah, massa, hadad, tema, jetur, naphish, kedemah),
judith, basemath, beeri, elon — UNCERTAIN: the thief's identity as the machine's (31:32's subject is Rachel by 31:19,
the narrator's knowledge, not Jacob's — noted on the entity), Keturah's identity (Bereshit Rabbah 61:4: Rav says Hagar —
recorded as a note, no fold).

### 7f. The calendar rows (calendar_parameters.yaml)
mamre_visit_date {passover_of_the_year_before (Bereshit Rabbah 48:12: "this teaches it was Passover" — the RUNNING
reading; joined by the ink's "at this season" 18:10, 18:14 and "at the set time" 21:2 to born:isaac, itself placed on
Passover by Rosh Hashanah 10b:10), unmarked}; binding_placement {before_sarahs_death (Bereshit Rabbah 58:5: "she died of
that grief, therefore the binding is set beside Sarah's life" — the RUNNING reading: Isaac 37 by 17:17 and 23:1),
page_order (unexercised)}; stew_day {abrahams_death_day (Bava Batra 16b:11 — the RUNNING reading), page_order};
blessing_placement {ishmaels_death_year (Bereshit Rabbah 68:5 Jacob 63; Megillah 17a:5 by 28:9's Mahalath — RUNNING),
page_order}; hidden_years {fourteen (Megillah 17a:5-6, Bereshit Rabbah 68:5, 68:11 — RUNNING), none (unexercised)};
rachel_remembered_date {rosh_hashanah (Rosh Hashanah 11a:16, Bereshit Rabbah 73:1 — recorded, UNEXERCISED: born:joseph
is the tape's by 41:46 and 47:9)}; wage_changes_count {ten (the ink, 31:7, 31:41), a_hundred (Bereshit Rabbah 74:3, 74:11
the rabbis' — unexercised)}; labans_pursuit {seven_days_distance (the ink 31:23), one_day (Bereshit Rabbah 74:6 —
unexercised)}. Every row with its arms visible; the running arm named RUNNING.

### 7g. The markers (the stitcher's table; every number parsed from the ink and re-verified at run time)
'Gen 18:10' F at 18:1 — M['mamre'] = the Passover of the year before born:isaac (cal_day(yr(born:isaac) - 1, 1, 15); the
row mamre_visit_date; the ink's "at this season" carries no number: assert_ink [] and the phrase named); 'Gen 19:15' F
[1 day] — dawn of the next day, M['sodom_dawn'] = mamre + 1 (19:1 "at evening", 19:15 "when the dawn rose", 19:23 "the
sun had risen"); 'Gen 22:1' F — READING-PLACED: M['binding'] = year_day(yr(born:isaac) + 37) (the row binding_placement;
Sarah 90 at his birth 17:17, 127 at 23:1 — 37 by the ink, the placement the shelf's); 'Gen 22:4' F ordinal [3] —
M['moriah_seen'] = binding + 2 (the third day, inclusive); 'Gen 25:29' F — READING-PLACED: M['stew_day'] = died:abraham
(the proleptic 25:7's day; the row stew_day; Bava Batra 16b:11); 'Gen 27:1' F — READING-PLACED: M['blessing'] =
year_day(yr(born:jacob) + 63) (the row blessing_placement; Bereshit Rabbah 68:5); 'Gen 28:9' F — M['mahalath'] =
died:ishmael (the proleptic 25:17's day: born:ishmael + 137 — the ink's; Megillah 17a:5's inference that Ishmael had
died); 'Gen 28:10' F — READING-PLACED: M['departure'] = add(died:ishmael, 14, 'year') (the row hidden_years; Megillah
17a:5-6 "hidden fourteen years in the house of Eber"); 'Gen 29:14' F — M['laban_month'] = add(departure, 1, 'month')
(the journey's days absorbed into the bound, said so; assert_ink [] at 29:14 — "a month of days" carries no numeral);
'Gen 29:20' F [7] — M['wedding'] = add(laban_month, 7, 'year') — the first timer's fire day; 'Gen 29:28' F [7] —
M['rachel_given'] = wedding + 7 (the week's end); 'Gen 29:30' F [7] at 30:25 — M['fourteen_end'] = add(rachel_given, 7,
'year') — the second timer's fire day, placed at 30:25 where the ink says "when Rachel had borne Joseph"; born:joseph
STANDS as the tape's (41:46, 45:6, 47:9 — 7h's join); 'Gen 31:41' F [6] at 31:17 — M['flight'] = add(fourteen_end, 6,
'year'); 'Gen 31:22' F ordinal [3] — M['told'] = flight + 2. The deaths 25:7 and 25:17 and the ages 25:20, 25:26, 26:34
STAND (S1's rows). THE RETROGRADE FORM: none in this stretch — every reading-placed date lies FORWARD of the counter,
so the placement is a forward marker with its teacher named, THE TIME CONSENSUS's (T2) class reading_placed avant la
lettre (the class field itself is T2's sitting).

### 7h. The checkpoints (the sequence runner; declared by the text or the shelf, computed by the engine)
CH0 THE SEASON'S JOIN — the one-year timer set at the visit (placed on Passover of 2048 by Bereshit Rabbah 48:12) fires
on born:isaac's day (placed on Passover of 2049 by Rosh Hashanah 10b:10): two shelf rows joined by the ink's own "at this
season" (18:10, 18:14, 21:2) — MATCH expected, NOT by construction (the two placements are independent rows). CH1 THE
TEN TRIALS — Mishnah Avot 5:3's ten against the ledger: the ink names ONE trial (22:1's verb), the shelf calls it the
tenth (Bereshit Rabbah 56:11) but lists no ten on the local shelf — DIVERGE expected, filed OPEN as the missing shelf
(Avot de-Rabbi Natan is not local). CH2 THE STEW DAY — Abraham dies when the twins are fifteen: died:abraham -
born:jacob = 15 years by the ink's three numbers (25:7, 21:5, 25:26) — MATCH expected. CH3 JACOB SIXTY-THREE AT
ISHMAEL'S DEATH — died:ishmael - born:jacob = 63 years by the ink (16:16, 25:17, 25:26) against Bereshit Rabbah 68:5's
sixty-three at the blessing — MATCH expected, a JOIN (the shelf's number, the ink's arithmetic). CH4 THE FOURTEEN'S END
IS JOSEPH'S BIRTH YEAR — yr(fourteen_end) == yr(born:joseph): the departure placed from Ishmael's side (25:17 + Megillah
17a's fourteen) and Joseph's birth placed from Pharaoh's side (41:46, 45:6, 47:9) meet at 2200 — MATCH expected, a JOIN
of two independent chains. CH5 MARRIED AT EIGHTY-FOUR — yr(wedding) - yr(born:jacob) = 84 against Bereshit Rabbah 68:5
— MATCH expected (a join). CH6 ESAU'S FORTY IS ISAAC'S HUNDRED — yr(age:esau:40) - yr(born:isaac) = 100 by the ink
(26:34, 25:26) — MATCH expected. CH7 THE WEEK BEFORE RACHEL — the seven-day timer of 29:27 fires before wife_taken
rachel on the tape — MATCH expected. CH8 THE EIGHTH DAYS — circumcision_due timers set on the stretch's births =
thirteen (the twins and the eleven sons), none on Dinah — MATCH expected (the male check). CH9 THE PROMISES CLOSED IN
THIS STRETCH — entries opened by S2 and the pre-Sinai engine and closed by this stretch's ink: buried_in_peace (15:15
at 25:8), seed_multiplied (16:10 at 25:16), son_promised_at_the_season (18:10 at 21:2 — opened here, closed on the
pre-Sinai engine's event), with_you_promised (28:15 at 31:5) — four closes performed — MATCH expected. CH10 SUPPLANTED
TWICE — the ledger's transfers on Jacob from Esau = two (25:33, 27:27) against 27:36's "these two times" — MATCH expected.

### 7i. The scene (the runner's own bare world; the rows in the text's order; the tuple predicted by a hand-model
### BEFORE the runner is typed — scratchpad o8_s3_predict.py — with the OP CLASS of every effect from the registry and
### the WRITE TIME of every timer: the two seven-year timers and the week fire inside the scene (its days walk past
### them), the thirteen eighth-day timers fire seven days after each birth, the one-year timer of 18:10 fires inside the
### scene too (the scene's day count passes it) but finds no born:isaac to close son_promised (the bare scene has no
### pre-Sinai birth), so the entry stays OPEN and the model counts it so)
The scene's days: 18:1 day 1; 19:1 evening day 1; 19:15 day 2; then the bare scene walks by whole years between the
undated stretches (the reading-placed markers are the tape's; the bare scene advances by the ink's numbers where it has
them — the third day 22:4, the month 29:14, the seven years 29:20, the week 29:28, the seven years 29:30, the six 31:41,
the third day 31:22 — and by one day elsewhere); the tuple's slots: the effect slots per (subject, effect) in the text's
order, then opens, timers set, fired, closes, the day. The scene's kind count, effect-slot count and the tuple are the
model's print, typed after.

### 7j. The answer sheet and the shelf the cells read
Mishnah rows verified by their own tokens: Bava Kamma 8:7 (the forgiveness rule from 20:7 and 20:17), Avot 5:3 (the ten
trials), Bava Metzia 7:8 (the four keepers), Bava Batra 8:5 (the firstborn's portion and the father's word), Bekhorot
8:1 (the firstborn for inheritance — the first to come out), Moed Katan 1:7 (no marriage on the festival — the joy
rule), Sanhedrin 10:3 (Sodom's men, S2's row executed). The Babylonian rows (file index 2*daf-2, +1 for b): Megillah
17a:5, 17a:6; Yevamot 64a:6; Yoma 28b:10; Kiddushin 82a:10; Bava Batra 16b:11, 16b:12; Bava Kamma 92a:4, 92a:16; Bava
Metzia 93b:3, 86b:3, 86b:7; Shabbat 127a:13; Sanhedrin 89b:8, 89b:9, 89b:14, 91a:16, 109a:8; Moed Katan 8b:9, 9a:4;
Chullin 91b:8; Rosh Hashanah 10b:10, 11a:2, 11a:16, 16a:16; Berakhot 6b:8, 26b:4, 26b:5, 26b:14; Ketubot 50a:3. The
Genesis spine's rows (Bereshit Rabbah, BR[par-1][row-1]): 48:12, 49:6, 49:8, 49:9, 49:12, 50:4, 51:5, 55:1, 56:9, 56:11,
58:5, 61:4, 62:1, 64:3, 64:6, 65:1, 65:14, 68:5, 68:10, 68:11, 70:7, 70:19, 72:2, 72:3, 72:5, 73:1, 74:3, 74:4, 74:5, 74:6,
74:9, 74:11 — every one located by script this sitting (scratchpad o8_shelf_s3 prints); Onkelos only from the units'
own notes (no Onkelos file on the shelf). NOT on the local shelf, named as absent: Avot de-Rabbi Natan (the ten trials'
list), Seder Olam (the ages), the Jerusalem Talmud (the wedding week's own seat).

### 7k. The edits to standing files (each with its check)
cold_run_primeval.py — law_primeval's shared branches narrowed from `if gen` to Genesis 2-16 (named, journeyed,
lord_descended, believed, fled, begot, bore, remembered, sent_away, famine_came, sister_asked, woman_taken,
altar_erected, called_on_the_name, olah_offered, barren, anger_burned, return_commanded, appeared, and married's upper
bound kept): the runner's own 206/206 unmoved, the sequence tape's double writes unchanged. cold_run_pre_sinai.py —
law_pre_sinai's `born` branch reads event.get('sex', 'm') == 'm' before writing circumcision_due (17:12 "every male"):
its own 212/212 unmoved; Dinah's birth on the tape sets no timer (CH8). cold_run_family.py — its gifts_given branch (24:53)
seat-checked to Gen 24 if it is not. cold_run_exodus_story.py — its pursued and decree_issued branches seat-checked to
Exodus if they are not (31:23, 26:11 would reach them). The stitcher: CLOCK_DAY_RUNNERS + 'mamre'; SPAN_ORDER
['pre_sinai', 'primeval', 'mamre', 'family', ...]; the thirteen rows of 7g; the DAYS key list extended. The sequence runner:
`import cold_run_mamre` after cold_run_primeval; DAEMON_ORDER + ('cold_run_mamre', 'law_mamre') ("ALL 42 DAEMONS");
CH0-CH10 before `verdicts`; VERDICTS extended; CENSUS, DAYS (+13 keys), RUN typed from the stitcher's print and the
first run, the RUN tuple READ BY SCRIPT before typing (S2's rule). daemon_dispositions.yaml: law_mamre with
installed_by absent (T1 is Numbers' sitting), the functions block `mamre:` seventeen cells. dependency_dispositions.yaml:
the span, the edges the census emits (CALL pre_sinai, offerings, temurah, family, mishpatim; FALSE the homographs the
tokens raise — the guilt of 26:10, the death formula of 26:11 in a king's mouth, the matzot of 19:3, the fine flour of
18:6, the oil of 28:18, the affliction of 31:50; the rest as the census names them), the registration edge sequence →
mamre. event_vocabulary.yaml, effect_vocabulary.yaml, calendar_parameters.yaml (+8 rows), entity_registry.yaml as 7b,
7c, 7f, 7e.

### 7l. The order of work (the wrap's rhythm, as 4l and 6l)
(1) this section; (2) the effects by script with the CLAIMS list verified — the NEW list checked against the registry
first; (3) the types by script, the events lint 0; (4) the calendar rows and the registry; (5) the daemon declared in
daemon_dispositions.yaml and the gate run to FAIL on the missing def; (6) the span on a stub and the census --emit, the
edges dispositioned; (7) the hand-model printed; (8) the code — the two shared-branch edits of 7k first, fix_percent,
then cold_run_mamre.py; (9) the run; (10) the recorder and the stitcher (the thirteen rows); the sequence runner's
literals; the sequence run; CH0-CH10 read; the RUN tuple read by script, then typed; (11) the gates, the probes, the
sweep, the corpus regression; (12) the records: 7n AS RUN, the report's third sitting, COMPILE_DEBT, THE_STEPS if a
convention is proven, THE_BRIEFING, the state doc, memory; a compaction point.

### 7m. OPEN at this sitting
The ten trials' list (CH1's missing shelf). The binding's year (37 by the running reading; the page-order arm
unexercised — T2's field will carry the class). The tape's born:joseph and Rachel's remembering on Rosh Hashanah (the
row recorded, unexercised). The thief's identity as the machine's knowledge against Jacob's ignorance (31:32 — the
ledger writes what the narrator wrote at 31:19). The kill intent of 27:41, the few days of 27:44, Esau's yoke of 27:40,
the two nations of 25:23 — entries the three books never close. Lot's daughters' and Nahor's births as `bore`/`begot`
under a covenant that does not bind them — the naming stand-in for installation (T1).

### 7n. AS RUN (2026-09-08; the account: REPORT_NARRATIVE_GAPS.md, the third sitting)
The order held: the effects (454 → 681 — 215 new, eleven more the types named and the effects script had omitted, the
season's return timer; twenty-eight reused with their ink lines extended; every count claim through the CLAIMS list and
verified by script — two claims REFUTED on the dry run and corrected beside their record, two runs misspelled, twelve
glosses refused for a semicolon), the types (445 → 624 — 179 new, twenty-four standing kinds extended; the events lint's
fourteen flags: five shared witnesses resolved, the nine omitted effects appended), eight calendar rows, the registry
(168 → 214 entities; the JOIN targets named by corpus ids mapped to the yaml's own or made NEW), the daemon declared and
the gate run to FAIL — the block first landed under `functions:` (law_primeval had been the last daemon) and was moved
above it. The span on a stub and the census --emit: fourteen edges, twelve pointers and the registration edge
dispositioned. The hand-model printed (362 slots) and MATCHED on the first graded run: 222/222 (pure ink 127 / recorded
moves 74 / answer-sheet 7 / data 6 / imports 8 / hypotheses 0). Two small lessons before the run: a roster name's probe
takes the verse's own form (the conjunction prefix ו "and" where the ink joins the names of 25:13); a scene field named
`day` is the engine's own word for the event's dated day — the two ordinals are `ordinal`. The recorder: 306 history
events. The stitcher, three honest stops: INK MISMATCH at 28:10 — the parser counts Beersheba's seven (באר שבע "the well
of the seven", 21:28-31), a place-name's numeral, recorded in the row's nums with its note; the visit's row read
born:isaac before 21:2 had set it — the year is 17:1's ninety-nine, on the tape before 18:1; and 18:1's "and the LORD
appeared" (וירא, the passive stem) was a REGISTER-OFF: the test's verb regex read lowercase stems only, and the passive,
intensive-passive and causative-passive codes are uppercase — fixed for every runner, no other event moved. Then 109
markers (92 forward / 15 proleptic / 2 retrograde), 749 events on the tape, 56 closes, 444 kinds. The sequence runner:
CH0-CH10 exactly as 7h expected on the first run (CH1 DIVERGE, the ten trials against the ink's one); C9 DIVERGED at the
day grain — the binding now sits in Sarah's death year and the purchase's bound opens at 22:4, two days into it, while
her death is modeled at the year's first day — and is compared at the YEAR grain (the time consensus's T3 rendering rule,
arriving early). THE RUN TUPLE READ BY SCRIPT forced two fixes before it was typed: (i) the first tape run wrote 909, two
more than the bare scene's 385 over S2's 522 — law_mamre's span check was a RANGE and let 21:2's birth and 23:19's
burial through, the pre-Sinai and family engines' events; the span is a SET with holes now; (ii) THE REST — the tape
minus the Mamre lines run as its own world — counted 165 entities against S2's 166 with every other count equal: a write
had MOVED, because the registry map is GLOBAL and the scene's generic tokens 'the-land' (26:1) and 'the-ram' (22:13)
re-homed the erection's land (high places banned) and Leviticus 9's ram onto the Genesis entities; the tokens are
the-land-of-canaan and the-ram-at-moriah, and the sequence runner now carries THE REST as its eighth checkpoint
(NEWEST_RUNNER and PREVIOUS_RUN, moved forward each sitting). Typed (749, 31, 27, 0, 0, 907, 11, 219, the two mornings,
56); 8/8. The census literal's subjects 199 → 198 after the token fix (the two generic tokens had been Mamre's alone as
event subjects; the-land-of-canaan was already a tape subject). The daemon gate at the close caught twenty-one kinds
DRIFTED between the first declaration (the types script's per-kind defaults) and the code (the hand-model's per-event
tables — the namings moved to their own `named` events, `barren` written under prayed and womb_opened, the week's
fulfillment writing nothing, the second seven owed at the demand): the watches re-declared from the model, the drift
list in the report; 42 daemons, 304 functions, 0 owed. The census after: Genesis 14 units / 461 verses still uncovered,
in two stretches (33-37, 39-47) — S4 as sized; Exodus 23:20-33 the one narrative unit outside every scene. The gates,
the probes, the sweep and the corpus regression: the report's closing section.

## 8. S4 — GENESIS 32-37, 39-47, 50 FROM THE FORD TO THE COFFIN: THE DECLARATION (2026-09-08, the sitting after O8 S3 in
## the same window; the owner: "Next"; declared whole BEFORE its code, as sections 4, 6 and 7 were)

### 8a. The span, the runner, the daemon
The span `joseph`: Genesis 32:1-33:20, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50:1-26 — the fourteen frozen
units the census lists as the two last Genesis stretches (gen_56 blessing_returned, gen_57 deceit_at_the_gate, gen_58
israel_written, gen_59 edom_ledger, gen_60 dreamer_sold, gen_62 potifar_house, gen_63 two_dreams_prison, gen_64
pharaoh_dreams_rise, gen_65 first_descent, gen_66 second_descent, gen_67 cup_and_surety, gen_68 i_am_yosef, gen_69
descent_seventy, gen_70 goshen_and_the_fifth: 461 verses) PLUS two stretches the census's coverage test hid — gen_55 (32:1-33,
the night at the Jabbok: covered only by the family engine's two seats, the renaming at 32:29 and the sinew statute at 32:33)
and gen_73 (50:1-26, the coffin: covered only by the family engine's burial at 50:12-13) — 59 verses more, 520 in all. Cut
out, as S3 cut 21, 23, 24: Genesis 38 (the family engine's), 48 and 49 (its adoption, crossing, testament, burial command),
and the family's own seats INSIDE the span (32:29 `renamed`, 32:33 `sinew_barred`, 50:12-13 `buried` with its close) — the
story scene submits the acts around them and never those. THE SPAN IS A SET (convention 20): the chapters 32-37, 39-47, 50,
and the shared kinds at the family's seats are the family's by the seat checks of 8k. The runner cold_run_joseph.py,
twenty-three cells in the text's order (jabbok, esau_met, shechem_arrival, dinah, bethel_again, three_deaths, edom,
dreamer, potiphar, prison_dreams, pharaoh_dreams, the_rise, first_descent, second_descent, cup, i_am_joseph, the_seventy,
goshen, the_fifth, the_oath, mourning, coffin, and the census cell over 46:8-27), each a bare-world unit; the callee imports
where the text reaches: the pre-Sinai code (the covenant's eighth day on Benjamin, Manasseh and Ephraim — the scene's laws
carry law_pre_sinai beside the story's, as S1 and S3), the offerings (46:1's sacrifices as 31:54's, the peace offering's
shape — Bereshit Rabbah 94:5; 35:14's libation by the token of the drink offering), the family engine (33:19's purchase by
its `purchased` kind, seat-checked; 47:29's burial command by its kind, seat-checked; the census of 46:8-27 against its
inheritance order — the firstborn Reuben kept at 46:8), the ordinances (THE MOHAR: 34:12's "multiply upon me bride-price
and gift" against the seducer's fixed mohar of Exodus 22:15-16 — the compiled function of cold_run_mishpatim_2, read by
call; THE THIEF SOLD: the three verdicts of 44:9, 44:10, 44:17 against Exodus 22:2's "sold for his theft" — the compiled
function of cold_run_mishpatim_3), the vestments (37:31's dipped tunic as the source of the tunic's atonement for
bloodshed — Arakhin 16a:13, Zevachim 88b:6: the flow reversed, a narrative verse feeding a law's row), the leaven
machine (44:12's "he searched ... and found" as the source of the search for leaven — Pesachim 7b:14 on Mishnah Pesachim
1:1: the flow reversed again). The daemon law_joseph, the FORTY-THIRD. The scene on a bare world with w.laws =
[law_joseph, law_pre_sinai]: three male births under the covenant (35:18, 41:50-52), each with the eighth-day timer.

### 8b. The types (event_vocabulary.yaml; NEW unless marked; witnesses cut from the verses' consonants by script and
### checked against the Tanakh DB before the append; the form by the register test; digits never in a name)
REUSED kinds, their witness lines extended: named (32:3 Mahanaim, 32:31 Peniel, 33:17 Sukkot, 33:20 the altar's name,
35:7 El-Bethel, 35:8 Allon-bachuth, 35:10 Israel by the formula, 35:15 Bethel, 35:18 Ben-oni and Benjamin, 41:45
Zaphenath-paneah, 41:51 Manasseh, 41:52 Ephraim, 50:11 Abel-mizraim — fourteen seats); appeared (35:9); born (35:18
Benjamin, 41:50-52 Manasseh and Ephraim — sex m, under the covenant); bore (36:4-5 Esau's wives, 36:12 Timna); married
(36:2-3 the three wives, 41:45 Asenath); died (35:8 Deborah, 35:19 Rachel, 35:29 Isaac, 50:26 Joseph); buried (35:8, 35:19,
35:29 — the family's seats 23, 48-50 untouched); journeyed (32:1, 33:16, 33:17, 33:18, 35:5, 35:16, 35:21, 35:27, 37:12,
37:17, 42:26, 45:25, 46:1, 46:5-6, 46:28, 50:7-9, 50:14); river_crossed (32:23-24 the Jabbok); prayed (32:10-13);
embraced, kissed, wept (33:4; 45:14-15; 46:29; 50:1; 50:17; 37:35; 42:24; 43:30; 45:2); rebuked (34:30; 37:10); envied
(37:11); loved_apart (37:3); anger_burned (39:19); fled (39:12-15); dreamed (37:5, 37:9, 40:5, 41:1-4, 41:5-7); feast_made
(40:20, 43:16-34); restored (40:21); counsel_given (41:33-36); famine_came (41:54); sent_away (44:3, 45:24); pursued
(44:4-6); bound (42:24 Simeon); ate_and_drank (43:34); gifts_given (45:22-23); silver_given (45:22); sacrificed (46:1);
blessed (47:7, 47:10); dwelt (50:22); sworn (47:31, 50:25); burial_commanded (47:29-30 — the family's kind, seat-checked
both ways by 8k); purchased (33:19 the field, 47:20 the ground of Egypt — the family's kind, seat-checked); altar_erected
(33:20, 35:7); pillar_set_and_anointed (35:14 — libation and oil); blessed_be_fruitful (35:11 — the S2 kind, singular);
land_promised (35:12 — the S2 kind); statute_set (47:26 — the exodus story's kind at Marah, seat-checked both ways).
NEW kinds (act unless [speech]): angels_met (32:2), messengers_sent (32:4-6), feared_greatly (32:8-9), gift_prepared
(32:14-22 — the droves' counts as the value), wrestled (32:25-26), blessing_demanded [speech] (32:27), name_asked [speech]
(32:30), sun_rose (32:32 — limping), esau_seen (33:1), children_divided (33:2), bowed (33:3 seven times; 33:6-7; 37:7
the sheaves; 42:6; 43:26; 43:28; 44:14; 47:31; 50:18 — the form as the value, Berakhot 34b:3's three), fell_on_the_neck
(33:4; 45:14; 46:29; 50:1 the face), children_declared [speech] (33:5), camp_explained [speech] (33:8-9), gift_urged
[speech] (33:10-11 — the returned word, and he took), convoy_declined [speech] (33:12-15), booths_made (33:17),
went_out_to_see (34:1), seized_and_violated (34:2), soul_cleaved (34:3), wife_asked [speech] (34:4), silence_kept (34:5),
came_to_speak (34:6), outraged (34:7), marriage_proposed [speech] (34:8-12), deceit_answered [speech] (34:13-17),
terms_accepted (34:18-19), gate_addressed [speech] (34:20-23), males_circumcised (34:24), city_struck (34:25-26),
city_plundered (34:27-29), answered_back [speech] (34:31), altar_commanded [speech] (35:1), purge_commanded [speech]
(35:2-3), gods_hidden (35:4), god_went_up (35:13), hard_birth (35:16-17), grave_pillar_set (35:20), lay_with_the_concubine
(35:22), sons_counted (35:22-26), withdrew (36:6-8), roster_listed (36:9-19; 36:20-30; 36:40-43), reigned (36:32),
reign_passed (36:33-39 — seven), evil_report_brought (37:2), coat_made (37:3), hated (37:4, 37:5, 37:8), dream_told [speech]
(37:6-7; 37:9-10; 40:9-11; 40:16-17; 41:17-24), errand_given [speech] (37:13-14), found_wandering (37:15-17), conspired
(37:18), plot_spoken [speech] (37:19-20), rescue_urged [speech] (37:21-22), stripped (37:23), cast_into_the_pit (37:24),
caravan_seen (37:25), sale_proposed [speech] (37:26-27), sold (37:28; 37:36), pit_found_empty (37:29-30), coat_dipped
(37:31-32), coat_recognized (37:33), mourned (37:34-35; 50:10), slave_bought (39:1), prospered (39:2-3),
appointed_over_the_house (39:4-6; 39:22-23), lie_with_me_demanded [speech] (39:7; 39:12), refused [speech] (39:8-10),
garment_seized (39:12), accused [speech] (39:14-18), imprisoned (39:20; 40:3), kindness_extended (39:21), offended (40:1-2),
appointed_to_serve (40:4), faces_downcast (40:6-8), interpreted [speech] (40:12-13; 40:18-19; 41:25-32),
remembrance_asked [speech] (40:14-15), hanged (40:22), forgot (40:23), spirit_troubled (41:8), offenses_recalled [speech]
(41:9-13), rushed_from_the_pit (41:14), counsel_accepted (41:37-39), set_over_egypt (41:40-44), went_out_over_egypt
(41:45-46), food_gathered (41:47-49), plenty_ended (41:53), cried_for_bread (41:55; 47:15), storehouses_opened (41:56-57),
descent_commanded [speech] (42:1-2; 43:2), went_down (42:3; 43:15), benjamin_withheld (42:4), brothers_recognized (42:7-8),
dreams_remembered (42:9), spies_charged [speech] (42:9, 42:12, 42:14), honesty_pleaded [speech] (42:10-11, 42:13), test_set
[speech] (42:15-16), custody_three_days (42:17), plan_revised [speech] (42:18-20), guilt_confessed [speech] (42:21-22;
44:16), interpreter_between (42:23), silver_returned (42:25), silver_found (42:27-28; 42:35), report_given [speech]
(42:29-34), bereaved_cried [speech] (42:36), pledge_of_sons_offered [speech] (42:37), descent_refused [speech] (42:38),
warning_cited [speech] (43:3-7), surety_offered [speech] (43:8-10), caravan_planned [speech] (43:11-14), house_ordered
[speech] (43:16-17), feared_at_the_door [speech] (43:18-22), peace_given [speech] (43:23), feet_washed (43:24),
gift_presented (43:25-26), welfare_asked [speech] (43:27-28), benjamin_seen (43:29), bread_set (43:31-32),
seated_by_birth_order (43:33), portions_lifted (43:34), cup_planted (44:1-2), theft_denied [speech] (44:7-8),
rash_sentence_offered [speech] (44:9), ruling_softened [speech] (44:10), bags_searched (44:11-12), tore_garments (37:29;
37:34; 44:13), divination_claimed [speech] (44:5; 44:15), ruling_given [speech] (44:17), judah_pleaded [speech] (44:18-34),
restraint_failed (45:1), identity_revealed [speech] (45:3-4), providence_declared [speech] (45:5-8), descent_urged [speech]
(45:9-13), voice_heard (45:16), come_to_me_commanded [speech] (45:17-20), wagons_given (45:21), told_joseph_lives [speech]
(45:26), wagons_seen (45:27), resolved_to_go [speech] (45:28), night_vision [speech] (46:2-4), census_listed (46:8-27),
judah_sent_ahead (46:28), let_me_die_said [speech] (46:30), audience_prepared [speech] (46:31-34), told_pharaoh [speech]
(47:1), five_presented (47:2), work_asked [speech] (47:3-4), goshen_granted [speech] (47:5-6), stood_before_pharaoh (47:7),
days_asked [speech] (47:8-9), settled (47:11), sustained (47:12; 50:21), silver_gathered (47:14), livestock_taken_for_bread
(47:16-17), second_year_came (47:18-19), people_moved (47:21), priests_exempted (47:22), seed_given [speech] (47:23-24),
servitude_accepted [speech] (47:25), fruitful_in_goshen (47:27), embalmed (50:2-3), leave_asked [speech] (50:4-5),
leave_granted [speech] (50:6), feared_joseph [speech] (50:15), forgiveness_asked [speech] (50:16-17), forgave [speech]
(50:19-21), grandsons_seen (50:23), visitation_promised [speech] (50:24). The count is the script's (about a hundred and
seventy new); the NEW list is checked against the registry before the append, and no kind of the family engine's is
reused where its branch carries no seat check (recognized, consented, gathered — 8k).

### 8c. The effects (effect_vocabulary.yaml; NEW unless marked; each ink claim verified by script before the append;
### the `he` quoted from the verse by the run's own index; the op class named for the hand-model)
REUSED, their ink lines extended: name_given [st] (the fourteen seats), wife_taken [st] (36:2-3, 41:45), encamped_at [st]
(32:1 Mahanaim, 33:17 Sukkot, 33:18 Shechem, 35:6 Luz, 35:21 Migdal-eder, 35:27 Hebron, 37:17 Dothan, 46:1 Beersheba,
46:28 Goshen, 47:11 Rameses, 50:10 Atad), river_crossed [st] (32:23), kissed_and_wept [st] (33:4 — the dotted kiss),
wept [st] (37:35, 42:24, 43:30, 45:2, 45:14-15, 46:29, 50:1, 50:17), loved_by_the_father [st] (37:3), envied [st] (37:11),
begotten [st] (36:4-5, 36:12), altar_built [st] (33:20, 35:7), pillar_anointed [st] (35:14), blessed_by_the_lord [st]
(35:9), fruitfulness_blessed [he] (35:11), land_promised [he] (35:12), return_promised [he] (28:15 — CLOSED at 35:6 by the
ink's own arrival "and Jacob came to Luz, that is Bethel"), vow_of_bethel [de] (28:20-22 — CLOSED at 35:7, the altar built
where the vow was made; Bereshit Rabbah 81:1-2 read the delay as punished — the reading recorded, the close at the ink's
own act), field_acquired [tr] (33:19 — by the family's effect at Jacob's seat, a hundred kesitah), fled_from_the_mistress
[st] — NOT reused (that is Hagar's), fear_not_promised [he] (46:3), great_nation_promised [he] (46:3), dwelling_granted
[st] (47:6), comforted [st] (50:21), sacrifice_offered [st] (46:1), oath_sworn [st] (47:31, 50:25), sent_out [tr] (44:3,
45:24), gifts_given [tr] (45:22-23), famine [st] (41:54 all the lands, 43:1, 47:13), feast_made [st] (40:20, 43:34),
parted [st] (36:6 Esau from before Jacob), slain_by_sword [bo] (34:25-26 the males of Shechem), gathered_to_his_people
[st] (35:29), circumcision_due [de] — written by law_pre_sinai on the three births; seed_as_dust, seed_as_stars, tithe_vowed
untouched (the tithe never narrated as paid: Bereshit Rabbah 70:7's Levi named, no close); kill_intent_after_the_mourning
[he] (27:41) — OPEN through 35:29's burial by Esau and Jacob together: the condition arrived and nothing followed (8h);
few_days_promised [he] (27:44) — OPEN forever: Rebekah's death is never narrated (Bereshit Rabbah 81:5 reads it under
35:8's "oak of weeping" — recorded on the entity).
NEW effects, by cell (op in brackets; subject; the seat): jabbok — camp_of_god_seen [st jacob 32:2-3], esau_approaching [st
jacob 32:7 — four hundred men], two_camps_made [st jacob 32:8-9], deliverance_prayed [st jacob 32:10-13 — 'deliver me
from the hand of my brother'], gift_sent_ahead [tr esau cp jacob 32:14-22 — the droves' five hundred and fifty counted from
the verse's numbers, a measurement], thigh_dislocated [bo jacob 32:26], blessing_demanded [st jacob 32:27], blessed_at_the_ford
[st jacob 32:30], limping [st jacob 32:32]. esau_met — children_divided [st jacob 33:2], bowed_seven_times [st jacob 33:3],
gift_declined [st esau 33:9], blessing_returned [tr esau cp jacob 33:11 — 'take, please, my blessing ... and he took': the
27:36 theft-cry's verb and noun with the roles exchanged, the frozen unit's crown], seir_promised [he jacob 33:14 — 'until I
come to my lord to Seir': OPEN forever, Avodah Zarah 25b:8, Bereshit Rabbah 78:14], convoy_declined [st jacob 33:15],
booths_made [st jacob 33:17], came_whole [st jacob 33:18 — Bereshit Rabbah 79:5 whole in body, money, Torah]. dinah —
violated [bo dinah 34:2], defiled [st dinah 34:5, 34:13, 34:27], marriage_demanded [st shechem 34:4], silence_kept [st
jacob 34:5], outrage_in_israel [st the_sons 34:7 — the outrage word's two Torah tokens, here and Deut 22:21, measured],
intermarriage_proposed [st hamor 34:8-10], mohar_offered_unbounded [st shechem 34:12 — the ordinances' fixed mohar by
call], circumcision_conditioned [st the_sons 34:15-17 — 'with deceit' 34:13], terms_accepted [st hamor 34:18-19],
city_persuaded [st the_men_of_shechem 34:20-24], circumcised_by_the_condition [st the_men_of_shechem 34:24 — not the
covenant's sign], hamor_and_shechem_slain [bo hamor, shechem 34:26], dinah_taken_back [tr dinah 34:26], spoil_taken [tr
the_sons 34:27-29], troubled_charged [st simeon, levi 34:30], question_unanswered [st the_sons 34:31]. bethel_again —
ascent_to_bethel_owed [de jacob 35:1 — CLOSED 35:6], altar_owed [de jacob 35:1 — CLOSED 35:7], foreign_gods_removal_owed
[de the_house_of_jacob 35:2 — CLOSED 35:4], foreign_gods_buried [st jacob 35:4], terror_of_god [st the_cities 35:5],
kings_promised [he jacob 35:11], assembly_of_nations_promised [he jacob 35:11], libation_poured [st the_pillar_of_bethel
35:14 — the drink offering's token, the offerings engine by reference]. three_deaths — nurse_died [st deborah 35:8],
midwife_comforted [st rachel 35:17], died_in_childbirth [st rachel 35:18-19], grave_marked [st the_grave_of_rachel 35:20 —
'to this day'], concubine_lain_with [st reuben 35:22 — the value read_not_translated: Mishnah Megillah 4:10], israel_heard
[st jacob 35:22], twelve_sons_listed [st jacob 35:22-26 — twelve], full_of_days [st isaac 35:29], buried_by_both_sons [st
isaac 35:29]. edom — dwelt_in_seir [st esau 36:8], sons_of_esau_listed [st the_chiefs_of_esau 36:9-19], horites_listed [st
the_sons-of-seir 36:20-30 — Bava Batra 115b:4's two Anas recorded], reigned_in_edom [st the_kings_of_edom 36:31-39 — eight
reigns counted before a king reigned for Israel], chiefs_by_places_listed [st the_chiefs_of_esau 36:40-43]. dreamer —
evil_report_brought [st joseph 37:2], coat_of_stripes_made [st joseph 37:3], hated [st the_sons 37:4, 37:5, 37:8],
dream_of_sheaves [st joseph 37:7], dream_of_sun_moon_stars [st joseph 37:9], word_kept [st jacob 37:11], errand_given [st
joseph 37:13-14], found_wandering [st joseph 37:15-17], conspired_to_kill [st the_sons 37:18-20], rescue_urged [st reuben
37:21-22], stripped_of_the_coat [st joseph 37:23], in_the_pit [bo joseph 37:24 — 'no water in it', Chagigah 3a:14],
sale_proposed [st judah 37:26-27], sold_into_egypt [tr joseph cp the_sons 37:28 — twenty silver; the seller UNCERTAIN in
the ink's grammar, certain in Joseph's mouth at 45:4: the counterparty follows Joseph's word, the note on the entity],
garments_torn [st reuben 37:29, jacob 37:34, the_sons 44:13], coat_dipped [st the_sons 37:31], coat_recognized [st jacob
37:33 — 'an evil beast devoured him': the planned lie of 37:20 spoken by the father], mourned_many_days [st jacob 37:34-35],
comfort_refused [st jacob 37:35], sold_to_potiphar [tr joseph cp the_medanites 37:36]. potiphar — bought_by_potiphar [tr
joseph cp potiphar 39:1], prospering [st joseph 39:2-3], appointed_over_the_house [st joseph 39:4], house_blessed_for_joseph
[st the_house_of_potiphar 39:5 — Berakhot 42a:8], lie_with_me_demanded [st potiphars_wife 39:7, 39:12], refused [st joseph
39:8-10 — Yoma 35b:12], garment_left [st potiphars_wife 39:12-16], fled_outside [st joseph 39:12], accused_falsely [st joseph
39:14-18], imprisoned [bo joseph 39:20], favor_in_the_keepers_eyes [st joseph 39:21], appointed_over_the_prisoners [st
joseph 39:22]. prison_dreams — offended_the_king [st the_cupbearer, the_baker 40:1], in_custody [bo the_cupbearer, the_baker
40:3], appointed_to_serve [st joseph 40:4], dreams_in_one_night [st the_cupbearer, the_baker 40:5], faces_downcast [st
the_cupbearer, the_baker 40:6-7], interpretation_given [st joseph 40:12-13, 40:18-19], head_lifted_up_due [ti the_cupbearer
40:13 — due three days: FIRES at the birthday 40:20], head_lifted_off_due [ti the_baker 40:19 — due three days: FIRES
40:20], remembrance_asked [st joseph 40:14-15 — 'stolen, I was stolen'], restored_to_the_cup [st the_cupbearer 40:21],
hanged [bo the_baker 40:22], petition_forgotten [st the_cupbearer 40:23]. pharaoh_dreams — pharaohs_dream_doubled [st
pharaoh_of_joseph 41:1-7], spirit_troubled [st pharaoh_of_joseph 41:8], no_interpreter [st the_magicians 41:8],
offenses_recalled [st the_cupbearer 41:9-13], rushed_from_the_pit [st joseph 41:14], not_i_god [st joseph 41:16], one_dream
[st pharaoh_of_joseph 41:25-32 — seven and seven], counsel_of_the_fifth [st joseph 41:33-36 — the fifth in the plenty
years, the food a deposit: the deposit's token FALSE for the guardians, a figure]. the_rise — counsel_accepted [st
pharaoh_of_joseph 41:37-39], set_over_the_house [st joseph 41:40], ring_given [tr joseph cp pharaoh_of_joseph 41:42],
set_over_egypt [st joseph 41:41-44 — Sotah 36b:19's astrologers], asenath_given [st joseph 41:45], thirty_at_the_standing
[st joseph 41:46 — the marker's number], food_gathered_as_sand [st joseph 41:47-49 — 'until he ceased counting'],
plenty_seven_years [ti the_land_of_egypt 41:47 — FIRES 41:53], two_sons_before_the_famine [st joseph 41:50 — Taanit 11a:4],
famine_seven_years [ti the_land_of_egypt 41:54 — FIRES at 47:28's walk on the bare scene, at the marker on the tape],
famine_in_all_lands [st the_lands 41:54-57 — 'and all the earth came', Pesachim 119a:6], storehouses_opened [st joseph
41:56]. first_descent — descent_commanded [st the_sons 42:1-2 — Taanit 10b:6], ten_went_down [st the_sons 42:3],
benjamin_withheld [st benjamin 42:4], bowed_as_the_sheaves [st the_sons 42:6 — the dream's fulfillment recorded],
recognized_one_way [st joseph 42:7-8 — Bava Metzia 39b:8], dreams_remembered [st joseph 42:9], spies_charged [st the_sons
42:9-14], honesty_pleaded [st the_sons 42:10-13 — 'twelve brothers'], test_set [st the_sons 42:15-16 — 'by the life of
Pharaoh'], custody_three_days [ti the_sons 42:17 — FIRES 42:18], plan_revised [st joseph 42:18-20], guilt_acknowledged [st
the_sons 42:21-22, 44:16], interpreter_between [st joseph 42:23], held_in_custody [bo simeon 42:24 — CLOSED 43:23],
silver_returned_in_the_sacks [st the_sons 42:25-28, 42:35], report_given [st the_sons 42:29-34], bereavement_charged [st
jacob 42:36 — the three 'is not': Chullin 95b:14's presumption at three], pledge_offered [st reuben 42:37 — Bava Batra
173b:10's kabbelanut, refused 42:38], descent_refused [st jacob 42:38]. second_descent — famine_heavy [st the_land_of_canaan
43:1, 47:13], warning_cited [st judah 43:3-7], surety_undertaken [de judah cp jacob 43:9 — Bava Batra 173b:9: 'from where
that a surety is bound? from here'; CLOSED at 45:25 by the ink's own return to Jacob with Benjamin among them], mercy_prayed
[st jacob 43:14 — 'El Shaddai give you mercy'], double_silver_taken [st the_sons 43:12, 43:15], house_ordered [st the_steward
43:16-17], feared_at_the_door [st the_sons 43:18-22], peace_given [st the_sons 43:23 — 'your God gave you treasure'],
feet_washed [st the_sons 43:24], gift_presented [tr joseph cp the_sons 43:25-26], welfare_asked [st joseph 43:27-28],
benjamin_seen [st joseph 43:29 — 'God be gracious to you, my son'], egyptians_eat_apart [st egypt_people 43:32 — 'an
abomination to Egypt'], seated_by_birth_order [st the_sons 43:33], five_hands [st benjamin 43:34 — five, measured].
cup — cup_planted [st the_steward 44:1-2], overtaken_with_the_cup [st the_sons 44:4-6], theft_denied [st the_sons 44:7-8],
death_and_slavery_offered [st the_sons 44:9 — the rash sentence], finder_a_slave_ruled [st the_steward 44:10 — the rest
clean: Bereshit Rabbah 92:8], cup_found [st benjamin 44:12 — 'at the eldest he began': Pesachim 7b:14's search],
fell_before_him [st the_sons 44:14], divination_claimed [st joseph 44:5, 44:15 — the token of the Sinai ban, no verdict
before Sinai: FALSE], slavery_of_the_finder_ruled [st benjamin 44:17 — the three verdicts against Exodus 22:2 by call],
surety_invoked [st judah 44:32], substitution_offered [st judah 44:33]. i_am_joseph — restraint_failed [st joseph 45:1],
revealed_to_his_brothers [st joseph 45:3-4], terrified [st the_sons 45:3 — Chagigah 4b:8], sent_by_god_declared [st joseph
45:5-8], goshen_promised [he the_house_of_jacob 45:10 — CLOSED 47:11], sustenance_promised [he jacob 45:11 — CLOSED 47:12],
good_in_pharaohs_eyes [st pharaoh_of_joseph 45:16], good_of_egypt_promised [he the_sons 45:17-20 — CLOSED 47:11],
wagons_given [tr the_sons cp joseph 45:21], three_hundred_silver [tr benjamin cp joseph 45:22], ten_donkeys_sent [tr jacob
cp joseph 45:23 — Megillah 16b:4], quarrel_barred [bl the_sons 45:24], heart_numb [st jacob 45:26], spirit_revived [st
jacob 45:27], resolved_to_go [st jacob 45:28]. the_seventy — brought_up_promised [he jacob 46:4 — 'I will surely bring you
up': CLOSED at 50:13 on the family engine's burial in Canaan, the daemon's close on another engine's event],
josephs_hand_on_the_eyes [he jacob 46:4 — CLOSED 50:1], came_to_egypt [st israel_people 46:5-7], souls_counted [st
israel_people 46:8-27 — the value the four registers and the two totals, every number parsed; the names counted by
script beside them: 8h], judah_sent_ahead [st judah 46:28], let_me_die_said [st jacob 46:30], shepherds_abhorred [st
egypt_people 46:34], audience_prepared [st the_sons 46:31-34]. goshen — told_pharaoh [st joseph 47:1], five_presented [st
the_sons 47:2 — Bava Kamma 92a:19], work_asked [st the_sons 47:3-4], pharaoh_blessed [st pharaoh_of_joseph 47:7, 47:10],
years_confessed [st jacob 47:9 — a hundred and thirty, few and evil], holding_given [tr the_sons cp joseph 47:11 —
Rameses], sustained_by_the_mouth [st the_house_of_jacob 47:12 — Nazir 3a:6]. the_fifth — silver_gathered_to_pharaoh [tr
pharaoh_of_joseph cp egypt_people 47:14], livestock_to_pharaoh [tr pharaoh_of_joseph cp egypt_people 47:16-17],
bodies_and_ground_offered [st egypt_people 47:18-19], ground_of_egypt_acquired [tr pharaoh_of_joseph cp egypt_people
47:20], people_moved_to_cities [st egypt_people 47:21], priests_ground_exempt [st the_priests_of_egypt 47:22 — the chok as
sustenance, Beitzah 16a:3], seed_given [tr egypt_people cp joseph 47:23], fifth_to_pharaoh [st egypt_people 47:24-26 — a
STATUTE 'to this day', the sanctuary's fifth a homograph FALSE], servants_to_pharaoh [st egypt_people 47:25],
fruitful_in_goshen [st israel_people 47:27]. the_oath — burial_in_canaan_sworn [de joseph 47:29-31 — CLOSED at 50:13 on the
family engine's burial], bowed_on_the_bed [st jacob 47:31 — Megillah 16b:6]. mourning — face_fallen_on [st jacob 50:1 —
CLOSES josephs_hand_on_the_eyes], embalming_forty_days [ti jacob 50:2-3 — FIRES], egypt_wept_seventy [ti egypt_people 50:3
— FIRES], burial_leave_asked [st joseph 50:4-5], leave_granted [st joseph 50:6], funeral_ascended [st the_sons 50:7-9],
seven_days_mourning [ti the_sons 50:10 — FIRES], abel_mizraim_named [st the_threshing_floor_of_atad 50:11], returned_to_egypt
[st the_sons 50:14]. coffin — feared_joseph [st the_sons 50:15], forgiveness_asked [st the_sons 50:16-17 — the invented
command: Yevamot 65b:7], forgiven [st the_sons 50:19-21 — Mishnah Bava Kamma 8:7's rule at its second showing],
dwelt_in_egypt [st joseph 50:22 — a hundred and ten], born_on_the_knees [st the_sons-of-machir 50:23], visitation_promised
[he israel_people 50:24 — CLOSED at Exod 4:31 on the exodus story's `believed` ('the LORD had visited'), the daemon's close
on another engine's event], bones_oath [de israel_people 50:25 — CLOSED at Exod 13:19 on the exodus story's bones_taken;
Mishnah Sotah 1:9, Ketubot 111a:23], embalmed_and_coffined [st joseph 50:26]. About two hundred new; the appender's count
is the record.

### 8d. The daemon's watches (daemon_dispositions.yaml — GENERATED FROM THE HAND-MODEL this sitting, S3's lesson: the
### declaration's per-kind effects are the model's per-event writes, so the gate's first fail is the missing def alone)
law_joseph watches every kind of 8b and writes the effects of 8c per cell; the REUSED kinds shared with other daemons
carry seat checks BOTH WAYS: law_joseph answers named, appeared, born, bore, married, died, buried, journeyed, river_crossed,
prayed, embraced, kissed, wept, rebuked, envied, loved_apart, anger_burned, fled, dreamed, feast_made, restored,
counsel_given, famine_came, sent_away, pursued, bound, ate_and_drank, gifts_given, silver_given, sacrificed, blessed,
dwelt, sworn, burial_commanded, purchased, altar_erected, pillar_set_and_anointed, blessed_be_fruitful, land_promised,
statute_set ONLY at seats in Genesis 32-37, 39-47, 50 (the chapter SET), and never `buried` at Genesis 50 (the family's
burial) nor `renamed` nor `sinew_barred` anywhere; law_family's purchased, burial_commanded, buried, recognized, consented,
gathered keep their seats by 8k's edits; law_mamre's tables answer nothing outside 18-31; law_primeval's Genesis 2-16;
law_exodus_story's statute_set at Exodus 15 (8k). The CLOSES on other engines' events, by seat inside law_joseph before
its span check: brought_up_promised and burial_in_canaan_sworn on the family's `buried` jacob at Gen 50:12-13;
visitation_promised on the exodus story's `believed` at Exod 4:31; bones_oath on its `bones_taken` at Exod 13:19. The
functions block: the twenty-three cells WRAPPED by law_joseph; no build() entry.

### 8e. The registry (logic/corpus/entity_registry.yaml — members with units [step9-scenes]; a scene's tokens are its own,
### convention 21: no generic noun another runner submits or writes on)
Scene tokens joined to EXISTING entities by script: jacob, esau, joseph, judah, reuben, simeon, levi, dinah, rachel, leah,
bilhah, zilpah, isaac, rebekah (35:8's nurse), god, israel_people (the sons of Israel from 46:8), egypt_people, the_sons
(the family's raw token for Jacob's sons — used as it stands), ephraim, manasseh (the family's raw tokens), the_land_of_canaan,
beer_sheva_place, the_place_luz_bethel, the_pillar_of_bethel, the_men_of_sodom none. NEW entities: benjamin, deborah_the_nurse,
hamor, shechem_son_of_hamor, the_men_of_shechem, the_city_of_shechem, the_field_at_shechem, the_altar_at_shechem (the
S2 id the_altar_at_shechem exists for 12:7 — 33:20's altar is a second altar at Shechem: the_altar_of_el_elohe_israel),
the_house_of_jacob, the_cities_around_shechem, the_grave_of_rachel, the_midwife, esaus_wives (adah, oholibamah,
basemath_bat_ishmael — UNCERTAIN against 26:34's Basemath daughter of Elon and 28:9's Mahalath: the ink's two Basemaths
and the Ishmaelite wife's two names recorded, no fold), the_chiefs_of_esau (the roster's names as member tokens),
the_sons_of_seir (theirs), the_kings_of_edom (bela, jobab, husham, hadad_ben_bedad, samlah, shaul_of_rehoboth, baal_hanan,
hadar), eliphaz, reuel, amalek, timna, the_coat_of_stripes, the_pit, the_ishmaelites, the_midianites, the_medanites (the
three caravans of 37:25-36), the_sellers_of_joseph (UNCERTAIN — the ink's grammar at 37:28; Joseph's 45:4 names the
brothers), the_man_at_shechem, potiphar, potiphars_wife, the_house_of_potiphar, the_prison, the_prison_keeper,
the_cupbearer, the_baker, paro_joseph_era (token pharaoh_of_joseph), the_magicians, asenath, poti_phera (UNCERTAIN =
potiphar by Sotah 13b:12, recorded, no fold), the_steward, the_interpreter, the_silver_cup, the_lands (all the earth that
came to buy), the_land_of_egypt, the_ground_of_egypt, the_priests_of_egypt, goshen, rameses, the_wagons,
the_threshing_floor_of_atad, the_sons_of_machir, jacobs_daughters, the_camp_of_god, the_gift_of_droves, the_ford_of_jabbok,
the_terebinth_at_shechem, the_oak_below_bethel.

### 8f. The calendar rows (calendar_parameters.yaml)
road_years {sukkot_eighteen_months_bethel_six (Megillah 17a:7: 'he came to Sukkot and made there eighteen months ... and at
Bethel six months and offered sacrifices' — the RUNNING reading: the two years that close Megillah 17a's arithmetic, Jacob
99 at his return), none (unexercised)}; joseph_seventeen_at_the_sale {jacob_one_hundred_and_eight (the ink's chain 47:9,
45:6, 41:46, 37:2 — RUNNING)}; prison_two_years {before_the_standing (41:1's two years counted back from 41:46's thirty —
RUNNING)}; the_seventy {sixty_nine_counted (the names by script; Bava Batra 123b:1 Jochebed born between the walls,
Bereshit Rabbah 94:9 — the tradition's answers named, the count itself the ink's), seventy_stated}; isaacs_death_after_the_sale
{twelve_years (the ink's arithmetic 35:28, 25:26, 41:46, 45:6, 47:9 — RUNNING)}; embalming_and_weeping {forty_and_seventy
(50:3 — RUNNING)}. Every row with its arms visible; the running arm named RUNNING.

### 8g. The markers (the stitcher's table; every number parsed from the ink and re-verified at run time; the table
### reads only markers already on the tape at its position — S3's lesson)
'Gen 31:23' F [7] at 32:1 — M['heap_morning'] = told + 5 (Laban overtook on the seventh day from the flight, the heap's night,
32:1 the morning: told = flight + 2, so + 5); 'Gen 32:14' F — M['jabbok_night'] = heap_morning + 1 (the night of the gift and
the crossing, 32:14, 32:22-23 — the same night); 'Gen 32:32' F — M['peniel_sunrise'] = jabbok_night + 1; 'Gen 33:17' F —
M['sukkot'] = peniel_sunrise + 1 (the meeting on the sunrise day, Sukkot the next: modeled, said so); 'Gen 33:18' F —
READING-PLACED: M['shechem'] = add(sukkot, 18, 'month') (the row road_years; Megillah 17a:7); 'Gen 35:6' F — READING-PLACED:
M['bethel_again'] = shechem + 1 day for 35:5's journey (the Shechem stay inside the eighteen months by the shelf's own count,
said so); 'Gen 35:16' F — READING-PLACED: M['ephrath_road'] = add(bethel_again, 6, 'month') (the six months at Bethel);
'Gen 35:27' F — M['hebron'] = ephrath_road + 1 (modeled): Jacob's return to his father — the arithmetic's ninety-nine, CJ1;
'Gen 35:28' P [100, 80] STANDS (died:isaac = born:isaac + 180, S1's proleptic row); 'Gen 37:2' F [17] — M['age:joseph:17'] =
year_day(yr(born:jacob) + 108) (the row joseph_seventeen_at_the_sale: born:joseph is set only at 41:46's row, so the sale's
year comes off born:jacob by the same chain 47:9 − 45:6's nine − 41:46's thirty + seventeen); 'Gen 40:12' F [3, 3] at 40:5 — READING-PLACED: M['prison_dreams'] = year_day(yr(born:jacob) + 119) − 2 (Joseph thirty at Jacob's
121 by 47:9 − 45:6's nine; the birthday two years before that by 41:1, so Jacob 119; the dreams two days before the
birthday, the third day inclusive — joseph30 itself is 41:46's row and not yet on the tape at 40:5); 'Gen 40:20' F ordinal
[3] — M['birthday'] = prison_dreams + 2; 'Gen 41:1' F [2] — M['pharaoh_dreams']
= add(birthday, 2, 'year') (= year_day(Jacob 121) = joseph30's day: the ink's own arithmetic, joined at 41:46 where S1's
row STANDS); 'Gen 41:53' F [7] — M['plenty_end'] = add(joseph30, 7, 'year'); 'Gen 45:6' F [2, 5] — M['famine_two'] =
add(plenty_end, 2, 'year') (= the descent's year by S1's construction, printed, no checkpoint); 'Gen 46:1' F — M['beersheba_descent']
= famine_two (the departure in the famine's second year); 'Gen 47:9' F [130] STANDS (descent); 'Gen 47:28' F [17, 147] STANDS
(jacob_147); 'Gen 50:3' F [40, 70] — M['embalmed'] = jacob_147 + 40, M['weeping_end'] = jacob_147 + 70; 'Gen 50:10' F [7] at
50:10 — M['atad'] = weeping_end + 1 (modeled), M['atad_end'] = atad + 7 at 50:14; 'Gen 50:26' P [110] STANDS (died:joseph =
born:joseph + 110, S1's row). No retrograde row: every reading-placed date lies forward of the counter.

### 8h. The checkpoints (the sequence runner; declared by the text or the shelf, computed by the engine)
CJ0 THE TWO ABSENCES — Megillah 17a:6-7: Joseph parted from his father twenty-two years as Jacob parted from his: computed
on two independent chains, yr(hebron) − yr(departure) [Jacob's: the road markers off Ishmael's death and Megillah 17a's
fourteen] and yr(famine_two) − yr(age:joseph:17) [Joseph's: Pharaoh's side] — both 22, MATCH expected, a JOIN. CJ1 JACOB
NINETY-NINE AT THE RETURN — yr(hebron) − yr(born:jacob) = 99 (63 at the blessing + 36: Megillah 17a:6's thirty-six) — MATCH
expected. CJ2 ISAAC'S DEATH TWELVE YEARS AFTER THE SALE — yr(died:isaac) − yr(age:joseph:17) = 12 by the ink's arithmetic
(35:28 − 25:26's sixty − 37:2's seventeen − Joseph's birth at Jacob's ninety-one) — MATCH expected; the page order (35:29
before 37:2) against the chronology, the proleptic marker carrying it. CJ3 THE SEVENTY — 46:27's seventy against the ink's
sub-totals 33 + 16 + 14 + 7 (parsed, MATCH expected) and against the names counted by script per register (Leah's 33 counts
32 living named — Er and Onan dead by 46:12 — or 34 with the dead: DIVERGE expected, the tradition's five answers named,
Bava Batra 123b:1 and Bereshit Rabbah 94:9 on the shelf, filed OPEN). CJ4 THE SIXTY-SIX — 46:26's sixty-six = seventy − Joseph
− his two sons − Jacob: the ink's own arithmetic, MATCH expected. CJ5 THE HUNDRED AND FORTY-SEVEN — 47:28's a hundred and
forty-seven = 47:9's a hundred and thirty + 47:28's seventeen, parsed — MATCH. CJ6 THE THIRD DAYS — the cupbearer's and the
baker's timers (three days from the dreams) and the custody's (three days, 42:17) fire on the tape's walks before their
acts (40:20-22, 42:18) — MATCH expected. CJ7 THE CLOSES ON OTHER ENGINES' EVENTS — four performed on the tape: return_promised
(28:15 at 35:6, its own), brought_up_promised and burial_in_canaan_sworn at Gen 50:13 (the family's burial), bones_oath at
Exod 13:19 (the exodus story's), visitation_promised at Exod 4:31 (its believed) — five closes, MATCH expected. CJ8 THE
EIGHTH DAYS — circumcision_due timers on the stretch's births = three (Benjamin, Manasseh, Ephraim) — MATCH. CJ9 THE
FAMINE'S TWO TIMERS — the seven years of 41:54 and the five remaining of 45:6 fire on ONE day (2244) — MATCH expected, the
ink's own arithmetic. CJ10 THE PRESUMPTION AT THREE — the three 'is not' tokens of 42:36 counted in the verse (Chullin 95b:14)
— 3, MATCH. CJ11 EXODUS 1:5's SEVENTY — the exodus story's Exod 1:5 (if on the tape with the count) against 46:27's seventy —
the two ink numbers parsed, MATCH expected (else printed).

### 8i. The scene (the runner's own bare world; the rows in the text's order; the tuple predicted by a hand-model
### BEFORE the runner is typed — scratchpad o8_s4_predict.py — with the OP CLASS of every effect from the registry and
### the WRITE TIME of every timer: ten story timers (the cupbearer's and the baker's three days, the custody's three, the
### plenty's seven years, the famine's seven, the five remaining, the embalming's forty days, Egypt's seventy, the seven
### days at Atad) and three eighth-day timers all fire inside the scene, so each is written once at its fire)
The scene's days: 32:1 day 1; the night 2; the sunrise 3; the meeting 3; Sukkot 4; then the bare scene walks by the ink's
numbers where it has them (eighteen months to Shechem, six months at Bethel, seventeen at the sale by a whole-year walk,
the third days, the two years of 41:1, the seven years of plenty, the two famine years of 45:6, the seventeen years of
47:28, the forty and seventy days, the seven at Atad, Joseph's remaining years) and by one day elsewhere; the slots: the
effect slots per (subject, effect) in the text's order, then opens, timers set, fired, closes, the day. The scene's kind
count, effect-slot count and the tuple are the model's print, typed after.

### 8j. The answer sheet and the shelf the cells read
Mishnah rows verified by their own tokens: Megillah 4:10 (Reuben's act read and not translated), Sotah 1:9 (Joseph buried
his father; Moses tended Joseph), Bava Batra 10:8 (the surety collects from free property), Bava Metzia 5:11 (the surety a
legal person), Shabbat 19:3 (the third day's pain — 34:25 the proof text), Pesachim 1:1 (the search for leaven), Bava Kamma
8:7 (forgiveness — the second showing), Ketubot 3:4 (the seducer's three and the rapist's four), Yevamot 6:6 (be fruitful —
the man commanded), Bava Batra 8:2 (the inheritance order — the firstborn kept at 46:8). The Babylonian rows (file index
2*daf-2, +1 for b), every one located by script this sitting (scratchpad o8_s4_shelf.txt): Megillah 16b:2, 16b:3, 16b:4,
16b:5, 16b:6, 16b:7, 17a:2, 17a:3, 17a:4, 17a:5, 17a:6, 17a:7, 18a:17; Bava Batra 115b:4, 123b:1, 173b:9, 173b:10; Chullin
95b:14, 101b:9; Pesachim 7b:14, 119a:6; Sotah 10b:7, 13b:12, 36b:9, 36b:19; Nedarim 31b:14; Yevamot 65b:5, 65b:7; Ketubot
111a:23; Taanit 10b:6, 10b:11, 11a:4; Sanhedrin 6b:5, 92a:3, 99b:8; Arakhin 16a:13; Berakhot 12b:28, 34b:3, 42a:8, 55b:2;
Shabbat 85a:2; Beitzah 16a:3; Bava Kamma 92a:19; Avodah Zarah 25b:8; Horayot 10b:11; Nazir 5a:5; Chagigah 3a:14, 4b:8; Bava
Metzia 39b:8. The Genesis spine's rows (Bereshit Rabbah, BR[par-1][row-1]): 78:9, 78:11, 78:12, 78:14, 79:5, 79:7, 79:8, 80:6,
80:8, 80:9, 80:10, 80:12, 81:1, 81:2, 81:5, 82:9, 82:10, 82:11, 82:14, 82:15, 83:1, 84:7, 84:8, 84:16, 84:17, 84:18, 84:19,
84:21, 86:3, 87:5, 87:10, 88:5, 88:7, 89:1, 90:3, 90:5, 91:3, 91:7, 91:8, 92:8, 92:9, 93:9, 93:12, 94:5, 94:9, 95:4, 96:5, 100:8,
100:9, 100:11 — every one located by script (the census); Onkelos only from the units' own notes. NOT on the local shelf,
named as absent: Seder Olam (the ages), the Jerusalem Talmud, Avot de-Rabbi Natan, Rashi.

### 8k. The edits to standing files (each with its check)
cold_run_family.py — law_family's purchased, burial_commanded, recognized, consented, gathered branches seat-checked
(purchased to Gen 23; burial_commanded to Gen 49; recognized to Gen 38; consented to Gen 24; gathered to Gen 49): its own
228/228 unmoved, the sequence tape's double writes unchanged. cold_run_exodus_story.py — its statute_set branch seat-checked
to Exodus if it is not (47:26 would reach it); its bones_taken and believed events untouched (law_joseph closes on them by
seat). cold_run_mamre.py — nothing (its tables answer nothing outside 18-31). The stitcher: CLOCK_DAY_RUNNERS + 'joseph';
SPAN_ORDER ['pre_sinai', 'primeval', 'mamre', 'joseph', 'family', ...]; the rows of 8g; AGES + ('Gen 37:2', 'joseph', 17) is
NOT used (born:joseph is not on the tape at 37:2 — the row computes off born:jacob); the DAYS key list extended. The
sequence runner: `import cold_run_joseph` after cold_run_mamre; DAEMON_ORDER + ('cold_run_joseph', 'law_joseph') ("ALL 43
DAEMONS"); CJ0-CJ11 before `verdicts`; VERDICTS extended; NEWEST_RUNNER = 'joseph', PREVIOUS_RUN = S3's tuple; CENSUS, DAYS
(+ the new keys), RUN typed from the stitcher's print and the first run, the RUN tuple READ BY SCRIPT before typing (THE
REST reproduces S3's exactly). daemon_dispositions.yaml: law_joseph's watches generated from the model, installed_by absent
(T1 is Numbers' sitting), the functions block `joseph:` twenty-three cells. dependency_dispositions.yaml: the span, the
edges the census emits (CALL pre_sinai, offerings, family, mishpatim_2, mishpatim_3; REFERENCE vestments, pesach; FALSE
the homographs — the deposit of 41:36, the fifth of 41:34 and 47:24, the minchah of 43:11, the abomination of 43:32, the
divination of 44:5, the chok of 47:22, the libation of 35:14 as REFERENCE), the registration edge sequence → joseph.
event_vocabulary.yaml, effect_vocabulary.yaml, calendar_parameters.yaml (+6 rows), entity_registry.yaml as 8b, 8c, 8f, 8e.

### 8l. The order of work (the wrap's rhythm, amended by S3's lesson)
(1) this section; (2) the effects by script with the CLAIMS list verified — the NEW list checked against the registry
first; (3) the types by script, the events lint 0; (4) the calendar rows and the registry; (5) THE HAND-MODEL printed; (6)
the daemon declared in daemon_dispositions.yaml with its watches GENERATED FROM THE MODEL, the gate run to FAIL on the
missing def; (7) the span on a stub and the census --emit, the edges dispositioned; (8) the code — the shared-branch edits of
8k first, fix_percent, then cold_run_joseph.py; (9) the run; (10) the recorder and the stitcher (the rows of 8g); the
sequence runner's literals; the sequence run; CJ0-CJ11 read; the RUN tuple read by script (THE REST test), then typed; (11)
the gates, the probes, the sweep, the corpus regression; (12) the records: 8n AS RUN, the report's fourth sitting,
COMPILE_DEBT, THE_STEPS if a convention is proven, THE_BRIEFING, the state doc, memory; a compaction point.

### 8m. OPEN at this sitting
The seventy's missing one (CJ3 — five answers on the shelf, none the ink's). The seller of Joseph (the ink's grammar at
37:28 against 45:4). Benjamin's plene spelling (Sotah 36b:9's claim measured against the DB's letters — recorded whichever
way it falls). Potiphar and Poti-phera (Sotah 13b:12 — recorded, no fold). Esau's wives' names against 26:34 and 28:9
(recorded, no fold). The kill intent of 27:41 outliving the mourning it waited for. Rebekah's death unnarrated. Seir
promised and never reached. The tithe of 28:22 never narrated as paid. Timna's Amalek (Sanhedrin 99b:8's conduct verdict —
a status, no engine). The two Anas (Bava Batra 115b:4). The fifth as Egypt's statute beside the sanctuary's fifth (a
homograph, FALSE). Exodus 23:20-33 outside every scene (the census's one narrative unit left). The Genesis eras' T2
placement class (page_order / text_constrained / reading_placed) — O9's field.

### 8n. AS RUN (2026-09-08; the account: REPORT_NARRATIVE_GAPS.md, the fourth sitting)
The order held: the effects (681 → 905 — 224 new, one the effects script omitted (five_years_of_famine_left) appended directly;
every count claim through the CLAIMS list — thirty-six claims REFUTED on the dry runs and corrected beside their record, the
"none located" placeholders struck after the rows were located by script), the types (624 → 791 — 167 new, forty standing
kinds extended; the events lint's shared-witness flag on feast_made resolved to 43:25), six calendar rows, the registry (214 →
268; two clashes under convention 21, 'adah' and 'the-baker', renamed adah-wife-of-esau and the-chief-baker), THE HAND-MODEL
printed (313 events, 207 kinds, 288 slots; nine story timers — the declaration's "ten" a miscount — and three eighth days;
twelve closes and two lines on S3's entries; day 11407), the daemon declared with its watches GENERATED FROM THE MODEL (207
+ believed and bones_taken for the by-seat closes = 209) and the gate run — ⚠ its first FAIL was a YAML PARSE ERROR of our
own (the functions block appended after the file's tail), read as the expected fail on the exit code alone and found only at
the next sitting; repaired, the honest missing-def FAIL recorded (scratchpad o8_s4_gate1b.txt). The span on a stub, the
census --emit: ten required edges (seven FALSE homographs, pre_sinai/offerings/family CALL), three live beyond the census (the
mohar, the thief sold, the tunic — rule 9; the tunic's edge first filed REFERENCE and corrected to CALL at the review), eighteen
pointers all INTERNAL, the registration edge. The 8k edits (five family
branches, the exodus story's statute) with both runners unmoved. The ink claims measured before typing: 42:36 carries "is
not" (איננו) TWICE — the design's CJ10 refuted, the presumption's third is Benjamin's clause without the token; Benjamin full
(בנימין — Binyamin with the second yod) at seven seats and Benjamin short (בנימן — the name without the second yod) at nine in Genesis, Sotah 36b:9 measured and recorded either way; the Name by chapter
37-50 = 39 eight, 38 three, 49 one, every other chapter zero; the seven/plenty skeleton (שבע — seven or plenty, one spelling)
thirty-one tokens in Genesis 41; Kiriath-arba's four uncounted by the parser (the article), Beersheba's seven counted. The
generator: 442 probes (the rosters' 91 names, three in their verses' plene forms), 207 branches (28 per-verse tables), 379
scene lines. The first graded run 280/282 — two misses read: THE THIEF SOLD's compiled verdict is the TERM
(six_years_for_the_principal) and the hand had typed the effect's name — corrected beside its record; and ONE open entry
more than the model — the pre-Sinai daemon's blessed_be_fruitful branch had no seat check and wrote on 'god' at 35:11
(seat-checked to 1:28, 9:1, 9:7). Second run 282/282 (pure ink 178 / recorded moves 81 / answer-sheet 10 / data 5 / imports 8
/ hypotheses 0). Before the tape, the third-day timers re-read INCLUSIVE (+2, the tape's convention at 22:4 and 31:22) — the
tuple unmoved, the cell measuring the span from the log. The recorder: 313 submits, 312 history + 1 statute. The stitcher,
one honest stop (INK MISMATCH at 35:27, Kiriath-arba); the register test set four events aside (the three marriages of 36:2-3
— the roster's perfect "took" — and 43:1's nominal famine clause): 309 on the tape; 129 markers (112 F / 15 P / 2 R), 1058
events, 70 closes, 611 kinds. The sequence runner's first tape run raised KeyError 'seat' at 35:12: law_primeval's
land_promised branch answered Joseph's event — its shared-kind set extended (the third leak caught since S2; convention 14
both ways); the second run 5/8: CJ6 DIVERGED on the custody (no marker between 42:17 and 42:18, the clock never walked to the
third day — the row 42:18 added, 8g had omitted it), CJ9 DIVERGED (the five-years timer set two years early: the speech's
event line 45:5-8 sorted before the marker at 45:6 — the marker positioned at 45:5), and the marker count read 111 against
the stitcher's 109 rows (two rows carried two w.marker calls — split: ONE MARKER PER ROW, 50:4 and 50:14); the third run 7/8
with THE REST reproducing S3's tuple exactly and every checkpoint as declared (CJ3b DIVERGE, the seventy's missing one);
THE RUN TUPLE READ BY SCRIPT (events 749 + 309; writes 907 + 321 − 4; set 31 + 12; fired 27 + 12; daemons 11 + 1; entities
219 + 33; closes 56 + 14 + 4) and typed (1058, 43, 39, 0, 0, 1224, 12, 252, the two mornings, 74); 8/8. The daemon gate at
the close: ZERO DRIFT (the watches generated from the model — S3's lesson closed), 43 daemons, 327 functions, 0 owed. The
census after: GENESIS WHOLE ON THE ENGINE — every narrative stretch of section 1's census on the tape; Exodus 23:20-33 the one
narrative unit outside every scene. The gates, the probes, the sweep and the corpus regression: the report's closing section.
REVIEWED (2026-09-08, the owner: "review what you did that took so long for errors" / "Yes go"): six errors found, none in a grade — (i) the
vestments edge filed REFERENCE on a live import (CALL by the census file's own rule; an edge beyond the token census is checked for its entry
alone — the gate cannot catch the disposition's value there); (ii) the seventy cell for Exodus 1:5 returned a typed literal behind a presence
check while saying "parsed" — it parses now; (iii) five shelf rows verified by token and read by no cell (Megillah 17a:2, Bereshit Rabbah
78:14, 80:9, 84:16, 84:17) — cited where the text reaches them; and Shabbat 85a:2, DECLARED in 8j, was never placed on the runner's shelf
(the shelf is forty-eight Babylonian rows and fifty-one of Bereshit Rabbah, 78:8 added beyond 8j's list) — the review's own first count said
"six on the shelf", corrected here: five on the shelf uncited, one declared and absent, left absent; (iv) "six FALSE" above was seven; (v) the
state doc's "twenty rows of 8g" — 8g had seventeen rows carrying nineteen markers, twenty rows after 42:18 and the split; (vi) memory's
"twenty-one marker rows" — twenty. The time: the gate's exit code read as its message; two divergences on the tape that earlier lessons
already covered (a marker at its event's first verse — S2's 7:4 at 7:1; one marker per row, kept unstated by every earlier row); the timer
semantics changed after the runner was green. The runner (282/282), the sequence runner (8/8), both gates and the sweep rerun after the fixes.
