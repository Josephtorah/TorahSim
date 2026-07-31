#!/usr/bin/env python3
"""discover_devices.py — empirical discovery of the Oral chain's technical
language from our cached sources.

Method: count word n-grams (2-5) across all cached Oral texts by DOCUMENT
frequency (how many distinct sources use the phrase), after removing (a) HTML,
vowel points and cantillation, and (b) phrases that occur in the Written Torah
itself (those are quotations of the object language, not the chain's own
metalanguage). What survives at high document frequency is, empirically, the
chain's working vocabulary — announcement formulas, teaching operators,
argument connectives. Discovery = documentation of usage; nothing here mints
a rule (ein adam dan me-atzmo — "one may not derive on his own").

Also scans a curated list of KNOWN-BUT-UNLISTED named devices (hekesh —
"juxtaposition"; semukhin — "adjacency"; asmakhta — "support text"; the
yakhol/talmud-lomar — "one might think… Scripture teaches" — structure, etc.)
so the census covers both mined and named candidates.

Output: DISCOVERY_devices_<date>.md (top mined phrases + named-device hits),
for human classification. Survey tool; Pre-Code safe.
"""
import glob
import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DB = ROOT / "torah_grok.sqlite"
OUT = ROOT / "logic" / "middot_scan"
CACHE = ROOT / "Data" / "sefaria_texts"

NIQQUD = re.compile(r"[֑-ׇ]")
PUNCT = re.compile(r'[״׳"\'().,:;!?\[\]{}<>«»—–-]')

MIN_DOCS = {2: 25, 3: 12, 4: 8, 5: 6}    # document-frequency floors per n
TOP = 130

# Known-but-unlisted named devices (each glossed) — scanned alongside mining.
NAMED_DEVICES = [
    ("hekesh (\"juxtaposition\": two topics in one verse share law)",
     ["היקש", "הקישא", "מקיש"]),
    ("semukhin (\"adjacency\": neighboring passages illuminate each other)",
     ["סמוכין", "סמוכים מן התורה", "למה נסמכה"]),
    ("asmakhta (\"support text\": citation as mnemonic support, not source)",
     ["אסמכתא"]),
    ("im eino inyan (\"if not needed for its own matter, apply it elsewhere\")",
     ["אם אינו ענין", "אם אינו עניין"]),
    ("yakhol … talmud lomar (\"one might think … Scripture teaches\": "
     "hypothesis-rejection structure)",
     ["יכול", "תלמוד לומר", 'ת"ל', "ת״ל"]),
    ("shomea ani (\"I might understand\": the Mekhilta's hypothesis marker)",
     ["שומע אני"]),
    ("ne'emar kan ve-ne'emar lehalan (\"said here and said there\": the "
     "verbal-analogy execution formula)",
     ["נאמר כאן ונאמר להלן", "נאמר להלן"]),
    ("mikan amru (\"from here they said\": derivation-to-law marker)",
     ["מכאן אמרו", "מיכן אמרו"]),
    ("melamed she- (\"it teaches that\": the tannaitic teaching operator)",
     ["מלמד ש", "מגיד ש", "מגיד הכתוב"]),
    ("lamah ne'emar (\"why is it stated\": the Yishmael-school question)",
     ["למה נאמר", "מה תלמוד לומר"]),
    ("ha keitzad (\"how so\": reconciliation of clashing sources)",
     ["הא כיצד"]),
    ("middah keneged middah (\"measure for measure\": narrative causality rule)",
     ["מדה כנגד מדה", "מידה כנגד מידה"]),
    ("bi-zekhut (\"in the merit of\": aggadic causality operator)",
     ["בזכות"]),
    ("kivyakhol (\"as it were\": anthropomorphism guard)",
     ["כביכול"]),
    ("ilmale mikra katuv (\"were it not written, it could not be said\": "
     "audacity guard on anthropomorphism)",
     ["אלמלא מקרא כתוב", "אילמלא מקרא כתוב"]),
    ("keri beih (\"read into it\": consonantal re-reading operator)",
     ["קרי ביה"]),
    ("zekher la-davar (\"a hint to the matter\": weak-support marker)",
     ["זכר לדבר"]),
]


def load_oral_texts():
    texts = {}
    for f in glob.glob(str(CACHE / "*.json")):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        ref = d.get("ref") or Path(f).stem
        he = d.get("he", "")
        if isinstance(he, list):
            he = " ".join(x if isinstance(x, str) else " ".join(map(str, x))
                          for x in he)
        t = NIQQUD.sub("", re.sub(r"<[^>]+>", "", he or ""))
        t = PUNCT.sub(" ", t)
        toks = [w for w in t.split() if w]
        if toks:
            texts[ref] = toks
    return texts


def torah_ngram_set(con, nmax=5):
    """All consonantal word n-grams of the Written Torah (to exclude quotations)."""
    rows = con.execute(
        "SELECT v.id, w.he_plain FROM words w JOIN verses v ON v.id=w.verse_id"
        " ORDER BY v.id, w.idx").fetchall()
    by_verse = defaultdict(list)
    for vid, hp in rows:
        by_verse[vid].append((hp or "").replace("/", ""))
    tset = set()
    for toks in by_verse.values():
        for n in range(2, nmax + 1):
            for i in range(len(toks) - n + 1):
                tset.add(" ".join(toks[i:i + n]))
    return tset


def mine(texts, torah_grams):
    doc_freq = {n: Counter() for n in MIN_DOCS}
    for ref, toks in texts.items():
        seen = set()
        for n in MIN_DOCS:
            for i in range(len(toks) - n + 1):
                g = " ".join(toks[i:i + n])
                if (n, g) not in seen:
                    seen.add((n, g))
        for n, g in seen:
            if g not in torah_grams:
                doc_freq[n][g] += 1
    # collect candidates over floor; prefer maximal phrases (drop grams whose
    # every occurrence context is covered by a selected longer gram)
    selected = []
    for n in sorted(MIN_DOCS, reverse=True):
        for g, df in doc_freq[n].items():
            if df >= MIN_DOCS[n]:
                if any(g in longer for longer, _ in selected):
                    continue
                selected.append((g, df))
    selected.sort(key=lambda x: -x[1])
    return selected


def named_hits(texts):
    hits = []
    for device, needles in NAMED_DEVICES:
        srcs = []
        for ref, toks in texts.items():
            t = " ".join(toks)
            if any(n in t for n in needles):
                srcs.append(ref)
        if srcs:
            hits.append((device, len(srcs), sorted(srcs)[:6]))
    hits.sort(key=lambda x: -x[1])
    return hits


def main():
    con = sqlite3.connect(str(DB))
    texts = load_oral_texts()
    torah_grams = torah_ngram_set(con)
    mined = mine(texts, torah_grams)
    named = named_hits(texts)

    lines = ["# DISCOVERY — the chain's technical language, mined from our cache",
             "",
             f"Corpus: {len(texts)} cached Oral sources (honest counter — "
             "coverage bounded by the cache). Method: word n-grams ranked by "
             "DOCUMENT frequency (distinct sources using the phrase), with all "
             "phrases occurring in the Written Torah excluded — what remains "
             "is the chain's own metalanguage, not quotation. Discovery = "
             "documentation of usage; no rule is minted here.",
             "",
             "## Named-but-unlisted devices (curated scan)",
             "",
             "device (glossed) | sources | examples"]
    lines.append("-----------------|---------|---------")
    for device, nsrc, ex in named:
        lines.append(f"{device} | {nsrc} | {', '.join(ex)}")
    lines += ["", "## Mined phrases (top by document frequency, "
              "quotations excluded)", "",
              "UNCLASSIFIED — for human classification into: known formula / "
              "NEW device candidate / connective / liturgical or noise.", "",
              "phrase | sources"]
    lines.append("-------|--------")
    for g, df in mined[:TOP]:
        lines.append(f"{g} | {df}")
    (OUT / "DISCOVERY_devices_2026-07-31.md").write_text("\n".join(lines),
                                                         encoding="utf-8")
    print(f"sources: {len(texts)} · torah-grams excluded: {len(torah_grams)} · "
          f"mined candidates: {len(mined)} (top {TOP} written) · "
          f"named devices found: {len(named)}")
    con.close()


if __name__ == "__main__":
    main()
