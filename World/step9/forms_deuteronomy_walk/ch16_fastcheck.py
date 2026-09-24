import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# a fast checker for the runner's ink asserts — parts 1 to 4 exec'd WITHOUT the guard (seconds, not the import cycle — the callees are imported live);
# every assert reported with its tuple (ch15_fastcheck.py's form). RUN FROM THE REPO ROOT.
import os, sys, re, subprocess, traceback, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
p1 = open(SP + '/ch16_part1.py', encoding='utf-8').read()
p1 = re.sub(r"^from compile_guards import.*$", "", p1, flags=re.M)
p1 = re.sub(r"^GUARDED = .*$\n^assert GUARDED.*$\n^print\('guard.*$", "GUARDED = 0", p1, flags=re.M)
p1 = p1.replace("_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))", "_ROOT = %r" % ROOT)
p1 = p1.replace("_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))", "_sys.path.insert(0, %r)" % (ROOT + '/World/step9'))
p1 = p1.replace("HERE = _os.path.dirname(_os.path.abspath(__file__))", "HERE = %r" % (ROOT + '/World/step9'))
ns = {'__file__': SP + '/ch16_part1.py', '__name__': 'fastcheck'}
def run_block(text, label):
    tree = ast.parse(text); bad = 0
    for node in tree.body:
        seg = ast.get_source_segment(text, node)
        try:
            exec(compile(ast.Module([node], []), label, 'exec'), ns)
        except AssertionError as e:
            bad += 1; print('ASSERT FAIL [%s] line %d: %s\n    %s' % (label, node.lineno, str(e)[:1600], seg[:400]))
        except Exception as e:
            bad += 1; print('ERROR [%s] line %d: %s: %s' % (label, node.lineno, type(e).__name__, str(e)[:300])); print('   ', seg[:200])
    return bad
b = [run_block(p1, 'part1')]
for n in (2, 3, 4):
    f = SP + '/ch16_part%d.py' % n
    b.append(run_block(open(f, encoding='utf-8').read(), 'part%d' % n) if os.path.exists(f) else -1)
print('fastcheck: part1 fails %d, part2 fails %d, part3 fails %d, part4 fails %d' % tuple(b))
