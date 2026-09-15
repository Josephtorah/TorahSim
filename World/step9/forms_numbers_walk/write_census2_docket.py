import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 8b — THE COMPILE OF THE SECOND CENSUS (2026-09-11): THE EXAM DOCKET for Numbers 25:19-26:65, written from the scan's
# dump (scratchpad/census2_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a
# verse of the span; the TOPIC rows = the Mishnah's rows the reading ledger's TESTING SHELF lines and the debt box name BY ADDRESS, Bava Batra
# 117a-123a whole, 143b, Sotah 12a-13a whole, Sanhedrin 110a, Yoma 73b, Seder Olam Rabbah 9-10 — the union rule of 2026-09-05; the CREDITED
# marks = addresses already verdicted in an earlier ledger, given their quick look here). Every address in the dump gets ONE verdict (parts
# A, B, C, D); the coverage is COMPUTED from the dump, never typed; the long ranges' sizes are read from the scan's own print. Append-only.
import re, os, sys, importlib.util
from collections import Counter
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_26_second_census_exam_2026-09-11.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/census2_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
assert len(ADDR) == 264 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 19 and len(CRED) == 124, (len(ADDR), len(CRED))
V = {}
for part in ('census2_docket_A', 'census2_docket_B', 'census2_docket_C', 'census2_docket_D'):
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
scan = open(f'{SCR}/census2_scan2.out', encoding='utf-8').read()
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 9, len(LONG)
WHOLE = {'Bava Batra 117a-123a', 'Bava Batra 143b-143b', 'Sotah 12a-13a', 'Sanhedrin 110a-110a', 'Yoma 73b-73b'}
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
hdr = (f'# THE EXAM DOCKET — Numbers 25:19-26:65 (the second census), THE NUMBERS WALK sitting 8b, the compile (2026-09-11; the owner: "Ok go" on the one-sitting form with the population table built first; the design World/step9/NUMBERS_WALK.md "Sitting 8b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites Numbers 25:19 or a verse of 26:1-65 (the scan by script over Data/sefaria_export, commentaries excluded: {sum(1 for k, _, _ in ADDR if k == "LINK")} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + '), and (2) THE TOPIC-ROUTED ROWS — the rows the reading ledger\'s TESTING SHELF lines and the COMPILE_DEBT box name BY ADDRESS: Mishnah Bava Batra 8:1-2 (the inheritance order — THE ANSWER SHEET the daughters\' row feeds) and 7:1-4 (the sale by measure — the estimate\'s vocabulary, Sifrei 132:4); BAVA BATRA 117a-123a WHOLE — the land\'s division (the exodus generation against the entrants, the lot and the Urim, the daughters, Jochebed, the birthright): 140 segments in the range, 10 of them link rows, the other 130 here by address; BAVA BATRA 143b (the plural for one son); SOTAH 12a-13a WHOLE (Amram, Jochebed, Miriam, Serah: 63 segments, 1 a link row); SANHEDRIN 110a WHOLE (Korach\'s deaths and his sons: 17, 4 link rows); YOMA 73b WHOLE (the Urim — the lot\'s mouth: 20); SEDER OLAM RABBAH 9-10 by address (the year and the order after the plague — the export\'s chapters under an empty key beside "Introduction", measured 2026-09-11: 5 rows): {sum(1 for k, _, _ in ADDR if k == "TOPIC")} rows, link-duplicates dropped. {len(CRED)} addresses ({ncred_link} link, {ncred_topic} topic) were ALREADY VERDICTED in earlier ledgers (the inheritance docket of THE TENT sitting 4 the largest share) and are marked CREDITED with the ledger named — each given its QUICK LOOK here (speed ruling (b), credit guard (1)), never a blind credit. Every row carries ONE verdict: LAW (a rule the compiled function answers — the CELL named, or the callee\'s cell by CALL), DERIVATION (a hook from the verse to a rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE (a row outside the span\'s ink — 27:21\'s Urim rows and Yoma\'s afflictions, named). The Sifrei on Numbers piska 132 (the reading shelf) was read at sitting 8, not here.\n'
       f'# THE LONG TALMUD RANGES the box names enter through the link rows or whole by address; their remainder is OUTSIDE DECLARED SCOPE, enumerated by count, never silently narrowed: ' + '; '.join(f'{n} ({s} segments, {l} of them link rows read here, {s - l} {"read whole by address" if n in WHOLE else "outside"})' for n, s, l in LONG) + '.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah; Seder Olam Rabbah by chapter:segment of the export (measured 2026-09-11).\n')
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
- THE DEAD INHERIT THE LIVING, ON THE TALMUD'S SHELF (Bava Batra 117a:2-117b:1; Rebbi's parable 117a:4): the Sifrei 132:1's four-way dispute on "to these" (26:53) against "by the names of the tribes of their fathers" (26:55) is the Talmud's three-way baraita (the outside teaching) — R. Yoshiyah those who left Egypt, R. Yonatan the entrants with the portions passing UP to the dead fathers and down again, R. Shimon ben Elazar both "so that both verses are satisfied"; the Zelophehad runner's row land_divided_among carries the three arms since THE TENT and is READ here by call, never re-declared — the Mishnah of 116b (Zelophehad and Hepher entitled) taught on the first arm (117a:1).
- THE LOT HAS A MOUTH AND THE MOUTH IS THE ORACLE (Bava Batra 122a:3-6; Yoma 73b:3): "only by lot" (26:55) and "by the mouth of the lot" (26:56) reconciled — Eleazar in the Urim, Joshua and all Israel before him, two receptacles (the tribes' names, the boundaries), the Spirit naming the pair before the lots emerge; a decree of the Urim cannot be retracted — "by the judgment of the Urim" (27:21, outside this span: Joshua's appointment, 27:12-23, not compiled at THE TENT — a readback line).
- BY TRIBES, THEN BY NUMBERS WITHIN (Bava Batra 121b:12 → 122a:1-2, 8): the dilemma tribes-or-skulls resolved from 26:56's "between the many and the few" — twelve equal wholes (Levi none — 26:62's clause), the individuals' shares differing within: the population table's two grains are the Talmud's two levels of the division; and the division "with money" — near Jerusalem against far, R. Eliezer money / R. Yehoshua land (122a:10-11), the row compensation_mode.
- "ONLY" EXCLUDES THE TWO, TWICE (Bava Batra 122a:12, 122b:2): Joshua by the LORD's word at Timnath-serah (Josh 19:50), Caleb's Hebron "as Moses had spoken" (Judg 1:20) with its outskirts (Josh 21:12) — the Sifrei 132:3's exclusion with Joshua's seat named; the reading's mistyped "Judges 15:13" read to its verse here.
- THE SPIES' PORTIONS AND THE PROTESTERS' (Bava Batra 117b:2, 118b:3-7): Joshua and Caleb took the spies' portions — 14:38's "lived" beside 26:65's "remained" (Ulla); the protesters and Korach's assembly no portion, their sons by the grandfathers; Abaye: the protesters = the TWO HUNDRED AND FIFTY (26:10's count by call) — the predicate's shelf corollary: who of the first roll's dead bequeathed.
- TEN PARTS FOR MANASSEH (Bava Batra 118b:8-119a:1; Josh 17:5): six fathers' houses + four of the daughters on the first arm; eight on the second; the Mishnah's three + an uncle — and THE LAND IN POSSESSION BEFORE IT IS ASSIGNED (119a:1, 119a:5): the table's rows are holdings before the lot.
- "MORASHA" RESOLVED BOTH WAYS (Bava Batra 119b:3-4; Exod 6:8): an inheritance from the fathers in the exodus generation's possession AND the generation bequeaths without inheriting — Exod 15:17's "You will bring THEM in" the song's unknowing prophecy; 26:64-65's predicate on the Talmud's page.
- JOCHEBED BETWEEN THE WALLS, ON THREE PAGES (Bava Batra 120a:1-2, 123b:1; Sotah 12a:14-15): the seventy's missing one is the woman 26:59 says was "born to Levi in Egypt" — conceived on the way; 130 at Moses' birth (210 years, Moses eighty), "a daughter" by her youth reborn; CJ3b's ink witness with the shelf's answer beside it, the verdict DIVERGE kept (the ink's own count unchanged).
- THE FIFTEENTH OF AV, THE DECREE CONSUMED (Bava Batra 121a:9-121b:1): the wilderness dying ceased — God spoke to Moses again only after the men of war were consumed (Deut 2:16-17); the tape's timer fired at (40, 5, 9), the dying ceased at (40, 5, 15) by the Shelach runner's row, the census "after the plague" at (40, 6, 1) after both.
- LEVI OUTSIDE, THE EDGES OUTSIDE (Bava Batra 121b:8-11): the decree's "twenty and upward" (14:29) is the census's count — Levi counted from thirty (Rav Hamnuna), the roll's Levites apart with their own threshold; under twenty and over sixty outside by "and upward" / "and upward" with the valuations (Rav Acha bar Yaakov); Yair and Machir the shelf's survivors (Seder Olam 9:2 with Nobah, Serah and Jochebed on both rolls) — the rows decree_age_edges and wilderness_survivors.
- KORACH'S TWO DEATHS ON ONE VERSE (Sanhedrin 110a:13-14): R. Yochanan reads 26:10 to EXCLUDE Korach from the fire (and 16:32 from the swallowing — the plague), the baraita reads 26:10 "with Korach" to INCLUDE him in both — the reading's PN26A-03 ("one verse, both deaths") is the second arm's ink; the Korach runner's row korach_death_mode (CK4 OPEN) read by call; "this is Dathan and Abiram" the same from beginning to end (Megillah 11a:17).
- THE PLURAL FOR ONE SON (Bava Batra 143b:5-7): "the sons of Pallu: Eliab" (26:8) proves 'sons' for one (Rava); a grandson is not a son (Mar bar Rav Ashi) — the roll's own Ard and Naaman under Bela (26:40) where Genesis 46:21 lists them as Benjamin's: the reading's "two moved a generation" is the Talmud's question.
- SERAH ON BOTH ROLLS (Sotah 13a:14; Seder Olam 9:2): the daughter of Asher who remained from the descent's generation showed Moses Joseph's grave — the reading's three rosters (Gen 46:17, Num 26:46, 1 Chr 7:30) with the predicate's two named exceptions beside Caleb and Joshua.
- JOSEPH'S DOUBLE ON THE CENSUS'S FACE (Bava Batra 123a:4-5, 10): the birthright to Joseph's sons (1 Chr 5:1-2) = two full portions ("Ephraim and Manasseh as Reuben and Simeon", Gen 48:5) — the roll counts Joseph's two as tribes among the twelve, Manasseh FIRST here against Ephraim first at 1:32, while Levi stands apart; and 26:5's "Reuben the firstborn" kept plene against the Chronicler's transfer.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_census2_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG))
