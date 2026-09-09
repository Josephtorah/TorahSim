#!/usr/bin/env python3
"""worldledger.py — the world journal's envelope, hash chain, and index.

The ONLY stable contract (owner design 2026-08-24, THE_WORLD.md):
one event per JSONL line, envelope {s, op, layer, kind, subj, data, prov,
chain}. Append-only; corrections are new events. No timestamps inside
segments (byte-grade determinism — peer-review delta 2). The chain field
makes in-place mutation DETECTABLE (peer delta b): each event's chain =
sha256(prev_chain + canonical_json(event_sans_chain))[:16].

SQLite is the INDEX, never the pen-holder: rebuilt from segments, never
written directly (single-writer rule).
"""
import hashlib
import json
import sqlite3


def canon(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


class Segment:
    """One append-only journal segment (one layer, one build)."""

    def __init__(self, layer, source):
        self.layer = layer
        self.source = source           # generator id, e.g. "build_world/0"
        self.events = []
        self._chain = "genesis"        # chain seed for the first event

    def append(self, kind, subj, data, prov, op=None):
        ev = {"s": len(self.events) + 1, "op": op, "layer": self.layer,
              "kind": kind, "subj": subj, "data": data, "prov": prov}
        self._chain = hashlib.sha256(
            (self._chain + canon(ev)).encode("utf-8")).hexdigest()[:16]
        ev["chain"] = self._chain
        self.events.append(ev)
        return ev

    def write(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(canon({"segment": self.layer, "source": self.source,
                           "events": len(self.events),
                           "chain_head": self._chain}) + "\n")
            for ev in self.events:
                f.write(canon(ev) + "\n")

    @staticmethod
    def verify(path):
        """Recompute the chain; True iff no line was mutated in place."""
        chain = "genesis"
        with open(path, encoding="utf-8") as f:
            head = json.loads(f.readline())
            for line in f:
                ev = json.loads(line)
                claimed = ev.pop("chain")
                chain = hashlib.sha256(
                    (chain + canon(ev)).encode("utf-8")).hexdigest()[:16]
                if chain != claimed:
                    return False
        return chain == head["chain_head"]


def index_sqlite(db_path, segment_paths):
    """Rebuild the index from segments (drop-and-rebuild, corpus pattern)."""
    db = sqlite3.connect(db_path)
    c = db.cursor()
    c.executescript("""
    DROP TABLE IF EXISTS events;
    CREATE TABLE events(seq INT, op INT, layer TEXT, kind TEXT, subj TEXT,
                        data TEXT, unit TEXT, ref TEXT, chain TEXT);
    CREATE INDEX idx_kind ON events(kind);
    CREATE INDEX idx_subj ON events(subj);
    CREATE INDEX idx_op ON events(op);
    """)
    n = 0
    for path in segment_paths:
        with open(path, encoding="utf-8") as f:
            f.readline()
            for line in f:
                ev = json.loads(line)
                c.execute("INSERT INTO events VALUES (?,?,?,?,?,?,?,?,?)",
                          (ev["s"], ev["op"], ev["layer"], ev["kind"],
                           ev["subj"], canon(ev["data"]),
                           ev["prov"].get("unit"), ev["prov"].get("ref"),
                           ev["chain"]))
                n += 1
    db.commit()
    db.close()
    return n
