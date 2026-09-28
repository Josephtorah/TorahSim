import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19 (LEAN, 2026-09-27): the chain's verdict recorded after the harness's DONE notification — its SUMMARY read ONCE (the cache law): a NOTE
# under #228 in the state doc, the recovery page's three phrases, the memory's walk line and note; every number READ FROM THE SUMMARY'S PRINT; the caps asserted.
# Sitting 18's precedent (the NOTE under #224 after the chain). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
S = rd(f'{SP}/ch29_gates_SUMMARY.txt'); assert S.rstrip().split('\n')[-1].startswith('ALL GREEN '), S[-200:]
RC = rd(f'{SP}/ch29_gates.DONE').strip(); assert RC == 'rc=0', RC
def hms(t): h, m, s = map(int, t.split(':')); return h * 3600 + m * 60 + s
T0 = R(r'^=== chain (\d\d:\d\d:\d\d)$', S, 't0'); T1 = R(r'^ALL GREEN (\d\d:\d\d:\d\d)$', S, 't1'); SEC = hms(T1) - hms(T0)
SEATS = re.findall(r'^(deu_\w+): seated (\d+) operators on \d+ steps (\[[^\]]*\]); scenarios (\d+) in the anchor form$', S, re.M)
CL = rd(f'{SP}/ch29_chain.log'); SEAT29 = R(r'^(deu_29_moab_covenant: seated \d+ operators on \d+ steps \[[^\]]*\]; scenarios \d+ in the anchor form)$', CL, 'seat 29')
VT = re.findall(r'^verify_text (deu_\w+): TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', S, re.M); assert len(VT) == 3, VT
RIT = len(re.findall(r'^=== ritual deu_', CL, re.M)); assert RIT == 3 and CL.count('RITUAL NOT COMPLETE') == 0
TRUTH = R(r'^(CORPUS TRUTH GREEN — one world, 247 units, [^\n]*hash 8b8fff1fa28953af)$', S, 'truth')
for g in ('build_world', 'journal_gate', 'register_gate', 'large_letter', 'home_gate'): assert re.search(rf'^=== {g} \d\d:\d\d:\d\d\nexit 0 \| ', S, re.M), g
LL = R(r'^exit 0 \| (\d+/\d+)$', S, 'large letter')
FZ = sum(rd(f'{ROOT}/logic/units/{u}.yaml').count('status: frozen') for u in ('deu_29_moab_covenant', 'deu_30_teshuvah_choice', 'deu_31_charge_torah')); assert FZ == 3, FZ
ct = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); U1 = int(R(r'assert len\(W\["units"\]\) == (\d+)', ct, 'U1')); S1 = int(R(r'assert len\(W\["standing"\]\) == (\d+)', ct, 'S1')); assert (U1, S1) == (247, 2344), (U1, S1)
print('THE SUMMARY READ ONCE:', T0, '->', T1, SEC, 's;', RC, '| seats', SEAT29.split(':')[1].strip()[:9], [(u, n, st) for u, n, st, sc in SEATS], '| verify_text', VT, '| rituals', RIT, 'frozen', FZ, '| truth:', TRUTH, '| large_letter', LL)
NOTE = (f'\n\nNOTE UNDER #228 (2026-09-27, {T1} — the chain\'s DONE notified by the harness after the clean point was written; its SUMMARY read ONCE, never polled): THE GATES CHAIN ALL GREEN ON ITS FIRST PASS ({SEC} s; {RC}) — the seats ({SEAT29.split(": ", 1)[1].split(";")[0]}; ' + '; '.join(f'{u} {n} operators on steps {st}' for u, n, st, sc in SEATS) + f'; the scenarios 7 per unit in the anchor form); verify_text TEXT LAYER GREEN x3 ({", ".join(f"{u.split(chr(95))[1]} {n} steps" for u, n, sc in VT)}); the ritual COMPLETE x3 — the three units FROZEN; THE FOLD — the tripwire set 244 -> {U1} and 2329 -> {S1}, {TRUTH} — the prediction held, the hash unmoved; build_world ALL GREEN; the journal gate GREEN; THE REGISTER GATE --strict GREEN; large_letter {LL}; the home gate GREEN. THE TAIL after the compaction: verify_claims (ch29_vc.sh), the display patch (the ten blank glosses probed first), the labels census --strict, the four records (the map\'s AS BUILT — LEAN with the departures and the lessons, the state doc\'s NOTE, the recovery page, the memory), COMPILE_DEBT\'s line (10), the commit message (18b + 19), the forms; then the commit on his word.')
sd = rd(SD); assert '\n#228 (' in sd and 'NOTE UNDER #228' not in sd
rec = rd(REC)
for old, new in (('29-31 READ, the chain running.', '29-31 READ, chain GREEN.'), ('- units 244 / standing 2329,', f'- units {U1} / standing {S1},'), ('THE CHAIN LAUNCHED — <scratch>/ch29_gates_SUMMARY.txt read ONCE at the tail.', 'THE CHAIN ALL GREEN (1st pass; fold 247/2344, hash unmoved).')):
    assert rec.count(old) == 1, old; rec = rec.replace(old, new)
mm = rd(MM)
old = 'the chain LAUNCHED — the seat, the freeze x3, the fold 244->247, the gates; its summary read at the tail)'
assert mm.count(old) == 1; mm = mm.replace(old, f'the chain ALL GREEN on its first pass ({SEC} s) — the seat, the freeze x3, the fold 244->247 / 2329->2344, hash unmoved, the gates)')
mw = rd(MW).rstrip('\n') + f'\n\nTHE CHAIN OF SITTING 19 ALL GREEN ON ITS FIRST PASS ({SEC} s; read once when the harness notified, after the clean point #228) — the three units frozen, the fold 247/2344 with the hash unmoved, the journal and register gates green. The tail after the compaction.\n'
assert len(rec.encode()) <= 10240 and len(mm.encode()) < 17000, (len(rec.encode()), len(mm.encode()))
home = os.path.expanduser('~'); assert home not in NOTE + rec + mm and SP not in NOTE + rec + mm
open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + NOTE + '\n'); open(REC, 'w', encoding='utf-8').write(rec); open(MM, 'w', encoding='utf-8').write(mm); open(MW, 'w', encoding='utf-8').write(mw)
for f in (SD, REC, MM, MW):
    out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]; print('  lint', os.path.basename(f), out)
print(f'THE CHAIN NOTE WRITTEN under #228 ({len(NOTE.encode())} bytes); the recovery page {len(rec.encode())}; MEMORY.md {len(mm.encode())}')
