#!/usr/bin/env python3
"""daemon_census.py — THE DAEMON-EDGE GATE (D9-ii, 2026-09-07; THE DAEMON CAMPAIGN
owner-ruled 2026-09-06, "that works"). Run by run_cold_all.py after the
dependency gate, before any cell is graded. The dependency gate's twin for the
simulator: what the dependency gate does for the ink's cross-references between
compiled spans, this does for the EVENTS a compiled function fires on and the
EFFECTS it writes.

What it measures, BY SCRIPT, from World/step9/cold_run_*.py and world_engine.py:
  1. every DAEMON — a top-level `def law_*(event, world)` — with the event kinds
     it watches (the `k == 'x'` / `event['kind'] == 'x'` branches), the fields it
     reads, and the effects each branch writes; and whether its body ever calls
     `.submit(` (THE FENCE: a daemon consumes events and writes the ledger — it
     never emits an event);
  2. every SUBMIT on a scene tape — explicit dicts, the tuple-driven tapes, the
     loop-driven sources — so a watched kind no tape fires, and a fired kind no
     daemon watches, are both visible;
  3. every COMPILED FUNCTION that writes the world: a top-level def whose source
     names a registered effect (the infrastructure names excluded), or the module
     itself where a table-shaped runner keeps its effects at module level.

What daemon_dispositions.yaml must DECLARE, and the gate verifies:
  daemons:    every daemon, its file, the runner it wraps, and its WATCHES —
              {kind: [effects]} — which must equal the parse exactly (a daemon
              edited without its declaration fails; the file may never under- or
              overstate the code);
  functions:  every compiled function's disposition —
                WRAPPED  by: a declared daemon that shares at least one effect
                         with the function (or, for a table-shaped runner, with
                         the module) — the wrap's live check, as CALL's is the
                         live import;
                OWED     why names a wrap-worklist line of COMPILE_DEBT.md before
                         "|" — the generated worklist (--debt);
                NONE     why says why no daemon is owed (reserved for the wraps);
  unfired:    every watched kind no tape submits, with a why;
  unconsumed: every submitted kind no daemon watches, with a why.
Every watched and submitted kind must be in event_vocabulary.yaml; every effect a
daemon writes must be in effect_vocabulary.yaml. The registry's aliases_in_code
(one act under two names, one name over two acts) are printed as OPEN ALIASES —
findings the wraps must close — and listed on the worklist.
The gate WRITES World/step9/DAEMON_INDEX.md each run (documentation, never
runtime). Coverage is printed first. Exit 1 on any failure.

Run: python3 World/step9/daemon_census.py [--emit] [--debt] [--no-index]
  --emit prints yaml stubs for every undispositioned function / unfired /
         unconsumed kind; --debt prints the OWED worklist by runner.
"""
import ast, glob, os, re, sys
from collections import defaultdict, OrderedDict
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import effects_layer as FX
import events_layer as EV

YAML = os.path.join(HERE, 'daemon_dispositions.yaml')
DEBT = os.path.join(HERE, 'COMPILE_DEBT.md')
INDEX = os.path.join(HERE, 'DAEMON_INDEX.md')
INFRA = {'cell', 'out', 'scene', 'scene_cell', 'build', 'run'}     # the runners' plumbing: never a compiled law
STATUSES = ('WRAPPED', 'OWED', 'NONE')


def runner_name(path):
    b = os.path.basename(path)
    return b[len('cold_run_'):-3] if b.startswith('cold_run_') else b[:-3]


def _balanced(text, start):
    depth, i, in_str = 0, start, None
    while i < len(text):
        c = text[i]
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == in_str:
                in_str = None
        elif c in ('"', "'"):
            in_str = c
        elif c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None


def parse_submits(src, base):
    """every .submit( on the module's tapes -> [(kind, subject, case_source, fields)]"""
    out = []
    for m in re.finditer(r'\.submit\(', src):
        end = _balanced(src, m.end() - 1)
        body = src[m.end():end - 1]
        pre = src[max(0, m.start() - 3000):m.start()]
        kind = re.search(r"'kind':\s*'([a-z_]+)'", body)
        subj = re.search(r"'subject':\s*'([^']+)'", body)
        fields = sorted(set(re.findall(r"'([a-z_]+)':", body)) - {'kind', 'subject', 'case_source', 'law'})
        cs = re.search(r"'case_source':\s*((?:'[^']*'\s*)+)", body)
        source = ''.join(re.findall(r"'([^']*)'", cs.group(1))) if cs else None
        if kind:
            if source is None or '%' in source:
                loop = re.findall(r"for [^\n]*? in [\(\[](.*?)[\)\]]:\s*$", pre, re.S | re.M)
                refs = re.findall(r"'((?:Gen|Exod|Lev|Num|Deut|Sifra|Mishnah)[^']*)'", loop[-1]) if loop else []
                if source and '%' in source:
                    nums = re.findall(r"\((\d+),\s*(\d+)\)", loop[-1]) if loop else []
                    refs = [source.replace('%d', v) for _, v in nums] or [source]
                source = '; '.join(refs) if refs else '?'
            out.append((kind.group(1), subj.group(1) if subj else '?', source, fields))
        else:
            loop = re.findall(r"for k, s, src in \((.*?)\):\s*$", pre, re.S | re.M)
            tape = re.findall(r"tape = \[(.*?)\]\s*$", pre, re.S | re.M)
            lst = loop[-1] if loop else (tape[-1] if tape else None)
            if lst:
                for t in re.findall(r"\('([a-z_]+)',\s*'([^']+)',\s*'([^']+)'\)", lst):
                    out.append((t[0], t[1], t[2], []))
            else:
                out.append(('?UNRESOLVED?', '?', body[:60].replace('\n', ' '), []))
    return out


def parse_daemons(src, base):
    """every def law_*(event, world) -> name -> {kinds: {kind: {fields, effects}}, submits: bool}"""
    daemons = OrderedDict()
    for dm in re.finditer(r"^def (law_[a-z_0-9]+)\(event, world\):\n(.*?)(?=^def |^class |^[A-Z_]+ = |\Z)", src, re.S | re.M):
        name, body = dm.group(1), dm.group(2)
        kinds = OrderedDict()
        cond = re.compile(r"(?<![A-Za-z0-9_])(?:k|event\['kind'\])\s*(==|!=)\s*'([a-z_]+)'")   # W2 (2026-09-07): a word boundary before k — `pk == 'x'` is not a kind branch
        pieces = list(cond.finditer(body))
        for i, p in enumerate(pieces):
            seg_end = pieces[i + 1].start() if i + 1 < len(pieces) else len(body)
            seg = body[p.end():seg_end] if p.group(1) == '==' else body[p.end():]
            effs = re.findall(r"E_?\('([a-z_]+)'", seg) + re.findall(r"'effect':\s*'([a-z_]+)'", seg)
            for cond_expr in re.findall(r"'effect':\s*\((.*?)\),\s*\n", seg, re.S):
                cond_expr = re.sub(r"event(?:\.get\(|\[)'[a-z_]+'\)?\]?", '', cond_expr)
                effs += re.findall(r"'([a-z_]+)'", cond_expr)
            if 'GUARDIAN_MATRIX[' in seg:
                mat = re.search(r"GUARDIAN_MATRIX = \{(.*?)\n\}", src, re.S)
                effs += sorted(set(re.findall(r":\s*'([a-z_]+)'", mat.group(1)))) if mat else ['?MATRIX?']
            flds = sorted(set(re.findall(r"event(?:\.get\(|\[)'([a-z_]+)'", seg)) - {'kind', 'subject', 'case_source', 'law'})
            k = p.group(2)
            d = kinds.setdefault(k, {'fields': [], 'effects': []})
            d['fields'] = sorted(set(d['fields']) | set(flds))
            d['effects'] = list(OrderedDict.fromkeys(d['effects'] + [e for e in effs if e]))
        daemons[name] = {'file': base, 'kinds': kinds, 'submits': bool(re.search(r'\.submit\(', body))}
    return daemons


def _effect_strings(node):
    """every registered-effect string constant inside an expression's AST (a list, a conditional, a sum, a call)"""
    return {c.value for c in ast.walk(node) if isinstance(c, ast.Constant) and isinstance(c.value, str) and c.value in FX.REGISTRY}


def _call_name(c):
    f = c.func
    return f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else None)


def written_effects(fn_node):
    """O3 THE GATE ITEMS (2026-09-07; REPORT_GATE_ITEMS.md): the effects a function WRITES — read from the forms that write, never from
    every string that spells an effect (THE VALUE/EFFECT HOMOGRAPH: a tier name, a cell value, a verdict value, a ledger read, a close
    note). The forms: the fx argument (the fourth) of a cell(...) call — any expression, a local NAME resolved to its assignments inside
    the function; the effects argument (the second) of out(...); the first argument of an E(...) / E_(...) call; an effect dict literal
    {'effect': 'x'}. A bare string as a cell's fourth argument is a note (the yoma shape), not fx."""
    effs, locals_ = set(), {}
    for c in ast.walk(fn_node):
        if isinstance(c, (ast.Assign, ast.AugAssign)):
            tgt = c.targets[0] if isinstance(c, ast.Assign) else c.target
            if isinstance(tgt, ast.Name):
                locals_.setdefault(tgt.id, set()).update(_effect_strings(c.value))
    def expr_effects(a):
        if isinstance(a, ast.Constant):
            return set()                                     # a bare string: a note, not fx
        if isinstance(a, ast.Name):
            return set(locals_.get(a.id, ()))
        out = _effect_strings(a)
        for n in ast.walk(a):
            if isinstance(n, ast.Name) and n.id in locals_:
                out |= locals_[n.id]
        return out
    for c in ast.walk(fn_node):
        if isinstance(c, ast.Call):
            name = _call_name(c)
            if name == 'cell' and len(c.args) >= 4:
                effs |= expr_effects(c.args[3])
            elif name == 'out' and len(c.args) >= 2:
                effs |= expr_effects(c.args[1])
            elif name in ('E', 'E_') and c.args and isinstance(c.args[0], ast.Constant) and c.args[0].value in FX.REGISTRY:
                effs.add(c.args[0].value)
        elif isinstance(c, ast.Dict):
            for k, v in zip(c.keys, c.values):
                if isinstance(k, ast.Constant) and k.value == 'effect' and isinstance(v, ast.Constant) and v.value in FX.REGISTRY:
                    effs.add(v.value)
    return sorted(effs)


def parse_functions(src, base):
    """the compiled functions that write the world: name -> sorted effects (the WRITING forms only — O3); plus the module's own effect set"""
    tree = ast.parse(src)
    cands, cells = OrderedDict(), {}
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef) or node.name in INFRA or node.name.startswith('law_'):
            continue
        seg = ast.get_source_segment(src, node) or ''
        effs = written_effects(node)
        if effs:
            cands[node.name] = effs
            cells[node.name] = seg.count('cell(')     # the modern shape carries its effects in its own cells; the older
                                                      # shape (no cell( call) has them attached by a module-level mapping
    module_effs = sorted(set(e for e in re.findall(r"'([a-z_]+)'", src) if e in FX.REGISTRY))
    if not cands and base.startswith('cold_run_') and 'effects_layer' in src and module_effs:
        cands['<module>'] = module_effs          # a table-shaped runner: its effects live at module level (the engine is not a runner)
        cells['<module>'] = 0
    return cands, module_effs, cells


def parse_all():
    files = sorted(glob.glob(os.path.join(HERE, 'cold_run_*.py'))) + [os.path.join(HERE, 'world_engine.py')]
    R = OrderedDict()
    for f in files:
        src = open(f, encoding='utf-8').read()
        base = os.path.basename(f)
        cands, module_effs, cells = parse_functions(src, base)
        R[runner_name(f)] = {'file': base, 'submits': parse_submits(src, base), 'daemons': parse_daemons(src, base),
                             'functions': cands, 'module_effects': module_effs, 'cells': cells}
    return R


def load_yaml():
    if not os.path.exists(YAML):
        sys.exit('DAEMON GATE: %s missing — every daemon must declare its watches and every compiled function its disposition' % YAML)
    d = yaml.safe_load(open(YAML, encoding='utf-8')) or {}
    return d.get('daemons') or {}, d.get('functions') or {}, d.get('unfired') or {}, d.get('unconsumed') or {}


def main():
    emit = '--emit' in sys.argv
    R = parse_all()
    daemons = OrderedDict((n, dict(d, runner=r)) for r, v in R.items() for n, d in v['daemons'].items())
    submits = [(r, k, s, cs, f) for r, v in R.items() for (k, s, cs, f) in v['submits']]
    funcs = OrderedDict((r, v['functions']) for r, v in R.items() if v['functions'])
    n_funcs = sum(len(v) for v in funcs.values())
    watched = OrderedDict()
    for n, d in daemons.items():
        for k in d['kinds']:
            watched.setdefault(k, []).append(n)
    submitted = OrderedDict()
    for r, k, s, cs, f in submits:
        submitted.setdefault(k, []).append((r, s, cs))
    print('DAEMON GATE coverage: %d modules scanned (%d runners + the engine); %d daemons watching %d kinds; %d submit records firing %d kinds; %d compiled functions writing effects in %d runners; event registry %d types, effects registry %d'
          % (len(R), len(R) - 1, len(daemons), len(watched), len(submits), len(submitted), n_funcs, len(funcs), len(EV.REGISTRY), len(FX.REGISTRY)))
    assert daemons and submits and funcs, 'ZERO-REPORT: the parse found nothing — the patterns are wrong'

    dy, fy, unfired_y, unconsumed_y = load_yaml()
    debt_text = open(DEBT, encoding='utf-8').read() if os.path.exists(DEBT) else ''
    fails, warns, stubs = [], [], {'daemons': {}, 'functions': {}, 'unfired': {}, 'unconsumed': {}}

    # ---- 1. the daemons: declared == parsed; the fence; the registries ----
    for n, d in daemons.items():
        if d['submits']:
            fails.append('THE FENCE: %s (%s) calls .submit( inside its body — a daemon may not emit an event' % (n, d['file']))
        for k, v in d['kinds'].items():
            if k not in EV.REGISTRY:
                fails.append('%s watches %r — not in event_vocabulary.yaml' % (n, k))
            for e in v['effects']:
                if e not in FX.REGISTRY:
                    fails.append('%s writes %r on %r — not in effect_vocabulary.yaml' % (n, e, k))
        decl = dy.get(n)
        if decl is None:
            fails.append('daemon %s (%s) has no declaration in daemon_dispositions.yaml' % (n, d['file']))
            stubs['daemons'][n] = {'file': d['file'], 'wraps': d['runner'], 'watches': {k: v['effects'] for k, v in d['kinds'].items()}}
            continue
        if decl.get('file') != d['file']:
            fails.append('daemon %s declared in %s, found in %s' % (n, decl.get('file'), d['file']))
        dw = decl.get('watches') or {}
        pw = {k: v['effects'] for k, v in d['kinds'].items()}
        if set(dw) != set(pw):
            fails.append('daemon %s: declared watches %s != parsed %s' % (n, sorted(set(dw) - set(pw)) or '', sorted(set(pw) - set(dw)) or ''))
        for k in set(dw) & set(pw):
            if sorted(set(dw[k] or [])) != sorted(set(pw[k])):
                fails.append('daemon %s on %r: declared effects %s != parsed %s' % (n, k, sorted(set(dw[k] or [])), sorted(set(pw[k]))))
    for n in dy:
        if n not in daemons:
            fails.append('daemon_dispositions.yaml declares %s but no def law_%s exists' % (n, n[4:]))

    # ---- 2. the tape: registered kinds; watched-never-fired; fired-never-watched ----
    for k, rows in submitted.items():
        if k not in EV.REGISTRY:
            fails.append('submitted kind %r (%s) is not in event_vocabulary.yaml' % (k, ', '.join(sorted({r for r, _, _ in rows}))))
    unfired = [k for k in watched if k not in submitted]
    unconsumed = [k for k in submitted if k not in watched]
    for k in unfired:
        if k not in unfired_y:
            fails.append('kind %r is watched by %s and submitted on NO tape — declare it under unfired: with a why' % (k, ', '.join(watched[k])))
            stubs['unfired'][k] = 'watched by %s; no tape fires it — why' % ', '.join(watched[k])
    for k in unfired_y:
        if k not in unfired:
            fails.append('unfired: declares %r but a tape now submits it (or no daemon watches it) — the file overstates' % k)
    for k in unconsumed:
        if k not in unconsumed_y:
            fails.append('kind %r is submitted (%s) and watched by NO daemon — declare it under unconsumed: with a why' % (k, ', '.join(sorted({r for r, _, _ in submitted[k]}))))
            stubs['unconsumed'][k] = 'submitted by %s; no daemon watches it — why' % ', '.join(sorted({r for r, _, _ in submitted[k]}))
    for k in unconsumed_y:
        if k not in unconsumed:
            fails.append('unconsumed: declares %r but a daemon now watches it (or no tape submits it) — the file overstates' % k)
    aliases = [(k, e['aliases_in_code']) for k, e in EV.REGISTRY.items() if e.get('aliases_in_code')]

    # ---- 3. the compiled functions: every one dispositioned; WRAPPED verified; OWED on the worklist ----
    owed = defaultdict(list)
    wrapped_n = none_n = 0
    for r, fns in funcs.items():
        decl_r = fy.get(r) or {}
        for fn, effs in fns.items():
            d = decl_r.get(fn)
            if d is None:
                fails.append('function %s.%s writes %s and has no disposition' % (r, fn, ', '.join(effs[:4]) + (' ...' if len(effs) > 4 else '')))
                stubs['functions'].setdefault(r, {})[fn] = {'status': 'OWED', 'why': 'W? — the %s wrap sitting | effects: %s' % (r, ', '.join(effs))}
                continue
            st = d.get('status')
            if st not in STATUSES:
                fails.append('function %s.%s: status %r not in %s' % (r, fn, st, STATUSES))
            elif st == 'WRAPPED':
                by = d.get('by')
                if by not in daemons:
                    fails.append('function %s.%s declared WRAPPED by %r — no such daemon' % (r, fn, by))
                else:
                    deffs = set(e for v in daemons[by]['kinds'].values() for e in v['effects'])
                    shared = set(effs) & deffs
                    level = 'function'
                    if not shared and R[r]['cells'].get(fn, 0) == 0:
                        # the older shape: a verdict function whose effects a module-level mapping attaches
                        # (vayikra5's effect_of; a table-shaped runner's <module>) — the module's set stands in;
                        # a function that carries its own cells must share at the function level
                        shared = set(R[r]['module_effects']) & deffs
                        level = 'module'
                    if not shared:
                        fails.append('function %s.%s declared WRAPPED by %s but shares no effect with it at the function level%s' % (r, fn, by, '' if R[r]['cells'].get(fn, 0) else ' (or the module level)'))
                    else:
                        d['_verified'] = '%s level: %s' % (level, ', '.join(sorted(shared)[:3]))
                        wrapped_n += 1
            elif st == 'OWED':
                why = d.get('why') or ''
                line = why.split('|')[0].strip()
                if not line or line not in debt_text:
                    fails.append('function %s.%s OWED — why must name a COMPILE_DEBT.md wrap line before "|": %r' % (r, fn, line))
                owed[r].append((fn, why))
            else:
                if not d.get('why'):
                    fails.append('function %s.%s NONE without a why' % (r, fn))
                none_n += 1
        for fn in decl_r:
            if fn not in fns:
                fails.append('daemon_dispositions.yaml dispositions %s.%s but no such effect-carrying function exists — the file overstates' % (r, fn))
    for r in fy:
        if r not in funcs:
            fails.append('daemon_dispositions.yaml has functions for %r but the runner has no effect-carrying function' % r)

    n_owed = sum(len(v) for v in owed.values())
    print('DAEMON GATE functions: %d WRAPPED (verified), %d OWED, %d NONE of %d; unfired kinds %d, unconsumed %d, open aliases %d'
          % (wrapped_n, n_owed, none_n, n_funcs, len(unfired), len(unconsumed), len(aliases)))
    for k, a in aliases:
        warns.append('OPEN ALIAS %s — %s' % (k, a[:140]))
    if emit and any(stubs.values()):
        print('\n# ---- yaml stubs for the undispositioned ----')
        print(yaml.safe_dump({s: v for s, v in stubs.items() if v}, allow_unicode=True, sort_keys=False, width=200))
    if '--debt' in sys.argv:
        print('\nOWED WRAP WORKLIST (generated from the dispositions): %d functions in %d runners' % (n_owed, len(owed)))
        for r in owed:
            print('  %s: %s' % (r, ', '.join(fn for fn, _ in owed[r])))
        for k in unfired:
            print('  UNFIRED %s — %s' % (k, unfired_y.get(k, '')))
        for k in unconsumed:
            print('  UNCONSUMED %s — %s' % (k, unconsumed_y.get(k, '')))
        for w in warns:
            print('  ' + w)

    # ---- the generated index ----
    if '--no-index' not in sys.argv:
        L = ['# THE DAEMON INDEX — GENERATED by daemon_census.py from daemon_dispositions.yaml and the parse of',
             '# World/step9/cold_run_*.py + world_engine.py. Do not edit: rerun the gate. Documentation; never a runtime path.',
             '#',
             '# coverage: %d modules; %d daemons watching %d kinds; %d submit records firing %d kinds; %d compiled functions in %d runners — %d WRAPPED, %d OWED, %d NONE; unfired %d; unconsumed %d; open aliases %d'
             % (len(R), len(daemons), len(watched), len(submits), len(submitted), n_funcs, len(funcs), wrapped_n, n_owed, none_n, len(unfired), len(unconsumed), len(aliases)), '']
        L.append('## THE DAEMONS')
        for n, d in daemons.items():
            L.append('- %s (%s; wraps %s): %d kinds' % (n, d['file'], (dy.get(n) or {}).get('wraps', '?'), len(d['kinds'])))
            for k, v in d['kinds'].items():
                fired_by = sorted({r for r, _, _ in submitted.get(k, [])})
                L.append('  - %s%s -> %s%s' % (k, (' [%s]' % ', '.join(v['fields'])) if v['fields'] else '', ', '.join(v['effects']) or 'no ledger write',
                                              ('  (fired by %s)' % ', '.join(fired_by)) if fired_by else '  (NEVER FIRED)'))
        L.append('')
        L.append('## THE TAPE — kinds submitted, by module')
        for r, v in R.items():
            ks = OrderedDict()
            for k, s, cs, f in v['submits']:
                ks.setdefault(k, []).append(s)
            if ks:
                L.append('- %s: %s' % (v['file'], ', '.join('%s%s' % (k, '' if k in watched else ' (UNCONSUMED)') for k in ks)))
        L.append('')
        L.append('## THE COMPILED FUNCTIONS — dispositions')
        for r, fns in funcs.items():
            L.append('### %s (%s)' % (r, R[r]['file']))
            for fn, effs in fns.items():
                d = (fy.get(r) or {}).get(fn) or {}
                st = d.get('status', 'UNDISPOSITIONED')
                extra = (' by %s (%s)' % (d.get('by'), d.get('_verified', 'UNVERIFIED'))) if st == 'WRAPPED' else ((' — ' + d.get('why', '')) if d.get('why') else '')
                L.append('- %s: %s%s  [effects: %s]' % (fn, st, extra, ', '.join(effs)))
            L.append('')
        if unfired or unconsumed or aliases:
            L.append('## OPEN — the findings the wraps must close')
            for k in unfired:
                L.append('- UNFIRED %s (watched by %s): %s' % (k, ', '.join(watched[k]), unfired_y.get(k, '')))
            for k in unconsumed:
                L.append('- UNCONSUMED %s: %s' % (k, unconsumed_y.get(k, '')))
            for k, a in aliases:
                L.append('- ALIAS %s: %s' % (k, a))
        with open(INDEX, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(L) + '\n')
        print('index: World/step9/DAEMON_INDEX.md regenerated (%d daemons, %d functions)' % (len(daemons), n_funcs))
    if fails:
        print('\nDAEMON GATE: %d failure(s)' % len(fails))
        for f in fails:
            print('  FAIL', f)
        sys.exit(1)
    print('DAEMON GATE: every daemon declared and its watches verified; every kind and effect registered; every compiled function dispositioned; every WRAPPED verified; every OWED on the worklist [gate satisfied]')


if __name__ == '__main__':
    main()
