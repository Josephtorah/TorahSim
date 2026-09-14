#!/usr/bin/env python3
"""build_plain_outline.py — the program in plain English, one bullet per verse.

Same walk as build_program_outline.py (every frozen unit, canonical
order), but each step is said in plain words: the verse, then what the
machine does with it, then what the teacher's shelf adds, then what was
checked against the letters. No operator syntax.

Read-only over the repository. Writes ONLY into ARCHITECTURE/program/:
  PLAIN_OUTLINE.md      the index
  PLAIN_GENESIS.md, PLAIN_EXODUS.md, PLAIN_LEVITICUS.md
  PLAIN_OUTLINE.html    one page, collapsible, searchable

    python3 ARCHITECTURE/tools/build_plain_outline.py

Where a unit gives no English for a verse (the tree-split steps), the
verse is shown word by word from the word database's own glosses and
marked as such.
"""
import html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_program_outline as base   # shares the loaders and glossers (read-only)
from build_program_outline import (ROOT, OUT, BOOK, ref_str, clean_en, shorten, load_manifest,
                                   norm_ref_key, gloss_translits, gloss_jargon, gloss_hebrew_runs,
                                   compiled_for, cw, gloss_db)

KEEP_CAPS = {"LORD", "GOD", "YHWH", "I", "A", "TIR", "PASS", "FAIL", "OK", "MS", "DB", "SNAPSHOT"}


def unshout(text):
    """ALL-CAPS emphasis -> ordinary case (ids and acronyms kept)"""
    def rep(m):
        w = m.group(0)
        if w in KEEP_CAPS or any(ch.isdigit() for ch in w) or "-" in w:
            return w
        return w.lower()
    out = re.sub(r"\b[A-Z][A-Z'’]+\b", rep, text)
    return out[:1].upper() + out[1:] if out else out


def plural(n, word):
    return "%d %s%s" % (n, word, "" if n == 1 else ("s" if not word.endswith("y") else ""))


def first_sentence(text, n=170):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    text = re.sub(r"^\s*\[[^\]]*\]\s*", "", text)          # leading [tags]
    m = re.search(r"[.;](\s|$)", text[:n + 60])
    if m and m.start() > 25:
        text = text[:m.start() + 1]
    return shorten(text, n)


def word_by_word(ref):
    try:
        ws = gloss_db.verse_words(ref.replace(" ", ".").replace(":", "."))
    except Exception:
        ws = []
    ens = [str(w[2]) for w in ws if w and w[2]]
    return " ".join(ens) if ens else ""


def parse_items(expr):
    m = re.search(r"\{([^}]*)\}", expr or "")
    return [x.strip() for x in m.group(1).split(",")] if m else []


def plain_ops(ops, gmap, seen):
    """operators -> list of plain clauses (machine) and shelf notes"""
    clauses, notes = [], []
    for o in ops:
        op = str(o.get("op") or "")
        ex = str(o.get("expr_en") or "")
        en = str(o.get("en") or "")
        g = lambda t: gloss_translits(t, gmap, seen)
        if op == "TIME_ANCHOR":
            clauses.append("starts the clock")
        elif op == "EVENT":
            m = re.search(r"Agent\(\w+,\s*([^)]+)\)", ex)
            clauses.append("records an act" + (" by " + g(m.group(1).strip()) if m else ""))
        elif op == "REGISTRY_INSTALL":
            items = parse_items(ex)
            clauses.append("adds to the world: " + ", ".join(g(i) for i in items) if items else "adds new things to the world")
        elif op == "PRECONDITION_STATE":
            clauses.append("holds this verse as a standing fact")
        elif op == "INVARIANT":
            clauses.append("keeps this condition true throughout")
        elif op == "DECLARE":
            clauses.append("a command is issued" + (" by God" if "Elohim" in ex or "YHWH" in ex else ""))
        elif op == "RESULT":
            clauses.append("the command is fulfilled and receipted")
        elif op == "TEST":
            clauses.append("the result is checked and approved as good" if "tov" in ex else "the result is checked")
        elif op == "NAME":
            pairs = re.findall(r"name\(([^)]+)\)\s*:=\s*([\w'\-]+)", ex)
            if pairs:
                clauses.append("gives names: " + "; ".join("%s is called %s" % (g(a), g(b)) for a, b in pairs))
            else:
                clauses.append("gives a name")
        elif op == "COMMIT":
            clauses.append("closes the day's ledger")
        elif op == "EVENT_PARTITION":
            clauses.append("divides one thing from another")
        elif op == "ORAL_UTTERANCE":
            m = re.search(r"UTTERANCE\((\d+)", ex)
            clauses.append("counted as utterance %s of the ten" % m.group(1) if m else "its place among the ten utterances is disputed")
        elif op == "CASE":
            m = re.search(r"ROUTE\(([^)]+)\)", ex)
            clauses.append("opens a case for this situation" + (", filed under " + g(m.group(1).replace("_", " ")) if m else ""))
        elif op == "HANDLER":
            clauses.append("installs a rule: when this verse's condition holds, its consequence follows")
        elif op == "STATUTE":
            if "FORBID" in ex:
                clauses.append("installs a standing prohibition")
            elif "BIND" in ex:
                clauses.append("installs a standing duty")
            else:
                clauses.append("installs a standing law")
        elif op == "BLESS":
            clauses.append("records a blessing")
        elif op == "ASSIGN":
            clauses.append("records an assignment")
        elif op == "SECTION":
            clauses.append("marks a section boundary")
        elif op == "PATTERN":
            clauses.append("notes a repeating pattern")
        elif op == "NOTE_PRESUPPOSED":
            clauses.append("flags something read here before it was ever introduced")
        elif op == "NOTE_SPEC_DELTA":
            clauses.append("flags a difference between what was ordered and what was delivered")
        elif op == "NOTE_ZERO_EVENTS":
            clauses.append("notes that nothing happens in this verse; it only sets the scene")
        elif op in ("WITNESS_READ", "WITNESS_STATE"):
            notes.append(unshout(first_sentence(en or ex, 190)))
        # TRIPLE and unknown internal ops are not said aloud
    # de-duplicate while keeping order
    out = []
    for c in clauses:
        if c not in out:
            out.append(c)
    return out, notes


def unit_plain(uid, d):
    meta = d.get("meta", {})
    steps = d.get("boot_steps") or []
    refs = [s.get("ref") for s in steps if s.get("ref")]
    try:
        gmap = gloss_db.build_translit_gloss(refs)
    except Exception:
        gmap = {}
    seen, seen_j = set(), set()
    manifest = load_manifest(uid)
    counts = {"acts": 0, "facts": 0, "commands": 0, "laws": 0, "cases": 0, "rules": 0, "names": 0, "commits": 0}
    rows = []
    for s in steps:
        ops = s.get("operators") or []
        for o in ops:
            op = o.get("op"); ex = str(o.get("expr_en") or "")
            if op == "EVENT": counts["acts"] += 1
            elif op == "PRECONDITION_STATE": counts["facts"] += 1
            elif op == "DECLARE": counts["commands"] += 1
            elif op == "STATUTE": counts["laws"] += 1
            elif op == "CASE": counts["cases"] += 1
            elif op == "HANDLER": counts["rules"] += 1
            elif op == "NAME": counts["names"] += 1
            elif op == "COMMIT": counts["commits"] += 1
        verse_en = clean_en(s.get("en"))
        wbw = False
        if not verse_en:
            verse_en = word_by_word(str(s.get("ref") or "")); wbw = True
        clauses, notes = plain_ops(ops, gmap, seen)
        claims = manifest.get(norm_ref_key(s.get("ref")), [])
        plain_claims = [gloss_jargon(gloss_translits(gloss_hebrew_runs(unshout(first_sentence(c.get("claim_en"), 200)), s.get("ref")), gmap, seen), seen_j)
                        for c in claims[:4]]
        extra = max(0, len(claims) - 4)
        rows.append({"ref": ref_str(s.get("ref")), "verse": gloss_jargon(verse_en, seen_j), "wbw": wbw,
                     "does": clauses,
                     "notes": [gloss_jargon(gloss_translits(gloss_hebrew_runs(n, s.get("ref")), gmap, seen), seen_j) for n in notes[:3]],
                     "claims": plain_claims, "extra": extra})
    step_keys = {norm_ref_key(s.get("ref")) for s in steps}
    unanchored = [c for k, cl in manifest.items() if k not in step_keys for c in cl]
    after = [a.get("en") for a in (d.get("state_after") or []) if a.get("en") and not str(a.get("en")).startswith("Tree-derived")]
    exports = [e.get("en") for e in (d.get("exports") or []) if e.get("en") and not str(e.get("en")).startswith(("Joseph-cycle span", "Tree-derived"))]
    summary = []
    if counts["acts"]: summary.append("records " + plural(counts["acts"], "act"))
    if counts["commands"]: summary.append("issues " + plural(counts["commands"], "command"))
    if counts["facts"]: summary.append("sets " + plural(counts["facts"], "standing fact"))
    if counts["names"]: summary.append("gives " + plural(counts["names"], "name"))
    if counts["commits"]: summary.append("closes " + ("1 ledger day" if counts["commits"] == 1 else "%d ledger days" % counts["commits"]))
    if counts["cases"]: summary.append("opens " + plural(counts["cases"], "case"))
    if counts["rules"]: summary.append("installs " + plural(counts["rules"], "rule"))
    if counts["laws"]: summary.append("installs " + plural(counts["laws"], "standing law"))
    n_claims = sum(len(v) for v in manifest.values())
    header = {"uid": uid, "title": unshout(str(meta.get("title_en") or uid)), "book": BOOK.get(uid[:3], uid[:3]),
              "refs": str(meta.get("refs") or ""), "n_steps": len(steps), "summary": summary,
              "n_claims": n_claims, "compiled": compiled_for(uid),
              "after": [gloss_translits(a, gmap, seen) for a in after[:1]],
              "exports": [shorten(unshout(e), 110) for e in exports[:4]],
              "unanchored": [gloss_translits(unshout(first_sentence(c.get("claim_en"), 200)), gmap, seen) for c in unanchored[:6]]}
    return header, rows


LEGEND = ("How to read this. One bullet per verse, in order. First the verse in English (marked "
          "'word by word' where the unit itself gives no English and the words are glossed one at a time). "
          "Then what the code does with that verse: starts the clock, records an act, adds something to the "
          "world, holds a standing fact, issues or fulfils a command, gives a name, closes a day, opens a case, "
          "installs a rule, or installs a standing duty or prohibition. Then what the teacher's shelf adds at "
          "that verse. Then what was checked against the letters of the text, the unit's claims, up to four "
          "per verse. A line at the top of each unit counts what the whole span does, and names its compiled "
          "function where one exists.")


def md_unit(h, rows):
    L = ["### %s %s — %s" % (h["book"], h["refs"], h["title"]), ""]
    line = "; ".join(h["summary"]) if h["summary"] else "reads %d verses into claims" % h["n_steps"]
    line = "This span " + line + "; " + plural(h["n_claims"], "claim") + " checked against the letters."
    if h["compiled"]:
        line += " Compiled function: " + h["compiled"] + "."
    L += [line, ""]
    if h["after"]:
        L += ["Afterwards: " + h["after"][0], ""]
    for r in rows:
        L.append("- **%s** %s%s" % (r["ref"], r["verse"], " *(word by word)*" if r["wbw"] else ""))
        if r["does"]:
            L.append("  - What the code does: " + "; ".join(r["does"]) + ".")
        for n in r["notes"]:
            L.append("  - The shelf adds: " + n)
        for c in r["claims"]:
            L.append("  - Checked: " + c)
        if r["extra"]:
            L.append("  - and %d more claims checked at this verse." % r["extra"])
    if h["unanchored"]:
        L.append("- **Checked across the span**")
        for c in h["unanchored"]:
            L.append("  - " + c)
    if h["exports"]:
        L += ["", "What this span hands forward: " + "; ".join(h["exports"]) + "."]
    L.append("")
    return "\n".join(L)


def html_unit(h, rows, open_default):
    e = html.escape
    line = "; ".join(h["summary"]) if h["summary"] else "reads %d verses into claims" % h["n_steps"]
    P = ['<details class="unit"%s id="%s"><summary><b>%s %s</b> — %s<span class="counts">%s; %d claims</span>%s</summary>'
         % (" open" if open_default else "", e(h["uid"]), e(h["book"]), e(h["refs"]), e(h["title"]), e(line), h["n_claims"],
            (' <span class="compiled">compiled: %s</span>' % e(h["compiled"])) if h["compiled"] else "")]
    if h["after"]:
        P.append('<p class="after"><b>Afterwards:</b> %s</p>' % e(h["after"][0]))
    P.append("<ul>")
    for r in rows:
        P.append('<li><b>%s</b> %s%s' % (e(r["ref"]), e(r["verse"]), ' <i class="wbw">(word by word)</i>' if r["wbw"] else ""))
        if r["does"] or r["notes"] or r["claims"]:
            P.append("<ul>")
            if r["does"]:
                P.append('<li class="does"><b>What the code does:</b> %s.</li>' % e("; ".join(r["does"])))
            for n in r["notes"]:
                P.append('<li class="note"><b>The shelf adds:</b> %s</li>' % e(n))
            for c in r["claims"]:
                P.append('<li class="claim"><b>Checked:</b> %s</li>' % e(c))
            if r["extra"]:
                P.append('<li class="claim">and %d more claims checked at this verse.</li>' % r["extra"])
            P.append("</ul>")
        P.append("</li>")
    if h["unanchored"]:
        P.append("<li><b>Checked across the span</b><ul>" + "".join('<li class="claim">%s</li>' % e(c) for c in h["unanchored"]) + "</ul></li>")
    P.append("</ul>")
    if h["exports"]:
        P.append('<p class="exports"><b>What this span hands forward:</b> %s.</p>' % e("; ".join(h["exports"])))
    P.append("</details>")
    return "\n".join(P)


CSS = base.CSS.replace("li.machine code{background:#e4eedd}li.note code{background:#f7ecd0}li.claim code{background:#dde7f0}",
                       "li.does{color:#2f5d8a}li.note{color:#7a5a10}li.claim{color:#57503f;font-size:.93em}.wbw{color:#8a6d2f;font-size:.85em}")


def main():
    units = cw.frozen_units_in_canonical_order()
    outlined = [unit_plain(uid, d) for uid, d in units]
    by_book = {"Genesis": [], "Exodus": [], "Leviticus": [], "Numbers": []}
    for h, rows in outlined:
        by_book.setdefault(h["book"], []).append((h, rows))
    n_units = len(outlined); n_steps = sum(h["n_steps"] for h, _ in outlined)

    idx = ["# THE PROGRAM IN PLAIN ENGLISH — what the code does, verse by verse", "",
           "Generated 2026-09-13 from the frozen units in canonical order: %d units, %d verses." % (n_units, n_steps), "",
           LEGEND, "",
           "The verse-by-verse text is in [Genesis](PLAIN_GENESIS.md), [Exodus](PLAIN_EXODUS.md), and "
           "[Leviticus](PLAIN_LEVITICUS.md), [Numbers](PLAIN_NUMBERS.md), or all at once in [PLAIN_OUTLINE.html](PLAIN_OUTLINE.html), "
           "which folds each unit and has a search box. The same walk with the operators as the code writes "
           "them is [PROGRAM_OUTLINE.md](PROGRAM_OUTLINE.md).", ""]
    for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):
        rows = by_book.get(book, [])
        idx += ["## %s — %d units" % (book, len(rows)), "", "| Span | What it covers | What the span does | Compiled function |", "|---|---|---|---|"]
        for h, _ in rows:
            idx.append("| %s | %s | %s | %s |" % (h["refs"], h["title"].replace("|", "/"),
                                                  "; ".join(h["summary"]) or ("reads %d verses into claims" % h["n_steps"]), h["compiled"] or ""))
        idx.append("")
    open(os.path.join(OUT, "PLAIN_OUTLINE.md"), "w", encoding="utf-8").write("\n".join(idx))

    for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):
        rows = by_book.get(book, [])
        L = ["# THE PROGRAM IN PLAIN ENGLISH — %s" % book, "", LEGEND, "", "Back to the [index](PLAIN_OUTLINE.md).", ""]
        for h, r in rows:
            L.append(md_unit(h, r))
        open(os.path.join(OUT, "PLAIN_%s.md" % book.upper()), "w", encoding="utf-8").write("\n".join(L))

    H = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         "<title>The Program in Plain English</title>", CSS, "</head><body>",
         "<h1>The program in plain English: what the code does, verse by verse</h1>",
         '<p class="legend">%s</p>' % html.escape(LEGEND),
         '<p class="legend">%d units · %d verses · generated 2026-09-13 from the frozen units in canonical order.</p>' % (n_units, n_steps),
         '<nav><input id="q" placeholder="search every verse, action, note, and claim ..."> '
         '<a href="#Genesis">Genesis</a><a href="#Exodus">Exodus</a><a href="#Leviticus">Leviticus</a><a href="#Numbers">Numbers</a> '
         '<a href="#" id="openall">open all</a><a href="#" id="closeall">close all</a></nav>']
    for book in ("Genesis", "Exodus", "Leviticus", "Numbers"):
        rows = by_book.get(book, [])
        H.append('<h2 id="%s">%s — %d units</h2>' % (book, book, len(rows)))
        for i, (h, r) in enumerate(rows):
            H.append(html_unit(h, r, open_default=(book == "Genesis" and i < 7)))
    H += [base.JS, "</body></html>"]
    open(os.path.join(OUT, "PLAIN_OUTLINE.html"), "w", encoding="utf-8").write("\n".join(H))
    for f in sorted(os.listdir(OUT)):
        if f.startswith("PLAIN_"):
            print("wrote program/%-22s %6d KB" % (f, os.path.getsize(os.path.join(OUT, f)) // 1024))


if __name__ == "__main__":
    main()
