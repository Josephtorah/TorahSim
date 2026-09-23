#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b — THE COMPILE OF CHAPTER 15 (2026-09-23; the docket THREE RUNS under THE COST RULES' ~700 clause — D1 the small works on the owner's "Go"
# after the compaction at #207, D2a Kiddushin 14b-22b on his "Reread go" after the compaction at #207 addendum 1, D2b Bekhorot 25a-28b on his "Continue" at 276.4k without
# a compaction): THE EXAM DOCKET for Deuteronomy 15:1-23, written from the scan's dump (scratchpad/ch15_docket_dump.txt: the LINK rows = every Babylonian Talmud /
# Mishnah / Tosefta segment on the local shelf citing a verse of the chapter; the TOPIC rows = the forty-six Mishnah rows, the eleven folio ranges and the four Tosefta
# chapters of the 13b design's exam, read WHOLE; the CREDITED marks = addresses already verdicted in an earlier ledger — CARRIED here with that ledger's own verdict line
# by ch15_credit_carry.py, or read whole here where the ledger's form carried no verdict — the shared file ch15_docket_U.py). Every address in the dump gets ONE verdict
# (the parts A..I on disk, each a SPEC over the dump's own addresses); the coverage is COMPUTED from the dump, never typed; the ranges' sizes are read from the scan's own
# print (ch15_docket_scan.out). Append-only. 12b's form (write_ch14_docket.py): every row read WHOLE.
import re, os, sys, importlib.util, subprocess
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT
SCR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SCR)
OUT = f'{ROOT}/logic/oral_triage/deu_15_reeh_exam_2026-09-23.md'
assert not os.path.exists(OUT), OUT
dump = open(f'{SCR}/ch15_docket_dump.txt', encoding='utf-8').read()
rows = re.findall(r'^## \[(LINK|TOPIC)\] (.+?)  (.*)$', dump, re.M)
ADDR, CRED = [], {}
for k, a, rest in rows:
    m = re.search(r'\{CREDITED: (.*?)\}', rest)
    if m: CRED[a.strip()] = m.group(1)
    ADDR.append((k, a.strip(), re.sub(r'\s*\{CREDITED:.*?\}', '', rest).strip()))
NL = sum(1 for k, _, _ in ADDR if k == 'LINK'); NT = len(ADDR) - NL
hdr_line = dump.split('\n', 1)[0]
assert hdr_line == 'ROWS %d LINK %d TOPIC %d CREDITED %d' % (len(ADDR), NL, NT, len(CRED)), (hdr_line, len(ADDR), NL, NT, len(CRED))
_seen = set(); _dedup = []; DUPS = []
for _k, _a, _vs in ADDR:
    if _a in _seen: DUPS.append(_a); continue
    _seen.add(_a); _dedup.append((_k, _a, _vs))
NDUP = len(ADDR) - len(_dedup); ADDR = _dedup; NT = len(ADDR) - NL   # an address listed twice in the dump (a link row inside a chapter read whole) is taken once — computed
from ch15_credited_rows import UNRESOLVED as UNRES   # the credited rows the carry could not resolve (read whole here)
from ch15_docket_crowns import crowns_d1, crowns_d2a, crowns_d2b
V = {}; STATS = []
for p in 'ABCDEFGHI':
    part = f'ch15_docket_{p}'
    spec = importlib.util.spec_from_file_location(part, f'{SCR}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    STATS.append(m.WHOLE_STATS)
    for addr, verdict, note in m.ROWS:
        if addr in V: assert V[addr] == (verdict, note), ('duplicate verdict differs', addr); continue
        assert verdict in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE'), (addr, verdict)
        V[addr] = (verdict, note)
missing = [a for _, a, _ in ADDR if a not in V]; extra = [a for a in V if a not in {x[1] for x in ADDR}]
if missing or extra:
    print('MISSING', len(missing), missing); print('EXTRA', len(extra), extra); sys.exit(1)
cnt = Counter(vd for vd, _ in V.values())
cnt_link = Counter(V[a][0] for k, a, _ in ADDR if k == 'LINK'); cnt_topic = Counter(V[a][0] for k, a, _ in ADDR if k == 'TOPIC')
works = Counter(a.rsplit(' ', 1)[0] for k, a, _ in ADDR if k == 'LINK')
scan = open(f'{SCR}/ch15_docket_scan.out', encoding='utf-8').read()
scan_r = scan[scan.index('THE RANGES SIZED:'):]
LONG = [(f'{w.replace("_", " ")} {a}-{z}', int(s), int(l)) for w, a, z, s, l in re.findall(r'^  (\S+)\s+(\d+[ab])-(\d+[ab])\s+(\d+) rows,\s+(\d+) link rows', scan_r, re.M)]   # read from the scan's print
assert len(LONG) == 11, ('the design names eleven folio ranges', len(LONG), LONG)
MISH = [a for k, a, _ in ADDR if k == 'TOPIC' and not re.search(r'\d+[ab]:\d+$', a)]   # the Mishnah and Tosefta rows among the topic rows
assert sum(s - l for _, s, l in LONG) + len(MISH) == NT, (sum(s - l for _, s, l in LONG), len(MISH), NT)   # every range read WHOLE
ncred_link = sum(1 for k, a, _ in ADDR if k == 'LINK' and a in CRED); ncred_topic = sum(1 for k, a, _ in ADDR if k == 'TOPIC' and a in CRED)
verses = Counter(h for k, _, vs in ADDR if k == 'LINK' for h in re.findall(r'Deut 15:\d+', vs)); assert verses, 'no verse hits parsed from the LINK headers'
UNCITED = [v for v in range(1, 24) if f'Deut 15:{v}' not in verses]   # computed, never typed
LAWCELLS = Counter(m.group(1) for vd, note in V.values() if vd == 'LAW' and not note.startswith('CREDITED (') for m in [re.search(r'\b(F[1-7])\b', note)] if m)   # this docket's own notes
NCARRIED = sum(1 for vd, note in V.values() if note.startswith('CREDITED (') and '; carried) — ' in note[:200]); NREADHERE = len(ADDR) - NCARRIED
TOT = {k: sum(s[k] for s in STATS) for k in STATS[0]}; assert TOT['rows'] == len(ADDR), (TOT, len(ADDR))   # the parts partition the UNIQUE addresses (the split by address)
NWHOLE = sum(1 for vd, note in V.values() if '[whole:' in note and '; carried) — ' not in note[:200]); assert NWHOLE == TOT['corrected'] == 0, (NWHOLE, TOT); assert NCARRIED == len(CRED) - len(UNRES), (NCARRIED, len(CRED), len(UNRES))
NOUT = Counter(a.rsplit(' ', 1)[0] for a, (vd, _) in V.items() if vd == 'OUTSIDE')
hdr = (f'''# THE EXAM DOCKET — Deuteronomy 15:1-23 (the release — at the end of every seven years you shall make a release, every creditor shall release what he lent to his neighbor, he shall not exact it of his neighbor and his brother because the LORD's release has been proclaimed, of the foreigner you may exact; the needy and the blessing — there shall be no needy among you, for the LORD will surely bless you in the land if only you diligently hearken, you shall lend to many nations and not borrow, rule over many nations and they shall not rule over you; the hand opened — if there is among you a needy man of your brothers you shall not harden your heart nor shut your hand, open, you shall open your hand and lend him sufficient for his need, beware lest there be a base thought in your heart saying the seventh year, the year of release, draws near, give, you shall give and your heart shall not be grieved, the needy shall never cease out of the land; the Hebrew slave — if your brother, a Hebrew man or a Hebrew woman, is sold to you he shall serve six years and in the seventh you shall send him free, you shall not send him away empty, furnish, you shall furnish him from your flock, your threshing floor and your winepress, remember that you were a slave in Egypt and the LORD redeemed you; the awl and the double hire — if he says I will not go out from you because he loves you and your house, take the awl and put it through his ear and into the door and he shall be your servant for ever, likewise to your maidservant, it shall not seem hard when you send him free for double the hire of a hireling he served you six years; the firstling — every firstling male born of your herd and of your flock you shall sanctify to the LORD, you shall do no work with the firstling of your ox nor shear the firstling of your flock, before the LORD you shall eat it year by year in the place He will choose, you and your household; the blemish and the blood — if it has a blemish, lame or blind, any ill blemish, you shall not sacrifice it, within your gates you shall eat it, the unclean and the clean alike, as the gazelle and as the hart, only its blood you shall not eat, on the earth you shall pour it as water) — THE DEUTERONOMY WALK sitting 13b, THE DOCKET IN THREE RUNS (2026-09-23; DEUTERONOMY_WALK.md "Sitting 13b — THE COMPILE OF CHAPTER 15 … THE DESIGN", THE ORDER; its "THE DOCKET — AS RUN (D1)", "(D2a)" and "(D2b)" paragraphs)
# DECLARED: the exam docket is the UNION (the standing rule of 2026-09-05) of (1) THE LINK-DRIVEN ROWS — every segment of the local shelf's Babylonian Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 15 (the scan ch15_docket_scan.py: {NL} rows in {len(works)} works) — and (2) THE TOPIC ROWS BY ADDRESS, the 13b design's exam sized by the scan and read WHOLE: the forty-six Mishnah rows (Sheviit 10 whole; Kiddushin 1:2-3; Peah 8:7-9; Bekhorot 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6 and 6 whole; Temurah 3:5; Arakhin 8:7; Shekalim 5:6; Chullin 2:9 — the link rows among them listed there); the eleven folio ranges {", ".join(n for n, _, _ in LONG)}; Tosefta Sheviit 8, Tosefta Kiddushin 1, Tosefta Bekhorot 1 and 2 WHOLE (the dict-text export read under its empty key). {len(CRED)} addresses CREDITED (read whole at an earlier sitting — chapter 14's docket the largest, the Exodus triage, chapter 12's docket, the priesthood docket, the Korach exam, the persons ledger, the sheviit docket, the ordinances docket, chapter 13's docket, the calendar blocks, the Genesis triage, the erection, family, backfill and code-hunt ledgers): {NCARRIED} CARRIED here with their ledgers' own verdict lines (ch15_credit_carry.py — the note begins "CREDITED (<ledger>; carried) —"), {len(UNRES)} whose ledger's form carried no verdict READ WHOLE HERE (the note names the ledger and says so — the shared file ch15_docket_U.py, filled across the three runs).
# THE TALMUD ADDRESSING: the export's index 0 is folio 1a (a page = index // 2 + 1; measured 2026-09-09); the Mishnah and the Tosefta by chapter:paragraph. An address listed twice in the dump (a link row inside a chapter read whole) is taken once with the same verdict at both ({NDUP} dropped, computed — {", ".join(DUPS)}, a link row and the chapter's row).
# READ WHOLE (THE WHOLE-ROW RULE, owner-ruled 2026-09-17 — "never ever cut corners with the Talmud"): every uncredited row was printed WHOLE (ch15_docket_uncred.py — the D1 series ch15_uncred_d1_00.txt to ch15_uncred_d1_03.txt; ch15_docket_uncred_d2.py — the D2 series RE-CHUNKED BY WORK: ch15_uncred_d2k_00.txt to ch15_uncred_d2k_02.txt for Kiddushin 14b-22b, ch15_uncred_d2b_00.txt and ch15_uncred_d2b_01.txt for Bekhorot 25a-28b; every chunk at most 64,000 bytes, one Read page; the unresolved credited rows ch15_uncred_unres_d1.txt, ch15_uncred_unres_d2k.txt and ch15_uncred_unres_d2b.txt, each line led by its dump index) and read entire before its verdict was typed — no cut, no overlay; the parts' WHOLE dicts empty, apply_whole's counts computed: {TOT["corrected"]} of {TOT["rows"]} rows corrected ({TOT["verdicts_changed"]} verdicts, {TOT["notes_changed"]} notes); {NREADHERE} rows read whole in the docket's THREE runs (D1 THE SMALL WORKS — every address outside the two long ranges, the split computed by address: A the link rows of the twenty-seven other works, B the Mishnah and the Tosefta rows, C Gittin 36a-37b and Arakhin 32b-33a, D Makkot 3b and Rosh Hashanah 8b-9a, E Bava Metzia 31b, 71a and Ketubot 67b, F Bekhorot 33a-37b and 53b; D2a KIDDUSHIN 14b-22b WHOLE with its own link rows — G the folios 14b-17b, H the folios 18a-22b, the clean point after it taken unconditionally; D2b BEKHOROT 25a-28b WHOLE with its own link rows — I; the unresolved rows in the shared file).
# THE VERDICTS: LAW names the cell of cold_run_release_firstborn.py (F1 the_release, F2 the_needy_and_the_blessing, F3 the_hand_opened, F4 the_hebrew_slave, F5 the_awl_and_the_double_hire, F6 the_firstling, F7 the_blemish_and_the_blood; the_readback the table) or the callee's cell by CALL; DERIVATION a hook from the verse to a rule; DISPUTE a parameter row with two arms; CONTEXT; OUTSIDE a declared range's matter on another subject. The link census: LAW {cnt_link.get("LAW", 0)} / DERIVATION {cnt_link.get("DERIVATION", 0)} / DISPUTE {cnt_link.get("DISPUTE", 0)} / CONTEXT {cnt_link.get("CONTEXT", 0)} / OUTSIDE {cnt_link.get("OUTSIDE", 0)}; the topic census: LAW {cnt_topic.get("LAW", 0)} / DERIVATION {cnt_topic.get("DERIVATION", 0)} / DISPUTE {cnt_topic.get("DISPUTE", 0)} / CONTEXT {cnt_topic.get("CONTEXT", 0)} / OUTSIDE {cnt_topic.get("OUTSIDE", 0)}; LAW by cell, this docket's own notes {dict(sorted(LAWCELLS.items()))}. The verses cited by the link rows: {", ".join(f"{v} ({n})" for v, n in sorted(verses.items(), key=lambda kv: int(kv[0].split(":")[1])))}; UNCITED by any row: {UNCITED}.
''')
body = ''
last = None
for k, a, vs in ADDR:
    work = a.rsplit(' ', 1)[0]
    if work != last:
        body += f'\n## {work}\n'; last = work
    vd, note = V[a]
    body += f'- {a} [{k}{(" — " + vs) if vs else ""}{(" — CREDITED: " + CRED[a]) if a in CRED else ""}] — {vd}. {note}\n'
crowns = '\n## The finds (this docket\'s crowns — the three runs)\n' + crowns_d1 + crowns_d2a + crowns_d2b
cite = '\n## CITE INDEX — every segment opened, each fully named\n(coverage COMPUTED by write_ch15_docket.py against the scan\'s dump: %d addresses, every one verdicted — missing 0, extra 0)\n' % len(ADDR)
cite += '\n'.join(a for _, a, _ in ADDR) + '\n'
tail = (f'\n**read: {len(ADDR)} of {len(ADDR)} — COMPLETE** (the link-driven rows {NL}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_link.items()))}; '
        f'the topic windows {NT}: {", ".join(f"{k} {n}" for k, n in sorted(cnt_topic.items()))}; all rows: {", ".join(f"{k} {n}" for k, n in sorted(cnt.items()))}; credited {len(CRED)} — {NCARRIED} carried with their ledgers\' own verdict lines and {len(UNRES)} read whole here; {NREADHERE} rows read whole in the three runs — the counts this script computed from the dump and the verdict lists, never typed; corrections {TOT["corrected"]}; the ranges: {"; ".join(f"{n} {s} rows ({l} link)" for n, s, l in LONG)}; the Mishnah and Tosefta rows {len(MISH)}; OUTSIDE by work: {dict(NOUT)}.)\n')
assert not re.search(r'[֐-׿]', hdr + crowns), 'no Hebrew script typed in the header or the crowns'
open(OUT, 'w', encoding='utf-8').write(hdr + body + crowns + cite + tail)
print('WROTE', OUT, os.path.getsize(OUT), 'bytes')
print('rows', len(ADDR), 'link', NL, 'topic', NT, 'credited', len(CRED), '(link', ncred_link, 'topic', ncred_topic, ')', 'carried', NCARRIED, 'unresolved_read_here', len(UNRES), 'read_here', NREADHERE, 'dup_dropped', NDUP, DUPS)
print('verdicts', dict(sorted(cnt.items())), 'link', dict(sorted(cnt_link.items())), 'topic', dict(sorted(cnt_topic.items())))
print('LAW by cell', dict(sorted(LAWCELLS.items())))
print('OUTSIDE by work', dict(NOUT))
print('verses cited', sorted(verses.items(), key=lambda kv: int(kv[0].split(':')[1])), 'UNCITED', UNCITED)
print('ranges', [(n, s, l) for n, s, l in LONG]); print('mishnah+tosefta rows', len(MISH))
