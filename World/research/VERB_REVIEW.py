#!/usr/bin/env python3
"""VERB_REVIEW.py — classify ALL Genesis verb lemmas for location-bearing.

Writes VERB_REVIEW.md: every one of the verb lemmas in Genesis, with its
gloss, its verse count, and a category. The ENUMERATION is measured from the
morphology; the CLASSIFICATION is a judgement and is recorded as such so it
can be argued with rather than trusted.

    LOC   self-locomotion            go, come, return, ascend, flee, cross
    CAUS  caused motion              send, take, bring, carry, drive out
    POS   position / rest / staying  dwell, encamp, lodge, stand, lie, bury
    HOLD  tenure of a place          possess, acquire, sell, buy
    -     not location-bearing
"""
import sqlite3, collections, pathlib

DB = "<repo-old>/torah_grok.SNAPSHOT-main-51801ca.sqlite"
OUT = pathlib.Path(__file__).resolve().parent / "VERB_REVIEW.md"

CLASS = {
    # --- LOC: the body moves itself -------------------------------------
    "935": "LOC", "3212": "LOC", "1980": "LOC", "3318": "LOC", "5927": "LOC",
    "3381": "LOC", "7725": "LOC", "5265": "LOC", "1481": "LOC", "1272": "LOC",
    "5674": "LOC", "5066": "LOC", "6965": "LOC", "7323": "LOC", "5493": "LOC",
    "7125": "LOC", "7291": "LOC", "5127": "LOC", "5437": "LOC", "6437": "LOC",
    "5503": "LOC", "7270": "LOC", "225": "LOC", "7392": "LOC", "6805": "LOC",
    "7300": "LOC", "1875": "LOC", "5381": "LOC", "7136": "LOC", "7122": "LOC",
    "6293": "LOC", "1692": "LOC", "6298": "LOC", "2015": "LOC", "7925": "LOC",
    "3363": "LOC", "6275": "LOC", "1540": "LOC",
    # --- CAUS: something is moved by an agent ---------------------------
    "7971": "CAUS", "3947": "CAUS", "5375": "CAUS", "1644": "CAUS",
    "5090": "CAUS", "5148": "CAUS", "7617": "CAUS", "7126": "CAUS",
    "7993": "CAUS", "6006": "CAUS", "2943": "CAUS", "5445": "CAUS",
    "4900": "CAUS", "5337": "CAUS", "3051": "CAUS", "7311": "CAUS",
    # --- POS: where something is, or stays ------------------------------
    "3427": "POS", "7931": "POS", "2583": "POS", "3885": "POS", "167": "POS",
    "5975": "POS", "7901": "POS", "6912": "POS", "5324": "POS", "7257": "POS",
    "2082": "POS", "5117": "POS", "5414": "POS", "7760": "POS", "7896": "POS",
    "3240": "POS", "3322": "POS", "3455": "POS", "5800": "POS", "3498": "POS",
    "7604": "POS", "5462": "POS", "6113": "POS", "3680": "POS",
    # --- HOLD: tenure of a place ----------------------------------------
    "3423": "HOLD", "7069": "HOLD", "4376": "HOLD", "7666": "HOLD",
    "1350": "HOLD",
}

NOTE = {
    "3212": "the miss that mattered — a SECOND go-verb beside 1980",
    "225": "a second come-verb beside 935",
    "3947": "not locomotion, but 'took him down to Egypt' places a person",
    "5414": "give/set — placement, not motion",
    "6912": "burial is final placement; the Machpelah material sits here",
    "5674": "crossing — the Jabbok, the Euphrates, borders",
    "7925": "rise early — idiomatic start of a journey, almost always with travel",
    "1540": "uncover / go into exile — the same root does both",
    "3423": "possess the land: tenure, not arrival",
    "5800": "leave/forsake — departure recorded as absence",
    "7666": "buy grain — the verb that sends the brothers to Egypt",
}


def is_verb(m):
    if not m:
        return False
    m = m[1:] if m.startswith("H") else m
    return any(s.startswith("V") for s in m.split("/"))


def base(l):
    return (l or "").split("/")[-1].split(" ")[0]


def main():
    db = sqlite3.connect(DB)
    cur = db.cursor()
    cur.execute("SELECT w.lemma,w.morph,w.gloss,v.id FROM words w "
                "JOIN verses v ON w.verse_id=v.id WHERE v.book='Gen'")
    V, G = collections.defaultdict(set), collections.defaultdict(collections.Counter)
    for lemma, morph, gloss, vid in cur.fetchall():
        if not is_verb(morph):
            continue
        b = base(lemma)
        V[b].add(vid)
        if gloss:
            G[b][gloss.lower().replace("and-", "").strip()] += 1

    # PROBE — the segmenter must find the known go-down at Gen 46:3
    assert "3381" in V, "REFUSING TO WRITE: probe lemma absent"

    rows = sorted(V.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    cats = collections.defaultdict(set)
    for b, vs in rows:
        cats[CLASS.get(b, "-")] |= vs
    total = 1533
    keep = cats["LOC"] | cats["CAUS"] | cats["POS"] | cats["HOLD"]

    L = []
    L.append("# Genesis verbs — complete review for location-bearing\n")
    L.append("Every verb lemma in Genesis, enumerated from the morphology "
             "(not chosen by hand), with a category.\n")
    L.append("The **enumeration is measured**. The **classification is a "
             "judgement** — recorded here so it can be argued with rather "
             "than trusted.\n")
    L.append("| category | meaning | verses |")
    L.append("|---|---|---|")
    for k, d in (("LOC", "self-locomotion"), ("CAUS", "caused motion"),
                 ("POS", "position / rest / staying"), ("HOLD", "tenure of a place")):
        L.append("| %s | %s | %d |" % (k, d, len(cats[k])))
    L.append("| **any** | **location-bearing** | **%d of %d (%.0f%%)** |"
             % (len(keep), total, 100 * len(keep) / total))
    L.append("\n**%d distinct verb lemmas** reviewed; **%d classified as "
             "location-bearing**, %d as not.\n"
             % (len(rows), sum(1 for b, _ in rows if CLASS.get(b, "-") != "-"),
                sum(1 for b, _ in rows if CLASS.get(b, "-") == "-")))

    L.append("\n## Classified as location-bearing\n")
    L.append("| Strong | gloss | verses | cat | note |")
    L.append("|---|---|---|---|---|")
    for b, vs in rows:
        c = CLASS.get(b, "-")
        if c == "-":
            continue
        g = G[b].most_common(1)[0][0] if G[b] else "?"
        L.append("| %s | %s | %d | %s | %s |" % (b, g, len(vs), c, NOTE.get(b, "")))

    L.append("\n## Reviewed and NOT classified as location-bearing\n")
    L.append("Recorded in full so the negative is auditable.\n")
    line = []
    for b, vs in rows:
        if CLASS.get(b, "-") != "-":
            continue
        g = G[b].most_common(1)[0][0] if G[b] else "?"
        line.append("`%s` %s (%d)" % (b, g, len(vs)))
    L.append(" · ".join(line))
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")

    print("wrote %s" % OUT)
    print("  %d verb lemmas reviewed" % len(rows))
    for k in ("LOC", "CAUS", "POS", "HOLD"):
        print("  %-5s %4d verses" % (k, len(cats[k])))
    print("  ANY   %4d verses of %d  (%.0f%%)" % (len(keep), total, 100 * len(keep) / total))


if __name__ == "__main__":
    main()
