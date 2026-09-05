# -*- coding: utf-8 -*-
"""Full-Tanakh accent-tree sweep: run taamim_tree_parse.parse_verse on
every verse of all 24 books (39 book files); count unique + leaf_complete."""
import sys, sqlite3, json, traceback
sys.path.insert(0, "<repo-old>")
import taamim_tree_parse as T

db = sqlite3.connect("<repo-old>/elijah_docket/tanakh.sqlite")
verses = db.execute("SELECT book, chapter, verse FROM verses ORDER BY id").fetchall()
version = T.load_active_version()
total = ok = 0
fails = []
by_book = {}
for book, ch, vs in verses:
    osis = "%s.%d.%d" % (book, ch, vs)
    total += 1
    try:
        r = T.parse_verse(osis, version)
        good = (r.get("status") == "unique") and T.leaf_complete(r)
    except Exception as e:
        good = False
        r = {"status": "error: %s" % e}
    b = by_book.setdefault(book, [0, 0])
    b[0] += 1
    if good:
        ok += 1
        b[1] += 1
    else:
        if len(fails) < 60:
            fails.append((osis, str(r.get("status"))[:80]))
    if total % 2000 == 0:
        print("... %d/%d (ok %d)" % (total, len(verses), ok), flush=True)

import os
# the result is a disposable measurement: written to the CURRENT session's scratchpad
# (or the cwd) — the earlier hardcoded scratchpad path belonged to a session long
# gone and would have failed silently (sitting C of the audit, 2026-09-05)
out = os.environ.get("SWEEP_OUT", os.path.join(os.getcwd(), "tanakh_parse_sweep_result.json"))
json.dump({"rules_version": version, "total": total, "ok": ok,
           "by_book": by_book, "first_fails": fails}, open(out, "w"), indent=1)
print("RESULT: %d/%d unique+leaf_complete under rules %s" % (ok, total, version))
for b, (n, k) in by_book.items():
    if k != n:
        print("  %-6s %d/%d" % (b, k, n))
print("fails sample:", fails[:8])
