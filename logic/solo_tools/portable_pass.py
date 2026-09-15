#!/usr/bin/env python3
"""portable_pass.py — THE PORTABLE REPO's one pass (2026-09-15; reviews/PORTABLE_repo_2026-09-15.md, decisions P1 ONE ROOT FROM THE FILE'S
OWN PLACE and P2 THE STORE LIVES IN THE REPO). Kept as the record of the pass.

    python3 logic/solo_tools/portable_pass.py --dry      # count what would change, file by file, nothing written
    python3 logic/solo_tools/portable_pass.py --apply    # rewrite; a second run finds nothing to do

WHAT IT DOES, per tracked Python file (ARCHITECTURE/ excluded — the design thread's; the never-commit set is untracked anyway):
  - every STRING token that carries the old absolute path becomes `(_ROOT + '<the rest>')` — a literal that is only the path becomes
    `_ROOT`; a path inside a longer string splits around it; the old store path elijah_docket/tanakh.sqlite becomes Data/tanakh.sqlite;
  - a docstring or a comment keeps its text with the new absolute name (documentation, not code);
  - an f-string piece carrying the path gets `{_ROOT}` in its place;
  - `import os as _os` and `_ROOT = ...` (the repo root computed from __file__ by the file's own depth) are inserted after the module
    docstring and any __future__ imports, once, only in files that need `_ROOT`.
Shell scripts: the old path becomes "$ROOT" with ROOT computed from git at the top. JSON files are listed, never touched.
"""
import os, sys, io, re, ast, tokenize, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
OLD = '<repo-old>'
NEW_NAME = '<repo>'
STORE_OLD, STORE_NEW = 'elijah_docket/tanakh.sqlite', 'Data/tanakh.sqlite'
EXCLUDE = ('ARCHITECTURE/',)
LIT = re.compile(r"^([rRbBuU]*)('''|\"\"\"|'|\")(.*)\2$", re.S)
ROOT_LINE = "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), %s))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place"


def tracked():
    out = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, cwd=ROOT).stdout
    return [l for l in out.split('\n') if l.strip() and not l.startswith(EXCLUDE)]


def rebuild(lit):
    """a code string carrying the old path → an expression over _ROOT; the store path renamed inside every piece"""
    m = LIT.match(lit)
    if not m or 'b' in m.group(1).lower():
        return None
    prefix, q, body = m.group(1), m.group(2), m.group(3)
    parts = [p.replace(STORE_OLD, STORE_NEW) for p in body.split(OLD)]
    pieces = []
    for k, part in enumerate(parts):
        if part:
            pieces.append('%s%s%s%s' % (prefix, q, part, q))
        if k < len(parts) - 1:
            pieces.append('_ROOT')
    return pieces[0] if len(pieces) == 1 else '(' + ' + '.join(pieces) + ')'


def is_docstring(toks, i):
    j = i - 1
    while j >= 0 and toks[j].type in (tokenize.NL, tokenize.COMMENT):
        j -= 1
    before = toks[j].type if j >= 0 else tokenize.NEWLINE
    k = i + 1
    while k < len(toks) and toks[k].type in (tokenize.NL, tokenize.COMMENT):
        k += 1
    after = toks[k].type if k < len(toks) else tokenize.NEWLINE
    return before in (tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT, tokenize.ENCODING) and after in (tokenize.NEWLINE, tokenize.ENDMARKER)


def insertion_line(src):
    """the line (1-based, insert BEFORE it) after the module docstring and any __future__ imports"""
    tree = ast.parse(src)
    line = 1
    for st in tree.body:
        if isinstance(st, ast.Expr) and isinstance(st.value, ast.Constant) and isinstance(st.value.value, str) and st is tree.body[0]:
            line = st.end_lineno + 1; continue
        if isinstance(st, ast.ImportFrom) and st.module == '__future__':
            line = st.end_lineno + 1; continue
        break
    return line


def rewrite_py(src, depth):
    """returns (new source, counts) — counts by kind; the source unchanged when nothing carries the path"""
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    edits, counts = [], {'code': 0, 'doc': 0, 'comment': 0, 'fstring': 0, 'store_only': 0}
    for i, t in enumerate(toks):
        s = t.string
        if t.type == tokenize.STRING and (OLD in s or STORE_OLD in s):
            if is_docstring(toks, i):
                new = s.replace(OLD, NEW_NAME).replace(STORE_OLD, STORE_NEW); counts['doc'] += 1
            elif OLD in s:
                new = rebuild(s)
                if new is None:
                    continue
                counts['code'] += 1
            else:
                new = s.replace(STORE_OLD, STORE_NEW); counts['store_only'] += 1
            edits.append((t.start, t.end, new))
        elif t.type == tokenize.COMMENT and (OLD in s or STORE_OLD in s):
            edits.append((t.start, t.end, s.replace(OLD, NEW_NAME).replace(STORE_OLD, STORE_NEW))); counts['comment'] += 1
        elif getattr(tokenize, 'FSTRING_MIDDLE', None) is not None and t.type == tokenize.FSTRING_MIDDLE and (OLD in s or STORE_OLD in s):
            edits.append((t.start, t.end, s.replace(OLD, '{_ROOT}').replace(STORE_OLD, STORE_NEW))); counts['fstring'] += 1
    if not edits:
        return src, counts
    lines = src.split('\n')
    for (sr, sc), (er, ec), new in sorted(edits, key=lambda e: e[0], reverse=True):
        head = lines[sr - 1][:sc]; tail = lines[er - 1][ec:]
        lines[sr - 1:er] = (head + new + tail).split('\n')
    out = '\n'.join(lines)
    if counts['code'] or counts['fstring']:
        ups = ', '.join(["'..'"] * depth)
        root_line = ROOT_LINE % ups if depth else "_ROOT = _os.path.dirname(_os.path.abspath(__file__))   # THE PORTABLE REPO (2026-09-15): the repo root is this file's own folder"
        at = insertion_line(out)
        ls = out.split('\n')
        ls[at - 1:at - 1] = ['import os as _os', root_line]
        out = '\n'.join(ls)
    return out, counts


def rewrite_sh(src):
    if OLD not in src:
        return src, 0
    n = src.count(OLD)
    out = src.replace(OLD, '"$ROOT"')
    lines = out.split('\n')
    at = 1 if lines and lines[0].startswith('#!') else 0
    lines[at:at] = ['ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"   # THE PORTABLE REPO (2026-09-15): the repo root from this script\'s own place']
    return '\n'.join(lines), n


def main(apply):
    total = {'py': 0, 'sh': 0, 'json': []}; files = 0; kinds = {'code': 0, 'doc': 0, 'comment': 0, 'fstring': 0, 'store_only': 0}
    for rel in tracked():
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            continue
        if rel.endswith('.py'):
            src = open(p, encoding='utf-8').read()
            if OLD not in src and STORE_OLD not in src:
                continue
            depth = rel.count('/')
            try:
                new, counts = rewrite_py(src, depth)
            except (tokenize.TokenError, SyntaxError) as e:
                print('  SKIPPED (cannot tokenize): %s — %s' % (rel, e)); continue
            if new != src:
                files += 1; total['py'] += sum(counts.values())
                for k, v in counts.items(): kinds[k] += v
                if apply:
                    try:
                        compile(new, rel, 'exec')                  # the rewritten file must compile before it is written
                    except SyntaxError as e:
                        print('  SKIPPED (the rewrite would not compile): %s — %s' % (rel, e)); files -= 1; continue
                    open(p, 'w', encoding='utf-8').write(new)
        elif rel.endswith('.sh'):
            src = open(p, encoding='utf-8').read()
            new, n = rewrite_sh(src)
            if n:
                files += 1; total['sh'] += n
                if apply:
                    open(p, 'w', encoding='utf-8').write(new)
        elif rel.endswith('.json'):
            if OLD in open(p, encoding='utf-8', errors='replace').read():
                total['json'].append(rel)
    print('THE PORTABLE PASS (%s): %d files rewritten — Python occurrences %d (code %d, docstrings %d, comments %d, f-strings %d, store-only %d), shell %d; JSON carriers left untouched: %s'
          % ('APPLIED' if apply else 'DRY', files, total['py'], kinds['code'], kinds['doc'], kinds['comment'], kinds['fstring'], kinds['store_only'], total['sh'], total['json'] or 'none'))
    return files


if __name__ == '__main__':
    if '--apply' in sys.argv:
        main(True)
    else:
        main(False)
