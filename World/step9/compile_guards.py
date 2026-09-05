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


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print('%s: %d tests, every expectation a literal' % (p, check_honest_pairing(p)))
