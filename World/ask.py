#!/usr/bin/env python3
"""ask.py — ask the world questions.

    python3 ask.py names                     every entity that was renamed
    python3 ask.py called jacob              what an entity was called, when
    python3 ask.py at Gen.30.24              the world as of a verse
    python3 ask.py open Gen.30.24            obligations outstanding then
    python3 ask.py career joseph             one entity's whole career
    python3 ask.py who Gen.32.4-33.17        entities present in a span
    python3 ask.py entities                  the cast, by weight
    python3 ask.py sql "SELECT ..."          raw SQL

Read-only. Rebuild with build_world.py (the merge of 2026-09-14: the one database World/journal/data/world.sqlite, the old tables its views).
"""
from __future__ import annotations
import sqlite3, sys
from pathlib import Path

DB = Path(__file__).resolve().parent / "journal" / "data" / "world.sqlite"    # D7'S MERGE (2026-09-14): the one database — the journal's index; the old tables are views over it


def con():
    if not DB.exists():
        sys.exit("no world.sqlite — run: python3 build_world.py")
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def show(rows, cols=None):
    rows = list(rows)
    if not rows:
        print("   (nothing)")
        return
    cols = cols or rows[0].keys()
    w = {k: max(len(str(k)), max(len(str(r[k])) for r in rows)) for k in cols}
    w = {k: min(v, 52) for k, v in w.items()}
    print("  " + "  ".join(str(k).ljust(w[k])[:w[k]] for k in cols))
    print("  " + "  ".join("-" * w[k] for k in cols))
    for r in rows:
        print("  " + "  ".join(str(r[k]).ljust(w[k])[:w[k]] for k in cols))
    print("  (%d rows)" % len(rows))


def ord_of(c, ref):
    r = c.execute("SELECT ord FROM refs WHERE ref=?", (ref,)).fetchone()
    if r:
        return r["ord"]
    r = c.execute("SELECT ord,ref FROM refs WHERE ref LIKE ? ORDER BY ord",
                  (ref.split("-")[0] + "%",)).fetchone()
    if not r:
        sys.exit("no such ref in the world: %s" % ref)
    print("   (nearest ref: %s)" % r["ref"])
    return r["ord"]


def cmd_names(c, _):
    print("\nENTITIES THAT CHANGED NAME\n")
    show(c.execute("""
      SELECT entity, value AS called, from_ref, COALESCE(to_ref,'(still)') AS until
      FROM entity_state WHERE key='name' AND entity IN
        (SELECT entity FROM entity_state WHERE key='name'
         GROUP BY entity HAVING count(DISTINCT value)>1)
      ORDER BY entity, from_ord"""))


def cmd_called(c, a):
    e = a[0]
    print("\nWHAT %s WAS CALLED, AND WHEN\n" % e.upper())
    show(c.execute("""
      SELECT value AS called, from_ref, COALESCE(to_ref,'(still)') AS until, seq
      FROM entity_state WHERE key='name' AND entity=? ORDER BY from_ord""", (e,)))


def cmd_at(c, a):
    o = ord_of(c, a[0])
    print("\nTHE WORLD AS OF %s\n" % a[0])
    for label, sql in (
        ("entities known", "SELECT count(DISTINCT entity) n FROM mentions m "
                           "JOIN refs r ON r.ref=m.ref WHERE r.ord<=?"),
        ("facts standing", "SELECT count(*) n FROM facts f JOIN refs r ON r.ref=f.ref WHERE r.ord<=?"),
        ("events so far", "SELECT count(*) n FROM fold_events e JOIN refs r ON r.ref=e.ref WHERE r.ord<=?"),   # the fold's events are the view fold_events (the journal's own table is `events`)
        ("demands raised", "SELECT count(*) n FROM demands d JOIN refs r ON r.ref=d.ref WHERE r.ord<=?"),
        ("standing law", "SELECT count(*) n FROM standing s JOIN refs r ON r.ref=s.ref WHERE r.ord<=?"),
    ):
        print("   %-16s %d" % (label, c.execute(sql, (o,)).fetchone()["n"]))
    print("\n   still outstanding:")
    show(c.execute("""
      SELECT d.ref, d.speaker, d.mood, substr(d.demand,1,44) AS demand
      FROM demands d JOIN refs r ON r.ref=d.ref
      WHERE r.ord<=? AND (d.status='OPEN' OR
            COALESCE((SELECT ord FROM refs WHERE ref=d.settled_ref),1e9) > ?)
      ORDER BY r.ord DESC LIMIT 12""", (o, o)))


def cmd_open(c, a):
    o = ord_of(c, a[0])
    print("\nOBLIGATIONS OUTSTANDING AS OF %s\n" % a[0])
    show(c.execute("""
      SELECT d.ref, d.speaker, d.mood, substr(d.demand,1,50) AS demand, d.status
      FROM demands d JOIN refs r ON r.ref=d.ref
      WHERE r.ord<=? AND (d.status='OPEN' OR
            COALESCE((SELECT ord FROM refs WHERE ref=d.settled_ref),1e9) > ?)
      ORDER BY r.ord""", (o, o)))


def cmd_career(c, a):
    e = a[0]
    print("\nCAREER OF %s\n" % e.upper())
    show(c.execute("""
      SELECT ref, relation, substr(object,1,46) AS object, source, unit
      FROM relations WHERE subject=? ORDER BY ord""", (e,)))


def cmd_who(c, a):
    span = a[0]
    lo = ord_of(c, span.split("-")[0])
    hi = ord_of(c, span.split("-")[1]) if "-" in span else lo
    print("\nWHO IS PRESENT IN %s\n" % span)
    show(c.execute("""
      SELECT m.entity, count(*) AS mentions, min(m.ref) AS first_here
      FROM mentions m JOIN refs r ON r.ref=m.ref
      WHERE r.ord BETWEEN ? AND ?
      GROUP BY m.entity ORDER BY mentions DESC""", (lo, hi)))


def cmd_entities(c, _):
    print("\nTHE CAST, BY WEIGHT\n")
    show(c.execute("""
      SELECT entity, mentions, as_agent, as_theme, first_ref
      FROM entities ORDER BY mentions DESC LIMIT 30"""))


def cmd_sql(c, a):
    print()
    show(c.execute(a[0]))


CMDS = {"names": cmd_names, "called": cmd_called, "at": cmd_at, "open": cmd_open,
        "career": cmd_career, "who": cmd_who, "entities": cmd_entities, "sql": cmd_sql}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print(__doc__)
        sys.exit(0)
    CMDS[sys.argv[1]](con(), sys.argv[2:])
