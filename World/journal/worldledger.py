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

    def __init__(self, layer, source, start_chain=None, header=None):
        self.layer = layer
        self.source = source           # generator id, e.g. "build_world/0"
        self.events = []
        self._chain = start_chain or "genesis"   # chain seed for the first event — THE LOOP step 4 (2026-09-09): an APPENDED segment
        self.start_chain = start_chain           # continues from the base's chain at the fork (D9); the default keeps every base segment byte-identical
        self.header = dict(header or {})         # extra header fields (the base's name, the fork line) — absent on a base segment

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
            head = {"segment": self.layer, "source": self.source,
                    "events": len(self.events), "chain_head": self._chain}
            if self.start_chain:                       # THE LOOP step 4 (2026-09-09): an appended segment names its start and its fork
                head["start_chain"] = self.start_chain
                head.update(self.header)
            f.write(canon(head) + "\n")
            for ev in self.events:
                f.write(canon(ev) + "\n")

    @staticmethod
    def verify(path):
        """Recompute the chain; True iff no line was mutated in place."""
        with open(path, encoding="utf-8") as f:
            head = json.loads(f.readline())
            chain = head.get("start_chain") or "genesis"     # THE LOOP step 4: an appended segment verifies from its start chain
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
    # THE LOOP step 2's remainder (2026-09-09; World/step9/THE_LOOP.md): the events table carries each row's SOURCE — the segment
    # header's own field, read where the header line was discarded — so the four run worlds' rows are told apart and the
    # appended segments of step 4 (D9) have their name; the four run views (World/journal/run_views.sql) are created over it
    c.executescript("""
    DROP TABLE IF EXISTS events;
    CREATE TABLE events(seq INT, op INT, layer TEXT, kind TEXT, subj TEXT,
                        data TEXT, unit TEXT, ref TEXT, chain TEXT, source TEXT);
    CREATE INDEX idx_kind ON events(kind);
    CREATE INDEX idx_subj ON events(subj);
    CREATE INDEX idx_op ON events(op);
    CREATE INDEX idx_source ON events(source);
    """)
    n = 0
    for path in segment_paths:
        with open(path, encoding="utf-8") as f:
            header = json.loads(f.readline())
            source = header.get("source")
            for line in f:
                ev = json.loads(line)
                c.execute("INSERT INTO events VALUES (?,?,?,?,?,?,?,?,?,?)",
                          (ev["s"], ev["op"], ev["layer"], ev["kind"],
                           ev["subj"], canon(ev["data"]),
                           ev["prov"].get("unit"), ev["prov"].get("ref"),
                           ev["chain"], source))
                n += 1
    db.commit()
    db.close()
    return n
