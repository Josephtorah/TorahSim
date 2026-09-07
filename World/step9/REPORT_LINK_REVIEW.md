# REPORT — THE LINK REVIEW (LR1, LR2, LR3 — 2026-09-07)

The owner, after W5's commit: "The teacher say not to create a link of our own unless it came
from a teacher. Yet I think we've done just that." The review that followed ran in three
sittings on one day: the law and the gates (LR1), the audit and the backfill (LR2), the cells
(LR3). This report is the three sittings' record; the state doc carries each sitting's entry.

## The rule, read from the shelf (not from memory)

A person does not derive a verbal analogy (gezerah shavah, the second of the thirteen
middot) on his own; a person may derive an a-fortiori (qal wa-chomer, the light-and-heavy inference) on his own. Both halves
stand in the Babylonian Talmud at Pesachim 66a:12 (the gemara on Hillel's Passover analogy:
"granted the analogy you had not received... but the a-fortiori, which a person derives on his
own, you should have derived yourselves") and Niddah 19b:12. The Jerusalem Talmud, Pesachim
6:1, has the elders of Beteira refuse Hillel's analogy by this very rule, accept him only on
"thus I heard from Shemaiah and Avtalyon," and state the reason by name — R. Abba bar Mamal:
deriving on one's own from "garment of skin"/"garment of skin" would make a creeping thing
defile in a tent; the shared word is an unbounded generator. Rashi's reason on both Bavli seats
is narrower: "perhaps the verse came for another matter." Tosefta Pesachim 4:11 has Hillel's
"and further, I have received from my teachers" as a fourth argument beside the three
inferences. Two riders from the Jerusalem passage: an analogy may uphold a received learning,
never overturn it; one refutes an a-fortiori, never a received analogy. Two nuances carried:
freeness of the word (mufneh) is a rival licensing regime, and Haggahot Ya'avetz on Niddah 22b
reads the Tannaim as divided on whether reception is required at all — this project gates on
reception, recorded as a choice; and the a-fortiori permission never installs a warning or a
penalty ("one does not warn from an inference," Rashi Pesachim 24a, Makkot 5b). The Bavli
files on the shelf are vocalized: strip the vowel points before a substring search, or the
rule's own line is missed — it was, on the first read.

## The distinction that saves most of the machine

A REFERENCE: the ink names an institution and the edge calls its definition ("the sin
offering" at Lev 5 calls Lev 4's engine; a law written twice; a run citing its spec). Licensed
by ink alone. A TRANSFER: a rule moves between contexts on a shared word or a topic — the
middah itself; it needs a teacher (a sugya, a Sifra passage, a catalogued move with its
exemplar named). An untaught transfer is a HYPOTHESIS (class H): the value kept, the flag
changed, never counted as compiled. THE TWO QUESTIONS — reference or transfer? if transfer,
taught by whom? — are asked before any seat, edge, unification, or type grouping is written,
and the answer is written beside it.

## LR1 — the law and the gates

- logic/MIDDOT.md under I2 carries the rule whole, with the counterpart, the two questions, and
  the choice; a case-law entry (the reception rule at Hillel's own analogy) beside the
  widow-widow refusal; line 110's order corrected — the lemma scan ENUMERATES, reception
  LICENSES; reception first, token pair second.
- THE_STEPS Step 5 (1): THE LINK REVIEW LAW paragraph.
- dependency_dispositions.yaml: every one of the 226 entries carries `link:` (reference /
  transfer / hypothesis / none / UNCLASSIFIED) and a transfer carries `taught_by:`;
  dependency_census.py rule 8 refuses a transfer without a teacher, an entry without the
  field, and `none` off a homograph; the LINK CENSUS line prints every run; `--links` prints
  the worklist.
- event_vocabulary.yaml: every type seated in more than one chapter carries `link:`;
  events_layer.py rule 7 verifies a reference by a shared CONTENT lemma (noun / verb /
  adjective, from the Tanakh DB's lemma and morph columns, the divine name excluded), refuses
  a transfer without `taught_by:`, and accepts a declared ground (`reference_by:`) counted
  apart.
- verify_claims.py: a claim beyond logic/oral_audit/claim_ceilings_LR1_2026-09-07.json (166
  manifests, 2,838 ids) without a middah label FAILS.
- Twelve fire-probes (three of them controls that pass): 12/12; the daemon gate's five 5/5
  after one stale probe was rewritten (the unfired list has been empty since W5).

## LR2 — the audit and the backfill

The 186 unclassified links read one by one against the two questions, and the 43 two-seat
types:

| population | reference | transfer (taught) | hypothesis | none |
|---|---|---|---|---|
| edges (154) | 91 | 27 (26 at LR2, one more at LR3) | 6 (7 at LR2, one reclassified at LR3) | 30 |
| pointers (72) | 62 | 0 | 0 | 10 |
| two-seat types (42 after the split) | 38 verified by lemma + 1 declared | 3 | 0 | — |

Every teacher was searched on the local shelf and its segment read before its address was
typed. Among them: the Mekhilta on Exod 20:23 [20:26] — R. Yishmael: "has it not already been
said, make them linen breeches?" (the vestments-ordinances edge); Midrash Tanchuma Terumah 11
— Moses' objection, a wooden altar under a perpetual fire; Zevachim 53a:9 — the red line from
"the net to the half of the altar"; Tanchuma Ki Tisa 11 3 — "from the goring ox it was
learned, thirty shekels"; Shabbat 87b:6 — the ten crowns; Mishnah Bikkurim 1:3 — no first
fruits before Atzeret, read on Exod 23:16's own clause; Sifra Emor Chapter 18 7 — R. Shimon's
azkarah-azkarah between Lev 24:7 and 5:12 (a link suspected ours, found taught); Mishnah
Chullin 5:5 and Chullin 83a — ben Zoma's "one day" at the creation and at "it and its young"
(the day boundary taught); Bereshit Rabbah 6:1 — "and for seasons: the three pilgrim
festivals"; Yevamot 59a:8 — widow-widow from Tamar CONSIDERED AND REFUSED, the edge carrying
the refusal; Bereshit Rabbah 85:5 — "Judah began the levirate commandment first"; Ketubot
10a:4 (found at LR3) — "money he shall weigh as the mohar of the virgins," the mohar and the
ketubah joined by the sages.

The hypotheses (class H, kept, the why carrying the H note): a bought field's tenure at
Machpelah and Gen 17:8's "everlasting holding" read under Lev 25 on the noun achuzah; Tamar's
pledge (eravon) as Exod 22:25's chavol and her widowhood under 22:21; the marriage formula's
closing token across Exod 22:15 / Gen 24:67 / 38:14; Lev 25:46's bequeathing verb with Gen
48:6's noun; the census-homed "widow" between Exod 22:21 and Lev 21:14. Searched; none found.

THE LEVIRATE SPLIT: Lev 18:18 is its own case type, rival_wife_taken, under the sanctions
daemon; levirate_commanded is restored verbatim to Gen 38:8 and the family runner; Tamar's
row went back with it (the sanctions scene literal 86 → 85 by print-then-type — the predicted
values matched, the slot index was off by one). D6's four unifications: the seventh year and
the fast are references, the omer a taught transfer, the first fruits a taught TIME GATE and
not one institution — the wording corrected. Every citation in the review resolved against
the shelf by script: 218 of 218, after "Mishnah Arakhin 9:?" (typed at W5) was replaced by the
Sifra's kin-ladder passage (Behar Chapter 8 2) and "Toharot" by the shelf's "Tahorot." The
duplicate pointer key (Exod 21:22 in two runners) is fixed and now fails the gate. One catch
on the record: the new lint's first live run flagged five references, and four were its own
parser dropping suffixed words (the pronominal suffix is the last morph segment) — read before
believed, fixed; the fifth was real and became the declared-ground case.

## LR3 — the cells

The census (scratchpad lr3_census.py), static over the 33 runners in their own shapes (the
standard `cell(v, TAG, why, fx)`; the list shape's `ink()/move()/data()` helpers; the tuple
rows ending in a tag; the eighth-day and Day runners' own forms): 3,016 cell call sites —
ink 1,481, move 755, answer-sheet 373, data 80, import 314, HYPOTHESIS 7, routed 6.

- The import cells INHERIT THEIR EDGE'S LINK: by their callee's edge, reference 194, transfer
  69, hypothesis 7 → the seven marked H (six in the family runner: the Machpelah tenure three
  ways, the widow's two seats, Tamar's pledge, the marriage formula's token; one in the
  sin-offering runner: Exod 21:28's eating clause read as an eating-only ban where Pesachim
  22b:6-7 and Bava Kamma 41a:20-23 read a benefit ban); the family runner's mohar cell,
  first counted a hypothesis, is TAUGHT (Ketubot 10a:4) — the edge mishpatim_2 → family
  reclassified with it; one cell under a hypothesis edge is a declared reference (the land's
  rest named a sabbath by the ink itself).
- The verse imports (a cell reading ink from outside its span with no live call): 56 carry a
  teacher in the why; 22 read as references (the institution's own other seat — the guilt
  offering's "most holy," the blemished beast's redemption, the wage law's second seat); 36
  call a runner with NO EDGE ON FILE (the live calls beyond the token census) — read, all
  references or taught; their EDGES remain unfiled (see the debt below).
- The move cells naming a cross-span verse: 120 taught, 0 untaught after nine whys gained
  the teacher they lacked (Horayot 8a:14 and Keritot 3a:20 for "one law for the unwitting";
  Keritot 22b for commandments-commandments; Sifra Emor 1 and Makkot 20a for baldness-
  baldness; Sanhedrin 74a:13 for "live by them"; Sifra Nedavah 13 4 and Menachot 84a:10 for
  the omer; Sanhedrin 56a:14 for "any man"; Zevachim 118b:13-15 for the seven and seven;
  Zevachim 44a:8 for profanation-profanation; the Sifra Shemini citation made visible).
- The 22 cells naming an analogy or adjacency outright: every one cites its teacher (Keritot
  25b:4, Makkot 23a:4, Yoma 86a:5, Yevamot 59a:8, Onkelos 31:13 with Mishnah Menachot 11:3,
  Shabbat 49b, Sifra Nedavah Section 8 7, Sanhedrin 39a:7 with Niddah 22b, Yevamot 63b:16-17,
  Shabbat 96b:2, Zevachim 59b:4-8, Arakhin 13a:8, Megillah 12a:7, Yoma 71b) or is an ink
  census of adjacency (the Name doubled at 34:6; the spec verses finding their run by a shared
  token; the work-list's juxtaposition).
- THE H CLASS installed: the sixth provenance tag `H = 'HYPOTHESIS'` in the 21 runners that
  carry the tag line (17 by script, four by hand — the appointed times, the offerings with its
  FENCE tag, the covenant cascade and the jubilee with no import tag), the frac dict and the
  FRACTIONS line extended: "hypotheses N/n" — the chip. The family runner now reads
  "hypotheses 6/228," the sin-offering runner "1/195," every other runner "0/n." The twelve
  runners of the older shapes carry no H cell and were not restyled.
- MOVE_CATALOG M-22, M-23, M-24 marked as GENERALIZATIONS: a teacher for a new verse pair only
  with a recorded exemplar named beside the application; M-24's "the machine's form is the
  dependency gate itself" glossed as an enumeration, not a license.
- The moadim first-fruits cell's "one institution at two seats" corrected to the time gate.

## The debt named, not paid

- THE UNFILED LIVE EDGES: 66 call pairs beyond the token census (the dependency gate's
  "live edges beyond the token census" list) carry no entry in dependency_dispositions.yaml
  and therefore no `link:`; their cells were read at LR3 (references or taught), the edges
  are to be filed as CALL entries with their link at the next sitting that touches each
  runner (W6, W7) or at one filing sitting.
- THE CLAIMS LABEL DEBT: 2,838 frozen claims, 36 with a middah label — gated forward by the
  ceilings file; the backfill unbounded, named.
- The seven hypotheses stand until a teacher is found; a later shelf read may retire any of
  them (LR3 retired one — the mohar).

## Lessons banked

- A gate's first honest failures are its own test: read every first flag before believing it
  (the suffix bug, the concatenated-why bug in the census, the reverse-edge lookup).
- Count by script, never by eye (the tuple slot; the census's implicit string concatenation).
- A citation typed with a question mark lasts until a resolver reads it — resolve at the seat.
- The lemma-overlap test is a NECESSARY condition (the levirate's seats share "woman"); the
  classification is read, the lint only refuses what cannot be a reference.
- A move catalogued from exemplars is a teacher only where a teacher used it.

## The scoreboard (the review's own numbers; the sweep's closing line below)

Edges 154: reference 91 / transfer 27 / hypothesis 6 / none 30. Pointers 72: reference 62 /
none 10. Two-seat types 42: reference 38 + 1 declared / transfer 3. Cells 3,016 sites:
hypothesis 7. Citations resolved 218/218. Probes 12/12 and 5/5. Registry 240 types; daemons
38 watching 238 kinds; 234 wrapped / 14 owed / 3 none; hash 8b8fff1fa28953af unmoved.
THE SWEEP at LR3's close: 33 of 33 runners green, 3,621 graded cells, both gates satisfied
(scratchpad sweep_lr3.txt, SWEEP-EXIT 0). Not one graded value moved in the three sittings —
the review changed provenance, whys, seats, and gates, never a verdict.
