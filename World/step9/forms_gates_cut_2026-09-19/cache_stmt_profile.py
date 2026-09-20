# time every top-level statement of a runner's module (the import's cost, statement by statement); run from World/step9 so the imports resolve
import ast, sys, time, io, contextlib, os
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src)
ns = {'__name__': os.path.basename(path)[:-3], '__file__': os.path.abspath(path)}
sys.path.insert(0, os.path.dirname(os.path.abspath(path))); sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(path)), '..', 'journal')))
rows = []; t_all = time.time()
for node in tree.body:
    seg = ast.get_source_segment(src, node).split('\n')[0][:110]
    t0 = time.time()
    with contextlib.redirect_stdout(io.StringIO()):
        try: exec(compile(ast.Module([node], []), path, 'exec'), ns)
        except BaseException as e: seg = 'ERR ' + repr(e)[:60] + ' | ' + seg
    rows.append((time.time() - t0, node.lineno, type(node).__name__, seg))
tot = time.time() - t_all
kinds = {}
for dt, ln, k, seg in rows:
    key = 'import' if k in ('Import', 'ImportFrom') else ('assert' if k == 'Assert' else ('def/class' if k in ('FunctionDef', 'ClassDef') else ('print' if seg.startswith('print(') else k)))
    kinds[key] = kinds.get(key, 0) + dt
print('%s: %.1f s in %d statements; by kind %s' % (os.path.basename(path), tot, len(rows), {k: round(v, 1) for k, v in sorted(kinds.items(), key=lambda kv: -kv[1])}))
for dt, ln, k, seg in sorted(rows, reverse=True)[:8]: print('   %5.1f s  line %4d  %s' % (dt, ln, seg))
