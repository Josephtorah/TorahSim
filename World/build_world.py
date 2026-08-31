#!/usr/bin/env python3
"""build_world.py — compile the whole derived corpus into a queryable world.

    python3 build_world.py            # build world.sqlite and reconcile
    python3 build_world.py --check    # reconcile an existing build only

READ-ONLY over the repo. Never writes to Torah_Grok. Drop world.sqlite and
rebuild at will — this is the model layer, not the evidence layer.

It does NOT re-extract the YAML. It consumes corpus_world.fold(), which is
the tested extraction that produces the era's proof, and projects it into a
schema you can ask questions of. That is deliberate: reconciliation against
the fold is then exact by construction rather than by luck.
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

REPO = Path("<repo-old>")
HERE = Path(__file__).resolve().parent
DB = HERE / "world.sqlite"
SCHEMA = HERE / "schema.sql"

sys.path.insert(0, str(REPO))
import corpus_world  # noqa: E402

BOOK_ORDER = corpus_world.BOOK_ORDER


# --------------------------------------------------------------- ref parsing
def parse_ref(ref):
    """'Gen.1.2' or 'Gen.1.2-3' -> (book, chapter, verse)."""
    book, ch, vs = ref.split(".")
    return book, int(ch), int(str(vs).split("-")[0])


def ref_key(ref):
    b, c, v = parse_ref(ref)
    return (BOOK_ORDER[b], c, v)



def tok2ent_pre(W, unit, token):
    """Resolve a unit-local token to its corpus entity id (same rule the fold
    uses); falls back to the token itself, which is the fold's own default."""
    if not hasattr(tok2ent_pre, "_m"):
        m = {}
        for x in W["mentions"]:
            m.setdefault((x["unit"], x["token"]), x["entity"])
        tok2ent_pre._m = m
    return tok2ent_pre._m.get((unit, token), token)


# --------------------------------------------------------------------- build
def build():
    print("folding the corpus (read-only) ...")
    W = corpus_world.fold(write=False)
    state_hash = corpus_world._state_hash(W)

    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA.read_text(encoding="utf-8"))
    c = con.cursor()

    # ---- the spine ---------------------------------------------------------
    # every ref that any row touches, in one global order
    seen = {}
    for key in ("facts", "events", "demands", "mentions", "names",
                "standing", "tests", "ledger"):
        for r in W[key]:
            seen.setdefault(r["ref"], []).append(r["seq"])
    unit_of = {}
    for r in W["facts"] + W["events"] + W["mentions"] + W["standing"]:
        unit_of.setdefault(r["ref"], r["unit"])

    ordered = sorted(seen, key=ref_key)
    ord_of = {}
    rows = []
    for i, ref in enumerate(ordered, start=1):
        ord_of[ref] = i
        b, ch, vs = parse_ref(ref)
        seqs = seen[ref]
        rows.append((i, ref, b, ch, vs, unit_of.get(ref), min(seqs), max(seqs)))
    c.executemany("INSERT INTO refs VALUES (?,?,?,?,?,?,?,?)", rows)

    # ---- units -------------------------------------------------------------
    c.executemany("INSERT INTO units VALUES (?,?,?,?,?,?)",
                  [(u["seq_unit"], u["unit"], u["first_ref"], u["steps"],
                    u["facts"], u["opened"]) for u in W["units"]])

    # ---- core tables -------------------------------------------------------
    c.executemany("INSERT INTO facts VALUES (?,?,?,?)",
                  [(f["seq"], f["unit"], f["ref"], f["fact"]) for f in W["facts"]])

    ev, th = [], []
    for e in W["events"]:
        ev.append((e["seq"], e["unit"], e["ref"], e["verb"], e["agent"]))
        for i, t in enumerate(e.get("themes") or []):
            th.append((e["seq"], i, t))
    c.executemany("INSERT INTO events VALUES (?,?,?,?,?)", ev)
    c.executemany("INSERT INTO event_themes VALUES (?,?,?)", th)

    c.executemany("INSERT INTO demands VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  [(d["seq"], d["unit"], d["ref"], d["speaker"], d["mood"],
                    d["demand"], d["status"], d["settled_seq"], d["settled_unit"],
                    d["settled_ref"], d["settle_kind"], d["basis_en"],
                    d["uncertain"]) for d in W["demands"]])

    c.executemany("INSERT INTO mentions VALUES (?,?,?,?,?,?)",
                  [(m["seq"], m["unit"], m["ref"], m["token"], m["role"],
                    m["entity"]) for m in W["mentions"]])

    c.executemany("INSERT INTO names VALUES (?,?,?,?,?)",
                  [(n["seq"], n["unit"], n["ref"], n["token"], n["label"])
                   for n in W["names"]])

    c.executemany("INSERT INTO standing VALUES (?,?,?,?,?)",
                  [(s["seq"], s["unit"], s["ref"], s["kind"], s["payload"])
                   for s in W["standing"]])

    c.executemany("INSERT INTO tests VALUES (?,?,?,?,?,?)",
                  [(t["seq"], t["unit"], t["ref"], t["verdict"], t["oracle"],
                    t["theme"]) for t in W["tests"]])

    c.executemany("INSERT INTO checkpoints VALUES (?,?,?,?,?,?)",
                  [(k["seq_unit"], k["unit"], k["seq"], k["facts_n"],
                    k["open_n"], k["state_hash"]) for k in W["checkpoints"]])

    # ---- entities ----------------------------------------------------------
    ent = {}
    for m in W["mentions"]:
        e = ent.setdefault(m["entity"], {"first_seq": m["seq"], "first_ref": m["ref"],
                                         "first_unit": m["unit"], "n": 0,
                                         "agent": 0, "theme": 0})
        e["n"] += 1
        if m["seq"] < e["first_seq"]:
            e.update(first_seq=m["seq"], first_ref=m["ref"], first_unit=m["unit"])
        if m["role"] == "agent":
            e["agent"] += 1
    theme_n = {}
    for e in W["events"]:
        for t_ in (e.get("themes") or []):
            theme_n[tok2ent_pre(W, e["unit"], t_)] = \
                theme_n.get(tok2ent_pre(W, e["unit"], t_), 0) + 1
    for k in theme_n:
        ent.setdefault(k, {"first_seq": 10**9, "first_ref": None,
                           "first_unit": None, "n": 0, "agent": 0})
    c.executemany("INSERT INTO entities VALUES (?,?,?,?,?,?,?)",
                  [(k, v["first_ref"], v["first_seq"], v["first_unit"],
                    v["n"], v["agent"], theme_n.get(k, 0)) for k, v in ent.items()])

    # ---- relations (a projection; every row cites its seq) -----------------
    tok2ent = {}
    for m in W["mentions"]:
        tok2ent.setdefault((m["unit"], m["token"]), m["entity"])

    def ent_of(unit, token):
        return tok2ent.get((unit, token), token)

    rel = []
    for e in W["events"]:
        o = ord_of.get(e["ref"])
        for t in (e.get("themes") or []):
            rel.append((e["seq"], o, e["ref"], e["unit"],
                        ent_of(e["unit"], e["agent"]), e["verb"],
                        ent_of(e["unit"], t), "event"))
    for n in W["names"]:
        rel.append((n["seq"], ord_of.get(n["ref"]), n["ref"], n["unit"],
                    ent_of(n["unit"], n["token"]), "named", n["label"], "name"))
    for d in W["demands"]:
        rel.append((d["seq"], ord_of.get(d["ref"]), d["ref"], d["unit"],
                    ent_of(d["unit"], d["speaker"]) if d["speaker"] else None,
                    "demands", d["demand"], "demand"))
    c.executemany("INSERT INTO relations VALUES (?,?,?,?,?,?,?,?)", rel)

    # ---- entity_state: names with validity ranges --------------------------
    by_ent = {}
    for n in W["names"]:
        e = ent_of(n["unit"], n["token"])
        by_ent.setdefault(e, []).append(
            (ord_of.get(n["ref"], 0), n["ref"], n["label"], n["seq"]))
    st = []
    for e, lst in by_ent.items():
        lst.sort()
        for i, (o, ref, label, seq) in enumerate(lst):
            nxt = lst[i + 1] if i + 1 < len(lst) else None
            st.append((e, "name", label, o, ref,
                       nxt[0] if nxt else None, nxt[1] if nxt else None, seq))
    c.executemany("INSERT INTO entity_state VALUES (?,?,?,?,?,?,?,?)", st)

    # ---- meta --------------------------------------------------------------
    open_n = sum(1 for d in W["demands"] if d["status"] == "OPEN")
    meta = {
        "built_from": "corpus_world.fold(write=False)",
        "repo": str(REPO),
        "state_hash": state_hash,
        "units": len(W["units"]), "refs": len(ordered),
        "facts": len(W["facts"]), "events": len(W["events"]),
        "demands": len(W["demands"]), "open_demands": open_n,
        "mentions": len(W["mentions"]), "names": len(W["names"]),
        "standing": len(W["standing"]), "tests": len(W["tests"]),
        "entities": len(ent), "relations": len(rel), "entity_state": len(st),
    }
    c.executemany("INSERT INTO meta VALUES (?,?)",
                  [(k, str(v)) for k, v in meta.items()])
    con.commit()
    return con, W, meta


# --------------------------------------------------------------- reconcile
def reconcile(con, W=None):
    """The database must agree with the fold. Disagreement is a finding."""
    if W is None:
        W = corpus_world.fold(write=False)
    c = con.cursor()

    def n(t):
        return c.execute("SELECT count(*) FROM %s" % t).fetchone()[0]

    open_db = c.execute(
        "SELECT count(*) FROM demands WHERE status='OPEN'").fetchone()[0]
    fold_open = sum(1 for d in W["demands"] if d["status"] == "OPEN")
    hash_db = c.execute(
        "SELECT value FROM meta WHERE key='state_hash'").fetchone()[0]

    checks = [
        ("units",        n("units"),    len(W["units"])),
        ("facts",        n("facts"),    len(W["facts"])),
        ("events",       n("events"),   len(W["events"])),
        ("demands",      n("demands"),  len(W["demands"])),
        ("open demands", open_db,       fold_open),
        ("mentions",     n("mentions"), len(W["mentions"])),
        ("names",        n("names"),    len(W["names"])),
        ("standing",     n("standing"), len(W["standing"])),
        ("tests",        n("tests"),    len(W["tests"])),
    ]
    print("\nRECONCILIATION — world.sqlite against corpus_world.fold()")
    print("  %-16s %10s %10s   %s" % ("", "database", "fold", ""))
    bad = 0
    for label, a, b in checks:
        ok = a == b
        bad += (not ok)
        print("  %-16s %10d %10d   %s" % (label, a, b, "ok" if ok else "*** MISMATCH"))
    hok = hash_db == corpus_world._state_hash(W)
    bad += (not hok)
    print("  %-16s %10s %10s   %s" % ("state hash", hash_db[:12],
                                      corpus_world._state_hash(W)[:12],
                                      "ok" if hok else "*** MISMATCH"))
    print("\n  %s" % ("ALL GREEN — the world agrees with the fold"
                      if not bad else "%d MISMATCH(ES) — this is a finding" % bad))
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="reconcile an existing world.sqlite, do not rebuild")
    a = ap.parse_args()
    if a.check:
        if not DB.exists():
            sys.exit("no world.sqlite — run without --check first")
        ok = reconcile(sqlite3.connect(DB))
        sys.exit(0 if ok else 1)

    con, W, meta = build()
    print("\nBUILT %s" % DB)
    for k in ("units", "refs", "entities", "facts", "events", "relations",
              "demands", "open_demands", "standing", "entity_state"):
        print("   %-14s %s" % (k, meta[k]))
    ok = reconcile(con, W)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
