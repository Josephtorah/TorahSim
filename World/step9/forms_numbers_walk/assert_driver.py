# run a module statement by statement, collecting EVERY failing assert at once (sitting 1's lesson on cuts, applied to the asserts)
import ast, sys, traceback
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'naso_ink', '__file__': path}
fails = []
for node in tree.body:
    seg = ast.get_source_segment(src, node)
    try: exec(compile(ast.Module([node], []), path, 'exec'), ns)
    except AssertionError as e: fails.append((node.lineno, seg[:160].replace('\n', ' '), repr(e)[:400]))
    except Exception as e: fails.append((node.lineno, seg[:160].replace('\n', ' '), 'ERROR ' + repr(e)[:300]))
print(f'{len(fails)} failing statements')
for ln, seg, msg in fails: print(f'--- line {ln}: {seg}\n    {msg}')
