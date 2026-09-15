#!/usr/bin/env python3
"""build_world.py — THE ONE DATABASE (rewritten 2026-09-14 at D7'S MERGE; World/step9/THE_LOOP.md "D7'S MERGE — ONE DATABASE": D19-D21).

    python3 build_world.py            # build the reading's layers, reindex the whole journal, create the views, reconcile
    python3 build_world.py --check    # reconcile the existing index against a fresh fold, nothing rebuilt

THE DATABASE IS World/journal/data/world.sqlite — the journal's index over every segment: L0 the operators, L1 THE FOLD (the frozen
corpus as corpus_world.fold() holds it, one row per item — World/journal/build_world.py), L2 the cases, L3 the runs. The World
folder's old tables (World/schema.sql, the record) are VIEWS over the fold's rows (World/journal/fold_views.sql) with their old names —
one exception, the fold's events are `fold_events` — so ask.py runs over the one database. World/world.sqlite is retired; nothing
here writes a row by hand and nothing writes back to the corpus.

THE RECONCILIATION (the gate moved upstream, D21 a): the views must agree with a fresh fold on nine counts and the state hash;
disagreement is a finding. The journal gate (World/step9/world_journal.py --gate) checks the fold layer's header against
logic/corpus/CORPUS_TRUTH.py's pinned tripwires without refolding (D21 b).
"""
from __future__ import annotations
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place

import argparse
import importlib.util
import os
import sqlite3
import sys
from pathlib import Path

REPO = Path(_ROOT)
HERE = Path(__file__).resolve().parent
JOURNAL = HERE / "journal"
DB = JOURNAL / "data" / "world.sqlite"

sys.path.insert(0, str(REPO))
sys.path.insert(0, str(HERE / "step9"))
sys.path.insert(0, str(JOURNAL))
import corpus_world  # noqa: E402


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def reconcile_index(db_path, W=None):
    """the views against the fold: nine counts and the state hash (the old reconcile, now over the one database); True iff all agree"""
    if W is None:
        W = corpus_world.fold(write=False)
    con = sqlite3.connect(str(db_path))
    c = con.cursor()

    def n(t):
        return c.execute("SELECT count(*) FROM %s" % t).fetchone()[0]

    open_db = c.execute("SELECT count(*) FROM demands WHERE status='OPEN'").fetchone()[0]
    fold_open = sum(1 for d in W["demands"] if d["status"] == "OPEN")
    row = c.execute("SELECT value FROM meta WHERE key='state_hash'").fetchone()
    hash_db = row[0] if row else '(no fold layer)'
    checks = [
        ("units",        n("units"),        len(W["units"])),
        ("facts",        n("facts"),        len(W["facts"])),
        ("events",       n("fold_events"),  len(W["events"])),
        ("demands",      n("demands"),      len(W["demands"])),
        ("open demands", open_db,           fold_open),
        ("mentions",     n("mentions"),     len(W["mentions"])),
        ("names",        n("names"),        len(W["names"])),
        ("standing",     n("standing"),     len(W["standing"])),
        ("tests",        n("tests"),        len(W["tests"])),
    ]
    print("\nRECONCILIATION — the one database's views against corpus_world.fold()")
    print("  %-16s %10s %10s   %s" % ("", "database", "fold", ""))
    bad = 0
    for label, a, b in checks:
        ok = a == b
        bad += (not ok)
        print("  %-16s %10d %10d   %s" % (label, a, b, "ok" if ok else "*** MISMATCH"))
    hok = hash_db == corpus_world._state_hash(W)
    bad += (not hok)
    print("  %-16s %10s %10s   %s" % ("state hash", str(hash_db)[:12], corpus_world._state_hash(W)[:12], "ok" if hok else "*** MISMATCH"))
    print("\n  %s" % ("ALL GREEN — the one database agrees with the fold" if not bad else "%d MISMATCH(ES) — this is a finding" % bad))
    con.close()
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="reconcile the existing index against a fresh fold, nothing rebuilt")
    args = ap.parse_args()
    print("folding the corpus (read-only) ...")
    W = corpus_world.fold(write=False)
    if not args.check:
        BW = _load(JOURNAL / "build_world.py", "journal_build_world")
        BW.build(W=W)
        import world_journal as WJ
        db, rows, segs = WJ.reindex()
        print("the index rebuilt: %s — %d rows from %d segments; the fourteen fold views and the five run views created" % (db, rows, segs))
        old = HERE / "world.sqlite"
        if old.exists():
            old.unlink()
            print("World/world.sqlite retired (deleted) — the database is %s" % DB)
    elif not DB.exists():
        sys.exit("no index at %s — run without --check first" % DB)
    ok = reconcile_index(DB, W)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
