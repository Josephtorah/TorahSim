#!/usr/bin/env python3
# THE NUMBERS WALK 4b — THE COMPILE OF SHELACH (2026-09-10): THE EXAM DOCKET for Numbers 13:1-15:31, written from the scan's dump
# (scratchpad/shelach_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a
# verse of the span; the TOPIC rows = the Mishnah's rows the three reading ledgers and the debt line name BY ADDRESS — the union rule of
# 2026-09-05). Every address in the dump gets ONE verdict (parts A, B, C, D); the coverage is COMPUTED from the dump, never typed; the
# long ranges' sizes are read from the scan's own print. Append-only once written.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_13_15_shelach_exam_2026-09-10.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/shelach_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR = [(k, a.strip(), v.strip()) for k, a, v in rows]
assert len(ADDR) == 313 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 180, len(ADDR)
V = {}
for part in ('shelach_docket_A', 'shelach_docket_B', 'shelach_docket_C', 'shelach_docket_D'):
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
scan = open(f'{SCR}/shelach_scan1.out', encoding='utf-8').read()
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 31, len(LONG)
hdr = (f'# THE EXAM DOCKET — Numbers 13:1-15:31 (Shelach; 15:32-41 frozen at THE TENT and skipped), THE NUMBERS WALK sitting 4b, the compile (2026-09-10; the owner: "Go" after the #123 rereads, on the ruling READ THEN COMPILE; the design World/step9/NUMBERS_WALK.md "Sitting 4b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of the span (the scan by script over Data/sefaria_export, commentaries excluded: {sum(1 for k, _, _ in ADDR if k == "LINK")} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + f'); and (2) THE TOPIC ROWS BY ADDRESS — the Mishnah chapters and mishnayot the three reading ledgers\' TESTING SHELF lines and the COMPILE_DEBT line name (Menachot 9, 12, 13; Zevachim 14; Shekalim 7; Kinnim 1-3; Challah 1-4; Terumot 4; Horayot 1-2; Keritot 1:1-2; Shabbat 7:1; Sanhedrin 1:6, 10:3; Ta\'anit 4:6-7; Sotah 7; Avot 3:11, 4:2, 5:4; Parah 1:3), {sum(1 for k, _, _ in ADDR if k == "TOPIC")} rows after the link-duplicates were dropped. Every row read whole and given ONE verdict: LAW (a rule the compiled function must answer — the CELL named), DERIVATION (a hook from the verse to a rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE.\n'
       f'# THE LONG TALMUD RANGES the ledgers name ("the tractate is the exam") enter through the link rows; their remainder is OUTSIDE DECLARED SCOPE, enumerated by count, never silently narrowed: ' + '; '.join(f'{n} ({s} segments, {l} of them link rows read here, {s - l} outside)' for n, s, l in LONG) + '. The Sifrei on Numbers is SILENT on chapters 13-14 (sitting 4\'s measured fact); Numbers Rabbah and the twenty-three commentary directories on Numbers OUTSIDE DECLARED SCOPE (the ledgers\' lists).\n'
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
- THE FORTY MINUS ONE (Taanit 29a:4-7): the baraita sends the spies on the twenty-ninth of Sivan and returns them "at the end of forty days" on the Ninth of Av; the gemara itself counts thirty-nine and Abaye makes Tammuz full — the tape's return marker at (2, 5, 9) and the machine's forty-day timer firing at (2, 5, 10) are the two sides of the gemara's own objection; "that night" the night of the Ninth of Av (29a:7, Sanhedrin 104b:4, Sotah 35a:11; Mishnah Ta'anit 4:6 the answer sheet).
- THE DEFINITE ONE ON THE ANSWER SHEET (Menachot 91b:9, 91b:20): "for the one lamb" includes the woman-after-childbirth's olah, "the one" the animal tithe's eleventh, "for the one bull" the calf — the tradition reads the very token the parser had left silent (THE DEFINITE ONE, sitting 4's named gap) as a load-bearing inclusion at three seats.
- THE TABLE IN LOGS (Mishnah Menachot 9:2-4, 12:4, 13:5; Menachot 104a, 107a): the hin is twelve logs, so the ink's quarter, third and half are three, four and six — the mixing rule and the donation floors (three, four, six, never one, two or five) are the table's own arithmetic; and the Sukkot-on-the-Sabbath sixty-one is the table summed over the day's animals — a checkable cell.
- THE CENSUS SET WITH ITS EDGES (Bava Batra 121b:8, 121b:11, 121a:9): "from twenty years old and upward, all your counted" — Levi outside (counted from thirty), the over-sixty outside by the valuations' "and upward", the dying ceased on the fifteenth of Av of the fortieth year (Deut 2:16-17 the speech resumed).
- THE CONGREGATION OF TEN (Mishnah Sanhedrin 1:6; Berakhot 21b, Megillah 23b, Sanhedrin 74b): "this evil congregation" = the twelve less Joshua and Caleb — the quorum's own source, carried by two verbal analogies to Korach and to the sanctification of the Name.
- THE WHOLE TORAH JUXTAPOSED TO IDOLATRY (Horayot 8a:14, Keritot 3a:20, Shabbat 69a:1, Yevamot 9a:9; Mishnah Keritot 1:2, Horayot 2:3, 2:6): 15:29-30's "one Torah... with a high hand" makes the karet class — intentional karet, unwitting sin offering — the rule the chatat engine already carries by IMPORT; its answer-sheet table at Horayot 2:6 collapses the leader and the anointed to the individual's she-goat for idolatry, exactly as chatat.rank reads.
- THE ALEPH ON THE ANSWER SHEET (Horayot 13a:4, Zevachim 90b:6): sitting 4's crown — "for a sin offering" without its aleph at 15:24, once in the Bible — is the gemara's own ground that the idolatry goat follows its bull.
- THE FORK ON THE DOUBLED INFINITIVE (Sanhedrin 64b:21-22, 90b:18; Shevuot 13a:2): R. Akiva's two worlds against R. Yishmael's "the Torah spoke in the language of men" — MIDDOT.md's governance row, at three seats; Rabbi's "before and after Yom Kippur" a third reading.
- THE CONVERT'S ENTRY (Keritot 8b:18-9a:10; Yevamot 46b:16; Mishnah Kinnim 1:1): "as you do, so shall he do" — the covenant's own offerings; the bird pair both olot; a court of three from "one judgment"; accepted "throughout your generations" without a Temple.
- THE LAND GATE'S TWO ARMS (Zevachim 111a:7; Kiddushin 37b:1): the libations from the entry, or from inheritance and settlement — the cell's own gate, not the daemon's; and the challah's "when you come" = ALL of you (Ketubot 25a, Niddah 47a) — rabbinic today.
- HEBRON AND THE CLUSTER (Sotah 34a:9, 34b:7, 34b:11; Ketubot 112a:8): "he came" singular = Caleb at the graves; "built seven years" = sevenfold fertility; "on a pole between two" = two poles, four (eight) bearers, 480 seah — the ink's numbers with the shelf's readings as data.
- ZELOPHEHAD AMONG THE PRESUMERS (Shabbat 97a:1): R. Yehuda ben Beteira places the daughters' father at 14:44 — THE TENT's fourth case reaching back into this portion's line.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_shelach_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))} — the counts the script\'s own Counter measured)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('wrote', OUT, '| rows', len(ADDR), dict(cnt), '| link', dict(cnt_link), '| topic', dict(cnt_topic))
