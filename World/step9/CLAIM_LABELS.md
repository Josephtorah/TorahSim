# THE CLAIMS LABEL DEBT — O11 (opened 2026-09-08, the last item of the open-items campaign before Numbers)

The debt as COMPILE_DEBT.md named it at sitting LR1 (2026-09-07): the frozen claims carry the middah
field (the inference-rule label the link review law demands of every claim seated from LR1 on) on a
few dozen rows only; the backfill of the rest was declared "an unbounded debt, named here". This file
is O11's record: the measurement by script BEFORE the design, the design (the label's home, the
vocabulary, the method, the gate), the batches as sized, and an append-only ledger of every batch as
run. Nothing in it was typed before its script printed it.

## 1. The debt as measured (2026-09-08, by script over logic/oral_audit/manifests/*_claims.json)

| measure | value |
|---|---|
| manifests (units with a claims file) | 166 |
| claims on file | 2,838 |
| rows carrying the middah key | 36 |
| of those, a NON-EMPTY label | 25 |
| of those, an EMPTY string ('') | 11 (gen_60 four, gen_61 three, gen_62 three, gen_63 one) |
| rows without a usable label (the debt) | 2,813 |
| claims beyond the LR1 ceiling (seated after the law) | 0 |

The earlier count "2,802 unlabeled of 2,838" counted the 36 rows with the KEY; eleven of them hold an
empty string, so the honest debt is 2,813. The 25 labels in use: E29 ten, E7 five, I2 four, E27 three,
E10 two, E5 one — every one a code from logic/MIDDOT.md, some with a parenthesized note (the gen_60-63
form, "E10 (repeated expression signifies)").

By book (claims / units): Genesis 1,663 / 73; Exodus 545 / 41; Leviticus 513 / 49; the three law-era
manifests of Exodus 21 (law01-03) 117 / 3. Per unit the debt runs from 2 to 44 rows, median 15.

By the claim's recorded SOURCE (the first name on the row's source field — the family decides how the
claim was derived, so it decides how the label is found):

| family | gen | exo | lev | law | all |
|---|---|---|---|---|---|
| Minchat Shai (the Masorah's notes: spelling, accent, maqqef, the written form) | 667 | 115 | 27 | 0 | 809 |
| Onkelos (the received translation) | 61 | 117 | 15 | 0 | 193 |
| Kitzur Baal HaTurim (letter-values, initials and finals, the concordance pair) | 258 | 154 | 2 | 0 | 414 |
| Sifra (the Leviticus law's own verse-by-verse teaching) | 1 | 0 | 450 | 0 | 451 |
| Bereshit Rabbah | 446 | 0 | 0 | 0 | 446 |
| Mekhilta | 10 | 20 | 0 | 2 | 32 |
| Talmud, Mishnah, Tosefta, Sifrei (case rows and sugyot) | 194 | 118 | 19 | 8 | 339 |
| other midrash (Tanchuma, Pesikta, Pirkei, Seder Olam, Soferim) | 10 | 18 | 0 | 1 | 29 |
| the later commentators (Rashi, Ramban, Torah Temimah, the law-era bibliography) | 9 | 1 | 0 | 66 | 76 |
| other (the law-era bibliography rows; four "the stream's own census" rows; one "the reading tradition") | 7 | 2 | 0 | 40 | 49 |

The machine's CHECK types on the rows (the verifier's own instrument): none 947, manual 618,
token_count 502, he_contains 404, adjacency 98, verse_token_count 70, maqqef_after 50, letters_multiset
37, final_letters 30, mark 22, spelling_variants 22, initial_letters 18, verse_word_count 18, career 1,
machine 1. A check type is the MACHINE'S verification of a fact in the claim, not the claim's inference
form: a Baal HaTurim row checked by final_letters asserts an acronym reading (E30), and the check only
confirms the letters.

A keyword census over the full claim text (gematria, notarikon and initials, a-fortiori, verbal analogy,
repetition, symmetry, parable, the general-and-particular forms, context, the third verse, the order
rule, spelling and mark words, grammar words, translation words) hits 1,695 rows at least once, 402 rows
more than once, and 1,143 rows not at all. The census is the reader's aid; it decides nothing.

THE LEDGERS DO NOT CARRY THE LABEL: zero lines anywhere under logic/ or World/step9 tie a claim id to a
middah code (the ledgers name a middah in prose on 43 files, never beside a claim id). The recorded
derivation the script can reach is the manifest row itself: the source, the claim text, the check.
So the plan's "where the ledger names the move, by script; the rest by reading" collapses to ONE path:
every label is READ off its own row, with the script's proposal printed beside the row as the aid.

## 2. The two strata

The claims live in two strata. The MANIFEST (logic/oral_audit/manifests/<unit>_claims.json, a JSON
list of rows: id, source, ref, claim_en, check) is the verifier's stratum — verify_claims.py reads the
middah field HERE (the LR1 gate). The frozen UNIT (logic/units/<unit>.yaml) seats the same ids as
"[claim ID]" markers inside its steps' prose: 154 units carry 1,191 of the 2,838 ids; 1,647 ids appear
in the manifest only; 12 older units (gen_02/03/04/07, exo_07/08/09/10/14, law01-03) carry no marker at
all. The unit stratum has no per-claim label field (gen_04's three `middah:` fields sit on ORAL_ entries
of the pre-manifest era and stay as they are). THE LABEL'S HOME IS THE MANIFEST ROW — one field, one
place, the place the gate reads. The manifest files are rewritten byte-for-byte by
json.dumps(indent=1, ensure_ascii=False) plus a newline (verified against the files before the first
write); adding the field changes nothing else in a row. holdings.py and the verifier are the only
readers of the manifests (measured by grep); both tolerate the field.

## 3. The vocabulary (a label is a CODE, then an optional parenthesized note; the code is what the gate lints)

- `ink` — the claim reads ITS OWN VERSE: the written form (a spelling, an accent, a maqqef, a count of
  words or letters, a word order, a grammatical form), or the received translation's rendering of it.
  The Masorah's comparison of forms across seats ("full here, lean there") is still ink — forms are
  compared, no rule moves. Minchat Shai and Onkelos rows are ink BY NATURE; each is scanned for the
  exception that carries an inference (a gematria, a concordance pair, an a-fortiori) and the exception
  takes that inference's code.
- `I1`..`I13` — the thirteen of Rabbi Ishmael, for a claim that derives a LAW; `E1`..`E32` — the
  thirty-two of Rabbi Eliezer, for a claim that reads NARRATIVE (logic/MIDDOT.md). The twins (I1/E5 the
  a-fortiori, I2/E7 the equal decree by shared wording, I3/E8 the paradigm case, I13/E15 the third
  verse) take the I code where the claim's conclusion is a rule of conduct or ritual and the E code
  otherwise; the unit's book is the script's default, the claim's own conclusion is the reader's rule.
- `E7` (the concordance pair — "the word stands exactly twice: here and there, to teach") is the Baal
  HaTurim's signature move and the largest single form in the debt; `E29` gematria (letter-values);
  `E30` notarikon (initials, finals, an acronym; an anagram of the same letters is noted under E30);
  `E10` repetition signifies; `E27` symmetry (a mirror, measure for measure); `E26` the parable; `E31`
  and `E32` the order rule; `E1`/`E2` the inclusion and restriction particles — used ALSO in a law span
  for the Sifra's "to include / to exclude" readings, with the note that the thirteen carry no row for
  Rabbi Akiva's particle method; `I4`..`I11` the general-and-particular and singled-out forms where the
  Sifra names the structure; `I12` context; `I13` two verses until a third.
- `plain` — a teacher's plain statement with no inference form the catalog names: an identification
  (Shem is Malkizedek), a narrative expansion, a recorded dispute, a translation's choice explained by
  the teacher's own reasoning. The eleven empty strings of gen_60-63 were this class left blank; they
  take the word.
- `M-NN` — a claim whose recorded derivation is a catalogued compile move (logic/MOVE_CATALOG.md) with
  no middah twin: M-22 the run read back into the spec, M-23 the second seat's delta, M-24 the
  repetition test, M-18 the freed token, and their kin. Where a move HAS a middah twin (M-02 is I1's
  form) the middah leads and the move follows in the note.
- `H` — an untaught TRANSFER of our own: the source is the stream's own census (not a teacher) and the
  claim moves a rule or a meaning between passages on a shared word. The link review's class H: the
  value kept, the flag changed, never counted as compiled. Expected on a handful of rows (four "the
  stream's own census" sources, one "the reading tradition").
- A claim carrying two forms takes the LEADING form as its code and names the second in the note
  ("E29 (gematria) with E7 (the pair)"). The note is English only.

## 4. The method (every batch)

1. The script prints the batch: every row's id, source, check type, and claim text, with a PROPOSED
   code computed from the row (the source family's nature; the check type's form; the keyword hits),
   and the flags that raised it. The proposal is the reader's aid.
2. The reading: each row's label is DECIDED by reading the row — the whole text where the proposal is
   an inference form or a flag fired; the head where the proposal is `ink` by nature and no flag fired
   (the full-text keyword scan is the script's, so an inference word deep in the row still flags it).
   The decisions are typed as a table {id: label} in the batch's decision file (scratchpad, then
   copied into this record's ledger by counts, with every exception named).
3. The apply script writes the labels into the manifests (the byte-faithful dump), then runs
   verify_claims.py on every touched manifest (0 FAILED, the LR1 gate unchanged) and the census gate.
4. The record: this file's ledger gains the batch's entry (counts by code, the exceptions to the
   proposal with their reasons, the H rows); COMPILE_DEBT.md's debt line carries the running count; the
   state doc its checkpoint.

## 5. The gate — logic/solo_tools/claim_labels_census.py (written before the first label; run to FAIL first)

Reads every manifest; prints the census (by book, by unit, by code) and FAILS on: a middah key whose
value is empty or whitespace (the eleven — the gate's first run fails on exactly these); a label whose
leading code is not in the vocabulary of section 3; a label carrying a Hebrew letter (the note is
English only). It does NOT fail on an unlabeled row — the debt is printed, not failed, until the last
batch lands; THEN the debt line becomes a failure condition (`--strict`), the O11 close.

## 6. The batches (sized from section 1)

| batch | rows | how |
|---|---|---|
| B1 THE INK LAYER — Minchat Shai + Onkelos, all books | 1,002 | ink by nature; each row scanned, flagged rows read whole; exceptions take their form |
| B2 THE KITZUR LAYER — Baal HaTurim, all books | 414 | E29 / E30 / E7 / E10 proposed from the check type and the keywords; every row read |
| B3 GENESIS'S TEACHERS — Bereshit Rabbah, Talmud, Mishnah, Mekhilta, the rest, in unit order | 677 (25 already labeled inside it) | every row read; the eleven empties become `plain` or their form |
| B4 EXODUS'S TEACHERS + THE LAW-ERA MANIFESTS — Mekhilta, Talmud, Tanchuma, the bibliography rows | 276 | every row read |
| B5 THE SIFRA — Leviticus's teachers | 469 | every row read; the I forms |

Sum 2,838 = 2,813 + 25. Sittings: B1 and B2 this sitting (1,416 rows, half the debt); B3-B5 over the
sittings after, as many as it takes, each closing with the gate green and this ledger appended.

## 7. Predictions (typed before B1 runs)

- B1's exceptions to `ink` are few: Minchat Shai rows that carry a Talmudic reading of the consonants
  stay ink (a reading of its own verse); Onkelos rows that carry a Tanchuma or Bereshit Rabbah reason
  beside the rendering stay ink with the teacher noted; a row asserting a concordance pair or a
  gematria takes E7 or E29. Under twenty exceptions of 1,002.
- After B1 the gate still FAILS: eight of the eleven empties are Bereshit Rabbah rows (B3's).
- No claim id, ref, source, claim text, or check changes; the corpus world's hash cannot move (its
  basis is facts, open demands and names — the manifests are not in it) and is not claimed as a test.

## BATCH LEDGER (append-only)

### THE GATE'S FIRST RUN (2026-09-08, before any label): FAILED, 12 lines
The eleven empty strings of gen_60-63 as predicted, and a TWELFTH the design had not seen: G61-17's
label reads "E29 (letter-values) / numeric count" — text after the closing parenthesis, outside the
vocabulary's shape (code, then one parenthesized note). The census counts it as unlabeled until B3
normalizes it to "E29 (letter-values; a numeric count)"; the honest count at the gate's first run is
therefore labeled 24, debt 2,814. The gate's FAIL was read line by line, not assumed from its exit code.

### THE MANIFESTS' FOUR SHAPES (found at B1's first apply, 2026-09-08)
Section 2's "byte-for-byte by json.dumps(indent=1, ensure_ascii=False) plus a newline" had been verified on ONE
file. The apply script's faithfulness guard (dump the unmodified rows again and compare to the file before writing)
refused 162 of 166 manifests on the first run. Measured by script over all 166: 122 are indent 1 with the Hebrew
unescaped and NO trailing newline (gen_38 too — the one file checked had been read with its newline assumed);
24 are indent 2; 16 are indent 1 with the Hebrew escaped; the three law-era manifests are one compact row per
line between '[' and ']'. The one file written before the guard (exo_16, three labels) gained a trailing newline
and was restored. The apply script now DETECTS each file's shape from its own bytes and writes it back in that
shape — the guard stays, so a fifth shape would refuse, never corrupt. Lesson: A FORMAT VERIFIED ON ONE FILE IS
A GUESS ABOUT THE OTHERS — the guard, not the sample, is what kept the manifests whole.

### B1 THE INK LAYER — DONE (2026-09-08): 987 labels in 114 manifests; 15 deferred
The 1,002 Minchat Shai and Onkelos rows printed compactly (the Hebrew runs stripped to a marker, the heads at
two hundred characters, every row with an inference flag printed whole — 194 of them) and read whole in eight
pages. Labels written: ink 975 (972 by the source's nature plus the three of exo_16), E7 1, E1 1, E2 1, M-22 7,
M-23 2. DEFERRED to B5: the fifteen Onkelos rows of Leviticus (lev_06, lev_07, lev_08, lev_18), whose claims are
Sifra bundles carrying the law's own forms — read in the Leviticus context, not here. THE EXCEPTIONS (31, every
one used):
- EX09-03 E7 — the one Masorah-pair row whose conclusion is the Kitzur's as-there-so-here reading (the
  he/alef pair; the repeat-offender rule read from it).
- EX25-03 E1 and EX31-03 E2 — the case shelf's particle readings carried on an Onkelos row ("so shall you
  make" including the generations; "but My Sabbaths" bounding the labors).
- The twenty compiled-run rows of Exodus 23-40 (an Onkelos source, a claim that is a cold runner's report):
  nine whose headline IS a catalogued move took the move — M-22 the run read back into the spec (EX25-15,
  EX28-15, EX31-09, EX35-08, EX37-07, EX39-06, EX40-08) and M-23 the second seat's delta (EX29-16, EX34-12);
  the other eleven took ink with the runner named ("the compiled run — cold_run_X.py; the answer sheet's rows
  as test data"), the runner's name read from the claim by script, never typed.
- Nineteen ink rows carrying a named rider (a letter-value, a concordance pair, an exclusion, a parable, a
  doubled-word count, the Mekhilta's revocalization at EX14-01): the written form or the rendering leads, the
  rider's code named in the note — never promoted to the leading code, because the row's ASSERTION is the
  form and the rider is what the teacher did with it.
- The corpus's own pair-observations (G69-07's two lean "to teach", G65-21's word career, EX02-02's two arks)
  stay ink: forms compared, no rule moved — no H in this batch; every source is a teacher.
The verifier (verify_claims.py) ran on all 115 touched manifests: 0 FAILED everywhere (1,272 verified, 600
uncheckable, 348 no-check as before; the LR1 gate's count of new claims 0). The census after B1: labeled 1,011,
debt 1,827, the nine Genesis failures of B3 standing.

### B2 THE KITZUR LAYER — DONE (2026-09-08, the same sitting): 414 labels in 84 manifests
The 414 Kitzur Baal HaTurim rows printed with the script's proposal beside each (E30 from the letters check
types, E7 otherwise) and read whole in six pages. Labels written: E7 283, E30 51, ink 39, E10 21, E29 12, I2 6,
E28 1, M-22 1. THE READING'S RULES, applied row by row (96 exceptions typed, 95 used — L19-03 is a Minchat Shai
row, labeled ink at B1):
- E7 is the Kitzur's signature and the batch's bulk: "the word stands exactly twice — here and there" with the
  reading drawn across the pair. It stays E7 (narrative strength) even in the Decalogue and the ordinances
  unless a RULE OF CONDUCT is carried on the pair — then I2: the maidservant likened to the wife on the shared
  exit-verb (EX21-05), the garment/betrayal pair (EX21-03), the stoning protocol for the generations from the
  mountain-toucher and the ox (EX19-10), the fast-day rule from the locust's rest (EX10-04), the addition to the
  Sabbath from the two seats' word order (EX16-09), the Sabbath limit and the court's lash from the three
  let-none-go-out seats (EX16-10).
- E10 for a word counted INSIDE its own passage (five bushes, three place-words, ten namings, the two
  conceivings, eight my-lords); E7 for a whole-Torah or whole-Scripture concordance. The physician's license from
  the doubled heal-verb (EX21-07) is E10 at law strength.
- E29 where the claim's CONCLUSION is a letter-sum (the awl's four hundred, the thick cloud's Presence, the
  Decalogue's crown and its Abraham-word, the shortness-of-breath's 430, the not-eaten ox's no-benefit — a
  halakhah carried by arithmetic); a letter-sum riding a pair stays in the note (EX20-01, EX18-01, G37-03,
  G41-11, G54-05).
- E30 for initials, finals, anagrams, and a name split into words (Rephidim as slack hands, EX17-06; the
  disease-word as bread and salt, EX15-06); the eight closing mems of the gift-verse (G55-02) are finals.
- ink for the verse's own count or written form with the Kitzur's homily on it and no rule moved: the seven
  hundred-word blessings (G30-02 to 08), the five-word Sabbath verse, the two tellings of the court-day and
  their two extra letters (EX18-07), the lean spellings read (G38-27, G41-17, EX20-07's world-to-come yod),
  the compass-scan and the twins' spellings compared, the paseq the stream does not write (EX15-07), the
  come/go dispatch rule (EX10-12), and the chapter remainders whose one checked anchor is a count or an
  adjacency (EX02-13, EX03-13, EX07-12, EX09-13).
- M-22 once: the doorposts-then-lintel command against the lintel-then-doorposts performance, the
  order-indifference rule read from the delta (EX12-11) — the Kitzur's own exemplar of the run read back into
  the spec. E28 once: the juxtaposition across the portion's seam (EX06-14).
- Measure for measure (E27) is the READING's content on five pairs (G46-16, G62-09, G44-17, G37-04, EX14-07);
  the device is still the pair, so E7 leads and E27 sits in the note.
- No H: every row's source is the Kitzur, a teacher; the corpus's own wires beside his readings are named as
  the corpus's and move no rule.
The census after B2: labeled 1,425, DEBT 1,413 — Genesis's teachers 653 (B3), Exodus's teachers 159 and the
law-era manifests 117 (B4), the Sifra and Leviticus's teachers 484 (B5, the fifteen deferred Onkelos rows among
them); the gate's nine Genesis failures stand until B3. The verifier loop over all 115 modified manifests after
B2: 0 FAILED everywhere (1,272 verified, 600 uncheckable, 348 no-check — the same tallies as before any label,
which is the proof that a label changes nothing the verifier checks). The diff over the 115 files is one added
line and one changed line per label and nothing else.

### B3 GENESIS'S TEACHERS — DONE (2026-09-08, the first sitting after compaction #104): 653 labels in 69 manifests
THE SELECTOR'S MISS FIRST: the batch printed 676 rows, not 677. Measured by script over all 2,838: one row was selected
by NO batch — G11-18 (gen_11), whose source opens "Sifra, Shemini, Mekhilta DeMiluim" and whose family the printer
therefore read as the Sifra, which B5 selects for Leviticus only. B3 now selects every Genesis row that is not Minchat
Shai, Onkelos, or the Kitzur; the five batches re-summed to 2,838 by script before the print was re-run. The print
compacted by a split script (the Hebrew runs to a marker, the source cut to seventy characters, every row WHOLE — a
teacher's row has no head to trust) into seven parts of sixty thousand characters, each read in two pages. Written:
652 rows without a label plus G61-17 RELABELED from "E29 (letter-values) / numeric count" to "E29 (letter-values; a
numeric count)" — the apply script gained a RELABEL table for exactly that case; the eight empty strings of gen_60-63
took `plain`, the class the design predicted for them. By code: plain 432, ink 88, E7 19, I2 17, E10 15, M-11 11,
E26 9, M-09 9, E2 7, E27 6, M-23 5, E5 5, E30 4, E1 3, E28 3, E29 3, M-03 3, M-16 3, E15 2, E32 2, I1 2, I3 1, M-05 1,
M-12 1, M-22 1, M-24 1. THE READING'S RULES, every row decided by hand (the decisions file lists all 640 read rows;
the twelve compiled-run rows took B1's "the compiled run — cold_run_X.py" with the runner's name read by script —
five on cold_run_pre_sinai.py, seven on cold_run_family.py — and G01-08, whose headline IS the spec/run pair, M-22):
- THE HEADLINE ASSERTION LEADS. A teacher's row in Genesis bundles two to five readings; the code is the form of the
  row's headline claim, the other readings named in the note as riders (B1's rule). Where a headline names two
  co-equal things, the CATALOGUED FORM wins over `plain` (G09-13 the orphan's wife by the shared for-him; G25-13 the
  name-of-other-gods analogy; G37-29 the suspected wife's a-fortiori; G46-37 the doubled good).
- `plain` is two-thirds of the batch (432): the identification, the narrative expansion, the recorded dispute — and
  the largest class inside it, THE VERSE'S OWN WORDING OR ACT READ AS THE RULE with no catalogued form: "from where do
  we know X? from here" — the detached blade from the knife taken, the vessel duty, the mourner's exemption from
  Abraham rising, the ten years in Canaan, the escort from the bringing verb, walking the land as acquisition, the
  wage-earner's day from the shepherds' rebuke, the seven days of mourning at 50:10. The tradition names no middah for
  these; the label says so rather than borrowing one.
- `ink` (88) where the COUNT OR FORM is the assertion: the seventy-one Names to 3:13, the eight my-lords against the
  eight reigns, the herald's hapax, the dotted words at their four seats and the dots-equal-letters case, the Names'
  holy-or-profane pointing (five stations), the scribal emendations, the grammar rule of the directional heh at its
  three seats, the chain's own counts that FAIL against the corpus (the first aging, the eighteen mentions) recorded
  as the chain's premise, and the tense or gender forms read (I-have-given; the feminine noun with the masculine
  participle). The four "the stream's own census" rows and the one "the reading tradition" row assert counts and
  NAME the readings; none transfers a rule of ours — NO H in this batch either.
- E7 (19) for the narrative pair; I2 (17) only where a rule of conduct or ritual rides the shared word: the seven
  laws wired token by token at Sanhedrin 56b (and their disputed wiring), the money betrothal from Ephron's field,
  the afternoon prayer's meditation-verb and the morning's standing, the bride's year, the quorum of ten, the sea's
  its-kind, the ason pair, the found-found chain, the levirate name at 48:6, affliction at Yom Kippur, the analogy
  WEIGHED AND DECLINED at Yevamot 17b (I2 with the refusal in the note). Measure for measure carried on a pair keeps
  B2's rule — E7 leads, E27 in the note (G46-31, G46-34, G65-29, G66-24); E27 leads where the mirror is the device
  (six restraints for six honours, the sister's name for the brother's, the rending repaid).
- E10 (15) for the doubled or redundant expression: the no-no oath and its cap, the doubled tithe verb's two tenths,
  the doubled circumcise-verb fought between the two grammar schools, the mourner's doubled from-before, the plea's
  three terms, she-had-no-child; whoever's name is repeated in Moses' blessing (G70-21, checked across all eleven).
- THE MOVES where the recorded derivation is a catalogued compile move with no middah twin: M-11 THE WORD-ORDER READ
  (11 — the sentencing order, the ark's two rosters, the way before the tree, from man to beast, the priesthood's
  clause-order slip, the servant's disclosure, Isaac before Ishmael, children married first, the ladder's ascending,
  Zebulun before Issachar); M-09 THE KEYWORD DICTIONARY (9 — spoke against said, angel-of-the-LORD against angel-of-
  God, the pure-bird test, shearing, the day-old ram, the plain kid, whoever-approached, sons over one son, a tribe a
  congregation); M-23 THE SECOND SEAT'S DELTA (5 — the praise rule twice, the wellsprings' dropped quantifier, the
  dropped earth-title, the appended with-you at Exodus 13:19); M-16 THE REVOCALIZATION (3 — kenegdo, a-people-like-
  the-donkey, the ox as the wall); M-03 THE COMPARISON (3), M-24 THE REPETITION TEST (1 — the repeated-at-Sinai
  framework itself, at its own statement), M-05, M-12, M-22 one each.
- The twins by the conclusion: E5 five against I1 two (the clean-speech rule from the circumlocution's extra letters;
  the bathing duty from the statue-scrubber); E15 two (the birds' two origins; the two clocks of Genesis 15); I3 once
  (any divination not like Eliezer's — the exemplar DEFINING the class); E32 twice (Terach's death before the call;
  the pieces before chapter 12); E26 nine; E30 four (old as this-one-acquired; the grudge verb's acronym; the acronym
  rule's own proof-seat at 17:5).
The census after B3: labeled 2,078, DEBT 760 — Exodus's teachers 159 and the law-era manifests 117 (B4), the Sifra and
Leviticus's teachers 484 (B5); Genesis 1,663 of 1,663; THE GATE PASSED for the first time since it was written, 0
failure lines. The diff over the 69 manifests: 1,297 lines added and 653 deleted — 644 rows gained a line, nine rows
(the eight empties and G61-17) changed one in place, nothing else moved. The verifier loop over all 115 modified
manifests after B3 (the 73 of Genesis among them): 0 FAILED everywhere, 1,272 verified, 600 uncheckable, 348 no-check,
the LR1 gate's count 0 — the same tallies as after B2 and as before any label. Lesson banked: A BATCH SELECTOR IS
RE-SUMMED TO THE WHOLE BEFORE ITS PRINT IS TRUSTED — the design's 677 was right, the printer's 676 was the miss, and
only the script that put every row into some batch found the one that fell between them.

### B4 EXODUS'S TEACHERS + THE LAW-ERA MANIFESTS — DONE (2026-09-08, the same sitting as B3): 276 labels in 36 manifests
THE RE-SUM FIRST (by script): 2,838 = 1,002 + 414 + 677 + 276 + 469, no row in two batches, none in none. The batch: the 159
teacher rows of Exodus (the Mekhilta 20, the Tanchuma 17, the Mishnah exam rows seated at their verses, the Talmud block bundles
of the campaign, the one "stream's own census" row EX03-02) and the 117 rows of the three law-era manifests (law01-03 — the
Exodus 21 reading's bibliography rows: the Torah Temimah, the two Mekhiltas, the later commentators, one compact row per line);
four compact parts read in seven pages. THE ID COLLISION, found at the dry check by script before the apply: L0-01 and L0-02
stand in BOTH law02 and law03 (the law-era manifests number their chapter-level rows from L0 per unit), and the apply script
keys its exceptions by id alone — the four rows were pulled out of the exceptions and dispatched by UNIT in the decisions
module's default; the dry check itself keys every row by (unit, id). ⚠ A CLAIM ID IS UNIQUE ONLY WITHIN ITS MANIFEST. Written:
276 — plain 148, E10 17, ink 15 (twelve read; three compiled-run rows on cold_run_ordinances.py by B1's convention, the runner's
name read by script), E2 11, M-09 11, M-23 8, I2 7, M-05 6, E27 5, M-11 4, I6 4, I1 3, I3 3, M-03 3, M-08 3, E1 2, E28 2, I13 2,
M-07 2, M-12 2, M-16 2, M-20 2, M-24 2, and one each of E12, E30, E32, I8, I11, I12, M-01, M-04, M-06, M-10, M-13, M-15. THE
READING'S RULES — B3's, plus THE BUNDLE RULE: a filed finding (the exam-block "F-NNN" rows) or a law-era row bundles five to
ten legs under one headline; the FIRST leg's form leads and every later leg's catalogued form is named in the note, so the
census counts one form per row and the note keeps the rest. Applied row by row:
- THE COMPILER-SEAT ROWS NAME THEIR OWN MOVES and the label takes them: M-09 and M-07 at EX21-15, M-07 at EX21-18, M-08 at
  EX21-19, M-06 at EX21-20, M-05 at EX21-21, M-01 with M-03 at EX22-11, M-04 at EX22-13, M-10 at EX22-14; M-15 THE VOICE READ
  at EX13-16 (the claim names it); M-16 at EX20-20's finale (the human face), EX21-25 (designate read as inform-her), EX23-13
  (shall-see and shall-be-seen). Where the move has a twin the middah leads: EX22-12's M-02 is I1.
- THE TRADITION NAMES ITS OWN MIDDOT in eight rows and the label takes them: I12 the context middah at EX21-26 and L16-02;
  I6 at L26-01 (tooth and eye) and at EX25-14 — THE METHOD FORK, Rebbi's general-particular-general against the
  amplify-limit-amplify engine, both tables recorded under the one code with the rival named; I8 at EX35-06 (kindling singled
  out); I11 at law02's L0-02 (the class-exit operator with a-day-or-two as its return clause); E12 at L9-02 (it came to teach
  and was taught); E32 at EX25-09 (no earlier-and-later, the Tanchuma's own words).
- M-23 THE SECOND SEAT'S DELTA (8) is the law-era's signature: found against seen, father-first against mother-first,
  your-cattle against your-ox-and-donkey, the vain clause against the false, the gender grid from the two seats, the two
  when-brings-you skeletons, one-who-strikes against a-man-who-strikes, testified against it-was-known. M-09 THE KEYWORD
  DICTIONARY (11): the powers-word as judges, bride-price as the marriage document, the when-word's senses, the blasphemy
  verb from Balaam, goring is the horn, the festival-word is the offering, the for-Me token, forever means the jubilee, the
  if-word obligatory, the preposition system, the piercing's court.
- E2 (11) at law strength as the vocabulary allows: the law spans' word-by-word exclusion tables — the appearance table, the
  five disqualified, the pit's ox-and-not-a-man, the refuge's word battery, the altar's to-die, his-fellow's ox, before-them,
  the object-particle's intent, the yet-particle dividing the day, for-you, you-and-not-the-heir. E10 (17): the doubled verbs
  at law strength — say-he-shall-say, heal-he-shall-heal, surely-be-put-to-death, the doubled count-verbs, the doubled morning,
  the doubled exit, Shmuel's doubled death-verb, the three nouns of 12:6, the extra ox and sheep tokens, ox seven times.
- `ink` (12 read): the count or form as the assertion — the singular camp-verb's three seats, the visit-formula's four
  stations, the frontlets' spelling census, the hooks' vav, the read form against the written skeleton, the imperfect
  if-he-schemes, the bound suffix's guarding grade, the pit clause's missing word with its full and defective spellings, the
  verse's own two indemnities and five-and-four pattern, the received translation's torn-from-the-living.
- `plain` (148): the answer sheet's rows seated at their verses, the Tanchuma's expansions, the bundles whose first leg is a
  reading or a recorded dispute, the law-era rows' case law and rationale stacks. L11-05's ten links between the block's
  clauses and the narratives each carry their commentator — taught, so not H. NO H in this batch either.
The census after B4: labeled 2,354, DEBT 484 — the Sifra and Leviticus's teachers with the fifteen deferred Onkelos rows, all
of B5; Exodus 545 of 545, the law-era manifests 117 of 117, Genesis 1,663 of 1,663; THE GATE PASSED, 0 lines. The diff over
the 36 manifests: 435 lines added and 276 deleted — the 117 law rows one compact line changed in place each, the 159 Exodus
rows one line gained and one changed each; the three law-era files kept their one-row-per-line shape (the guard's fourth shape).
The verifier loop over all 120 modified manifests after B4: 0 FAILED everywhere, 1,272 verified — the same count as after B2
and B3 and as before any label — with 619 uncheckable and 481 no-check, the growth from B3's 600 and 348 being exactly the 152
rows of the five manifests newly in the loop (exo_22, exo_23, and the three law-era files, none of which B1-B3 had touched),
measured by script; the LR1 gate's count 0. Lesson banked: A CLAIM ID IS UNIQUE ONLY WITHIN ITS MANIFEST — key every table by
(unit, id); the apply script's id-keyed exceptions would have given law03's two chapter rows law02's labels, and only the
unit-keyed dry check saw it.

### B5 THE SIFRA + LEVITICUS'S TEACHERS + THE FIFTEEN ONKELOS ROWS — DONE (2026-09-09, the first sitting after compaction #107): 484 labels in 49 manifests
THE MEASURE FIRST, by script: the 484 unlabeled were Leviticus alone — the Sifra 450, the Talmud and Mishnah teachers 19, the
Onkelos family 15 — with no claim id repeating across units among them, and NONE of the fifteen Onkelos rows labeled at B1. So
the move was made in both selectors at once: B1 gave up Leviticus's Onkelos family and B5 took it, and the five batches were
summed again before the print — 987 + 414 + 677 + 276 + 484 = 2,838, no row in two batches, none in none. The print (484 rows;
64 flagged; the proposal blank on 427 — a Sifra row's text rarely names its own structure) was split into three compact parts and
read whole in five pages; every row decided by hand into the decisions file (484 entries, none left to the default). THE DRY CHECK
by (unit, id): 484 decided, none missing, none stray, no id repeating, no bad code, none already labeled, no Hebrew in a note; the
gloss lint on the notes found one hyphenated word, reworded, then 0. APPLIED: 484 — plain 330, ink 25, I3 13, M-09 13, E2 12,
E10 12, E1 9, I2 9, M-11 7, M-12 7, M-03 6, M-22 5, M-23 4, and threes of E26, E27, E28, I1, I8, M-05, M-10, two of I13, ones of
E30, E32, I4, I11, I12, M-13, M-16, M-18, M-20. The diff measured by rebuilding each manifest's pre-apply dump in its detected shape:
968 lines added, 484 deleted — every row gained a line, none changed in place, no unfaithful shape. THE READING'S RULES — B3's and
B4's, applied to the Sifra's own bundles:
- THE BUNDLE RULE GOVERNS THE SIFRA. A Sifra row here bundles two to ten readings of one passage under a headline; the FIRST leg's
  form leads and every later leg's catalogued form is named in the note ("the doubled morning, E10, beside"). This is why `plain`
  is two-thirds of the batch (330): the first leg is most often the Sifra reading the verse's own wording as the rule — a
  definition, a role table, a case matrix, a recorded dispute — with no catalogued form; the tradition names no middah for these
  and the label says so.
- THE TRADITION NAMING ITS OWN MIDDAH TAKES THE LABEL: I11 at LV07B-01 (the school of R. Yishmael naming Hermeneutical Principle
  11 on the thank offering's loaves); I3 at LV07B-07 (the building principle named as Principle 3 from the investiture's burn
  clause) and at LV16B-01, LV16B-04, LV08-03, LV11A-08, LV11B-05, LV11B-13, LV14A-05, LV21B-02, LV25A-01, LV01A-01, LV07C-04 — the
  exemplar generalized; I8 went-out-to-teach at LV02-07, LV06-09, LV25A-04; I4 general-and-particular at LV18-04; I13 the
  two-verse resolution at LV07A-06 and LV19B-06; I12 context at LV26-02; I1 at LV07C-01 (weighed and refuted — the refusal in the
  note), LV12-02 (the a-fortiori's own case law, sufficiency), LV20-06; I2 only where a rule of conduct or ritual rides the shared
  word (the shofar from the Jubilee twice, the fill-fill fistful, affliction by the hunger analogy, the body's impurity with
  Num 19:13, talion as payment on the strike-verb, the acquisition modes on 'possession', the named verbal analogy at LV25C-12).
- E1/E2 AT LAW STRENGTH for the Sifra's to-include and to-exclude on a particle or a word (the vocabulary's note): 'to him',
  'his hand', the species words, 'the sons of Aaron', 'from your neighbor's hand', 'of the seed', 'it' bounding the work ban;
  'every male', 'all his flesh', 'on the day', 'the holy things', 'any man'. E10 for the doubled or tripled expression read
  (the tripled slaughter-verb, the tripled tent clause, linen four times, the doubled six-years, the tripled uncircumcised
  root, 'the second ram' re-stated). E27 the mirror (the sin-bird's rite, the calf for the calf, one verb in good and evil);
  E26 the parable (the princess, the falling load, the long laborer); E28 the juxtaposition (the sanctuary beside the Sabbath,
  the Sabbath beside the festivals, the corner among the festivals); E30 the acronym (the elder); E32 the transposed verse.
- THE MOVES with no twin: M-09 the keyword (13 — peace in the name, congregation is the court, burn against boil, 'his tent',
  keep and do, dwell as you live, walking is study, casual for casual, faintness, 'in his brother', the perpetuity word,
  excision is destruction, malignant as loss); M-11 the order (7 — parch before grind, the whole section in order but one
  verse, the dues after the fat by Num 5:31's clause order, the five verbs' escalation, the burnt offering written first and
  set aside, the seven states, the fathers reversed); M-12 the number (7 — the two verb-numbers, the elders' plurals, 'shall
  THEY slaughter', 'they shall take out', 'praises', 'years of crops', 'the laws'); M-03 the comparison (6); M-22 the run read
  back into the spec (5 — the investiture ram verse for verse, the eighth day's run graded and teaching, the Sinai word
  understood at the event, the Writings' log quoting the Sabbath-debt clause); M-23 the second seat (4 — the ram's list
  against the lamb's, the lamp against Exod 27:20, iron against brass, the second half's clauses by call); M-10 the pointer
  (3); M-05 the parse (3 — 'many days' to its minimum, the forty seah out of 'all his flesh', forty-nine); M-13 the position
  (the guilt offering's 'it'); M-16 (LV20-05's revocalization twice); M-18 the freed token (the eating clause re-typed onto the
  slaughter); M-20 (Lev 19 arming Exodus 22 and Leviticus 5).
- THE FIFTEEN ONKELOS BUNDLES take the Sifra leg's form with the received translation named as the ink leg: plain nine, I13,
  I3 twice, I2, M-03, E10 — and `ink` once, LV18-05, where the translation's parse of the sister clauses IS the claim.
- THE COMPILED AND FILED ROWS: LV09-10 M-22 (its headline is the run graded against its spec, as G01-08 at B3; the runner's
  name in the note); `ink` where a token census is the assertion — the tail token's two seats, the domain phrase at five, the
  clocks summed, the purity verb's four seats, the pairs engine's three seats, the fifteen women computed from the verse's own
  relation terms, the mixture noun thrice, the hapax tokens, the sanction vocabulary, the six kin tokens, the twelve class
  heads, eating fourteen times, the acceptance root at seven, Shavuot's numerals (17 rows); the answer-sheet rows seated
  `plain` (LV02-11, LV05A-09, LV10-11).
- NO H. No Sifra row and no Leviticus teacher row moves a rule of ours; every transfer in the batch has its teacher on the row.
The census after B5: labeled 2,838 of 2,838, DEBT 0 — Genesis 1,663, Exodus 545, the law-era manifests 117, Leviticus 513; THE
GATE PASSED plain AND `--strict`, 0 lines. The verifier loop over all 166 modified manifests (every manifest now carries labels):
0 FAILED, 1,272 verified and 619 uncheckable — unchanged since before any label — and 947 no-check, the growth of 466 from B4's
481 exactly the rows of the 46 manifests newly in the loop (all Leviticus, none with a check block), the four tallies summing to
2,838; the LR1 gate 0.

### O11 CLOSED (2026-09-09)
THE WHOLE RECORD BY CODE over 2,838 claims: ink 1,142, plain 910, E7 308, E10 67, E30 57, I2 43, M-09 33, E2 31, E29 24, M-11 22,
M-23 19, E27 17, I3 17, E1 15, M-22 14, E26 12, M-03 12, M-05 10, M-12 10, E28 9, I1 8, E5 6, M-16 6, E32 4, I13 4, I6 4, I8 4,
M-10 4, M-08 3, M-20 3, M-24 3, E15 2, I11 2, I12 2, M-07 2, M-13 2, E12 1, I4 1, M-01 1, M-04 1, M-06 1, M-15 1, M-18 1 — and H 0:
the record holds no untaught transfer among the frozen claims; the nine hypotheses of ours live in the runners' cells, where the
link review flagged them. What the whole says: two-fifths of the claims read their own verse's ink; a third are the teacher's
plain reading of the wording as the rule; the concordance pair is the largest single inference form because the Kitzur carries it
on nearly every row; the thirteen and thirty-two together label 611 rows and the catalogued moves 191. The gate stays in force on
every seat from LR1 on (the ceilings file); `--strict` is the standing form. The five decisions files and the verifier prints are
scratchpad records of this session (o11_b1..b5_decisions.py, o11_b1..b5_verify.txt); the manifests are the record.
