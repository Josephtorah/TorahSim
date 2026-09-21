#!/usr/bin/env python3
# THE DEUTERONOMY WALK 10b — the docket's close (2026-09-21, D2b the third run): the map's "THE DOCKET D2b — AS RUN … AND THE DOCKET WHOLE" paragraph, the
# state doc's #201 addendum 3, the recovery page's section-2 lines, RESUME's head, MIDDOT's docket entry (every code checked in MIDDOT.md before it was
# typed — I1, I2, I3, I6, I12, E28, E29; the juxtapositions, the do-not-read readings, the transposition and the list read backward NAMED, no code),
# MISHNAH_TOPICS' row notes, the memory, the index, the commit message file (NEW — commit_msg_ch12b.txt, the headline written at RUN B). EVERY COUNT PARSED
# from the writer's print (ch12_docket_write.out) and the three runs' check prints, never typed; every text built whole before its file is opened; the
# size caps asserted. 9b's form (write_ch11_docket_records.py). Run from the repo root; --check runs the anchors and the caps only.
import os, re, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
P = R(f'{SCR}/ch12_docket_write.out')
m = re.search(r'WROTE (\S+) (\d+) bytes', P); OUTP, NB = m.group(1), int(m.group(2))
m = re.search(r'rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \) carried (\d+) unresolved_read_here (\d+) read_here (\d+) dup_dropped (\d+)', P)
NR, NL, NT, NC, NCL, NCT, NCAR, NUNR, NRH, NDUP = map(int, m.groups())
m = re.search(r"verdicts (\{.*?\}) link (\{.*?\}) topic (\{.*?\})", P); VD, VL, VT = (eval(x) for x in m.groups())
LAWC = eval(re.search(r'LAW by cell (\{.*?\})', P).group(1)); NOUT = eval(re.search(r'OUTSIDE by work (\{.*?\})', P).group(1))
UNC = eval(re.search(r'UNCITED (\[.*?\])', P).group(1)); RANGES = eval(re.search(r'ranges (\[.*\])', P).group(1)); NMISH = int(re.search(r'mishnah\+midrash rows (\d+)', P).group(1))
NWORKS = len(set(re.findall(r'^- (.+?) \d+[ab]?:\d+ \[LINK', R(OUTP), re.M)))
assert NRH == NR - NCAR and NUNR + NCAR == NC and len(RANGES) == 25, (NRH, NR, NCAR, NUNR, NC, len(RANGES))
def run(out, tag):
    mm = re.search(tag + r" TOTAL (\d+) (\{.*?\}) carried (\d+) unresolved read here (\d+) read here (\d+)", R(f'{SCR}/{out}')); return int(mm.group(1)), eval(mm.group(2)), int(mm.group(3)), int(mm.group(4)), int(mm.group(5))
NR1, VD1, NCAR1, NUNR1, NRH1 = run('ch12_d1_check.out', 'D1'); NR2, VD2, NCAR2, NUNR2, NRH2 = run('ch12_d2_check.out', 'D'); NR3, VD3, NCAR3, NUNR3x, NRH3 = run('ch12_d2b_check.out', 'EFG')
LAWC3 = eval(re.search(r'EFG TOTAL .*LAW by cell \(own notes\) (\{.*?\})', R(f'{SCR}/ch12_d2b_check.out')).group(1))
NUNR3 = sum(1 for l in R(f'{SCR}/ch12_uncred_unres_D2b.txt').split('\n') if l.strip()); NDOUBLE = NUNR3x - NUNR3   # the check's count over-counts carried rows whose ledger line was itself a read-whole note
assert NR1 + NR2 + NR3 == NR and NCAR1 + NCAR2 + NCAR3 == NCAR and NUNR1 + NUNR2 + NUNR3 == NUNR and NRH1 + NRH2 + NRH3 == NRH, (NR1, NR2, NR3, NR)
U = R(f'{SCR}/ch12_docket_uncred.out'); chunks = re.findall(r'(ch12_uncred_\d\d\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', U)
d2b = [c for c in chunks if int(c[1]) >= 933]; NUNCRED3 = sum(int(c[3]) for c in d2b); assert NUNCRED3 + NUNR3 == NRH3, (NUNCRED3, NUNR3, NRH3)
vd = lambda d: ', '.join(f'{k} {d.get(k, 0)}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'))
MAPP = f'''
THE DOCKET D2b — AS RUN (2026-09-21, on "Continue" after the compaction at #201 addendum 2 — THE THIRD OF THE DOCKET'S THREE RUNS) AND THE DOCKET WHOLE:
the dump's rows 933-1537 — Bekhorot 15a-16a and 33a-b, Temurah 3b-4a (carried) and 17b, Makkot 13a-b (carried), 17a-19b and 23b, Sotah 37b-38b,
Sanhedrin 20b and 74a-b, Kiddushin 36b-37a (carried), Rosh Hashanah 4a-6b, Yevamot 47b (carried), Keritot 20b-22a, Megillah 9b-10a, Pesachim 8b (carried)
— VERDICTED in three parts on disk (ch12_docket_E.py rows 933-1185, _F.py 1186-1396, _G.py 1397-1537; SPEC = CREDITED_SPEC + OWN, build() asserting each
slice matched — no unmatched address on the first check of all three): {NR3} rows — {vd(VD3)}; {NCAR3} CARRIED with their ledgers' own verdict lines and
{NUNR3} whose ledger's form carried no verdict READ WHOLE HERE (ch12_uncred_unres_D2b.txt); {NUNCRED3} uncredited rows READ WHOLE in {len(d2b)} chunk files
({", ".join(f"{c[0]} rows {c[1]}-{c[2]} ({c[3]} rows)" for c in d2b)} — the two 76k chunks in two Read pages each); {NRH3} ROWS READ WHOLE IN THIS RUN; LAW by cell, this docket's own
notes {LAWC3}; no cut, no overlay. THE WRITER derived from 9b's by asserted line substitutions (derive_ch12_docket_writer.py — the seven parts, the chapter's
verse regex and range, the header ch12_docket_hdr.py and the crowns ch12_docket_crowns.py spliced in, the twenty-five ranges ASSERTED against the scan's print)
and run once: logic/oral_triage/deu_12_reeh_exam_2026-09-20.md — {NR} rows (link {NL} in {NWORKS} works, topic {NT}: the {NMISH} Mishnah rows listed as topic rows;
{"; ".join(f"{n} {s}" for n, s, l in RANGES)}); the verdicts {vd(VD)} (the link rows {vd(VL)}; the topic rows {vd(VT)}); LAW by cell, this docket's own notes
{LAWC}; credited {NC} — {NCAR} CARRIED WITH THEIR LEDGERS' OWN VERDICT LINES and {NUNR} READ WHOLE HERE; {NRH} ROWS READ WHOLE IN THE THREE RUNS (D1 {NRH1} of {NR1}, D2a {NRH2}
of {NR2}, D2b {NRH3} of {NR3}); coverage computed (missing 0, extra 0; {NDUP} duplicate address); OUTSIDE by work {NOUT}; the verses no link row cites {UNC}; lint 0
after one gloss inserted at its source (part B) and in the file. THE CROWNS OF D2b (the file's finds section holds the three runs' together): THE BLEMISHED
CONSECRATED'S TABLE AT ITS FOLIO (Bekhorot 15b:9-12 — the blemish before the consecration "only the mitzva (commandment) of value", the consecration before the
blemish "ONLY THE PERMISSION OF CONSUMPTION": 12:15's release read on the redeemed animal; 15a:6-8 the firstborn and the gifts excluded by "as the gazelle and
the hart" with "however" bounding; 15a:13-17 the fat from "its blood" so its karet (excision) stands; 15b:1 "you may slaughter and eat" the permission from the
slaughter); THE EATERS (33a:4 R. Akiva — a gentile eats it, the comparison's third seat; 33a:8-11 Beit Shammai / Beit Hillel — 12:15's "the impure" UNQUALIFIED,
unlike Numbers 9:10); 12:26'S WORDS PARSED (Temurah 17b:15-17 — "only your holy things" the substitutes, "that you have" the offspring; 12:27 the rule of
their treatment; "only" R. Yishmael's exclusion / needless for R. Akiva); THE LADDER AT ITS BAVLI SEAT (Makkot 17a:12-17b:1 — R. Shimon's five rungs on
12:17's list; 17b:3-8 Rava's refutation of each; 17b:9 THE LIST READ BACKWARD; 17b:10 a mere prohibition from the inference); THE SECOND TITHE AND THE
TEMPLE (19a:3-5 — juxtaposed to the firstborn in 14:23; 19a:7 I3 refuted; 19a:10 the chain rule); THE IMPURE TITHE'S WARNING FROM THE CHAPTER'S OWN GATES
(19b:3-7 — 12:15's "the impure … within your gates" against 12:17's "you may not eat within your gates"); "TOO FAR" AS ANY INABILITY (19b:9-13 — "unable to
carry it" is eating; one stride outside the wall; "from you" from your fullness); THE LASHES AND KARET (23b:4-7) and the 613 (23b:18 — E29); THE NAME NOT
ELSEWHERE by R. Yoshiya's TRANSPOSITION of Exodus 20:20 (Sotah 38a:11) with Mishnah Sotah 7:6's tail (38a:1); THE THREE COMMANDMENTS OF THE ENTRY (Sanhedrin
20b:11-12) and DAVID'S REST BEFORE THE SEEKING OF THE SITE (20b:14 — 12:10-11's order in the run); THE PERSECUTION'S EDGES (74b:1, 74b:5-7; 74b:9 the limb
of a living animal among the seven — 12:23's limb); THE DELAY'S CLOCK (Rosh Hashanah 6b:3; 6b:10 Shavuot's date floating; 6b:13 the heir excluded) and THE
WOMAN'S REJOICING (6b:15-16 — her obligation, or her husband's to make her joyful: a two-arm parameter on 12:7, 12, 18's household); THE BLOOD'S CLASSES
(Mishnah Keritot 5:1 at 20b:7-8; 20b:9-21a:8 the species by Leviticus 7:26's general-particular-general, I6; 21b:6 THE WILD ANIMAL'S BLOOD UNDER THE BAN;
21b:11 the three classes; 22a:4 HUMAN BLOOD OUTSIDE 12:16'S "THE BLOOD"; 22a:10 the life-blood's boundary; 22a:17-19 THE EXUDATE'S KARET WITHOUT ATONEMENT);
SHILOH AND JERUSALEM AT THE SECOND ANSWER SHEET (Mishnah Megillah 1:10-11 at 9b:15-10a:1 — the inheritance forever) and THE SANCTITY AFTER THE TEMPLE
(10a:2-9 — R. Yitzchak's Onias ruling RETRACTED before Mishnah Zevachim 14:8; R. Eliezer / R. Yehoshua the arms). THE MIDDOT OF D2b (checked in MIDDOT.md
before typing): I1 at Bekhorot 33a:2-3, 33b:16, Temurah 17b:6-7, Makkot 17a:12-18, 17b:3-8 (the refutations), 17b:10 (the rider — no punishment from an
inference), Keritot 22a:2-3; I2 at Makkot 18b:14, Sotah 38a:4, 38a:6; I3 at Makkot 19a:7; I6 at Keritot 21a:5 and 21a:7's rider (R. Yishmael's school on
unlike generalizations); E29 at Makkot 23b:18; the juxtapositions named (Bekhorot 15a:12, 15a:15-17, 16a:14; Makkot 19a:5; 19a:10 the chain rule), the
transposition (Sotah 38a:11), the list read backward (Makkot 17b:9), the do-not-read reading (Sotah 38b:10) and the generalization-and-detail (Keritot
21a:4) named, no code. THE LESSONS OF D2b: three carried rows in part G (Pesachim 8b:6-8) carry a ledger line that was itself an earlier docket's read-whole
note — the check's "unresolved read here" over-counted them by {NDOUBLE}; the count taken from the carry's own split file; the ledger's count from the
carry's list; a gloss the part's lint passed and the ledger's lint caught — the word at a line's end, glossed at the source and in the file; the derive
ASSERTS the ranges' count against the design. COMPILE_DEBT's 10b box (k) is marked PAID with the box at RUN B. THE INSTRUMENTS (the scratchpad, copied by
copy_ch12_docket_forms.py): ch12_docket_E/F/G.py, ch12_d2_check.py EFG (ch12_d2b_check.out), ch12_docket_hdr.py, ch12_docket_crowns.py,
derive_ch12_docket_writer.py, write_ch12_docket.py, ch12_docket_write.out, write_ch12_docket_records.py. RUN B next on the owner's word, after a compaction:
the probes to FAIL (Q31-Q33, BEFORE the types; the high_places_banned ONE literals grepped and retyped from the print), the types with the docket's names and
values (the_rite_of_slaughter from Mishnah Chullin 2:1 — the gullet and the windpipe, the majority of one sign for a bird and of two for an animal;
the_wilderness_flesh's two arms with the exile's third state; the woman's rejoicing as a DATA row), the callees' facts, the runner cold_run_place_name.py
the 67th, the recorder with the cache off, the stitcher, the literals DD1-DD9, the tape, the chain LAUNCHED, the clean point; THE TAIL.
'''
STATE = f'''
#201 ADDENDUM 3 (2026-09-21, at the close of THE DOCKET D2b of THE DEUTERONOMY WALK sitting 10b — the third of the docket's three runs, on "Continue" after the compaction — A CLEAN COMPACTION POINT): THE STATE: THE DOCKET WRITTEN — logic/oral_triage/deu_12_reeh_exam_2026-09-20.md, {NR} rows (link {NL} in {NWORKS} works, topic {NT}; {vd(VD)}; LAW by cell, own notes {LAWC}; credited {NC}: {NCAR} CARRIED with their ledgers' own verdict lines by ch12_credit_carry.py, {NUNR} read whole here; {NRH} rows read whole in the three runs — D1 {NRH1}, D2a {NRH2}, D2b {NRH3}; the twenty-five ranges asserted; coverage computed, missing 0, extra 0; lint 0 after one gloss at its source), the writer derived from 9b's (derive_ch12_docket_writer.py → write_ch12_docket.py, the header and the crowns typed from the three runs' notes); D2b = rows 933-1537 in parts E-G ({NR3} rows — {vd(VD3)}; {NCAR3} carried, {NUNR3} unresolved read whole here, {NUNCRED3} uncredited read whole in three chunks; LAW by cell, own notes {LAWC3}); the map's "THE DOCKET D2b — AS RUN … AND THE DOCKET WHOLE" paragraph (the crowns, the middot, the lessons), MIDDOT's docket entry, MISHNAH_TOPICS' row notes, RESUME, the recovery page, the memory, the commit message file started (<scratch>/commit_msg_ch12b.txt — the headline at RUN B); the forms copied. NOT COMMITTED (since 4af2953): RUN A's records, the design, the docket's three runs. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (compact before RUN B). NEXT ON "Go": RUN B — patch_probes_ch12.py (Q31-Q33 to FAIL, BEFORE the types — 7b's lesson 2; the literals holding high_places_banned ONE grepped: three seats in cold_run_sequence.py, two in readback_probes.py predicted, the grep decides — retyped ONE → TWO from the print BEFORE the tape), add_types_ch12.py (event_vocabulary +5: demolition_restated, place_chosen_declared, profane_slaughter_permitted, nations_cut_off_warned — form statute, witnesses Deut 12:1, 12:5, 12:15, 12:29 — and place_name_case; effect_vocabulary +7: name_erasure_barred, holy_things_in_the_gates_barred, levite_forsaking_barred, foreign_rite_inquiry_barred (block), place_chosen_required, rejoicing_before_the_lord_commanded, profane_slaughter_permitted (status), high_places_banned's row amended with the chapter's seat; daemon_dispositions law_place_name given_at Deut 12:1 installed_by boot, the six cells WRAPPED; dependency_dispositions the span [[Deut, 12, 1, 31]] and the seventeen CALL edges predicted, the one AS_WHEN pointer at 12:20 — the census decides; installation_probes I5 71 → 72; calendar_parameters.yaml +2 — the_rite_of_slaughter (Mishnah Chullin 2:1's value: the gullet and the windpipe, the majority of one sign for a bird and of two for an animal — Chullin 28a:5) and the_wilderness_flesh (R. Yishmael's release at the entry / R. Akiva's rite required, the exile's third state — Chullin 16b:15-17a:4)), ch12_callees.py (every CALL's facts printed before any assert), the runner cold_run_place_name.py the 67th in parts with ch12_fastcheck.py and ch12_cases_gen.py (six cells F1-F6 and the_readback's thirty-one rows; the docket's crowns as exam rows), seq_record_ch12.py (INK_CACHE=0) and seq_stitch_ch12.py (no marker — the four lines on the counter's day (40, 11, 1)), patch_seq_literals_ch12.py (DD1-DD9; RUN = (1323, 96, 88, 0, 12, 1626, 43, 319, the four pairs, 127) predicted), the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, write_ch12b_records.py and copy_ch12b_forms.py WRITTEN, gates_chain.sh LAUNCHED in the background, the clean point → THE TAIL after the compaction (the summary read once, the demands filed, the records from the sheet in one call — the map's AS BUILT, COMPILE_DEBT's sitting-10 box PAID and the 10b box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6 row, RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory — the forms, the commit message, the 10b timing rows reported). POST-COMPACTION REREADS: the recovery page, the map's "Sitting 10b … THE DESIGN" (the newest section) with its three AS RUN paragraphs, MEMORY.md.
'''
RESUME = f'''# ⚠ THE DEUTERONOMY WALK sitting 10b — THE DOCKET DONE IN THREE RUNS (2026-09-20/21; logic/oral_triage/deu_12_reeh_exam_2026-09-20.md — {NR} rows, {NCAR} carried
# with their ledgers' verdicts, {NRH} read whole here; {vd(VD)}): the receipt without the Name's referent IS THE ORAL LAW (Chullin 28a:5 — the_rite_of_slaughter's
# value), the wilderness flesh's arms with the distance their ground and the exile a third state (Chullin 16b:15-17a:4), the stations and 12:9's two nouns four
# ways at their folio (Zevachim 112b-119b), the ladder at its Bavli seat and the impure tithe's warning from the chapter's own gates (Makkot 17a-19b), Rabbi's
# 12:25 defended by the context (Chullin 115b:2), the blood's classes (Keritot 20b-22a), Shiloh and Jerusalem at the second answer sheet (Megillah 9b-10a).
# NEXT: RUN B after a compaction (the probes to FAIL, the types, the runner cold_run_place_name.py, the tape, the chain launched, the records).
'''
MIDDOT = f'''
### THE DEUTERONOMY WALK 10b — THE DOCKET OF CHAPTER 12 (2026-09-20/21, three runs; logic/oral_triage/deu_12_reeh_exam_2026-09-20.md, {NR} rows — {NCAR} carried, {NRH} read whole here)
Every code checked in this file's tables before it was typed. I1 (qal wa-chomer, the a-fortiori): Bekhorot 33a:1-3 — the non-priest's eating from the impure
priest's (the refutation: the communal service; Beit Hillel: the inference is on the eating); 33b:16 — the cut to the detached (Leviticus 22:24); Temurah
17b:6-7 — the offspring from the substitute, REFUTED (substitution applies to every offering) so the verse is needed; Makkot 17a:12-18 — R. Shimon's five rungs
on 12:17's list (the wall from the second tithe, the sprinkling from the peace offering, the non-priest from the firstborn, the curtains from the sin offering),
17b:3-8 — Rava's refutation of each rung (the acute mourner, the coin, the hands and the waving, the womb, the atonement), 17b:10 — THE RIDER: a mere
prohibition, no lashes, from an inference; 18a:2 (carried) — Rava: the repetition designates, not the a-fortiori; 23b:2 (carried) — the blood's reward; Keritot
22a:2-3 — human milk from the non-kosher animal's, REFUSED by Leviticus 11:29; Bekhorot 33a:1, Zevachim 85a:5 and Chullin 84b:6, 102b:2, 114a:9, 114a:13,
114b:1, 115a:4, 115b:8 (the earlier runs). I2 (gezerah shavah, the verbal analogy): Makkot 18b:14 — "hand" (26:4) / "hand" (Leviticus 7:30): the first
fruits waved by the priest under the owner's hands; Sotah 38a:4 — "so you shall bless" (Numbers 6:23) / "stand … to bless" (27:12): standing; 38a:6 — the same
with Aaron's lifted hands (Leviticus 9:22); 38a:10 (carried) — "to put His name there" (12:5) / "put My name" (Numbers 6:27): the Name pronounced only in the
Temple; the earlier runs' seats (Bekhorot 15b:8, Keritot 3b:12, Makkot 16b:15, 19b:6, Menachot 77b:4, Sanhedrin 47b:18, Yevamot 73b:7, 86a:5, Zevachim 83a:3,
83a:5, 86a:7, 119a:6; Chullin 115b:4, 115b:7, 116a:7) with the riders at Zevachim 86a:8 (the freeness) and Chullin 115b:13 (not refuted by reasoning). I3
(binyan av, the common element): Makkot 19a:7 — the first fruits and the firstborn, REFUTED (both have an altar aspect) so the juxtaposition of 14:23 is needed;
Chullin 114a:15-17, 115b:16, 116a:1-2 (the earlier run — the refutation rule). I6 (kelal u-frat u-kelal, general-particular-general): Keritot 21a:5 — "no
manner of blood" / "of bird or of animal" / "any blood" (Leviticus 7:26-27): the like of the detail — a light and a severe impurity, forbidden-or-permitted, a
type of meat; 21a:7 — THE RIDER: R. Yishmael's school expounds even where the generalizations differ (lashes against karet (excision)). I12 (davar ha-lamed
me-inyano, the context): Chullin 115b:2 — Rabbi's 12:25 defended from the adjacent verses (the earlier run). E28 (from-the-preceding): Chullin 102a:11, 113a:19,
115b:5 (the earlier runs). E29 (gematria, letter-values): Makkot 23b:18 — "Torah" (33:4) six hundred and eleven, with the two heard from the Mouth the 613
(the row continues past the range). THE JUXTAPOSITIONS (the likening by adjacency) — no code, named: Bekhorot 15a:12 (the animals of 12:15's comparison),
15a:15-17 (the fat's karet by "its blood" against the juxtaposition), 16a:14 (the substitutes to the five sin offerings by "split hoof"), Makkot 19a:5 (the
second tithe to the firstborn in 14:23 — only with the Temple), 19a:10 (the chain rule — a matter derived by juxtaposition teaches by juxtaposition for the
non-sacred), and the earlier runs' (Bekhorot 14b:13, Chagigah 4b:2, Keritot 3b:13, Zevachim 107a:1, 60b:4, 62b:10, 84b:7, 115a:6, 116a:2, Pesachim 22a:8,
22b:3, 24a:12, Yevamot 73b:2, Chullin 28a:4, 84a:5, 84a:7, 115a:6). THE READINGS "DO NOT READ" (al tikrei) — no code, named: Sotah 38b:10 ("will be
blessed" / "will bless"); Zevachim 115b:12, 115b:15, 119b:8; Chullin 115a:5 (the earlier runs). THE TRANSPOSITION — no code, named: Sotah 38a:11 (R. Yoshiya's
Exodus 20:20 reordered — where I come and bless you, there My name). THE LIST READ FROM ITS END — no code, named: Makkot 17b:9 (R. Shimon on 12:17). THE
GENERALIZATION AND A DETAIL WITHOUT THE SECOND GENERALIZATION — no code, named: Keritot 21a:4 (refused: the verse generalizes again). THE DISPUTES AS
PARAMETERS (the machine's data channel): Chullin 16b:15-17a:4 (the wilderness flesh — released at the entry / the rite required; the exile the third state);
Chullin 28a:4-6 (the bird's slaughter by Torah law or the scribes; which sign); Zevachim 119a:9-13, 119b:1-5 (12:9's two nouns four ways); 117a:8-117b:1 (the
Gilgal row's five arms); Bekhorot 33a:8-11 (the impure eater of the blemished firstborn — from his own body or from outside); 33b:5-7 (the congested firstborn's
bloodletting — three arms); Temurah 17b:11-13 (the blemished peace offering's offspring — the altar / grazing); Makkot 23b:4-7 (the flogged exempt from karet
(excision) or not); Rosh Hashanah 6b:15-16 (the woman's rejoicing — hers or her husband's); Keritot 22a:10-13 (the life-blood's boundary — while it spurts /
from the last black drop); 21b:11-14 (the blood of creeping animals — lashes under which warning); Megillah 10a:2-9 (the first consecration for its time or
forever); Chullin 116a:12-14 (the wild animal and the bird in milk).
'''
MEMO = f'''
THE DOCKET DONE IN THREE RUNS (2026-09-21, D2b on "Continue" after the compaction at #201 add. 2): deu_12_reeh_exam_2026-09-20.md — {NR} rows ({vd(VD)}; credited
{NC}: {NCAR} carried with their ledgers' own verdict lines, {NUNR} read whole here; {NRH} rows read whole in the three runs — D1 {NRH1}, D2a {NRH2}, D2b {NRH3}); LAW by cell,
own notes {LAWC}; D2b's crowns: the blemished consecrated's table at its folio (Bekhorot 15b:9-12 — 12:15's release "only the permission of consumption"),
the ladder at its Bavli seat with the list read backward (Makkot 17a:12-17b:10), the impure tithe's warning from the chapter's own gates (19b:3-7), "too far"
as any inability (19b:9-13), the Name not elsewhere by transposition (Sotah 38a:11), David's rest before the seeking of the site (Sanhedrin 20b:14), the
woman's rejoicing a two-arm parameter (Rosh Hashanah 6b:15-16), the blood's classes with human blood outside the ban and the exudate's karet (excision)
without atonement (Keritot 20b-22a), Shiloh and Jerusalem at the second answer sheet and the Onias ruling retracted (Megillah 9b:15-10a:9). LESSON: a carried
ledger line can itself be an earlier docket's read-whole note — the unresolved count from the carry's file, never from the note text. NEXT: RUN B after a
compaction (the state doc's #201 addendum 3 the newest).
'''
MSG0 = f'''CHAPTER 12 COMPILED AND ON THE TAPE — (THE HEADLINE WRITTEN AT RUN B). THE DOCKET, THREE RUNS (2026-09-20/21, on the owner's "Reread then go" for D1, D1's window for D2a, "Continue" after the compaction for D2b): logic/oral_triage/deu_12_reeh_exam_2026-09-20.md — {NR} rows ({vd(VD)}; link {NL} in {NWORKS} works, topic {NT}: the twenty-five folio ranges whole, the thirty Mishnah rows; credited {NC} — {NCAR} CARRIED WITH THEIR LEDGERS' OWN VERDICT LINES (ch12_credit_carry.py, 9b's form), {NUNR} read whole here where the ledger's form carried no verdict; {NRH} rows read whole in the three runs; the chunker flushing at the runs' boundaries; the 76k chunks read in two pages), coverage computed, the twenty-five ranges asserted, lint 0; its crowns: THE RECEIPT WITHOUT THE NAME'S REFERENT IS THE ORAL LAW (Chullin 28a:5 — the gullet and the windpipe, the majority of one sign for a bird and of two for an animal; Mishnah Chullin 2:1 the_rite_of_slaughter's value), THE WILDERNESS FLESH'S ARMS NARRATED WITH THE DISTANCE THEIR GROUND AND THE EXILE A THIRD STATE (Chullin 16b:15-17a:4), THE STATIONS AT THEIR FOLIO with the karet (excision) matrix, the eleven differences, the eras' durations and 12:9'S TWO NOUNS FOUR WAYS (Zevachim 112b-119b), THE LADDER OF A FORTIORI AT ITS BAVLI SEAT with the list read backward and the bar's onset at the wall (Makkot 17a-19b), THE IMPURE TITHE'S WARNING FROM THE CHAPTER'S OWN GATES (Makkot 19b:7), THE BLEMISHED CONSECRATED'S TABLE — 12:15's release "only the permission of consumption" (Bekhorot 15b:9-12), 12:26's words parsed into the substitutes and the offspring (Temurah 17b:15-17), RABBI'S 12:25 DEFENDED BY THE CHAPTER'S OWN CONTEXT — I12 (Chullin 115b:2) with flesh in milk at its folio, the civility and the partitive "of" (Chullin 84a:18-21), THE BLOOD'S CLASSES with human blood outside the ban and the exudate's karet without atonement (Keritot 20b-22a), THE NAME PRONOUNCED ONLY THERE by analogy and by transposition (Sotah 38a:10-11), the three commandments of the entry and David's rest before the seeking of the site (Sanhedrin 20b:8-14), the woman's rejoicing a two-arm parameter (Rosh Hashanah 6b:15-16), SHILOH AND JERUSALEM AT THE SECOND ANSWER SHEET and the sanctity after the Temple with the Onias ruling retracted (Megillah 9b:15-10a:9); MIDDOT's docket entry (I1, I2, I3, I6, I12, E28, E29 checked before typed; the riders at their seats), MISHNAH_TOPICS' row notes, the state doc's #201 addenda 1-3, the recovery page, RESUME, the memory.
'''
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; RES = f'{ROOT}/World/RESUME.md'; MID = f'{ROOT}/logic/MIDDOT.md'
MT = f'{ROOT}/logic/MISHNAH_TOPICS.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'; MSG = f'{SCR}/commit_msg_ch12b.txt'
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-20, 10b D2a done; the state doc #201 add. 2 the newest)", "## 2. WHERE IT STANDS (2026-09-21, 10b docket done; the state doc #201 add. 3 the newest)"),
             (f'- COMMITTED 4af2953 (NOT PUSHED). 10b A + D1 + D2a DONE ({NR1 + NR2} rows in parts A-D; #201 add. 2). NEXT ON "Go": D2b (rows 933-1537), then RUN B.',
              f'- COMMITTED 4af2953 (NOT PUSHED). 10b A + THE DOCKET DONE ({NR:,} rows in parts A-G, three runs; {NRH:,} whole here; #201 add. 3). NEXT ON "Go": RUN B after a compaction.')]
IDX_EDIT = ("10b A + D1 + D2a DONE; NEXT: the docket D2b", "10b A + DOCKET DONE (3 runs); NEXT: RUN B")
MT_EDITS = [("**41. Mishnah, Animal Offerings**", " — 14:4-8 READ WHOLE 2026-09-20 with Zevachim 112b-119b (THE DEUTERONOMY WALK 10b's docket: THE STATIONS' six rows at their folio, the karet (excision) matrix, the eleven differences, the eras' durations, 12:9's two nouns four ways — 119a:9-13); 9:5-6 with 83a-86a (the bones and the sinews); 10:1-2 (the order of offerings); 14:8's 'everlasting inheritance' the answer sheet that retracts the Onias ruling (Megillah 10a:5)."),
            ("**38. Mishnah, Idolatry**", " — 3:5 and 3:7 CARRIED 2026-09-20 from chapter 7's docket (10b's docket); 3:6 READ WHOLE at Avodah Zarah 47a:21 (the fallen wall withdrawn four cubits — 12:3's demolition at the neighbor's edge)."),
            ("**43. Mishnah, Slaughter**", " — 2:1 READ WHOLE 2026-09-20 (10b's docket: THE RITE'S VALUE — the gullet and the windpipe, one sign for a bird and two for an animal — Rabbi's referent for 12:21's 'as I have commanded you', Chullin 28a:5); 2:9 and 6:1 with 84a-b (the blood like water — no covering for the domestic animal); 8:1-4 with 113a-116a (flesh in milk; Rabbi's 12:25 defended by the context, 115b:2); 8:3 at Keritot 22a:5 (the heart's blood); 10:1 (the gifts)."),
            ("**44. Mishnah, Firstborn**", " — 2:2-3 READ WHOLE 2026-09-21 with Bekhorot 15a-16a (10b's docket: THE BLEMISHED CONSECRATED'S TABLE — Rav Sheshet's baraita 15b:9-12, 12:15's release 'only the permission of consumption'); 9:3 (the tithe's partners); 5:3 at 33b:5 (the congested firstborn's bloodletting — three arms); 33a:4-11 the eaters (a gentile; the impure unqualified)."),
            ("**46. Mishnah, Substitution**", " — 3:5 CARRIED 2026-09-21 from the vows' docket (10b's docket: Temurah 3b-4a); 3:1 READ WHOLE at 17b:3 with 17b:15-17 — 12:26's 'only your holy things' the substitutes, 'that you have' the offspring, 12:27 the rule of their treatment."),
            ("**35. Mishnah, Lashes**", " — 3:3 READ WHOLE 2026-09-21 at Makkot 17a:7 with 17a-19b (10b's docket: THE GATES' BAR'S LASHES — R. Shimon's ladder on 12:17's list, the list read backward 17b:9; the impure tithe's warning from the chapter's own gates 19b:7; 13a-b carried); 3:15-16 with 23b (the blood's reward; the lashes and karet (excision); the 613)."),
            ("**28. Mishnah, Suspected Wife**", " — 7:6 READ WHOLE 2026-09-21 at Sotah 38a:1 with 37b-38b (10b's docket: the Name as written in the Temple, its substitute in the country — 12:5's 'to put His name there' by analogy at 38a:10 and by R. Yoshiya's transposition of Exodus 20:20 at 38a:11)."),
            ("**30. Mishnah, Betrothal**", " — 1:9 CARRIED 2026-09-21 with Kiddushin 36b-37a from the borders' docket (10b's docket: the land-bound rule — 12:1's 'in the land')."),
            ("**16. Mishnah, Day of Atonement**", " — 1:1 READ WHOLE 2026-09-20 (10b's docket: 'his house' is his wife — 12:7's household; Rosh Hashanah 6b:15-16 the woman's rejoicing a two-arm parameter)."),
            ("**59. Mishnah, Enabling Liquids**", " — 6:4 READ WHOLE 2026-09-20 (10b's docket: the seven liquids — 'like water' (12:16) for susceptibility, Chullin 33a:12; the four readings of the blood as water)."),
            ("**39. Mishnah, Fathers (ethics)**", " — 2:1 READ WHOLE 2026-09-20 (10b's docket: the ladder of learning behind 12:28's 'observe and hear' — the Sifrei 79:1's kin)."),
            ("**21. Mishnah, Scroll of Esther**", " — 1:10-11 READ WHOLE 2026-09-21 at Megillah 9b:15-10a:1 (10b's docket: the great altar and the small — the Paschal; Shiloh's eating wherever it is seen, Jerusalem's within the walls; after Shiloh the improvised altars permitted, after Jerusalem never — 12:9's inheritance forever; 10a:2-9 the sanctity after the Temple disputed, the Onias ruling retracted); 1:9 read whole, outside the chapter (the two High Priests)."),
            ("**47. Mishnah, Excision Offenses**", " — 5:1 READ WHOLE 2026-09-21 at Keritot 20b:7-8 with 20b-22a (10b's docket: THE BLOOD'S CLASSES — the blood with which the soul departs of an animal or a bird; the species by Leviticus 7:26's general-particular-general (I6); the three classes karet (excision) / lashes / no liability; human blood outside 12:16's ban; the exudate's karet without atonement); 5:2 read whole, outside the chapter."),
            ("**24. Mishnah, Levirate Marriage**", " — Yevamot 47b CARRIED 2026-09-21 from the sanctions docket (10b's docket: the blood's classes' kin)."),
            ("**19. Mishnah, New Year**", " — Rosh Hashanah 4a-6a CARRIED 2026-09-21 from the vows' docket and 6b READ WHOLE (10b's docket: 'you shall not delay' on 12:6's vows and firstlings — a year or three Festivals, 6b:3; Shavuot's date floating with the months, 6b:10; the heir excluded, 6b:13; THE WOMAN BOUND TO REJOICE, 6b:15-16)."),
            ("**34. Mishnah, Courts**", " — 2:4 READ WHOLE 2026-09-21 at Sanhedrin 20b:4, outside the chapter (the king's war); Sanhedrin 20b:8-14 (10b's docket: THE THREE COMMANDMENTS OF THE ENTRY in order; David's rest before the seeking of the site — 12:10-11's order in the run); 74a-b (the persecution — 25 of 33 carried; the limb of a living animal among the seven, 74b:9)."),
            ("**14. Mishnah, Passover**", " — Pesachim 8b CARRIED 2026-09-21 from chapter 11's docket (10b's docket: the Levite's pilgrimage — 12:19)."),]
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:60]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
for a, _ in MT_EDITS:
    if R(MT).count(a) != 1: print('MT ANCHOR', R(MT).count(a), a); ok = False
assert 'THE DOCKET D2b — AS RUN' not in R(MAP) and '#201 ADDENDUM 3' not in R(STATEDOC) and '#201 ADDENDUM 2' in R(STATEDOC)
assert not os.path.exists(MSG), MSG
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT)
mt = R(MT)
for a, b in MT_EDITS:
    lines = mt.split('\n'); i = next(i for i, l in enumerate(lines) if l.startswith(a)); lines[i] = lines[i].rstrip() + b; mt = '\n'.join(lines)
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the docket %d bytes, %d rows; works %d; D2b %d rows, unresolved %d (the check over-counted by %d)' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), NB, NR, NWORKS, NR3, NUNR3, NDOUBLE))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
W(MAP, R(MAP).rstrip('\n') + '\n' + MAPP); W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE); W(REC, rec); W(RES, RESUME + R(RES))
W(MID, R(MID).rstrip('\n') + '\n' + MIDDOT); W(MT, mt); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx); W(MSG, MSG0)
print('written: the map, the state doc, the recovery page, RESUME, MIDDOT, MISHNAH_TOPICS, the memory note, the index, the commit message file (new)')
for p in (MAP, STATEDOC, REC, RES, MID, MT, WALK, IDX):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
