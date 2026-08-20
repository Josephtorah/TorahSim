#!/usr/bin/env python3
"""
corpus_world.py — THE WORLD: one persistent state built by running every
frozen unit in canonical text order (Pre-Code; owner design 2026-08-09).

The simulation frame (owner's): the CODE is the physics — frozen YAMLs +
interpreter, built once, never altered by running. The WORLD is the
simulation state: facts, open demands, names, standing law, accumulated
in canonical order with unit+verse provenance. There is ONE world; runs
revise it in place and the journal keeps every prior revision as history
(audit trail, no standing). Nothing is ever closed by hand — settlement
is always computed (in-unit exact RESULT) or authored-with-citation
(logic/corpus/settlement_links.yaml), never stamped.

Config (authored, YAML): logic/corpus/entity_registry.yaml (who is who;
uncertainty marked), logic/corpus/settlement_links.yaml (cross-unit
demand settlements with basis).

Output: world.sqlite (current state + append-only journal +
per-unit checkpoints) and logic/corpus/CORPUS_TRUTH.py (baked proof —
rerunning it refolds the world and asserts identity).

Guarantees:
  - per-unit consistency: the fold's extraction of each unit is checked
    against the Stage D interpreter's actual final state — any drift is
    a hard stop, so the world can never disagree with the machine.
  - determinism: fold(write=False) from the same law + config is
    identical every time; CORPUS_TRUTH.py re-proves it.

Usage:
  python3 corpus_world.py           # fold, write DB + truth file
  python3 corpus_world.py verify    # refold in memory, compare to DB
"""
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import sys as _vsys; from pathlib import Path as _VP; _vsys.path.insert(0, str(_VP(__file__).resolve().parent / "vendor"))
import yaml
import run_unit as ru

UNITS_DIR = ROOT / "logic" / "units"
CORPUS_DIR = ROOT / "logic" / "corpus"
DB_PATH = ROOT / "data" / "world.sqlite"
TRUTH_PATH = CORPUS_DIR / "CORPUS_TRUTH.py"
BOOK_ORDER = {"Gen": 1, "Exod": 2, "Lev": 3, "Num": 4, "Deut": 5}


# ---------------------------------------------------------------- loading
def frozen_units_in_canonical_order():
    """[(uid, unit_dict)] sorted by text position of the first step."""
    out = []
    for p in sorted(UNITS_DIR.glob("*.yaml")):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not (isinstance(d, dict) and d.get("meta", {}).get("status") == "frozen"):
            continue
        r = d["boot_steps"][0]["ref"]
        book, ch, vs = r.split(".")
        key = (BOOK_ORDER[book], int(ch), int(vs.split("-")[0]))
        out.append((key, d["meta"]["id"], d))
    out.sort(key=lambda t: t[0])
    return [(uid, d) for _, uid, d in out]


def load_config():
    reg = yaml.safe_load((CORPUS_DIR / "entity_registry.yaml").read_text(
        encoding="utf-8")) or {}
    links = yaml.safe_load((CORPUS_DIR / "settlement_links.yaml").read_text(
        encoding="utf-8")) or {}
    # token -> [(entity_id, units_or_None)]
    tokmap = {}
    for e in reg.get("entities", []):
        for m in e.get("members", []):
            tokmap.setdefault(m["token"], []).append(
                (e["id"], set(m.get("units") or []) or None))
    return tokmap, reg.get("entities", []), links.get("links") or []


def entity_for(tokmap, token, uid):
    """Resolve a unit-local token to its corpus entity id (default rule:
    an unlisted token is its own singleton entity)."""
    for eid, units in tokmap.get(token, []):
        if units is None or uid in units:
            return eid
    return token


# ------------------------------------------------------------ extraction
def _names_list(blob):
    return [x.strip() for x in blob.split(",") if x.strip()]


def fold(write=True):
    """Run the whole simulation: every frozen unit, canonical order.
    Returns the world dict; optionally writes DB + truth file."""
    tokmap, reg_entities, links = load_config()
    units = frozen_units_in_canonical_order()

    W = {"facts": [], "events": [], "demands": [], "mentions": [],
         "names": [], "standing": [], "tests": [], "ledger": [],
         "units": [], "checkpoints": []}
    seq = 0

    def mention(uid, ref, token, role):
        W["mentions"].append({"seq": seq, "unit": uid, "ref": ref,
                              "token": token, "role": role,
                              "entity": entity_for(tokmap, token, uid)})

    for uid, unit in units:
        opn_before = sum(1 for d in W["demands"] if d["status"] == "OPEN")
        u_facts, u_invariants, u_partitions = [], [], []
        u_created, u_presup, u_names = set(), set(), {}
        u_declares, u_tests, u_ledger = 0, [], []
        u_mach_events = 0  # mirrors run_unit: most handlers log an event
        u_open = []  # this unit's queue (mirror of SPECS)

        for st in unit["boot_steps"]:
            ref = st["ref"]
            for op in st.get("operators", []):
                seq += 1
                k, e = op.get("op"), str(op.get("expr_en", ""))
                if k == "PRECONDITION_STATE":
                    for f in re.findall(r"HOLDS\((.+?),\s*t\d+\)", e):
                        f = f.strip()
                        u_facts.append(f)
                        W["facts"].append({"seq": seq, "unit": uid,
                                           "ref": ref, "fact": f})
                elif k == "EVENT":
                    verb = re.match(r"(\w+)\(e\d+\)", e)
                    agent = re.search(r"Agent\(e\d+,\s*([\w-]+)\)", e)
                    themes = re.findall(r"Theme\(e\d+,\s*([\w-]+)\)", e)
                    u_mach_events += 1
                    W["events"].append({"seq": seq, "unit": uid, "ref": ref,
                                        "verb": verb.group(1) if verb else "?",
                                        "agent": agent.group(1) if agent else None,
                                        "themes": themes})
                    if agent:
                        mention(uid, ref, agent.group(1), "agent")
                elif k == "REGISTRY_INSTALL":
                    m = re.search(r"WORLD \+= \{([^}]*)\}", e)
                    for n in _names_list(m.group(1)):
                        u_created.add(n)
                        mention(uid, ref, n, "install")
                elif k == "NOTE_PRESUPPOSED":
                    m = re.match(r"(.+?) are READ", e)
                    for n in _names_list(m.group(1)):
                        u_presup.add(n)
                        mention(uid, ref, n, "presupposed")
                elif k == "NAME":
                    for ent, label in re.findall(
                            r"name\(([\w-]+)\)\s*:=\s*(\w+)", e):
                        u_names[ent] = label
                        u_mach_events += 1
                        W["names"].append({"seq": seq, "unit": uid,
                                           "ref": ref, "token": ent,
                                           "label": label})
                        mention(uid, ref, ent, "named")
                elif k == "DECLARE":
                    sp = re.search(r"DECLARE\((\w+),", e)
                    mood = ("CMD-US?" if "CMD-US?(" in e else
                            "CMD-US" if "CMD-US(" in e else
                            "LET?" if "LET?(" in e else
                            "LET-NOT" if "LET-NOT(" in e else "LET")
                    dm = re.search(r"(?:LET\??(?:-NOT)?|CMD-US\??)\((.+)\)\)", e)
                    u_declares += 1
                    u_mach_events += 1
                    d = {"seq": seq, "unit": uid, "ref": ref,
                         "speaker": sp.group(1) if sp else "?",
                         "mood": mood,
                         "demand": dm.group(1).strip() if dm else "?",
                         "status": "OPEN", "settled_seq": None,
                         "settled_unit": None, "settled_ref": None,
                         "settle_kind": None, "basis_en": None,
                         "uncertain": 0}
                    W["demands"].append(d)
                    u_open.append(d)
                    if sp:
                        mention(uid, ref, sp.group(1), "speaker")
                elif k == "RESULT":
                    hm = re.search(r"HOLDS\((.+?),\s*t\d+\)", e)
                    want = hm.group(1).strip()
                    u_mach_events += 1
                    hit = next((d for d in u_open if d["demand"] == want), None)
                    if hit is not None:
                        hit.update(status="SETTLED", settled_seq=seq,
                                   settled_unit=uid, settled_ref=ref,
                                   settle_kind="in_unit")
                        u_open.remove(hit)
                    else:
                        # interpreter tolerates a RESULT with no queue match
                        # (the demandee-mismatch class) — record, don't stop
                        W["standing"].append({"seq": seq, "unit": uid,
                                              "ref": ref,
                                              "kind": "RESULT_UNMATCHED",
                                              "payload": want})
                    em = re.search(r"exists\((\w+)\)", want)
                    if em:  # fiat-result install, mirrors h_result
                        u_created.add(em.group(1))
                        mention(uid, ref, em.group(1), "install")
                elif k == "TEST":
                    m = re.search(r"(PASS|FAIL)\((\w+),\s*(\w+)\)", e)
                    u_tests.append((m.group(1), m.group(2), m.group(3)))
                    W["tests"].append({"seq": seq, "unit": uid, "ref": ref,
                                       "verdict": m.group(1),
                                       "oracle": m.group(2),
                                       "theme": m.group(3)})
                elif k == "INVARIANT":
                    m = re.search(r"INVARIANT\((.+)\)\s*during", e)
                    u_invariants.append(m.group(1).strip())
                    W["standing"].append({"seq": seq, "unit": uid, "ref": ref,
                                          "kind": "INVARIANT",
                                          "payload": m.group(1).strip()})
                elif k == "EVENT_PARTITION":
                    m = re.search(r"between\(([\w-]+),\s*([\w-]+)\)", e)
                    u_partitions.append((m.group(1), m.group(2)))
                    u_mach_events += 1
                    W["standing"].append({"seq": seq, "unit": uid, "ref": ref,
                                          "kind": "PARTITION",
                                          "payload": "%s | %s" % m.groups()})
                elif k == "COMMIT":
                    m = re.search(r"LEDGER\[day (\d+)\]", e)
                    u_ledger.append(int(m.group(1)))
                    W["ledger"].append({"seq": seq, "unit": uid, "ref": ref,
                                        "day": int(m.group(1))})
                elif k == "BLESS":
                    m = re.search(r"BLESS\((\w+),\s*([\w-]+)\)", e)
                    mt = re.search(r"MANDATE \{([^}]*)\}", e)
                    u_mach_events += 1
                    for item in _names_list(mt.group(1)) if mt else []:
                        f = "mandate: %s" % item   # h_bless: standing fact
                        u_facts.append(f)
                        W["facts"].append({"seq": seq, "unit": uid,
                                           "ref": ref, "fact": f})
                    W["standing"].append({"seq": seq, "unit": uid, "ref": ref,
                                          "kind": "BLESS",
                                          "payload": "%s -> %s" % m.groups()})
                    mention(uid, ref, m.group(1), "blesser")
                    mention(uid, ref, m.group(2), "blessee")
                elif k == "ASSIGN":
                    # office binding — a REGISTRY write like NAME (h_assign)
                    pairs = re.findall(r"([\w-]+)->([\w-]+)", e)
                    u_mach_events += len(pairs)
                    for ent, role in pairs:
                        u_names[ent] = role
                        W["names"].append({"seq": seq, "unit": uid,
                                           "ref": ref, "token": ent,
                                           "label": role})
                        mention(uid, ref, ent, "assigned")
                    W["standing"].append({"seq": seq, "unit": uid, "ref": ref,
                                          "kind": "ASSIGN", "payload": e[:400]})
                elif k in ("STATUTE", "HANDLER", "CASE", "PATTERN"):
                    # law operators install standing WORLD facts (run_unit
                    # h_case/h_handler/h_pattern/h_statute string formats)
                    u_mach_events += 1
                    if k == "CASE":
                        m = re.search(r"CASE\((.+)\)\s*ROUTE\(([\w-]+)\)", e)
                        f = "case: %s -> %s" % (m.group(1).strip(), m.group(2))
                    elif k == "HANDLER":
                        m = re.search(r"HANDLER IF\((.+)\) THEN\((.+)\)", e)
                        f = "handler: IF(%s) THEN(%s)" % (
                            m.group(1).strip(), m.group(2).strip())
                    elif k == "PATTERN":
                        m = re.search(r"PATTERN\((.+)\)", e)
                        f = "pattern: %s" % m.group(1).strip()
                    else:
                        m = re.search(r"STATUTE (FORBID|BIND)\((.+)\)", e)
                        f = "statute: %s(%s)" % (m.group(1), m.group(2).strip())
                    u_facts.append(f)
                    W["facts"].append({"seq": seq, "unit": uid, "ref": ref,
                                       "fact": f})
                    W["standing"].append({"seq": seq, "unit": uid, "ref": ref,
                                          "kind": k, "payload": f})
                elif k == "SECTION":
                    u_mach_events += 1
                    W["standing"].append({"seq": seq, "unit": uid, "ref": ref,
                                          "kind": k, "payload": e[:400]})
                elif k in ("TRIPLE", "NOTE_SPEC_DELTA",
                           "TIME_ANCHOR", "NOTE_ZERO_EVENTS",
                           "ORAL_UTTERANCE", "WITNESS_STATE"):
                    W["standing"].append({"seq": seq, "unit": uid, "ref": ref,
                                          "kind": k, "payload": e[:400]})
                else:
                    raise SystemExit("unmapped operator kind in fold: %s (%s)"
                                     % (k, uid))

        # ---- per-unit consistency gate vs the Stage D interpreter -------
        truth = ru.run_steps(unit)
        checks = [
            (sorted(u_facts), sorted(truth.WORLD["facts"]), "facts"),
            (u_created, truth.created_set(), "created"),
            (u_presup, truth.presupposed_set(), "presupposed"),
            (u_names, truth.REGISTRY["names"], "names"),
            (sorted(d["demand"] for d in u_open),
             sorted(e["demand"] for e in truth.SPECS["queue"]),
             "open demands"),
            (u_declares, len(truth.SPECS["log"]), "declares"),
            (u_tests, [(t["verdict"], t["oracle"], t["theme"])
                       for t in truth.TESTS], "tests"),
            (sorted(u_ledger), sorted(truth.LEDGER), "ledger"),
            (u_mach_events, len(truth.EVENTS), "events"),
            (sorted(u_invariants), sorted(truth.WORLD["invariants"]),
             "invariants"),
        ]
        for got, want, label in checks:
            if got != want:
                raise SystemExit("FOLD DRIFT %s (%s): fold=%r interpreter=%r"
                                 % (uid, label, got, want))

        opn_now = sum(1 for d in W["demands"] if d["status"] == "OPEN")
        W["units"].append({"seq_unit": len(W["units"]) + 1, "unit": uid,
                           "first_ref": unit["boot_steps"][0]["ref"],
                           "steps": len(unit["boot_steps"]),
                           "facts": len(u_facts),
                           "opened": opn_now - opn_before + 0})
        W["checkpoints"].append({
            "seq_unit": len(W["units"]), "unit": uid, "seq": seq,
            "facts_n": len(W["facts"]),
            "open_n": opn_now,
            "state_hash": _state_hash(W)})

    # ---- authored cross-unit settlements (cited, possibly uncertain) ----
    for ln in links:
        cand = [d for d in W["demands"]
                if d["status"] == "OPEN" and d["demand"] == ln["demand"]
                and d["unit"] == ln["from_unit"]]
        if not cand:
            raise SystemExit("settlement link matches no open demand: %r" % ln)
        cand[0].update(status="SETTLED",
                       settled_unit=ln["settled_by"]["unit"],
                       settled_ref=ln["settled_by"]["ref"],
                       settle_kind="authored",
                       basis_en=ln.get("basis_en"),
                       uncertain=1 if ln.get("uncertain") else 0)

    if write:
        _write_db(W, reg_entities)
        _write_truth(W)
    return W


# --------------------------------------------------------------- hashing
def _state_hash(W):
    basis = {"facts": [(f["unit"], f["ref"], f["fact"]) for f in W["facts"]],
             "open": sorted(d["demand"] for d in W["demands"]
                            if d["status"] == "OPEN"),
             "names": [(n["token"], n["label"]) for n in W["names"]]}
    return hashlib.sha256(
        json.dumps(basis, sort_keys=True, ensure_ascii=False)
        .encode("utf-8")).hexdigest()[:16]


# ------------------------------------------------------------------ store
def _write_db(W, reg_entities):
    db = sqlite3.connect(str(DB_PATH))
    c = db.cursor()
    c.executescript("""
    CREATE TABLE IF NOT EXISTS journal(
      revision INTEGER PRIMARY KEY, built_at TEXT, law_commit TEXT,
      units_n INT, facts_n INT, open_n INT, settled_n INT, state_hash TEXT);
    DROP TABLE IF EXISTS units;    DROP TABLE IF EXISTS facts;
    DROP TABLE IF EXISTS events;   DROP TABLE IF EXISTS demands;
    DROP TABLE IF EXISTS mentions; DROP TABLE IF EXISTS names;
    DROP TABLE IF EXISTS standing; DROP TABLE IF EXISTS tests;
    DROP TABLE IF EXISTS ledger;   DROP TABLE IF EXISTS checkpoints;
    DROP TABLE IF EXISTS registry;
    CREATE TABLE units(seq_unit INT, unit TEXT, first_ref TEXT, steps INT,
                       facts INT, opened INT);
    CREATE TABLE facts(seq INT, unit TEXT, ref TEXT, fact TEXT);
    CREATE TABLE events(seq INT, unit TEXT, ref TEXT, verb TEXT,
                        agent TEXT, themes TEXT);
    CREATE TABLE demands(seq INT, unit TEXT, ref TEXT, speaker TEXT,
                         mood TEXT, demand TEXT, status TEXT,
                         settled_seq INT, settled_unit TEXT,
                         settled_ref TEXT, settle_kind TEXT,
                         basis_en TEXT, uncertain INT);
    CREATE TABLE mentions(seq INT, unit TEXT, ref TEXT, token TEXT,
                          role TEXT, entity TEXT);
    CREATE TABLE names(seq INT, unit TEXT, ref TEXT, token TEXT, label TEXT);
    CREATE TABLE standing(seq INT, unit TEXT, ref TEXT, kind TEXT,
                          payload TEXT);
    CREATE TABLE tests(seq INT, unit TEXT, ref TEXT, verdict TEXT,
                       oracle TEXT, theme TEXT);
    CREATE TABLE ledger(seq INT, unit TEXT, ref TEXT, day INT);
    CREATE TABLE checkpoints(seq_unit INT, unit TEXT, seq INT,
                             facts_n INT, open_n INT, state_hash TEXT);
    CREATE TABLE registry(entity TEXT, en TEXT, kind TEXT, token TEXT,
                          units TEXT, note TEXT);
    """)
    c.executemany("INSERT INTO units VALUES (?,?,?,?,?,?)",
                  [(u["seq_unit"], u["unit"], u["first_ref"], u["steps"],
                    u["facts"], u["opened"]) for u in W["units"]])
    c.executemany("INSERT INTO facts VALUES (?,?,?,?)",
                  [(f["seq"], f["unit"], f["ref"], f["fact"])
                   for f in W["facts"]])
    c.executemany("INSERT INTO events VALUES (?,?,?,?,?,?)",
                  [(e["seq"], e["unit"], e["ref"], e["verb"], e["agent"],
                    ",".join(e["themes"])) for e in W["events"]])
    c.executemany("INSERT INTO demands VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  [(d["seq"], d["unit"], d["ref"], d["speaker"], d["mood"],
                    d["demand"], d["status"], d["settled_seq"],
                    d["settled_unit"], d["settled_ref"], d["settle_kind"],
                    d["basis_en"], d["uncertain"]) for d in W["demands"]])
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
    c.executemany("INSERT INTO ledger VALUES (?,?,?,?)",
                  [(l["seq"], l["unit"], l["ref"], l["day"])
                   for l in W["ledger"]])
    c.executemany("INSERT INTO checkpoints VALUES (?,?,?,?,?,?)",
                  [(cp["seq_unit"], cp["unit"], cp["seq"], cp["facts_n"],
                    cp["open_n"], cp["state_hash"])
                   for cp in W["checkpoints"]])
    rows = []
    for e in reg_entities:
        for m in e.get("members", []):
            rows.append((e["id"], e.get("en", ""), e.get("kind", ""),
                         m["token"], ",".join(m.get("units") or []),
                         (e.get("note") or "").strip()))
    c.executemany("INSERT INTO registry VALUES (?,?,?,?,?,?)", rows)

    try:
        law = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True,
                             cwd=str(ROOT)).stdout.strip()
    except Exception:
        law = "?"
    open_n = sum(1 for d in W["demands"] if d["status"] == "OPEN")
    c.execute("INSERT INTO journal(built_at, law_commit, units_n, facts_n, "
              "open_n, settled_n, state_hash) VALUES (?,?,?,?,?,?,?)",
              (time.strftime("%Y-%m-%d %H:%M:%S"), law, len(W["units"]),
               len(W["facts"]), open_n,
               len(W["demands"]) - open_n, _state_hash(W)))
    db.commit()
    db.close()


# ------------------------------------------------------------------ truth
def _write_truth(W):
    open_d = sorted((d["unit"], d["ref"], d["mood"], d["demand"])
                    for d in W["demands"] if d["status"] == "OPEN")
    body = '''#!/usr/bin/env python3
# CORPUS_TRUTH.py — GENERATED by corpus_world.py. Do not edit — regenerate.
# Baked from the fold of ALL frozen units in canonical order; running this
# file refolds the world and asserts it lands in the identical state.
# Experimental model — not binding religious law.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "press"))
import corpus_world

W = corpus_world.fold(write=False)
assert len(W["units"]) == %d
assert len(W["facts"]) == %d
assert len(W["demands"]) == %d
assert len(W["events"]) == %d
assert len(W["names"]) == %d
assert len(W["standing"]) == %d
open_d = sorted((d["unit"], d["ref"], d["mood"], d["demand"])
                for d in W["demands"] if d["status"] == "OPEN")
assert len(open_d) == %d
assert open_d == %r
assert corpus_world._state_hash(W) == %r
print("CORPUS TRUTH GREEN — one world, %%d units, %%d facts, "
      "%%d demands (%%d open), hash %%s" %% (
      len(W["units"]), len(W["facts"]), len(W["demands"]),
      len(open_d), corpus_world._state_hash(W)))
''' % (len(W["units"]), len(W["facts"]), len(W["demands"]),
       len(W["events"]), len(W["names"]), len(W["standing"]),
       len(open_d), open_d, _state_hash(W))
    TRUTH_PATH.write_text(body, encoding="utf-8")


# ------------------------------------------------------------------ modes
def verify():
    W = fold(write=False)
    db = sqlite3.connect(str(DB_PATH))
    row = db.execute("SELECT units_n, facts_n, open_n, state_hash FROM "
                     "journal ORDER BY revision DESC LIMIT 1").fetchone()
    db.close()
    open_n = sum(1 for d in W["demands"] if d["status"] == "OPEN")
    fresh = (len(W["units"]), len(W["facts"]), open_n, _state_hash(W))
    if row is None:
        raise SystemExit("no stored world to verify against")
    if tuple(row) != fresh:
        raise SystemExit("VERIFY RED: stored %r != fresh %r"
                         % (tuple(row), fresh))
    print("VERIFY GREEN — stored world = fresh fold (hash %s)" % fresh[3])


def _report(W):
    open_d = [d for d in W["demands"] if d["status"] == "OPEN"]
    settled = [d for d in W["demands"] if d["status"] == "SETTLED"]
    print("THE WORLD — %d units, canonical order %s .. %s" % (
        len(W["units"]), W["units"][0]["unit"], W["units"][-1]["unit"]))
    print("facts %d · events %d · names %d · standing %d · tests %d" % (
        len(W["facts"]), len(W["events"]), len(W["names"]),
        len(W["standing"]), len(W["tests"])))
    print("demands %d: %d settled (%d in-unit, %d authored), %d OPEN" % (
        len(W["demands"]), len(settled),
        sum(1 for d in settled if d["settle_kind"] == "in_unit"),
        sum(1 for d in settled if d["settle_kind"] == "authored"),
        len(open_d)))
    for d in open_d:
        print("  OPEN  %-12s %-11s %s(%s)  %s" % (
            d["unit"].split("_")[0] + "_" + d["unit"].split("_")[1],
            d["ref"], d["mood"], d["speaker"], d["demand"]))
    print("state hash %s" % _state_hash(W))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "verify":
        verify()
    else:
        W = fold(write=True)
        _report(W)
        print("wrote %s + %s" % (DB_PATH.name, TRUTH_PATH.name))
