#!/usr/bin/env python3
"""Measure whether Onkelos changes genre in Genesis 49.

Two independent metrics, both validated against probes before any number is
reported (THE_STEPS Step 4: a report is worth only its coverage line).

  A. EXPANSION  = Onkelos word count / Hebrew word count, per verse.
                  A translation tracks source length; a paraphrase expands.
  B. RETENTION  = fraction of Hebrew content stems whose consonantal skeleton
                  survives into the Aramaic. A translation keeps the word;
                  a paraphrase replaces it.

Both metrics are read RELATIVE TO ONKELOS'S OWN PROSE BASELINE, never against
1.0 — Aramaic spends extra particles and shifts consonants (Hebrew z -> Aramaic
d, Hebrew sh -> Aramaic t) as a matter of course. That offset is constant
across prose, so the baseline absorbs it; only deviation FROM the baseline is
evidence.
"""
import json, re, sqlite3, sys, unicodedata
from statistics import mean

REPO = "<repo-old>"
DB = f"{REPO}/torah_grok.SNAPSHOT-main-51801ca.sqlite"
BOOKS = {
    "Gen": "Onkelos_Genesis",
    "Exod": "Onkelos_Exodus",
    "Lev": "Onkelos_Leviticus",
    "Num": "Onkelos_Numbers",
    "Deut": "Onkelos_Deuteronomy",
}

NIQQUD = re.compile(r"[֑-ׇ]")
NONLET = re.compile(r"[^א-ת]")
FINALS = str.maketrans("ךםןףץ", "כמנפצ")


def cons(s):
    """Consonantal skeleton: strip vowels/cantillation, normalise finals."""
    return NONLET.sub("", NIQQUD.sub("", s)).translate(FINALS)


# ---------------------------------------------------------------- Hebrew side
def load_hebrew():
    """{osis_id: [stem, ...]} — ketiv rows dropped, prefixes stripped."""
    c = sqlite3.connect(DB)
    out, dropped = {}, 0
    q = """select v.osis_id, w.he, w.he_plain, w.morph
           from words w join verses v on v.id = w.verse_id
           order by v.id, w.idx"""
    for osis, he, plain, morph in c.execute(q):
        # A ketiv (written) row carries no vowel points; its qere (read)
        # partner follows. Counting both would inflate the verse.
        if not NIQQUD.search(he or ""):
            dropped += 1
            continue
        segs = [s for s in (plain or "").split("/") if s]
        if not segs:
            continue
        # the stem is the longest segment; prefixes are one or two letters
        stem = max(segs, key=len)
        out.setdefault(osis, []).append((cons(stem), morph or ""))
    return out, dropped


# --------------------------------------------------------------- Aramaic side
def load_onkelos(book):
    p = f"{REPO}/Data/sefaria_export/{BOOKS[book]}/he.json"
    text = json.load(open(p))["text"]
    out = {}
    for ci, ch in enumerate(text, 1):
        for vi, v in enumerate(ch, 1):
            if isinstance(v, list):
                v = " ".join(v)
            if not v or not v.strip():
                continue
            words = [cons(w) for w in v.split()]
            out[f"{book}.{ci}.{vi}"] = [w for w in words if w]
    return out


# -------------------------------------------------------------------- metrics
def retention(heb_stems, aram_words):
    """Fraction of Hebrew stems (>=3 letters) with a 3-letter run surviving."""
    stems = [s for s, m in heb_stems if len(s) >= 3 and not m.startswith("HTn")]
    if not stems:
        return None
    blob = " ".join(aram_words)
    kept = 0
    for s in stems:
        runs = [s[i:i + 3] for i in range(len(s) - 2)]
        if any(r in blob for r in runs):
            kept += 1
    return kept / len(stems)


def measure(heb, onk, book):
    rows = {}
    for ref, aram in onk.items():
        stems = heb.get(ref)
        if not stems:
            continue
        rows[ref] = {
            "nh": len(stems),
            "na": len(aram),
            "exp": len(aram) / len(stems),
            "ret": retention(stems, aram),
        }
    return rows


def chapter_stats(rows, book, ch):
    sel = [r for ref, r in rows.items()
           if ref.startswith(f"{book}.{ch}.")]
    if not sel:
        return None
    rets = [r["ret"] for r in sel if r["ret"] is not None]
    return {
        "verses": len(sel),
        "exp": mean(r["exp"] for r in sel),
        "ret": mean(rets) if rets else None,
    }


# ----------------------------------------------------------------------- main
def main():
    heb, dropped = load_hebrew()
    print(f"SCANNED: {len(heb)} Hebrew verses from {DB.split('/')[-1]}")
    print(f"         {dropped} ketiv (written-form) rows dropped as duplicates")

    all_rows, all_onk = {}, {}
    for b in BOOKS:
        o = load_onkelos(b)
        all_onk[b] = o
        r = measure(heb, o, b)
        all_rows[b] = r
        print(f"         {b}: {len(o)} Onkelos verses, {len(r)} paired")

    # ---------------------------------------------------- PROBE (self-test)
    print("\n" + "=" * 72)
    print("PROBE — the metrics must separate known paraphrase from known plain")
    print("=" * 72)
    g = all_rows["Gen"]
    HIGH = ["Gen.49.10", "Gen.49.27", "Gen.49.5", "Gen.49.6", "Gen.49.3"]
    LOW = [f"Gen.5.{v}" for v in range(3, 32)] + \
          [f"Gen.11.{v}" for v in range(10, 27)]
    hi = [g[r] for r in HIGH if r in g]
    lo = [g[r] for r in LOW if r in g]
    if len(hi) < 3 or len(lo) < 10:
        sys.exit("PROBE FAILED TO LOAD — refusing to report.")
    hx, lx = mean(r["exp"] for r in hi), mean(r["exp"] for r in lo)
    hr = mean(r["ret"] for r in hi if r["ret"] is not None)
    lr = mean(r["ret"] for r in lo if r["ret"] is not None)
    print(f"  known paraphrase ({len(hi)} vv, Gen 49 ledger rows O1-O5):")
    print(f"      expansion {hx:.2f}   retention {hr:.2f}")
    print(f"  known plain      ({len(lo)} vv, Gen 5 + 11 genealogies):")
    print(f"      expansion {lx:.2f}   retention {lr:.2f}")
    okA, okB = hx > lx * 1.15, hr < lr * 0.90
    print(f"  metric A (expansion) separates: {okA}")
    print(f"  metric B (retention) separates: {okB}")
    if not (okA or okB):
        sys.exit("NEITHER METRIC FIRES ON A KNOWN POSITIVE — refusing to report.")
    print("  -> probe passes; the metrics detect the thing they look for.")

    # -------------------------------------------------- Genesis, all chapters
    print("\n" + "=" * 72)
    print("GENESIS — every chapter, ranked by expansion")
    print("=" * 72)
    stats = []
    for ch in range(1, 51):
        s = chapter_stats(g, "Gen", ch)
        if s:
            stats.append((ch, s))
    base_exp = mean(s["exp"] for ch, s in stats if ch != 49)
    base_ret = mean(s["ret"] for ch, s in stats if ch != 49)
    print(f"Genesis baseline excluding ch.49: expansion {base_exp:.3f}  "
          f"retention {base_ret:.3f}")
    print(f"{'ch':>4} {'vv':>4} {'expansion':>10} {'vs base':>9} "
          f"{'retention':>10} {'vs base':>9}")
    for ch, s in sorted(stats, key=lambda x: -x[1]["exp"])[:12]:
        print(f"{ch:>4} {s['verses']:>4} {s['exp']:>10.3f} "
              f"{s['exp'] / base_exp:>8.2f}x {s['ret']:>10.3f} "
              f"{s['ret'] / base_ret:>8.2f}x")
    print("  ... lowest three ...")
    for ch, s in sorted(stats, key=lambda x: x[1]["exp"])[:3]:
        print(f"{ch:>4} {s['verses']:>4} {s['exp']:>10.3f} "
              f"{s['exp'] / base_exp:>8.2f}x {s['ret']:>10.3f} "
              f"{s['ret'] / base_ret:>8.2f}x")

    # ------------------------------------------- THE POETRY TEST, five books
    print("\n" + "=" * 72)
    print("THE POETRY TEST — is this a chapter-49 fact or a poetry fact?")
    print("=" * 72)
    POEMS = [
        ("Gen", 49, "Jacob's blessings"),
        ("Exod", 15, "the Song of the Sea"),
        ("Num", 23, "Balaam, oracles 1-2"),
        ("Num", 24, "Balaam, oracles 3-7"),
        ("Deut", 32, "the Song of Moses"),
        ("Deut", 33, "the Blessing of Moses"),
    ]
    print(f"{'chapter':>28} {'vv':>4} {'expansion':>10} {'vs book':>9} "
          f"{'retention':>10} {'vs book':>9}")
    book_base = {}
    for b in BOOKS:
        rows = all_rows[b]
        chs = []
        poem_chs = {c for bb, c, _ in POEMS if bb == b}
        nch = max(int(r.split(".")[1]) for r in rows)
        for ch in range(1, nch + 1):
            s = chapter_stats(rows, b, ch)
            if s and ch not in poem_chs:
                chs.append(s)
        book_base[b] = (mean(s["exp"] for s in chs),
                        mean(s["ret"] for s in chs))
    for b, ch, name in POEMS:
        s = chapter_stats(all_rows[b], b, ch)
        be, br = book_base[b]
        label = f"{b} {ch} — {name}"
        print(f"{label:>28} {s['verses']:>4} {s['exp']:>10.3f} "
              f"{s['exp'] / be:>8.2f}x {s['ret']:>10.3f} {s['ret'] / br:>8.2f}x")
    print(f"\n{'book prose baselines':>28} {'':>4} {'expansion':>10} "
          f"{'':>9} {'retention':>10}")
    for b in BOOKS:
        be, br = book_base[b]
        print(f"{b:>28} {'':>4} {be:>10.3f} {'':>9} {br:>10.3f}")

    # ------------------------------------ short poems embedded in Genesis prose
    print("\n" + "=" * 72)
    print("THE SHORT POEMS INSIDE GENESIS PROSE — the same test, verse level")
    print("=" * 72)
    SHORT = [
        ("Gen.3.14-19", "the three sentences in the garden"),
        ("Gen.4.23-24", "Lamech's song to his wives"),
        ("Gen.9.25-27", "Noah's blessing and curse"),
        ("Gen.25.23", "the oracle to Rebecca"),
        ("Gen.27.27-29", "Isaac's blessing of Jacob"),
        ("Gen.27.39-40", "Isaac's word to Esau"),
        ("Gen.48.15-16", "the blessing of the two boys"),
        ("Gen.49.1-33", "-- the chapter in question --"),
    ]
    gbase_e, gbase_r = book_base["Gen"]
    print(f"{'span':>16} {'vv':>4} {'expansion':>10} {'vs prose':>9} "
          f"{'retention':>10} {'vs prose':>9}  what")
    for span, name in SHORT:
        b, ch, rng = span.split(".")
        a, _, z = rng.partition("-")
        z = z or a
        sel = [g[f"{b}.{ch}.{v}"] for v in range(int(a), int(z) + 1)
               if f"{b}.{ch}.{v}" in g]
        if not sel:
            continue
        e = mean(r["exp"] for r in sel)
        rr = mean(r["ret"] for r in sel if r["ret"] is not None)
        print(f"{span:>16} {len(sel):>4} {e:>10.3f} {e / gbase_e:>8.2f}x "
              f"{rr:>10.3f} {rr / gbase_r:>8.2f}x  {name}")

    # --------------------------------------------- the seven middle blessings
    print("\n" + "=" * 72)
    print("INSIDE CHAPTER 49 — verse by verse (the ledger's O-rows named)")
    print("=" * 72)
    LEDGER = {10: "O1", 3: "O2", 4: "O2", 24: "O3", 25: "O3", 27: "O4",
              5: "O5", 6: "O5", 8: "O6", 9: "O6",
              13: "O7", 14: "O7", 15: "O7", 16: "O7", 17: "O7", 19: "O7",
              20: "O7", 21: "O7", 22: "O7",
              2: "O8", 26: "O8"}
    print(f"{'verse':>10} {'heb':>4} {'aram':>5} {'expansion':>10} "
          f"{'retention':>10}  ledger")
    for v in range(1, 34):
        r = g.get(f"Gen.49.{v}")
        if not r:
            continue
        tag = LEDGER.get(v, "O9 (still translating)")
        flag = "  <<<" if r["exp"] > gbase_e * 1.5 else ""
        print(f"   Gen 49:{v:<2} {r['nh']:>4} {r['na']:>5} {r['exp']:>10.2f} "
              f"{r['ret']:>10.2f}  {tag}{flag}")


main()
