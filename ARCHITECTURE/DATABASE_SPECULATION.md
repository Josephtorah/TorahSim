# Database speculation — the population table, from the ark forward

Stored on the owner's word, 2026-09-11, at the close of THE NUMBERS WALK sitting 7b (Balak compiled). Two voices: the report from the
torah-grok-ce thread (pasted by the owner) and the main thread's response. STATUS: SPECULATION, NOTHING BUILT. The owner's instruction:
"we'll come back to it after we do chapter 26." Chapter 26, the second census, is read first and then compiled; the design of any
population table belongs at that compile, on the owner's word, as a model-layer item under the constitution (immutable evidence,
rewritable models; code from the 24 books only; the Mishnah and Talmud as test data).

---

## 1. The report (torah-grok-ce, 2026-09-11)

Speculation from two sittings, checked against the word database and the local shelf. Nothing built.

**1. The ark is the first enumerated population table, and the text writes its schema.** Creation makes the classes, "after its kind."
The ark is where the classes are listed with columns, each verified in the ink: kind, four times in 7:14; sex, "male and female" (6:19,
7:16); a count per kind, two, and sevens for the clean (7:2-3); a classification field, "clean," making its first Torah appearance as
cargo arithmetic at 7:2; a timestamp, the first full calendar date in the Bible at 7:11; a container with a lock, "the LORD shut him in"
(7:16); an exit "by their families" at 8:19, the family word's first token; and a membership predicate, the covenant's roster "all that
came out of the ark" (9:10). Rows, columns, a snapshot date, and a membership query.

**2. The tradition reads it as a store with integrity rules.** Three decks, refuse, beasts, people (Sanhedrin 108b). Compartments,
"rooms and dwelling quarters" (Bereshit Rabbah 31:9). Kinds kept unmixed and each fed at its own hour (Sanhedrin 108b:19). The manifest
changed during the voyage: what walked out "after their kinds" were descendants (Bereshit Rabbah on 8:19), so the table is keyed by kind
with counts, not by individual. The flood's cause is read as "all flesh corrupted its way," mating across kinds (Sanhedrin 108a). The
database's first invariant, kinds do not mix, is stated at the flood, enforced by the ark's compartments, and legislated at Leviticus
19:19.

**3. The schema lineage runs into Numbers.** Each step keeps the family column and adds keys.

| Table | Verses | Columns the text writes |
|---|---|---|
| the ark | Genesis 6:19-20, 7:2-3, 7:14, 8:19 | kind, sex, count, clean, family, date |
| the nations table | Genesis 10:5, 20, 31 | family, tongue, land, nation |
| the descent roster | Genesis 46 | persons by name, seventy |
| the first census | Numbers 1:2-3 | family, fathers' house, number of names, male, poll, age band, host |
| the second census | Numbers 26:53-55 | names, tribes, fathers, land joined by lot |

Numbers is the ark's schema at national scale.

**4. What the engine holds today.** Kinds are not entities: the registry has no animal rows, "the beasts" is one token, the boarding is
a debit closed by its receipt in the primeval runner, and the clean beasts of 7:2 enter only as a live call into the species classifier.
That call is the seed of the right thing: the ark's clean list is the labeled data the Leviticus 11 predicate later computes from
signs. The bamidbar runner asserts the census arithmetic from the ink, 603,550 summed three ways, the Levite houses 22,300 against
22,000, the firstborn surplus 273 redeemed at 1,365, but as parsed numbers, not row operations.

**5. How the table would function.** Two tiers, matching the text's grain: named rows for persons the ink names, counted aggregates per
family and fathers' house for everyone else, with kinds as classes above both. No invented individuals; 603,550 is a number on a row.
It changes only by events on the tape: a birth marker opens a row and a life era, a death total closes it, "begot" adds a family edge,
a census marker writes aggregates, an allotment verse joins a family to land. Every write is by a daemon or a marker, never by hand.
Declared totals become checkpoints: a verse restating a count is compared to the rows, and chapter 26's deltas, Simeon 59,300 to 22,200
with no births or deaths on the tape, are reported as declared and left open. Membership is always as-of a marker, the ark's own
semantics.

**6. Who reads it.** Daemons would find their subjects by query instead of receiving them inside the event: the census shekel asks for
males twenty and up by house; the Levite service for thirty to fifty by clan; the firstborn redemption for firstborn males against the
Levite count; the inheritance engine, already compiled at chapter 27, for a house with no sons and the nearest kinsman; the land laws of
Leviticus 25 for each man's holding so the Jubilee's return has somewhere to return him; the mixture laws for the ark's invariant on
every pairing. A shelf scenario such as "a daughter of a house with no sons" could then be put to the live world by query, which is what
the loop's scenario step was built for.

**7. What it cannot do, by design.** It cannot age an uncounted person, since only markers give ages; fill a family below the count the
text gives; or resolve a delta the text leaves unexplained. Each silence is shown as a labeled gap, as the tape prints its undated
stretches.

**8. Why it matters for the destination.** When the Prophets run as the tape the daemons fire against, every indictment names a who: a
tribe, a house, the priests. The ledger can hold what is owed; only a population table can hold who owes it. That is the missing half of
the whole-Tanakh check, and the ark is where the text first builds it.

**9. Timing and status.** Not before Balak's compile, by the standing order. The natural moment is chapter 26, the first time the text
counts the same families twice and joins them to land. It would be model-layer work under the constitution: seeded at the ark with rules
rather than numbers, forked at the nations table, filled by name at Genesis 46, counted at Numbers 1 and 26; design first, probes to
fail, then code. A candidate for THE_WORLD's build queue on the owner's word, nothing more.

---

## 2. The main thread's response (Torah Grok Main, 2026-09-11)

The report is mostly right, with one correction and one caution.

- **The ark is where the database begins, but only one of its two tiers.** The ark is the first table of CLASSES with counts: kind,
  sex, count, clean, a date, a locked container, and a membership predicate ("all that came out of the ark"). The other tier is older.
  Genesis 5 is already a table of named persons with timestamps: name, age at begetting, remaining years, total, death. The tape holds
  that tier now as the life eras and birth markers (the DAYS literals of cold_run_sequence.py — born:seth, born:noach, born:shem …).
  So the named-person ledger starts at Genesis 4-5, the counted-class table at the ark, and the two are joined for the first time at
  Numbers 1 (names, houses, counts) and then at Numbers 26 (plus land).
- **The schema is the ink's own words, which is what makes it buildable under the constitution.** Family, fathers' house, number of
  names, male, poll, age band, kind, clean: every column is a token the text writes. The counts are data rows. No invented individuals;
  603,550 is a number on a row.
- **The engine's state is described accurately.** Kinds are not entities, the boarding is a debit closed by a receipt, and Bamidbar's
  arithmetic is parsed and asserted, not stored as rows. The entity registry (327 rows at 7b's close) is a person table already, but
  keyed by narrative naming with no aggregates.
- **The strongest idea is daemons finding subjects by query.** The census shekel, the Levite service ages, the firstborn redemption, the
  inheritance engine, the Jubilee's return: each is a query the text itself phrases. That is also what would turn chapter 26's deltas
  into checkpoints: Simeon's fall from 59,300 to 22,200 sits beside the Peor plague entry's 24,000 (on the tape since 7b), with the
  tribe assignment a shelf claim (the Sifrei 131:2's "twenty-four thousand of his tribe"), so it would print as a labeled gap, not a
  computed row.
- **Caution.** The "kinds do not mix" invariant is the tradition's reading of the flood's cause (Sanhedrin 108a), not the ink's; it
  belongs as a data row until Leviticus 19:19 writes it.
- **Timing.** Agreed: not before the reading of chapter 26, which is the first time the text counts the same families twice. The
  design belongs at 26's compile, on the owner's word, as a model-layer item on THE_WORLD's build queue.

## 3. What to bring back to this file after chapter 26

- The second census's own columns as read (26:5-51 the families by name and count; 26:53-56 the land by lot and by count; 26:57-62 the
  Levites apart; 26:63-65 the membership predicate "not a man of those counted by Moses and Aaron in the wilderness of Sinai" — the
  ark's exit roster at national scale).
- The deltas per tribe between Numbers 1 and 26, computed by the parser at both seats, and which ones the tape can explain (the plague's
  24,000, Korach's 14,700 and the 250, the wilderness generation's deaths) against which it cannot.
- Whether the registry's person rows and the ledger's aggregates can share one table without inventing anyone.

### After the reading of chapter 26 (sitting 8, 2026-09-11) — the columns as read, before the compile

- **The second census's own columns** (the ledger num_26_second_census_2026-09-11.md, every fact computed): per tribe a HEAD ("the sons of X by
  their families"; Reuben "the firstborn of Israel"), the FAMILIES as name → gentilic pairs ("of Pallu, the family of the Palluite" — seventy-eight
  "family of" tokens, sixty-eight gentilic forms, fifty-seven families in the twelve tribes; one form without its yod), a SUMMARY in one of three
  forms with a COUNT-WORD in eleven of twelve (Simeon's bare), the COUNT (the parser reading all twelve, summing to the ink's 601,730), and
  EXCEPTIONS written inside the roster (Er and Onan dead in Canaan; Dathan and Abiram and Korach with their two deaths and "the sons of Korach did
  not die"; Zelophehad "no sons, only daughters" with the five named; Serah the daughter); the LEVITES apart with their own reason ("not counted...
  for no inheritance"); the TOTAL; and the MEMBERSHIP PREDICATE (26:63-64 one sentence twice — the priest and the place the deltas; "not a man" of
  the first roll on the second; 26:65 the decree's words and the two exceptions by name). Chapter 1 counts "by the number of names" and never says
  "family of"; chapter 26 says "family of" seventy-eight times and applies chapter 1's phrase to the LAND (26:53): the roll that counted the host
  sizes the portions.
- **The deltas per tribe** (computed by the parser at both seats): Reuben −2,770, Simeon −37,100, Gad −5,150, Judah +1,900, Issachar +9,900, Zebulun
  +3,100, Manasseh +20,500, Ephraim −8,000, Benjamin +10,200, Dan +1,700, Asher +11,900, Naphtali −8,000; five fell (61,020), seven rose (59,200),
  the whole −1,820; the Levites +1,000. **What the tape can explain against what it cannot:** the Peor plague's 24,000 (on the tape since 7b, its
  tribe the shelf's claim) is smaller than Simeon's fall alone — 13,100 remain even if every dead man were his; Korach's 250 and 14,700 carry no
  tribe in the ink (Dathan and Abiram Reubenites, Korah a Levite, the 14,700 unassigned); the wilderness generation's deaths are nowhere counted.
  So the deltas are DECLARED rows, not derivable: the table carries them as the ink's numbers with the tape's explanations beside them and the
  remainder labeled — exactly the report's item 7.
- **One table for persons and aggregates?** The reading says the ink already keeps two grains inside one chapter: named rows (Er, Onan, Dathan,
  Abiram, Korach, the daughters, Serah, Jochebed, Miriam, Nadab, Abihu, Caleb, Joshua — persons the roster names) and counted rows (the families
  and the tribes). The registry's person rows (327 at 7b) are the named grain; the counted grain has no home yet. 26:59's Jochebed "whom she bore
  — her — to Levi IN EGYPT" (the verb without its subject) is a named row whose one datum ("in Egypt") decides an aggregate (the seventy of
  Genesis 46:26-27 — the tape's CJ3b open by one): a person's row and a count's row joined by the ink itself. The design belongs at 26's compile,
  on the owner's word.

### Built at the compile of chapter 26 (sitting 8b, 2026-09-11) — the owner's decision and what stands

- **The decision** (the owner, 2026-09-11: "Let's discuss the database option again" → "What do you recommend" → "Ok go"): built inside
  8b as one sitting, minimal and honest; the backward seeding filed, not built.
- **What was built**: THE POPULATION TABLE as engine state (World.tables, the fifth registry World/step9/population_schema.yaml — the
  columns the ink's own words, three grains: counted / named / delta), written only by a daemon consuming an event (World.row refuses a row
  by hand), queried by daemons during the run (World.population), journaled as the ninth log class ROW (run.row), read back by the fifth
  view run_population and the fifth question `population [tribe]`; the probes population_probes.py 0/9 → 9/9. The first writer:
  law_second_census — the first roll's rows on chapter 1's own event (a shared kind, rows only), the second roll's twelve tribes and
  fifty-seven families (the families with NO count: the ink gives none), the DECLARED delta rows (Simeon −37,100 explained by the Peor
  plague's 24,000 by call with the tribe the shelf's, −13,100 labeled unexplained; every other delta wholly unexplained), the Levites 22,000
  → 23,000 (+1,000 unexplained; five families for eight), the named rows (29 persons the roll names with the clause the ink writes). The
  first readers: the daughters' row (26:33 — the premise on the table before the plea at 27:1; the inheritance engine's heir_of answers
  from it) and Jochebed's row (26:59 — CJ3b's ink witness; the verdict stays DIVERGE, the row a witness, not a resolution).
- **The three answers of section 3, as built**: (1) the columns as read are the schema's; (2) the deltas per tribe are declared rows with
  the tape's explanations beside them — one explained in part (Simeon), twelve unexplained (the Levites' among them); (3) the person rows
  and the aggregates share ONE table in two grains with a third for the deltas — no invented individual: the registry's persons keep their
  ids, the tribes and the families are names, not entities.
- **Filed** (COMPILE_DEBT.md): the backward seeding — the ark's kind table (Gen 6:19-20, 7:2-3, 7:14, 8:19), the nations table (Gen 10),
  Genesis 46's roster by name (the Joseph runner's ROSTERS hold it as lists) — to be built when a daemon queries a person before Numbers
  1; the "kinds do not mix" invariant a data row until Leviticus 19:19 writes it. THE LINK QUESTION ON THE ARK: the reading's claim set
  26:64's predicate beside "all that came out of the ark" (Gen 9:10) — a shared phrase with no teacher: carried in the runner as ONE
  HYPOTHESIS cell (class H, counted apart in the FRACTIONS line), the primeval runner not called.
- **The record**: World/step9/NUMBERS_WALK.md "Sitting 8b" (the design and the as-built), World/step9/THE_LOOP.md's ninth-class section.

## 4. The ink's architecture, measured (2026-09-11 — the discussion's step after sitting 8b; the owner: "Yes let's take the next discussion step",
## then "Ok now can we determine the intended architecture", then "Yes let's do 1,3 then 2 in the next sitting")

Two measurements on the Tanakh DB (every token of the Torah with its lemma column) with the step-9 parser reading the numerals — the scratch
scripts structural_census.py and architecture_census.py of session 379bc7e8 and their prints; THE REGISTER GATE of the next sitting houses the
formulas in the repo. Nothing built here. The owner's "1, 3" put the findings in this section (with the pointer in THE_WORLD.md and the finding in
RESEARCH_LOG.md) and the seeding's design beside its debt in World/step9/COMPILE_DEBT.md.

### 4.1 The key words' seats (Genesis 1 through Numbers 26; the Torah whole in brackets)

| word | tokens to Num 26 [Torah] | first seat | where it is dense |
|---|---|---|---|
| family מִשְׁפָּחָה ("family") | 174 [185] | Gen 8:19 לְמִשְׁפְּחֹתֵיהֶם ("by their families") — the exit from the ark | Gen 10 (5), Exod 6 (6), Lev 25 (5), Num 1 (14), 3 (21), 4 (18), 26 (94); Numbers holds 159 of the Torah's 185 |
| name שֵׁם ("name") | 208 [252] | Gen 2:11 | Genesis' narrative (113); Num 1 (16), 26 (5) |
| number מִסְפָּר ("number") | 34 [46] | Gen 34:30 | Num 1 (14), 3 (5) |
| the counted / count פָּקַד ("count", "visit") | 129 [135] | Gen 21:1 | Exod 30 (5), Num 1 (22), 2 (19), 3 (12), 4 (22), 26 (20) |
| generations תּוֹלְדוֹת ("generations") | 29 [29] | Gen 2:4 | Genesis 13, Exodus 3, Numbers 13 (Num 1 alone 12) |
| kind מִין ("kind") | 26 [30] | Gen 1:11 | Gen 1 (10), 6:20 (3), 7:14 (4), Lev 11 (9), Deut 14 (4) — nowhere else in the Torah |
| poll גֻּלְגֹּלֶת ("skull", "poll") | 7 [7] | Exod 16:16 | Exod 16, 38; Num 1, 3 |
| fathers' house (house + fathers adjacent) | [69] | Gen 12:1 (the narrative's "your father's house") | Numbers 46 of the 69 |

THE CORRECTION to section 1's lineage table: the family key is NOT kept at every step. It is minted at 8:19, used in the nations table (10:5, 18, 20,
31, 32), ABSENT from Genesis 5, Genesis 11, Genesis 46 and Exodus 1 — the registers that run on names, sons, begot, years and died — and returns at
Exodus 6:14-27 ("these are the heads of their fathers' houses"; six family tokens), then carries Numbers. Two grains alternate in the ink: a COUNTED
grain keyed by family (the ark's exit, the nations, Numbers 1-4, 26) and a NAMED grain keyed by name (Genesis 5, 11, 46, Exodus 1). They are joined
at Exodus 6, Numbers 3 and Numbers 26 (chapter 26: 94 family tokens beside 42 "sons", 5 "begot", 5 names). The two grains the table was built with are
the ink's — found, not chosen.

### 4.2 The heading formulas — the ink's table headers and footers

A verse-initial אֵלֶּה ("these are") heads 101 verses in the Torah; 68 of them head one of five register nouns — sons (22), names (14), families
(12), the counted (9), generations (11: Gen 2:4, 6:9, 10:1, 11:10, 11:27, 25:12, 25:19, 36:1, 36:9, 37:2, Num 3:1). Measured by the numeral on the
line: a formula carrying a number CLOSES a register (the checksum), one without OPENS it. Generations 9 open / 2 close; names 13 / 1; sons 17 / 5
(Gen 46:15, 18, 22, 25 — the sub-totals 33, 16, 14, 7 — and Num 26:41); families 2 / 10 (Num 26:7 through 26:50 — each tribe's row closed by its
count); the counted 6 / 3 (Num 1:44, 2:32, 26:51 — the grand totals). Of the 101, 25 carry a number, 21 of those on a register noun. So the record
format at the ink's registers is HEADER → ROWS → FOOTER CARRYING THE CHECKSUM, and the header's noun says the grain: "the generations of" and
"the names of" open the named grain; "the families of" and "the counted of" close the counted grain.

### 4.3 The checksums — every declared total against its parts, by script

| register | parts → sum | declared | verdict |
|---|---|---|---|
| Gen 5 the book of Adam | begot-at + after = total, nine rows, and Noah (5:32; 9:28-29) | per row | 10/10 MATCH |
| Gen 11:10-26 Shem to Terah | begot-at, after | NO total written | the checksum column dropped |
| Gen 46 the descent | 33 + 16 + 14 + 7 = 70 | 66 (46:26), then 70 (46:27) | DIFFERS, then the ink restates |
| Exod 38:25-28 the shekels | 100 talents × 3,000 + 1,775 = 301,775 shekels = 603,550 half-shekels | 603,550 (38:26) | MATCH |
| Num 1 | the twelve | 603,550 (1:46) | MATCH |
| Num 2 | 3 × 4 camps → 4 sums → total | 186,400 / 151,450 / 108,100 / 157,600 → 603,550 (2:32) | MATCH, nested twice |
| Num 3 the houses | 7,500 + 8,600 + 6,200 = 22,300 | 22,000 (3:39) | DIFFERS |
| Num 3 the firstborn | 22,273 − 22,000 = 273; 273 × 5 = 1,365 | 273 (3:46), 1,365 (3:50) | MATCH |
| Num 4 | 2,750 + 2,630 + 3,200 | 8,580 (4:48) | MATCH |
| Num 7 | 12 × one prince's row | 7:84-88: 2,400; 120; 24, 60, 60, 60 | MATCH |
| Num 26 | the twelve | 601,730 (26:51) | MATCH |

The ark writes per-kind counts (7:2-3: sevens and twos) and no total. Two declared totals differ from their parts, and both are the seats where the
tradition supplies a hidden row — Jochebed born between the walls (Bava Batra 123a) and the three hundred firstborn Levites (Bekhorot 5a) — and both
are already DIVERGE cells in the engine (CJ3b; the Bamidbar runner's levites('delta') = 300). A declared total that differs from its parts is the
ink's way of writing a row it does not name.

### 4.4 Membership as of an event

The predicates sit at the register boundaries and nowhere else: "went out of the ark" Gen 8:16, 8:19, 9:10, 9:18; "came into Egypt" Gen 46:6, 46:7,
46:8, 46:26, 46:27, Exod 1:1; "came out of the land of Egypt" at the census heads Num 1:1 and 26:4; "the counted … in the wilderness of Sinai" Num
1:19 and 26:64 ONLY; "the number of names" Num 1 (fourteen seats — every tribe's row), 3:40, 3:43, 26:53 (the land); "lift the head" Exod 30:12, Num
1:2, 4:2, 4:22, 26:2, 31:26, 31:49. The ink never carries a count forward: the same families are re-counted whole at 26 and the changes are stated by
NAME (Er and Onan, Dathan and Abiram, Korach and the sons who did not die, Zelophehad's daughters, Caleb and Joshua) — twelve numerical deltas, none
explained by arithmetic. Registers are SNAPSHOTS at markers with named exceptions, not a running balance.

### 4.5 The law blocks and the receipts

The speech formula וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר ("and the LORD spoke to Moses, saying") opens 83 verses (Exod 11, Lev 32, Num 39, Deut 1;
Lev 23 five times, Num 3 four); the variant "and the LORD said to Moses" 67 (Exod 42, Num 21). The footers "these are the statutes / commandments /
judgments / words" (Exod 21:1; Lev 26:46, 27:34; Num 30:17, 36:13; Deut 1:1, 4:45, 12:1, 28:69) stamp PLACE and CHANNEL: "in Mount Sinai by the hand
of Moses" (Lev 26:46, 27:34; Lev 25:1's opening), "in the plains of Moab" (Num 36:13), "between a man and his wife" (Num 30:17 — a scope stamp). The
receipt כַּאֲשֶׁר צִוָּה יְהוָה אֶת־מֹשֶׁה ("as the LORD commanded Moses") closes 58 lines (Exodus 22 — chapter 39 eight times, 40 seven —, Leviticus
11 — chapter 8 six —, Numbers 17, Deuteronomy 8), eleven with "so did he / they" on the same line (Exod 7:6, 7:10, 7:20, 12:28, 12:50, 39:43, Num
8:3, 8:22 …). A law block has an issuer, a channel, a place stamp and a receipt. The case is the exception path — Num 27:5 "and Moses brought their
judgment before the LORD" → 27:11 "a statute of judgment" — and 27:21 names the query interface ("by the judgment of the Urim … by his mouth they go
out and by his mouth they come in").

### 4.6 The five structures and the engine — the answer to "can we determine the intended architecture"

| the ink's structure | its device | seats | the engine's part |
|---|---|---|---|
| register | header; footer carrying the checksum | 68 register headers, 21 closes with a number | the population table, two grains |
| event stream | dated lines; membership as of an event | 157 markers on the tape, 102 text-constrained | the tape and the clock |
| snapshot with named deltas | re-count whole; exceptions by name | 12 declared deltas, 0 derived | the delta rows, declared and labeled |
| law block | the speech opening; a footer stamping place and channel | 83 + 67 openings; 5 stamped footers | THE LOOP's installation registry (given_at, installed_by) |
| command and receipt | "as the LORD commanded Moses … so did he" | 58 receipts, 11 with "so did" | the ledger's debit and close |

The ink determines the DATA architecture (registers with headers, footers and checksums; keys; snapshots as of an event; deltas by name) and the
CONTROL architecture's shape (stamped law blocks; receipts; the case form). It does not determine the implementation (the files, the formats, the
language) and it cannot state an intent — it uses these devices at every register, consistently. Still unmeasured: whether the later books RUN the
registers (Ezra 2:62 the failed lookup; Neh 7:5, 7:64; Ezek 13:9; Exod 32:32's book).

### 4.7 The measurement's own miss

The date-row filter (year AND month AND day on one line) found two lines; the ink's date formula "on the first of the second month, in the second
year" (Num 1:1) carries no day-word, so the filter was wrong — the tape's 157 markers are the count. Filed so the gate does not repeat it. And the
chat's first numbers were off by a miscount (66 headers, 23 closes): the record's 68 and 21 are the script's.

### 4.8 What follows (the owner's word, 2026-09-11: "Yes let's do 1,3 then 2 in the next sitting")

1 — this section, the pointer in THE_WORLD.md, the finding in RESEARCH_LOG.md: DONE. 3 — the seeding's design settled beside its debt in
COMPILE_DEBT.md, nothing built: DONE (a register at its own marker; no roll-forward). 2 — THE REGISTER GATE, its own sitting next: the three
formulas read off the DB — every close carrying a number → a row on the population table or a declared reason; every receipt → a close on the
ledger at that verse or listed open; every footer's place stamp → the installation registry's given_at — probes to fail first, the script in
claim_labels_census.py's form, the first run READ, then the sweep. Then chapter 28.
