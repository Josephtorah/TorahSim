#!/usr/bin/env python3
# THE NUMBERS WALK 2b — THE COMPILE OF NASO (2026-09-10): THE EXAM DOCKET for Numbers 4:21-7:89, written from the scan's dump
# (scratchpad/naso_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a
# verse of the span; the TOPIC rows = the Mishnah's rows the seven reading ledgers name BY ADDRESS — the union rule of 2026-09-05).
# Every address in the dump gets ONE verdict (parts A, B, C); the coverage is COMPUTED from the dump, never typed. Append-only once written.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_04_07_naso_exam_2026-09-10.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/naso_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR = [(k, a.strip(), v.strip()) for k, a, v in rows]
assert len(ADDR) == 638 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 473, len(ADDR)
V = {}
for part in ('naso_docket_A', 'naso_docket_B', 'naso_docket_C'):
    spec = importlib.util.spec_from_file_location(part, f'{SCR}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
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
LONG = [('Sotah 2a-31a', 994, 98), ('Nazir 2a-66b', 1297, 104), ('Bava Kamma 103a-111a', 274, 15), ('Sotah 37b-40a', 84, 6), ('Shevuot 35b-36a', 56, 4), ('Menachot 59a-b', 52, 1),
        ('Pesachim 67a-68a', 48, 4), ('Sotah 28a-29a', 45, 14), ('Menachot 90b-91a', 43, 1), ('Yoma 3b-4b', 40, 1), ('Nazir 47b-48b', 34, 9), ('Nazir 60a-61a', 32, 5),
        ('Eruvin 83a-b', 32, 0), ('Berakhot 19b-20a', 27, 1), ('Nedarim 9b-10a', 25, 2), ('Kiddushin 27b-28a', 21, 3)]   # typed from the scan's print (naso_docket_scan.py, 2026-09-10)
hdr = (f'# THE EXAM DOCKET — Numbers 4:21-7:89 (Naso), THE NUMBERS WALK sitting 2b, the compile (2026-09-10; the owner: "Finish compiling before moving on"; the design World/step9/NUMBERS_WALK.md "Sitting 2b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 4:21-7:89 (the scan by script over Data/sefaria_export, commentaries excluded: {sum(1 for k, _, _ in ADDR if k == "LINK")} segments in {len(works)} works — {", ".join(f"{w} {n}" for w, n in works.most_common())}), and (2) THE TOPIC-ROUTED ROWS — the Mishnah\'s rows the seven reading ledgers\' TESTING SHELF lines name BY ADDRESS (Sotah 1-6 whole with 7:1, 7:6, 9:9; Nazir 1-9 whole; Bava Kamma 9:5-12; Nedarim 1:1; Niddah 5:6; Kinnim 1:1, 2:5; Eduyot 5:6; Parah 1:3, 6:1; Tamid 7:2; Megillah 4:3-7; Terumot 4:5; Maaser Sheni 5:1-5; Kelim 1:5-9; Sanhedrin 6:2; Makkot 3; Tahorot 4-6 — {sum(1 for k, _, _ in ADDR if k == "TOPIC")} rows after the link duplicates drop), every row verdicted, the ones on another subject set aside as OUTSIDE. Every address in the scan\'s dump (scratchpad/naso_docket_dump.txt) carries exactly one verdict here — asserted by the script. Verdicts: LAW (a rule the compiled function must answer — the CELL named), DERIVATION (a hook from the verse to the rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE.\n'
       f'# THE LONG TALMUD RANGES the ledgers name ("the tractate is the exam") enter through the link rows; their remainder is OUTSIDE DECLARED SCOPE, enumerated by count, never silently narrowed: ' + '; '.join(f'{n} ({s} segments, {l} of them link rows read here, {s - l} outside)' for n, s, l in LONG) + '. Bikkurim, Chullin 24a, Bekhorot 49a and Mishnah Shekalim 5:2 stand read at Bamidbar (credited); the Jerusalem Talmud and the commentaries outside declared scope.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah.\n\n')
body = ''
last = None
for k, a, vs in ADDR:
    work = a.rsplit(' ', 1)[0]
    if work != last:
        body += f'\n## {work}\n'; last = work
    vd, note = V[a]
    body += f'- {a} [{k}{(" — " + vs) if vs else ""}] — {vd}. {note}\n'
crowns = '''
## The finds (this docket's crowns)
- THE TRANSLATION DECIDES A TANNAITIC DISPUTE (Nazir 39a:2): "in accordance with whose opinion do we TRANSLATE 'from the seeds to the skins'?" — R. Yosei's; the chartzan/zag question of Mishnah Nazir 6:2 is settled by Onkelos' two words, cut at the reading (num_06_nazir's ledger). The translation layer load-bearing a fourth time (after the sela, the teruah, the wail).
- THE SHELF PLACES A DATE THE INK LEAVES BARE (Gittin 60a:17): R. Levi's eight sections said on the day the tabernacle was erected — the sending away of the impure (5:1-4) among them, and the Levites' section (8:5-26, Beha'alotcha's): a reading-placed RETROGRADE marker at 5:1, its teacher named; the design amended at the docket (fourteen new markers).
- THE THREE GOATS OF ONE DAY (Zevachim 101b:6): Lev 10:16's "the goat of the sin-offering" is Nahshon's (7:12), the eighth day's (Lev 9:13) and the New Moon's (Num 28:15) — three goats on the first of Nisan: the day-stack of Sifrei 44:1 and Shabbat 87b witnessed on the answer sheet at the dedication's first day (the checkpoint CD5's shelf witness).
- THE SCHEDULE'S CONTINUITY IS THE SHELF'S RULE (Moed Katan 9a:11-12): "on the day of the ELEVENTH day", "on the day of the TWELFTH day" — the doubled "day" makes the twelve days one continuous period, the Sabbath overridden: the engine's retro-write schedule (day n = the anointing day + n − 1, no gap) is exactly the sugya's reading of the ink's own doubling, measured at the reading (7:72, 7:78).
- THE MIDDOT'S OWN CASE LAW, THREE MORE ENTRIES: THE METHOD FORK on 6:3-4 (Nazir 34b:5-7 — R. Elazar's amplification-and-restriction against the Rabbis' general-and-detail, the leaves the difference); THE HALAKHAH UPROOTS THE VERSE at three seats including 6:5's "razor" (Sotah 16a:6); and R. AKIVA'S A-FORTIORI REFUSED BY "A HALAKHAH TO MOSES FROM SINAI" (Mishnah Nazir 7:4 — the quarter-log of blood): a transmitted rule that no inference may overturn.
- THE EQUATING RULE ON THIS SPAN'S VERSE (Bava Kamma 15a and five more seats): 5:6 "a man or WOMAN" — a woman equals a man for all the Torah's punishments: the theft verse legislates the whole code's gender scope.
- THE DEBT-TRANSFER RULE ON 5:7 (R. Natan, six seats): "he gives it to the one with regard to whom he is guilty" — the courts pay a creditor's creditor directly; the courts engine's reference into this span.
- THE ATTRIBUTION VARIES BY TRACTATE (Nazir 38b:4 against Pesachim 41b:5): the two-sets-of-lashes count is Abaye's in Nazir and Rava's in Pesachim — recorded on the row general_prohibition_lashes as the tradition's own variance (the corpus' attribution guard).
- THE FACE LIFTED, THREE RECONCILIATIONS: 6:26 against Deut 10:17 — the Sifrei's "when they do His will", Berakhot 20b's "beyond the letter of the law", Niddah 70b's "before the sentence": one contradiction, three recorded settings on the row face_lifted.
- BAMIDBAR'S FORWARD POINTER CONFIRMED ON THE ANSWER SHEET (Mishnah Sotah 5:3): the two thousand cubits are Num 35:5's Sabbath limit (R. Akiva), not the camp's distance — the docket of 1b's correction witnessed by the Mishnah itself.
- THE SPELLING THE TEACHER RE-READS (Kiddushin 62a:2; Sotah 3a:4): 5:19's "hinnaki" written without the yod read as "chinnaki" (you shall choke) — the defective spelling carries the curse's unstated side; 5:12's "tisteh" read with a shin as folly — M-16's shape twice on the sotah's own verses (the points measured on the DB at the code).
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_naso_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))} — the counts the script\'s own Counter measured)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('wrote', OUT, '| rows', len(ADDR), dict(cnt), '| link', dict(cnt_link), '| topic', dict(cnt_topic))
