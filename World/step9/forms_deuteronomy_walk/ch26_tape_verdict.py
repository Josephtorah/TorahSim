# 18b: the tape print's verdict read small — the N/10 line, the DL verdicts, every DIVERGE checkpoint's name (the eighteen known misses named apart). Usage: python3 ch26_tape_verdict.py <tape print> [<checkpoint_check print>]
import re, sys
t = open(sys.argv[1], encoding='utf-8').read().split('\n')
KNOWN = {'C1', 'C3a', 'C3d-85', 'C3c-literal', 'C4', 'C10', 'CS0', 'CS1', 'CS4', 'CD8', 'CE3', 'CE8', 'CF2', 'CF6', 'CK4', 'CM5', 'CH1', 'CJ3b'}
cps = [(re.match(r'\s*CHECKPOINT (\S+)', l).group(1), l.split()[-1]) for l in t if re.match(r'\s*CHECKPOINT (\S+)', l)]
div = [n for n, v in cps if v == 'DIVERGE']
print('VERDICT:', [l.strip() for l in t if re.search(r'^\s*\d+/\d+ checkpoints', l)], '| DL:', [(n, v) for n, v in cps if n.startswith('DL')])
print('DIVERGE not among the known eighteen:', [n for n in div if n not in KNOWN], '| known diverging:', len([n for n in div if n in KNOWN]), '| Traceback:', any('Traceback' in l for l in t))
if len(sys.argv) > 2:
    c = open(sys.argv[2], encoding='utf-8').read().split('\n'); miss = [re.match(r'\s*MISS\s+(\S+)', l).group(1) for l in c if re.match(r'\s*MISS\s+(\S+)', l)]
    print('CHECKPOINT_CHECK:', [l.strip()[:120] for l in c if l.startswith('checkpoint_check:')], '| misses not known:', [m for m in miss if m not in KNOWN])
