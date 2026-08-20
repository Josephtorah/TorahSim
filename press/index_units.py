#!/usr/bin/env python3
"""
index_units.py — Step 2 of PLAN_fullstack_architecture_2026-07-28.md

Indexes logic/units/*.yaml into derivation.sqlite (units / steps / coverage /
unit_scenarios tables + FTS rows). READ-ONLY over the YAML: validation problems
are flagged into `warnings`, never fixed here. The YAML stays canonical
(Pre-Code rule); drop these tables and re-run any time.
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import sys as _vsys; from pathlib import Path as _VP; _vsys.path.insert(0, str(_VP(__file__).resolve().parent / "vendor"))
import yaml

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "derivation.sqlite"
UNITS = ROOT / "logic" / "units"

REQUIRED_META = ["id", "refs", "status"]

DDL = """
DROP TABLE IF EXISTS units;
DROP TABLE IF EXISTS steps;
DROP TABLE IF EXISTS coverage;
DROP TABLE IF EXISTS unit_scenarios;
DROP TABLE IF EXISTS unit_oral_notes;
DROP TABLE IF EXISTS unit_amendments;
CREATE TABLE units (id INTEGER PRIMARY KEY, unit_id TEXT UNIQUE, file TEXT,
                    book_en TEXT, refs TEXT, status TEXT, genre TEXT,
                    confidence TEXT, title_en TEXT, tree_derive_version TEXT,
                    n_steps INT, n_scenarios INT);
CREATE TABLE steps (id INTEGER PRIMARY KEY, unit_id TEXT, step_id TEXT,
                    ord TEXT, ref TEXT, op TEXT, he TEXT, translit TEXT,
                    en TEXT, comment TEXT, confidence TEXT, source TEXT);
CREATE TABLE coverage (unit_id TEXT, ref TEXT, coverage_json TEXT);
CREATE TABLE unit_scenarios (unit_id TEXT, sid TEXT, title_en TEXT,
                             expect_en TEXT, extra_json TEXT);
CREATE TABLE unit_oral_notes (unit_id TEXT, note_id TEXT, status TEXT,
                              work_en TEXT, he TEXT, translit TEXT,
                              en TEXT, comment_en TEXT, source TEXT);
CREATE TABLE unit_amendments (unit_id TEXT, date TEXT, authorized TEXT,
                              what TEXT);
CREATE INDEX ix_steps_unit ON steps(unit_id);
CREATE INDEX ix_steps_ref ON steps(ref);
"""


def main() -> None:
    con = sqlite3.connect(DB)
    con.executescript(DDL)
    con.execute("DELETE FROM warnings WHERE kind LIKE 'unit-%'")
    con.execute("DELETE FROM fts WHERE unit IN ('step')")

    files = sorted(UNITS.glob("*.yaml"))
    n_units = n_steps = n_scen = n_warn = 0
    for f in files:
        if f.name.startswith("unit_template"):
            continue
        try:
            d = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception as e:
            con.execute("INSERT INTO warnings VALUES(?,?,?)",
                        (f.name, "unit-parse-error", str(e)[:200]))
            n_warn += 1
            continue
        meta = d.get("meta", {}) or {}
        missing = [k for k in REQUIRED_META if not meta.get(k)]
        if missing:
            con.execute("INSERT INTO warnings VALUES(?,?,?)",
                        (f.name, "unit-missing-meta", ",".join(missing)))
            n_warn += 1
        uid = meta.get("id", f.stem)
        steps = d.get("boot_steps") or []
        scen = d.get("scenarios") or []
        con.execute(
            "INSERT OR REPLACE INTO units(unit_id, file, book_en, refs, status, genre,"
            " confidence, title_en, tree_derive_version, n_steps, n_scenarios)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (uid, str(f.relative_to(ROOT)), meta.get("book_en"), str(meta.get("refs")),
             meta.get("status"), meta.get("genre"), meta.get("confidence_overall"),
             str(meta.get("title_en"))[:120], meta.get("tree_derive_version"),
             len(steps) if isinstance(steps, list) else 0,
             len(scen) if isinstance(scen, list) else 0),
        )
        n_units += 1
        for o in (d.get("oral_notes") or []):
            if isinstance(o, dict):
                con.execute(
                    "INSERT INTO unit_oral_notes VALUES(?,?,?,?,?,?,?,?,?)",
                    (uid, o.get("id"), o.get("status"), o.get("work_en"),
                     o.get("he"), o.get("he_translit"), str(o.get("en", "")),
                     str(o.get("comment_en", "")), str(o.get("source", ""))))
        for a in (d.get("amendment_log") or []):
            if isinstance(a, dict):
                con.execute(
                    "INSERT INTO unit_amendments VALUES(?,?,?,?)",
                    (uid, str(a.get("date")), str(a.get("authorized", "")),
                     str(a.get("what", ""))))
        if isinstance(steps, list):
            for s in steps:
                if not isinstance(s, dict):
                    continue
                con.execute(
                    "INSERT INTO steps(unit_id, step_id, ord, ref, op, he, translit,"
                    " en, comment, confidence, source) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                    (uid, s.get("id"), str(s.get("order", "")), s.get("ref"),
                     s.get("op"), s.get("he"), s.get("he_translit"), s.get("en"),
                     str(s.get("comment", ""))[:400], s.get("confidence"),
                     str(s.get("source", ""))),
                )
                con.execute("INSERT INTO fts VALUES(?,?,?,?,?,?)",
                            (s.get("ref") or uid, "step", s.get("id") or "",
                             s.get("he") or "", s.get("he_translit") or "",
                             s.get("en") or ""))
                n_steps += 1
        cov = d.get("tree_coverage") or {}
        for ref, cv in (cov.get("verses") or {}).items() if isinstance(cov.get("verses"), dict) else []:
            con.execute("INSERT INTO coverage VALUES(?,?,?)",
                        (uid, str(ref), json.dumps(cv, ensure_ascii=False)[:4000]))
        if isinstance(scen, list):
            for s in scen:
                if not isinstance(s, dict):
                    continue
                extra = {k: v for k, v in s.items() if k not in ("id", "title_en", "expect_en")}
                con.execute("INSERT INTO unit_scenarios VALUES(?,?,?,?,?)",
                            (uid, s.get("id"), s.get("title_en"), s.get("expect_en"),
                             json.dumps(extra, ensure_ascii=False)[:2000]))
                n_scen += 1

    con.execute("INSERT OR REPLACE INTO meta VALUES('units_indexed', ?)", (str(n_units),))
    con.execute("INSERT OR REPLACE INTO meta VALUES('unit_steps_indexed', ?)", (str(n_steps),))
    con.commit()
    con.close()
    print(f"indexed {n_units} units · {n_steps} steps · {n_scen} scenarios · {n_warn} warnings")


if __name__ == "__main__":
    main()
