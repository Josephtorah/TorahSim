import sys, re
f, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
t = open(f, encoding='utf-8').read()
blocks = re.split(r'\n(?=== Deut )', t)
out = []
for b in blocks:
    m = re.match(r'== Deut (\d+):(\d+)', b.strip())
    if not m: continue
    v = int(m.group(2))
    if lo <= v <= hi:
        out.append('\n'.join(l for l in b.strip().split('\n') if not l.startswith('  MOR') and not l.startswith('  LEM')))
s = '\n\n'.join(out); print(s); print('\n[bytes', len(s.encode()), '| verses', len(out), ']', file=sys.stderr)
