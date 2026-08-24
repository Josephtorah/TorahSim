#!/usr/bin/env python3
"""The 231 gates against the Torah's verb-root inventory — the
reproduction script for the fifth look of
RESEARCH_sefer_yetzirah_database_2026-08-24.md.

Sefer Yetzirah 2:4-5 combines the 22 letters pairwise into 231 gates
("all that is spoken emerges from them"); 2:3 gives the five
mouth-classes. This script builds the wheel from the Torah's real verb
roots and tests whether the unused gates fall where the classes
predict. Model-layer research; grounds no claim in any unit.

Inputs:
  data/tanakh.sqlite            — the parse database (in-repo path)
  HebrewStrong.xml              — Strong's lexicon headwords, public
    domain, NOT committed; fetch beside this script (or pass its path
    as argv[1]):
      curl -sL -o docs/research/HebrewStrong.xml \
        https://raw.githubusercontent.com/openscriptures/HebrewLexicon/master/HebrewStrong.xml

Run from the repo root: python3 docs/research/research_sy_gates.py
"""
import re, sqlite3, unicodedata, itertools, collections, math, sys, os
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
XML = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "HebrewStrong.xml")
DB = os.path.join(REPO, "data", "tanakh.sqlite")

# Sefer Yetzirah 2:3 — the five mouth-classes, SY's own phonetics
SY_CLASSES = {
    "throat": set("אהחע"),   # alef-heh-chet-ayin
    "palate": set("גיכק"),   # gimel-yod-kaf-qof
    "tongue": set("דטלנת"),  # dalet-tet-lamed-nun-tav
    "teeth":  set("זסשרצ"),  # zayin-samekh-shin-resh-tsadi
    "lips":   set("בומפ"),   # bet-vav-mem-peh
}
LETTERS = sorted(set().union(*SY_CLASSES.values()))
assert len(LETTERS) == 22
def sy_class(c):
    for name, s in SY_CLASSES.items():
        if c in s: return name

FINALS = {"ך": "כ", "ם": "מ", "ן": "נ", "ף": "פ", "ץ": "צ"}  # final forms normalized (khaf/mem/nun/peh/tsadi)
def skeleton(word):
    """Pointed headword -> consonantal skeleton (marks stripped, finals normalized)."""
    return "".join(FINALS.get(c, c) for c in word
                   if unicodedata.category(c) != "Mn" and "א" <= c <= "ת")  # alef..tav

def load_strongs():
    ns = {"s": "http://openscriptures.github.com/morphhb/namespace"}
    out = {}
    for e in ET.parse(XML).getroot().findall("s:entry", ns):
        w = e.find("s:w", ns)
        if w is not None and w.text:
            out[e.get("id").lstrip("H")] = (
                w.text.strip(),
                w.get("{http://www.w3.org/XML/1998/namespace}lang"))
    return out

def verb_roots(strongs, torah_only=True):
    """Distinct triliteral consonantal skeletons of the corpus's verb lemmas."""
    con = sqlite3.connect(DB)
    scope = ("JOIN verses v ON w.verse_id = v.id "
             "WHERE v.book IN ('Gen','Exod','Lev','Num','Deut') AND "
             if torah_only else "WHERE ")
    rows = con.execute(
        f"SELECT DISTINCT w.lemma FROM words w {scope}"
        "(w.morph LIKE 'HV%' OR w.morph LIKE '%/V%')").fetchall()
    con.close()
    skels, outliers = set(), []
    for (lemma,) in rows:
        m = re.match(r"\d+", str(lemma))
        if not m or m.group(0) not in strongs: continue
        head, lang = strongs[m.group(0)]
        if lang == "arc": continue          # Aramaic entries excluded
        sk = skeleton(head)
        if len(sk) == 3: skels.add(sk)
        elif sk: outliers.append((m.group(0), head, sk))
    return skels, outliers

def gate_counts(skels):
    """Adjacent-slot pair counts (first-second, second-third) + geminate tallies."""
    adj = collections.Counter()
    gem12 = gem23 = 0
    freq1, freq2, slot_pairs = collections.Counter(), collections.Counter(), 0
    for r in sorted(skels):
        c1, c2, c3 = r
        if c1 == c2: gem12 += 1
        if c2 == c3: gem23 += 1
        for a, b in ((c1, c2), (c2, c3)):
            slot_pairs += 1; freq1[a] += 1; freq2[b] += 1
            if a != b: adj[frozenset((a, b))] += 1
    return adj, gem12, gem23, freq1, freq2, slot_pairs

def analyze(label, skels):
    adj, gem12, gem23, f1, f2, sp = gate_counts(skels)
    gates = [frozenset(p) for p in itertools.combinations(LETTERS, 2)]
    same = [g for g in gates if len({sy_class(c) for c in g}) == 1]
    cross = [g for g in gates if len({sy_class(c) for c in g}) > 1]
    empty = [g for g in gates if adj[g] == 0]
    same_empty = [g for g in empty if g in set(same)]
    print(f"\n===== {label}: {len(skels)} distinct triliteral roots =====")
    print(f"attested gates: {231 - len(empty)}/231")
    print(f"same-class empty: {len(same_empty)}/{len(same)} "
          f"({100*len(same_empty)/len(same):.0f}%)   cross-class empty: "
          f"{len(empty)-len(same_empty)}/{len(cross)} "
          f"({100*(len(empty)-len(same_empty))/len(cross):.0f}%)")
    print(f"geminates: first=second {gem12}   second=third {gem23}")
    exp = lambda a, b: (f1[a]*f2[b] + f1[b]*f2[a]) / sp
    for name, gs in (("same-class", same), ("cross-class", cross)):
        O = sum(adj[g] for g in gs); E = sum(exp(*sorted(g)) for g in gs)
        print(f"{name} O/E = {O}/{E:.1f} = {O/E:.2f}")
    print("same-class gates (letter-pair O observed, E expected; · = empty):")
    for g in sorted(same, key=lambda g: (sy_class(sorted(g)[0]), "".join(sorted(g)))):
        a, b = sorted(g)
        print(f"  {a}{b} ({sy_class(a):7s}) O={adj[g]:2d} E={exp(a,b):5.2f}"
              f"{'  EMPTY' if adj[g]==0 else ''}")
    print("cross-class empty gates:",
          " ".join(sorted("".join(sorted(g)) for g in empty if g not in set(same))))
    # chance of the same-class clustering (hypergeometric upper tail)
    N, K, n, k = 231, len(same), len(empty), len(same_empty)
    p = sum(math.comb(K, i)*math.comb(N-K, n-i)
            for i in range(k, min(K, n)+1)) / math.comb(N, n)
    print(f"P(clustering this strong by chance) = {p:.2e}")
    return empty

if __name__ == "__main__":
    strongs = load_strongs()
    torah, outliers = verb_roots(strongs, torah_only=True)
    print("non-triliteral outliers excluded (Torah scope):")
    for num, head, sk in sorted(outliers, key=lambda x: len(x[2])):
        print(f"  H{num} {head} -> {sk} ({len(sk)})")
    analyze("TORAH (Genesis-Deuteronomy)", torah)
    tanakh, _ = verb_roots(strongs, torah_only=False)
    analyze("TANAKH-WIDE (robustness)", tanakh)
