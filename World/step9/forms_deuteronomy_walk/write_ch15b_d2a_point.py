#!/usr/bin/env python3
# 13b docket D2a — THE CLEAN POINT'S RECORDS (write_ch15b_d1_point.py's form): the parts G, H re-checked as a partition of Kiddushin 14b-22b, the census COMPUTED (never typed),
# the re-chunker's counts READ FROM ITS PRINT, the timing rows read from the tsv; then, with every text built first and the caps asserted: the map's "THE DOCKET — AS RUN (D2a)"
# paragraph appended (no Hebrew script — the map's lint 0), the state doc's "#207 ADDENDUM 2" appended, the recovery page's section-2 lines rewritten in place (<= 10,240 bytes),
# MEMORY.md's walk line (<= 17,000), the memory's deuteronomy-walk.md line appended; the D2a instruments copied to the forms folder.
import os, re, sys, importlib.util, subprocess, shutil
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
from ch15_docket_common import D2_UNIQUE, KIND_FIRST, long_range
from ch15_docket_crowns import crowns_d1, crowns_d2a
RANGE = 'Kiddushin 14b-22b'; TARGET = [a for a in D2_UNIQUE if long_range(a) == RANGE]; NB = sum(1 for a in D2_UNIQUE if long_range(a) == 'Bekhorot 25a-28b')
V = {}; per = {}
for p in 'GH':
    part = f'ch15_docket_{p}'; spec = importlib.util.spec_from_file_location(part, f'{SP}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    per[p] = len(m.ROWS); assert m.WHOLE_STATS['corrected'] == 0
    for a, vd, n in m.ROWS:
        assert a not in V, ('overlap', a, p); V[a] = (vd, n)
assert set(V) == set(TARGET) and len(V) == len(TARGET), (len(V), len(TARGET))
N = len(V); NL = sum(1 for a in V if KIND_FIRST[a] == 'LINK'); NT = N - NL
cnt = Counter(vd for vd, _ in V.values()); cl = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'LINK'); ct = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'TOPIC')
carried = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and '; carried) — ' in n[:200]); unres = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and 'read whole here' in n[:400] and '; carried) — ' not in n[:200])
readhere = N - carried; own = N - carried - unres
LAWCELLS = Counter(mm.group(1) for vd, n in V.values() if vd == 'LAW' and not n.startswith('CREDITED (') for mm in [re.search(r'\b(F[1-7])\b', n)] if mm)
NOUT = Counter(a.rsplit(':', 1)[0].split(' ')[1] for a, (vd, _) in V.items() if vd == 'OUTSIDE')
unc = open(f'{SP}/ch15_docket_uncred_d2.out', encoding='utf-8').read()
um = re.search(r'D2 (\d+) uncredited (\d+) \| Kiddushin 14b-22b (\d+) chunks (\d+) \| Bekhorot 25a-28b (\d+) chunks (\d+)', unc); U_D2, U_UNC, K_UNC, K_CH, B_UNC, B_CH = map(int, um.groups())
kchunks = re.findall(r'K (ch15_uncred_d2k_\d+\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', unc); bchunks = re.findall(r'B (ch15_uncred_d2b_\d+\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', unc)
ur = re.search(r'unresolved credited rows D2 (\d+) \| Kiddushin (\d+) (\d+) bytes \| Bekhorot (\d+) (\d+) bytes', unc); UR_D2, UK, UKB, UB, UBB = map(int, ur.groups())
assert U_D2 == len(D2_UNIQUE) and K_UNC == own and UK == unres and len(kchunks) == K_CH and len(bchunks) == B_CH, (U_D2, len(D2_UNIQUE), K_UNC, own, UK, unres)
rows = [l.split('\t') for l in open(f'{SP}/ch15b_timing.tsv', encoding='utf-8').read().splitlines() if '\t13b D2' in l]
TIM = '; '.join(f'{n} {s}s (at {t}, rc {r})' for t, n, s, r in rows)
kchunk_txt = ', '.join(f'{f} rows {a}-{z} ({n} rows, {b} bytes)' for f, a, z, n, b in kchunks); bchunk_txt = ', '.join(f'{f} rows {a}-{z} ({n} rows, {b} bytes)' for f, a, z, n, b in bchunks)
census = (f'{N} addresses of {RANGE} (link {NL}, topic {NT}; no address listed twice): LAW {cnt["LAW"]} / DERIVATION {cnt["DERIVATION"]} / DISPUTE {cnt["DISPUTE"]} / CONTEXT {cnt["CONTEXT"]} / OUTSIDE {cnt["OUTSIDE"]} '
          f'(the link rows {dict(sorted(cl.items()))}; the topic rows {dict(sorted(ct.items()))}); credited {carried + unres} — {carried} CARRIED with their ledgers\' own verdict lines, '
          f'{unres} whose ledger\'s form carried no verdict READ WHOLE HERE (the U file, now {len(m.OWN_U)} rows); {readhere} rows read whole in this run ({own} uncredited); LAW by cell, this docket\'s own notes {dict(sorted(LAWCELLS.items()))}; OUTSIDE by folio {dict(NOUT)}')
DATE = '2026-09-23'
MAP = (f'\nTHE DOCKET — AS RUN (D2a, {DATE}; the owner\'s "Reread go" after the compaction at #207 addendum 1): KIDDUSHIN 14b-22b WHOLE WITH ITS OWN LINK ROWS — the first of the two long '
       f'ranges, THE CLEAN POINT AFTER IT TAKEN UNCONDITIONALLY as the design ruled. THE INSTRUMENT ADDED: the D2 series RE-CHUNKED BY WORK (ch15_docket_uncred_d2.py — the dump-order '
       f'series ch15_uncred_d2_NN.txt mixed the two ranges in one file; the same {U_UNC} uncredited rows printed again whole into one series per range, asserted byte-identical to the old '
       f'series\' rows: {RANGE} {K_UNC} rows in {K_CH} files — {kchunk_txt}; Bekhorot 25a-28b {B_UNC} rows in {B_CH} files — {bchunk_txt}; the unresolved D2 file split the same way — '
       f'Kiddushin {UK} rows, {UKB} bytes; Bekhorot {UB} rows, {UBB} bytes). EVERY ROW OF KIDDUSHIN 14b-22b READ WHOLE (three chunk pages and the unresolved page, one Read each — '
       f'{readhere} rows); the middah codes checked in MIDDOT.md before they were typed (I1, I2, I6; E28 from the preceding; the amplification-restriction named as the rival method, '
       f'no code); THE PARTS G and H on ch15_docket_common.build_set over D2_UNIQUE by long_range and folio (G the folios 14b-17b with the link rows of the dump\'s 56-73 — {per["G"]}; '
       f'H the folios 18a-22b with the link rows 74-78 — {per["H"]}); the shared U file\'s {unres} Kiddushin rows appended (_U_ROWS_D2K; its assert widened to U_RUNS = the runs read so '
       f'far); THE D2 CHECK (ch15_docket_d2_check.py — the D1 checker with the target a long range named on the command line) — the parts a PARTITION of the range, missing 0, extra 0. '
       f'THE CENSUS (computed): {census}. THE EXAM FILE IS WRITTEN ONCE AT D2b\'S END; the parts, the tools and the chunk rosters copied to the forms folder at this point. THE TIMING: '
       f'{TIM}. THE FINDS OF KIDDUSHIN 14b-22b (carried into the exam file\'s "## The finds" after D1\'s):\n{crowns_d2a}')
assert not re.search(r'[֐-׿]', MAP) and '/Users/' not in MAP.replace('/Users/Shared', '') and not re.search(r'[֐-׿]', crowns_d1)
STATE = (f'\n#207 ADDENDUM 2 — THE DOCKET D2a (2026-09-23, THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15; THE DOCKET\'S SECOND RUN, ITS FIRST HALF, on the owner\'s '
         f'"Reread go" after the compaction at #207 addendum 1; A CLEAN COMPACTION POINT — Kiddushin 14b-22b closed, NO BEKHOROT 25a-28b ROW VERDICTED): THE STATE: chapter 15 read, '
         f'frozen, COMMITTED b0eaa56 (not pushed); the design in the map (RUN A); D1 DONE (#207 addendum 1); D2a DONE — {census}; the parts G, H, the U file (86 rows), the re-chunker '
         f'(ch15_docket_uncred_d2.py), the D2 checker and the crowns\' second paragraph in the scratchpad AND copied to World/step9/forms_deuteronomy_walk/; the map\'s "THE DOCKET — AS '
         f'RUN (D2a)" paragraph appended to the 13b section (its finds inside); NO exam file yet (written once at D2b\'s end — the parts hold the verdicts). THE TIMING: {TIM}. NOT '
         f'COMMITTED (since b0eaa56): the commit\'s own records, the design, #207 with its addenda and notes, the recovery page\'s and the memory\'s lines, the forms. NOTHING MID-FLIGHT. '
         f'NEXT ON HIS WORD (after a compaction: "Reread", then "Go"): D2b — Bekhorot 25a-28b WHOLE ({NB} addresses with their link rows; the chunk files ch15_uncred_d2b_00.txt and '
         f'ch15_uncred_d2b_01.txt in the scratchpad, {B_UNC} rows; the unresolved file ch15_uncred_unres_d2b.txt {UB} rows) — read in two Read pages, part I on build_set over the range, '
         f'the U file\'s {UB} Bekhorot rows appended (U_RUNS widened to all three), the D2 check on I; then THE WRITER derived from write_ch14_docket.py (the parts A-I joined; the '
         f'eleven ranges asserted against ch15_docket_scan.out\'s "THE RANGES SIZED:"; the dump\'s twice-listed address dropped by computation; coverage computed; the crowns\' three '
         f'paragraphs under "## The finds"; OUT logic/oral_triage/deu_15_reeh_exam_2026-09-23.md, lint 0), the docket\'s records (COMPILE_DEBT\'s 13b box (o), MIDDOT — every code '
         f'checked before typed, MISHNAH_TOPICS, the state doc\'s checkpoint), its clean point; then RUN B. POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 13b — THE '
         f'COMPILE OF CHAPTER 15 … THE DESIGN" whole with its "THE DOCKET — AS RUN (D1)" and "(D2a)" paragraphs (the newest section), MEMORY.md; then #207, its addenda 1-2 and the two NOTES.\n')
assert '/Users/' not in STATE.replace('/Users/Shared', '')
RP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; rp = open(RP, encoding='utf-8').read()
H_OLD = '## 2. WHERE IT STANDS (2026-09-23, 13b D1 closed; the state doc #207 addendum 1 the newest)'
H_NEW = '## 2. WHERE IT STANDS (2026-09-23, 13b D2a closed; the state doc #207 addendum 2 the newest)'
lm = re.search(r'D1 DONE — (\d+) addresses, (\d+) read whole \(the parts in the forms\)\.', rp); N1 = lm.group(1)
L_OLD = lm.group(0); L_NEW = f'D1 DONE ({N1}), D2a DONE (Kiddushin 14b-22b, {N}; the parts in the forms).'
X_OLD = '- NEXT ON HIS WORD: D2 (Kiddushin 14b-22b whole, the clean point, Bekhorot 25a-28b), then RUN B.'
X_NEW = '- NEXT ON HIS WORD: D2b (Bekhorot 25a-28b whole, the writer, the exam file, the records), then RUN B.'
assert rp.count(H_OLD) == 1 and rp.count(L_OLD) == 1 and rp.count(X_OLD) == 1
rp2 = rp.replace(H_OLD, H_NEW).replace(L_OLD, L_NEW).replace(X_OLD, X_NEW); assert len(rp2.encode()) <= 10240, len(rp2.encode())
MP = f'{MEM}/MEMORY.md'; mem = open(MP, encoding='utf-8').read()
mm_ = re.search(r'13b: design DONE, DOCKET D1 DONE \((\d+)\); NEXT: D2 \(Kiddushin 14b-22b, Bekhorot 25a-28b\)', mem); assert mm_ and mm_.group(1) == N1
M_OLD = mm_.group(0); M_NEW = f'13b: design, D1 ({N1}), D2a Kiddushin ({N}) DONE; NEXT: D2b (Bekhorot 25a-28b, the exam file)'
mem2 = mem.replace(M_OLD, M_NEW); assert mem2.count(M_NEW) == 1 and len(mem2.encode()) <= 17000, len(mem2.encode())
WALK = f'{MEM}/deuteronomy-walk.md'; walk_line = (f'\nSITTING 13b DOCKET D2a DONE {DATE} — Kiddushin 14b-22b whole: {N} addresses (link {NL}, topic {NT}; carried {carried}, read whole here {readhere}); '
                                                f'the parts G, H, the U file (86), the re-chunker by work and the D2 checker in the forms; the clean point after Kiddushin taken unconditionally. NEXT on his word: D2b (Bekhorot 25a-28b whole, part I, the writer, the exam file, the records), then RUN B.\n')
MAPF = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; mp = open(MAPF, encoding='utf-8').read(); sec = mp[mp.rfind('\n## Sitting 13b — THE COMPILE OF CHAPTER 15'):]
assert 'THE DOCKET — AS RUN (D1' in sec and 'THE DOCKET — AS RUN (D2a' not in sec
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; sd = open(SD, encoding='utf-8').read(); assert '#207 ADDENDUM 2' not in sd and sd.rstrip().endswith('then #207, ADDENDUM 1 and its two NOTES.')
# every text built and every cap asserted — now the writes
open(MAPF, 'a', encoding='utf-8').write(MAP); open(SD, 'a', encoding='utf-8').write(STATE); open(RP, 'w', encoding='utf-8').write(rp2); open(MP, 'w', encoding='utf-8').write(mem2); open(WALK, 'a', encoding='utf-8').write(walk_line)
F = f'{ROOT}/World/step9/forms_deuteronomy_walk'; copied = []
for fn in sorted(os.listdir(SP)):
    if re.match(r'(ch15_docket_(G|H|U|crowns|d2_check|uncred_d2)\.py|ch15_docket_(d2a_check|uncred_d2)\.out|ch15_uncred_unres_d2[kb]\.txt|ch15b_timing\.tsv|write_ch15b_d2a_point\.py|ch15_docket_U_d2k_block\.txt)$', fn):
        shutil.copy(f'{SP}/{fn}', f'{F}/{fn}'); copied.append(fn)
print('MAP +', len(MAP.encode()), 'bytes; STATE +', len(STATE.encode()), '; recovery', len(rp2.encode()), '; MEMORY.md', len(mem2.encode()), '; walk +', len(walk_line.encode()))
print('CENSUS', census); print('COPIED', len(copied), copied)
