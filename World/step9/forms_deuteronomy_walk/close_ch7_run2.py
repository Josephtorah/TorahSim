import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# 5b RUN 2's close: run the docket writer, lint the docket, then the records with the counts parsed from the writer's print (never typed)
import subprocess, re, ast, os, sys
SP = os.path.dirname(os.path.abspath(__file__)); ROOT = _ROOT
class _O: pass
if os.path.exists(f'{SP}/ch7_docket_write.out'):   # the rerun after the memory cap tripped: the writer's print reused, the docket already written
    out = _O(); out.stdout = open(f'{SP}/ch7_docket_write.out').read(); out.returncode = 0
else:
    out = subprocess.run([sys.executable, f'{SP}/write_ch7_docket.py'], capture_output=True, text=True, cwd=ROOT)
    print(out.stdout); print(out.stderr[-2000:])
    assert out.returncode == 0 and 'WROTE' in out.stdout, 'the writer failed'
    open(f'{SP}/ch7_docket_write.out', 'w').write(out.stdout)
DOCKET = f'{ROOT}/logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md'
lint = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', DOCKET], capture_output=True, text=True).stdout.strip().splitlines()[-1]
print('docket lint:', lint); assert lint.endswith('0 flag(s)'), lint
def d(label):
    m = re.search(r'^' + re.escape(label) + r' (\{.*?\})', out.stdout, re.M); return ast.literal_eval(m.group(1))
V = d('verdicts'); LC = d('LAW by cell'); NO = d('OUTSIDE by work')
link = ast.literal_eval(re.search(r'verdicts \{.*?\} link (\{.*?\}) topic', out.stdout).group(1)); topic = ast.literal_eval(re.search(r'topic (\{.*?\})$', out.stdout, re.M).group(1))
rows = re.search(r'^rows (\d+) link (\d+) topic (\d+) credited (\d+) \(link (\d+) topic (\d+) \)', out.stdout, re.M); N, NL, NT, NC, NCL, NCT = map(int, rows.groups())
az = re.search(r'Avodah Zarah 42a-54b whole (\d+) read (\d+) remainder (\[.*\])', out.stdout); AZW, AZR, REM = int(az.group(1)), int(az.group(2)), az.group(3)
size = os.path.getsize(DOCKET)
cen = ', '.join(f'{k} {V[k]}' for k in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE') if k in V)
lc = ', '.join(f'{k} {v}' for k, v in sorted(LC.items())); no = ', '.join(f'{k} {v}' for k, v in sorted(NO.items(), key=lambda kv: -kv[1]))
# ---- 1. the state doc's addendum (RUN 2's close)
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
sd = open(SD, encoding='utf-8').read(); assert '#195 ADDENDUM 2 (2026-09-18)' in sd
DONE1 = '#195 ADDENDUM 3' in sd
add = f"""
#195 ADDENDUM 3 (2026-09-18): 5b RUN 2 CLOSED — A CLEAN COMPACTION POINT. Parts C and D read WHOLE and verdicted (ch7_docket_C.py 134 rows, ch7_docket_D.py 129 rows; every part's WHOLE dict empty, apply_whole's counts zero — computed); write_ch7_docket.py (write_ch6_docket.py's form — the ENUMERATED line parsed for Avodah Zarah 42a-54b, LONG 13 ranges asserted, MISH 36, the six amudim ranges asserted to sum to the read count, the verse hits asserted) WROTE logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md ({size} bytes): {N} rows (link {NL}, topic {NT}), credited {NC} (link {NCL}, topic {NCT}); the verdicts {cen} (link {link}; topic {topic}); LAW by cell {lc}; OUTSIDE by work {no}; Avodah Zarah 42a-54b whole {AZW}, read {AZR}, the remainder {AZW - AZR} enumerated by amud {REM}; coverage computed, the cite index {N} addresses, missing 0 extra 0; lint 0. THE CROWNS (fifteen in the docket's finds section): the three readings of "show them no favor"; the marriage bar's scope (the seven nations by Torah law; every nation by R. Shimon's reason or the captive's verse) and THE CHILD FOLLOWS THE MOTHER; the Asherah defined (7:5 "hew" and 12:3 "burn" TWO CASES on the shelf); the order of the demolition (fell, conquer, eradicate) and its reason (the Land Israel's, the gentiles' worship the calf's agency — 53b:7-11); the altar and the platform measured; the nullification (a gentile's idol at once from 7:25's word; the Joshua-war idols NOT revoked — the devoted nations' idols stay forbidden); "on them" against "with them" (the decorative item); the abomination into the house (the residence, the wall, a house bowed to, the impurity); the devoted thing and the exchange (the Asherah's wood flogged under 7:26 and 13:18); which figure is an idol; another's property (a rite upon it — Ahaz's vessels the source); "consume" the war's spoil; the ban's condition and scope (repentance releases; the Canaanite outside the Land not devoted; the hornet at the Jordan's bank / two hornets); the blessings and the reward; the lashes' count. THREE THINGS THE DESIGN DID NOT PREDICT, for RUN 3: (1) THE PITY'S HOLE HAS NO ROW — "your eye shall not pity" (7:16) is cited by no link row on the shelf (verse 16 once, Bava Kamma 113b on "consume"); the write pity_barred stands on the ink alone, its exam rows the book's later seats forward — the runner's F4 consume_no_pity carries the note; (2) the shelf's THEORY OF THE DEMOLITION COMMAND (Avodah Zarah 53b:7-11) — a DATA row for F1 the_four_objects (the_calfs_agency), beside the_devotings; (3) THE BAN'S CONDITION on the shelf (Sotah 35b:10-13, 36a:1 — R. Shimon's "lest they teach you" written below the plaster; 21:10's captives) — F1 the_ban's exam parameters as DATA (the_bans_condition), 20:16-18's cell OWED FORWARD as designed. THE TREE: + logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md (new, untracked); the scratchpad holds ch7_docket_scan.py (patched), ch7_scan.out, ch7_docket_dump.txt, ch7_docket_common.py, ch7_docket_rows.py, ch7_docket_A-D.py, ch7_rows_A-D.txt, write_ch7_docket.py, ch7_docket_write.out, close_ch7_run2.py — copied to the forms at RUN 4. THE WORD FOR THE NEXT SITTING — RUN 3 OF 5b ON THE OWNER'S WORD, per the design's THE ORDER: add_types_ch7.py (from add_types_ch6.py — three tape kinds, one case kind, four effects, the daemon block, the functions block, the span, the CALL edges, I5 66 → 67), the recorder and the stitcher (the scratch copies: SPAN_ORDER + 'seven_nations', no marker row), the gates to FAIL (daemon, dependency), the runner ch7_part1-4.py assembled by cat (the fast checker over parts 1 and 2; the honest-pairing guard; zero-report probes; the scene and the narrative predicted by script; CASES generated from the cells' asks; the three DATA rows above added), the recorder, the stitcher, the literals CQ1-CQ9 (patch_seq_literals_ch7.py), the tape run to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, the checkpoint (#195 addendum 4). The commit whenever his word comes (the message at <scratch>/commit_msg_ch7.txt — add the docket's line).
"""
if not DONE1: open(SD, 'a', encoding='utf-8').write(add)
# ---- 2. the recovery page's IN FLIGHT line
RP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
rp = open(RP, encoding='utf-8').read()
old = '- IN FLIGHT: 5b RUN 1 DONE (the design in the map); NEXT: RUN 2 — readback Q16-Q18 to FAIL, then the docket WHOLE. The commit on his word.'
new = f'- IN FLIGHT: 5b RUN 2 DONE (the docket {N} rows WHOLE, lint 0); NEXT: RUN 3 — the types, the runner, the stitch, the tape 10/10. The commit on his word.'
assert rp.count(old) + rp.count(new) == 1; rp = rp.replace(old, new); open(RP, 'w', encoding='utf-8').write(rp)
print('recovery page', os.path.getsize(RP), 'bytes (cap 10240)'); assert os.path.getsize(RP) <= 10240
# ---- 3. the memory index line and the walk memory's paragraph
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
mi = open(f'{MEM}/MEMORY.md', encoding='utf-8').read()
new = f'5b RUN 2 DONE (docket {N} rows); NEXT: RUN 3 the tape'
for old in ('5b RUN 1 DONE (the design); NEXT: RUN 2 the docket', f'5b RUN 2 DONE (the docket {N} rows whole); NEXT: RUN 3 the runner and the tape'):
    if mi.count(old) == 1: mi = mi.replace(old, new)
assert mi.count(new) == 1; open(f'{MEM}/MEMORY.md', 'w', encoding='utf-8').write(mi)
print('MEMORY.md', len(mi.encode('utf-8')), 'bytes (cap 17000)'); assert len(mi.encode('utf-8')) < 17000
dw = open(f'{MEM}/deuteronomy-walk.md', encoding='utf-8').read(); assert 'SITTING 5b RUN 1 DONE 2026-09-18' in dw
DONE3 = 'SITTING 5b RUN 2 DONE' in dw
para = f"""
SITTING 5b RUN 2 DONE 2026-09-18 (on "Go" after the reread; the state doc #195 addenda 2-3): the readback probes Q16-Q18 written to FAIL (15/18); the scan rerun with the six Avodah Zarah amudim named (42a-42b, 44b-46b, 47b-48b, 49b, 51b-52b, 53b-54b — {AZR} rows read of {AZW}; the remainder {AZW - AZR} enumerated by amud); THE DOCKET logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md — {N} rows (link {NL}, topic {NT}; credited {NC}) EVERY ROW READ WHOLE FROM THE START (no cut, no overlay; four parts A-D on 4b's instruments by sed, the ADDRS assert from the dump's header); the verdicts {cen}; LAW by cell {lc}. LESSONS: (1) the whole-range scan's credit count (89) counted credits in the enumerated part — the rerun with the amudim named gives the true {NC}; (2) OUTSIDE (1b's form — a declared range's digression) is the honest verdict for the tractate's digressions when a range is read whole ({V.get('OUTSIDE', 0)} rows here); (3) a hole predicted by the design may have NO ROW on the shelf — the pity's (7:16) has none; the write stands on the ink alone; (4) the shelf teaches the demolition command's REASON (the calf's agency, Avodah Zarah 53b:7-11) and the ban's CONDITION (repentance, Sotah 35b:10) — DATA rows the design did not name, added at run 3. NEXT: RUN 3 — the types, the recorder and the stitcher, the runner cold_run_seven_nations.py in parts, the literals CQ1-CQ9, the tape 10/10, checkpoint_check.py --all after the tape.
"""
if not DONE3: open(f'{MEM}/deuteronomy-walk.md', 'a', encoding='utf-8').write(para)
# ---- 4. the map's RUN 2 — AS RUN paragraph (appended at the file's end — the 5b design is the newest section)
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
mp = open(MAP, encoding='utf-8').read(); assert 'the commit message for the owner' in mp.rstrip()[-80:], repr(mp.rstrip()[-80:])
DONE4 = 'RUN 2 — AS RUN (2026-09-18' in mp
run2 = f"""
RUN 2 — AS RUN (2026-09-18, on "Go" after the reread; the compaction point #195 with its addenda 1-3): THE PROBES FIRST — readback_probes.py Q16-Q18 written
to FAIL before the runner exists, 15/18 (Q16 the runner absent; Q17-Q18 their tuples). THE SCAN RERUN with the six Avodah Zarah amudim named and the
remainder enumerated ({AZW} whole, {AZR} read, {AZW - AZR} by amud {REM}); the dump {N} rows (link {NL}, topic {NT}, credited {NC} — the whole-range scan's 89 had
counted credits in the enumerated part). THE INSTRUMENTS by sed from 4b's (the ADDRS assert from the dump's header, never typed; N huge prints the row
whole); the four parts printed WHOLE and every row read whole before its verdict — no cut, no overlay, apply_whole's counts zero (computed). THE VERDICTS
{cen} in the four parts (A 88, B 169, C 134, D 129); LAW by cell {lc}; OUTSIDE {V.get('OUTSIDE', 0)} — a declared range's digression on another matter (1b's
form: {no}). THE DOCKET logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md ({size} bytes; coverage computed, the cite index, lint 0) with its
fifteen crowns — the design's (o) expected them and the rows gave them: the three readings of favor (20a:1-4); the seven nations only by Torah law and the
child follows the mother (36b:5; Kiddushin 68b:2-3; Yevamot 23a:11; Mishnah Kiddushin 3:12); THE ASHERAH DEFINED — the shelf reads 7:5 "hew" and 12:3 "burn"
AS TWO CASES (45b:9); THE ORDER OF THE DEMOLITION (45b:10-12: fell, conquer, eradicate; break and leave; pursue then return to burn) — the demolition's
reference row against journeys' OPEN debit reads as the shelf reads it; the renaming for the worse (45b:16-46a:3 — the Sifrei 61:7's seat); the altar
and the platform (53b:18: one stone / many; most destroyed); the nullification from 7:25's word (52a:9-10) and the Joshua-war idols NOT revoked
(53b:5); "on them" against "with them" (51b:10-11); the abomination into the house (Mishnah 1:9; 47b:4-12 — a house bowed to); the devoted thing and the
exchange, the Asherah's wood flogged (54b:4-11; Makkot 22a:2-3); which figure (42b:13-14; 44b:1-15); another's property and Ahaz's vessels (54a:9-54b:2);
"consume" the war's spoil (Bava Kamma 113b:7); the ban's condition and scope and the hornet at the Jordan (Sotah 35b:10-36a:1, 36a:8-10). THREE THINGS
THE DESIGN DID NOT PREDICT, carried to RUN 3 as DATA rows: (1) THE PITY'S HOLE HAS NO ROW — "your eye shall not pity" (7:16) is cited by no link row on the
shelf; the write pity_barred stands on the ink alone, its exam rows the book's later seats forward (the runner's F4 carries the note); (2) the shelf's
THEORY OF THE DEMOLITION COMMAND (53b:7-11 — the Land already Israel's from the fathers, so the gentiles could not forbid its trees except as Israel's
agents after the calf: the Asherim a Jew's idols, irrevocable, hence burned) — the_calfs_agency beside the_devotings in F1; (3) THE BAN'S CONDITION on
the shelf (35b:10: R. Shimon's "lest they teach you" written below the plaster — the inhabitants who repent accepted; 35b:13, 36a:1: the Canaanite
outside the Land not devoted) — the_bans_condition in F1 the_ban, with 20:16-18's cell OWED FORWARD as designed. NEXT: RUN 3 per THE ORDER above.
"""
if not DONE4: open(MAP, 'a', encoding='utf-8').write(run2)
for f in (SD, RP, MAP, f'{MEM}/MEMORY.md', f'{MEM}/deuteronomy-walk.md', DOCKET):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().splitlines()[-1]
    print(os.path.basename(f), r)
print(subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True).stdout.strip().splitlines()[-1])
