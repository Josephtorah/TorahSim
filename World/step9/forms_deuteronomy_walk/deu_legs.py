# THE LEG DIAGNOSTIC (sitting 6's lesson): exec the ink module's non-assert statements, then print each failing assert's legs one by one
import ast, sys
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'deu_ink', '__file__': path}
for node in tree.body:
    if isinstance(node, ast.Assert): continue
    try: exec(compile(ast.Module([node], []), path, 'exec'), ns)
    except Exception as ex: print('NONASSERT ERROR line', node.lineno, repr(ex)[:200])
LEGS = [l.strip() for l in open(sys.argv[2], encoding='utf-8').read().split('\n') if l.strip() and not l.startswith('#')]
for e in LEGS:
    try: print(f'{e}  =>  {eval(e, ns)!r}')
    except Exception as ex: print(f'{e}  =>  ERROR {ex!r}')
