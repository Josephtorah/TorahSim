#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_unit.py <content_module.py> [--out PATH]

Solo-era unit builder: renders a draft unit YAML from a content module,
pulling every mechanical layer (plain he, translit, accented tree halves,
etnachta ("rest," the mid-verse pause) splits with strongest-disjunctive
fallback, VERIFIED split tags)
from the SNAPSHOT, and merging the module's authored META / DRAFT_NOTE /
STEPS / SCENS.

Content-module contract (plain python file):
  UID  = "gen_54_..."           # unit id == output basename
  BOOK = "Gen"
  SPAN = (31, 22, 31, 54)       # ch_start, v_start, ch_end, v_end
  META = [(key, rendered-value-string), ...]   # id..unit_span_planned
  DRAFT_NOTE = '''...'''
  STEPS = [dict(ref=(ch,vs), op=..., en=..., tl_en=..., tr_en=...,
                ops=[dict(op=..., expr=..., frag=(anchor, n[, occ]), prose=...)],
                comment=...), ...]
  SCENS = [dict(id=..., ref=(ch,vs), frag=(anchor,n), occ=1,
                title=..., given=..., expect=[clause, ...]), ...]
  EXTRA_SUBS = {}               # optional, overrides/extends GLOBAL_SUBS

Built-in checks (all fail loudly):
  - translit cleanup completeness (no ה left in translit output)
  - vowel sanity on every plain he line
  - EXPECT SIMULATOR: replays every step's ops (DECLARE push, RESULT pop,
    NAME/ASSIGN registry writes, REGISTRY_INSTALL world adds) and verifies
    each scenario's queue/registry/world clauses against the simulated
    state — the bookkeeping layer is computed, not trusted.
"""
import importlib.util
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DB = REPO / "source-snapshot.sqlite"
ACCENTS = re.compile("[֑-ֽ֯]")
VOWELS = re.compile("[ְ-ׇ]")
MAQQEF = "־"
BOOK_STEP = {"Gen": "Gn", "Exod": "Ex", "Lev": "Lv", "Num": "Nm", "Deut": "Dt"}


def load_module(path):
    spec = importlib.util.spec_from_file_location("unit_content", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def nfc(s):
    return unicodedata.normalize("NFC", s)


def fetch_span(book, span):
    ch1, v1, ch2, v2 = span
    con = sqlite3.connect(str(DB))
    if ch1 == ch2:
        cond, args = "v.chapter=? AND v.verse BETWEEN ? AND ?", (ch1, v1, v2)
    else:
        cond = ("((v.chapter=? AND v.verse>=?) OR (v.chapter>? AND v.chapter<?) "
                "OR (v.chapter=? AND v.verse<=?))")
        args = (ch1, v1, ch1, ch2, ch2, v2)
    rows = con.execute(
        "SELECT v.chapter, v.verse, w.idx, w.he, w.maqqef_after, w.mark_id, "
        "w.mark_rank, w.translit FROM words w JOIN verses v ON v.id=w.verse_id "
        "WHERE v.book=? AND %s ORDER BY v.chapter, v.verse, w.idx" % cond,
        (book,) + args).fetchall()
    V = {}
    for ch, vs, idx, he, mq, mk, mr, tr in rows:
        V.setdefault((ch, vs), []).append(
            {"idx": idx, "he": he, "mq": mq, "mk": mk, "mr": mr, "tr": tr})
    if not V:
        sys.exit("no tokens for %s %s" % (book, span))
    return V


class Renderer:
    def __init__(self, V, subs):
        self.V, self.subs = V, subs

    def tr_tok(self, t):
        s = self.subs.get(t["tr"], t["tr"])
        if "ה" in s:  # a ה survived cleanup
            sys.exit("UNSUBBED HE-CHAR TRANSLIT: %r — add to SUBS/EXTRA_SUBS" % s)
        return s

    @staticmethod
    def is_ketiv(t):
        return not VOWELS.search(t["he"])

    def join_he(self, toks, plain):
        out = ""
        for i, t in enumerate(toks):
            h = t["he"].replace("/", "")
            if plain:
                h = ACCENTS.sub("", h)
            out += h
            if i < len(toks) - 1:
                out += MAQQEF if (plain and t["mq"]) else " "
        return nfc(out)

    def join_tr(self, toks):
        parts, buf = [], ""
        for t in toks:
            if self.is_ketiv(t):
                continue  # written-form token: he lines only (gen_43 25:23)
            w = self.tr_tok(t)
            if buf:
                parts.append(buf + "-" + w); buf = ""
            elif t["mq"]:
                buf = w
            else:
                parts.append(w)
        if buf:
            parts.append(buf)
        return " ".join(parts)

    def frag(self, ref, anchor, n, occ=1):
        toks, seen = self.V[ref], 0
        for i, t in enumerate(toks):
            if t["tr"] == anchor or self.subs.get(t["tr"], t["tr"]) == anchor:
                seen += 1
                if seen < occ:
                    continue
                if i + n > len(toks):
                    sys.exit("frag overrun %s %r" % (ref, anchor))
                return toks[i:i + n]
        sys.exit("frag anchor not found %s %r" % (ref, anchor))

    def split(self, ref):
        """(L, R, idx, mark). Etnachta, else earliest strongest disjunctive
        before the final word (gen_03 1:13 / gen_50 29:22 precedent)."""
        toks = self.V[ref]
        et = [t for t in toks if t["mk"] == "etnachta"]
        if et:
            e, label = et[0]["idx"], "etnachta"
        else:
            r, e, label = min((t["mr"], t["idx"], t["mk"]) for t in toks[:-1]
                              if t["mr"] and t["mr"] < 9)
        return ([t for t in toks if t["idx"] <= e],
                [t for t in toks if t["idx"] > e], e, label)


def yq(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


# ---------------------------------------------------------------------------
# Expect simulator — computes queue/registry/world state per step and checks
# every scenario clause the interpreter would check, before preflight.
# ---------------------------------------------------------------------------

def simulate_and_check(mod):
    bk = BOOK_STEP[mod.BOOK]
    queue, writes, world = [], 0, {}       # world: entity -> step ref str
    facts = []                              # law register: case/handler/statute/pattern
    state_after = {}                        # "STEP_<Bk>_ch_vs" -> snapshot
    errors = []
    for st in mod.STEPS:
        ch, vs = st["ref"]
        ref = "STEP_%s_%d_%d" % (bk, ch, vs)
        for op in st["ops"]:
            kind, expr = op["op"], op["expr"]
            if kind == "DECLARE":
                m = re.search(r"(?:LET\??(?:-NOT)?|CMD-US\??)\((.+)\)\)", expr)
                if not m:
                    errors.append("%s: DECLARE payload unparsed: %s" % (ref, expr))
                else:
                    queue.append(m.group(1).strip())
            elif kind == "RESULT":
                m = re.search(r"HOLDS\((.+?),\s*t\d+\)", expr)
                if not m:
                    errors.append("%s: RESULT without HOLDS(q, tN): %s" % (ref, expr))
                else:
                    q = m.group(1).strip()
                    if q in queue:
                        queue.remove(q)
                    else:
                        errors.append("%s: RESULT pops %r but queue=%s" % (ref, q, queue))
            elif kind in ("NAME", "ASSIGN"):
                pairs = re.findall(r"name\(([\w-]+)\)\s*:=\s*(\w+)", expr) or \
                        re.findall(r"([\w-]+)->([\w-]+)", expr)
                if not pairs:
                    errors.append("%s: %s without pairs: %s" % (ref, kind, expr))
                for ent, _label in pairs:
                    writes += 1
                    if ent not in world:
                        errors.append("%s: %s on %r before any install "
                                      "(flag named_before_any_presence would fire — "
                                      "install first or note the flag)" % (ref, kind, ent))
            elif kind == "REGISTRY_INSTALL":
                m = re.search(r"WORLD \+= \{([^}]*)\}", expr)
                if not m:
                    errors.append("%s: REGISTRY_INSTALL without WORLD += {..}: %s" % (ref, expr))
                else:
                    for name in [x.strip() for x in m.group(1).split(",") if x.strip()]:
                        world[name] = ref
            elif kind == "TEST":
                errors.append("%s: TEST op present — simulator assumes TESTS 0; "
                              "extend simulate_and_check before using TEST" % ref)
            elif kind == "CASE":
                m = re.search(r"CASE\((.+)\)\s*ROUTE\(([\w-]+)\)", expr)
                if not m:
                    errors.append("%s: CASE without 'CASE(..) ROUTE(..)': %s" % (ref, expr))
                else:
                    facts.append("case: %s -> %s" % (m.group(1).strip(), m.group(2)))
            elif kind == "HANDLER":
                m = re.search(r"HANDLER IF\((.+)\) THEN\((.+)\)", expr)
                if not m:
                    errors.append("%s: HANDLER without 'HANDLER IF(..) THEN(..)': %s" % (ref, expr))
                else:
                    facts.append("handler: IF(%s) THEN(%s)"
                                 % (m.group(1).strip(), m.group(2).strip()))
            elif kind == "STATUTE":
                m = re.search(r"STATUTE (FORBID|BIND)\((.+)\)", expr)
                if not m:
                    errors.append("%s: STATUTE without 'STATUTE FORBID(..)/BIND(..)': %s" % (ref, expr))
                else:
                    facts.append("statute: %s(%s)" % (m.group(1), m.group(2).strip()))
            elif kind == "PATTERN":
                m = re.search(r"PATTERN\((.+)\)", expr)
                if not m:
                    errors.append("%s: PATTERN without 'PATTERN(p)': %s" % (ref, expr))
                else:
                    facts.append("pattern: %s" % m.group(1).strip())
        state_after[ref] = {"queue": list(queue), "writes": writes,
                            "world": dict(world), "facts": list(facts)}

    for sc in mod.SCENS:
        m = re.search(r"STEP_%s_(\d+)_(\d+)" % bk, sc["title"])
        if not m or (int(m.group(1)), int(m.group(2))) != tuple(sc["ref"]):
            errors.append("%s: title lacks matching 'after STEP_%s_%d_%d' anchor"
                          % (sc["id"], bk, sc["ref"][0], sc["ref"][1]))
            continue
        stref = "STEP_%s_%d_%d" % ((bk,) + tuple(sc["ref"]))
        snap = state_after.get(stref)
        if snap is None:
            errors.append("%s: no step %s" % (sc["id"], stref)); continue
        for cl in sc["expect"]:
            c = cl.strip().rstrip(".").rstrip(";")
            mt = re.search(r"(?:LET|LET\?|LET-NOT|CMD-US\??)\((.+?)\) pushed and OPEN", c)
            if mt:
                if mt.group(1) not in snap["queue"]:
                    errors.append("%s: expects %r OPEN but simulated queue=%s"
                                  % (sc["id"], mt.group(1), snap["queue"]))
                continue
            if c == "SPECS empty":
                if snap["queue"]:
                    errors.append("%s: expects SPECS empty but queue=%s"
                                  % (sc["id"], snap["queue"]))
                continue
            if c == "no test, no name":
                if snap["writes"]:
                    errors.append("%s: 'no test, no name' but writes=%d"
                                  % (sc["id"], snap["writes"]))
                continue
            mt = re.search(r"REGISTRY (\d+) writes", c)
            if mt:
                if snap["writes"] != int(mt.group(1)):
                    errors.append("%s: expects REGISTRY %s writes, simulated %d"
                                  % (sc["id"], mt.group(1), snap["writes"]))
                continue
            mt = re.search(r"WORLD \+= (\w+)", c)
            if mt:
                if snap["world"].get(mt.group(1)) != stref:
                    errors.append("%s: expects WORLD += %s installed AT %s, got %s"
                                  % (sc["id"], mt.group(1), stref,
                                     snap["world"].get(mt.group(1))))
                continue
            mt = re.match(r"Facts (.+?) HOLD", c)
            if mt:
                for token in [t.strip() for t in mt.group(1).split("/")]:
                    parts = token.split("-")
                    if not any(all(p in f for p in parts) for f in snap["facts"]):
                        errors.append("%s: expects fact %r but simulated facts=%s"
                                      % (sc["id"], token, snap["facts"][-3:]))
                continue
            mt = re.search(r"STATUTES (\d+) standing", c)
            if mt:
                n = sum(1 for f in snap["facts"] if f.startswith("statute:"))
                if n != int(mt.group(1)):
                    errors.append("%s: expects STATUTES %s standing, simulated %d"
                                  % (sc["id"], mt.group(1), n))
                continue
            errors.append("%s: clause not simulatable (would be UNCHECKED "
                          "in run_unit.py too?): %r" % (sc["id"], c))
    return errors, state_after


# ---------------------------------------------------------------------------

def build(mod, out_path):
    from subs import GLOBAL_SUBS
    subs = dict(GLOBAL_SUBS)
    subs.update(getattr(mod, "EXTRA_SUBS", {}))
    V = fetch_span(mod.BOOK, mod.SPAN)
    R = Renderer(V, subs)

    errors, _ = simulate_and_check(mod)
    if errors:
        for e in errors:
            print("EXPECT-SIM FAIL:", e)
        sys.exit(1)
    print("expect simulator: %d steps, %d scenarios — all clauses match "
          "simulated state" % (len(mod.STEPS), len(mod.SCENS)))

    out = []
    w = out.append
    w("meta:")
    for k, v in mod.META:
        w("  %s: %s" % (k, v))
    w("  data_paths_he:")
    w("  - Data/%s.xml" % mod.BOOK)
    w("  status: draft")
    w("  dry_run_only: true")
    w("  draft_note_en: >")
    for line in mod.DRAFT_NOTE.strip("\n").split("\n"):
        w("    " + line if line else "")
    w("")
    w("scenarios:")
    for sc in mod.SCENS:
        toks = R.frag(tuple(sc["ref"]), sc["frag"][0], sc["frag"][1],
                      sc.get("occ", 1))
        w("- id: %s" % sc["id"])
        w("  title_en: %s" % yq(sc["title"]))
        w("  given_en: %s" % yq(sc["given"]))
        w("  expect_en: |")
        for ln in sc["expect"]:
            w("    " + ln)
        w("  value_he: %s" % R.join_he(toks, plain=False).replace(MAQQEF, " "))
        w("  value_he_translit: %s" % R.join_tr(toks))
        w("")
    w("boot_steps:")
    bk = BOOK_STEP[mod.BOOK]
    for order, st in enumerate(mod.STEPS, 1):
        ch, vs = st["ref"]
        toks = V[(ch, vs)]
        L, Rt, e, mklabel = R.split((ch, vs))
        w("- id: STEP_%s_%d_%d" % (bk, ch, vs))
        w("  order: %d" % order)
        w("  ref: %s.%d.%d" % (mod.BOOK, ch, vs))
        w("  op: %s" % st["op"])
        w("  he: %s" % R.join_he(toks, plain=True))
        w("  he_translit: %s" % R.join_tr(toks))
        w("  en: %s" % yq("[EN-AID] " + st["en"]))
        w("  tree_left:")
        w("    he: %s" % R.join_he(L, plain=False))
        w("    he_translit: %s" % R.join_tr(L))
        last = R.tr_tok(L[-1]).split("-")[-1]
        if mklabel == "etnachta":
            tag = ("%s (etnachta on %s) [VERIFIED: SNAPSHOT %s.%d.%d idx%d "
                   "mark_id=etnachta]" % (st["tl_en"], last, mod.BOOK, ch, vs, e))
        else:
            tag = ("%s (NO etnachta in verse: split at %s on %s) [VERIFIED: "
                   "SNAPSHOT %s.%d.%d idx%d mark_id=%s rank=2; no etnachta "
                   "token]" % (st["tl_en"], mklabel, last, mod.BOOK, ch, vs, e, mklabel))
        w("    en: %s" % yq(tag))
        w("  tree_right:")
        w("    he: %s" % R.join_he(Rt, plain=False))
        w("    he_translit: %s" % R.join_tr(Rt))
        w("    en: %s" % yq("%s (verse-final %s) [VERIFIED: SNAPSHOT %s.%d.%d "
                            "idx%d-%d]" % (st["tr_en"],
                                           R.tr_tok(Rt[-1]).split("-")[-1],
                                           mod.BOOK, ch, vs, e + 1, len(toks) - 1)))
        w("  operators:")
        for op in st["ops"]:
            f = op["frag"]
            ftoks = R.frag((ch, vs), f[0], f[1], f[2] if len(f) > 2 else 1)
            w("  - op: %s" % op["op"])
            w("    expr_en: %s" % op["expr"])
            w("    he: %s" % R.join_he(ftoks, plain=True))
            w("    he_translit: %s" % R.join_tr(ftoks))
            w("    en: >")
            for ln in op["prose"].strip("\n").split("\n"):
                w("      " + ln if ln else "")
            w("    cites: []")
            w("    confidence: tested")
        w("  comment: >")
        w("    " + st["comment"])
        w("  confidence: tested")
        w('  source: "[HE-WRITTEN][HE-STRUCT]"')
        w("")

    text = "\n".join(out).rstrip() + "\n"
    for ln in text.split("\n"):
        if ln.startswith("  he: ") and not VOWELS.search(ln):
            sys.exit("VOWELLESS he LINE: %r" % ln)
    Path(out_path).write_text(text)
    print("WROTE %s (%d lines); vowel sanity OK" % (out_path, len(out)))


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    mod_path = Path(args[0]).resolve()
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    mod = load_module(mod_path)
    out = (REPO / "logic/units" / (mod.UID + ".yaml"))
    if "--out" in args:
        out = Path(args[args.index("--out") + 1])
    build(mod, out)


if __name__ == "__main__":
    main()
