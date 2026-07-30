#!/usr/bin/env python3
"""
verify_rarity.py — evidence tool for the Written<->Written echo register.

For each signature phrase (consonantal Hebrew), asks Sefaria's search API how many
DISTINCT Tanakh verses contain it, and lists them. This is the "rarity count" that
an edge's evidence line must cite — always from a real query, never from memory.

Sefaria etiquette (standing rule): sequential, 0.5s delay between queries, tiny
payloads. Every run is logged by hand in Data/FETCHLOG.md.

Usage:
    python3 verify_rarity.py "תהו ובהו" ["phrase2" ...]     # ad-hoc
    python3 verify_rarity.py --edges                          # all signatures in v1/edges.yaml

Output per phrase: rarity=N (distinct verses) + the verse list. The raw hit count
is larger because Sefaria indexes each text VERSION separately; we dedupe by ref.
"""

import json
import sys
import time
import urllib.request
from pathlib import Path

API = "https://www.sefaria.org/api/search-wrapper"
DELAY = 0.5


def rarity(phrase):
    body = json.dumps({
        "query": phrase, "type": "text", "field": "exact", "slop": 0,
        "size": 100, "filters": ["Tanakh"], "filter_fields": ["path"],
        "source_proj": True, "sort_type": "score", "sort_method": "score",
    }).encode("utf-8")
    req = urllib.request.Request(API, data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    refs = sorted({h["_source"]["ref"] for h in d.get("hits", {}).get("hits", [])})
    return refs


def phrases_from_edges():
    import yaml
    edges = yaml.safe_load(
        (Path(__file__).parent / "v1" / "edges.yaml").read_text(encoding="utf-8"))
    return [(e["id"], e["signature"]["he"]) for e in edges["edges"]]


def main():
    if "--edges" in sys.argv:
        jobs = phrases_from_edges()
    else:
        jobs = [(None, p) for p in sys.argv[1:]]
    if not jobs:
        print(__doc__)
        sys.exit(1)
    for i, (label, phrase) in enumerate(jobs):
        if i:
            time.sleep(DELAY)
        refs = rarity(phrase)
        head = ("[%s] " % label) if label else ""
        print("%s%s -> rarity=%d" % (head, phrase, len(refs)))
        for ref in refs:
            print("    ", ref)


if __name__ == "__main__":
    main()
