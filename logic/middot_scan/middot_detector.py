#!/usr/bin/env python3
"""middot_detector.py — machine-surfaced candidates for the classical interpretive
rules (middot = "measures"). Survey tool: derives no law, touches no unit YAML.

Corpus side : rare shared lemmas = candidate verbal-analogy (gezerah shavah,
              "equal decree") join keys, graded by overload (mufneh, "free").
Chain side  : rule-announcement formulas searched in the locally cached Oral
              sources (bounded by cache; honest counters reported).
Calibration : both sides joined against the triage ledgers.

Outputs: derived DB tables middot_joins / middot_invocations (rebuildable) and
markdown reports in logic/middot_scan/.
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

RARE_MAX = 12          # lemma total occurrences in the Torah to count as join-grade rare
NIQQUD = re.compile(r"[֑-ׇ]")   # Hebrew vowel points + cantillation marks

# The chain's rule-announcement formulas (unpointed), each tagged with its
# rulebook — "13" = Rabbi Yishmael's thirteen middot ("measures"), the LAW-side
# inference rules; "32" = Rabbi Eliezer b. R. Yose the Galilean's thirty-two,
# the NARRATIVE-side (aggadah, "telling") reading rules; "shared" = in both;
# "operator" = standard midrashic citation/alternation operators that ride
# alongside the rules. Every Hebrew formula carries its English counterpart
# (absolute glossing rule).
FORMULAS = [
    ("shared", "kal va-chomer (light-and-heavy: the how-much-more-so argument)",
     ["קל וחומר", "קל חומר", "על אחת כמה וכמה", 'ק"ו', "ק״ו", "קו וחומר"]),
    ("shared", "gezerah shavah (equal decree: verbal analogy on a shared word)",
     ["גזרה שוה", "גזירה שוה", "גזרה שווה", "גזירה שווה", 'גז"ש', "גז״ש"]),
    ("shared", "atya (\"it is derived\": the Aramaic verbal-analogy operator)",
     ["אתיא", "אתא קרא"]),
    ("shared", "katuv echad omer (\"one verse says\": contradiction until a third decides)",
     ["כתוב אחד אומר", "כתוב א' אומר"]),
    ("13", "mufneh (\"free\": join-key availability check for verbal analogy)",
     ["מופנה", "מפנה גבי"]),
    ("shared", "binyan av (\"father-building\": prototype generalization)",
     ["בנין אב", "בניין אב"]),
    ("13", "klal u-frat (\"general and particular\": scope restriction family)",
     ["כלל ופרט", "פרט וכלל", "כלל ופרט וכלל"]),
    ("shared", "mah lehalan af kan (\"as there, so here\": analogy transfer formula)",
     ["מה להלן אף כאן", "מה כאן אף להלן"]),
    # ---- 32-side (aggadah, narrative) instruments ----
    ("32", "ribbui (\"inclusion\": et/gam/af come to include — rules 1/3)",
     ["לרבות", "אין רבוי אחר רבוי", "ריבה"]),
    ("32", "mi'ut (\"exclusion\": akh/raq exclude — rules 2/4)",
     ["למעט", "אין מיעוט אחר מיעוט"]),
    ("32", "mashal (\"parable\" — rule 26; the king-parable is its classic form)",
     ["משל למלך", "משל לאחד", "משל למה הדבר דומה"]),
    ("32", "lashon nofel al lashon (\"language falling on language\": wordplay — rule 28 family)",
     ["לשון נופל על לשון", "לשון הנופל על לשון"]),
    ("32", "gematria (\"letter-arithmetic\": words as number values — rule 29)",
     ["גימטריא", "בגימטריא", "גמטריא"]),
    ("32", "notarikon (\"acronym reading\": a word unpacked as initials — rule 30)",
     ["נוטריקון", "נוטריקין"]),
    ("32", "mukdam u-me'uchar (\"earlier and later\": narrative order is not event order — rules 31/32)",
     ["אין מוקדם ומאוחר", "מוקדם ומאוחר"]),
    ("32", "al tikrei (\"do not read X but Y\": revocalization device)",
     ["אל תקרי", "אל תיקרי", "אל תקרא"]),
    ("operator", "hada hu dikhtiv (\"this is what is written\": the prooftext opener of Bereshit Rabbah — \"Great Genesis\")",
     ["הדא הוא דכתיב", 'הה"ד', "הה״ד"]),
    ("operator", "zeh she-amar ha-katuv (\"this is what Scripture said\": the sermon/petichta opener)",
     ["זה שאמר הכתוב", 'זש"ה', "זש״ה"]),
    ("operator", "davar acher (\"another interpretation\": the multi-reading alternation operator)",
     ["דבר אחר", 'ד"א', "ד״א"]),
    # ---- discovered 2026-07-31 by corpus mining (DISCOVERY_devices report) ----
    ("discovered", "ein ketiv kan ela (\"it is not written here … but rather\": the chain's diff operator — expected wording vs actual)",
     ["אין כתיב כאן", "אין כתוב כאן"]),
    ("discovered", "kemah de-at amar (\"as you say [elsewhere]\": usage-analogy — a word's sense imported from another verse)",
     ["כמה דאת אמר", "כמא דאת אמר", "כמה דתימר"]),
    ("discovered", "ein X ela Y (\"X means nothing but Y\": the lexical definition operator)",
     ["ואין טוב אלא", "אין טוב אלא", "ואין מים אלא", "ואין אור אלא"]),
    ("discovered", "lekhakh ne'emar (\"therefore it is stated\": derivation closer)",
     ["לכך נאמר", "לכך הוא אומר"]),
    ("discovered", "ve-khen hu omer (\"and so it says\": corroborating second prooftext)",
     ["וכן הוא אומר", "וכה הוא אומר"]),
    ("discovered", "yakhol/talmud lomar (\"one might think … Scripture teaches\": hypothesis-rejection structure — most widespread device in the cache)",
     ["תלמוד לומר", 'ת"ל', "ת״ל", "שומע אני"]),
    ("discovered", "melamed she- (\"it teaches that\": tannaitic teaching operator)",
     ["מלמד ש", "מגיד הכתוב"]),
    ("discovered", "bi-zekhut (\"in the merit of\": aggadic causality operator)",
     ["בזכות"]),
    ("discovered", "kivyakhol (\"as it were\": anthropomorphism guard)",
     ["כביכול"]),
]


def strip_points(s):
    return NIQQUD.sub("", s or "")


def norm_lemma(lemma):
    if not lemma:
        return None
    core = lemma.split("/")[-1].strip()
    return core if re.match(r"\d", core) else None


def content_seg(morph, he_plain):
    """(kind, display) for the content segment: verb/noun/adjective."""
    if not morph:
        return None, None
    segs = morph[1:].split("/")
    toks = (he_plain or "").split("/")
    for i, s in enumerate(segs):
        if s and s[0] in ("V", "N", "A"):
            disp = toks[i] if i < len(toks) else (he_plain or "")
            return s[0], disp
    return None, None


# ------------------------------------------------------------- corpus side --

def corpus_joins(con):
    """Rare lemmas shared across >=2 chapters -> candidate verbal-analogy keys."""
    rows = con.execute(
        "SELECT v.book b, v.chapter c, v.verse vs, w.he_plain hp, w.translit tr,"
        " w.lemma lm, w.morph mo FROM words w JOIN verses v ON v.id=w.verse_id"
        " ORDER BY v.id, w.idx").fetchall()
    uses = defaultdict(list)
    disp = {}
    for b, c, vs, hp, tr, lm, mo in rows:
        core = norm_lemma(lm)
        if not core:
            continue
        kind, d = content_seg(mo, hp)
        if kind is None:
            continue
        uses[core].append((b, c, vs))
        disp.setdefault(core, (d, tr))
    joins = []
    for core, refs in uses.items():
        total = len(refs)
        if 2 <= total <= RARE_MAX:
            chaps = {(b, c) for b, c, _ in refs}
            books = {b for b, _, _ in refs}
            if len(chaps) >= 2:
                # mufneh ("free") grade: fewer distinct passages = cleaner join key
                grade = ("A-cross-book" if len(books) >= 2 else
                         "B-cross-chapter")
                joins.append((core, disp[core][0], disp[core][1], total,
                              len(chaps), len(books), grade, refs))
    joins.sort(key=lambda j: (j[6], j[3]))
    return joins


# -------------------------------------------------------------- chain side --

def chain_invocations():
    """Scan every cached Oral source for rule-announcement formulas."""
    files = sorted(glob.glob(str(CACHE / "*.json")))
    hits = []
    for f in files:
        try:
            d = json.load(open(f))
        except Exception:
            continue
        ref = d.get("ref") or Path(f).stem
        he = d.get("he", "")
        if isinstance(he, list):
            he = " ".join(x if isinstance(x, str) else " ".join(map(str, x))
                          for x in he)
        text = strip_points(re.sub(r"<[^>]+>", "", he or ""))
        for book, rule, needles in FORMULAS:
            for n in needles:
                for m in re.finditer(re.escape(n), text):
                    s = max(0, m.start() - 50)
                    snippet = text[s:m.end() + 70].replace("|", " ")
                    hits.append((ref, book, rule, n, snippet.strip()))
                    break   # one hit per needle per source is enough
    return files, hits


# -------------------------------------------------------------- persistence --

def write_tables(con, joins, hits):
    con.executescript("""
        DROP TABLE IF EXISTS middot_joins;
        CREATE TABLE middot_joins (lemma TEXT, display_he TEXT, translit TEXT,
            total INT, n_chapters INT, n_books INT, grade TEXT, refs TEXT);
        DROP TABLE IF EXISTS middot_invocations;
        CREATE TABLE middot_invocations (source_ref TEXT, rulebook TEXT,
            middah TEXT, formula TEXT, snippet TEXT);
    """)
    con.executemany("INSERT INTO middot_joins VALUES (?,?,?,?,?,?,?,?)",
                    [(l, d, t, tot, nc, nb, g,
                      json.dumps([f"{b} {c}:{v}" for b, c, v in refs]))
                     for l, d, t, tot, nc, nb, g, refs in joins])
    con.executemany("INSERT INTO middot_invocations VALUES (?,?,?,?,?)", hits)
    con.commit()


def write_reports(con, joins, files, hits):
    # ---- joins report
    lines = ["# Candidate verbal-analogy join keys (gezerah shavah, \"equal decree\")",
             "",
             "Machine-surfaced substrates ONLY (observation tier): rare lemmas "
             "(dictionary words) shared across separate passages. A join becomes "
             "meaningful only where the chain applied it (see invocations/"
             "calibration). Grade A = spans books; grade B = spans chapters. "
             f"Rarity cap: {RARE_MAX} total occurrences.", "",
             "lemma | form | translit (English added where known in calibration) "
             "| total | chapters | books | grade | refs",
             "------|------|----------|-------|----------|-------|-------|-----"]
    for l, d, t, tot, nc, nb, g, refs in joins[:200]:
        rf = ", ".join(f"{b} {c}:{v}" for b, c, v in refs[:8])
        more = f" +{len(refs)-8}" if len(refs) > 8 else ""
        lines.append(f"{l} | {d} | {t} | {tot} | {nc} | {nb} | {g} | {rf}{more}")
    lines.append(f"\nTotal candidates: {len(joins)} "
                 f"(showing first 200, grade order).")
    (OUT / "MIDDOT_joins_torah.md").write_text("\n".join(lines), encoding="utf-8")

    # ---- invocations report (with triage join)
    tri = {r[0]: (r[1], r[2]) for r in con.execute(
        "SELECT source_ref, unit, verdict_class FROM triage")}
    lines = ["# Chain-side rule invocations found in the local cache", "",
             f"Cache scanned: {len(files)} files (coverage is bounded by what we "
             "have fetched — honest counter). A hit means the source announces a "
             "rule by formula; it does NOT mean the rule bears on our verses — "
             "see the calibration report for that join. Rulebook column: 13 = "
             "Rabbi Yishmael's law-side rules; 32 = R. Eliezer b. R. Yose the "
             "Galilean's narrative-side (aggadah, \"telling\") rules; shared = "
             "both lists; operator = midrashic citation/alternation operators.",
             "",
             "source | book | rule (glossed) | formula | in triage? | snippet",
             "-------|------|----------------|---------|------------|--------"]
    for ref, book, rule, n, snip in sorted(hits):
        t = tri.get(ref)
        tcol = f"{t[0]} ({t[1]})" if t else "not yet triaged"
        lines.append(f"{ref} | {book} | {rule} | {n} | {tcol} | …{snip}…")
    by_book = Counter(h[1] for h in hits)
    lines.append(f"\nTotal invocations: {len(hits)} across "
                 f"{len({h[0] for h in hits})} sources. By rulebook: " +
                 " · ".join(f"{k}: {v}" for k, v in sorted(by_book.items())))
    (OUT / "MIDDOT_invocations_cached.md").write_text("\n".join(lines),
                                                      encoding="utf-8")


def main():
    con = sqlite3.connect(str(DB))
    joins = corpus_joins(con)
    files, hits = chain_invocations()
    write_tables(con, joins, hits)
    write_reports(con, joins, files, hits)
    in_triage = sum(1 for h in hits if con.execute(
        "SELECT 1 FROM triage WHERE source_ref=?", (h[0],)).fetchone())
    print(f"joins: {len(joins)} candidate keys "
          f"({sum(1 for j in joins if j[6].startswith('A'))} cross-book)")
    print(f"invocations: {len(hits)} formula hits in "
          f"{len({h[0] for h in hits})} of {len(files)} cached sources; "
          f"{in_triage} hits are in already-triaged sources")
    con.close()


if __name__ == "__main__":
    main()
