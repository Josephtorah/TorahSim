#!/usr/bin/env python3
"""DISPOSABLE learning-pass scanner (branch brian-speed-test).

Sweeps the DB (verses/words: OSHB morph + Strong-style lemmas) and emits, per book:
  <BOOK>_digest.md   — per-chapter pattern census (moods, fixtures, tempo) + new/read symbol ratio
  <BOOK>_symbols.md  — the compiler view: content lemmas as symbols, defined-at vs read-at
  <BOOK>_formulas.md — repeated word-sequences (formula concordance) + preset lemma trails

NOT logic. No unit YAML is produced or touched. Survey only (Pre-Code safe).
"""
import argparse
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "torah_grok.sqlite"
OUT = ROOT / "DISPOSABLE_scan"

BOOK_ORDER = ["Gen", "Exod", "Lev", "Num", "Deut"]


def norm_lemma(lemma):
    """'c/7235 a' -> '7235 a'; 'b/7225' -> '7225'; 'l' -> None (pure particle)."""
    if not lemma:
        return None
    core = lemma.split("/")[-1].strip()
    return core if re.match(r"\d", core) else None


def content_seg(morph, he_plain):
    """Return (kind, display) for the content segment of a word.
    kind: 'V' verb, 'Nc' common noun, 'Np' proper noun, None otherwise."""
    if not morph:
        return None, None
    segs = morph[1:].split("/")  # drop leading language 'H'
    toks = (he_plain or "").split("/")
    for i, s in enumerate(segs):
        if s and s[0] in ("V", "N"):
            disp = toks[i] if i < len(toks) else (he_plain or "")
            kind = "V" if s[0] == "V" else ("Np" if s.startswith("Np") else "Nc")
            return kind, disp
    return None, None


def verb_codes(morph):
    """All verb code segments in a morph string (e.g. ['Vqw3ms'])."""
    if not morph:
        return []
    return [s for s in morph[1:].split("/") if s.startswith("V")]


def load(book):
    con = sqlite3.connect(str(DB))
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT v.chapter c, v.verse vs, v.osis_id osis, w.idx, w.he_plain hp,"
        " w.translit tr, w.lemma lm, w.morph mo"
        " FROM words w JOIN verses v ON v.id=w.verse_id"
        " WHERE v.book=? ORDER BY v.chapter, v.verse, w.idx", (book,)).fetchall()
    con.close()
    return rows


# ---------------------------------------------------------------- digest ----

FIX_LEMMAS = {"1254": "bara", "6213": "asah", "3335": "yatzar", "7121": "qara",
              "1288": "berakh", "8435": "toledot", "559": "amar", "1696": "dibber"}


def scan_book(book):
    rows = load(book)
    chapters = defaultdict(list)
    for r in rows:
        chapters[r["c"]].append(r)

    # ---- symbol table over the whole book ----
    first_seen = {}            # lemma -> (chap, verse, kind, display)
    uses = defaultdict(list)   # lemma -> [(chap, verse)]
    for r in rows:
        lm = norm_lemma(r["lm"])
        if not lm:
            continue
        kind, disp = content_seg(r["mo"], r["hp"])
        if kind is None:
            continue
        if lm not in first_seen:
            first_seen[lm] = (r["c"], r["vs"], kind, disp)
        uses[lm].append((r["c"], r["vs"]))

    # ---- per-chapter census ----
    digest = []
    for c in sorted(chapters):
        ws = chapters[c]
        vt = len({w["vs"] for w in ws})
        cnt = Counter()
        for i, w in enumerate(ws):
            mo, hp = w["mo"] or "", w["hp"] or ""
            for vcode in verb_codes(mo):
                a = vcode[2] if len(vcode) > 2 else ""
                cnt["wayyiqtol"] += a == "w"
                cnt["jussive_LET"] += a == "j"
                cnt["imperative_CMD"] += a == "v"
                cnt["cohortative"] += a == "h"
                cnt["weqatal_THEN"] += a == "q"
                cnt["participle"] += a == "r"
            cnt["et_marker"] += "To" in mo
            lm = norm_lemma(w["lm"])
            core = lm.split()[0] if lm else ""
            if core in FIX_LEMMAS and verb_codes(mo):
                cnt[FIX_LEMMAS[core]] += 1
            if core == "8435":
                cnt["toledot"] += 1
            # token fixtures (bigrams)
            if hp.endswith("יהי") and i + 1 < len(ws):
                nxt = ws[i + 1]["hp"]
                if nxt == "כן" and ws[i + 1]["vs"] == w["vs"]:
                    cnt["va_yehi_khen"] += 1
                if nxt == "ערב":
                    cnt["commit_formula"] += 1
            if hp == "כי" and i + 1 < len(ws) and ws[i + 1]["hp"].endswith("טוב"):
                cnt["ki_tov"] += 1
        new_syms = [lm for lm, fs in first_seen.items() if fs[0] == c]
        reads = sum(1 for w in ws
                    if (lambda l: l and l in first_seen and first_seen[l][0] < c)
                    (norm_lemma(w["lm"])))
        content_total = sum(1 for w in ws if content_seg(w["mo"], w["hp"])[0])
        digest.append((c, vt, cnt, len(new_syms), reads, content_total, new_syms))
    return rows, chapters, first_seen, uses, digest


def write_digest(book, digest, first_seen):
    lines = [f"# {book} — chapter digest (DISPOSABLE learning pass)\n",
             "chap | vv | wayyiqtol | LET(j) | CMD!(v) | LET?/impf-cands | THEN(q) | "
             "ptc | et | bara | asah | qara | berakh | yehi-khen | ki-tov | commit | "
             "toledot | NEW syms | read% ",
             "-----|----|-----------|--------|---------|------------------|---------|"
             "----|----|------|------|------|--------|-----------|--------|--------|"
             "---------|----------|------"]
    for c, vt, cnt, nnew, reads, ctot, _ in digest:
        readpct = f"{100*reads//max(1,ctot)}%"
        lines.append(
            f"{c} | {vt} | {cnt['wayyiqtol']} | {cnt['jussive_LET']} | "
            f"{cnt['imperative_CMD']} | — | {cnt['weqatal_THEN']} | {cnt['participle']} | "
            f"{cnt['et_marker']} | {cnt['bara']} | {cnt['asah']} | {cnt['qara']} | "
            f"{cnt['berakh']} | {cnt['va_yehi_khen']} | {cnt['ki_tov']} | "
            f"{cnt['commit_formula']} | {cnt['toledot']} | {nnew} | {readpct}")
    lines.append("\nNotes: LET?/imperfect-in-command needs speech-context detection — "
                 "see formulas file for speech spans; read% = share of content words "
                 "whose lemma was first seen in an EARLIER chapter (the 'reads prior "
                 "output' ratio). NEW syms = lemmas making their book-debut here.")
    (OUT / f"{book}_digest.md").write_text("\n".join(lines), encoding="utf-8")


def write_symbols(book, first_seen, uses):
    lines = [f"# {book} — symbol table (defined-at / read-at) — DISPOSABLE\n"]
    # chapter-1 installs and their afterlife
    lines.append("## Chapter 1 installs and their afterlife\n")
    lines.append("lemma | form | kind | defined | later uses | later chapters")
    lines.append("------|------|------|---------|------------|---------------")
    ch1 = [(lm, fs) for lm, fs in first_seen.items() if fs[0] == 1]
    ch1.sort(key=lambda x: -len(uses[x[0]]))
    for lm, (c, v, kind, disp) in ch1[:60]:
        later = [(cc, vv) for cc, vv in uses[lm] if cc > 1]
        chs = sorted({cc for cc, _ in later})
        span = (f"{chs[0]}–{chs[-1]}" if chs else "—")
        lines.append(f"{lm} | {disp} | {kind} | 1:{v} | {len(later)} | "
                     f"{len(chs)} chs ({span})")
    # long-range rare reads
    lines.append("\n## Long-range rare reads (defined once early, read far later, <10 uses)\n")
    lines.append("lemma | form | defined | uses (all refs)")
    lines.append("------|------|---------|----------------")
    rare = []
    for lm, (c, v, kind, disp) in first_seen.items():
        us = uses[lm]
        if 2 <= len(us) <= 9:
            chs = sorted({cc for cc, _ in us})
            if len(chs) >= 2 and chs[-1] - chs[0] >= 5:
                rare.append((chs[-1] - chs[0], lm, disp, c, v, us))
    rare.sort(reverse=True)
    for span, lm, disp, c, v, us in rare[:80]:
        refs = ", ".join(f"{cc}:{vv}" for cc, vv in us)
        lines.append(f"{lm} | {disp} | {c}:{v} | {refs}")
    (OUT / f"{book}_symbols.md").write_text("\n".join(lines), encoding="utf-8")


TRAILS = {
    "pru-u-rvu mandate (6509 parah + 7235 ravah adjacent)": ("6509", "7235"),
    "sharatz swarm (8317)": ("8317",),
    "bara creation verb (1254)": ("1254",),
    "tehom the deep (8415)": ("8415",),
    "tov-test collocation (7200 raah + 2896 tov same verse)": ("7200", "2896"),
    "qara-shem naming (7121 + 8034 same verse)": ("7121", "8034"),
    "toledot headers (8435)": ("8435",),
}


def write_formulas(book, rows, uses):
    lines = [f"# {book} — formula concordance + lemma trails — DISPOSABLE\n"]
    # preset trails
    lines.append("## Preset trails (later code re-running earlier formulas)\n")
    verse_lemmas = defaultdict(set)
    for r in rows:
        lm = norm_lemma(r["lm"])
        if lm:
            verse_lemmas[(r["c"], r["vs"])].add(lm.split()[0])
    for title, needles in TRAILS.items():
        hits = sorted(k for k, s in verse_lemmas.items()
                      if all(any(x == n or x.startswith(n + " ") for x in s)
                             for n in needles))
        refs = ", ".join(f"{c}:{v}" for c, v in hits)
        lines.append(f"- **{title}** — {len(hits)} verses: {refs}")
    # n-gram concordance (consonantal, word-level)
    lines.append("\n## Repeated word-sequences (4-grams in ≥2 chapters, ≤12 total hits)\n")
    toks = [(r["c"], r["vs"], (r["hp"] or "").replace("/", "")) for r in rows]
    grams = defaultdict(list)
    for i in range(len(toks) - 3):
        window = toks[i:i + 4]
        if any(t[0] != window[0][0] or t[1] != window[0][1] for t in window):
            continue  # keep n-grams verse-internal
        g = " ".join(t[2] for t in window)
        grams[g].append((window[0][0], window[0][1]))
    scored = []
    for g, refs in grams.items():
        chs = {c for c, _ in refs}
        if len(refs) >= 2 and len(chs) >= 2 and len(refs) <= 12:
            scored.append((len(chs), len(refs), g, refs))
    scored.sort(reverse=True)
    for nch, nref, g, refs in scored[:70]:
        rf = ", ".join(f"{c}:{v}" for c, v in refs[:10])
        lines.append(f"- `{g}` — {nref}x in {nch} chs: {rf}")
    (OUT / f"{book}_formulas.md").write_text("\n".join(lines), encoding="utf-8")


CROSS_TRAILS = dict(TRAILS)
CROSS_TRAILS.update({
    "brit covenant (1285)": ("1285",),
    "shabbat rest (7676 or verb 7673)": ("7676",),
    "tzelem image (6754)": ("6754",),
    "mabbul flood (3999)": ("3999",),
})


def scan_torah_crossbook():
    """Torah-wide symbol table: which books define, which books read."""
    first_seen = {}                 # lemma -> (book, chap, verse, disp)
    uses = defaultdict(list)        # lemma -> [(book, chap, verse)]
    book_stats = []
    for book in BOOK_ORDER:
        rows = load(book)
        tokens = 0
        reads_earlier = 0
        new_here = set()
        for r in rows:
            lm = norm_lemma(r["lm"])
            if not lm:
                continue
            kind, disp = content_seg(r["mo"], r["hp"])
            if kind is None:
                continue
            tokens += 1
            if lm in first_seen and first_seen[lm][0] != book:
                reads_earlier += 1
            if lm not in first_seen:
                first_seen[lm] = (book, r["c"], r["vs"], disp)
                new_here.add(lm)
            uses[lm].append((book, r["c"], r["vs"]))
        book_stats.append((book, tokens, len(new_here), reads_earlier))

    lines = ["# TORAH — cross-book symbol view (DISPOSABLE learning pass)\n",
             "## Per book: content tokens, book-debut lemmas, tokens reading earlier books\n",
             "book | content tokens | NEW lemmas (book debut) | tokens reading earlier-book symbols | read%",
             "-----|----------------|-------------------------|--------------------------------------|------"]
    for book, tokens, new, reads in book_stats:
        lines.append(f"{book} | {tokens} | {new} | {reads} | {100*reads//max(1,tokens)}%")

    lines.append("\n## Cross-book trails (later books re-running earlier formulas)\n")
    verse_lemmas = defaultdict(set)
    for book in BOOK_ORDER:
        for r in load(book):
            lm = norm_lemma(r["lm"])
            if lm:
                verse_lemmas[(book, r["c"], r["vs"])].add(lm.split()[0])
    order = {b: i for i, b in enumerate(BOOK_ORDER)}
    for title, needles in CROSS_TRAILS.items():
        hits = sorted((k for k, s in verse_lemmas.items()
                       if all(n in s for n in needles)),
                      key=lambda k: (order[k[0]], k[1], k[2]))
        by_book = Counter(b for b, _, _ in hits)
        dist = " · ".join(f"{b}:{by_book[b]}" for b in BOOK_ORDER if by_book[b])
        sample = ", ".join(f"{b} {c}:{v}" for b, c, v in hits[:14])
        more = f" … +{len(hits)-14}" if len(hits) > 14 else ""
        lines.append(f"- **{title}** — {len(hits)} verses ({dist}): {sample}{more}")

    lines.append("\n## Genesis-1 installs read by ALL five books\n")
    lines.append("lemma | form | defined | Gen | Exod | Lev | Num | Deut")
    lines.append("------|------|---------|-----|------|-----|-----|-----")
    g1 = [(lm, fs) for lm, fs in first_seen.items()
          if fs[0] == "Gen" and fs[1] == 1]
    rows_out = []
    for lm, (b, c, v, disp) in g1:
        per = Counter(bb for bb, _, _ in uses[lm])
        if all(per[bb] for bb in BOOK_ORDER):
            rows_out.append((sum(per.values()), lm, disp, v, per))
    rows_out.sort(reverse=True)
    for tot, lm, disp, v, per in rows_out[:40]:
        lines.append(f"{lm} | {disp} | Gen 1:{v} | " +
                     " | ".join(str(per[bb]) for bb in BOOK_ORDER))
    (OUT / "TORAH_crossbook.md").write_text("\n".join(lines), encoding="utf-8")
    print("TORAH cross-book view -> DISPOSABLE_scan/TORAH_crossbook.md")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", default="Gen", choices=BOOK_ORDER + ["all"])
    args = ap.parse_args()
    books = BOOK_ORDER if args.book == "all" else [args.book]
    for book in books:
        rows, chapters, first_seen, uses, digest = scan_book(book)
        write_digest(book, digest, first_seen)
        write_symbols(book, first_seen, uses)
        write_formulas(book, rows, uses)
        print(f"{book}: {len(chapters)} chapters · {len(rows)} words · "
              f"{len(first_seen)} distinct content lemmas -> DISPOSABLE_scan/")
    if args.book == "all":
        scan_torah_crossbook()


if __name__ == "__main__":
    main()
