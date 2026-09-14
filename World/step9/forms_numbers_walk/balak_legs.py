#!/usr/bin/env python3
# THE LEG-BY-LEG DIAGNOSTIC (sitting 6's lesson): a compound assert's failure names nothing — run the module statement by statement,
# and for every failing assert whose test is an AND-chain, evaluate each leg alone and print the failing legs with the LEFT side's value.
import ast, sys, unicodedata
path = sys.argv[1]; src = open(path, encoding='utf-8').read(); tree = ast.parse(src); ns = {'__name__': 'balak_ink', '__file__': path}
for node in tree.body:
    seg = ast.get_source_segment(src, node)
    try:
        exec(compile(ast.Module([node], []), path, 'exec'), ns)
    except AssertionError:
        print(f'=== line {node.lineno}')
        legs = node.test.values if isinstance(node.test, ast.BoolOp) and isinstance(node.test.op, ast.And) else [node.test]
        for leg in legs:
            try:
                ok = eval(compile(ast.Expression(leg), path, 'eval'), ns)
            except Exception as e:
                ok = f'ERROR {e!r}'
            if ok is True: continue
            lsrc = ast.get_source_segment(src, leg)
            val = ''
            if isinstance(leg, ast.Compare):
                try:
                    lv = eval(compile(ast.Expression(leg.left), path, 'eval'), ns)
                    val = repr(lv)
                    if isinstance(lv, str) and leg.comparators and isinstance(leg.comparators[0], ast.Constant) and isinstance(leg.comparators[0].value, str):
                        typed = leg.comparators[0].value
                        val += f'  [NFC-equal to the typed form: {unicodedata.normalize("NFC", lv) == unicodedata.normalize("NFC", typed)}; codepoints db {[hex(ord(c)) for c in lv]} typed {[hex(ord(c)) for c in typed]}]'
                except Exception as e:
                    val = f'ERROR {e!r}'
            print(f'  LEG: {lsrc[:220]}\n     -> {str(ok)[:60]} ; value: {val[:700]}')
    except Exception as e:
        print(f'=== line {node.lineno} ERROR {e!r}')
print('done')
