#!/usr/bin/env python3
# THE NUMBERS WALK 5b — THE COMPILE OF KORACH (2026-09-10): THE EXAM DOCKET for Numbers 16:1-18:32, written from the scan's dump
# (scratchpad/korach_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a
# verse of the span; the TOPIC rows = the Mishnah's rows the three reading ledgers and the debt line name BY ADDRESS — the union rule of
# 2026-09-05; the CREDITED marks = addresses already verdicted in an earlier ledger, given their quick look here). Every address in the
# dump gets ONE verdict (parts A, B, C, D); the coverage is COMPUTED from the dump, never typed; the long ranges' sizes are read from the
# scan's own print. Append-only once written.
import re, os, sys, importlib.util
from collections import Counter
ROOT = '<repo-old>'
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_16_18_korach_exam_2026-09-10.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/korach_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
assert len(ADDR) == 316 and sum(1 for k, _, _ in ADDR if k == 'LINK') == 209 and len(CRED) == 94, (len(ADDR), len(CRED))
V = {}
for part in ('korach_docket_A', 'korach_docket_B', 'korach_docket_C', 'korach_docket_D'):
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
scan = open(f'{SCR}/korach_scan1.out', encoding='utf-8').read()
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 33, len(LONG)
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
hdr = (f'# THE EXAM DOCKET — Numbers 16:1-18:32 (Korach), THE NUMBERS WALK sitting 5b, the compile (2026-09-10; the owner: "Go" after the #125 rereads, on the ruling READ THEN COMPILE; the design World/step9/NUMBERS_WALK.md "Sitting 5b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of the span (the scan by script over Data/sefaria_export, commentaries excluded: {sum(1 for k, _, _ in ADDR if k == "LINK")} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + f'); and (2) THE TOPIC ROWS BY ADDRESS — the Mishnah chapters and mishnayot the three reading ledgers\' TESTING SHELF lines and the COMPILE_DEBT line name (Bekhorot 1, 4, 8; Zevachim 5:8; Terumot 1, 2, 4; Ma\'aserot 1; Ma\'aser Sheni 5; Challah 1:9, 4:9; Arakhin 8:6-7; Ketubot 5:2-3; Yoma 2; Sanhedrin 9:6, 10:3; Middot 1, 5:4; Avot 4:13, 5:6, 5:17; Tamid 1:1-2), {sum(1 for k, _, _ in ADDR if k == "TOPIC")} rows after the link-duplicates were dropped. Every row read whole and given ONE verdict: LAW (a rule the compiled function must answer — the CELL named), DERIVATION (a hook from the verse to a rule), DISPUTE (a parameter row), CONTEXT, OUTSIDE. THE CREDITED ROWS: {len(CRED)} addresses ({ncred_link} link, {ncred_topic} topic) were already verdicted in an earlier logic/oral_triage ledger (the scan\'s prior-read pass, this sitting\'s three reading ledgers excluded) — speed ruling (b) with credit guard (1): each got a QUICK LOOK here and the same one verdict, its earlier ledger named on the row.\n'
       f'# THE LONG TALMUD RANGES the ledgers name ("the tractate is the exam") enter through the link rows; their remainder is OUTSIDE DECLARED SCOPE, enumerated by count, never silently narrowed: ' + '; '.join(f'{n} ({s} segments, {l} of them link rows read here, {s - l} outside)' for n, s, l in LONG) + '. The Sifrei on Numbers is SILENT on chapters 16-17 and read on 18 at sitting 5 (its rows in the reading ledger); Numbers Rabbah and the twenty-three commentary directories on Numbers OUTSIDE DECLARED SCOPE (the ledgers\' lists).\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah.\n\n')
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
- KORACH'S DEATH ARGUED ON THE SHELF (Sanhedrin 110a:13-14): R. Yochanan reads 16:32 "all the men who were with Korach" as NOT Korach, and 26:10's "two hundred and fifty men" as not him either — he died in the plague; the baraita (the outside teaching) reads 26:10 "swallowed them WITH Korach" and 16:35's fire — both. The ink's silence at 16:32 (sitting 5's crown) is the tradition's own open question: the tape's put_to_death on Korach carries the OPEN row korach_death_mode with the two shelf arms.
- THE TRANSLATION LOAD-BEARING, AGAIN (Zevachim 91a:19; Chullin 132b:14; Sotah 15a:5; Zevachim 28a:10): the priests may eat their gifts as they choose because 18:8's "for anointing" is rendered "for GREATNESS" — the Talmud cites Onkelos (the Aramaic translation) by name as the ground; the reading had cut the word from the shelf's bytes.
- THE DECREE OVER THE A-FORTIORI ON THE ANSWER SHEET (Mishnah Ketubot 5:3; Sifrei 117:2): the betrothed daughter of an Israelite eats terumah (the priests' portion) by the ink's argument, and "a court that convened after them said: not until she enters the canopy" — the parameter row betrothed_eats with the Torah arm and the decree arm.
- THE STRANGER'S DEATH BY TWO IDENTITIES (Sanhedrin 83b:4, 84a:13; Mishnah Sanhedrin 9:6): 18:7 "shall be put to death" / 17:28 "shall die" — R. Yishmael: death by Heaven; R. Akiva: strangulation — the row zar_who_served that Bamidbar's compile already carries at 1:51 is the same row at its fourth seat: read by CALL, never a second row.
- THE TITHE OF THE TITHE IS ONE IN A HUNDRED (Menachot 54b:11; Beitzah 13b:3-7; Berakhot 47a:15; Pesachim 35b; Eruvin 31b; Shabbat 127b): the Levite's terumah is a tenth of the tenth — the cell's arithmetic — and THE LEVITE WHO PRECEDED THE PRIEST on the stalks owes the tithe's terumah only, after the pile the great terumah too ("a tenth part of the tithe" against "from ALL that is given you"): six seats, one rule, the pile the threshold the answer sheet sets at Ma'aserot 1:6.
- BY ESTIMATE AND BY THOUGHT (Beitzah 13b:3; Bekhorot 58b:11, 59a:1; Menachot 54b:11; Gittin 30b:13; Mishnah Terumot 1:7, 4:6): Abba Elazar ben Gomel's "YOUR terumah" (plural) equates the two terumot — Sifrei 121:1's own row at five Talmud seats; and the tithe called "terumah" at 18:24 carries the estimate to the tithes and the animal tithe.
- THE COAL PANS ELEVATED (Menachot 99a:11): "one elevates in sanctity" derived from 17:3 — the censers, service vessels, became the altar's own covering: the tape's altar_plated write has its rule.
- THE COURT'S SUMMONS READ OFF THE CHAPTER (Moed Katan 16a:3-5): the agent sent (16:12), the defendant in person, before a great man, both parties named, a date set — "tomorrow" (16:16), the report of disrespect permitted (16:14): a procedure compiled from the rebellion's verbs.
- THE FIRSTBORN'S WINDOW BY JUXTAPOSITION (Bekhorot 27b:7, 28a:2; Zevachim 57a:5-13; Temurah 21b:13; Mishnah Zevachim 5:8): "as the breast of waving and the right thigh" — two days and a night; the second "it shall be yours" the second day (R. Akiva against R. Yosei HaGelili's thanks offering); the blood ONE PLACEMENT on the base (Zevachim 56b:12) — the answer sheet's row for 18:17-18.
- THE STAFF BESIDE THE ARK (Horayot 12a:1-3; Keritot 5b:16-20; Yoma 52b:15): "for safekeeping" / "for safekeeping" — the staff with its almonds and blossoms sequestered with the ark, the jar and the oil (Josiah): the reading's manna-jar formula is the shelf's own verbal analogy.
- A CONGREGATION IS TEN, FROM KORACH (Berakhot 21b:5; Megillah 23b:7; Sanhedrin 74b:3): "from among this congregation" (16:21) — the quorum's source runs through this chapter to the spies' (14:27).
- THE SEQUENCE'S OWN HOMOGRAPH CLASS (the docket's rows on 18:12, 18:29-30 — Bekhorot 53b:17, 54b:2; Temurah 5a:11): "the best of the oil, the best of the wine" — kind for kind, each type its own first — the Mishnah Terumot 2:4 row that the reading's reversed triad (oil, wine, grain) sits on.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_korach_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {sum(1 for k, _, _ in ADDR if k == "LINK")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {sum(1 for k, _, _ in ADDR if k == "TOPIC")}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts the script\'s own Counter measured)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('wrote', OUT, '| rows', len(ADDR), dict(cnt), '| link', dict(cnt_link), '| topic', dict(cnt_topic), '| credited', len(CRED))
