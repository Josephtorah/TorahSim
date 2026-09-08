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
