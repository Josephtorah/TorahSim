#!/usr/bin/env python3
"""
check_edges.py — golden-style guard for the Written<->Written echo register
(v1/edges.yaml), in the pattern of oral_provenance/check_coverage.py.

Checks, per edge:
  1. required fields present; id unique
  2. verdict in the register's own vocabulary; a non-open verdict requires
     owner_signoff + confidence (high/medium/low)
  3. signature has kind (from meta.signature_kinds) + he/translit/en
  4. anchor.osis exists in the verses table; target.ref is a bare Tanakh verse
  5. provenance: origin includes 'sefaria-link' -> the (anchor, target) pair
     must exist in echo_candidates; origin includes a chain-citation -> at
     least one evidence line must name that source; every edge needs >= 1
  6. every evidence line that states a rarity carries 'rarity=' + a date
     (real-query discipline: numbers come from verify_rarity.py / FTS runs)

Exit 1 on any violation. The register stays canonical; this only guards it.
"""

import re
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
REG = yaml.safe_load((Path(__file__).parent / "v1" / "edges.yaml").read_text(encoding="utf-8"))

TANAKH_REF_RX = re.compile(r"^(I{1,2} )?[A-Z][A-Za-z ]+ \d+:\d+(-\d+)?$")
DATE_RX = re.compile(r"\d{4}-\d{2}-\d{2}")

REQUIRED = ["id", "anchor", "target", "signature", "evidence", "origin",
            "verdict", "confidence", "owner_signoff"]
TEXT_KEYS = ["he", "translit", "en"]


def main():
    cx = sqlite3.connect(ROOT / "torah_grok.sqlite")
    verse_osis = {r[0] for r in cx.execute("SELECT osis_id FROM verses")}
    candidates = {(a, t) for a, t in
                  cx.execute("SELECT anchor_osis, target_ref FROM echo_candidates")}

    vocab = set(REG["meta"]["verdict_vocabulary"])
    kinds = set(REG["meta"]["signature_kinds"])
    errors = []
    seen_ids = set()

    for e in REG["edges"]:
        eid = e.get("id", "<no id>")
        err = lambda msg: errors.append("%s: %s" % (eid, msg))

        if eid in seen_ids:
            err("duplicate id")
        seen_ids.add(eid)

        for k in REQUIRED:
            if k not in e:
                err("missing field '%s'" % k)

        v = e.get("verdict")
        if v not in vocab:
            err("verdict %r not in vocabulary %s" % (v, sorted(vocab)))
        if v and v != "open":
            if not e.get("owner_signoff"):
                err("non-open verdict without owner_signoff")
            if e.get("confidence") not in ("high", "medium", "low"):
                err("non-open verdict without confidence high/medium/low")

        sig = e.get("signature", {})
        if sig.get("kind") not in kinds:
            err("signature.kind %r not in %s" % (sig.get("kind"), sorted(kinds)))
        for part in ("anchor", "target", "signature"):
            d = e.get(part, {})
            for k in TEXT_KEYS:
                if not d.get(k):
                    err("%s missing %s" % (part, k))

        osis = e.get("anchor", {}).get("osis")
        if osis not in verse_osis:
            err("anchor.osis %r not in verses table" % osis)
        tref = e.get("target", {}).get("ref", "")
        if not TANAKH_REF_RX.match(tref):
            err("target.ref %r is not a bare Tanakh verse ref" % tref)

        origin = e.get("origin", [])
        ev_text = " | ".join(e.get("evidence", []))
        if not origin:
            err("empty origin")
        if "sefaria-link" in [str(o).split(" ")[0] for o in origin]:
            if (osis, tref) not in candidates:
                err("origin says sefaria-link but (%s, %s) not in echo_candidates"
                    % (osis, tref))
        for o in origin:
            m = re.match(r"chain-citation:(.+)$", str(o))
            if m and m.group(1) not in ev_text:
                err("chain-citation %r not named in any evidence line" % m.group(1))

        rarity_lines = [ln for ln in e.get("evidence", []) if "rarity=" in ln]
        if not rarity_lines:
            err("no rarity= evidence line (real-query discipline)")
        for ln in rarity_lines:
            if not DATE_RX.search(ln):
                err("rarity line lacks a query date: %r" % ln[:60])

    if errors:
        print("ECHO REGISTER VIOLATIONS:")
        for msg in errors:
            print("  ", msg)
        sys.exit(1)

    by_verdict = {}
    for e in REG["edges"]:
        by_verdict[e["verdict"]] = by_verdict.get(e["verdict"], 0) + 1
    print("edges: %d (%s) · candidates in DB: %d · register status: %s"
          % (len(REG["edges"]),
             " · ".join("%s=%d" % kv for kv in sorted(by_verdict.items())),
             len(candidates), REG["meta"]["status"]))
    print("ALL EDGES VALID · written_echo v1")


if __name__ == "__main__":
    main()
