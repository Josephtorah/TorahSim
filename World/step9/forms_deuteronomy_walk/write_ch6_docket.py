import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 4b — THE COMPILE OF CHAPTER 6 (2026-09-17): THE EXAM DOCKET for Deuteronomy 6:1-25, written from the scan's dump
# (scratchpad/ch6_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# chapter — the export's chapter 6 the DB's; the TOPIC rows = the Mishnah rows and the folio ranges of the design's item (l) read WHOLE, Berakhot
# 2a-16a's verse-anchored amudim among them, the range's remainder enumerated outside declared scope; the CREDITED marks = addresses already verdicted
# in an earlier ledger, given their quick look here). Every address in the dump gets ONE verdict (parts A..D on disk, each a SPEC over the dump's own
# addresses); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own print (ch6_scan.out). Append-only.
# Sitting 3b's form (write_ch5_docket.py).
import re, os, sys, importlib.util, subprocess
from collections import Counter
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SCR)
OUT = f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/ch6_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
hdr_line = dump.split('\n', 1)[0]
assert hdr_line == 'ROWS %d LINK %d TOPIC %d CREDITED %d' % (len(ADDR), NL, NT, len(CRED)), (hdr_line, len(ADDR), NL, NT, len(CRED))
V = {}; STATS = []
for p in 'ABCD':
    part = f'ch6_docket_{p}'
    spec = importlib.util.spec_from_file_location(part, f'{SCR}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    STATS.append(m.WHOLE_STATS)   # THE WHOLE-ROW RULE (2026-09-17): each part's reread-whole corrections, computed by apply_whole
    for addr, verdict, note in m.ROWS:
        assert addr not in V, ('duplicate verdict', addr)
        assert verdict in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'), (addr, verdict)
        V[addr] = (verdict, note)
missing = [a for _, a, _ in ADDR if a not in V]; extra = [a for a in V if a not in {x[1] for x in ADDR}]
if missing or extra:
    print('MISSING', len(missing), missing); print('EXTRA', len(extra), extra); sys.exit(1)
cnt = Counter(vd for vd, _ in V.values())
cnt_link = Counter(V[a][0] for k, a, _ in ADDR if k == 'LINK'); cnt_topic = Counter(V[a][0] for k, a, _ in ADDR if k == 'TOPIC')
works = Counter(a.rsplit(' ', 1)[0] for k, a, _ in ADDR if k == 'LINK')
scan = open(f'{SCR}/ch6_scan.out', encoding='utf-8').read()
me = re.search(r'ENUMERATED OUTSIDE DECLARED SCOPE — Berakhot 2a-16a whole: (\d+) rows; the amudim read here: (\d+)', scan); B_WHOLE, B_READ = int(me.group(1)), int(me.group(2))
scan_r = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) rows,\s+(\d+) link rows', scan_r, re.M)]   # read from the scan's print
assert len(LONG) == 16, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and not re.search(r'\d+[ab]:\d+$', a)]   # the Mishnah rows among the topic rows (the link ones dropped)
assert len(MISH) == 21, MISH
assert sum(s - l for _, s, l in LONG) + len(MISH) == NT, (sum(s - l for _, s, l in LONG), len(MISH), NT)   # every range read WHOLE
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in re.findall(r'Deut 6:\d+', vs))
LAWCELLS = Counter(m.group(1) for vd, note in V.values() if vd == 'LAW' for m in [re.search(r'\b(F[1-6])\b', note)] if m)
TOT = {k: sum(s[k] for s in STATS) for k in STATS[0]}; assert TOT['rows'] == len(ADDR), TOT
NWHOLE = sum(1 for vd, note in V.values() if '[whole:' in note); assert NWHOLE == TOT['corrected'], (NWHOLE, TOT)
hdr = (f'# THE EXAM DOCKET — Deuteronomy 6:1-25 (the Shema — the creed and the love; the four duties: the words on the heart, the teaching, the tefillin, the mezuzah; the gift and the warning; the test at Massah; the right and the good; the son\'s question and the answer that retells the exodus), THE DEUTERONOMY WALK sitting 4b (2026-09-17; World/step9/DEUTERONOMY_WALK.md "Sitting 4b"; the runner cold_run_hear_o_israel.py, the daemon law_hear_o_israel).\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 6 (the scan ch6_docket_scan.py: {NL} rows in {len(works)} works; the export\'s chapter 6 the DB\'s twenty-five verses, no division map; the verses cited most {", ".join(f"{v} {n}" for v, n in verses.most_common(7))}), and (2) THE TOPIC ROWS by address (the reading ledger\'s TESTING paragraph, COMPILE_DEBT\'s sitting-4 box (l), the design\'s (l)): the Mishnah rows {", ".join(MISH)} and the folio ranges read WHOLE — {"; ".join(f"{n} ({s} rows, {l} of them link rows)" for n, s, l in LONG)} = {NT} topic rows; BERAKHOT 2a-16a ({B_WHOLE} rows) is read at its VERSE-ANCHORED amudim only ({B_READ} rows: 2a-2b the evening\'s time, 10b-11a the postures, 13a-13b the intention and the language, 15a-16a the audibility and the exemptions), its remainder ({B_WHOLE - B_READ} rows — the night\'s watches, David\'s harp, the laws of prayer and the synagogue) ENUMERATED and marked OUTSIDE DECLARED SCOPE (Step 2\'s standing rule). EVERY ADDRESS ONE VERDICT: LAW (the cell of cold_run_hear_o_israel.py named — F1 the_header, F2 the_creed, F3 the_four_duties, F4 the_gift_and_the_warning, F5 the_test_and_the_right, F6 the_sons_question — or the callee\'s cell by CALL), DERIVATION, DISPUTE, CONTEXT, OUTSIDE; {len(CRED)} addresses CREDITED from earlier ledgers (link {ncred_link}, topic {ncred_topic}) with their quick look. The rows were FIRST read at a short cut (the address, the kind, the first 170 characters) and THEN REREAD WHOLE on the owner\'s ruling (the REREAD WHOLE line below); the rows are the answer sheet\'s: the Mishnah GRADES, the Talmud TEACHES per gap; nothing here is code.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah.\n'
       f'# REREAD WHOLE (2026-09-17 — THE WHOLE-ROW RULE, owner-ruled "never ever cut corners with the Talmud"): the first pass gave every verdict from the row\'s first 170 characters; every row was then printed WHOLE and read against that verdict — {TOT["corrected"]} of {TOT["rows"]} rows corrected ({TOT["verdicts_changed"]} verdicts changed, {TOT["notes_changed"]} notes rewritten; a corrected note ends "[whole: …]" naming what the cut missed; the cut\'s verdicts stay in the parts\' SPEC lists as the record). The counts computed by apply_whole, never typed.\n')
body = ''
last = None
for k, a, vs in ADDR:
    work = a.rsplit(' ', 1)[0]
    if work != last:
        body += f'\n## {work}\n'; last = work
    vd, note = V[a]
    body += f'- {a} [{k}{(" — " + vs) if vs else ""}{(" — CREDITED: " + CRED[a]) if a in CRED else ""}] — {vd}. {note}\n'
crowns = '''
## The finds (this docket's crowns)
- THE TIMES FROM "LIE DOWN" AND "RISE" (Mishnah Berakhot 1:1-2; Berakhot 2a:6-8, 2b:1-19, 10b:31-35): the evening from the priests' terumah until the first watch / midnight / dawn, the morning from blue-against-white until sunrise / three hours — the two clauses of 6:7 the two times, the bounds a PARAMETER table: F3 recite_when, the DATA row the_recitation_times.
- THE POSTURES (Mishnah Berakhot 1:3; Berakhot 10b:37-11a:23): Shammai by the letter — recline in the evening, stand in the morning; Hillel — each in his way, "when you walk by the way"; R. Tarfon's reclining "deserved his life"; R. Yishmael and R. Elazar ben Azariah — the Sifrei 34:9-10's Talmud seat: F3 the_postures.
- THE EXEMPTION FROM "THE WAY" (Berakhot 11a:4-11, 16a:20-23; Sukkah 25a:5; Tosefta Berakhot 1:5; Mishnah Berakhot 2:5, 3:1-3): "when you walk by the way" — a voluntary walk; one busy with a mitzva, the groom of a virgin, the mourner before his dead exempt; women, slaves and minors exempt from the Shema and tefillin, obligated in mezuzah: F3 recite_who, the DATA row the_exemptions.
- "HEAR" READ TWICE (Berakhot 15a:9-10, 13a:25-35; Megillah 20a:2; Sotah 32b:18-21; Mishnah Sotah 7:1; Mishnah Berakhot 2:3): audible to your ear (R. Yose — the Sifrei 31:7) and in any language you hear (the Rabbis against Rabbi's "and they shall be"); the halakha: audible ab initio, fulfilled after the fact (Rav Chisda, 15b:12): F3 recite_how, the DATA row the_language.
- THE INTENTION AND THE FIRST VERSE (Berakhot 13a:22-13b:21): the whole portion requires intent (R. Akiva — the halakha); the first verse's intent; standing still for it ("upon your heart"); Rabbi's Shema the single verse; ONE PROLONGED — in the dalet (Sumakhos, Rav Acha: 13b:14-15): the letter the store drops (the DATA row the_large_letters' neighbor): F3 recite_how.
- THE THREE TERMS (Mishnah Berakhot 9:5; Berakhot 54a:6, 61b:5-10; Sanhedrin 74a:10-23; Yoma 82a:10; Pesachim 25a:11): the two inclinations, the soul even if He takes it — R. Akiva combed with iron reciting the Shema, his soul at "one"; the money — the body dearer / the property dearer (74a:16 — the Sifrei 32:6); the three sins one dies for; persecution's minor mitzva: F2 with_all_your_heart, with_all_your_soul, with_all_your_might.
- THE FOUR PASSAGES AND THE COMPARTMENTS (Mishnah Menachot 3:7; Menachot 34a:16-35a:2; Sanhedrin 4b:12-14; Zevachim 37b:14): the hand's one hide, the head's four — from the SPELLINGS of "frontlets" (two defective, one plene — the count that reads 11:18 defective where the ink is plene: THE OPEN ROW, the number a PARAMETER) and, without the spellings, from "tot" and "pat" (R. Akiva); the vocalization against the tradition (Sanhedrin 4b): F3 tefillin_compartments, the DATA row the_spellings.
- THE LEFT ARM, THE BICEP, THE HEAD (Menachot 36b:11-37b:7; Eruvin 95b:17; Menachot 37a:6): "your hand" the left (Judges 5:26, Isaiah 48:13 — the Sifrei 35:8); "yadkha" with a heh (Exodus 13:16) the weak hand — THE INK'S FOURTH SPELLING OF "YOUR HAND" read by the shelf; the amputee (R. Yose HaChorem — 35:10); the bicep, "a sign for you" (35:5-6), opposite the heart (35:7); the head's height — "between your eyes" a place fit for baldness (14:1 — THE INK'S FIFTH SEAT) and for a plague-mark (R. Yehuda — 35:12): F3 tefillin_arm, tefillin_head.
- THE ORDER (Menachot 36a:1-6): the arm first, the head first off — "and they shall be" plural (the Sifrei 35:11); speaking between them a sin: F3 tefillin_order.
- THE TEFILLIN'S TIME AND FORM (Menachot 35a:3-36b:9; Kiddushin 34a:1-6; Berakhot 20b:4; Arakhin 3b:10): days not nights, Shabbat and festivals excluded ("from days to days" / "a sign" — Exodus 13:9-10 by the passover's cell), the halakhot to Moses from Sinai (square, black, the knot's dalet) THE SECOND CHANNEL beside the ink; everyone obligated; women exempt: F3 tefillin, the DATA row the_tefillin_table.
- THE MEZUZAH'S WRITING (Berakhot 15b:23-26; Shabbat 103b:14-17; Menachot 31b:5-32b:8, 34a:12-15; Megillah 9a:5-9; Gittin 45b:6; Menachot 42b:1): a perfect writing (ukhtavtam — the Sifrei 36:1), in Hebrew ("and they shall be" — 6:6), on a scroll not stone — THE TWO ANALOGIES chosen by "which it resembles" (34a:12-13 — the Sifrei 36:2), the sotah's analogy refused by the verse's own word (15b:26), written first then affixed (34a:14-15 — Onkelos's "and fix them"); the writer who is in the binding: F3 mezuzah_writing.
- THE MEZUZAH'S POST, SIDE, HEIGHT AND GATES (Menachot 32b:9-34a:5, 34a:6-11; Yoma 11a; Mishnah Maaser Sheni 3:8; Chullin 135b:15; Bava Metzia 101b:19): affixed not hung; one post (R. Meir — extension after extension, the Sifrei 36:3; R. Akiva's father from Exodus 12:22 — 36:4); the right by "your coming" (36:5); the upper third; the dwelling's gates — city gates obligated, the hay-store, the bathhouse, the tannery exempt, the Temple's chambers by their opening (36:6-8): F3 mezuzah_doorpost, mezuzah_gates, the DATA row the_mezuzah_table.
- THE SEVEN (Menachot 43b:10-12): beloved are Israel — the tefillin's two, the fringes' four, the mezuzah's one; David naked in the bathhouse remembering his circumcision (the Sifrei 36:9): F3 the_seven.
- THE FATHER'S DUTY TO TEACH (Kiddushin 29a:6-10, 29b:8-11, 30a:1-7, 30b:1-2; Berakhot 13b:12, 14b:13): teach his son Torah from "and you shall teach them to your sons" (11:19 with 6:7); the mother not obligated; the grandfather — two tannaim (30a:5-6: "your sons" not the sons' sons / the sons' sons from 4:9), R. Yehoshua ben Levi's "as if from Sinai" (30a:7); the words sharp in your mouth (30a:9-15 — the Sifrei 34:1); the extent, the three parts of one's years: F3 teach_your_sons, the DATA row the_fathers_duties.
- THE CREED AT JACOB'S BED AND THE RESPONSE LINE (Pesachim 56a:6-13): "hear, Israel our father — as in your heart only One, so in ours"; Jacob's "blessed be the name of His glorious kingdom" — Moses did not say it, so it is said quietly (aloud in Nehardea for the heretics); Jericho's bundling — no pause after "one": the Sifrei 31:6's Talmud seat: F2 hear_o_israel, F3 recite_how.
- THE SON'S ANSWER IS THE HAGGADAH'S (Mishnah Pesachim 10:4; Pesachim 116a:5-116b:9): "according to the son's understanding"; "with disgrace" — Shmuel: "WE WERE SLAVES TO PHARAOH" (6:21); Rava: one must say "AND HE TOOK US OUT FROM THERE" (6:23); "in every generation one sees himself as though he left Egypt" — "you shall tell your son" (Exodus 13:8): THE READBACK'S THIRD FORM TAUGHT BY THE SHELF — the retelling commanded, its rows 6:21 and 6:23 the telling's obligatory clauses: F6 the_four_askings, the_answer_rows, the DATA row the_four_sons.
- THE TRUE OATH PERMITTED BY 6:13 (Temurah 3b:16-18, 4a:2): the bailee's oath in court (Exodus 22:10, at 3b:16), then "by His name you shall swear" (6:13 at 3b:17; 10:20 at 3b:18) — the true oath permitted, an oath to keep the commandments a duty ("I have sworn and will fulfil"); "you shall fear" offered as the warning for the Name in vain and refused as a positive command (4a:2): F4 fear_serve_swear, the DATA row the_oath_by_the_name; "et" includes the scholars (Bava Kamma 41b:7).
- THE ABUTTER AND THE RIGHT-AND-GOOD (Bava Metzia 108a:9-15, 108b:4, 16b:13, 35a:12): the neighbor displaces the buyer; the debtor's land returned; the appraisal reversed — "you shall do the right and the good" (6:18) a rule beyond the letter with its cases: F5 the_abutter, the DATA row the_abutter.
- YOU SHALL NOT TEST — EXCEPT THE TITHE (Taanit 9a:3): "you shall not test the LORD your God" (6:16) with Malachi 3:10's "test Me in this": F5 you_shall_not_test (the one exception — DATA).
- THE CONQUEST'S HOUSES (Chullin 17a:12): "houses full of all good" (6:11) — forbidden foods permitted in the seven years (Rav): F4 the_list (201:3's kin — the spoil permitted, a LAW of the conquest).
- THE BLIND EXEMPT FROM 6:1 (Bava Kamma 87a:2): R. Yehuda reads "and this is the commandment, the statutes and the judgments" as one scope — whoever is in the judgments is in the commandments: F1 the_header (the triad read by the shelf as a scope rule — DATA the_blind).
- THE LARGE LETTERS' TALMUD SEAT (Kiddushin 30a:11-14): the soferim who counted; the vav of "belly" the letters' middle, "then he shall be shaven" the verses' middle — read here and left as the parked hypothesis' seat (RESEARCH_LOG 2026-09-17: the three middles diverge from the text's count).
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_ch6_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0; Berakhot 2a-16a\'s remainder %d rows enumerated outside declared scope, not opened)\n' % (len(ADDR), B_WHOLE - B_READ)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed; the Berakhot remainder {B_WHOLE - B_READ} rows outside declared scope, enumerated).\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, os.path.getsize(OUT), 'bytes')
print('rows', len(ADDR), 'link', NL, 'topic', NT, 'credited', len(CRED), '(link', ncred_link, 'topic', ncred_topic, ')')
print('verdicts', dict(sorted(cnt.items())), 'link', dict(sorted(cnt_link.items())), 'topic', dict(sorted(cnt_topic.items())))
print('LAW by cell', dict(sorted(LAWCELLS.items())))
print('ranges', [(n, s, l) for n, s, l in LONG]); print('mishnah rows', len(MISH), '| Berakhot whole', B_WHOLE, 'read', B_READ)
