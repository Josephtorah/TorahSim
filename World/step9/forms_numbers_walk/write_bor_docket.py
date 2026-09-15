import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 14b — THE COMPILE OF THE BORDERS (2026-09-13): THE EXAM DOCKET for Numbers 34:1-29, written from the scan's dump
# (scratchpad/bor_docket_dump.txt: the LINK rows = every Babylonian Talmud / Mishnah / Tosefta segment on the local shelf citing a verse of the
# span; the TOPIC rows = Mishnah Gittin 1:1-2, Mishnah Sheviit 6:1 and 9:2, the four folio ranges of COMPILE_DEBT's sitting-14 box (h) read WHOLE,
# and the Tosefta Sheviit's boundary rows — the union rule of 2026-09-05; the CREDITED marks = addresses already verdicted in an earlier ledger,
# given their quick look here). Every address in the dump gets ONE verdict (parts A..D); the coverage is COMPUTED from the dump, never typed; the
# ranges' sizes are read from the scan's own print (bor_docket_scan.out). Append-only. write_jou_docket.py's form.
import re, os, sys, importlib.util
from collections import Counter
ROOT = _ROOT
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = f'{ROOT}/logic/oral_triage/num_34_borders_exam_2026-09-13.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/bor_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
assert len(ADDR) == 171 and NL == 6 and len(CRED) == 118, (len(ADDR), NL, len(CRED))
V = {}
for p in 'ABCD':
    part = f'bor_docket_{p}'
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
assert len(works) == 4, len(works)
scan = open(f'{SCR}/bor_docket_scan.out', encoding='utf-8').read()
scan = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) segments,\s+(\d+) link rows', scan, re.M)]   # read from the scan's print
assert len(LONG) == 4, len(LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Mishnah')]
TOS = [a for k, a, _ in ADDR if k == 'TOPIC' and a.startswith('Tosefta')]
assert len(MISH) == 4 and len(TOS) == 2, (MISH, TOS)
assert sum(s - l for _, s, l in LONG) + len(MISH) + len(TOS) == NT, (sum(s - l for _, s, l in LONG), len(MISH), len(TOS), NT)   # every range read WHOLE
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in vs.split())
hdr = (f'# THE EXAM DOCKET — Numbers 34:1-29 (the borders: the land that shall fall by its borders, the four sides, Moses\' restatement to the nine and a half, the dividers named — Eleazar, Joshua and one prince from a tribe — and the roster), THE NUMBERS WALK sitting 14b, the compile (2026-09-13; the owner: "Go" after the #155 rereads, on 1b\'s order — the measurements, the design, the probes (none owed), the docket, the types, the runner; the design World/step9/NUMBERS_WALK.md "Sitting 14b").\n'
       f'# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf\'s Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Numbers 34:1-29 (the scan by script over Data/sefaria_export, commentaries excluded: {NL} rows in {len(works)} works — ' + ', '.join(f'{w} {n}' for w, n in works.most_common()) + '; the verses cited ' + ', '.join(f'{v} {n}' for v, n in verses.most_common()) + f' — the dividers\' verse 34:18 the most), and (2) THE TOPIC-ROUTED ROWS — Mishnah Gittin 1:1-2 (the borders for the bills\' law — Rekem, Ashkelon, Akko), Mishnah Sheviit 6:1 and 9:2 (the three lands), the four folio ranges of COMPILE_DEBT\'s sitting-14 box (h) read WHOLE with the link rows dropped — ' + '; '.join(f'{r} {s} segments ({l} link rows)' for r, s, l in LONG) + f' — and the Tosefta Sheviit\'s boundary rows ({len(TOS)}, found LOCAL — 4:4 the land for the sabbatical law, 4:12 the imports): {NT} topic rows. {len(CRED)} addresses already verdicted in earlier ledgers are marked CREDITED with their ledger and given a QUICK LOOK here (speed ruling (b), credit guard (1)) — {ncred_link} link rows, {ncred_topic} topic rows; Bava Batra 117a-122a whole is the second census\'s, the inheritance\'s, Gad and Reuben\'s and the journeys\' dockets\', read there and looked at here for the dividers (122a:4-6 the lottery\'s picture and 122a:12 "only" excludes Joshua and Caleb READ WHOLE for this chapter). Every address gets ONE verdict: LAW (a rule the runner must reproduce — the cell named: F1 the_land_and_its_fall, F2 the_four_sides, F3 moses_restatement, F4 the_dividers, F5 the_roster, or the callee\'s cell by CALL), DERIVATION (a hook from the verse to a rule — a labeled move), DISPUTE (a parameter row — a DATA row named), CONTEXT, OUTSIDE (the export\'s empty or editorial row). Terse for the non-material (speed ruling (c)). The Sifrei on Numbers has no row on the chapter (the reading); the Tosefta Terumot 2:12 is quoted inside Gittin 8a:4 and not opened apart.\n'
       f'# THE TALMUD ADDRESSING: the export\'s index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah by chapter:mishnah; the Tosefta by chapter:segment.\n')
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
- THE LOTTERY'S PICTURE IS THE DIVIDERS AT WORK (Bava Batra 122a:4-6, credited and read whole here): Eleazar the High Priest dressed with the Urim, Joshua and all Israel standing before him, two receptacles — the names of the tribes and THE BOUNDARIES OF THE TWELVE REGIONS — and the lot of the tribe emerging with the lot of its boundary: the two men 34:17 names at the lot with the chapter's one border cut into twelve; Sanhedrin 16a:3 names the same three instruments (the lots, the Urim, all Israel) as what the first division needed and a later border dispute does not; and the boundary the shelf gives Naphtali is GINNOSAR — the word the translation gives 34:11's sea ("the sea of Gennesar", Onkelos's one seat), the region named by the chapter's east point in the translation's tongue.
- THE SEA AS A BORDER, TWO WAYS (Gittin 8a:4-7 on 34:6): Rabbi Yehuda reads "and its border" as the sea itself within the land — every place directly across; the Rabbis draw A STRING from Turei Amnon in the north to the River of Egypt in the south and count the islands inside it — the west drawn as a line between the ink's own two corners (the north's mountain, the south's brook), the Tosefta's picture; one word of 34:6 read two ways.
- THE JORDAN AS A BORDER, TWO WAYS (Bekhorot 55a:10 on 34:12; 55a:14 on 34:15): "by its borders round about" makes all the land one border with the tribes' demarcations inside it; Rabbi Shimon ben Yochai reads "beyond the Jordan AT JERICHO" — as Jericho is Canaan's, the river is Canaan's: the reading's inclusio (34:2, 34:12) and its "at Jericho" pair (22:1, 34:15) each carried as a rule on the shelf.
- THE LAW OF AGENCY ASKED OF 34:18 AND ANSWERED WITH THE STEWARD (Kiddushin 42a:6-8): Rav Giddel's "one prince from each tribe you shall take" as the founding of agency — refused, since minors have no agency and the princes divided for them; the verse kept for Rava bar Rav Huna's rule that the court appoints a steward for orphans "to their disadvantage and to their benefit" — the dividers a court acting for those who cannot act, the class the daughters' holding on the tape already carries (its counterparty the court; paid before Eleazar and Joshua at Joshua 17:4).
- THE CHAPTER'S HEADING AS A TITLE CLAIM (Sanhedrin 91a:6): the people of Afrikiya claim the land from 34:2's "the land of Canaan" — Canaan their forefather named in the deed; the tape's answer is canaan's status since Genesis 9:25 (a slave's acquisitions are his master's), the reading's find that the article stands on "the land" and not on "Canaan" the shelf's litigants' handle.
- THE SHELF'S OWN BORDER POINTS AND THE TRANSLATION'S NAME (Mishnah Gittin 1:2; Sheviit 6:1; Tosefta Sheviit 4:4): for the bills' law Rabbi Yehuda draws the east at REKEM, the south at Ashkelon, the north at Akko — and Rekem is the translation's name for 34:4's Kadesh-barnea ("Rekem Geah", Onkelos at both Numbers seats): the ink's south-east corner is the Mishnah's east; for the sabbatical law the three lands are two holdings' lines inside 34's one border (those who came up from Babylon, those who came up from Egypt — Chezib, the river, Amanah), the Tosefta's "two lands" from the river north of Achziv to Ammon and Moab and the land of Egypt.
- THE BORDERS' LEGAL REACH (Mishnah Kiddushin 36b:8; 37a:3-6): a commandment dependent on the land applies inside the border only, an obligation of the body everywhere — the classing taught from Deuteronomy 12:1-2's adjacent verses (the idolatry's ban the exemplar): the rule the chapter's border serves, a DATA row the_land_bound_rule added at the docket, its classing Deuteronomy's — the readback's.
- THE SEVENTY-ONE AT THE FIRST DIVISION (Sanhedrin 16a:2-3): Ulla's likeness — a border dispute between two tribes before the Great Sanhedrin as the first division was by seventy-one elders — refused because the first division also needed the lots, the Urim and all Israel; and 16a:16-17 reads Joshua's commission verse (27:21 — "he shall stand before Eleazar the priest") for the king's war: the same pair, Eleazar and Joshua, at the seat the chapter's dividers repeat — Numbers 27:12-23 uncompiled, the row carried to that debt.
- "ONLY" EXCLUDES JOSHUA AND CALEB (Bava Batra 122a:12, read whole here): the two dividers took their own portions NOT BY THE LOT they administer — Joshua by the LORD's word at Timnath-serah (Joshua 19:50), Caleb by Moses' oath at Hebron (Joshua 14:13 — the holding owed on the tape since 14:24); and Joshua 17:14-18 (118a:4) shows a divider answering a tribe's claim — the commanded debit's runs.
'''
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_bor_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — the counts this script computed from the dump and the verdict lists, never typed)\n')
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, len(ADDR), 'rows;', dict(cnt), '; link', dict(cnt_link), '; topic', dict(cnt_topic), '; credited', len(CRED), '; long ranges', len(LONG))
