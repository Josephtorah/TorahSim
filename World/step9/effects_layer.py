#!/usr/bin/env python3
# THE EFFECTS LAYER (2026-09-03, under THE EFFECTS LAW — owner-ruled:
# "It should be coded every time for effects.")
#
# The registry discipline in code: a compiled function may emit an effect
# ONLY if the effect is registered in effect_vocabulary.yaml (discovered,
# never designed). This module loads the registry, validates every id at
# emission time, and renders the STATE CHANGES a verdict writes — to the
# LEDGER, never the event stream (method law 6, clarified 2026-09-03).
# Model layer; read-only over the registry.

import os
import yaml

_REG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'effect_vocabulary.yaml')
with open(_REG_PATH) as _f:
    REGISTRY = yaml.safe_load(_f)['effects']

# NONE is the honest non-effect: a classification cell, a pending state,
# or a matter routed outside the compiled span. It writes nothing.
NONE = '—'


def validate(effect_ids):
    """Every emitted effect must be registered — or the run refuses."""
    for eid in effect_ids:
        if eid == NONE:
            continue
        if eid not in REGISTRY:
            raise SystemExit(
                'EFFECTS LAW: %r is not in effect_vocabulary.yaml — '
                'an unregistered effect may not be emitted. Register it '
                'with its ink/corpus/exam witnesses first.' % eid)
    return effect_ids


def render(effect_ids, note=''):
    """One printable line per effect: id [ledger_op] — English."""
    lines = []
    for eid in validate(effect_ids):
        if eid == NONE:
            lines.append('  %s %s' % (NONE, note or
                         '(no state change: classification, pending, '
                         'or routed outside the span)'))
            continue
        e = REGISTRY[eid]
        lines.append('  %-18s [%s]  %s' % (eid, e['ledger_op'], e['en']))
    return lines


def summarize(used):
    """Tally the ledger operations a run actually wrote."""
    ops = {}
    for eid in used:
        if eid == NONE:
            continue
        op = REGISTRY[eid]['ledger_op']
        ops[op] = ops.get(op, 0) + 1
    return ops
