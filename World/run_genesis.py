#!/usr/bin/env python3
"""run_genesis.py — RUN all of Genesis, slowly, and teach while doing it.

    python3 run_genesis.py                # full run, pause at each parashah
    python3 run_genesis.py --no-pause     # stream straight through
    python3 run_genesis.py --quiet        # build + narrate to the table only

What this is: the same world build_world.py makes in one gulp, played back
one row at a time in corpus order, so a person can watch the world grow and
learn what each kind of row means. The narration is SAVED to a `narration`
table in world.sqlite, so any stretch can be re-read later:

    python3 ask.py sql "SELECT line FROM narration WHERE parashah='Vayetze'"

THE HEBREW RULE (owner, standing): Hebrew script never appears without its
English beside it — and this program QUOTES ink, it never composes Hebrew.
Every row cites the verse it came from; the Hebrew shown is lifted from that
verse's own words with the corpus's own gloss. Three classes, decided per
row: ink-backed -> quoted with gloss; entity -> its first inked form; the
machine's own notation -> English, plainly. No match -> English, honestly.

RULES OF THIS FOLDER (RESUME.md): read-only over the repo; never invent a
row; the end state MUST reconcile with corpus_world.fold() on every count
and the state hash — the slow teaching run provably builds the same world.
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

REPO = Path("<repo-old>")
HERE = Path(__file__).resolve().parent
DB = HERE / "world.sqlite"
SCHEMA = HERE / "schema.sql"
SNAP = REPO / "torah_grok.SNAPSHOT-main-51801ca.sqlite"

sys.path.insert(0, str(REPO))
import corpus_world  # noqa: E402
import build_world   # noqa: E402  (parse_ref, ref_key, reconcile — one source)

# ------------------------------------------------------------ the parashiyot
# Hebrew versification, matching the corpus's own verse table.
PARASHIYOT = [
    ("בְּרֵאשִׁית", "Bereshit", "In the beginning", ("Gen", 6, 8)),
    ("נֹחַ", "Noach", "Noah", ("Gen", 11, 32)),
    ("לֶךְ־לְךָ", "Lech Lecha", "Go forth", ("Gen", 17, 27)),
    ("וַיֵּרָא", "Vayera", "And He appeared", ("Gen", 22, 24)),
    ("חַיֵּי שָׂרָה", "Chayei Sarah", "The life of Sarah", ("Gen", 25, 18)),
    ("תּוֹלְדֹת", "Toledot", "Generations", ("Gen", 28, 9)),
    ("וַיֵּצֵא", "Vayetze", "And he went out", ("Gen", 32, 3)),
    ("וַיִּשְׁלַח", "Vayishlach", "And he sent", ("Gen", 36, 43)),
    ("וַיֵּשֶׁב", "Vayeshev", "And he settled", ("Gen", 40, 23)),
    ("מִקֵּץ", "Miketz", "At the end", ("Gen", 44, 17)),
    ("וַיִּגַּשׁ", "Vayigash", "And he drew near", ("Gen", 47, 27)),
    ("וַיְחִי", "Vayechi", "And he lived", ("Gen", 50, 26)),
]

# ------------------------------------------------------- first-time lessons
LESSONS = {
    "spine": (
        "LESSON — THE SPINE. Before anything happens, the program lays down\n"
        "the clock: every verse of Genesis in reading order. Every question\n"
        "about the world is 'as of' a point on this line. Nothing here is a\n"
        "happening yet — it is the empty calendar the happenings land on."),
    "fact": (
        "LESSON — A FACT. A fact is something a verse installs as standing\n"
        "truth in the world: the earth was unformed, the human is formed,\n"
        "the field has no shrub yet. The machine holds it from this verse\n"
        "on. Facts only accumulate — the world never forgets one."),
    "event": (
        "LESSON — AN EVENT. An event is something HAPPENING: a verb with an\n"
        "actor (and sometimes things acted on). Facts are the standing\n"
        "furniture; events are the motion between them."),
    "demand": (
        "LESSON — A DEMAND. When someone commands, asks, or vows, an\n"
        "obligation OPENS, and it stays open until a later verse settles\n"
        "it. Watching demands open and close is watching the book's\n"
        "unfinished business. Some stay open for the whole book."),
    "settle": (
        "LESSON — A SETTLEMENT. A demand raised earlier is now discharged —\n"
        "the machine points from the verse that closed it back to the verse\n"
        "that opened it. This is the bookkeeping most readers do in their\n"
        "heads; here it is a table."),
    "name": (
        "LESSON — A NAMING. Someone or something receives a name — or a NEW\n"
        "name. The world keeps every name with the span of verses it was\n"
        "valid for, so 'what was he called at this verse?' has an exact\n"
        "answer (Abram until 17:5, Abraham after)."),
    "standing": (
        "LESSON — A WITNESS ROW. The tradition's own reading, seated beside\n"
        "the machine: what the chain of transmission says this verse\n"
        "carries. These rows come from the reading work (the ledgers), and\n"
        "each cites the sources actually read."),
    "test": (
        "LESSON — A TEST. One of the machine's instruments fires and\n"
        "records a verdict against the text itself. Rare, and worth\n"
        "noticing every time."),
    "unit": (
        "LESSON — A UNIT CLOSES. The corpus is derived in blocks (73 for\n"
        "Genesis). At each close the machine takes stock: how many facts\n"
        "stand, how many obligations remain open."),
}

STRIP_ACCENTS = re.compile("[֑-ֽ֯]")


def clean_he(s):
    return STRIP_ACCENTS.sub("", s or "").replace("/", "").replace("־", "-").strip()


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


# ------------------------------------------------------------- ink resolver
class Ink:
    """Quote-never-compose: resolve a fold token to the written form in the
    verse the row itself cites. Failure returns None and the caller shows
    English — never a guessed Hebrew form."""

    def __init__(self):
        db = sqlite3.connect(SNAP)
        self.verse = {}
        for osis, tr, he, gl in db.execute(
                "SELECT v.osis_id, w.translit, w.he, w.gloss FROM words w "
                "JOIN verses v ON w.verse_id = v.id"):
            self.verse.setdefault(osis, []).append(
                (norm(tr), [norm(p) for p in re.split(r"[-/]", tr or "") if p],
                 clean_he(he), (gl or "").strip()))
        db.close()
        self.entity_cache = {}
        self.hits = 0
        self.misses = 0

    def word(self, ref, token):
        t = norm(token)
        if not t or len(t) < 2:
            return None
        words = self.verse.get(ref, [])
        for full, parts, he, gl in words:          # exact written form
            if full == t:
                return he, gl
        for full, parts, he, gl in words:          # prefix-stripped (the
            for i in range(1, len(parts)):         # morphology layer's gift)
                if "".join(parts[i:]) == t:
                    return he, gl
        if len(t) >= 5:
            for full, parts, he, gl in words:      # last resort, containment
                if t in full or (len(full) >= 5 and full in t):
                    return he, gl
        return None

    def entity(self, ent, W):
        """An entity's canonical ink: its first resolvable mention."""
        if ent in self.entity_cache:
            return self.entity_cache[ent]
        got = None
        for m in W["mentions"]:
            if m["entity"] == ent or m["token"] == ent:
                got = self.word(m["ref"], m["token"])
                if got:
                    break
        self.entity_cache[ent] = got
        return got

    GLUE = {"ha", "va", "ve", "et", "ba", "be", "la", "le", "ka", "ke",
            "el", "min", "al", "ki", "lo", "es", "im", "u", "vi", "bi"}

    def phrase(self, ref, token):
        """Multiword fold token ('va_timale_ha_aretz_chamas') -> quoted ink
        if every meaningful part resolves in the cited verse. Glue particles
        are skipped; ONE unresolved content word fails the whole phrase, so
        a clause is never half-quoted."""
        parts = [p for p in re.split(r"[^A-Za-z0-9]+", token)
                 if len(p) >= 3 and p.lower() not in self.GLUE]
        if not parts:
            return None
        inks, glosses = [], []
        for p in parts:
            r = self.word(ref, p)
            if not r:
                return None
            if not inks or inks[-1] != r[0]:
                inks.append(r[0])
                glosses.append(r[1] or p)
        return " ".join(inks), " ".join(glosses)

    def show(self, ref, token, W=None, entity=False):
        """Render one token under the three-class rule. Always returns a
        string; counts its own coverage."""
        if entity and W is not None:
            r = self.word(ref, token) or self.entity(token, W)
        else:
            r = self.phrase(ref, token)   # clauses: all words or nothing
        if r:
            self.hits += 1
            he, gl = r
            return "%s (%s)" % (he, gl or token)
        self.misses += 1
        return token  # the machine's own notation, or unmatched: English.


# ---------------------------------------------------------------- the tape
def make_tape(W):
    """Every stream row, one tape, sorted by the fold's own sequence."""
    tape = []
    kinds = {"facts": "fact", "events": "event", "demands": "demand",
             "mentions": "mention", "names": "name", "standing": "standing",
             "tests": "test"}
    for kind, k1 in kinds.items():
        for r in W[kind]:
            tape.append((r["seq"], k1, r))
    for d in W["demands"]:                 # settlements narrate at their own
        if d.get("settled_seq"):           # place on the clock
            tape.append((d["settled_seq"], "settle", d))
    for k in W["checkpoints"]:
        tape.append((k["seq"], "unit", k))
    tape.sort(key=lambda x: (x[0], 0 if x[1] != "unit" else 1))
    return tape


def parashah_of(ref):
    b, c, v = build_world.parse_ref(ref)
    for he, tr, gl, (eb, ec, ev) in PARASHIYOT:
        if b != "Gen":
            return PARASHIYOT[-1][1]
        if (c, v) <= (ec, ev):
            return tr
    return PARASHIYOT[-1][1]


# ------------------------------------------------------------------ the run
def run(pause=True, quiet=False):
    print("folding the corpus (read-only) ...")
    W = corpus_world.fold(write=False)
    state_hash = corpus_world._state_hash(W)
    ink = Ink()

    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA.read_text(encoding="utf-8"))
    con.execute("CREATE TABLE narration (id INTEGER PRIMARY KEY, seq INTEGER,"
                " kind TEXT, ref TEXT, unit TEXT, parashah TEXT, line TEXT)")
    c = con.cursor()

    taught = set()
    nrows = []

    def say(seq, kind, ref, unit, line, teach=None):
        para = parashah_of(ref) if ref else None
        if teach and teach not in taught:
            taught.add(teach)
            for l in LESSONS[teach].split("\n"):
                nrows.append((None, seq, "lesson", ref, unit, para, l))
                if not quiet:
                    print("  | " + l)
        nrows.append((None, seq, kind, ref, unit, para, line))
        if not quiet:
            print("  " + line)

    # ---- the spine, laid down first and narrated once ----------------------
    seen = {}
    for key in ("facts", "events", "demands", "mentions", "names",
                "standing", "tests", "ledger"):
        for r in W[key]:
            seen.setdefault(r["ref"], []).append(r["seq"])
    unit_of = {}
    for r in W["facts"] + W["events"] + W["mentions"] + W["standing"]:
        unit_of.setdefault(r["ref"], r["unit"])
    ordered = sorted(seen, key=build_world.ref_key)
    ord_of = {}
    rows = []
    for i, ref in enumerate(ordered, start=1):
        ord_of[ref] = i
        b, ch, vs = build_world.parse_ref(ref)
        seqs = seen[ref]
        rows.append((i, ref, b, ch, vs, unit_of.get(ref), min(seqs), max(seqs)))
    c.executemany("INSERT INTO refs VALUES (?,?,?,?,?,?,?,?)", rows)
    c.executemany("INSERT INTO units VALUES (?,?,?,?,?,?)",
                  [(u["seq_unit"], u["unit"], u["first_ref"], u["steps"],
                    u["facts"], u["opened"]) for u in W["units"]])
    say(0, "spine", None, None,
        "THE SPINE IS DOWN: %d verses, %d derived blocks. Nothing has "
        "happened yet." % (len(ordered), len(W["units"])), teach="spine")

    # ---- replay ------------------------------------------------------------
    tape = make_tape(W)
    unit_seq = {u["unit"]: i for i, u in enumerate(W["units"], start=1)}
    n_units = len(W["units"])
    facts_n = events_n = 0
    open_now = set()
    mentions_batch = 0
    cur_para_i = 0
    para_start_counts = (0, 0)

    def parashah_banner(i):
        he, tr, gl, _ = PARASHIYOT[i]
        line = "=" * 66
        for out in (line,
                    "PARASHAH %d of 12 — %s (%s, '%s')" % (i + 1, he, tr, gl),
                    line):
            nrows.append((None, None, "parashah", None, None, tr, out))
            if not quiet:
                print(out)

    def parashah_close(i):
        he, tr, gl, _ = PARASHIYOT[i]
        opens = len(open_now)
        summary = ("%s (%s) CLOSES — world so far: %d facts, %d events, "
                   "%d obligations still open."
                   % (he, tr, facts_n, events_n, opens))
        nrows.append((None, None, "summary", None, None, tr, summary))
        if not quiet:
            print()
            print("  " + summary)
        if pause and not quiet:
            try:
                input("  -- press Enter for the next parashah --")
            except EOFError:
                pass

    parashah_banner(0)
    last_unit_banner = None

    for seq, kind, r in tape:
        ref = r.get("ref") or r.get("first_ref")
        # parashah rollover
        if ref:
            while cur_para_i < 11:
                eb, ec, ev = PARASHIYOT[cur_para_i][3]
                b, ch, vs = build_world.parse_ref(ref)
                if (ch, vs) <= (ec, ev):
                    break
                parashah_close(cur_para_i)
                cur_para_i += 1
                parashah_banner(cur_para_i)
        # unit banner
        u = r.get("unit")
        if u and u != last_unit_banner and kind != "unit":
            last_unit_banner = u
            line = "-- block %s (%d of %d) -- %s" % (
                u, unit_seq.get(u, 0), n_units, ref or "")
            nrows.append((None, seq, "block", ref, u, parashah_of(ref), line))
            if not quiet:
                print()
                print("  " + line)

        if kind == "fact":
            facts_n += 1
            c.execute("INSERT INTO facts VALUES (?,?,?,?)",
                      (r["seq"], r["unit"], r["ref"], r["fact"]))
            say(seq, "fact", ref, u, "%s  FACT: %s" %
                (ref, ink.show(ref, r["fact"])), teach="fact")
        elif kind == "event":
            events_n += 1
            c.execute("INSERT INTO events VALUES (?,?,?,?,?)",
                      (r["seq"], r["unit"], r["ref"], r["verb"], r["agent"]))
            for i, t in enumerate(r.get("themes") or []):
                c.execute("INSERT INTO event_themes VALUES (?,?,?)",
                          (r["seq"], i, t))
            agent = ink.show(ref, r["agent"], W, entity=True) if r["agent"] else "(no actor named)"
            th = ", ".join(ink.show(ref, t, W, entity=True)
                           for t in (r.get("themes") or []))
            say(seq, "event", ref, u, "%s  EVENT: %s — %s%s" %
                (ref, agent, r["verb"], (" -> " + th) if th else ""),
                teach="event")
        elif kind == "demand":
            c.execute("INSERT INTO demands VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (r["seq"], r["unit"], r["ref"], r["speaker"], r["mood"],
                       r["demand"], r["status"], r["settled_seq"],
                       r["settled_unit"], r["settled_ref"], r["settle_kind"],
                       r["basis_en"], r["uncertain"]))
            # a demand enters the live open-count only if the record says it
            # stays open, or names the later verse that closes it; 18 rows
            # are marked settled with no clock pointer — never live-open.
            if r["status"] == "OPEN" or r.get("settled_seq"):
                open_now.add(r["seq"])
            spk = ink.show(ref, r["speaker"], W, entity=True) if r["speaker"] else "(unspoken)"
            say(seq, "demand", ref, u, "%s  DEMAND OPENS [%s]: %s — %s   "
                "(open now: %d)" % (ref, r["mood"], spk,
                                    ink.show(ref, r["demand"]),
                                    len(open_now)), teach="demand")
        elif kind == "settle":
            open_now.discard(r["seq"])
            say(seq, "settle", r["settled_ref"], r["settled_unit"],
                "%s  SETTLED: the demand of %s (%s) — %s   (open now: %d)" %
                (r["settled_ref"], r["ref"], ink.show(r["ref"], r["demand"]),
                 r["settle_kind"] or "settled", len(open_now)), teach="settle")
        elif kind == "mention":
            c.execute("INSERT INTO mentions VALUES (?,?,?,?,?,?)",
                      (r["seq"], r["unit"], r["ref"], r["token"], r["role"],
                       r["entity"]))
            mentions_batch += 1   # counted, not narrated: cast bookkeeping
        elif kind == "name":
            c.execute("INSERT INTO names VALUES (?,?,?,?,?)",
                      (r["seq"], r["unit"], r["ref"], r["token"], r["label"]))
            say(seq, "name", ref, u, "%s  NAMED: %s is called %s" %
                (ref, ink.show(ref, r["token"], W, entity=True),
                 ink.show(ref, r["label"])), teach="name")
        elif kind == "standing":
            c.execute("INSERT INTO standing VALUES (?,?,?,?,?)",
                      (r["seq"], r["unit"], r["ref"], r["kind"], r["payload"]))
            say(seq, "standing", ref, u, "%s  WITNESS [%s]: %s" %
                (ref, r["kind"], ink.show(ref, r["payload"])),
                teach="standing")
        elif kind == "test":
            c.execute("INSERT INTO tests VALUES (?,?,?,?,?,?)",
                      (r["seq"], r["unit"], r["ref"], r["verdict"],
                       r["oracle"], r["theme"]))
            say(seq, "test", ref, u, "%s  TEST FIRES: %s — verdict %s (oracle %s)"
                % (ref, ink.show(ref, r["theme"] or ""), r["verdict"],
                   r["oracle"]), teach="test")
        elif kind == "unit":
            c.execute("INSERT INTO checkpoints VALUES (?,?,?,?,?,?)",
                      (r["seq_unit"], r["unit"], r["seq"], r["facts_n"],
                       r["open_n"], r["state_hash"]))
            say(seq, "unit", None, r["unit"],
                "BLOCK CLOSES: %s (%d of %d) — %d facts stand, %d obligations "
                "open." % (r["unit"], r["seq_unit"], n_units, r["facts_n"],
                           r["open_n"]), teach="unit")

    parashah_close(cur_para_i)

    # ---- projections + meta: identical to the one-gulp build ---------------
    tok2ent = {}
    for m in W["mentions"]:
        tok2ent.setdefault((m["unit"], m["token"]), m["entity"])

    def ent_of(unit, token):
        return tok2ent.get((unit, token), token)

    ent = {}
    for m in W["mentions"]:
        e = ent.setdefault(m["entity"], {"first_seq": m["seq"],
                                         "first_ref": m["ref"],
                                         "first_unit": m["unit"], "n": 0,
                                         "agent": 0})
        e["n"] += 1
        if m["seq"] < e["first_seq"]:
            e.update(first_seq=m["seq"], first_ref=m["ref"],
                     first_unit=m["unit"])
        if m["role"] == "agent":
            e["agent"] += 1
    theme_n = {}
    for e in W["events"]:
        for t_ in (e.get("themes") or []):
            k = ent_of(e["unit"], t_)
            theme_n[k] = theme_n.get(k, 0) + 1
    for k in theme_n:
        ent.setdefault(k, {"first_seq": 10**9, "first_ref": None,
                           "first_unit": None, "n": 0, "agent": 0})
    c.executemany("INSERT INTO entities VALUES (?,?,?,?,?,?,?)",
                  [(k, v["first_ref"], v["first_seq"], v["first_unit"],
                    v["n"], v["agent"], theme_n.get(k, 0))
                   for k, v in ent.items()])

    rel = []
    for e in W["events"]:
        o = ord_of.get(e["ref"])
        for t in (e.get("themes") or []):
            rel.append((e["seq"], o, e["ref"], e["unit"],
                        ent_of(e["unit"], e["agent"]), e["verb"],
                        ent_of(e["unit"], t), "event"))
    for n in W["names"]:
        rel.append((n["seq"], ord_of.get(n["ref"]), n["ref"], n["unit"],
                    ent_of(n["unit"], n["token"]), "named", n["label"],
                    "name"))
    for d in W["demands"]:
        rel.append((d["seq"], ord_of.get(d["ref"]), d["ref"], d["unit"],
                    ent_of(d["unit"], d["speaker"]) if d["speaker"] else None,
                    "demands", d["demand"], "demand"))
    c.executemany("INSERT INTO relations VALUES (?,?,?,?,?,?,?,?)", rel)

    by_ent = {}
    for n in W["names"]:
        e = ent_of(n["unit"], n["token"])
        by_ent.setdefault(e, []).append(
            (ord_of.get(n["ref"], 0), n["ref"], n["label"], n["seq"]))
    st = []
    for e, lst in by_ent.items():
        lst.sort()
        for i, (o, ref2, label, seq2) in enumerate(lst):
            nxt = lst[i + 1] if i + 1 < len(lst) else None
            st.append((e, "name", label, o, ref2,
                       nxt[0] if nxt else None, nxt[1] if nxt else None,
                       seq2))
    c.executemany("INSERT INTO entity_state VALUES (?,?,?,?,?,?,?,?)", st)

    open_n = sum(1 for d in W["demands"] if d["status"] == "OPEN")
    meta = {
        "built_from": "run_genesis.py replay of corpus_world.fold(write=False)",
        "repo": str(REPO), "state_hash": state_hash,
        "units": len(W["units"]), "refs": len(ordered),
        "facts": len(W["facts"]), "events": len(W["events"]),
        "demands": len(W["demands"]), "open_demands": open_n,
        "mentions": len(W["mentions"]), "names": len(W["names"]),
        "standing": len(W["standing"]), "tests": len(W["tests"]),
        "entities": len(ent), "relations": len(rel), "entity_state": len(st),
        "ink_hits": ink.hits, "ink_misses": ink.misses,
    }
    c.executemany("INSERT INTO meta VALUES (?,?)",
                  [(k, str(v)) for k, v in meta.items()])
    c.executemany("INSERT INTO narration VALUES (?,?,?,?,?,?,?)", nrows)
    con.commit()

    cov = 100.0 * ink.hits / max(1, ink.hits + ink.misses)
    print()
    print("RUN COMPLETE — %d narration lines saved to the narration table."
          % len(nrows))
    print("Ink coverage: %d of %d displayed tokens tied to their verse's own "
          "written form (%.0f%%); the rest shown in English, never guessed."
          % (ink.hits, ink.hits + ink.misses, cov))
    ok = build_world.reconcile(con, W)
    con.close()
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-pause", action="store_true")
    ap.add_argument("--quiet", action="store_true",
                    help="no terminal narration; still saved to the table")
    a = ap.parse_args()
    ok = run(pause=not a.no_pause, quiet=a.quiet)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
