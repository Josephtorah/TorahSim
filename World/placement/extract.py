#!/usr/bin/env python3
"""PHASE 2 — the extractor.

For one parashah, propose placements: WHO was WHERE, WHEN, and on what evidence.
Emits nothing it cannot cite. Each proposal carries the verb that licensed it,
the preposition that gave it direction, and the verse.

A proposal is a CANDIDATE, not a fact. Phase 3 reads them.

Relations:
  to    arrival / motion toward   (directional ending, or "to/toward" + a place)
  at    rest / dwelling / staying (a POS verb + "in" + a place)
  from  departure                 ("from" + a place)
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import json, sqlite3, sys
from collections import defaultdict

REPO = _ROOT
DB = f"{REPO}/torah_grok.SNAPSHOT-main-51801ca.sqlite"
WORLD = ((_ROOT + '/World') + "/world.sqlite")
GAZ = ((_ROOT + '/World') + "/placement/gazetteer.json")

PARASHOT = {
    "vayetze": ("Gen", (28, 10), (32, 3)),
}

VERB_CAT = {}
for line in open(((_ROOT + '/World') + "/research/VERB_REVIEW.md")):
    p = [x.strip() for x in line.split("|")]
    if len(p) > 5 and p[1].isdigit() and p[4] in ("LOC", "CAUS", "POS", "HOLD"):
        VERB_CAT[p[1]] = (p[4], p[2])

TO_PREP = {"413": "to", "5704": "as far as", "5921": "upon"}
# Direction is very often carried by a common-noun HEAD that governs the name,
# not by the name itself: "land-ward, Canaan" (31:18), "to the mountain of
# Gilead" (31:21), "in the land of Egypt". Requiring the marker on the proper
# noun alone was the extractor's largest recall loss.
HEAD_NOUNS = {"776": "land", "2022": "mountain", "5892": "city", "4725": "place",
              "7704": "field", "4057": "wilderness", "1516": "valley",
              "5158": "wadi", "6160": "plain", "1004": "house"}
AT_PREP = {"b": "in", "9003": "in"}
FROM_PREP = {"m": "from", "4480": "from"}


def base(l):
    return l.split("/")[-1].rstrip("+").split()[0] if l else ""


def pref(l):
    return set(l.split("/")[:-1]) if l and "/" in l else set()


def is_np(m):
    return any(s.startswith("Np") for s in m.lstrip("H").split("/"))


def is_verb(m):
    return any(s.startswith("V") for s in m.lstrip("H").split("/"))


def has_sd(m):
    return "Sd" in m.split("/")


def join_compounds(ws):
    out, i = [], 0
    while i < len(ws):
        w = ws[i]
        if (is_np(w["mor"]) and w["lem"].rstrip("+") != w["lem"]
                and i + 1 < len(ws) and is_np(ws[i + 1]["mor"])
                and base(ws[i + 1]["lem"]) == base(w["lem"])):
            n = ws[i + 1]
            out.append(dict(w, tr=w["tr"] + "-" + n["tr"],
                            gl=n["gl"] if n["gl"] != "?" else w["gl"],
                            mor=(n["mor"] + "/Sd" if has_sd(w["mor"])
                                 and not has_sd(n["mor"]) else n["mor"])))
            i += 2
            continue
        out.append(w)
        i += 1
    return out


def main(name="vayetze"):
    book, (c1, v1), (c2, v2) = PARASHOT[name]
    gaz = json.load(open(GAZ))
    placeish = {k for k, e in gaz.items()
                if e["verdict"] in ("place", "both", "place?")}
    personish = {k for k, e in gaz.items()
                 if e["verdict"] in ("person", "both")}

    w = sqlite3.connect(WORLD)
    ords = {r: (o, u) for r, o, u in w.execute(
        "select ref, ord, unit from refs where book=?", (book,))}
    fold_agents = defaultdict(list)
    for r, e in w.execute("""select ref, entity from mentions
                             where role in ('agent','speaker')"""):
        if e not in fold_agents[r]:
            fold_agents[r].append(e)

    c = sqlite3.connect(DB)
    q = """select v.chapter, v.verse, w.idx, w.translit, w.gloss, w.lemma, w.morph
           from words w join verses v on v.id = w.verse_id
           where v.book=? order by v.id, w.idx"""
    verses = defaultdict(list)
    for ch, vn, idx, tr, gl, lem, mor in c.execute(q, (book,)):
        if (ch, vn) < (c1, v1) or (ch, vn) > (c2, v2):
            continue
        verses[(ch, vn)].append(dict(ch=ch, vn=vn, idx=idx, tr=tr or "",
                                     gl=gl or "", lem=lem or "", mor=mor or ""))

    proposals, novtarget, noverb = [], [], []
    for (ch, vn), raw in sorted(verses.items()):
        ws = join_compounds(raw)
        ref = f"{book}.{ch}.{vn}"
        o, unit = ords.get(ref, (None, None))
        verbs = [x for x in ws if is_verb(x["mor"]) and base(x["lem"]) in VERB_CAT]
        if not verbs:
            noverb.append(ref)
            continue
        # candidate targets: a place-ish proper noun with direction evidence
        targets = []
        for i, x in enumerate(ws):
            if not is_np(x["mor"]):
                continue
            k = base(x["lem"])
            if k not in placeish:
                continue
            p = pref(x["lem"])
            mor = x["mor"]
            # inherit direction from a governing place-head noun
            head = None
            for back in (1, 2):
                j = i - back
                if j < 0:
                    break
                h = ws[j]
                if base(h["lem"]) in HEAD_NOUNS and not is_np(h["mor"]):
                    head = h
                    break
            if head is not None and not (p & (set(TO_PREP) | set(AT_PREP)
                                              | set(FROM_PREP))) \
                    and not has_sd(mor):
                p = p | pref(head["lem"])
                if has_sd(head["mor"]):
                    mor = mor + "/Sd"
            if has_sd(mor):
                rel, why = "to", "directional ending"
            elif p & set(TO_PREP):
                rel, why = "to", "preposition toward"
            elif p & set(AT_PREP):
                rel, why = "at", "preposition in"
            elif p & set(FROM_PREP):
                rel, why = "from", "preposition from"
            else:
                continue
            targets.append((k, gaz[k].get("gloss") or x["gl"], rel, why, x))
        if not targets:
            novtarget.append((ref, [v["gl"] for v in verbs]))
            continue
        # who moves: prefer the fold's own recorded agent for this verse;
        # fall back to the nearest preceding person name in the clause.
        for k, gloss, rel, why, tok in targets:
            subj, subj_ev = None, ""
            agents = fold_agents.get(ref, [])
            if agents:
                subj, subj_ev = agents[0], "the fold's recorded agent at this verse"
            else:
                for j in range(tok["idx"] - 1, -1, -1):
                    cand = next((y for y in ws if y["idx"] == j), None)
                    if cand and is_np(cand["mor"]) and base(cand["lem"]) in personish:
                        subj = gaz[base(cand["lem"])].get("gloss") or cand["gl"]
                        subj_ev = "nearest preceding person name"
                        break
            vb = min(verbs, key=lambda v: abs(v["idx"] - tok["idx"]))
            proposals.append(dict(
                ref=f"{book} {ch}:{vn}", ord=o, unit=unit,
                subject=subj, subject_ev=subj_ev,
                relation=rel, place=gloss, place_key=k,
                place_verdict=gaz[k]["verdict"],
                verb=vb["gl"], verb_cat=VERB_CAT[base(vb["lem"])][0],
                why=why))

    print(f"PARASHAH {name} — {book} {c1}:{v1} to {c2}:{v2}")
    print(f"SCANNED: {len(verses)} verses")
    print(f"  verses with NO location-bearing verb      : {len(noverb)}")
    print(f"  verses with a verb but NO named target    : {len(novtarget)}"
          f"   <- these need reading")
    print(f"  verses yielding proposals                 : "
          f"{len({p['ref'] for p in proposals})}")
    print(f"  PROPOSALS                                 : {len(proposals)}\n")

    print(f"{'ref':<12} {'subject':<12} {'rel':<5} {'place':<14} "
          f"{'cat':<5} {'verb':<18} evidence")
    for p in proposals:
        print(f"{p['ref']:<12} {str(p['subject'])[:11]:<12} {p['relation']:<5} "
              f"{p['place'][:13]:<14} {p['verb_cat']:<5} {p['verb'][:17]:<18} "
              f"{p['why']}")

    print(f"\nVERSES WITH A MOVEMENT VERB BUT NO NAMED PLACE ({len(novtarget)}) "
          f"— the reading queue")
    for ref, vbs in novtarget:
        print(f"  {ref:<12} {', '.join(v[:20] for v in vbs[:4])}")

    json.dump(proposals, open(
        f"{_ROOT}/World/placement/proposals_{name}.json", "w"),
        ensure_ascii=False, indent=1)
    print(f"\nwrote placement/proposals_{name}.json")


main(sys.argv[1] if len(sys.argv) > 1 else "vayetze")
