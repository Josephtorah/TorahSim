#!/usr/bin/env python3
"""edit_ch32b_copier_lists.py — the copier's lists extended for the tail's second half (edit_ch32b_tail2_writers.py wrote its four files and tripped on its own last
check before this fifth: an f-string in the OUT comprehension is an ast.JoinedStr, not a Constant — the check corrected here). By ast: the list literal's closing bracket."""
import ast, os, re
SP = os.path.dirname(os.path.abspath(__file__))
cp = open(f'{SP}/copy_ch32_forms.py', encoding='utf-8').read(); b = cp.encode('utf-8'); t = ast.parse(cp); starts = [0]
for line in b.split(b'\n'): starts.append(starts[-1] + len(line) + 1)
ADDS = {'PY': ['patch_runner_fbind_ch32b.py', 'edit_ch32b_tail2_writers.py', 'edit_ch32b_copier_lists.py', 'write_ch32b_point4.py'],
        'OUT': ['ch32b_runner_fbind_check.out', 'ch32b_runner_fbind.out', 'ch32b_runner_lint2.out', 'ch32b_tail_chain2.sh', 'ch32b_tail_chain2.log', 'ch32b_tail_chain2.DONE', 'ch32_runner_run5.out', 'ch32b_cache_clear2.out', 'ch32b_gates3_SUMMARY.txt', 'ch32b_gates3.log', 'ch32b_writers_edit.out', 'ch32b_copier_lists.out', 'ch32b_point4_check.out', 'ch32b_point4_write.out', 'ch32b_forms5.out', 'ch32b_home5.out']}
ins = []
for n in t.body:
    if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ADDS:
        v = n.value
        while isinstance(v, ast.BinOp): v = v.left
        assert isinstance(v, ast.List), (n.targets[0].id, type(v).__name__)
        end = starts[v.end_lineno - 1] + v.end_col_offset - 1; assert b[end:end + 1] == b']', b[end - 20:end + 2]
        present = {e.value for e in v.elts if isinstance(e, ast.Constant)}; new = [x for x in ADDS[n.targets[0].id] if x not in present]
        ins.append((end, (', ' + ', '.join(repr(x) for x in new)).encode('utf-8'), n.targets[0].id, len(new)))
assert len(ins) == 2 and all(k for _, _, _, k in ins), ins
for end, txt, nm, k in sorted(ins, reverse=True): b = b[:end] + txt + b[end:]
cp2 = b.decode('utf-8'); t2 = ast.parse(cp2)
got = {n.targets[0].id: n.value for n in t2.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ADDS}
consts = {k: {e.value for e in ast.walk(v) if isinstance(e, ast.Constant) and isinstance(e.value, str)} for k, v in got.items()}
assert all(x in consts[k] for k in ADDS for x in ADDS[k]) and any(isinstance(e, ast.JoinedStr) for e in ast.walk(got['OUT'])), 'the copier lists'
assert os.path.expanduser('~') not in cp2 and SP not in cp2
open(f'{SP}/copy_ch32_forms.py', 'w', encoding='utf-8').write(cp2)
print('the copier lists: PY +%d, OUT +%d; the spine comprehension kept | WRITTEN' % tuple(k for _, _, nm, k in sorted(ins, key=lambda x: x[2] != 'PY')))
