#!/usr/bin/env python3
# THE DEUTERONOMY WALK 9b — the docket run's close (2026-09-20): the map's "THE DOCKET — AS RUN" paragraph, the state doc's #199 addendum 1, the recovery
# page's section-2 lines, RESUME's head, MIDDOT's docket entry (every code checked in MIDDOT.md before it was typed — I1, I2, E26, E28; the do-not-read
# readings and the juxtapositions NAMED, no code), MISHNAH_TOPICS' eight row notes, the memory, the index, the commit message file (NEW — commit_msg_ch11.txt,
# the headline written at RUN B). EVERY COUNT PARSED from the writer's print (ch11_docket_write.out), never typed; every text built whole before its file is
# opened; the size caps asserted. 8b's form (write_ch10_docket_records.py). Run from the repo root.
import os, re, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
P = R(f'{SCR}/ch11_docket_write.out')
m = re.search(r'WROTE (\S+) (\d+) bytes', P); OUTP, NB = m.group(1), int(m.group(2))
m = re.search(r'rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \) carried (\d+) unresolved_read_here (\d+) read_here (\d+) dup_dropped (\d+)', P)
NR, NL, NT, NC, NCL, NCT, NCAR, NUNR, NRH, NDUP = map(int, m.groups())
m = re.search(r"verdicts (\{.*?\}) link (\{.*?\}) topic (\{.*?\})", P); VD, VL, VT = (eval(x) for x in m.groups())
LAWC = eval(re.search(r'LAW by cell (\{.*?\})', P).group(1)); NOUT = eval(re.search(r'OUTSIDE by work (\{.*?\})', P).group(1))
UNC = eval(re.search(r'UNCITED (\[.*?\])', P).group(1)); RANGES = eval(re.search(r'ranges (\[.*\])', P).group(1)); NMISH = int(re.search(r'mishnah\+midrash rows (\d+)', P).group(1))
NWORKS = len(set(re.findall(r'^- (.+?) \d+[ab]?:\d+ \[LINK', R(OUTP), re.M)))
assert NRH == NR - NCAR and NUNR + NCAR == NC, (NRH, NR, NCAR, NUNR, NC)
vd = lambda d: ', '.join(f'{k} {d.get(k, 0)}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'))
MAPP = f'''
THE DOCKET — AS RUN (2026-09-20, on "Go" after the compaction at #199 — ITS OWN RUN under the two-run rule's docket clause): logic/oral_triage/
deu_11_ekev_reeh_exam_2026-09-20.md — {NR} rows (link {NL} in {NWORKS} works, topic {NT}: the eight Mishnah rows; {"; ".join(f"{n} {s}" for n, s, l in RANGES)};
Tosefta Sotah 8 and Tosefta Sheviit 4 whole; Tosefta Sotah 8:6 listed twice in the dump — the link row and the chapter's listing — taken once, {NDUP} dropped, computed);
the verdicts {vd(VD)} (the link rows {vd(VL)}; the topic rows {vd(VT)}); LAW by cell, this docket's own notes {LAWC}; credited {NC} — {NCAR} CARRIED WITH THEIR
LEDGERS' OWN VERDICT LINES (ch11_credit_carry.py over the crediting ledgers by regex on their two forms: chapter 6's docket 298, the Devarim docket 75, the Musafim
docket 48, chapter 5's 35, the borders' 34, chapter 7's 26, chapter 4's 15, chapter 10's 15, the rest by ones — THE CREDITED ROW LISTED WITH ITS LEDGER, its note
beginning "CREDITED (<ledger>; carried) —") and {NUNR} whose ledger's form carried no verdict (the Exodus and Genesis triages' CREDIT rows, the topic dockets' lists,
the gen_ tables) READ WHOLE HERE; {NRH} ROWS READ WHOLE IN THIS RUN in ten chunk files (ch11_docket_uncred.py — 27,000 bytes each, the row printed entire);
coverage computed (missing 0, extra 0); lint 0 after one gloss on a carried word; the verses no row cites {UNC}. THE CROWNS (the file's finds section): THE YOKE
OF THE COMMANDMENTS NAMED BY THE ANSWER SHEET (Berakhot 14b:11 — the Mishnah's reason; 14b:12-14 the paragraph typed TEACH AND PERFORM; 14b:19 Rav's order;
14b:24 the Shema without tefillin false testimony) — yoke_of_the_commandments_accepted's name and value CONFIRMED; THE PRAYER FROM THE PARAGRAPH'S OWN CLAUSE
AND THE RAIN ATTACHED TO IT (Ta'anit 2a:11 — 11:13's "serve Him with all your heart" is prayer, 11:14's rain follows; Berakhot 33a:11, 33a:29 the mention and the
request INDISPENSABLE) with THE DATES EVERY ONE FROM A ROW (the mention from the feast's last day to Passover — 2a:1-3; the request from the third or the seventh
of Marcheshvan, the seventh the halakha (the ruling) — 10a:11-12; the diaspora sixty days — 10a:12, 10a:15; the early rain in Marcheshvan, the late in Nisan —
6a:5, 6a:7; the fasts from the seventeenth and from Kislev's New Moon — 10a:16): rain_dates' VALUES; THE DECREE FIXED AT THE HEAD OF THE YEAR, THE DISTRIBUTION
FREE (Rosh Hashanah 17b:11-13 — "IN ITS SEASON" (11:14) THE FREE VARIABLE AFTER THE DECREE; 8a:16, 16b:12 the year judged at its head) — rain_in_its_season's
value made precise; THE SHUTTING'S VALUE (Ta'anit 3b:6 — the clouds and the winds, not rain alone), THRESHOLD (6b:8 — the barrel's mud) AND CAUSES (7b:5-8a:8 —
the sentence of destruction from 11:17, the tithes, slander, the impudent, the neglect of Torah, robbery, no whisperers of prayer; the shutting verb the wombs',
8a:18, 8b:1-3 — the Sifrei 306:6 at its Bavli seat; Solomon's dedication the run's receipt, 7b:4) — heavens_shut_for_turning's value and the cause a PARAMETER
with many arms; THE LAND WATERED BY HEAVEN, FIRST (Ta'anit 10a:2-3 — the Sifrei 37-40's baraita at its Bavli seat; THE SOURCE OF RAIN A DISPUTE, 9b:10-11 — 11:11
R. Yehoshua's verse; Bava Batra 19a:18; Shabbat 85a:3); THE CATTLE BEFORE THE MAN (Berakhot 40a:1, Gittin 62a:16 — a rule from 11:15's clause order); THE
PARAGRAPH'S DUTIES GRADED BY THE CLASS RULE (Mishnah Kiddushin 1:7; Kiddushin 34a:2, 34a:8; Yoma 11b:8; Bava Batra 21a:2 — "you shall teach them" read "you
yourselves"; Shabbat 32b:4 — the adjacency's reach, E28); THE CEREMONY — ITS PLACE THREE WAYS (Sotah 33b:4-10 — Shechem / two mounds by the Jordan / A ROUTE,
NOT A PLACE; 33b:6 the Samaritans' "Shechem" conceded and refuted), ITS FORM (32a:11-13; 37a:7-11; Tosefta Sotah 8:7 — FORTY-EIGHT COVENANTS), ITS TONGUE
(32a:6-7, 33a:13-14 — "voice" / "voice" with Exodus 19:19), ITS DAY THE CROSSING'S (Tosefta 8:1), the dispossession the crossing's condition (Tosefta 8:3);
THE RECEIPT'S POINTER TAUGHT A SECOND TIME (Tosefta Sotah 8:6 — 11:25's "no man shall stand" joined to Exodus 23:27 as the Sifrei 52:4 did; Pesachim 8b:7-9 the
pilgrimage's guard); THE DWELLING WEIGHED AND ITS COUNTER-ARM (Ketubot 110b:7, 110b:23-24 — outside the Land as idolatry, 11:16's phrase; 111a:1-8 the exile's
decree and the oaths; 111a:16-21 the dead outside not rising against Isaiah 26:19); STUDY GREATER FOR IT LEADS TO DEED (Kiddushin 40b:8 — the Sifrei 41:12 at
its Bavli seat); THE SHEMA'S LANGUAGE AND ORDER (Sotah 32a:5, 32b:19-33a:4). WHAT THE DESIGN DID NOT PREDICT (carried to RUN B as DATA rows or values): the
shutting's value and threshold; "in its season" the free variable after the decree; the cattle-before-the-man rule; the pointer's second teacher; the place a
THREE-arm parameter; the ceremony's day, tongue and covenant count; the dispossession as the crossing's condition; the Samaritan variant conceded; the rain's
source a dispute; the causes a parameter; the export's empty row Sotah 32a:4; the duplicate address. THE MIDDOT (checked in MIDDOT.md before typing): I1 at
Berakhot 14a:3, 33a:1, 33a:33, Rosh Hashanah 16b:11, Pesachim 8b:8, Sukkah 52a:1; I2 at Kiddushin 36a:9, Rosh Hashanah 8b:6, 9b:11 (7a:18 REFUSED for the months'
count), Ta'anit 2a:9, Sotah 32a:7, 32a:8, 32a:10, 33a:12, 33a:13, 33a:14, 33b:1, 33b:5, 33b:6, Ketubot 111a:9, 111a:19 — and 32b:8's guard (the bare "say"
learns only from the bare "say") and 33b:2's rule (THE ANALOGY NEEDS A TEACHER — the link review law's own sentence); E26 at Ta'anit 10a:3, Kiddushin 40b:6,
Rosh Hashanah 17b:18; E28 at Shabbat 32b:4; the do-not-read readings (Bava Batra 21a:2; Rosh Hashanah 16b:3; Berakhot 14a:11, 14a:18; Ta'anit 7b:9; Sotah 37a:1;
Sukkah 52a:8) and the juxtapositions (Ta'anit 2a:11; Kiddushin 34a:8 refused) NAMED, no code. THE INSTRUMENTS (the scratchpad, copied to the forms folder by
copy_ch11_docket_forms.py): ch11_docket_common.py and ch11_docket_rows.py (8b's by sed), ch11_docket_uncred.py (the chunk files), ch11_credit_survey.py (the
sixty-six ledgers' forms), ch11_credit_carry.py and ch11_credited_rows.py (the carry, generated), ch11_docket_A/B/C.py (the parts — SPEC = CREDITED_SPEC + OWN),
ch11_docket_hdr.py and ch11_docket_crowns.py (the header and the finds), derive_ch11_docket_writer.py (8b's writer by asserted line substitutions — the duplicate
address taken once, the LAW-by-cell and whole-row counts over this docket's own notes) and write_ch11_docket.py, ch11_docket_write.out, write_ch11_docket_records.py.
THE LESSONS: a credited row is CARRIED with its ledger's own verdict line, by regex on the ledger's form — read whole where the form carries no verdict; a carried
note names ITS OWN docket's cells and marks — the counts over this docket's own notes only; an address can stand twice in a dump (a link row inside a chapter
read whole) — taken once, computed; a gloss on a carried word is display, inserted at the carry. COMPILE_DEBT's sitting-9 box (n) is marked PAID with the box at
RUN B. RUN B next on the owner's word, after a compaction: the probes to FAIL (Q28-Q30; the debit-count literals 9 → 10), the types with the docket's names and
values (rain_dates from 2a:1-3, 6a:5-7, 10a:11-16; gerizim_ebal_place three arms; heavens_shut_for_turning's value 'the clouds and the winds withheld'), the
callees' facts, the runner cold_run_blessing_and_curse.py, the recorder with the cache off, the stitcher, the literals DC1-DC9, the tape, the chain, the records.
'''
STATE = f'''
#199 ADDENDUM 1 (2026-09-20, at the close of THE DOCKET of THE DEUTERONOMY WALK sitting 9b — its own run, on the owner's "Go" after the compaction — A CLEAN COMPACTION POINT): THE STATE: the docket logic/oral_triage/deu_11_ekev_reeh_exam_2026-09-20.md WRITTEN — {NR} rows (link {NL} in {NWORKS} works, topic {NT}; {vd(VD)}; credited {NC}: {NCAR} CARRIED with their ledgers' own verdict lines by ch11_credit_carry.py, {NUNR} read whole here; {NRH} rows read whole in this run in ten chunk files; Tosefta Sotah 8:6 twice in the dump, taken once), coverage computed (missing 0, extra 0), lint 0; its crowns in the file's finds section and the map's "THE DOCKET — AS RUN" paragraph — THE YOKE OF THE COMMANDMENTS NAMED BY THE ANSWER SHEET (Berakhot 14b:11; the paragraph TEACH AND PERFORM, 14b:14), THE PRAYER FROM 11:13'S OWN CLAUSE AND THE RAIN ATTACHED (Ta'anit 2a:11) with rain_dates' VALUES every one from a row (2a:1-3, 6a:5-7, 10a:11-16), "IN ITS SEASON" THE FREE VARIABLE AFTER THE DECREE (Rosh Hashanah 17b:11-13), THE SHUTTING'S VALUE (the clouds and the winds — Ta'anit 3b:6), THRESHOLD (6b:8) AND CAUSES (7b:5-8a:8), THE LAND WATERED FIRST (10a:2-3) and the source of rain a dispute (9b:10-11), THE CATTLE BEFORE THE MAN (Berakhot 40a:1), the duties by the class rule (Mishnah Kiddushin 1:7; Kiddushin 34a:2-8), THE CEREMONY'S PLACE THREE WAYS (Sotah 33b:4-10 — Shechem / the Jordan's mounds / a route), its form, tongue, day and forty-eight covenants (Tosefta Sotah 8), THE RECEIPT'S POINTER TAUGHT A SECOND TIME (Tosefta Sotah 8:6 with Exodus 23:27), THE DWELLING WEIGHED (Ketubot 110b:7, 110b:23) with its counter-arm (111a:1-8), STUDY GREATER (Kiddushin 40b:8); MIDDOT's docket entry (I1, I2, E26, E28 checked; the do-not-read readings and the juxtapositions named, no code), MISHNAH_TOPICS' eight rows, RESUME, the recovery page, the memory, the commit message file started (<scratch>/commit_msg_ch11.txt — the headline at RUN B). NOT COMMITTED (since 2f4ec5b): RUN A's records and this docket; a985fbc the last push. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (compact before RUN B). NEXT ON THE RULING: RUN B — patch_probes_ch11.py (Q28-Q30 to FAIL, BEFORE the types; the open-debit literals 9 → 10 retyped from the print — DB7 and 8b's retyped older ones, the grep decides), add_types_ch11.py (the two kinds and the case kind; the five effects with the docket's values — rain_in_its_season 'the rain of your land in its season, the early and the late — the decree fixed at the year's head, its season free', heavens_shut_for_turning 'the clouds and the winds withheld — the barrel's mud the threshold', yoke_of_the_commandments_accepted, blessing_and_curse_set, gerizim_ebal_ceremony_owed 'the holy tongue, the loud voice, the Amen, forty-eight covenants; the day the crossing's'; law_blessing_and_curse given_at Deut 11:1 boot; the span and the fifteen CALL edges predicted, the one AS_WHEN pointer; rain_dates and gerizim_ebal_place (three arms) in calendar_parameters.yaml), ch11_callees.py (every CALL's facts printed), the runner cold_run_blessing_and_curse.py the 66th in parts with ch11_fastcheck.py and ch11_cases_gen.py (six cells; the readback rows; the two own-day lines; the docket's crowns as exam rows), seq_record_ch11.py (INK_CACHE=0) and seq_stitch_ch11.py, patch_seq_literals_ch11.py (DC1-DC9), the tape to 10/10 with THE REST, checkpoint_check.py --all, gates_chain.sh, write_ch11b_records.py from the sheet (COMPILE_DEBT's sitting-9 box PAID and the 9b box), copy_ch11b_forms.py, the commit message. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 9b … THE DESIGN" and its "THE DOCKET — AS RUN" paragraph (the newest section), MEMORY.md.
'''
RESUME = f'''# ⚠ THE DEUTERONOMY WALK sitting 9b — THE DOCKET DONE (2026-09-20; logic/oral_triage/deu_11_ekev_reeh_exam_2026-09-20.md — {NR} rows, {NCAR} carried with
# their ledgers' verdicts, {NRH} read whole here; {vd(VD)}): the yoke of the commandments named by the answer sheet (Berakhot 14b:11), the prayer from 11:13's
# clause with the rain attached (Ta'anit 2a:11) and the rain's dates from the rows, "in its season" free after the decree (Rosh Hashanah 17b:11-13), the shutting
# = the clouds and the winds (Ta'anit 3b:6), the ceremony's place three ways (Sotah 33b:4-10), the receipt's pointer taught twice (Tosefta Sotah 8:6). NEXT: RUN B
# after a compaction (the probes to FAIL, the types, the runner, the tape, the chain, the records).
'''
MIDDOT = f'''
### THE DEUTERONOMY WALK 9b — THE DOCKET OF CHAPTER 11 (2026-09-20; logic/oral_triage/deu_11_ekev_reeh_exam_2026-09-20.md, {NR} rows — {NCAR} carried, {NRH} read whole here)
Every code checked in this file's tables before it was typed. I1 (qal wa-chomer, the a-fortiori): Berakhot 14a:3 — the Shema interrupted for a greeting, so hallel
(the praise psalms) all the more (refused for the miracle's publicity); 33a:1 — the pious man before the King of kings; 33a:33 — havdala (the distinction blessing)
over the cup from the prayer's; Rosh Hashanah 16b:11 — the priests' defilement to the festival's purification; Pesachim 8b:8 — the animals guarded on the
pilgrimage, the men all the more; Sukkah 52a:1 — the eulogy's separation to the water-drawing's. I2 (gezerah shavah, the verbal analogy): Kiddushin 36a:9 —
"between your eyes" (Deuteronomy 14:1) / "between your eyes" (11:18): women exempt from the baldness bar as from tefillin (Isi); Rosh Hashanah 8b:6 and 9b:11 —
"year" (Leviticus 25:4; 19:24) / "year" (11:12 "from the beginning of the year"): the sabbatical and the planting counted from Tishri; 7a:18 — the same analogy
REFUSED for the months' count (a "year" with "months" learns only from a "year" with "months"); Ta'anit 2a:9 — "beyond comprehension" (Job 5:9) / (Isaiah 40:28):
the rain's might the creation's; Sotah 32a:7, 32a:8, 33a:13 — "speak and say" (26:5; 25:9) / "the Levites shall speak and say" (27:14): the first fruits and
halitza (the shoe-loosing) in the holy tongue; 33b:1 — the analogy reversed for R. Yehuda (the Levites' tongue from halitza's); 33a:14 — "a loud voice" (27:14) /
"by a voice" (Exodus 19:19): the Levites' own Hebrew; 32a:10, 33b:5, 33b:6 — "the terebinths of Moreh" (11:30) / (Genesis 12:6): Shechem — the Samaritans'
forged "Shechem" conceded and refuted by the analogy they do not use; 33a:12 — "sins" (Leviticus 5:21) / "sins" (5:1): the deposit oath in any language; Ketubot
111a:9 — "an altar of earth" (Exodus 20:21) / "the land of His people" (32:43): burial in the Land as under the altar; 111a:19 — "to the people upon it" (Isaiah
42:5) / "with the donkey" (Genesis 22:5). THE ANALOGY'S GUARDS AT TWO SEATS: Sotah 32b:8 — the bare "say" learns only from the bare "say", not from "speak and
say"; Sotah 33b:2 — "he learned 'speak' / 'speak' from his teacher, and did not learn 'voice' / 'voice' from his teacher": THE ANALOGY NEEDS A TEACHER — the
link review law's own sentence on the shelf (Pesachim 66a's rule at a second seat). E26 (mashal, the parable): Ta'anit 10a:3 — the cheese-kneader who takes the
food and leaves the refuse (the Land drinks first); Kiddushin 40b:6-7 — the tree in a pure place with branches over an impure (the righteous), and its mirror;
Rosh Hashanah 17b:18 — the king's oath and the friend's debt (between man and God, between man and man). E28 (from-the-preceding, the adjacency reading):
Shabbat 32b:4 — "that your days be multiplied" (11:21) read with the mezuzah's verse before it alone, or with the teaching's verse before that too: children
die for the one neglect or the other — THE ADJACENCY'S REACH THE DISPUTE. THE READINGS "DO NOT READ" (al tikrei) — NO CODE IN THIS FILE, named by their rows:
Bava Batra 21a:2 ("them" / "you yourselves" — the father teaches, 11:19), Rosh Hashanah 16b:3 ("from the beginning" / "poverty" — the year's arc, 11:12),
Berakhot 14a:11 ("how" / "an altar") and 14a:18 ("satisfied" / "seven"), Ta'anit 7b:9 ("is changed" / "is hated"), Sotah 37a:1 ("ruling them" / "descending to
the sea"), Sukkah 52a:8 ("reward" / "reconcile"). THE JUXTAPOSITIONS (the likening by adjacency) — no code, named: Ta'anit 2a:11 (11:13's service of the heart =
prayer, 11:14's rain next to it — the request for rain in the prayer); Kiddushin 34a:8 (the mezuzah beside study — REFUSED by the reward clause 11:21);
Shabbat 32b:4 (E28 above). THE DISPUTES AS PARAMETERS (the machine's data channel): Mishnah Ta'anit 1:1-3 through 2a:1-3 and 10a:11-12 (the mention from the
first / the last day of the feast; the request from the third / the seventh of Marcheshvan; the diaspora's sixty days); Ta'anit 9b:10-11, 9b:14-16, 10a:4-7 (the
source of rain — the ocean sweetened in the clouds / the upper waters, 11:11 R. Yehoshua's); Ta'anit 3b:6 (the shutting — the clouds and the winds); 7b:5-8a:6
(the shutting's cause — many arms); Sotah 33b:4-10 (the ceremony's place — Shechem / two mounds by the Jordan / a route); Sotah 37a:7-9 and Tosefta Sotah 8:7 (the
Levites' placement — the elders below / the fit below / all below); Tosefta Sotah 8:5 (the writing on the stones / on the plaster); Sotah 32b:19 (the Shema as
written / in any language); Berakhot 33a:24 (havdala's seat); Ketubot 111a:1-6 (the ascent — the exile's decree and the oaths / the individual's leave); 111a:16-21
(the dead outside the Land — not rising / rising by tunnels); Rosh Hashanah 17a:12-13 (how He tilts the scale; the first sin overlooked).
'''
MEMO = f'''
THE DOCKET DONE (2026-09-20, "Go" after the compaction at #199): deu_11_ekev_reeh_exam_2026-09-20.md — {NR} rows ({vd(VD)}; credited {NC}: {NCAR} CARRIED with
their ledgers' own verdict lines by ch11_credit_carry.py — THE NEW FORM: a credited row listed with its ledger, its verdict parsed from the ledger's line; {NUNR}
read whole here where the form carried none; {NRH} rows read whole in this run in ten chunk files; Tosefta Sotah 8:6 twice in the dump, taken once); the crowns:
the yoke of the commandments named by the answer sheet (Berakhot 14b:11 — TEACH AND PERFORM, 14b:14), the prayer from 11:13's clause with the rain attached
(Ta'anit 2a:11) and rain_dates' values from the rows (2a:1-3, 6a:5-7, 10a:11-16), "IN ITS SEASON" THE FREE VARIABLE AFTER THE DECREE (Rosh Hashanah 17b:11-13),
the shutting = the clouds and the winds (Ta'anit 3b:6; the barrel's mud the threshold, 6b:8; the causes a parameter, 7b:5-8a:8), the Land watered first (10a:2-3)
and the source of rain a dispute (9b:10-11), the cattle before the man (Berakhot 40a:1), the ceremony's place THREE ways (Sotah 33b:4-10 — Shechem / the Jordan's
mounds / a route), its form, tongue, day and forty-eight covenants (Tosefta Sotah 8), the receipt's pointer taught a second time (Tosefta Sotah 8:6 with Exodus
23:27), the dwelling weighed (Ketubot 110b:23) with its counter-arm (111a:1-8). NEXT: RUN B after a compaction (the state doc's #199 addendum 1 the newest).
'''
MSG0 = f'''CHAPTER 11 COMPILED AND ON THE TAPE — (THE HEADLINE WRITTEN AT RUN B). THE DOCKET, ITS OWN RUN (2026-09-20, on the owner's "Go" after the compaction at #199): logic/oral_triage/deu_11_ekev_reeh_exam_2026-09-20.md — {NR} rows ({vd(VD)}; link {NL} in {NWORKS} works, topic {NT}: the fifteen folio ranges whole, the eight Mishnah rows, Tosefta Sotah 8 and Tosefta Sheviit 4 whole; credited {NC} — {NCAR} CARRIED WITH THEIR LEDGERS' OWN VERDICT LINES, the new form of the credit (a credited row listed with its ledger, its verdict parsed from the ledger's line — ch11_credit_carry.py), {NUNR} read whole here where the ledger's form carried no verdict; {NRH} rows read whole in this run), coverage computed, lint 0; its crowns: THE YOKE OF THE COMMANDMENTS NAMED BY THE ANSWER SHEET (Berakhot 14b:11 — the second paragraph TEACH AND PERFORM), THE PRAYER FROM 11:13'S OWN CLAUSE AND THE RAIN ATTACHED TO IT (Ta'anit 2a:11) with the rain's dates every one from a row, "IN ITS SEASON" THE FREE VARIABLE AFTER THE DECREE (Rosh Hashanah 17b:11-13), THE SHUTTING'S VALUE — the clouds and the winds (Ta'anit 3b:6), its threshold (6b:8) and its causes (7b:5-8a:8), the Land watered first (10a:2-3) and the source of rain a dispute (9b:10-11), the cattle before the man (Berakhot 40a:1), the paragraph's duties by the class rule (Mishnah Kiddushin 1:7), THE CEREMONY'S PLACE THREE WAYS (Sotah 33b:4-10 — Shechem, the Jordan's mounds, a route), its form, tongue, day and forty-eight covenants (Tosefta Sotah 8), THE RECEIPT'S POINTER TAUGHT A SECOND TIME (Tosefta Sotah 8:6 with Exodus 23:27, the Sifrei 52:4 the first), the dwelling weighed and its counter-arm (Ketubot 110b:7-111a:21), study greater for it leads to deed (Kiddushin 40b:8); MIDDOT's docket entry (I1, I2, E26, E28 checked before typed; the analogy's two guards), MISHNAH_TOPICS' eight rows, the state doc's #199 addendum 1, the recovery page, RESUME, the memory.
'''
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; RES = f'{ROOT}/World/RESUME.md'; MID = f'{ROOT}/logic/MIDDOT.md'
MT = f'{ROOT}/logic/MISHNAH_TOPICS.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'; MSG = f'{SCR}/commit_msg_ch11.txt'
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-20, 9b run A done; the state doc #199 the newest)", "## 2. WHERE IT STANDS (2026-09-20, 9b docket done; the state doc #199 addendum 1 the newest)"),
             ("- 9b RUN A DONE (the design in the map; #199): THE DOCKET its own run NEXT (1,072 rows, 622 credited), then RUN B. The push on his word.",
              f"- 9b A + DOCKET DONE ({NR:,} rows: {NRH} whole here, {NCAR} carried; #199 add. 1). NEXT: RUN B after a compaction. The push on his word.")]
IDX_EDIT = ("9b A done; docket next", "9b A+docket done; B next")
MT_EDITS = [("**1. Mishnah, Blessings**", " — 2:2 CARRIED 2026-09-20 (THE DEUTERONOMY WALK 9b's docket: the yoke of the kingdom before the yoke of the commandments — Berakhot 14b:11 the seat); 5:2 READ WHOLE through Berakhot 33a:11 (the mention of rain in the resurrection blessing, the request in the years' — both indispensable, 33a:29)."),
            ("**5. Mishnah, Seventh Year**", " — 6:1 CARRIED 2026-09-20 (9b's docket; the three lands); Tosefta Sheviit 4 READ WHOLE (4:5 the baraita of the borders' towns — the returners' line by its towns, 11:24's extents for the land laws)."),
            ("**19. Mishnah, New Year**", " — 1:2 CARRIED 2026-09-20 (9b's docket: the four seasons' judgment; Rosh Hashanah 16a-17b read — the three books, 16b:12; the rain's decree fixed at the head of the year and its season free, 17b:11-13)."),
            ("**20. Mishnah, Fasts**", " — 1:1-1:5 READ WHOLE 2026-09-20 through the Gemara's citations (9b's docket; the export lacks Mishnah Ta'anit): the mention from the feast's first / last day (2a:1), the request near the season (2a:3), from the third / the seventh of Marcheshvan (10a:11), the fasts from the seventeenth and from Kislev's New Moon (10a:16) — rain_dates' rows."),
            ("**25. Mishnah, Marriage Contracts**", " — 13:11 READ WHOLE 2026-09-20 through Ketubot 110b:7 (9b's docket: all may force ascent to the Land, none removal — 11:31's 'dwell in it' the exam's row; 110b:23 the dwelling weighed; 111a:1-8 the counter-arm)."),
            ("**28. Mishnah, Suspected Wife**", " — 7:1 READ WHOLE 2026-09-20 through Sotah 32a:5 (9b's docket: the Shema in any language) and 7:2-7:5 CARRIED (the holy tongue; the ceremony's form); Tosefta Sotah 8 READ WHOLE (8:1 the day the crossing's, 8:3 the dispossession the crossing's condition, 8:5 the writing's place, 8:6 the receipt's pointer to Exodus 23:27, 8:7 forty-eight covenants)."),
            ("**30. Mishnah, Betrothal**", " — 1:7 READ WHOLE 2026-09-20 (9b's docket: the class rule behind the paragraph's duties — tefillin time-bound, mezuzah not, study the son's); 1:9 CARRIED; 1:10 READ WHOLE through Kiddushin 40b:5 (Bible, Mishnah and conduct; 40b:8 study greater for it leads to deed)."),
            ("**42. Mishnah, Grain Offerings**", " — 3:7 CARRIED 2026-09-20 (9b's docket: the four compartments, the mezuzah's two passages — the frontlets' spellings the open row).")]
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:50]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
for a, _ in MT_EDITS:
    if R(MT).count(a) != 1: print('MT ANCHOR', R(MT).count(a), a); ok = False
assert 'THE DOCKET — AS RUN (2026-09-20, on "Go" after the compaction at #199' not in R(MAP) and '#199 ADDENDUM 1' not in R(STATEDOC) and 'COMPACTION POINT #199' in R(STATEDOC)
assert not os.path.exists(MSG), MSG
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT)
mt = R(MT)
for a, b in MT_EDITS:
    lines = mt.split('\n'); i = next(i for i, l in enumerate(lines) if l.startswith(a)); lines[i] = lines[i].rstrip() + b; mt = '\n'.join(lines)
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the docket %d bytes, %d rows; works %d' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), NB, NR, NWORKS))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
W(MAP, R(MAP).rstrip('\n') + '\n' + MAPP); W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE); W(REC, rec); W(RES, RESUME + R(RES))
W(MID, R(MID).rstrip('\n') + '\n' + MIDDOT); W(MT, mt); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx); W(MSG, MSG0)
print('written: the map, the state doc, the recovery page, RESUME, MIDDOT, MISHNAH_TOPICS, the memory note, the index, the commit message file (new)')
for p in (MAP, STATEDOC, REC, RES, MID, MT, WALK, IDX):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
