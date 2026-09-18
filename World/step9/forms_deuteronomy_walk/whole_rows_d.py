#!/usr/bin/env python3
# THE WHOLE-ROW FIX, part (d) (2026-09-17): every row of a committed docket's dump longer than the 650-character print, printed WHOLE beside the
# verdict and note its part gave it — chunk files in the scratchpad, read one by one against the verdict. N = whole, never a cut.
import re, os, sys, importlib.util
ROOT = __import__('subprocess').check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__)); F = f'{ROOT}/World/step9/forms_deuteronomy_walk'
def load(parts, folder):
    V = {}
    for p in parts:
        spec = importlib.util.spec_from_file_location(p, f'{folder}/{p}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for addr, vd, note in m.ROWS:
            assert addr not in V, addr; V[addr] = (vd, note)
    return V
def run(tag, dump_path, parts, folder, expect_rows, expect_long, chunk):
    dump = open(dump_path, encoding='utf-8').read()
    V = load(parts, folder)
    blocks = dump.split('\n## ')[1:]
    rows = []
    for b in blocks:
        head, _, text = b.partition('\n')
        m = re.match(r'\[(LINK|TOPIC)\] (.+?)  (.*)$', head); assert m, head
        addr = m.group(2).strip(); text = ' '.join(text.split())
        assert addr in V, addr
        rows.append((m.group(1), addr, m.group(3).strip(), text))
    assert len(rows) == expect_rows, len(rows)
    long = [r for r in rows if len(r[3]) > 650]
    assert len(long) == expect_long, len(long)
    n = 0; files = []
    for c in range(0, len(long), chunk):
        n += 1; out = f'{SCR}/whole_{tag}_{n}.txt'; files.append(out)
        with open(out, 'w', encoding='utf-8') as fh:
            for i, (k, addr, rest, text) in enumerate(long[c:c + chunk], c + 1):
                vd, note = V[addr]
                fh.write(f'==== [{i}/{len(long)}] {addr} [{k}{(" — " + rest) if rest else ""}] — {vd}. {note}\n{text}\n\n')
        print(tag, n, out.rsplit("/", 1)[1], len(long[c:c + chunk]), 'rows', os.path.getsize(out), 'bytes')
    print(tag, 'LONG', len(long), 'of', len(rows), 'chars', sum(len(r[3]) for r in long))
run('ch4', f'{F}/ch4_docket_dump.txt', [f'ch4_docket_{p}' for p in 'ABCD'], F, 327, 114, 38)
run('deu', f'{SCR}/deu_docket_dump.txt', [f'deu_docket_{p}' for p in 'ABCDEFGH'], F, 864, 215, 54)
