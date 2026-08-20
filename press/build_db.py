#!/usr/bin/env python3
"""
build_db.py — Step 1 of PLAN_fullstack_architecture_2026-07-28.md

Builds derivation.sqlite: a DERIVED, REBUILDABLE index of the whole Torah —
verses, words, morpheme segments, ta'amim trees (active rule version), leaves,
and auto roles. Never the system of record (Pre-Code rule): delete and rebuild
at any time with `python3 build_db.py`.

Sources read (never written): Data/*.xml (OSHB), logic/taamim_rules/ (via
taamim_tree_parse), and the role/lexicon rules currently inline in
press/render_flat_ledger_morph_html.py.
"""
from __future__ import annotations

import importlib.util
import json
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "derivation.sqlite"
BOOKS = ["Gen", "Exod", "Lev", "Num", "Deut"]

sys.path.insert(0, str(ROOT))
import taamim_tree_parse as ttp  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "rendermod", ROOT / "press/render_flat_ledger_morph_html.py"
)
render = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(renderer := render)  # noqa: F841

ROLE_RULESET = renderer.ROLE_RULESET  # from logic/role_rules/<CURRENT>/rules.yaml

SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE meta      (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE verses    (id INTEGER PRIMARY KEY, osis_id TEXT UNIQUE, book TEXT,
                        chapter INT, verse INT, system TEXT);
CREATE TABLE words     (id INTEGER PRIMARY KEY, verse_id INT REFERENCES verses(id),
                        idx INT, he TEXT, he_plain TEXT, translit TEXT, gloss TEXT,
                        lemma TEXT, morph TEXT, mark_id TEXT, mark_kind TEXT,
                        mark_rank INT, maqqef_after INT);
CREATE TABLE segments  (id INTEGER PRIMARY KEY, word_id INT REFERENCES words(id),
                        seg_idx INT, he TEXT, translit TEXT, lemma_seg TEXT,
                        morph_seg TEXT, gloss TEXT);
CREATE TABLE trees     (id INTEGER PRIMARY KEY, verse_id INT REFERENCES verses(id),
                        rule_version TEXT, status TEXT, tree_json TEXT);
CREATE TABLE leaves    (id INTEGER PRIMARY KEY, tree_id INT REFERENCES trees(id),
                        b_index INT, w_start INT, w_end INT, end_mark TEXT,
                        rank INT, path TEXT, he TEXT, translit TEXT, en TEXT);
CREATE TABLE roles     (leaf_id INT REFERENCES leaves(id), role TEXT,
                        ruleset_version TEXT);
CREATE TABLE warnings  (osis_id TEXT, kind TEXT, detail TEXT);
CREATE INDEX ix_words_verse ON words(verse_id);
CREATE INDEX ix_leaves_tree ON leaves(tree_id);
CREATE VIRTUAL TABLE fts USING fts5(osis_id, unit, ref, he_plain, translit, gloss);
"""


def verse_ids(book: str) -> list[tuple[str, int, int]]:
    xml = (ROOT / "shelf" / "sources" / f"{book}.xml").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(rf'osisID="{book}\.(\d+)\.(\d+)"', xml):
        out.append((f"{book}.{m.group(1)}.{m.group(2)}", int(m.group(1)), int(m.group(2))))
    return out


def build() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)
    t0 = time.time()
    n_verses = n_words = n_segs = n_leaves = n_mismatch = 0
    status_counts: dict[str, int] = {}

    for book in BOOKS:
        xml_path = ROOT / "shelf" / "sources" / f"{book}.xml"
        ids = verse_ids(book)
        print(f"{book}: {len(ids)} verses")
        for osis, ch, vs in ids:
            parsed = ttp.parse_verse(osis)
            status_counts[parsed["status"]] = status_counts.get(parsed["status"], 0) + 1
            cur = con.execute(
                "INSERT INTO verses(osis_id, book, chapter, verse, system) VALUES(?,?,?,?,?)",
                (osis, book, ch, vs, parsed["system"]),
            )
            verse_id = cur.lastrowid
            n_verses += 1

            # OSHB join (words + morpheme segments + translit/gloss)
            try:
                oshb = renderer.load_oshb_words(xml_path, ch, vs)
            except SystemExit:
                oshb = []
            joined = len(oshb) == len(parsed["words"])
            if not joined:
                n_mismatch += 1
                con.execute(
                    "INSERT INTO warnings VALUES(?,?,?)",
                    (osis, "word-count-mismatch",
                     f"parser={len(parsed['words'])} oshb={len(oshb)}"),
                )

            word_ids = []
            for w in parsed["words"]:
                i = w["index"]
                ow = oshb[i] if joined else None
                translit = renderer.word_translit(ow) if ow else ""
                gloss = renderer.word_gloss(ow) if ow else ""
                cur = con.execute(
                    "INSERT INTO words(verse_id, idx, he, he_plain, translit, gloss,"
                    " lemma, morph, mark_id, mark_kind, mark_rank, maqqef_after)"
                    " VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (verse_id, i, w["he"], w["he_plain"], translit, gloss,
                     ow["lemma"] if ow else None, ow["morph"] if ow else None,
                     w["mark_id"], w["mark_kind"], w["rank"],
                     1 if (ow and ow["maqqef_after"]) else 0),
                )
                word_ids.append(cur.lastrowid)
                n_words += 1
                con.execute(
                    "INSERT INTO fts VALUES(?,?,?,?,?,?)",
                    (osis, "word", f"w{i}", w["he_plain"], translit, gloss),
                )
                if ow:
                    segs = renderer.word_segments(ow)
                    for si, (t, l, m) in enumerate(segs):
                        con.execute(
                            "INSERT INTO segments(word_id, seg_idx, he, translit,"
                            " lemma_seg, morph_seg, gloss) VALUES(?,?,?,?,?,?,?)",
                            (word_ids[-1], si, t,
                             renderer.translit_segment(t, si == len(segs) - 1),
                             l.strip(), m, renderer.seg_lemma_gloss(l, m)),
                        )
                        n_segs += 1

            # tree + leaves + roles
            cur = con.execute(
                "INSERT INTO trees(verse_id, rule_version, status, tree_json) VALUES(?,?,?,?)",
                (verse_id, parsed["rule_set_version"], parsed["status"],
                 json.dumps(parsed["tree"], ensure_ascii=False) if parsed["tree"] else None),
            )
            tree_id = cur.lastrowid
            if parsed["tree"]:
                for li, leaf in enumerate(renderer.collect_leaves(parsed["tree"])):
                    idx = leaf["indices"]
                    if joined:
                        he = ""
                        for j, i in enumerate(idx):
                            he += oshb[i]["text"].replace("/", "")
                            if j < len(idx) - 1:
                                he += "־" if oshb[i]["maqqef_after"] else " "
                        tr = " ".join(renderer.word_translit(oshb[i]) for i in idx)
                        en = " ".join(renderer.word_gloss(oshb[i]) for i in idx)
                    else:
                        he = " ".join(parsed["words"][i]["he"].replace("/", "") for i in idx)
                        tr = en = ""
                    cur = con.execute(
                        "INSERT INTO leaves(tree_id, b_index, w_start, w_end, end_mark,"
                        " rank, path, he, translit, en) VALUES(?,?,?,?,?,?,?,?,?,?)",
                        (tree_id, li, idx[0], idx[-1], leaf["mark"], leaf["rank"],
                         "·".join(leaf["path"]) if leaf["path"] != "ROOT" else "ROOT",
                         he, tr, en),
                    )
                    leaf_id = cur.lastrowid
                    n_leaves += 1
                    con.execute(
                        "INSERT INTO fts VALUES(?,?,?,?,?,?)",
                        (osis, "leaf", f"B{li}",
                         ttp.strip_taamim_and_points(he), tr, en),
                    )
                    if joined:
                        leaf_segs = []
                        for i in idx:
                            leaf_segs.extend(renderer.word_segments(oshb[i]))
                        con.execute(
                            "INSERT INTO roles VALUES(?,?,?)",
                            (leaf_id, renderer.leaf_role(leaf_segs), ROLE_RULESET),
                        )
        con.commit()

    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                                capture_output=True, text=True, cwd=ROOT).stdout.strip()
    except Exception:
        commit = "unknown"
    meta = {
        "built_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "built_from_commit": commit,
        "taamim_rule_version": ttp.load_active_version(),
        "role_ruleset": ROLE_RULESET,
        "lexicon_version": renderer.LEX_VERSION,
        "lexicon_note": "logic/lexicon: hand glosses override Strong's auto (#IMPOSED, public domain); EN-AID only",
        "verses": str(n_verses), "words": str(n_words), "segments": str(n_segs),
        "leaves": str(n_leaves), "word_count_mismatches": str(n_mismatch),
        "status_counts": json.dumps(status_counts),
    }
    con.executemany("INSERT INTO meta VALUES(?,?)", meta.items())
    con.commit()
    con.close()
    print(f"\nbuilt {DB_PATH.name} in {time.time()-t0:.1f}s")
    for k, v in meta.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    build()
