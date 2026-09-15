#!/usr/bin/env python3
"""PHASE 1 — the gazetteer.

Split Genesis's proper nouns into PERSONS and PLACES from evidence, never by
hand. Every verdict carries the evidence that produced it.

WHAT THE FIRST DRAFT GOT WRONG, kept here because it is the lesson:
it treated "governed by a locative preposition" as a PLACE signal. But
"to Jacob" and "to Bethel" take the same preposition, so that signal fired on
every major character in the book and reported Jacob, Joseph, Abraham and
Pharaoh as places. Morphology cannot tell those two apart. What CAN:

  PERSONS ACT. PLACES DO NOT.

So persons are identified by positive evidence (they speak, they are the
subject of a verb, they stand in a kinship phrase, the fold records them
acting), and a name with locative evidence and NO person evidence is a
probable place. The signals are graded, and the grade is reported.

  STRONG place : Sd  the directional ending ("Haran-ward") — only places take it
                 CON "land of X" / "city of X" / "wilderness of X"
  STRONG person: SUBJ a finite verb immediately followed by the name
                 KIN  "son of X" / "X son of" / begetting
                 SAY  subject of a speech verb
                 ENT  the fold records the name acting (matched on translit)
  WEAK   place : PREP governed by a locative preposition, with no person
                 evidence anywhere in the book

Compound names (Beth-el, Beer-sheba) are joined mechanically: the corpus marks
the first half with a '+' on its Strong's number and gives both halves the same
number. No hand list.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import json, sqlite3
from collections import defaultdict

REPO = _ROOT
DB = f"{REPO}/torah_grok.SNAPSHOT-main-51801ca.sqlite"
WORLD = "<world-link>/world.sqlite"
OUT = "<world-link>/placement/gazetteer.json"

LOC_PREP = {"b", "9003", "m", "4480", "413", "5921", "5704"}
# Only heads whose complement is ALWAYS a toponym. Deliberately EXCLUDED:
# "house of X", "field of X", "mountain of X", "place of X", "God of X" — all
# take a PERSON as possessor ("the field of Ephron" is Ephron's field, not a
# town called Ephron), and including them reported Jacob, Joseph and the divine
# Name as places.
PLACE_HEADS = {"5892": "city", "1516": "valley", "6160": "plain",
               "8179": "gate", "4057": "wilderness", "5158": "wadi"}
# "land of X" is DEMOTED to weak: it is the toponymic phrase in "land of Canaan"
# but plain possession in "land of Pharaoh" (47:20), which is what made the
# divine Name and Pharaoh register as places. The genuine eponyms (Egypt,
# Canaan, Edom, Seir, Cush) keep their place status from the directional ending
# and from city/wilderness constructs.
WEAK_HEADS = {"776": "land"}
KIN = {"1121": "son", "1323": "daughter", "3205": "beget", "251": "brother",
       "1": "father", "517": "mother", "802": "wife", "269": "sister"}
SAY = {"559", "1696", "7121", "6030", "6680"}


def base(l):
    if not l:
        return ""
    return l.split("/")[-1].rstrip("+").split()[0]


def pref(l):
    return set(l.split("/")[:-1]) if l and "/" in l else set()


def is_np(m):
    return any(s.startswith("Np") for s in m.lstrip("H").split("/"))


def is_verb(m):
    return any(s.startswith("V") for s in m.lstrip("H").split("/"))


def load():
    c = sqlite3.connect(DB)
    q = """select v.osis_id, v.chapter, v.verse, w.idx, w.he_plain, w.translit,
                  w.gloss, w.lemma, w.morph
           from words w join verses v on v.id = w.verse_id
           where v.book='Gen' order by v.id, w.idx"""
    vs = defaultdict(list)
    for osis, ch, vn, idx, pl, tr, gl, lem, mor in c.execute(q):
        vs[(ch, vn)].append(dict(ch=ch, vn=vn, idx=idx, pl=pl or "", tr=tr or "",
                                 gl=gl or "", lem=lem or "", mor=mor or ""))
    return vs


def join_compounds(ws):
    """The corpus marks a compound's first half with '+' on the Strong's number
    and gives both halves the same number. Join them into one token."""
    out, i = [], 0
    while i < len(ws):
        w = ws[i]
        if (is_np(w["mor"]) and w["lem"].rstrip("+") != w["lem"]
                and i + 1 < len(ws) and is_np(ws[i + 1]["mor"])
                and base(ws[i + 1]["lem"]) == base(w["lem"])):
            nxt = ws[i + 1]
            out.append(dict(w, pl=w["pl"] + "-" + nxt["pl"],
                            tr=w["tr"] + "-" + nxt["tr"],
                            gl=nxt["gl"] if nxt["gl"] != "?" else w["gl"],
                            mor=(nxt["mor"] + "/Sd"
                                 if "Sd" in w["mor"].split("/")
                                 and "Sd" not in nxt["mor"].split("/")
                                 else nxt["mor"]), compound=True))
            i += 2
            continue
        out.append(dict(w, compound=False))
        i += 1
    return out


def fold_actors():
    c = sqlite3.connect(WORLD)
    return {e for (e,) in c.execute(
        """select distinct entity from mentions
           where role in ('agent','speaker','blesser','blessee','assigned')""")}


# Genesis MAKES toponyms by naming them, and the fold already recorded every
# naming it derived. A naming whose subject is a place-word ("the place", "the
# well", "the heap", "the altar") produces a PLACE — read from the corpus's own
# names table rather than pattern-matched out of the text.
PLACE_TOKENS = ("maqom", "beer", "gal", "har", "nahar", "alon", "mizbeach",
                "ir", "sadeh", "emeq", "machaneh")


def fold_place_namings():
    """-> {label: (ref, token)} for namings that produced a place name."""
    c = sqlite3.connect(WORLD)
    out = {}
    for ref, token, label in c.execute("select ref, token, label from names"):
        t = (token or "").lower()
        if any(t == p or t.startswith(p + "_") or t.startswith("ha_" + p)
               or ("_" + p) in t for p in PLACE_TOKENS):
            out[(label or "").lower()] = (ref, token)
    return out


def build():
    verses, actors, namings = load(), fold_actors(), fold_place_namings()
    g = defaultdict(lambda: dict(place=[], person=[], tokens=0, refs=[],
                                 gloss="", translit=""))
    for (ch, vn), raw in sorted(verses.items()):
        ws = join_compounds(raw)
        for i, w in enumerate(ws):
            if not is_np(w["mor"]):
                continue
            # The lemma is the canonical identity. Keying on the transliteration
            # made "and-Lot", "to-Pharaoh" and "from-Beer-sheba" separate names
            # from Lot, Pharaoh and Beer-sheba — 629 names where there are ~400.
            key = base(w["lem"])
            if not key:
                continue
            e = g[key]
            e["tokens"] += 1
            cleaned = w["gl"].split("-suffix")[0]
            if "-" in cleaned and not w.get("compound"):
                cleaned = cleaned.split("-")[-1]      # strip and-/to-/from-
            if cleaned and cleaned != "?" and not e["gloss"]:
                e["gloss"] = cleaned
            if not e["translit"] or len(w["tr"]) < len(e["translit"]):
                e["translit"] = w["tr"]
            ref = f"Gen {ch}:{vn}"
            if len(e["refs"]) < 40:
                e["refs"].append(ref)
            prv = ws[i - 1] if i else None
            nxt = ws[i + 1] if i + 1 < len(ws) else None
            # ---- STRONG place
            if "Sd" in w["mor"].split("/"):
                e["place"].append(["Sd", ref, "directional ending"])
            if prv and base(prv["lem"]) in PLACE_HEADS:
                e["place"].append(["CON", ref,
                                   PLACE_HEADS[base(prv["lem"])] + " of —"])
            elif prv and base(prv["lem"]) in WEAK_HEADS:
                e["place"].append(["LAND", ref, "land of — (weak: also possession)"])
            # ---- STRONG person
            # A SUBJECT never carries a locative or dative prefix. Without this
            # guard, "he came to-Sodom" (preposition prefixed to the name, so
            # the verb sits immediately before it) reads as "Sodom came", and
            # Sodom, Gerar, Zoar and Timnah all register as people.
            # The directional ending is a SUFFIX, so a prefix test misses it:
            # "Timnah-ward he went up" put the verb immediately before the name
            # and Timnah, Sodom, Gerar, Zoar and Asshur all read as subjects.
            fronted = (bool(pref(w["lem"]) & (LOC_PREP | {"l", "9005"}))
                       or "Sd" in w["mor"].split("/"))
            if prv and is_verb(prv["mor"]) and not fronted:
                if base(prv["lem"]) in SAY:
                    e["person"].append(["SAY", ref, "subject of a speech verb"])
                else:
                    e["person"].append(["SUBJ", ref,
                                        "subject of the verb " + prv["gl"]])
            if prv and base(prv["lem"]) in KIN:
                e["person"].append(["KIN", ref, KIN[base(prv["lem"])] + " —"])
            if nxt and base(nxt["lem"]) in KIN:
                e["person"].append(["KIN", ref, "— " + KIN[base(nxt["lem"])]])
            # ---- WEAK place
            if pref(w["lem"]) & LOC_PREP:
                e["place"].append(["PREP", ref, "locative preposition"])
    # the fold's own place-namings
    for key, e in g.items():
        for form in {(e["translit"] or "").lower().replace("-", "_"),
                     (e["gloss"] or "").lower().replace("-", "_")}:
            if form and form in namings:
                ref, token = namings[form]
                e["place"].append(["NAMED", ref.replace(".", " ", 1).replace(".", ":"),
                                   f"the fold records '{token}' being named this"])
                break
    for key, e in g.items():
        stem = (e["gloss"] or "").lower().replace("-", "_")
        if stem and (stem in actors or stem.replace("_", "") in actors):
            e["person"].append(["ENT", "world.mentions",
                                "the fold records this name acting"])
    return g


def verdict(e):
    pk = {k for k, _, _ in e["place"]}
    qk = {k for k, _, _ in e["person"]}
    # "land of X" is possession when occasional ("land of Pharaoh", once) and
    # toponymic when it is the name's normal use ("land of Canaan", repeatedly).
    # Three or more occurrences promotes it; below that it stays weak.
    nland = sum(1 for k, _, _ in e["place"] if k == "LAND")
    strong_p = bool(pk & {"Sd", "CON", "NAMED"}) or nland >= 3
    strong_q = bool(qk)
    if strong_p and strong_q:
        return "both"
    if strong_p:
        return "place"
    if strong_q:
        return "person"
    if pk & {"PREP", "LAND"}:
        return "place?"
    return "unknown"


def main():
    g = build()
    print(f"SCANNED: 1533 Genesis verses, {sum(e['tokens'] for e in g.values())} "
          f"proper-noun tokens after compound joining, {len(g)} distinct names")
    print(f"         {len(fold_actors())} acting entities in the fold available "
          f"to match against\n")
    buckets = defaultdict(list)
    for k, e in g.items():
        buckets[verdict(e)].append((e["tokens"], k, e))
    print("GAZETTEER VERDICTS")
    for v in ("place", "person", "both", "place?", "unknown"):
        print(f"  {v:>7}: {len(buckets[v]):>3} names, "
              f"{sum(t for t, _, _ in buckets[v]):>4} tokens")
    nent = sum(1 for e in g.values() if any(k == "ENT" for k, _, _ in e["person"]))
    print(f"\n  ENT signal fired on {nent} names "
          f"({'OK' if nent else 'ZERO — the match is broken, do not trust it'})")

    print("\nPLACES — strong evidence only (top 30)")
    for t, k, e in sorted(buckets["place"], reverse=True)[:30]:
        kinds = "+".join(sorted({x for x, _, _ in e["place"] if x != "PREP"}))
        print(f"  {(e['gloss'] or k):<20} {k:<16} {t:>3}  [{kinds}]")
    print("\nBOTH — strong evidence on BOTH sides (these need reading)")
    for t, k, e in sorted(buckets["both"], reverse=True)[:20]:
        pk = "+".join(sorted({x for x, _, _ in e["place"] if x != "PREP"}))
        qk = "+".join(sorted({x for x, _, _ in e["person"]}))
        print(f"  {(e['gloss'] or k):<20} {k:<16} {t:>3}  place[{pk}] person[{qk}]")
    print("\nPROBABLE PLACES — locative preposition, no person evidence (top 20)")
    for t, k, e in sorted(buckets["place?"], reverse=True)[:20]:
        print(f"  {(e['gloss'] or k):<20} {k:<16} {t:>3}  {e['refs'][0]}")

    out = {k: dict(verdict=verdict(e), gloss=e["gloss"], translit=e["translit"],
                   tokens=e["tokens"], refs=e["refs"][:12],
                   place=e["place"][:8], person=e["person"][:8])
           for k, e in g.items()}
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"\nwrote {OUT} — {len(out)} names")


main()
