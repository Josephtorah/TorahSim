#!/usr/bin/env python3
# 13b docket D1 — THE CLEAN POINT'S RECORDS (12b's form): the parts A-F re-checked as a partition of D1, the census COMPUTED (never typed), the carry's and the chunker's
# counts READ FROM THEIR PRINTS, the timing rows read from the tsv; then, with every text built first and the caps asserted: the map's "THE DOCKET — AS RUN (D1)"
# paragraph appended (no Hebrew script — the map's lint 0), the state doc's "#207 ADDENDUM 1" appended, the recovery page's section-2 lines rewritten in place
# (<= 10,240 bytes), MEMORY.md's walk line (<= 17,000), the memory's deuteronomy-walk.md line appended; the D1 instruments copied to the forms folder.
import os, re, sys, importlib.util, subprocess, shutil, datetime
from collections import Counter
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
from ch15_docket_common import D1_UNIQUE, D2_UNIQUE, KIND_FIRST, ADDRS
from ch15_docket_crowns import crowns_d1
V = {}; per = {}
for p in 'ABCDEF':
    part = f'ch15_docket_{p}'; spec = importlib.util.spec_from_file_location(part, f'{SP}/{part}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    per[p] = len(m.ROWS); assert m.WHOLE_STATS['corrected'] == 0
    for a, vd, n in m.ROWS:
        assert a not in V, ('overlap', a, p); V[a] = (vd, n)
assert set(V) == set(D1_UNIQUE) and len(V) == len(D1_UNIQUE), (len(V), len(D1_UNIQUE))
N = len(V); NL = sum(1 for a in V if KIND_FIRST[a] == 'LINK'); NT = N - NL
cnt = Counter(vd for vd, _ in V.values()); cl = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'LINK'); ct = Counter(vd for a, (vd, _) in V.items() if KIND_FIRST[a] == 'TOPIC')
carried = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and '; carried) — ' in n[:200]); unres = sum(1 for vd, n in V.values() if n.startswith('CREDITED (') and 'read whole here' in n[:400] and '; carried) — ' not in n[:200])
readhere = N - carried; own = N - carried - unres
LAWCELLS = Counter(mm.group(1) for vd, n in V.values() if vd == 'LAW' and not n.startswith('CREDITED (') for mm in [re.search(r'\b(F[1-7])\b', n)] if mm)
NOUT = Counter(a.rsplit(' ', 1)[0] for a, (vd, _) in V.items() if vd == 'OUTSIDE')
carry = open(f'{SP}/ch15_credit_carry.out', encoding='utf-8').read().splitlines()[0]
cm = re.match(r'credited (\d+) resolved (\d+) unresolved (\d+) unresolved bytes (\d+)', carry); C_ALL, C_RES, C_UNRES = int(cm.group(1)), int(cm.group(2)), int(cm.group(3))
unc = open(f'{SP}/ch15_docket_uncred.out', encoding='utf-8').read()
um = re.search(r'rows (\d+) D1 (\d+) D2 (\d+) \| uncredited D1 (\d+) chunks (\d+) \| uncredited D2 (\d+) chunks (\d+)', unc); U_ROWS, U_D1, U_D2, U_UD1, U_CH1, U_UD2, U_CH2 = map(int, um.groups())
chunks = re.findall(r'D1 (ch15_uncred_d1_\d+\.txt) rows (\d+)-(\d+) \((\d+) rows, (\d+) bytes\)', unc)
ur = re.search(r'unresolved credited rows (\d+) D1 (\d+) (\d+) bytes D2 (\d+) (\d+) bytes', unc); UR_ALL, UR_D1, UR_D1B, UR_D2 = int(ur.group(1)), int(ur.group(2)), int(ur.group(3)), int(ur.group(4))
from ch15_docket_U import CRED as _CRED
dups = [a for a, c in Counter(ADDRS).items() if c > 1]; nd_uncred = sum(c - 1 for a, c in Counter(ADDRS).items() if c > 1 and a not in _CRED)   # the twice-listed addresses, computed from the dump
assert U_D1 == len(D1_UNIQUE) + len(dups) and UR_D1 == unres and U_UD1 == own + nd_uncred, (U_D1, len(D1_UNIQUE), len(dups), UR_D1, unres, U_UD1, own, nd_uncred)
rows = [l.split('\t') for l in open(f'{SP}/ch15b_timing.tsv', encoding='utf-8').read().splitlines() if '\t13b D1' in l]
TIM = '; '.join(f'{n} {s}s (at {t}, rc {r})' for t, n, s, r in rows)
chunk_txt = ', '.join(f'{f} rows {a}-{z} ({n} rows, {b} bytes)' for f, a, z, n, b in chunks)
census = (f'{N} addresses (link {NL}, topic {NT}; {len(dups)} address(es) listed twice in the dump — {", ".join(dups)}, a link row and the chapter\'s row — taken once): '
          f'LAW {cnt["LAW"]} / DERIVATION {cnt["DERIVATION"]} / DISPUTE {cnt["DISPUTE"]} / CONTEXT {cnt["CONTEXT"]} / OUTSIDE {cnt["OUTSIDE"]} '
          f'(the link rows {dict(sorted(cl.items()))}; the topic rows {dict(sorted(ct.items()))}); credited {carried + unres} — {carried} CARRIED with their ledgers\' own verdict lines, '
          f'{unres} whose ledger\'s form carried no verdict READ WHOLE HERE (the U file); {readhere} rows read whole in this run ({own} uncredited); LAW by cell, this docket\'s own notes {dict(sorted(LAWCELLS.items()))}; OUTSIDE by work {dict(NOUT)}')
DATE = '2026-09-23'
MAP = (f'\nTHE DOCKET — AS RUN (D1, {DATE}; the owner\'s "Go" after the compaction at #207 and his "Reread"): THE SMALL WORKS — every address outside Kiddushin 14b-22b and '
       f'Bekhorot 25a-28b. THE INSTRUMENTS derived from 12b\'s by asserted substitutions (derive_ch15_docket_tools.py — the carry, the common file with THE SPLIT BY ADDRESS '
       f'appended: long_range() names the two long ranges, D1 and D2 are SETS computed from the dump, a part builds over a subset of D1 by the address\'s first kind and its work; '
       f'the rows printer) and the chunker typed fresh (ch15_docket_uncred.py — two chunk series, one per run). THE CARRY (ch15_credit_carry.py): credited {C_ALL}, resolved {C_RES} '
       f'with their ledgers\' own verdict lines, unresolved {C_UNRES} (D1 {UR_D1}, D2 {UR_D2} — the ledgers whose form carries no verdict: the Exodus triage, the sheviit topic docket\'s '
       f'Mishnah Sheviit 10, the calendar blocks\' Rosh Hashanah 9a, the Genesis ledgers\' Ketubot 67b:2 …). THE CHUNKS: the dump\'s {U_ROWS} rows — D1 {U_D1} ({U_UD1} uncredited in {U_CH1} '
       f'files: {chunk_txt}; the unresolved D1 file {UR_D1} rows, {UR_D1B} bytes), D2 {U_D2} ({U_UD2} uncredited in {U_CH2} files). EVERY ROW READ WHOLE (four Read pages and the '
       f'unresolved file, one page each); the middah codes checked in MIDDOT.md before they were typed (I1, I2, I3, I5, I6, I8, I12, I13; E28, E30); THE PARTS A-F on '
       f'ch15_docket_common.build_set — A the link rows of the twenty-seven works ({per["A"]}), B the Mishnah and the Tosefta rows ({per["B"]}), C Gittin 36a-37b and Arakhin '
       f'32b-33a ({per["C"]}), D Makkot 3b and Rosh Hashanah 8b-9a ({per["D"]}), E Bava Metzia 31b, 71a and Ketubot 67b ({per["E"]}), F Bekhorot 33a-37b and 53b ({per["F"]}); the '
       f'shared U file the {unres} unresolved credited rows with the ledgers\' names read from the dump\'s marks; THE D1 CHECK (ch15_docket_d1_check.py) — the parts a PARTITION of '
       f'D1, missing 0, extra 0. THE CENSUS (computed): {census}. THE EXAM FILE IS WRITTEN ONCE AT D2\'S END (12b\'s form — write_ch15_docket.py derived from 12b\'s); the parts, '
       f'the tools and the chunk lists copied to the forms folder at this point. THE TIMING: {TIM}. THE FINDS OF D1 (carried into the exam file\'s "## The finds" at D2):\n{crowns_d1}')
assert not re.search(r'[֐-׿]', MAP) and '/Users/' not in MAP.replace('/Users/Shared', '')
STATE = (f'\n#207 ADDENDUM 1 — THE DOCKET D1 (2026-09-23, THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15; THE DOCKET\'S FIRST RUN under the ~700 clause, on the '
         f'owner\'s "Reread" then "Go" after the compaction at #207; A CLEAN COMPACTION POINT — D1 closed, NO D2 ROW READ): THE STATE: chapter 15 read, frozen, COMMITTED b0eaa56 (not '
         f'pushed); the design in the map (RUN A); THE DOCKET D1 DONE — {census}; the parts A-F, the U file, the tools (derive_ch15_docket_tools.py, ch15_credit_carry.py, '
         f'ch15_docket_common.py, ch15_docket_uncred.py, ch15_docket_d1_check.py, ch15_docket_crowns.py) and the chunk lists in the scratchpad AND copied to '
         f'World/step9/forms_deuteronomy_walk/; the map\'s "THE DOCKET — AS RUN (D1)" paragraph appended to the 13b section (its finds inside); NO exam file yet (written once at '
         f'D2\'s end — the parts hold the verdicts). THE TIMING: {TIM}. NOT COMMITTED (since b0eaa56): the commit\'s own records, the design, #207 and this addendum, the recovery '
         f'page\'s and the memory\'s lines, the forms. NOTHING MID-FLIGHT. NEXT ON HIS WORD (after a compaction: "Reread", then "Go"): D2 — Kiddushin 14b-22b WHOLE ({sum(1 for a in D2_UNIQUE if a.startswith("Kiddushin"))} addresses '
         f'with their link rows; the chunk files ch15_uncred_d2_00.txt … in the scratchpad, the unresolved D2 file ch15_uncred_unres_d2.txt {UR_D2} rows), THE CLEAN POINT after it '
         f'UNCONDITIONALLY, then Bekhorot 25a-28b WHOLE ({sum(1 for a in D2_UNIQUE if a.startswith("Bekhorot"))}), the writer derived from write_ch14_docket.py (the eleven ranges asserted against the scan\'s print; '
         f'the coverage computed), the docket\'s records (COMPILE_DEBT\'s box (o), MIDDOT, MISHNAH_TOPICS), its clean point; then RUN B. POST-COMPACTION REREADS: the recovery '
         f'page, the map\'s "Sitting 13b — THE COMPILE OF CHAPTER 15 … THE DESIGN" with its "THE DOCKET — AS RUN (D1)" paragraph, MEMORY.md; then #207 and this addendum.\n')
assert '/Users/' not in STATE.replace('/Users/Shared', '')
RP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; rp = open(RP, encoding='utf-8').read()
H_OLD = '## 2. WHERE IT STANDS (2026-09-22, 13b RUN A closed; the state doc #207 the newest)'
H_NEW = '## 2. WHERE IT STANDS (2026-09-23, 13b D1 closed; the state doc #207 addendum 1 the newest)'
L_OLD = ('- SITTING 13 (ch 15 read and frozen; two runs + the tail): 132 sources; 7 claims. 13b RUN A CLOSED — the design in the map\n'
         '  (4 lines, 12 effects, 27 parameters; the docket TWO RUNS; the NFKC lesson corrected: the export is clean).\n'
         '- NEXT ON HIS WORD: the docket D1 (the small works), D2 (Kiddushin 14b-22b, Bekhorot 25a-28b), RUN B.')
L_NEW = (f'- SITTING 13 (ch 15 read and frozen): 132 sources; 7 claims. 13b RUN A CLOSED — the design in the map (4 lines, 12 effects,\n'
         f'  27 parameters; the NFKC lesson corrected). D1 DONE — {N} addresses, {readhere} read whole (the parts in the forms).\n'
         f'- NEXT ON HIS WORD: D2 (Kiddushin 14b-22b whole, the clean point, Bekhorot 25a-28b), then RUN B.')
assert rp.count(H_OLD) == 1 and rp.count(L_OLD) == 1, (rp.count(H_OLD), rp.count(L_OLD))
rp2 = rp.replace(H_OLD, H_NEW).replace(L_OLD, L_NEW); assert len(rp2.encode()) <= 10240, len(rp2.encode())
MP = f'{MEM}/MEMORY.md'; mem = open(MP, encoding='utf-8').read()
M_OLD = '15 READ AND FROZEN, COMMITTED b0eaa56 (13; not pushed); 13b RUN A CLOSED (the design; the docket TWO runs); NEXT: the docket D1'
M_NEW = f'15 READ, FROZEN, COMMITTED b0eaa56 (not pushed); 13b: design DONE, DOCKET D1 DONE ({N}); NEXT: D2 (Kiddushin 14b-22b, Bekhorot 25a-28b)'
assert mem.count(M_OLD) == 1; mem2 = mem.replace(M_OLD, M_NEW); assert len(mem2.encode()) <= 17000, len(mem2.encode())
WALK = f'{MEM}/deuteronomy-walk.md'; walk_line = (f'\nSITTING 13b DOCKET D1 DONE {DATE} — {N} addresses of the small works verdicted (link {NL}, topic {NT}; carried {carried}, read whole here {readhere}); '
                                                f'the parts A-F, the U file and the tools in the forms; the exam file written once at D2\'s end. NEXT on his word: D2 (Kiddushin 14b-22b whole, the clean point, Bekhorot 25a-28b), then RUN B.\n')
MAPF = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; mp = open(MAPF, encoding='utf-8').read()
assert mp.rfind('\n## Sitting 13b — THE COMPILE OF CHAPTER 15') > mp.rfind('\n## Sitting 13 — ') and 'THE DOCKET — AS RUN (D1' not in mp[mp.rfind('\n## Sitting 13b'):]
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; sd = open(SD, encoding='utf-8').read(); assert '#207 ADDENDUM 1' not in sd and sd.rstrip().endswith('then #207 and this NOTE.')
# every text built and every cap asserted — now the writes
open(MAPF, 'a', encoding='utf-8').write(MAP); open(SD, 'a', encoding='utf-8').write(STATE); open(RP, 'w', encoding='utf-8').write(rp2); open(MP, 'w', encoding='utf-8').write(mem2); open(WALK, 'a', encoding='utf-8').write(walk_line)
F = f'{ROOT}/World/step9/forms_deuteronomy_walk'; copied = []
for fn in sorted(os.listdir(SP)):
    if re.match(r'(ch15_docket_(A|B|C|D|E|F|U|common|uncred|d1_check|crowns|rows|scan|scan_derive)\.(py|out)|ch15_credit_carry\.(py|out)|ch15_credited_rows\.py|ch15_uncred_unres(_d1|_d2)?\.txt|derive_ch15_docket_(tools|scan)\.py|ch15_docket_dump\.txt|ch15b_timing\.tsv|write_ch15b_(design|cleanpoint|d1_point)\.py|ch15_compile_recon\.py|ch14_aramaic_nfkc\.(py|out)|ch15_docket_uncred\.out)$', fn):
        shutil.copy(f'{SP}/{fn}', f'{F}/{fn}'); copied.append(fn)
print('MAP +', len(MAP.encode()), 'bytes; STATE +', len(STATE.encode()), '; recovery', len(rp2.encode()), '; MEMORY.md', len(mem2.encode()), '; walk +', len(walk_line.encode()))
print('CENSUS', census); print('COPIED', len(copied), copied)
