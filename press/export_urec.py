#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""export_urec.py — the per-unit record bundle for the redesigned scroll.

One JSON file, scroll/data/urec.json: for every canonical unit, the
facts the scroll page's unit bands render — title, span, revision,
stamp, the declared-reading arithmetic from the triage ledger's LAST
completion line, the verdict-class tallies and material findings from
the triage index, the oral teaching blocks from the unit YAML, and the
kept-out example (the unit's first enrichment row — the reading that
changed nothing, shown beside the teachings that changed everything).

Everything here is a transform of the records — the YAMLs under
logic/units/, the ledgers under logic/oral_triage/, and the triage
table in data/derivation.sqlite. The mill asserts nothing: a unit with
no ledger simply ships no reading arithmetic, and the page says so.

Run from the repo root after any landing, before export_web/export_site:
    python3 press/export_urec.py
"""
import glob
import json
import os
import re
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "press", "vendor"))
import yaml  # noqa: E402  (vendored, owner-approved 2026-08-20)

# The creation-week census thread, the one STEP 5 peek each of these
# units shows (the ordinals as each unit's own reading recorded them;
# they are dispute-relative and the texts say so).
CENSUS = {
    "gen_01_creation_boot": "utterances #1 and #2 — the opening word "
        "itself counts (the day-one canon), then “let there be "
        "light.”",
    "gen_02_raqia_day": "utterance #3 — and #4 under the recorded "
        "dissent that counts the wind of 1:2; both ordinals are carried.",
    "gen_03_double_build": "utterances #4 and #5 — the gathering of the "
        "waters and the sprouting of the earth.",
    "gen_04_lights_calendar": "utterance #6 — “let there be "
        "lights,” the calendar's own fiat.",
    "gen_05_swarms_blessing": "utterance #7 — the swarming waters; a "
        "recorded dispute carries a tenth-utterance candidate here too.",
    "gen_06_land_adam_dominion": "utterances #8, #9 and #10 — the "
        "beasts, “let us make man,” and the food grant: the "
        "census CLOSES on this block.",
}


def stamp_of(meta):
    for line in meta.get("changelog") or []:
        m = re.search(r"rev (\d+) \((\d{4}-\d{2}-\d{2})\).*FULL-RULE STAMP",
                      str(line))
        if m:
            return m.group(2)
    return None


def main():
    cx = sqlite3.connect(os.path.join(ROOT, "data", "derivation.sqlite"))
    urec = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "logic", "units",
                                              "*.yaml"))):
        d = yaml.safe_load(open(path, encoding="utf-8"))
        meta = d["meta"]
        uid = meta["id"]
        rows = cx.execute(
            "SELECT row_num, source_ref, verdict_class, note FROM triage "
            "WHERE unit LIKE ? ORDER BY row_num", (uid + "%",)).fetchall()
        cls = {}
        for _n, _s, vc, _note in rows:
            cls[vc] = cls.get(vc, 0) + 1
        leds = sorted(glob.glob(os.path.join(
            ROOT, "logic", "oral_triage", uid + "_*.md")))
        led, read, declared = None, None, None
        if leds:
            led = os.path.basename(leds[-1])
            mts = re.findall(r"\*\*read: (\d+) of (\d+)",
                             open(leds[-1], encoding="utf-8").read())
            if mts:
                read, declared = int(mts[-1][0]), int(mts[-1][1])
        kept = next((["%s" % s, note or "", n]
                     for n, s, vc, note in rows if vc == "enrichment"),
                    None)
        teach = [{"id": b["id"], "work": b.get("work_en"),
                  "he": b.get("he"), "tr": b.get("he_translit"),
                  "en": b.get("en"), "status": b.get("status")}
                 for b in d.get("oral_notes") or []
                 if str(b.get("en") or "").strip()
                 and str(b.get("he") or "").strip()]
        urec[uid] = {
            "t": meta.get("title_en"),
            "book": meta.get("book_en"),
            "refs": meta.get("refs"),
            "rev": meta.get("rev", 1),
            "full": meta.get("tree_derive_version")
                    == "logic_derived_v2_full_rule",
            "stamped": stamp_of(meta),
            "led": led, "read": read, "declared": declared,
            "cls": cls,
            "mat": [[s, note or ""] for _n, s, vc, note in rows
                    if vc == "material"],
            "rows": [[n, s, vc] for n, s, vc, _note in rows],
            "kept": kept,
            "teach": teach,
            "census": CENSUS.get(uid),
        }
    out = os.path.join(ROOT, "scroll", "data", "urec.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(urec, f, ensure_ascii=False, separators=(",", ":"))
    with_led = sum(1 for u in urec.values() if u["led"])
    print("urec: %d units (%d with reading ledgers), %d triage rows, "
          "%.0f KB -> %s"
          % (len(urec), with_led,
             sum(len(u["rows"]) for u in urec.values()),
             os.path.getsize(out) / 1024, os.path.relpath(out, ROOT)))


if __name__ == "__main__":
    main()
