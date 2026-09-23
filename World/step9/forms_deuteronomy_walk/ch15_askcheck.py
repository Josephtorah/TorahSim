#!/usr/bin/env python3
# every ask of every cell CALLED on the parts as they stand (the fast checker execs the defs; this calls them) — an undefined name or a bad key found before the generator. RUN FROM THE REPO ROOT.
import os, sys, re, ast, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, ROOT + '/World/step9')
p1 = open(SP + '/ch15_part1.py', encoding='utf-8').read()
p1 = re.sub(r"^from compile_guards import.*$", "", p1, flags=re.M); p1 = re.sub(r"^GUARDED = .*$\n^assert GUARDED.*$\n^print\('guard.*$", "GUARDED = 0", p1, flags=re.M)
p1 = p1.replace("_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))", "_ROOT = %r" % ROOT).replace("_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))", "_sys.path.insert(0, %r)" % (ROOT + '/World/step9')).replace("HERE = _os.path.dirname(_os.path.abspath(__file__))", "HERE = %r" % (ROOT + '/World/step9'))
ns = {'__file__': SP + '/ch15_part1.py', '__name__': 'askcheck'}
exec(compile(p1, 'part1', 'exec'), ns)
bad = 0; n = 0
PARTS = sys.argv[1:] or ['ch15_part2.py', 'ch15_part3.py']
for part in PARTS:   # every part exec'd FIRST (the table's asks read DATA, defined in part 4), then every ask called
    src = open(f'{SP}/{part}', encoding='utf-8').read(); exec(compile(src, part, 'exec'), ns)
for part in PARTS:
    src = open(f'{SP}/{part}', encoding='utf-8').read()
    for name, asks in re.findall(r"\ndef ([a-z_]+)\(case, data\):.*?(?=\ndef |\Z)", src, flags=re.S) and [(m.group(1), re.findall(r"if ask == '([a-z_0-9]+)':", m.group(0))) for m in re.finditer(r"\ndef ([a-z_]+)\(case, data\):.*?(?=\ndef |\Z)", src, flags=re.S)]:
        fn = ns[name]
        for a in asks:
            n += 1
            try:
                v, e, prov = fn({'ask': a}, ns.get('DATA', {}))
                assert v != 'no verdict in span', 'no verdict'
                assert all(x == 'accepted' or x in ns['_FXV'] or x == ns['FX'].NONE for x in e), ('an effect off the registry', e)
            except Exception as ex:
                bad += 1; print('ASK FAIL %s.%s: %s: %s' % (name, a, type(ex).__name__, str(ex)[:300]))
print('askcheck: %d asks called, %d failed' % (n, bad))
