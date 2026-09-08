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

## O4 — THE EDGE FILING (2026-09-07; the open-items campaign's fourth sitting; the plan: the state doc's compaction point #90)

The debt this file named at LR3 ("THE UNFILED LIVE EDGES") paid: every live import edge the dependency gate sees
carries its own entry with THE TWO QUESTIONS answered, and the gate refuses a live edge without one from this sitting
on. Declared BEFORE the code; every teacher resolved on the local shelf by script (scratchpad o4_cite.py) before a link
was written; the call sites read at the CELL that consumes the fetched value (scratchpad o4_cells.py), never at the
import line.

### The measure, by script (scratchpad o4_census.py, before a line was filed)

Live import edges the gate sees: 129; beyond the token census: 66 — 34 with their own entry (the erection's 6 and the
incense-shekel runner's 12 among them, W6's filing), 13 filed ONLY THE OTHER WAY (a REVERSE entry on the callee's side:
pre_sinai's nine, family's two, minchah's one, offerings' one), 19 with no entry either way. Unfiled: 32, by runner as
COMPILE_DEBT's line says (pre_sinai 15, family 6, holiness 3, metzora 2, sanctions 2, clocks 1, minchah 1, offerings 1,
yoma 1). THE SEQUENCE RUNNER: 33 import lines, 32 REGISTRATION TUPLES over 32 modules — the guardians runner is imported
bare (its daemon is the library's world_engine.law_guardians; the import registers nothing and its alias is never used),
and the gate's own rule reads an unused import as no call. So the plan's "33 as none" is 32 as none, the correction
written beside the plan. The gate saw NONE of the 32 as live: its import scan reads `alias.name(` forms only, and the
sequential run fetches its daemons by `getattr(sys.modules[m], n)` over the string tuples of DAEMON_ORDER — a form the
file could not carry and the code did: the file understated the code by thirty-two edges the gate could not see.

### The rule (rule 9 of the dependency gate; the yaml header; THE_STEPS Step 5 (1))

1. EVERY LIVE IMPORT EDGE HAS ITS OWN ENTRY. An edge the token census never required is still the code's, and the file
   may not understate the code: a live edge (r → h) with no entry (r → h) FAILS the gate, whatever the census says. A
   REVERSE entry on the callee's side (h → r) files the callee's required edge, not the caller's live call — the caller
   files its own.
2. THE REGISTRATION FORM IS A CALL. A module imported and then named as a string in a `('cold_run_x', 'fn')` tuple —
   the sequential run's DAEMON_ORDER, fetched through sys.modules — is a live edge, read by the gate beside the
   `alias.name(` form. A bare import whose module is never used stays what it was: not an edge.
3. `none` IS LICENSED IN ONE MORE PLACE. Beside FALSE (a homograph has no link), a CALL from a runner whose declared span
   is EMPTY — the sequential run registers daemons and compiles no verse, so no ink of its own names an institution and
   no rule crosses. A CALL from a runner WITH a span still refuses `none` (the LR1 probe keeps firing).
4. The `--emit` stubs cover the unfiled live edges too; the "live edges beyond the token census" line now reports them
   all on file or fails naming each.

### The classifications (32 entries; each `why` in dependency_dispositions.yaml carries the reading in full)

| edge | link | the teacher (verified by script) | what crosses |
|---|---|---|---|
| pre_sinai → calendar | reference | — (Exod 23:12's seventh day is Gen 2:2-3's: שביעי "seventh", the rest verb) | verdict |
| pre_sinai → clocks | reference | — (Lev 12:3's "on the EIGHTH day... circumcised" restates Gen 17:12) | count |
| pre_sinai → decalogue | reference | — (Exod 20:11 quotes Gen 2:2-3) | verdict |
| pre_sinai → erection | transfer | Keritot 9a:4 — "as your fathers entered the covenant only by circumcision, immersion and the sprinkling of blood" | procedure |
| pre_sinai → holiness | transfer (+ a reference beside) | Sanhedrin 56b:7 — "of every tree of the garden — and not robbery" (the theft law read out of Gen 2:16); Lev 19:3's "My SABBATHS" a reference | verdict |
| pre_sinai → holiness_b | transfer (+ a reference beside) | Shabbat 108a:7-10 — "his foreskin" (Gen 17:14) with "its foreskin" (Lev 19:23): the rite's site; Lev 19:30's "My SABBATHS" a reference | verdict |
| pre_sinai → incense_shekel | reference | — (Exod 31:17 the THIRD seat of the creation-rest clause; the tokens counted at both) | verdict |
| pre_sinai → mishpatim | transfer | Sanhedrin 59a:11-13 — the repetition rule (Gen 9:6's bloodshed at Exod 21:12) | count |
| pre_sinai → offerings | transfer | Sanhedrin 59a:11-13 — the repetition rule (Gen 9:4's blood ban at Lev 3:17) | verdict |
| pre_sinai → ordinances | transfer (+ a reference beside) | Sanhedrin 56b:5 (the courts from "and He commanded"), 56b:4-8 (the seven read out of Gen 2:16); 56a:14 ("any man" includes the nations); 58a:8 ("one flesh" excludes the beast); the firstling's eighth beside Gen 17:12's a reference | verdict |
| pre_sinai → pesach | reference | — (Exod 12:44's מקנת כסף "bought with money" is Gen 17:12-13's own phrase; the rite named) | verdict |
| pre_sinai → priesthood | transfer (+ two references beside) | Mishnah Chullin 5:5; Chullin 83a:15-16 — ben Zoma's "one day" (Gen 1:5, Lev 22:28); the eighth day and Lev 24:8's Sabbath references | verdict |
| pre_sinai → tochacha | reference | — (Lev 26:42 "I will REMEMBER My covenant" = Gen 9:15 token for token) | verdict |
| pre_sinai → tzav | transfer | Sifra Tzav Section 10 1 — "the children of Israel are warned about the fat and the nations are not" (the refuted a-fortiori from the limb); Sanhedrin 59a:11-13 for the blood ban's karet | verdict |
| pre_sinai → yoma | reference | — (Lev 16:31 "a SABBATH of solemn rest") | verdict |
| family → clocks | transfer | Niddah 28a:9 — Rav Huna: "a fetus that put out its hand and withdrew it — its mother is impure as one who gave birth, as it is said (Gen 38:28): he PUT OUT A HAND" | count |
| family → guardians | transfer | Shevuot 38b:20 — Rav Yehuda citing Rav: the court oath is "the oath stated in the Torah — I will make you swear by the LORD, the God of heaven" (Gen 24:3) | verdict |
| family → holiness | HYPOTHESIS | none — Gen 49:2 "listen to ISRAEL YOUR FATHER" read under the parents' honor on the word "father" alone; Bereshit Rabbah 98:3 reads the clause three other ways (the God of Israel; God as the father who creates worlds; the Shema's origin) | verdict |
| family → holiness_b | HYPOTHESIS | none — 48:2's sitting up and 48:12's bow read under Lev 19:32's rising and honor by topic; Midrash Tanchuma Vayechi 6 5 reads 48:2 the OTHER way ("although he is my son, he is a king, and I will accord him honor") | verdict |
| family → mishpatim | HYPOTHESIS | none — the marriage formula's closing token לאשה "as a wife" across Exod 22:15, Gen 24:67, 38:14 (the mirror of the REVERSE entry; the cell already H since LR3) | count |
| family → mishpatim_2 | transfer | Ketubot 10a:4 — the mohar of the virgins (the mirror of the REVERSE entry) | value |
| holiness → tzav | reference | — (Lev 19:5-8 names the peace offering's window, leftover and pigul in Lev 7:16-18's words: והנותר "the leftover", פגול "pigul", ביום השלישי "on the third day") | window |
| holiness → vayikra5 | reference | — (Lev 19:11-12's warnings in Lev 5:21-24's own verbs: כחש "deny", שקר "lie", נשבע "swear") | verdict |
| holiness → yovel | transfer | Mishnah Bava Metzia 5:11 — the interest lender transgresses Lev 25's two, Exod 22's two, AND "before the blind you shall not put a stumbling block" (Lev 19:14) | verdict |
| metzora → tzav | reference | — (Lev 14:12-14 names the guilt offering; its law Lev 7:1-7; the pointer 14:13 already CALL) | verdict |
| metzora → vayikra5 | reference | — (Lev 14:21-22 "if he is poor and his hand does not reach... two turtledoves... the one a sin offering and the one a burnt offering" — Lev 5:7's scale in its own nouns) | verdict |
| clocks → vayikra5 | reference | — (Lev 12:8's bird pair in Lev 5:7's four nouns; the order from 5:8's "first") | verdict |
| minchah → vayikra5 | reference | — (Lev 5:11-13's sinner's MEAL OFFERING in Lev 2:1's nouns, the oil and frankincense reversed) | verdict |
| offerings → pesach | transfer | Mishnah Zevachim 1:1 — "except the paschal and the sin offering"; Zevachim 7b:10-11 — the paschal from Deut 16:1 | verdict |
| sanctions → chatat | transfer | Mishnah Keritot 1:2 — "for their willful act karet, for their unwitting act a sin offering, for their unknown act a suspended guilt offering"; Horayot 8a:8 | verdict |
| sanctions → shemini | reference | — (Lev 20:25 "SEPARATE between the pure beast and the impure" = Lev 11:47's closing clause) | verdict |
| yoma → moadim | reference | — (Lev 16:29-31 = Lev 23:27-32 word for word: the affliction, the Sabbath of rest, the karet) | verdict |

And the sequential run's 32: `{from: sequence, to: <runner>, disposition: CALL, link: none, carries: procedure}` — the
registration edge: the runner imported, its daemon fetched and registered on the one world; no verse compiled here, no
rule crossing.

THE TWO HYPOTHESES ARE NEW: the family runner's cells 909 (the aged father honored by call) and 995 (the parents' order by
call) are TAGGED H by the LR3 marker's own method (scratchpad o4_mark.py), their values unchanged; the family runner's
FRACTIONS line moves from "hypotheses 6/228" to 8/228 — printed by the run, read, then recorded. The third hypothesis edge
(family → mishpatim) mirrors an entry on file; its cell (648) has carried H since LR3.

### The predictions (written before the run)

The probes (scratchpad o4_gate_fires.py, EIGHT — written first): against the unchanged gate 2 of 8 fire (the two
regression guards: `none` on a spanned runner's CALL; a bare import dispositioned CALL); after the edit, before the filing,
the gate on the standing file FAILS naming every unfiled live edge — 32 standing + 32 registration = 64 failures, each
read; after the filing 8 of 8 fire and the gate is satisfied. The counts after: live import edges 129 → 161; beyond the
token census 66 → 98, all on file; dispositions 167 → 231 edges + 72 pointers; LINK CENSUS reference 162 → 177, transfer
31 → 45, hypothesis 6 → 9, none 40 → 72. The standing probes unchanged (o3 11/11, d9ii 5/5, lr1 12/12, clock 12/12,
sequence 4/4). The sweep 34/34 at 3,633 — no graded value moves (a filing changes provenance, never a verdict); the
family runner 228/228 with hypotheses 8/228; the daemon gate 244 / 0 / 0; hash 8b8fff1fa28953af unmoved.

### As run (O4's close)

THE PROBES FIRST, and their first flags read before believed: against the unchanged gate 3 of 8 fired, not the predicted 2 —
probe 2 ("the registration tuple read as live") fired for the WRONG reason (its check looked for a message the old gate could
never print, because the CALL-without-live-edge check had only ever run on census-REQUIRED entries; an unrequired CALL entry
with no live edge passed in silence — which is why probe 7, predicted a regression guard, was SILENT: a target, not a guard),
and the control (6) fired because the unfiled file passed the old gate. Probe 2 rewritten to remove the sequence's own entry
and expect the gate to name it; the CALL-must-be-live check extended to every entry on file.

THE GATE RUN TO FAIL on the standing file after the edit: 65 failures — the 64 declared (32 standing + 32 registration) AND
ONE MORE, honest: the clock sitting's yovel → tochacha, dispositioned CALL, registers the exile daemon BY ATTRIBUTE
(`T.law_tochacha` placed in the fork world's laws list) — a third live form neither `alias.name(` nor the registration tuple
reads, so the file had been RIGHT and the gate blind since the clock sitting; the daemon-reference form `alias.law_x` added
(daemons alone are named law_*, the standing rule; a constant read alone stays no call form), the docstring and the yaml
header amended, a probe-8 case added. The second run: 64 failures exactly, every one read; live import edges 162 (the
prediction said 161 — the jubilee-exile edge is the one), beyond the token census 99 (predicted 98, the same edge).

THE FILING (scratchpad o4_file.py; its first run refused itself on a tripwire that matched the new yaml HEADER, not a prior
filing — sharpened to the block's own header line): 32 standing + 32 registration entries before `pointers:`. The gate
satisfied on the first run after: dispositions 231 edges + 72 pointers; LINK CENSUS reference 177 / transfer 45 / hypothesis 9
/ none 72 — EXACTLY the declared counts; the listing "99 — ALL ON FILE (rule 9)". Probes 8/8 (o4), 12/12 (lr1 — its
control had failed on the unfiled file, as it should), 5/5 (d9ii), 11/11 (o3), 12/12 (clock), 4/4 (sequence). The `--links`
worklist: UNCLASSIFIED 0, hypothesis 9 (the six standing + the three filed here).

THE TWO CELLS MARKED H (scratchpad o4_mark.py — LR3's own patch; fix_percent lifted 0): family 995 and 909; the family runner
228/228 on its first run after, FRACTIONS "hypotheses 8/228" printed as declared, no graded value moved. The LR3 cell census
rerun: import cells calling a runner with NO EDGE on file 0 (was 30), cells inheriting a hypothesis edge 0 (the two carry their
own H), H cells 9 (was 7), import cells by their edge's link reference 204 / transfer 94 / hypothesis 1.

### Findings

1. **THE GATE'S LISTING WAS A DEBT WITH A NAME.** For nine sittings the gate printed the live edges beyond the census and
   demanded nothing of them; sixty-four calls stood live in the code and silent in the file, thirty-two of them invisible
   to the gate's own scan. A listing that does not gate is a worklist nobody owns — rule 9 makes it the gate's.
2. **THREE WAYS TO DEPEND, ONE OF THEM FOUND BY THE GATE'S FIRST HONEST FIRE.** A call, a daemon registered by name from a
   table, a daemon placed in a laws list by attribute — the third had been on file as CALL since the clock sitting and
   never once verified. The file was right; the instrument was blind; the fix is in the instrument.
3. **THE ACT OF FILING FOUND TWO HYPOTHESES THE CELLS HAD CARRIED AS IMPORTS.** The family runner read Jacob's summons
   ("listen to Israel your father") under the honor of parents and his sitting up under the honor of the aged; the shelf
   reads the first verse three other ways and the second the OTHER way round (the father honoring the son's kingship,
   Tanchuma Vayechi 6 5). No teacher — so H, by the review's own rule, values unchanged.
4. **A PROBE CAN FIRE FOR THE WRONG REASON.** Probe 2's first form matched a message the old gate could not print, and the
   "fire" was the absence of a check; read before believed, it exposed that the CALL-must-be-live rule had never run on an
   unrequired entry.
5. **THE PLAN'S COUNT WAS THE IMPORT COUNT.** "The sequence runner's 33" — thirty-two are registration edges; the guardians
   import is bare (its daemon is the library's) and, by the gate's own rule, no edge. The script's number is the one
   filed, the plan's corrected beside it.

### The scoreboard after O4

Edges 231: reference 177 / transfer 45 / hypothesis 9 / none 72. Pointers 72: reference 62 / none 10. Live import edges 162,
of which 99 beyond the token census — ALL ON FILE. Cells 3,024 sites: hypothesis 9 (family 8/228, chatat 1/195). Citations
for the fourteen new transfers resolved by script (scratchpad o4_cite.py) before any link was written. Probes 8/8 + 12/12 +
5/5 + 11/11 + 12/12 + 4/4.
THE SWEEP at O4's close: 34 of 34 runners green, 3,633 graded cells, both gates satisfied first (scratchpad sweep_o4.txt,
SWEEP-EXIT 0): DEPENDENCY GATE 162 live edges, 231 + 72 on file; DAEMON GATE 38 daemons / 267 kinds / 776 submit records,
244 WRAPPED / 0 OWED / 0 NONE, unfired 0, unconsumed 0, open aliases 0. No frozen unit touched; the corpus regression
green, hash 8b8fff1fa28953af unmoved. Not one graded value moved: a filing changes provenance, never a verdict.
