#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b — the docket run's close (2026-09-20): the map's "THE DOCKET — AS RUN" paragraph, the state doc's #197 addendum 8, the recovery
# page's section-2 lines, RESUME's head, MIDDOT's docket entry (every code checked in MIDDOT.md before it was typed — I1, I2, E1, E4, E26, E30; the
# do-not-read readings and the juxtapositions NAMED, no code), MISHNAH_TOPICS' three rows, the memory, the commit message's paragraph. EVERY COUNT PARSED
# from the writer's print (ch10_docket_write.out), never typed; every text built whole before its file is opened; the size caps asserted. 7b's form
# (write_ch9_docket_records.py). Run from the repo root.
import os, re, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)
P = R(f'{SCR}/ch10_docket_write.out')
m = re.search(r'WROTE (\S+) (\d+) bytes', P); OUTP, NB = m.group(1), int(m.group(2))
m = re.search(r'rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \)', P); NR, NL, NT, NC, NCL, NCT = map(int, m.groups())
m = re.search(r"verdicts (\{.*?\}) link (\{.*?\}) topic (\{.*?\})", P); VD, VL, VT = (eval(x) for x in m.groups())
LAWC = eval(re.search(r'LAW by cell (\{.*?\})', P).group(1)); NOUT = eval(re.search(r'OUTSIDE by work (\{.*?\})', P).group(1))
UNC = eval(re.search(r'UNCITED (\[.*?\])', P).group(1)); RANGES = eval(re.search(r'ranges (\[.*\])', P).group(1)); NMISH = int(re.search(r'mishnah\+midrash rows (\d+)', P).group(1))
NWORKS = len(set(re.findall(r'^- ([A-Z][A-Za-z ]+?) \d+[ab]:\d+ \[LINK', R(OUTP), re.M)))
vd = lambda d: ', '.join(f'{k} {d.get(k, 0)}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'))
MAPP = f'''
THE DOCKET — AS RUN (2026-09-20, on "The docket go" in the same window as RUN A — the owner's word after the recommendation to compact; ITS OWN RUN under
the two-run rule's docket clause): logic/oral_triage/deu_10_ekev_exam_2026-09-20.md — {NR} rows (link {NL} in {NWORKS} works, topic {NT}: Mishnah Shekalim 6:1-2,
Mishnah Sotah 7:6, Mishnah Berakhot 9:5; {"; ".join(f"{n} {s}" for n, s, l in RANGES)}; Seder Olam Rabbah 6, 9 and 10 WHOLE — the export's chapters under its
EMPTY key, 7b's "unreachable" the reader's index; Tosefta Sotah 7 whole, fifteen rows); the verdicts {vd(VD)} (the link rows {vd(VL)}; the topic rows {vd(VT)});
LAW by cell {LAWC}; credited {NC}; EVERY ROW READ WHOLE FROM THE START (the parts A-C on 7b's instruments, corrections 0, coverage computed: missing 0,
extra 0); the verses no row cites {UNC}. THE CROWNS (the docket's finds section): THE SECOND ASCENT'S DATE MATCHES SEDER OLAM 6:2 — down the 28th of Av and
carved, UP THE 29TH OF AV, down the 10th of Tishri: the machine's (1, 5, 29) by subtraction is the shelf's own date, 7b's OPEN row on the clock CLOSED (the
"first of Elul" not this shelf's text; 7b's owed item (iii) PAID; DB4 asserts it); THE ARK ONE IN THE BAVLI'S OWN WORDS ("the ark that Moses fashioned" with
Exodus 25:10's cubits — Bava Batra 14a:8) and TWO IN THE TOSEFTA'S (Sotah 7:9 — the war ark with the scroll, the camp ark with the fragments: the parameter's
second arm, a DISPUTE row and the exam's row; decision (1) stands); THE FRAGMENTS' THREE DERIVATIONS (10:2's "them"; 2 Samuel 6:2's doubled Name; 1 Kings
8:9's double restriction, E4) and WHAT ELSE THE ARK HELD (the scroll inside for R. Meir, beside for R. Yehuda — the effect's value's second parameter); the
Levites' separation read for the blessing — standing, the lifted hands, not itself "service" (Sotah 38a:5-8, Arakhin 11a:10), "which time" asked by no row;
THE FEAR OF HEAVEN THE ONE FREE VARIABLE (Berakhot 33b:23 — the effect fear_of_heaven_asked named by the shelf; "a small thing" for Moses, E26);
THE HEART'S FORESKIN GUARDED BY GRAMMAR (Shabbat 108a:7 — the verbal analogy refuses the construct form: not the circumcision law's object) and NAMED THE
EVIL INCLINATION (Sukkah 52a:7 — the effect's value); the attributes three and no more (Yoma 69b:13-16, Berakhot 33b:22) and the face thrice reconciled;
the bribe even to judge truly and by words (Ketubot 105a:10, 105b:8-15 — the exam's six judges); the stranger's thirty-six warnings and the reason clause's
rule (Bava Metzia 59b:14-15) with the convert's intake (Yevamot 47a-b); THE CLEAVING'S VALUE THE SCHOLARS (Ketubot 111b:7) and THE POSITIVE FORM of 10:20's
four clauses (Temurah 4a:2; Sanhedrin 56a:11 — STATUS confirmed, no lashes); "walk after Him" = bury the dead (Sotah 14a:4, beside 10:6's passive burial);
Jochebed the seventieth (Bava Batra 123b:1); the retreat of seven stations read whole (Seder Olam 9:2). WHAT THE DESIGN DID NOT PREDICT carried to RUN B: the
date's MATCH (DB4 retyped from OPEN to MATCH); the two arks' dispute row; the ark's contents' two arms; the grammar guard; the inclination's name; the burial
among the attributes; the positive form; the intake as the stranger line's exam; the editor's "first of Tammuz" variant a DATA note. THE MIDDOT (checked in
MIDDOT.md before typing): I1 at Ketubot 105a:16; I2 at Shabbat 108a:7 (refused for the construct), Menachot 43b:9, Shevuot 35b:23; E1 at Pesachim 22b:11,
Bava Batra 123a:21; E4 at Bava Batra 14a:10; E26 at Berakhot 33b:22, 33b:25, Megillah 25a:8, 25a:10, Menachot 99b:7, Niddah 70b:11, Bava Batra 123a:12; E30
at Ketubot 105b:5; the do-not-read readings (Menachot 43b:15; Rosh Hashanah 3a:2; Ta'anit 9a:11) and the juxtapositions (Sotah 38a:8; Megillah 31a:13) NAMED —
no code on file. RUN B next on the owner's word, after a compaction: the probes to FAIL (Q25-Q27), the types with the docket's names and values, the callees'
facts, the runner cold_run_second_tablets.py, the recorder with the cache off, the stitcher, the literals DB1-DB9, the tape, the chain, the records.
'''
STATE = f'''
#197 ADDENDUM 8 (2026-09-20, at the close of THE DOCKET of THE DEUTERONOMY WALK sitting 8b — its own run, in RUN A's window on the owner's "The docket go" — A CLEAN COMPACTION POINT): THE STATE: the docket logic/oral_triage/deu_10_ekev_exam_2026-09-20.md WRITTEN — {NR} rows (link {NL}, topic {NT}; {vd(VD)}; credited {NC}), EVERY ROW READ WHOLE FROM THE START on 7b's instruments (ch10_docket_A/B/C.py, ch10_docket_common.py, ch10_docket_rows.py, write_ch10_docket.py in the scratchpad and copied to the forms folder; the six row prints), coverage computed (missing 0, extra 0), lint 0; its crowns in the file's finds section and the map's "THE DOCKET — AS RUN" paragraph — THE SECOND ASCENT'S DATE MATCHES SEDER OLAM RABBAH 6:2 (the 29th of Av — the machine's (1, 5, 29) the shelf's own; 7b's OPEN row on the clock CLOSED, its owed item (iii) PAID), the ark ONE in the Bavli's words and TWO in the Tosefta's (a DISPUTE row), the fragments' three derivations and the ark's contents' two arms (the effect's value), the fear of Heaven the one free variable (the effect's name from Berakhot 33b:23), the heart's foreskin guarded by grammar and named the evil inclination, the cleaving's value the scholars, the four clauses' positive form (STATUS confirmed), the bribe's six judges and the convert's intake the exam's persons; MIDDOT's docket entry (I1, I2, E1, E4, E26, E30 checked; the do-not-read readings and the juxtapositions named, no code), MISHNAH_TOPICS' three rows, RESUME, the recovery page, the memory, the commit message's paragraph. NOT COMMITTED (since a985fbc): THE VERIFIED-IMPORT CACHE, 7b, 8, 8b's design and this docket — ONE message at <scratch>/commit_msg_ch9b.txt covers all (the owner's word: "commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT (the window past 600k: compact before RUN B). NEXT ON THE RULING: RUN B — patch_probes_ch10.py (Q25-Q27 to FAIL, BEFORE the types; the stale 'markers 169' literals — the stitcher's docstring, DA9, Q23 — retyped from the print), add_types_ch10.py (the six kinds and the case kind; the five effects with the docket's values — fragments_in_the_ark 'the tablets and the fragments; the scroll inside or beside', heart_circumcision_commanded 'the evil inclination', cleaving_commanded 'the scholars'; law_second_tablets given_at Deut 10:1 boot; the span and the eighteen CALL edges predicted, the two AS_WHEN pointers), ch10_callees.py (every CALL's facts printed — the call forms, the first verses), the runner cold_run_second_tablets.py the 65th in parts with ch10_fastcheck.py and ch10_cases_gen.py (six cells; the readback rows; the two retrograde lines and the four own-day lines; DB4 the date MATCH), seq_record_ch10.py (INK_CACHE=0) and seq_stitch_ch10.py (the placement print read), patch_seq_literals_ch10.py (DB1-DB9), the tape to 10/10 with THE REST, checkpoint_check.py --all, gates_chain.sh, write_ch10b_records.py from the sheet (COMPILE_DEBT's sitting-8 box PAID and the 8b box; 7b's owed item (iii) marked paid), copy_ch10b_forms.py, the commit message. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 8b … THE DESIGN" and its "THE DOCKET — AS RUN" paragraph (the newest section), MEMORY.md.
'''
RESUME = f'''# ⚠ THE DEUTERONOMY WALK sitting 8b — THE DOCKET DONE (2026-09-20; logic/oral_triage/deu_10_ekev_exam_2026-09-20.md — {NR} rows whole, {vd(VD)}): THE SECOND
# ASCENT'S DATE MATCHES SEDER OLAM 6:2 (the 29th of Av — 7b's open row closed), the ark one in the Bavli and two in the Tosefta (a dispute row), the fear of
# Heaven the one free variable (Berakhot 33b:23), the heart's foreskin guarded by grammar (Shabbat 108a:7), the cleaving = the scholars (Ketubot 111b:7), the
# four clauses positive (Temurah 4a:2). NEXT: RUN B after a compaction (the probes to FAIL, the types, the runner, the tape, the chain, the records).
'''
MIDDOT = f'''
### THE DEUTERONOMY WALK 8b — THE DOCKET OF CHAPTER 10 (2026-09-20; logic/oral_triage/deu_10_ekev_exam_2026-09-20.md, {NR} rows whole)
Every code checked in this file's tables before it was typed. I1 (qal wa-chomer, the a fortiori): Ketubot 105a:16 — "a bribe blinds the eyes of the wise", a
fortiori the fools; "perverts the words of the righteous", a fortiori the wicked (Deuteronomy 16:19). I2 (gezerah shavah, the verbal analogy): Shabbat 108a:7
— orlato / orlato (Leviticus 12:3 the circumcision, 19:23 the orlah tree): the complete form alone, the construct orlat of Deuteronomy 10:16's "foreskin of
your heart" REFUSED — the analogy's own grammar rule; Menachot 43b:9 — oto / oto (Numbers 15:39 "look upon it"; Deuteronomy 6:13 "Him you shall serve") the
Presence; Shevuot 35b:23 — ala / ala (Leviticus 5:1; Numbers 5:21) the oath in the Name. E1 (ribui, the extension by et): Pesachim 22b:11 — Shimon
HaAmmassoni's every "et" and his withdrawal at "you shall fear ET the LORD your God" (10:20), R. Akiva's et = the Torah scholars; Bava Batra 123a:21 — "ET
his daughter Dinah" a twin (refuted by "ET Benjamin"). E4 (restriction after restriction, which extends): Bava Batra 14a:10 — "there was NOTHING in the ark
EXCEPT the two tablets" (1 Kings 8:9) includes the Torah scroll (R. Meir) or the fragments (R. Yehuda, 14a:15). E26 (mashal, the parable): Berakhot 33b:22
and Megillah 25a:8 — the king's gold dinars praised as silver; Berakhot 33b:25 and Megillah 25a:10 — the large vessel owned seems small; Menachot 99b:7 —
the sparrow entrusted to the slave; Niddah 70b:11 — the king's feast sent to those he loves; Bava Batra 123a:12 — the orphan raised in the house. E30
(notarikon, a word read as words): Ketubot 105b:5 — shochad, "bribe", read she-hu chad, "he is one" with the giver. THE READINGS "DO NOT READ" (al tikrei) —
NO CODE IN THIS FILE, named by their rows: Menachot 43b:15 (ma / me'a — a hundred blessings from 10:12's "what"), Rosh Hashanah 3a:2 and Ta'anit 9a:11
(vayiru / vayera'u — "they saw" / "they were seen", the clouds gone at Aaron's death). THE JUXTAPOSITIONS (hekkesh, a likening by adjacency) — no code,
named: Sotah 38a:8 (the blessing beside the service in 10:8; the sons beside Aaron in 18:5), Megillah 31a:13 (10:17's greatness beside 10:18's humility).
THE DISPUTES AS PARAMETERS (the machine's data channel): Bava Batra 14a:8-14b:5 (the cubit six / five; the scroll inside / beside; the silver columns);
Tosefta Sotah 7:9 against Bava Batra 14a:8 (two arks / one); Chagigah 12b:4 (two firmaments / seven); Yevamot 47a:1 (the convert's proof — in the land only /
everywhere), 47a:9-12 (the private convert's word — his children), 47b:16-19 (the emancipated slave's yoke; the captive); Bava Metzia 59b:14 (thirty-six /
forty-six warnings); Ketubot 105a:11-13 (bribe / salary / evident loss); Seder Olam 10:2's Aaron in Av against the editor's Tammuz variant.
'''
MEMO = f'''
THE DOCKET DONE (2026-09-20, "The docket go" in RUN A's window): deu_10_ekev_exam_2026-09-20.md — {NR} rows whole ({vd(VD)}; credited {NC}); the crowns:
THE SECOND ASCENT'S DATE MATCHES SEDER OLAM RABBAH 6:2 (up the 29th of Av, down the 10th of Tishri — the machine's (1, 5, 29) the shelf's own; 7b's OPEN
row on the clock CLOSED, "the first of Elul" not this shelf's text; Seder Olam reachable under the export's EMPTY key), the ark ONE in the Bavli ("the ark
that Moses fashioned", Bava Batra 14a:8) and TWO in the Tosefta (Sotah 7:9 — a DISPUTE row), the fragments' three derivations and the ark's contents' two
arms, the fear of Heaven the one free variable (Berakhot 33b:23 — fear_of_heaven_asked named), the heart's foreskin guarded by grammar (Shabbat 108a:7) and
named the evil inclination (Sukkah 52a:7), the cleaving = the scholars (Ketubot 111b:7), 10:20's four clauses POSITIVE (Temurah 4a:2 — STATUS, no lashes),
the bribe's six judges and the convert's intake the exam's persons, "walk after Him" = bury the dead (Sotah 14a:4). NEXT: RUN B after a compaction (the
window past 600k).
'''
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; RES = f'{ROOT}/World/RESUME.md'; MID = f'{ROOT}/logic/MIDDOT.md'
MT = f'{ROOT}/logic/MISHNAH_TOPICS.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'; MSG = f'{SCR}/commit_msg_ch9b.txt'
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-20, after 8b's RUN A; the state doc #197 addendum 7 the newest)", "## 2. WHERE IT STANDS (2026-09-20, after 8b's docket; the state doc #197 addendum 8 the newest)"),
             ("- Uncommitted since a985fbc: the cache, 7b, 8 and 8b's design; ONE message at <scratch>/commit_msg_ch9b.txt covers all.", "- Uncommitted since a985fbc: the cache, 7b, 8, 8b's design and docket; ONE message at <scratch>/commit_msg_ch9b.txt covers all."),
             ("- 8b RUN A DONE (the design in the map; the DB series). NEXT: the docket (its own run, 510 rows whole), then RUN B.",
              f"- 8b RUN A AND THE DOCKET DONE ({NR} rows whole; the second ascent's date MATCH — Seder Olam 6:2). NEXT: RUN B after a compaction.")]
IDX_EDIT = ("8b RUN A DONE (1-8 PUSHED a985fbc; the rest UNCOMMITTED); NEXT: the docket, then RUN B", "8b RUN A + DOCKET DONE (1-8 PUSHED a985fbc; the rest UNCOMMITTED); NEXT: RUN B")
MT_EDITS = [("**1. Mishnah, Blessings**", " — 9:5 REREAD WHOLE 2026-09-20 (THE DEUTERONOMY WALK 8b's docket: 'with all your might' beside 10:12's heart and soul without it; the Name in greeting; the seal from everlasting to everlasting)."),
            ("**15. Mishnah, Shekels**", " — 6:1-2 REREAD WHOLE 2026-09-20 (8b's docket: the thirteen prostrations and the fourteenth at the wood depository — the ark sequestered, the priest who died: the ark's run past the Torah, a DATA note)."),
            ("**28. Mishnah, Suspected Wife**", " — 7:6 REREAD WHOLE 2026-09-20 (8b's docket: the blessing's form — three blessings outside, one in the Temple; the Name; the hands above the head; naso.blessing by CALL for 10:8's third office; Tosefta Sotah 7 whole — 7:5 the blemished excluded, 7:9 R. Yehuda ben Lakish's two arks).")]
MSG_EDIT = ("NEXT on the owner's word: the docket its own run (510 rows, every row whole), then RUN B.",
            f"AND THE DOCKET, ITS OWN RUN (2026-09-20, on the owner's \"The docket go\" in the same window): logic/oral_triage/deu_10_ekev_exam_2026-09-20.md — {NR} rows ({vd(VD)}; link {NL} in {NWORKS} works, topic {NT}: the twenty-one folio ranges whole, the three Mishnah rows, Seder Olam Rabbah 6, 9 and 10 whole — reachable under the export's empty key — and Tosefta Sotah 7 whole; credited {NC}), EVERY ROW READ WHOLE FROM THE START, coverage computed; its crowns: THE SECOND ASCENT'S DATE MATCHES SEDER OLAM 6:2 (up the 29th of Av — the machine's (1, 5, 29) the shelf's own; 7b's open row on the clock closed), the ark one in the Bavli's words and two in the Tosefta's (a dispute row), the fragments' three derivations and the ark's contents' two arms (the effect's value), the fear of Heaven the one free variable (Berakhot 33b:23 — the effect's name), the heart's foreskin guarded by grammar (Shabbat 108a:7) and named the evil inclination (Sukkah 52a:7), the cleaving's value the scholars (Ketubot 111b:7), the four clauses' positive form (Temurah 4a:2 — STATUS, no lashes), the bribe's six judges and the convert's intake the exam's persons; MIDDOT's docket entry (I1, I2, E1, E4, E26, E30 checked before typed), MISHNAH_TOPICS' three rows, the state doc's #197 addendum 8, the recovery page, RESUME, the memory. NEXT on the owner's word: RUN B.")
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:50]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
if R(MSG).count(MSG_EDIT[0]) != 1: print('MSG ANCHOR', R(MSG).count(MSG_EDIT[0])); ok = False
for a, _ in MT_EDITS:
    if R(MT).count(a) != 1: print('MT ANCHOR', R(MT).count(a), a); ok = False
assert 'THE DOCKET — AS RUN (2026-09-20' not in R(MAP) and '#197 ADDENDUM 8' not in R(STATEDOC) and '#197 ADDENDUM 7' in R(STATEDOC)
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT); msg = R(MSG).replace(*MSG_EDIT)
mt = R(MT)
for a, b in MT_EDITS:
    lines = mt.split('\n'); i = next(i for i, l in enumerate(lines) if l.startswith(a)); lines[i] = lines[i].rstrip() + b; mt = '\n'.join(lines)
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the docket %d bytes, %d rows; works %d' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), NB, NR, NWORKS))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
W(MAP, R(MAP).rstrip('\n') + '\n' + MAPP); W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE); W(REC, rec); W(RES, RESUME + R(RES))
W(MID, R(MID).rstrip('\n') + '\n' + MIDDOT); W(MT, mt); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx); W(MSG, msg)
print('written: the map, the state doc, the recovery page, RESUME, MIDDOT, MISHNAH_TOPICS, the memory note, the index, the commit message')
for p in (MAP, STATEDOC, REC, RES, MID, MT, WALK, IDX):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
