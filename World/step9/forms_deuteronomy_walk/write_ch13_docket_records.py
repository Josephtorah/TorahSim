#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b — the docket's close (2026-09-21, ONE RUN): the map's "THE DOCKET — AS RUN" paragraph, the state doc's #203 addendum 1, the
# recovery page's section-2 lines, RESUME's head, MIDDOT's docket entry (every code checked in MIDDOT.md before it was typed — I1, I2, I4; the juxtapositions
# and the disputes-as-parameters NAMED, no code), MISHNAH_TOPICS' row notes, the memory, the index, the commit message file (NEW — commit_msg_ch13b.txt, the
# headline written at RUN B). EVERY COUNT PARSED from the writer's print (ch13_docket_write.out), the check's print (ch13_d1_check.out) and the chunker's
# print, never typed; every text built whole before its file is opened; the size caps asserted. 10b's form (write_ch12_docket_records.py). Run from the repo
# root; --check runs the anchors and the caps only.
import os, re, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
P = R(f'{SCR}/ch13_docket_write.out')
m = re.search(r'WROTE (\S+) (\d+) bytes', P); OUTP, NB = m.group(1), int(m.group(2))
m = re.search(r'rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \) carried (\d+) unresolved_read_here (\d+) read_here (\d+) dup_dropped (\d+)', P)
NR, NL, NT, NC, NCL, NCT, NCAR, NUNR, NRH, NDUP = map(int, m.groups())
m = re.search(r"verdicts (\{.*?\}) link (\{.*?\}) topic (\{.*?\})", P); VD, VL, VT = (eval(x) for x in m.groups())
LAWC = eval(re.search(r'LAW by cell (\{.*?\})', P).group(1)); NOUT = eval(re.search(r'OUTSIDE by work (\{.*?\})', P).group(1))
UNC = eval(re.search(r'UNCITED (\[.*?\])', P).group(1)); RANGES = eval(re.search(r'ranges (\[.*\])', P).group(1)); NMISH = int(re.search(r'mishnah\+midrash rows (\d+)', P).group(1))
NWORKS = len(set(re.findall(r'^- (.+?) \d+[ab]?:\d+ \[LINK', R(OUTP), re.M)))
assert NRH == NR - NCAR and NUNR + NCAR == NC and len(RANGES) == 14, (NRH, NR, NCAR, NUNR, NC, len(RANGES))
C = R(f'{SCR}/ch13_d1_check.out')
mm = re.search(r"TOTAL (\d+) (\{.*?\}) carried (\d+) unresolved read here (\d+) read here (\d+) LAW by cell \(own notes\) (\{.*?\})", C)
NRC, VDC, NCARC, NUNRC, NRHC, LAWCC = int(mm.group(1)), eval(mm.group(2)), int(mm.group(3)), int(mm.group(4)), int(mm.group(5)), eval(mm.group(6))
assert NRC == NR + NDUP and NCARC == NCAR and NUNRC == NUNR and NRHC == NRH + NDUP, (NRC, NR, NDUP, NCARC, NCAR, NUNRC, NUNR, NRHC, NRH)
PARTS = re.findall(r"^([ABCD]) rows (\d+) (\{.*?\}) carried (\d+) unresolved-read-here (\d+) own (\d+)", C, re.M)
NU = int(re.search(r'U rows (\d+) used (\d+)', C).group(1))
U = R(f'{SCR}/ch13_docket_uncred.out'); chunks = re.findall(r'(ch13_uncred_\d\d\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', U); NUNCRED = sum(int(c[3]) for c in chunks)
assert NUNCRED + NUNR == NRH + NDUP, (NUNCRED, NUNR, NRH, NDUP)   # the chunker counts the dump's duplicate among the uncredited rows; the writer drops it
CARRY = R(f'{SCR}/ch13_credit_carry.out'); mm = re.search(r'credited (\d+) resolved (\d+) unresolved (\d+)', CARRY); assert (int(mm.group(1)), int(mm.group(2)), int(mm.group(3))) == (NC, NCAR, NUNR)
vd = lambda d: ', '.join(f'{k} {d.get(k, 0)}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'))
parts_txt = '; '.join(f'{p} {n} rows ({vd(eval(v))}; {car} carried, {un} unresolved read here, {own} own)' for p, n, v, car, un, own in PARTS)
MAPP = f'''
THE DOCKET — AS RUN (2026-09-21, on "Run" after the compaction at #203 — ITS OWN RUN, ONE RUN under the two-run rule's ~700 clause): logic/oral_triage/
deu_13_reeh_exam_2026-09-21.md — {NR} rows (link {NL} in {NWORKS} works, topic {NT}: the {NMISH} Mishnah, Tosefta and Sifrei rows listed as topic rows;
{"; ".join(f"{n} {s}" for n, s, l in RANGES)}); the verdicts {vd(VD)} (the link rows {vd(VL)}; the topic rows {vd(VT)}); LAW by cell, this docket's own
notes {LAWC}; credited {NC} — {NCAR} CARRIED WITH THEIR LEDGERS' OWN VERDICT LINES (ch13_credit_carry.py, 10b's form) and {NUNR} whose ledger's form carried
no verdict READ WHOLE HERE from ONE SHARED FILE (ch13_docket_U.py — every part imports it, SPEC = CREDITED_SPEC + OWN_U + OWN: no index lookup for the
unresolved rows, and the dump's one duplicate — Tosefta Sanhedrin 14:1, a link row and the whole-chapter row — verdicted once there so both parts match the
same tuple); {NUNCRED} uncredited rows READ WHOLE in {len(chunks)} chunk files at 64,000 bytes, ONE READ PAGE EACH ({", ".join(f"{c[0]} rows {c[1]}-{c[2]} ({c[3]} rows)" for c in chunks)} — 10b's D2
lesson held); {NRH} ROWS READ WHOLE IN THIS RUN; VERDICTED in four parts on disk ({parts_txt}; build() asserting each slice matched — no unmatched address on
the first check of all four; the {NU} shared rows all used); coverage computed (missing 0, extra 0; {NDUP} duplicate address); OUTSIDE by work {NOUT}; the verses
no link row cites {UNC}; lint 0 on the first run. THE INSTRUMENTS derived from 10b's forms by derive_ch13_docket_tools.py with three departures asserted (the
cells' names; the chunk cap 76,000 → 64,000; NO run boundary — SPLIT_AT empty) and the writer by derive_ch13_docket_writer.py (the four parts, the verse
regex and range, the header ch13_docket_hdr.py and the crowns ch13_docket_crowns.py spliced in, the FOURTEEN ranges ASSERTED against the scan's print).
THE CROWNS (the file's finds section): THE SEDUCERS' PARAMETERS FROM ONE NOUN AT THEIR BAVLI SEAT (Sanhedrin 111b:14-15 — "gone out" themselves, "men"
two and not women or children, "Belial" without a yoke, "from your midst" not the border, "their city", "saying" the witnesses and the forewarning for each:
93:1-5 clause by clause; Mishnah 10:4's mode-property inverse THE PROPERTY TABLE'S GROUND); JERUSALEM CANNOT BECOME ONE (Bava Kamma 82b:4, 8 — "to dwell
there", not apportioned to a tribe); THE MAJORITY'S PROCEDURE A PARAMETER (112a:4-5 — imprison each / stone each until half then the sword / multiply the
courts), THE VENUE the Great Sanhedrin from 17:5 (112a:6), THE THRESHOLD thirty days (112a:7-9), THE SELF-DRAWN CITY THE OPEN DILEMMA (112a:2-3); THE
PROPERTY TABLE'S FOUR CELLS FROM THE VERSE'S FOUR PHRASES (112a:10) with its edges (112a:11-17 — the deposits, the joint animal, the wig, the carcass; R.
Shimon's reason), "by any means" (Bava Metzia 31b:3), THE SWORD'S SEAT (Sanhedrin 52b:12); HEAVEN'S SPOIL AT ITS FOLIO (112b:1-113a:2; Temurah 8a:9 — die
/ redeemed / decay / interred; R. Shimon's exclusions; Shmuel's rule; the wall's two capacities); THE HEAP'S ARMS AT THEIR PRINCIPLE (113a:4-6 — R. Avin's
rule, I4 refused / applied) and JERICHO the run's case with Hiel (113a:7-10); "WHOLLY" AS THE WHOLE OFFERING'S CREDIT (111b:12); THE BENEFIT BAN'S SOURCE
AND REACH (Avodah Zarah 12b:7 the stores; 34b:15 the whole animal; Tosefta Avodah Zarah 7:5 the pedestal; Pesachim 48a:5 the warning; Mishnah Shabbat 9:6
any amount; Sukkah 34b:8 THE CITRON OF A CONDEMNED CITY UNFIT; Avodah Zarah 50a:10 an idolatrous offering never nullified); THE ANGER KEYED AND THE MERCY
TWO-ARMED at three seats (Mishnah 10:6, 113b:2-3, Tosefta Sotah 10:1; Shabbat 151b:14, Yevamot 79a:3, Beitzah 32b:4 — DATA rows, no write); THE FALSE
PROPHET'S TABLE AND THE SIGN'S DOMINION (Sanhedrin 90a:2-11 — the essence / the part / the hour; idolatry even a day; R. Yosei HaGelili's dominion at its
Bavli seat, R. Akiva's Hananiah; Mishnah 11:1 and 11:5; 89b:15-21's arms with their grounds — I2 on "thrust", an unspecified death strangling); THE SIGN
AND THE PRESUMPTION (89b:6-7 — the established prophet needs none; 13:2 the definition of a prophet, Horayot 13a:12); ELIJAH AT CARMEL HEEDED and
SAFEGUARDING A MATTER (Yevamot 90b:5-6; the court's emergency stoning the same ground, 90b:10-11); THE INCITER'S MISHNAH AND THE ENTRAPMENT (67a:2-16 — no
forewarning to two hearers, the fence and the lit room, THE FIFTEEN UTTERANCES a three-by-five table, ben Setada hanged); THE COURT'S RULE INVERTED AT ITS
SEAT (33b:7, 36b:5, 43a:21; 85b:2 the son against his father; 61b:3-11 the consent alone, the near teach the far; 63b:7 13:12 the inciter's warning); THE
SEVEN INTERROGATIONS AND THE PROBES (40a:1-4, 40a:15, 40b:1-20 — I2 "diligently" FREE, eleven terms, THE EIGHTH, the tolerance table, the deliberation's
order the rule 13:9 inverts; 41a:18-23 "CERTAIN" THE CONGRUENCE RULE; 40b:21-41a:12 the forewarning's four sources and its purpose; 41a:25 the capital
court's end forty years before the destruction — a clock datum); THE EXECUTION'S TIMING NAMING THE CHAPTER'S THREE (Mishnah 11:4; Tosefta Sanhedrin 11:3);
THE HEADER AT THREE GRAINS (Mishnah Zevachim 8:10 and Zevachim 80a:1-4, 81a:1-4 — the active graver than the passive; Sukkah 34b:3-4 THE COUNTS FROM THE
VERSE'S OWN NUMBERS; Menachot 41b:12-42a:2 four or three strings, no maximum but a minimum; Chagigah 8b:11 the festival's days); THE CHAPTER'S WORDS SPENT
ELSEWHERE (Sotah 39b:9; Chullin 139a:1; Kiddushin 80b:6; Chullin 4b:10; the Belial analogies; Sanhedrin 3a:1's waiver; 54b:5's stoning by "kill"); THE
SPINE'S OWN SEATS ON THE KIN (Sifrei Bamidbar 103, 113 — R. Yitzchak's I1 from idolatry, 114 — the stones and the stone with 13:10-11 inside); THE LAW AS
A STUDY TEXT (Tosefta Sanhedrin 14:1 — the English machine-translated past its head). THE MIDDOT (checked in MIDDOT.md before typing): I1 at Sifrei
Bamidbar 113:1, Sanhedrin 40b:7-8, 40b:10, 41a:8 (the "written though derivable" rider), Mishnah Makkot 1:4 (86:3's ground); I2 at Sanhedrin 40b:4-6
(with the FREENESS rider at 13:15's third verb), 89b:16, 89b:18-19, 84a:14, 54b:5, 41a:4, Bava Batra 10a:10, Ketubot 68a:2, Tosefta Peah 4:19, Berakhot
31b:4; I4 at Sanhedrin 113a:4-6 (refused by R. Yosei HaGelili under R. Avin's rule, applied by R. Akiva); the doubled verb NAMED at Bava Metzia 31b:3 and
Sanhedrin 33b:7, no code. THE DISPUTES AS PARAMETERS: the_prophets_death (89b:15-21, 90a:1-11, 67a:7-8, 84a:14, Mishnah 11:1), the_signs_status (90a:10-11,
89b:6-7), the_execution_timing (Mishnah 11:4, Tosefta 11:3), the_inquiries' COUNT (40b:11-14) and the hour's tolerance (40a:8), the probes' weight
(41a:23), the majority's procedure (112a:4-5), a city in two tribes (111b:16-19), the self-drawn city (112a:2-3), the square (112a:18), the heap
(113a:4-6), the consecrated animals (112b:2-6), the heave offering by possession (112b:10-11), the second tithe Heaven's (112b:12), the species' counts
(Sukkah 34b:2-7), the strings (Menachot 41b:12-15), the mixed bloods (Zevachim 80a:2-4, 81a:2-4; Eruvin 100a:18), the festival's days (Chagigah 8b:11),
the consent alone (61b:3-9), the deaths' severity order (40b:8). THE LESSONS: ONE SHARED FILE for the unresolved rows spares every part an index lookup and
verdicts the dump's duplicate once; the check's total counts the duplicate, the writer's drops it — the records assert the difference from the prints; the
export's empty rows (Sanhedrin 90a:14; Tosefta Sanhedrin 11:1, 12:1-4) are read as empty and said so; a machine-translated Tosefta row is read whole and its
illegible tail named. COMPILE_DEBT's 11b box (l) is marked PAID with the box at RUN B. THE INSTRUMENTS (the scratchpad, copied by copy_ch13_docket_forms.py):
derive_ch13_docket_tools.py and its five, ch13_credit_carry.out, ch13_credited_rows.py, ch13_docket_U.py, ch13_docket_A-D.py, ch13_d1_check.py and its
print, ch13_docket_hdr.py, ch13_docket_crowns.py, derive_ch13_docket_writer.py, write_ch13_docket.py and its print, write_ch13_docket_records.py, the dump.
RUN B next on the owner's word, after a compaction: the probes to FAIL (Q34-Q36, BEFORE the types; the reuse literals adding_barred / cleaving_commanded /
pity_barred ONE grepped and retyped from the print), the types with the docket's names and values (the_prophets_death — stoning the Sifrei's and the
Rabbis' / strangling R. Shimon's and the answer sheet's; the_signs_status — R. Yosei HaGelili's dominion / R. Akiva's fallen prophet; the_execution_timing
— kept to the Festival / at once with the notice; the_inquiries — the seven, "I do not know" voids the interrogations not the examinations, a contradiction
both, "certain" the congruence rule; the majority's procedure, the self-drawn city and the property table's edges as DATA rows), the callees' facts, the
runner cold_run_seducers.py the 68th, the recorder with the cache off, the stitcher, the literals DE1-DE9, the tape, the chain LAUNCHED, the clean point;
THE TAIL.
'''
STATE = f'''
#203 ADDENDUM 1 (2026-09-21, at the close of THE DOCKET of THE DEUTERONOMY WALK sitting 11b — ITS OWN RUN, ONE RUN, on the owner's "Run" after the compaction at #203 — A CLEAN COMPACTION POINT): THE STATE: THE DOCKET WRITTEN — logic/oral_triage/deu_13_reeh_exam_2026-09-21.md, {NR} rows (link {NL} in {NWORKS} works, topic {NT}; {vd(VD)}; LAW by cell, own notes {LAWC}; credited {NC}: {NCAR} CARRIED with their ledgers' own verdict lines by ch13_credit_carry.py, {NUNR} read whole here from the shared file ch13_docket_U.py; {NRH} rows read whole in this run — {NUNCRED} uncredited in {len(chunks)} chunk files at 64,000 bytes, one Read page each; the fourteen ranges asserted; coverage computed, missing 0, extra 0; lint 0 on the first run), the instruments derived from 10b's forms (derive_ch13_docket_tools.py — the cap 64,000, no run boundary; derive_ch13_docket_writer.py → write_ch13_docket.py with the header and the crowns typed); the parts A-D on disk ({parts_txt}); the map's "THE DOCKET — AS RUN" paragraph (the crowns, the middot, the parameters, the lessons), MIDDOT's docket entry (I1, I2, I4 checked before typed), MISHNAH_TOPICS' row notes, RESUME, the recovery page, the memory, the commit message file started (<scratch>/commit_msg_ch13b.txt — the headline at RUN B); the forms copied. THE TIMING (the sitting's tsv continued): the tools derived, the carry, the chunker and the survey under a second each; the parts' check, the writer's derive and the writer under a second each — the run's machine time nothing, its reading the whole. NOT COMMITTED (since fb797a1): this docket and its records. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (compact before RUN B). NEXT ON "Go": RUN B — patch_probes_ch13.py (Q34-Q36 to FAIL, BEFORE the types — 7b's lesson 2; the literals holding adding_barred ONE (CC3 at cold_run_sequence.py's count over ab_oh), cleaving_commanded ONE (the 8b checkpoint if it counts) and pity_barred ONE (the 5b checkpoint if it counts) grepped — retyped ONE → TWO from the print BEFORE the tape), add_types_ch13.py (event_vocabulary +5: word_sealed, prophet_test_declared, inciter_law_declared, condemned_city_law_declared — form statute, witnesses Deut 13:1, 13:2, 13:7, 13:13 — and seducers_case; effect_vocabulary +7: false_prophet_hearing_barred, devoted_thing_cleaving_barred (block), tested_by_the_lord, israel_hears_and_fears, condemned_city_inquiry_required (status), evil_purged_from_the_midst (body — THE PURGE FORMULA'S FIRST SEAT OF NINE), city_devoted (destroy); adding_barred's, cleaving_commanded's and pity_barred's rows amended with the chapter's seats; daemon_dispositions law_seducers given_at Deut 13:1 installed_by boot, the seven WRAPPED (the six cells and the_readback — 10b's lesson 3); dependency_dispositions the span [[Deut, 13, 1, 19]] and the nineteen CALL edges predicted, the one AS_WHEN pointer at 13:18 — the census decides; installation_probes I5 72 → 73; calendar_parameters.yaml +4 — the_signs_status (R. Yosei HaGelili's dominion — the sign real and no title / R. Akiva's — only a once-true prophet, Hananiah; Sanhedrin 90a:10-11), the_prophets_death (stoning — the Sifrei 86:6, 90:2 and the Rabbis by I2 on "thrust" / strangling — R. Shimon and Mishnah Sanhedrin 11:1's list; 89b:15-21), the_execution_timing (kept to the Festival, R. Akiva / at once with the notice, R. Yehuda — Mishnah 11:4, Tosefta 11:3 naming the chapter's three), the_inquiries (the seven from three verses' terms; "I do not know" voids the interrogations, not the examinations; a contradiction voids both; "certain" the congruence rule; the eighth R. Abbahu's — Mishnah 5:1-2, Sanhedrin 40a-41a)), ch13_callees.py (every CALL's facts printed before any assert — nineteen callees), the runner cold_run_seducers.py the 68th in parts with ch13_fastcheck.py and ch13_cases_gen.py (six cells F1-F6 and the_readback's nineteen rows; the docket's crowns as exam rows — the fifteen utterances, the seven interrogations, the property table's cells, Heaven's spoil, the false prophet's table, the inciter's kin, the entrapment's script, the citron of a condemned city, the store with roses; the exempt persons — Elijah at Carmel, the prophet keeping part of another commandment, the inciter who retracts; the lashes person — Makkot 22a's devoted benefit if read so), seq_record_ch13.py (INK_CACHE=0) and seq_stitch_ch13.py (no marker — the four lines on the counter's day (40, 11, 1)), patch_seq_literals_ch13.py (DE1-DE9; RUN = (1327, 96, 88, 0, 12, 1634, 44, 319, the four pairs, 127) predicted), the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, write_ch13b_records.py and copy_ch13b_forms.py WRITTEN (RUN A's instruments in the copier too), gates_chain.sh LAUNCHED in the background, the clean point → THE TAIL after the compaction (the summary read once, the demands filed, the records from the sheet in one call — the map's AS BUILT, COMPILE_DEBT's sitting-11 box PAID and the 11b box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6 row, RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory — the forms, the commit message, the 11b timing rows reported). POST-COMPACTION REREADS: the recovery page, the map's "Sitting 11b … THE DESIGN" (the newest section) with its "THE DOCKET — AS RUN" paragraph, MEMORY.md; THE_STEPS' compiler block, Step 2's head and Step 5's head BEFORE any derive.
'''
RESUME = f'''# ⚠ THE DEUTERONOMY WALK sitting 11b — THE DOCKET DONE IN ONE RUN (2026-09-21; logic/oral_triage/deu_13_reeh_exam_2026-09-21.md — {NR} rows, {NCAR} carried with
# their ledgers' verdicts, {NRH} read whole here; {vd(VD)}): the seducers' parameters from one noun at their Bavli seat (Sanhedrin 111b:14-15), Jerusalem
# never a condemned city (Bava Kamma 82b:8), the majority's procedure a parameter and the self-drawn city an open dilemma (112a:2-5), the property table's four
# cells from four phrases (112a:10), Heaven's spoil and the wall's two capacities (112b-113a), the heap's arms at R. Avin's principle and Jericho with Hiel
# (113a:4-10), the false prophet's table and the sign's dominion (90a:2-11), the sign and the presumption (89b:6-7), Elijah at Carmel heeded (Yevamot 90b:5-6),
# the entrapment and the fifteen utterances (67a:2-16), the seven interrogations with the eighth and "certain" the congruence rule (40a-41a), the citron of a
# condemned city unfit (Sukkah 34b:8). NEXT: RUN B after a compaction (the probes to FAIL, the types, the runner cold_run_seducers.py, the tape, the chain launched).
'''
MIDDOT = f'''
### THE DEUTERONOMY WALK 11b — THE DOCKET OF CHAPTER 13 (2026-09-21, one run; logic/oral_triage/deu_13_reeh_exam_2026-09-21.md, {NR} rows — {NCAR} carried, {NRH} read whole here)
Every code checked in this file's tables before it was typed. I1 (qal wa-chomer, the a-fortiori): Sifrei Bamidbar 113:1 — R. Yitzchak: if IDOLATRY, the
gravest, is not liable without forewarning, how much more every commandment — so "those who found him" teaches the warning NAMES THE LABOR (the inciter's
warning WAIVED at Sanhedrin 67a:4 the chapter's exception — a DATA row); Sanhedrin 40b:7 — the seven interrogations to the strangled and the burned from the
stoned and the sword; 40b:8 — the inference stands for the Rabbis' severity order, not R. Shimon's (the order a parameter); 40b:10 and 41a:8 — THE RIDER: a
matter derivable by a-fortiori the verse still writes; Mishnah Makkot 1:4 — the plotting witness defined, the ground of the Sifrei 86:3's a-fortiori for the
false prophet's death. I2 (gezerah shavah, the verbal analogy): Sanhedrin 40b:4-6 — "diligently" / "diligently" / "diligently" (13:15, 17:4, 19:18) with THE
FREENESS RIDER (the word superfluous by design; at 13:15 the third verb the freeness — 92:2); 89b:16 — the Rabbis: "thrust" of the prophet (13:6) from
"thrust" of the layman (13:11), stoned (the Sifrei 86:6, 90:2 at its Bavli seat); 89b:18-19 — the city's subverters' "drawn away" (13:14) from either, R.
Shimon's from the prophet; 84a:14 — "shall be put to death" of the non-priest (Numbers 18:7) from the prophet's (13:6): stoning (R. Akiva) / strangling (R.
Yochanan ben Nuri); 54b:5 — "you shall kill" of bestiality from "you shall kill him … stone him" (13:10-11): stoning; 41a:4 — "the matter" (22:24) / speech:
the verbal forewarning; Bava Batra 10a:10, Ketubot 68a:2, Tosefta Peah 4:19 — "Belial" (15:9) / "Belial" (13:14): the eye averted from charity as idolatry;
Berakhot 31b:4 — Hannah's "Belial" (1 Samuel 1:16) / 13:14: the drunken prayer as idolatry; Sanhedrin 67a:21-22 (carried, outside) — the witch's death. I4
(kelal u-frat, general then particular): Sanhedrin 113a:4-6 — "a heap forever" (a positive generalization) and "not built again" (a prohibition's detail):
R. Yosei HaGelili REFUSES the reading under R. Avin's rule (a positive general followed by a negative detail is two laws), R. Akiva applies it (the general
means only the detail — gardens permitted); at 113a:6 both accept R. Avin and dispute "again". THE DOUBLED VERB — no code, named: Bava Metzia 31b:3 ("smite,
you shall smite" — by any means), Sanhedrin 33b:7 (Rav Kahana: "kill, you shall kill him" — the court's rule inverted), 40b:6 (the Torah could have doubled
one verb — the freeness). THE MNEMONIC — named: Sanhedrin 40b:2 (escapes, sword, forewarning — the three cases' differences). THE DISPUTES AS PARAMETERS
(the machine's data channel): Sanhedrin 89b:15-21, 90a:1-11, 67a:7-8, 84a:14 with Mishnah Sanhedrin 11:1 (the_prophets_death — stoning / strangling; the
essence, the part, the hour; idolatry even a day); 90a:10-11 with 89b:6-7 (the_signs_status — R. Yosei HaGelili's dominion / R. Akiva's fallen prophet; the
established prophet needs no sign); Mishnah Sanhedrin 11:4 and Tosefta Sanhedrin 11:3 (the_execution_timing — kept to the Festival / at once with the notice);
40b:11-14 (the interrogations' count — seven / eight), 40a:8 (the hour's tolerance — one / two hours), 41a:23 (ben Zakkai's probes weighed as interrogations);
40b:8 (the deaths' severity — the Rabbis / R. Shimon); 61b:3-9 (the incited's consent alone — the individual / the multitude); 112a:4-5 (the majority's
procedure — imprison / stone until half / multiply the courts); 111b:16-19 (one city in two tribes); 112a:2-3 (the self-drawn city — open); 112a:18 (the
square — from the outset / made); 113a:4-6 (the heap — no gardens / gardens); 112b:2-6 (the consecrated animals — die / graze / redeemed), 112b:10-11 (the
heave offering by possession), 112b:12 (the second tithe Heaven's or the owner's); Sukkah 34b:2-7 (the species' counts — three / one myrtle); Menachot
41b:12-15 (the strings — four / three); Zevachim 80a:2-4, 81a:2-4 and Eruvin 100a:18 (the mixed bloods — four placements / one; the active graver than the
passive); Chagigah 8b:11 (the festival's animals completed / an added day). THE JUXTAPOSITION — none this docket.
'''
MEMO = f'''
THE DOCKET DONE IN ONE RUN (2026-09-21, on "Run" after the compaction at #203): deu_13_reeh_exam_2026-09-21.md — {NR} rows ({vd(VD)}; credited {NC}: {NCAR} carried
with their ledgers' own verdict lines, {NUNR} read whole here from ONE SHARED FILE ch13_docket_U.py; {NRH} rows read whole in this run — {NUNCRED} uncredited in {len(chunks)} chunks at
64,000 bytes, one Read page each); LAW by cell, own notes {LAWC}; the crowns: the seducers' parameters from one noun at their Bavli seat (Sanhedrin 111b:14-15),
Jerusalem never a condemned city (Bava Kamma 82b:8), the majority's procedure a parameter and the self-drawn city an open dilemma (112a:2-5), the property table's
four cells from four phrases (112a:10) with its edges, Heaven's spoil and the wall's two capacities (112b-113a), the heap's arms at R. Avin's principle (I4) and
Jericho with Hiel (113a:4-10), the false prophet's table and the sign's dominion (90a:2-11), the sign and the presumption (89b:6-7), Elijah at Carmel heeded and
safeguarding (Yevamot 90b:5-6), the entrapment with the fifteen utterances (67a:2-16), the seven interrogations with the eighth and "certain" the congruence rule
(40a-41a), the citron of a condemned city unfit (Sukkah 34b:8), the benefit ban's source (Avodah Zarah 12b:7). LESSON: ONE SHARED FILE for the unresolved rows —
every part imports it; no index lookup; the dump's duplicate verdicted once. NEXT: RUN B after a compaction (the state doc's #203 addendum 1 the newest).
'''
MSG0 = f'''CHAPTER 13 COMPILED AND ON THE TAPE — (THE HEADLINE WRITTEN AT RUN B). THE DOCKET, ONE RUN (2026-09-21, on the owner's "Run" after the compaction at #203): logic/oral_triage/deu_13_reeh_exam_2026-09-21.md — {NR} rows ({vd(VD)}; link {NL} in {NWORKS} works, topic {NT}: the fourteen folio ranges whole, the twenty-two Mishnah rows, the Tosefta and Sifrei chapters; credited {NC} — {NCAR} CARRIED WITH THEIR LEDGERS' OWN VERDICT LINES (ch13_credit_carry.py, 10b's form), {NUNR} read whole here from ONE SHARED FILE where the ledger's form carried no verdict; {NRH} rows read whole in this run — {NUNCRED} uncredited in four chunks at 64,000 bytes, one Read page each), coverage computed, the fourteen ranges asserted, lint 0 on the first run; its crowns: THE SEDUCERS' PARAMETERS FROM ONE NOUN AT THEIR BAVLI SEAT (Sanhedrin 111b:14-15 — "gone out" themselves, "men" two and not women or children, "Belial" without a yoke, "from your midst" not the border, "saying" the witnesses and the forewarning), JERUSALEM NEVER A CONDEMNED CITY by "to dwell there" (Bava Kamma 82b:8), THE MAJORITY'S PROCEDURE A PARAMETER and THE SELF-DRAWN CITY AN OPEN DILEMMA (Sanhedrin 112a:2-5), THE PROPERTY TABLE'S FOUR CELLS FROM THE VERSE'S FOUR PHRASES with its edges (112a:10-17), HEAVEN'S SPOIL and the wall's two capacities (112b:1-113a:2), THE HEAP'S ARMS AT R. AVIN'S PRINCIPLE (I4 refused and applied — 113a:4-6) and JERICHO WITH HIEL the run's case (113a:7-10), "WHOLLY" AS THE WHOLE OFFERING'S CREDIT (111b:12), THE BENEFIT BAN'S SOURCE AND REACH (Avodah Zarah 12b:7; 34b:15; Tosefta Avodah Zarah 7:5; Pesachim 48a:5; Sukkah 34b:8 the citron of a condemned city; Avodah Zarah 50a:10 the offering never nullified), THE FALSE PROPHET'S TABLE AND THE SIGN'S DOMINION (Sanhedrin 90a:2-11 with Mishnah Sanhedrin 11:1 and 11:5), THE SIGN AND THE PRESUMPTION (89b:6-7), ELIJAH AT CARMEL HEEDED AND SAFEGUARDING A MATTER (Yevamot 90b:5-6), THE INCITER'S MISHNAH AND THE ENTRAPMENT with THE FIFTEEN UTTERANCES a three-by-five table (67a:2-16), THE COURT'S RULE INVERTED AT ITS SEAT with the son against his father (33b:7, 85b:2), THE SEVEN INTERROGATIONS AND THE PROBES with the verbal analogy's freeness, THE EIGHTH and "CERTAIN" THE CONGRUENCE RULE (40a-41a), THE EXECUTION'S TIMING NAMING THE CHAPTER'S THREE (Tosefta Sanhedrin 11:3), THE HEADER AT THREE GRAINS (Zevachim 80a-81a, Sukkah 34b:3-4, Menachot 41b:12-42a:2), THE SPINE'S OWN SEATS ON THE KIN (Sifrei Bamidbar 103, 113, 114); MIDDOT's docket entry (I1, I2, I4 checked before typed; the freeness rider at 13:15's third verb), MISHNAH_TOPICS' row notes, the state doc's #203 addendum 1, the recovery page, RESUME, the memory.
'''
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; RES = f'{ROOT}/World/RESUME.md'; MID = f'{ROOT}/logic/MIDDOT.md'
MT = f'{ROOT}/logic/MISHNAH_TOPICS.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'; MSG = f'{SCR}/commit_msg_ch13b.txt'
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-21, 11b RUN A closed; the state doc #203 the newest)", "## 2. WHERE IT STANDS (2026-09-21, 11b docket done; state doc #203 add. 1 newest)"),
             ("- COMMITTED fb797a1 (2026-09-21; NOT PUSHED). NEXT ON HIS WORD: THE DOCKET, one run (566 addresses, 196 credited); then RUN B.",
              f"- COMMITTED fb797a1 (NOT PUSHED). DOCKET DONE, one run ({NR} rows, {NRH} whole here; #203 add. 1). NEXT ON HIS WORD: RUN B after a compaction.")]
IDX_EDIT = ("11b RUN A CLOSED (the design); COMMITTED fb797a1, NOT PUSHED; NEXT: the docket, one run", "11b RUN A + DOCKET DONE (1 run); COMMITTED fb797a1, NOT PUSHED; NEXT: RUN B")
MT_EDITS = [("**34. Mishnah, Courts**", f" — 10:4-6 READ WHOLE 2026-09-21 with Sanhedrin 111b-113b (THE DEUTERONOMY WALK 11b's docket: THE CONDEMNED CITY — the seducers' parameters from one noun 111b:14-15, the mode-property inverse, the property table's four cells 112a:10, Heaven's spoil 112b:1, the heap's arms at R. Avin's principle 113a:4-6, Jericho and Hiel 113a:7-10; deu_13_reeh_exam_2026-09-21.md); 7:10 CARRIED and 67a READ WHOLE (the inciter's mishnah, the entrapment, the fifteen utterances 67a:6); 5:1-2 with 40a-41a (the seven interrogations, the eighth 40b:11, the tolerance table, 'certain' the congruence rule 41a:18-19); 11:1 and 11:5 read whole (the false prophet's table — strangling the answer sheet's arm) with 89a-90a (the sign's dominion 90a:10-11; the presumption 89b:6-7); 11:4 (the execution's timing; Tosefta Sanhedrin 11:3 naming the chapter's three); 1:5 and 4:1 carried; 7:6 carried (the honors); 88b carried whole from chapter 4."),
            ("**35. Mishnah, Lashes**", " — 1:4-5 READ WHOLE 2026-09-21 (11b's docket: the plotting witness defined — the ground of the Sifrei 86:3's a-fortiori for the false prophet's death; 1:5's multiplicity outside the chapter); 1:6 carried; Makkot 22a:2, 22a:9 the lashes for the devoted thing's benefit (the link rows on 13:18)."),
            ("**41. Mishnah, Animal Offerings**", " — 8:10 READ WHOLE 2026-09-21 with Zevachim 80a-81b (11b's docket: THE MIXED BLOODS — four placements 'do not add', one 'do not diminish' (13:1); the active graver than the passive 80a:4; the dispute's true field the intermingled cups 81a:2; the range's tail on the placements outside)."),
            ("**17. Mishnah, Booth**", " — 3:4 READ WHOLE 2026-09-21 with Sukkah 34b (11b's docket: THE FOUR SPECIES' COUNTS FROM THE VERSE'S OWN NUMBERS 34b:3 — one citron, one palm branch by the defective spelling, three boughs, two willows; each indispensable by 'a complete taking' 34b:4; adding a species the barred edge of 13:1); 3:5 at 34b:8 — THE CITRON OF A CONDEMNED CITY UNFIT (13:18's devoted thing in the answer sheet's list)."),
            ("**12. Mishnah, Sabbath**", " — 9:6 READ WHOLE 2026-09-21 with Shabbat 90a:6 (11b's docket: idolatry's accessories carried out — any amount, R. Yehuda from 13:18); Shabbat 151b READ WHOLE (151b:14 the mercy two-armed — 'give you mercy' as compassion for creatures returned from Heaven; the rest outside)."),
            ("**38. Mishnah, Idolatry**", " — 3:3-4 and 3:9 CARRIED 2026-09-21 from chapter 7's docket with Avodah Zarah 49b (11b's docket); 50a READ WHOLE (Mercury's stones by proximity; AN IDOLATROUS OFFERING NEVER NULLIFIED 50a:10 — Psalms 106:28); 12b:7 THE BENEFIT BAN'S SOURCE from 13:18 (the stores adorned with roses); 34b:15 the whole animal against the stoned ox's flesh; 42a, 43b, 44b, 48b carried (the link rows on 13:18)."),
            ("**39. Mishnah, Fathers (ethics)**", " — 3:9 and 3:14 READ WHOLE 2026-09-21 (11b's docket: the footer's rows — fear of sin before wisdom; Israel called children, 14:1 ahead); 2:1 carried from chapter 12's docket."),
            ("**19. Mishnah, New Year**", " — Rosh Hashanah 28b CARRIED WHOLE 2026-09-21 from chapter 4's docket (11b's docket: the priests' blessing not added to — 13:1 at the word's grain, 82:5)."),
            ("**13. Mishnah, Merging Domains**", " — Eruvin 96a CARRIED WHOLE 2026-09-21 from chapter 4's docket (11b's docket: 13:1's not-adding at the phylacteries' seat); 100a:18 READ WHOLE (R. Eliezer and R. Yehoshua: one sprinkling 'do not diminish', four 'do not add')."),
            ("**32. Mishnah, Middle Gate**", " — Bava Metzia 59b CARRIED WHOLE 2026-09-21 from chapter 4's docket (11b's docket: the oven of Akhnai — the sign not decisive, the false prophet's kin); 31b:3 READ WHOLE ('smite, you shall smite' — the condemned city's people by any means)."),
            ("**24. Mishnah, Levirate Marriage**", " — Yevamot 90b READ WHOLE 2026-09-21 (11b's docket: ELIJAH AT CARMEL HEEDED — 'to him you shall listen' (18:15) even to transgress for the hour, 90b:5; safeguarding a matter different, 90b:6; the court's emergency stoning the same ground 90b:10-11; the mishnah's tail outside); 79a:3 David's three marks — the merciful from 13:18; 122b:8 13:15's inquiry to monetary law by 'one law'."),
            ("**42. Mishnah, Grain Offerings**", " — Menachot 41b-42a READ WHOLE 2026-09-21 (11b's docket: THE FRINGES' STRINGS four or three 41b:12 — the count's grain of 13:1's not-adding; no maximum but a minimum 42a:1; 40b:10 a second set an act; the placement and the blessing outside)."),
            ("**43. Mishnah, Slaughter**", " — Chullin 4b:10, 139a:1, 140a:13 and 89a:11-12 READ WHOLE 2026-09-21 (11b's docket: 'entice' with food and drink; 'purge the evil' (13:6) on a bird liable to death; the burned city's ashes not for the covering of the blood)."),
            ("**46. Mishnah, Substitution**", " — Temurah 8a:9 READ WHOLE 2026-09-21 (11b's docket: Tosefta Sanhedrin 4:5 at Temurah's seat — R. Shimon's 'its animals' excludes the firstborn and the tithe, 'its spoil' the second-tithe money, 13:16-17)."),
            ("**40. Mishnah, Erroneous Rulings**", " — Horayot 13a:12 and Tosefta Horayot 2:8 READ WHOLE 2026-09-21 (11b's docket: 'sign' means a prophet from 13:2 — the definition of a prophet in the precedence table)."),
            ("**23. Mishnah, Pilgrimage Offering**", " — Chagigah 8b:11 READ WHOLE 2026-09-21 (11b's docket: the festival peace offering's animals completed on another day — no 'do not add' (Reish Lakish) / an added day (R. Yochanan): 13:1 at the day's grain)."),
            ("**14. Mishnah, Passover**", " — Pesachim 48a:5 READ WHOLE 2026-09-21 (11b's docket: 13:18 THE WARNING for benefit from the worshipped tree's wood)."),
            ("**1. Mishnah, Blessings**", " — Berakhot 31b:4 READ WHOLE 2026-09-21 (11b's docket: the drunken prayer as idolatry by the verbal analogy 'Belial' — Hannah / 13:14)."),
            ("**30. Mishnah, Betrothal**", " — Kiddushin 80b:6 READ WHOLE 2026-09-21 (11b's docket: the allusion to seclusion from 13:7's 'the son of your mother'; Sanhedrin 21b:2 the reading)."),
            ("**25. Mishnah, Marriage Contracts**", " — Ketubot 68a:2 READ WHOLE 2026-09-21 (11b's docket: the eye averted from charity as idolatry — 'Belial' 15:9 / 13:14, with Bava Batra 10a:10 and Tosefta Peah 4:19)."),
            ("**33. Mishnah, Last Gate**", " — Bava Batra 10a:10 READ WHOLE 2026-09-21 (11b's docket: R. Yehoshua ben Korcha's analogy on 'Belial' — 13:14's word for the charity refuser)."),
            ("**31. Mishnah, First Gate**", " — Bava Kamma 82b:4 and 82b:8 READ WHOLE 2026-09-21 (11b's docket: THE TEN MATTERS OF JERUSALEM — it cannot become a condemned city; the reason from 13:13's 'to dwell there', not apportioned to a tribe)."),
            ("**18. Mishnah, Festival Day**", " — Beitzah 32b:4 READ WHOLE 2026-09-21 (11b's docket: the wealthy without compassion not Abraham's seed — 13:18's mercy the seed's mark; a DATA row)."),
            ("**28. Mishnah, Suspected Wife**", " — Sotah 39b:9 READ WHOLE 2026-09-21 (11b's docket: walk after the Torah scroll from 13:5's first verb); 14a:3 carried (the attributes walked after); Tosefta Sotah 10:1 read whole (the anger keyed to the wicked's presence — 13:18)."),
            ("**2. Mishnah, Corner of the Field**", " — Tosefta Peah 4:19 READ WHOLE 2026-09-21 (11b's docket: the charity refuser as an idolater by 'Belial' — 13:14)."),]
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:60]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
for a, _ in MT_EDITS:
    if sum(1 for l in R(MT).split('\n') if l.startswith(a)) != 1: print('MT ANCHOR', a); ok = False
assert 'THE DOCKET — AS RUN (2026-09-21, on "Run"' not in R(MAP) and '#203 ADDENDUM 1' not in R(STATEDOC) and '#203 — COMMITTED fb797a1' in R(STATEDOC)
assert R(MAP).rstrip('\n').split('\n')[-1].startswith("11's, for the owner's word).") or 'Sitting 11b — THE COMPILE OF CHAPTER 13' in R(MAP)[-70000:]
assert not os.path.exists(MSG), MSG
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT)
mt = R(MT)
for a, b in MT_EDITS:
    lines = mt.split('\n'); i = next(i for i, l in enumerate(lines) if l.startswith(a)); lines[i] = lines[i].rstrip() + b; mt = '\n'.join(lines)
for name, txt in (('MAPP', MAPP), ('STATE', STATE), ('RESUME', RESUME), ('MIDDOT', MIDDOT), ('MEMO', MEMO), ('MSG0', MSG0)):
    assert not re.search(r'/Users/(?!Shared/)', txt) and os.path.expanduser('~') not in txt and '/private' + '/tmp' not in txt, name
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the docket %d bytes, %d rows; works %d; parts %s; chunks %d; shared rows %d' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), NB, NR, NWORKS, [(p, n) for p, n, *_ in PARTS], len(chunks), NU))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
W(MAP, R(MAP).rstrip('\n') + '\n' + MAPP); W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE); W(REC, rec); W(RES, RESUME + R(RES))
W(MID, R(MID).rstrip('\n') + '\n' + MIDDOT); W(MT, mt); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx); W(MSG, MSG0)
print('written: the map, the state doc, the recovery page, RESUME, MIDDOT, MISHNAH_TOPICS, the memory note, the index, the commit message file (new)')
for p in (MAP, STATEDOC, REC, RES, MID, MT, WALK, IDX):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
