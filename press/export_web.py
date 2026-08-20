#!/usr/bin/env python3
"""
export_web.py — SERVE-layer exporter: derivation.sqlite -> web/scroll/data/
  manifest.json            book/chapter/verse map + build provenance
  <Book>_<chapter>.json    one bundle per chapter (whole Torah, 187 bundles)

Derived artifact like the DB itself: never hand-edited, regenerate at will.
Reuses render_flat_ledger_from_db.py (which reuses the original renderer) so
grammar text, froze-reasons and code lines have a single source of truth.

Usage: python3 export_web.py            (whole Torah, ~30s)
"""

import importlib.util
import json
import sqlite3
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ["TS_OUT"]) if os.environ.get("TS_OUT") \
    else ROOT / "scroll" / "data"

_spec = importlib.util.spec_from_file_location(
    "rdb", ROOT / "press" / "render_flat_ledger_from_db.py")
RDB = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(RDB)

BOOKS = ["Gen", "Exod", "Lev", "Num", "Deut"]
BOOK_NAMES = {"Gen": "Genesis", "Exod": "Exodus", "Lev": "Leviticus",
              "Num": "Numbers", "Deut": "Deuteronomy"}


def load_jps(shape):
    """JPS 1917 (public domain, Data/tanakh_*_jps1917_en.json) keyed (book, ch).
    A chapter is used ONLY if its verse count matches the DB exactly — the three
    Decalogue-region chapters (Exod 20, Num 25, Deut 5) merge verses in JPS's
    digitization, and a misaligned translation is worse than none (flag, never
    fake). Skipped chapters fall back to the word-gloss chain in the app."""
    jps, skipped = {}, []
    for b in BOOKS:
        path = ROOT / "shelf" / "sources" / ("tanakh_%s_jps1917_en.json" % BOOK_NAMES[b].lower())
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for i, ch_text in enumerate(data["text"], 1):
            if shape[b].get(i) == len(ch_text):
                jps[(b, i)] = ch_text
            else:
                skipped.append("%s %d (DB %s vs JPS %d)"
                               % (b, i, shape[b].get(i), len(ch_text)))
    if skipped:
        print("JPS versification skip (gloss-chain fallback): " + "; ".join(skipped))
    return jps


def build_search_index(cx, jps):
    """data/search.json — one entry per verse: unpointed Hebrew, translit,
    glosses, JPS English. Loaded lazily by the app on first search (~2.5 MB)."""
    acc = {}
    for r in cx.execute("""SELECT v.book b, v.chapter c, v.verse v,
                                  w.he_plain, w.translit, w.gloss
                           FROM words w JOIN verses v ON w.verse_id = v.id
                           ORDER BY v.id, w.idx"""):
        e = acc.setdefault((r["b"], r["c"], r["v"]), {"he": [], "tr": [], "en": []})
        e["he"].append((r["he_plain"] or "").replace("/", ""))
        e["tr"].append(r["translit"] or "")
        e["en"].append(r["gloss"] or "")
    out = []
    for key in sorted(acc, key=lambda k: (BOOKS.index(k[0]), k[1], k[2])):
        b, c, v = key
        ch_jps = jps.get((b, c))
        out.append({"b": b, "c": c, "v": v,
                    "he": " ".join(x for x in acc[key]["he"] if x),
                    "tr": " ".join(x for x in acc[key]["tr"] if x),
                    "en": " ".join(x for x in acc[key]["en"] if x),
                    "fen": ch_jps[v - 1] if ch_jps else ""})
    path = OUT / "search.json"
    path.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print("search.json: %d verses, %.1f MB" % (len(out), path.stat().st_size / 1e6))


def code_lines(d):
    """Same mapping as the report's code_section, structured for JSON."""
    lines = []
    for lf in d["leaves"]:
        role = lf["role"] or ""
        head, _, rest = role.partition("(")
        arg = rest.rstrip(")")
        tag = RDB.leaf_verb_tag(d, lf)
        cmt = "# B%d %s — %s%s" % (lf["b_index"], lf["translit"], lf["en"], tag)
        if head in RDB.ROLE_EMIT:
            code = RDB.ROLE_EMIT[head](arg)
            if head in RDB.TIR_NOTE:
                cmt += "  [%s]" % RDB.TIR_NOTE[head]
        elif head in RDB.EVENT_ROLES:
            verb = head.split("/")[0].lower()
            code = 'EVENT("%s"%s)' % (verb, ', "%s"' % arg if arg else "")
        else:
            code = "pass"
            if role:
                cmt += "  (context: %s)" % role
        lines.append({"c": code, "m": cmt})
    return lines


def verse_json(d, frozen_rows, fen, oral=None):
    words, leaves = d["words"], d["leaves"]
    out = {"v": d["verse"]["verse"], "osis": d["osis"],
           "sys": d["verse"]["system"], "status": d["tree"]["status"],
           "fen": fen,
           "frozen": ["%s · %s (%s)" % (r["unit_id"], r["step_id"], r["op"])
                      for r in (frozen_rows or [])]}
    if oral:
        out["oral"] = oral  # [enumerated, read, material] — honest counters
    out["leaves"] = []
    for lf in leaves:
        ws, we = lf["w_start"], lf["w_end"]
        out["leaves"].append({
            "b": lf["b_index"],
            "w": "w%d" % ws if ws == we else "w%d–%d" % (ws, we),
            "path": lf["path"], "he": lf["he"], "tr": lf["translit"],
            "en": lf["en"], "mark": lf["end_mark"], "rank": lf["rank"],
            "froze": RDB.froze_because(words, ws, we),
            "role": lf["role"] or ""})
    out["morph"] = []
    for lf in leaves:
        first = True
        for wi in range(lf["w_start"], lf["w_end"] + 1):
            segs = d["segs"][wi]
            main_idx = RDB.main_seg_idx(segs)
            for s in segs:
                wlab = str(wi) if len(segs) == 1 \
                    else "%d%s" % (wi, chr(ord("a") + s["seg_idx"]))
                out["morph"].append({
                    "b": lf["b_index"], "bs": first, "w": wlab,
                    "he": s["he"], "tr": s["translit"], "en": s["gloss"] or "",
                    "code": s["morph_seg"] or "",
                    "g": RDB.grammar_text(s, s["seg_idx"] == main_idx)})
                first = False
    out["code"] = code_lines(d)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cx = sqlite3.connect(str(RDB.DB))
    cx.row_factory = sqlite3.Row
    meta = dict(cx.execute("SELECT key, value FROM meta"))

    frozen_steps = {}
    for r in cx.execute("""SELECT s.ref, s.unit_id, s.step_id, s.op FROM steps s
                           JOIN units u ON u.unit_id = s.unit_id
                           WHERE u.status = 'frozen' AND s.ref IS NOT NULL"""):
        frozen_steps.setdefault(r["ref"], []).append(r)

    shape = {}   # book -> {chapter: verse_count}
    for r in cx.execute("""SELECT book, chapter, COUNT(*) n FROM verses
                           GROUP BY book, chapter"""):
        shape.setdefault(r["book"], {})[r["chapter"]] = r["n"]

    # per-verse Oral triage counts: [enumerated, read, material] — the three
    # honest numbers, derived from oral_links (anchors) x triage (verdicts).
    oral_counts = {}
    try:
        for osis, e, rd, m in cx.execute("""
                SELECT ol.anchor_osis,
                       COUNT(DISTINCT ol.source_ref),
                       COUNT(DISTINCT t.source_ref),
                       COUNT(DISTINCT CASE WHEN t.verdict_class = 'material'
                                           THEN t.source_ref END)
                FROM oral_links ol
                LEFT JOIN triage t ON t.source_ref = ol.source_ref
                WHERE ol.tier = 1
                GROUP BY ol.anchor_osis"""):
            oral_counts[osis] = [e, rd, m]
    except sqlite3.OperationalError:
        pass  # oral_links / triage not built yet -> no badges

    jps = load_jps(shape)
    build_search_index(cx, jps)
    if "--search-only" in sys.argv:
        return

    manifest = {"built_at": meta.get("built_at"),
                "taamim": meta.get("taamim_rule_version"),
                "roles": meta.get("role_ruleset"),
                "lexicon": meta.get("lexicon_version"),
                "translation": "The Holy Scriptures (JPS 1917, public domain)"
                               if jps else None,
                "verses_total": int(meta.get("verses", 0)),
                "books": [{"id": b, "name": BOOK_NAMES[b],
                           "chapters": [shape[b][c]
                                        for c in sorted(shape[b])]}
                          for b in BOOKS]}
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False), encoding="utf-8")

    n_ch = n_v = 0
    for b in BOOKS:
        for ch in sorted(shape[b]):
            verses = []
            for v in range(1, shape[b][ch] + 1):
                d = RDB.fetch_verse(cx, b, ch, v)
                if d is None:
                    continue
                ch_jps = jps.get((b, ch))
                fen = ch_jps[v - 1] if ch_jps else (
                    RDB.VERSE_EN.get((ch, v)) if b == "Gen" else None)
                verses.append(verse_json(d, frozen_steps.get(d["osis"]), fen,
                                         oral_counts.get(d["osis"])))
                n_v += 1
            (OUT / ("%s_%d.json" % (b, ch))).write_text(
                json.dumps({"book": b, "chapter": ch, "verses": verses},
                           ensure_ascii=False), encoding="utf-8")
            n_ch += 1
        print("%s: %d chapters" % (b, len(shape[b])))

    size = sum(f.stat().st_size for f in OUT.glob("*.json")) / 1e6
    print("wrote %d bundles · %d verses · %.1f MB -> %s" % (n_ch, n_v, size, OUT))


if __name__ == "__main__":
    main()
