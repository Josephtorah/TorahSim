#!/usr/bin/env python3
# THE HONEST-PAIRING GUARD (2026-09-05, REVIEW_BEHAR item 6 — built into
# the shared test helper on the next compile, as the review ordered).
#
# The trap it closes: two consecutive compiles' first drafts graded a
# cell against a value COMPUTED FROM THE CELL ITSELF (round 45's date
# cell; round 46's priest count). Such a test passes forever and proves
# nothing. Caught twice in self-review; from this file forward it is
# caught by the machine.
#
# The rule: every EXPECTED value in a runner's TESTS table must be a
# LITERAL — a constant the author typed from the answer sheet (or a list
# of constants for a recorded dispute). An expected value that is a
# name, an attribute, a subscript, or a call is REFUSED: it could only
# have been derived from engine state. The check runs on the runner's
# own source text by the parser, before anything is graded.
#
# Model layer; read-only over the runner's source.
import ast
import sys


def _is_literal(node):
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return all(_is_literal(e) for e in node.elts)
    if isinstance(node, ast.Dict):
        return all(_is_literal(k) and _is_literal(v)
                   for k, v in zip(node.keys, node.values))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return _is_literal(node.operand)
    return False


def check_honest_pairing(source_path, table_name='TESTS', expected_index=2):
    """Refuse any test whose expected value is not a literal.

    Returns the number of tests checked. Exits the run on the first
    non-literal expectation, naming the line."""
    tree = ast.parse(open(source_path, encoding='utf-8').read(), source_path)
    table = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == table_name:
                    table = node.value
    if table is None or not isinstance(table, (ast.List, ast.Tuple)):
        raise SystemExit('HONEST-PAIRING GUARD: no literal table %r found in %s'
                         % (table_name, source_path))
    n = 0
    for row in table.elts:
        if not isinstance(row, ast.Tuple) or len(row.elts) <= expected_index:
            raise SystemExit('HONEST-PAIRING GUARD: malformed test row at line %d'
                             % row.lineno)
        exp = row.elts[expected_index]
        if not _is_literal(exp):
            raise SystemExit(
                'HONEST-PAIRING GUARD: the expected value at %s:%d is not a '
                'literal (%s) — an expectation derived from engine state grades '
                'a cell against itself. Type the answer sheet\'s value.'
                % (source_path, exp.lineno, ast.dump(exp)[:60]))
        n += 1
    return n


def check_honest_dict(source_path, table_name='ORACLE'):
    """The dict form of the table (sitting C retrofit, 2026-09-05): every
    VALUE of the literal dict named table_name must be a literal — the
    guardians runner's ORACLE {(role, event): verdict}."""
    tree = ast.parse(open(source_path, encoding='utf-8').read(), source_path)
    table = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == table_name:
                    table = node.value
    if table is None or not isinstance(table, ast.Dict):
        raise SystemExit('HONEST-PAIRING GUARD: no literal dict %r found in %s'
                         % (table_name, source_path))
    for k, v in zip(table.keys, table.values):
        if not _is_literal(v):
            raise SystemExit('HONEST-PAIRING GUARD: the expected value at %s:%d is not a '
                             'literal (%s)' % (source_path, v.lineno, ast.dump(v)[:60]))
    return len(table.values)


def check_honest_calls(source_path, func_name, expected_index, cells_arg=None):
    """The call-site form (sitting C retrofit): every call to func_name in the
    runner's source is checked. With cells_arg=None the positional argument
    at expected_index must itself be a literal (yoma's cell(name, got, want,
    ...)). With cells_arg=k the k-th positional argument must be a literal
    list of tuples whose expected_index element is a literal — or a Name
    bound to such a list (mishpatim's grade(fn, oracle, cells)). Returns the
    number of expectations checked; refuses on the first non-literal."""
    src = open(source_path, encoding='utf-8').read()
    tree = ast.parse(src, source_path)
    # O3 THE GATE ITEMS (2026-09-07; REPORT_GATE_ITEMS.md): every assignment to a name, in source order — a call's list is
    # THE BINDING IN EFFECT AT THE CALL'S LINE (the nearest assignment before it), never the file's last (the last-binding
    # weakness: `cells = [...]; grade(..., cells); cells = [...]; grade(..., cells)` checked the last list twice)
    bindings = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            bindings.setdefault(node.targets[0].id, []).append((node.lineno, node.value))
    def binding_at(name, lineno):
        prior = [(ln, v) for ln, v in bindings.get(name, []) if ln < lineno]
        return max(prior, key=lambda t: t[0])[1] if prior else None
    n = 0
    calls = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else None)
        if name != func_name:
            continue
        calls += 1
        if cells_arg is None:
            if len(node.args) <= expected_index:
                raise SystemExit('HONEST-PAIRING GUARD: %s() at %s:%d has no positional argument %d'
                                 % (func_name, source_path, node.lineno, expected_index))
            exp = node.args[expected_index]
            if not _is_literal(exp):
                raise SystemExit('HONEST-PAIRING GUARD: the expected value at %s:%d is not a '
                                 'literal (%s) — an expectation derived from engine state grades a '
                                 'cell against itself. Type the answer sheet\'s value.'
                                 % (source_path, exp.lineno, ast.dump(exp)[:60]))
            n += 1
            continue
        if len(node.args) <= cells_arg:
            raise SystemExit('HONEST-PAIRING GUARD: %s() at %s:%d has no cells argument %d'
                             % (func_name, source_path, node.lineno, cells_arg))
        cells = node.args[cells_arg]
        if isinstance(cells, ast.Name):
            cells = binding_at(cells.id, node.lineno)
        if not isinstance(cells, (ast.List, ast.Tuple)):
            raise SystemExit('HONEST-PAIRING GUARD: %s() at %s:%d — the cells are not a literal list'
                             % (func_name, source_path, node.lineno))
        for row in cells.elts:
            if not isinstance(row, ast.Tuple) or len(row.elts) <= expected_index:
                raise SystemExit('HONEST-PAIRING GUARD: malformed cell at %s:%d' % (source_path, row.lineno))
            exp = row.elts[expected_index]
            if not _is_literal(exp):
                raise SystemExit('HONEST-PAIRING GUARD: the expected value at %s:%d is not a '
                                 'literal (%s)' % (source_path, exp.lineno, ast.dump(exp)[:60]))
            n += 1
    if calls == 0:
        raise SystemExit('HONEST-PAIRING GUARD: no call to %s() found in %s — nothing checked'
                         % (func_name, source_path))
    return n


if __name__ == '__main__':
    # CLI: compile_guards.py <runner> [--table NAME [--index N]] [--dict NAME]
    #      [--calls FUNC --index N [--cells-arg K]]  — default: TESTS at index 2
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__ or 'usage: compile_guards.py <runner.py> [options]')
    p = args[0]
    opts = args[1:]
    def opt(name, default=None):
        return opts[opts.index(name) + 1] if name in opts else default
    if '--dict' in opts:
        print('%s: %d expectations in dict %s, every value a literal' % (p, check_honest_dict(p, opt('--dict')), opt('--dict')))
    elif '--calls' in opts:
        ca = opt('--cells-arg')
        print('%s: %d expectations at %s() calls, every one a literal' % (
            p, check_honest_calls(p, opt('--calls'), int(opt('--index', 2)), int(ca) if ca is not None else None), opt('--calls')))
    else:
        print('%s: %d tests in %s, every expectation a literal' % (
            p, check_honest_pairing(p, opt('--table', 'TESTS'), int(opt('--index', 2))), opt('--table', 'TESTS')))
