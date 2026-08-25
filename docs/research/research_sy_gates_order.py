#!/usr/bin/env python3
"""Order is meaning: the directionality of the gates — the
reproduction script for the sixth look of
RESEARCH_sefer_yetzirah_database_2026-08-24.md.

Sefer Yetzirah's tzeruf ("combination") doctrine holds that letter
ORDER carries meaning (3:7-9: the male formed with alef-mem-shin, the
female with alef-shin-mem). This script asks the order question of
the Torah's verb roots: when a gate (letter-pair) is used, does the
lexicon use both directions, or is the door one-way? Controls: a
fair-coin null (simulated), and a strong-letters-only frame that
excludes the glides heh/vav/yod whose citation-form slots would
manufacture directionality. Model-layer research; grounds no claim.

Inputs: data/tanakh.sqlite (in-repo) and HebrewStrong.xml (public
domain, NOT committed; fetch per research_sy_gates.py's header).
Run from the repo root: python3 docs/research/research_sy_gates_order.py
"""
import re, sqlite3, unicodedata, itertools, collections, random, sys, os
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
XML = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "HebrewStrong.xml")
DB = os.path.join(REPO, "data", "tanakh.sqlite")

SY_CLASSES = {
    "throat": set("אהחע"),   # alef-heh-chet-ayin
    "palate": set("גיכק"),   # gimel-yod-kaf-qof
    "tongue": set("דטלנת"),  # dalet-tet-lamed-nun-tav
    "teeth":  set("זסשרצ"),  # zayin-samekh-shin-resh-tsadi
    "lips":   set("בומפ"),   # bet-vav-mem-peh
}
def sy_class(c):
    for n, s in SY_CLASSES.items():
        if c in s: return n
GLIDES = set("הוי")          # heh-vav-yod, the citation-form weak letters
MOTHERS = "אמש"              # alef-mem-shin
FINALS = {"ך": "כ", "ם": "מ", "ן": "נ", "ף": "פ", "ץ": "צ"}  # final forms normalized
def skeleton(w):
    return "".join(FINALS.get(c, c) for c in w
                   if unicodedata.category(c) != "Mn" and "א" <= c <= "ת")  # alef..tav

def load_roots(torah_only=True):
    ns = {"s": "http://openscriptures.github.com/morphhb/namespace"}
    strongs = {}
    for e in ET.parse(XML).getroot().findall("s:entry", ns):
        w = e.find("s:w", ns)
        if w is not None and w.text:
            strongs[e.get("id").lstrip("H")] = (
                w.text.strip(),
                w.get("{http://www.w3.org/XML/1998/namespace}lang"))
    con = sqlite3.connect(DB)
    scope = ("JOIN verses v ON w.verse_id = v.id "
             "WHERE v.book IN ('Gen','Exod','Lev','Num','Deut') AND "
             if torah_only else "WHERE ")
    rows = con.execute(
        f"SELECT DISTINCT w.lemma FROM words w {scope}"
        "(w.morph LIKE 'HV%' OR w.morph LIKE '%/V%')").fetchall()
    con.close()
    roots = set()
    for (lemma,) in rows:
        m = re.match(r"\d+", str(lemma))
        if m and m.group(0) in strongs:
            head, lang = strongs[m.group(0)]
            if lang != "arc":
                sk = skeleton(head)
                if len(sk) == 3: roots.add(sk)
    return sorted(roots)

def directed_counts(roots):
    d = collections.Counter()
    for r in roots:
        for a, b in ((r[0], r[1]), (r[1], r[2])):
            if a != b: d[(a, b)] += 1
    gate = {}
    for p in {frozenset(k) for k in d}:
        a, b = sorted(p)
        gate[p] = (d[(a, b)], d[(b, a)])
    return d, gate

def oneway_stats(gate, label):
    print(f"\n== {label}: {len(gate)} attested gates ==")
    rng = random.Random(7)
    for K in (2, 3, 4, 6):
        gs = {g: v for g, v in gate.items() if sum(v) >= K}
        oneway = [g for g, (x, y) in gs.items() if x == 0 or y == 0]
        exp = sum(2 * 0.5 ** sum(v) for v in gs.values())
        ns_ = [sum(v) for v in gs.values()]
        obs, hits, T = len(oneway), 0, 20000
        for _ in range(T):
            c = sum(1 for n in ns_
                    if (lambda k: k == 0 or k == n)(
                        sum(rng.random() < .5 for _ in range(n))))
            if c >= obs: hits += 1
        maj = sum(max(v) for v in gs.values())
        tot = sum(sum(v) for v in gs.values())
        print(f"  >= {K} roots: {len(gs)} gates, one-way {obs} "
              f"(fair-coin exp {exp:.1f}, p~{hits/T:.4f}), "
              f"majority-direction share {100*maj/tot:.0f}%")

if __name__ == "__main__":
    roots = load_roots(torah_only=True)
    print(f"Torah triliteral verb roots: {len(roots)}")
    directed, gate = directed_counts(roots)

    oneway_stats(gate, "ALL letters")
    strong = {g: v for g, v in gate.items() if not (set(g) & GLIDES)}
    oneway_stats(strong, "STRONG letters only (no heh/vav/yod)")

    print("\nstrong-letter one-way gates with >= 4 roots:")
    for g, (x, y) in sorted(strong.items(), key=lambda kv: -sum(kv[1])):
        if (x == 0 or y == 0) and sum((x, y)) >= 4:
            a, b = sorted(g)
            d = f"{a}→{b}" if x else f"{b}→{a}"
            print(f"  {d}  {max(x,y)}:0  ({sy_class(a)}/{sy_class(b)})")

    print("\nbusiest two-way strong gates:")
    for g, (x, y) in sorted(strong.items(), key=lambda kv: -sum(kv[1]))[:8]:
        a, b = sorted(g)
        print(f"  {a}{b}: {a}→{b} {x} / {b}→{a} {y}")

    print("\nper-slot share by mouth-class, strong letters only (1st/2nd/3rd):")
    pos = collections.defaultdict(lambda: [0, 0, 0])
    for r in roots:
        for i, c in enumerate(r):
            if c not in GLIDES: pos[sy_class(c)][i] += 1
    for name, (a, b, c) in pos.items():
        t = a + b + c
        print(f"  {name:7s} {100*a/t:4.0f}% {100*b/t:4.0f}% {100*c/t:4.0f}%  (n={t})")

    print("\nmost slot-skewed common strong letters (>=20 root occurrences):")
    skew = []
    for L in sorted(set("".join(roots))):
        if L in GLIDES: continue
        c = [0, 0, 0]
        for r in roots:
            for i, ch in enumerate(r):
                if ch == L: c[i] += 1
        if sum(c) >= 20: skew.append((max(c)/sum(c), L, c, sum(c)))
    for s, L, c, t in sorted(skew, reverse=True)[:6]:
        print(f"  {L}: slots {c} of {t} ({100*s:.0f}% in one slot)")

    print("\nthe three mothers (alef-mem-shin): orderings lexicalized, Tanakh-wide:")
    tanakh = load_roots(torah_only=False)
    print(f"  (Tanakh verb roots: {len(tanakh)})")
    for p in ("".join(x) for x in itertools.permutations(MOTHERS)):
        hit = p in set(tanakh)
        print(f"  {p}: {'ROOT EXISTS' if hit else '—'}")
