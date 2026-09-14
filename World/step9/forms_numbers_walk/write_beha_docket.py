#!/usr/bin/env python3
# THE NUMBERS WALK 3b — THE COMPILE OF BEHA'ALOTCHA (2026-09-10): THE EXAM DOCKET for Numbers 8:1-26 + 10:1-12:16, written from the scan's dump
# (scratchpad/beha_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of
# the span; the TOPIC rows = the Mishnah's rows the four reading ledgers name BY ADDRESS — the union rule of 2026-09-05). Every address in
# the dump gets ONE verdict (parts A, B, C); the coverage is COMPUTED from the dump, never typed; the long ranges' sizes are read from the
# scan's own print. Append-only once written.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_08_12_beha_exam_2026-09-10.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/beha_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR = [(k, a.strip(), v.strip()) for k, a, v in rows]
assert len(ADDR) == 212 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 131, len(ADDR)
V = {}
for part in ('beha_docket_A', 'beha_docket_B', 'beha_docket_C'):
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
scan = open(f'{SCR}/beha_scan3.out', encoding='utf-8').read()
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 35, len(LONG)
hdr = (f'# THE EXAM DOCKET — Numbers 8:1-26 + 10:1-12:16 (Beha\'alotcha; chapter 9 frozen at THE TENT and skipped), THE NUMBERS WALK sitting 3b, the compile (2026-09-10; the owner: "Keep going" on the ruling READ THEN COMPILE; the design World/step9/NUMBERS_WALK.md "Sitting 3b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of the span (the scan by script over Data/sefaria_export, commentaries excluded: {sum(1 for k, _, _ in ADDR if k == "LINK")} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + f'); and (2) THE TOPIC ROWS BY ADDRESS — the Mishnah chapters and mishnayot the four reading ledgers\' TESTING SHELF lines name (Menachot 3:7, 4:4; Tamid 3:9, 6:1, 7:3; Chullin 1:6; Arakhin 2:3-6; Rosh Hashanah 3-4; Ta\'anit 1-3; Sukkah 5; Yadayim 3:5; Sanhedrin 1; Sotah 1:7-9; Bava Kamma 2:5; Negaim 2-3:2; Moed Katan 3:1-2; Berakhot 5:5; Avot 5:4; Bekhorot 1:1), {sum(1 for k, _, _ in ADDR if k == "TOPIC")} rows after the link-duplicates were dropped. Every row read whole and given ONE verdict: LAW (a rule the compiled function must answer — the CELL named), DERIVATION (a hook from the verse to a rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE.\n'
       f'# THE LONG TALMUD RANGES the ledgers name ("the tractate is the exam") enter through the link rows; their remainder is OUTSIDE DECLARED SCOPE, enumerated by count, never silently narrowed: ' + '; '.join(f'{n} ({s} segments, {l} of them link rows read here, {s - l} outside)' for n, s, l in LONG) + '. Numbers Rabbah and the twenty-three commentary directories on Numbers OUTSIDE DECLARED SCOPE (the ledgers\' lists).\n'
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
- THE DAY-STACK ON THE SHELF (Taanit 29a:2-5): the twentieth of Iyar (10:11), plus three days' journey (10:33), the month of flesh ending on the twenty-second of Sivan, Hazeroth with Miriam's seven days until the twenty-ninth, the spies sent that day — the portion's three READING-PLACED markers (11:1, 11:35, 12:16) and its three timers are the gemara's own arithmetic; the machine's month timer will DIVERGE by two days from the Hazeroth marker (the inclusive count with a full Iyar — the gemara's own "forty days minus one" at 29a:5 is the same problem); Seder Olam Rabbah 8:2's twenty-eighth the variant row.
- ONE PLAGUE, TWO TIMERS (Yoma 75b:2 = Sifrei 94:1): "while the meat was yet between their teeth" against "a whole month until it comes out of your nostrils" — the average died at once, the wicked after a month: the tape's put_to_death at 11:33 and the flesh_for_a_month timer are the reconciliation's two arms.
- THE IDENTITY CARRIES THE SHOFAR'S ORDER FROM THE TRUMPETS (Rosh Hashanah 34a:6-8; Sukkah 53b; Arakhin 10a): "teruah" in the wilderness / "teruah" at Rosh Hashanah — tekiah-teruah-tekiah from 10:5-6's verbs and the superfluous "second"; the moadim engine's sound is CALLED from the trumpets' cell; R. Yehuda's one-unit against the Rabbis' three the parameter.
- THE 2x2 ON THE ANSWER SHEET (Menachot 28a:16-18; Mishnah Rosh Hashanah 3:6): the lampstand of gold must be beaten, of other metals may be cast; the trumpets silver only, fragments valid — while a shofar of fragments is unfit: Sifrei 61:1's table at three seats.
- THE INSTANCE SCOPE OF A VESSEL (Menachot 28b:2-3): "for you" written twice — Moses' trumpets were his alone and hidden, every other vessel he made served the generations: the engine's first vessel with an instance scope beside the lampstand's generation scope.
- DAYO AT FOUR SEATS (Bava Kamma 25a:3, Bava Batra 111a:5, Zevachim 69b:6, Mishnah Bava Kamma 2:5): the a-fortiori's cap is Torah law, proved from Miriam's seven days; 12:15's second verse makes it general (not respect for Moses); the goring ox its answer-sheet application.
- THE SEVENTY-TWO BALLOTS (Sanhedrin 17a:4-5): six per tribe, seventy by lot from a box — the 273's mechanism at its second seat; "with you" read four ways (counted with them / fit to rule / whole in body / of fit lineage — Horayot 4b, Kiddushin 76b, Sanhedrin 36b).
- THE SPINE'S DUAL TRACK ON THE ANSWER SHEET (Sanhedrin 17a:12-13): "they prophesied and did not continue" read "did not stop" (as Deut 5:19's great voice) — the gemara argues the very reading Onkelos chose ("did not cease"), and settles the two by 11:27's participle: the seventy stopped, Eldad and Medad did not.
- THE SECTION OUT OF PLACE (Shabbat 115b-116a; Mishnah Yadayim 3:5): the eighty-five letters computed on the ink at sitting 3 are the Mishnah's own measure for a scroll that defiles the hands and the gemara's for one rescued from a fire; R. Shimon b. Gamliel's "to separate the two punishments" beside Rebbi's "a book in itself" — two readings of the inverted nuns the DB carries as marks.
- WHO DECLARED MIRIAM (Zevachim 101b:19; Mishnah Negaim 2:5, 3:1): not Moses the non-priest, not Aaron her kin (R. Meir), only a priest's mouth declares — the parameter row who_declared_miriam with its three settings.
- THE ARTICLE BLOCKS THE IDENTITY (Yoma 76a:1): "man" / "man" reads Joshua at 27:18, not "THE man Moses" at 12:3 — a rule about I2's token-matching, filed in the middot's case law.
- THE TRUMPETS' OPPRESSION IS ANY OPPRESSION (Mishnah Ta'anit 1:4-3:8): drought's ladder, pestilence's threshold (three dead in three days per five hundred), the spreading calamities everywhere, the Sabbath's three dangers, the one exclusion (too much rain) — 10:9's "the oppressor that oppresses you" unrolled into the fasts' whole table; the alarm sounded on the last seven fasts, the priests' blasts between the blessings inside the Temple only.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_beha_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))} — the counts the script\'s own Counter measured)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('wrote', OUT, '| rows', len(ADDR), dict(cnt), '| link', dict(cnt_link), '| topic', dict(cnt_topic))
