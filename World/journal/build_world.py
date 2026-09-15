#!/usr/bin/env python3
"""build_world.py — THE READING'S LAYERS OF THE WORLD JOURNAL (rewritten 2026-09-14 at D7'S MERGE; World/step9/THE_LOOP.md "D7'S MERGE —
ONE DATABASE: the design", decision D19 THE FOLD IS THE STRUCTURE LAYER; the probes World/step9/merge_probes.py written first).

  L0 scripture — one event per operator of the frozen units in canonical order (scripture.op; as since 2026-08-24).
  L1 the fold  — one row per item of corpus_world.fold()'s ten lists (units, facts, events, demands, mentions, names, standing, tests,
                 checkpoints, ledger — the kinds fold.unit … fold.ledger), one fold.ref per distinct verse of the spine (the ordinal
                 computed here, deterministically, in canonical order), and one fold.meta carrying the counts and the state hash; each
                 row's data the item exactly as the fold holds it, its prov {unit, ref}, its op the operator's ordinal. The segment's
                 header carries the counts and the hash too. The World folder's old tables are VIEWS over these rows
                 (World/journal/fold_views.sql; D20); World/build_world.py reconciles them against a fresh fold (D21).

The August tree model (L1_structure.jsonl, world_tree.json, its checklist) is RETIRED as D10 ruled: the build removes its files from the
data folder. No index step here — the index is world_journal's, rebuilt over every segment; run `python3 World/build_world.py` for the
whole merge (build, reindex, views, reconcile). Read-only over the corpus; deterministic (no timestamps; canonical JSON; --selftest folds
again in a second process and byte-compares both segments).

Run: python3 World/journal/build_world.py [--selftest]      (WORLD_OUT_DIR overrides the data folder)
"""
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]                     # the repo root (TorahSim)
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import yaml                                # noqa: E402
import corpus_world as cw                  # noqa: E402
from worldledger import Segment, canon     # noqa: E402

DATA = Path(os.environ.get("WORLD_OUT_DIR", str(HERE / "data")))
FOLD_LISTS = ('units', 'facts', 'events', 'demands', 'mentions', 'names', 'standing', 'tests', 'checkpoints', 'ledger')
KIND = {'units': 'fold.unit', 'facts': 'fold.fact', 'events': 'fold.event', 'demands': 'fold.demand', 'mentions': 'fold.mention',
        'names': 'fold.name', 'standing': 'fold.standing', 'tests': 'fold.test', 'checkpoints': 'fold.checkpoint', 'ledger': 'fold.ledger'}
AUGUST = ('L1_structure.jsonl', 'world_tree.json')      # the retired tree's files (D10)
L0_NAME, L1_NAME = 'L0_scripture.jsonl', 'L1_fold.jsonl'


def known_kinds():
    reg = yaml.safe_load((HERE / 'registers' / 'event_kinds.yaml').read_text(encoding='utf-8'))
    return {k['id'] for k in reg['kinds']}


def parse_ref(ref):
    """'Gen.1.2' or 'Gen.1.2-3' -> (book, chapter, verse)"""
    book, ch, vs = ref.split('.')
    return book, int(ch), int(str(vs).split('-')[0])


def ref_key(ref):
    b, c, v = parse_ref(ref)
    bo = cw.BOOK_ORDER
    order = bo.index(b) if isinstance(bo, (list, tuple)) else bo.get(b, 99)
    return (order, c, v, ref)


def build(out_dir=None, W=None):
    """write L0 and L1 into out_dir (the data folder by default); returns ({'L0': path, 'L1': path}, the counts, the state hash)"""
    out = Path(out_dir) if out_dir else DATA
    out.mkdir(parents=True, exist_ok=True)
    kinds = known_kinds()
    for k in list(KIND.values()) + ['fold.ref', 'fold.meta', 'scripture.op']:
        if k not in kinds:
            raise SystemExit('unregistered event kind: %s (register it in registers/event_kinds.yaml first)' % k)
    if W is None:
        print('folding the corpus (read-only) ...')
        W = cw.fold(write=False)
    h = cw._state_hash(W)

    # ---- L0: the operators ----
    L0 = Segment('L0', 'build_world/0')
    seq = 0
    for uid, unit in cw.frozen_units_in_canonical_order():
        for st in unit['boot_steps']:
            ref = st['ref']
            for op in st.get('operators', []):
                seq += 1
                L0.append('scripture.op', uid, {'k': str(op.get('op', '')), 'x': str(op.get('expr_en', ''))[:160]}, {'unit': uid, 'ref': ref}, op=seq)

    # ---- L1: the fold ----
    seen, unit_of = {}, {}
    for k in ('facts', 'events', 'demands', 'mentions', 'names', 'standing', 'tests', 'ledger'):
        for r in W[k]:
            seen.setdefault(r['ref'], []).append(r['seq'])
    for r in W['facts'] + W['events'] + W['mentions'] + W['standing']:
        unit_of.setdefault(r['ref'], r['unit'])
    ordered = sorted(seen, key=ref_key)
    counts = {k: len(W[k]) for k in FOLD_LISTS}
    open_n = sum(1 for d in W['demands'] if d['status'] == 'OPEN')
    header = dict(counts, state_hash=h, refs=len(ordered), open_demands=open_n, built_from='corpus_world.fold(write=False)')
    L1 = Segment('L1', 'build_fold/0', header=header)
    for i, ref in enumerate(ordered, 1):
        b, c, v = parse_ref(ref)
        seqs = seen[ref]
        L1.append('fold.ref', ref, {'ord': i, 'ref': ref, 'book': b, 'chapter': c, 'verse': v, 'unit': unit_of.get(ref), 'first_seq': min(seqs), 'last_seq': max(seqs)},
                  {'unit': unit_of.get(ref), 'ref': ref}, op=min(seqs))
    tok2ent = {}
    for m in W['mentions']:
        tok2ent.setdefault((m['unit'], m['token']), m['entity'])

    def ent(unit, token):
        return tok2ent.get((unit, token), token) if token else 'world'

    def subj_of(k, it):
        if k == 'mentions':
            return it['entity']
        if k == 'events':
            return ent(it['unit'], it.get('agent'))
        if k == 'demands':
            return ent(it['unit'], it.get('speaker'))
        if k == 'names':
            return ent(it['unit'], it.get('token'))
        if k == 'ledger':
            return 'clock'
        return it['unit']

    for k in FOLD_LISTS:
        for it in W[k]:
            L1.append(KIND[k], subj_of(k, it), it, {'unit': it.get('unit'), 'ref': it.get('ref') or it.get('first_ref')}, op=it.get('seq', it.get('seq_unit', 0)))
    L1.append('fold.meta', 'world', header, {'unit': None, 'ref': None}, op=0)

    p0, p1 = out / L0_NAME, out / L1_NAME
    L0.write(str(p0))
    L1.write(str(p1))
    for name in AUGUST:
        f = out / name
        if f.exists():
            f.unlink()
    print('=== THE READING\'S LAYERS BUILT === L0 %d operators · L1 %d rows (the fold: %s; refs %d; meta 1) · hash %s · %s' % (
        len(L0.events), len(L1.events), ', '.join('%s %d' % (k, counts[k]) for k in FOLD_LISTS), len(ordered), h, out))
    return {'L0': str(p0), 'L1': str(p1)}, counts, h


def selftest_determinism():
    """byte-grade determinism: fold in a SEPARATE PROCESS into a temp dir, byte-compare both segments"""
    import filecmp
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        r = subprocess.run([sys.executable, __file__], env=dict(os.environ, WORLD_OUT_DIR=td), capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-800:], r.stderr[-800:])
            raise SystemExit('determinism selftest: the second fold failed')
        for seg in (L0_NAME, L1_NAME):
            if not filecmp.cmp(str(DATA / seg), str(Path(td) / seg), shallow=False):
                raise SystemExit('DETERMINISM FAIL: %s differs across processes' % seg)
    print('DETERMINISM: byte-identical across two processes — GREEN')


if __name__ == '__main__':
    build()
    if '--selftest' in sys.argv:
        selftest_determinism()
