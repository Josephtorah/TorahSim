#!/usr/bin/env python3
"""holdings.py — search EVERYTHING the machine holds, in all three strata.

F-006 (owner: "build F-006"), from the pilot's one blind spot: the exam's
first holdings-search read claims manifests and witness rows but not
OPERATOR PROSE — and so reported a dispute "missing" that gen_06's BLESS
operator had carried since 2026-08-23. This module is the fix: one search,
three strata, so no future exam calls a verdict unheld before looking
everywhere the corpus actually writes.

    from holdings import search
    search(["miscarriage"])   -> {"claims": [...], "witness": [...],
                                  "operator_prose": [...]}

Terms are matched case-insensitively; ALL terms must appear. Each hit
carries enough to open the source (unit, id/ref/seq, snippet).
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import glob
import json
import re
import sqlite3
from pathlib import Path

REPO = Path(_ROOT)
WORLD_DB = Path(__file__).resolve().parent.parent / "world.sqlite"

_cache = {}


def _load():
    if _cache:
        return _cache
    claims = []
    for f in glob.glob(str(REPO / "logic/oral_audit/manifests/*_claims.json")):
        uid = Path(f).name.replace("_claims.json", "")
        for c in json.load(open(f)):
            claims.append((uid, c["id"], str(c.get("claim_en", ""))))
    witness = []
    if WORLD_DB.exists():
        con = sqlite3.connect(WORLD_DB)
        witness = [(u, ref, "seq %d [%s]" % (s, k), p or "")
                   for s, u, ref, k, p in con.execute(
                       "SELECT seq, unit, ref, kind, payload FROM standing")]
        con.close()
    prose = []
    # the third stratum: every operator's en: text in every frozen unit —
    # parsed with YAML and walked recursively (any mapping carrying both
    # 'op' and 'en'), the same walk the audit's cross-wire detector used.
    import yaml

    def walk(node):
        if isinstance(node, dict):
            if "op" in node and "en" in node:
                yield node
            for v in node.values():
                yield from walk(v)
        elif isinstance(node, list):
            for v in node:
                yield from walk(v)

    for f in glob.glob(str(REPO / "logic/units/*.yaml")):
        try:
            d = yaml.safe_load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if not (isinstance(d, dict)
                and d.get("meta", {}).get("status") == "frozen"):
            continue
        uid = Path(f).stem
        for op in walk(d):
            body = re.sub(r"\s+", " ", str(op.get("en", ""))).strip()
            if body:
                prose.append((uid, str(op.get("op", "?")), body))
    _cache.update(claims=claims, witness=witness, prose=prose)
    return _cache


def search(terms):
    terms = [t.lower() for t in terms]
    db = _load()

    def hit(text):
        t = text.lower()
        return all(x in t for x in terms)

    return {
        "claims": [(u, cid, en[:120]) for u, cid, en in db["claims"]
                   if hit(en)],
        "witness": [(u, ref, tag, p[:120]) for u, ref, tag, p
                    in db["witness"] if hit(p)],
        "operator_prose": [(u, op, body[:120]) for u, op, body
                           in db["prose"] if hit(body)],
    }


def held_anywhere(terms):
    r = search(terms)
    return any(r.values()), r


if __name__ == "__main__":
    import sys
    res = search(sys.argv[1:])
    for stratum, hits in res.items():
        print("%s: %d" % (stratum, len(hits)))
        for h in hits[:5]:
            print("   ", h)
