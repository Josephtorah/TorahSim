import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# a fast checker for the runner's ink asserts — parts 1 and 2 exec'd WITHOUT the callee imports and the guard (seconds, not the import cycle);
# every assert reported with its tuple (ch6_fastcheck.py's form)
import os, sys, re, subprocess, traceback, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
p1 = open(SP + '/ch7_part1.py', encoding='utf-8').read()
p1 = re.sub(r"^import cold_run_\w+ as \w+ .*$", "", p1, flags=re.M)
p1 = re.sub(r"^from compile_guards import.*$", "", p1, flags=re.M)
p1 = re.sub(r"^GUARDED = .*$\n^assert GUARDED.*$\n^print\('guard.*$", "GUARDED = 0", p1, flags=re.M)
p1 = p1.replace("_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))", "_ROOT = %r" % ROOT)
p1 = p1.replace("_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))", "_sys.path.insert(0, %r)" % (ROOT + '/World/step9'))
p1 = p1.replace("HERE = _os.path.dirname(_os.path.abspath(__file__))", "HERE = %r" % (ROOT + '/World/step9'))
ns = {'__file__': SP + '/ch7_part1.py', '__name__': 'fastcheck'}
def run_block(text, label):
    tree = ast.parse(text); bad = 0
    for node in tree.body:
        seg = ast.get_source_segment(text, node)
        try:
            exec(compile(ast.Module([node], []), label, 'exec'), ns)
        except AssertionError as e:
            bad += 1; print('ASSERT FAIL [%s] line %d: %s\n    %s' % (label, node.lineno, str(e)[:1200], seg[:400]))
        except Exception as e:
            bad += 1; print('ERROR [%s] line %d: %s: %s' % (label, node.lineno, type(e).__name__, str(e)[:300])); print('   ', seg[:200])
    return bad
b1 = run_block(p1, 'part1')
p2 = open(SP + '/ch7_part2.py', encoding='utf-8').read()
b2 = run_block(p2, 'part2')
print('fastcheck: part1 fails %d, part2 fails %d' % (b1, b2))
