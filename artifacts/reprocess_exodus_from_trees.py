#!/usr/bin/env python3
"""
Reprocess Exodus units tree-first (tree_derived_v1).

Order: Hebrew verse → ta'amim tree v1 → top-split arms → one STEP per verse
       → maps_to that STEP → tree_coverage.

Does not invent binding law. English is [EN-AID] gloss only.
See reviews/EXODUS_TREE_DERIVE_2026-07-24.md
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from taamim_tree_parse import parse_verse, tree_ascii_string, strip_taamim_and_points  # noqa: E402

UNITS = ROOT / "logic" / "units"
MEKH_HE = ROOT / "Data" / "mekhilta_he.json"

# Chapter lengths Exod (OSIS / Data/Exod.xml)
COUNTS = {
    1: 22, 2: 25, 3: 22, 4: 31, 5: 23, 6: 30, 7: 29, 8: 28, 9: 35, 10: 29,
    11: 10, 12: 51, 13: 22, 14: 31, 15: 27, 16: 36, 17: 16, 18: 27, 19: 25, 20: 26,
    21: 37, 22: 30, 23: 33, 24: 18, 25: 40, 26: 37, 27: 21, 28: 43, 29: 46, 30: 38,
    31: 18, 32: 35, 33: 23, 34: 35, 35: 35, 36: 38, 37: 29, 38: 31, 39: 43, 40: 38,
}

PHASES: dict[str, list[str]] = {
    "1": ["exo_01_israel_egypt_oppression"],
    "2a": [
        "exo_01_israel_egypt_oppression",
        "exo_02_moses_midian",
        "exo_03_bush_call",
        "exo_04_signs_return",
        "exo_05_bricks_worse",
        "exo_06_name_roster",
    ],
    "2b": [
        "exo_07_staff_blood",
        "exo_08_frogs_to_swarm",
        "exo_09_livestock_hail",
        "exo_10_locust_dark",
        "exo_11_last_warning",
    ],
    "2c": [
        "exo_12_pesach_command",
        "exo_12_midnight_leave",
        "exo_13_firstborn_matzot",
        "exo_13_route_pillar",
        "exo_14_sea",
        "exo_15_song",
        "exo_15_marah",
        "exo_16_manna_shabbat",
        "exo_17_water_amalek",
        "exo_18_yitro",
        "exo_19_sinai_prep",
        "exo_20_decalogue_altar",
        "exo_21_slave_person",
        "exo_21_ox_pit",
        "exo_22_property_social",
        "exo_23_justice_calendar",
        "exo_23_escort_land",
        "exo_24_covenant_ascent",
    ],
    "2d": [
        "exo_25_ark_table_menorah",
        "exo_26_curtains_boards",
        "exo_27_altar_court",
        "exo_28_priest_garments",
        "exo_29_investiture",
        "exo_30_incense_shekel",
        "exo_31_craftsmen_shabbat",
    ],
    "2e": [
        "exo_32_golden_calf",
        "exo_33_presence",
        "exo_34_second_tablets",
    ],
    "2f": [
        "exo_35_shabbat_donate",
        "exo_35_36_work_start",
        "exo_37_furniture_made",
        "exo_38_court_inventory",
        "exo_39_garments_done",
        "exo_40_erect_fill",
    ],
}

# Simple consonant-oriented translit (reading aid only)
_HE_MAP = {
    "א": "'", "ב": "b", "ג": "g", "ד": "d", "ה": "h", "ו": "v", "ז": "z",
    "ח": "ch", "ט": "t", "י": "y", "כ": "k", "ך": "k", "ל": "l", "מ": "m",
    "ם": "m", "נ": "n", "ן": "n", "ס": "s", "ע": "'", "פ": "p", "ף": "p",
    "צ": "tz", "ץ": "tz", "ק": "q", "ר": "r", "ש": "sh", "ת": "t",
    "־": "-", " ": " ", "/": "/",
}


def yaml_quote(s: Optional[str]) -> str:
    if s is None:
        return '""'
    if any(c in s for c in ':"\'\n#{}[]|&*>!%@`') or s == "" or s.strip() != s:
        return json.dumps(s, ensure_ascii=False)
    return s


def translit_plain(he_plain: str) -> str:
    p = he_plain.replace("/", "")
    out = []
    for ch in p:
        if ch in _HE_MAP:
            out.append(_HE_MAP[ch])
        elif "\u05B0" <= ch <= "\u05BD" or "\u05C1" <= ch <= "\u05C7":
            continue  # points
        elif ch in "ְֱֲֳִֵֶַָֹֺֻּׁׂ":
            continue
        else:
            # keep digits etc; skip remaining marks
            if ord(ch) < 0x0590 or ord(ch) > 0x05FF:
                out.append(ch)
    s = "".join(out)
    s = re.sub(r"'+", "'", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s or "x"


def extract_meta_block(text: str) -> dict[str, Any]:
    """Pull key meta fields from existing unit (best-effort)."""
    out: dict[str, Any] = {}
    for key in (
        "id", "title_en", "title_he", "title_he_translit", "title_he_en",
        "book_he", "book_he_translit", "book_en", "refs", "genre", "build_track",
    ):
        m = re.search(rf'^\s*{key}:\s*(.+)$', text, re.M)
        if not m:
            continue
        val = m.group(1).strip()
        if val.startswith('"') or val.startswith("'"):
            try:
                out[key] = json.loads(val.replace("'", '"')) if val.startswith("'") else json.loads(val)
            except Exception:
                out[key] = val.strip('"').strip("'")
        else:
            out[key] = val
    # depends_on list
    dm = re.search(r"depends_on:\n((?:\s+-\s+.+\n)+)", text)
    deps = []
    if dm:
        deps = re.findall(r'-\s*"?([^"\n]+)"?', dm.group(1))
    out["depends_on"] = deps
    # imports / oral notes free text
    im = re.search(r"imports_note_en:\s*(.+)", text)
    out["imports_note_en"] = im.group(1).strip().strip('"') if im else ""
    om = re.search(r"oral_policy_note_en:\s*>\n((?:\s{4}.+\n)+)", text)
    if om:
        out["oral_policy_note_en"] = " ".join(
            ln.strip() for ln in om.group(1).splitlines() if ln.strip()
        )
    else:
        out["oral_policy_note_en"] = (
            "Written trees first. Mekhilta dual-track on law densification; "
            "never silent-merge. MH endpoints remain possible Oral."
        )
    # mekh lean from comments
    if "mekhilta" in text.lower() or "Mekhilta" in text:
        out["mekh"] = "sample"
    else:
        out["mekh"] = "thin"
    # exports from old unit
    exports = []
    for m in re.finditer(
        r"-\s+id:\s*(\S+)\n(?:\s+he:\s*(.+)\n)?(?:\s+he_translit:\s*(.+)\n)?\s+en:\s*(.+)",
        text,
    ):
        if m.group(1).startswith("EXPORT") or m.group(1).startswith("export"):
            he = (m.group(2) or "").strip().strip('"')
            tr = (m.group(3) or "").strip().strip('"')
            en = (m.group(4) or "").strip().strip('"')
            exports.append((m.group(1), he or None, tr or None, en))
    out["exports"] = exports[:12]
    return out


def parse_refs(refs: str) -> tuple[int, int, int, int]:
    """Parse '1:1-22' or '12:29-51' or '35:30-36:38'."""
    refs = refs.strip().strip('"')
    m = re.match(r"(\d+):(\d+)-(\d+):(\d+)$", refs)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    m = re.match(r"(\d+):(\d+)-(\d+)$", refs)
    if m:
        ch = int(m.group(1))
        return ch, int(m.group(2)), ch, int(m.group(3))
    m = re.match(r"(\d+):(\d+)$", refs)
    if m:
        ch, v = int(m.group(1)), int(m.group(2))
        return ch, v, ch, v
    raise ValueError(f"bad refs: {refs}")


def verse_list(ch_s: int, v_s: int, ch_e: int, v_e: int) -> list[tuple[int, int]]:
    out = []
    for ch in range(ch_s, ch_e + 1):
        lo = v_s if ch == ch_s else 1
        hi = v_e if ch == ch_e else COUNTS[ch]
        for v in range(lo, hi + 1):
            out.append((ch, v))
    return out


def top_arms(tree: dict, words: list[dict]) -> dict[str, Any]:
    children = tree.get("children") or []
    if len(children) >= 2:
        left, right = children[0], children[1]
    elif len(children) == 1:
        left, right = children[0], {"he_span": "", "word_indices": []}
    else:
        left = right = {
            "he_span": tree.get("he_span", ""),
            "word_indices": tree.get("word_indices", []),
        }

    def arm(node: dict) -> dict[str, Any]:
        idxs = node.get("word_indices") or []
        plains = []
        trs = []
        for i in idxs:
            if 0 <= i < len(words):
                hp = words[i]["he_plain"].replace("/", "")
                plains.append(hp)
                trs.append(translit_plain(words[i]["he_plain"]))
        he = " ".join(plains)
        # head = last disjunctive prefer etnachta else last
        head_i = idxs[-1] if idxs else 0
        head_mark = ""
        for i in idxs:
            w = words[i]
            if "etnachta" in (w.get("mark_en") or ""):
                head_i = i
                head_mark = w.get("mark_en") or ""
                break
        else:
            if idxs:
                head_mark = words[idxs[-1]].get("mark_en") or ""
        head_he = words[head_i]["he_plain"].replace("/", "") if idxs and head_i < len(words) else ""
        return {
            "he": he,
            "he_translit": " ".join(trs),
            "he_span_raw": (node.get("he_span") or "")[:200],
            "head_he": head_he,
            "head_i": head_i,
            "head_mark": head_mark,
            "idxs": idxs,
        }

    return {"left": arm(left), "right": arm(right)}


def role_for_plain(he_plain: str) -> tuple[str, str]:
    p = he_plain.replace("/", "").replace("־", "")
    # strip points for match
    p0 = strip_taamim_and_points(p) if p else p
    glue = {
        "את", "אל", "על", "מן", "עם", "או", "אם", "כי", "גם", "אשר", "לא", "כל",
        "זה", "זו", "זאת", "בן", "בין", "ו", "ה", "ב", "כ", "ל", "מ",
    }
    if p0 in glue or len(p0) <= 1:
        return "glue", "glue"
    people = (
        "משה", "אהרן", "ישראל", "פרעה", "יוסף", "יעקב", "אברהם", "יצחק",
        "מרים", "צפורה", "יתרו", "נדב", "אביהוא", "אלעזר", "איתמר",
    )
    if any(x in p0 for x in people):
        return "agent_or_person", "logic_bearing"
    return "logic_bearing_leaf", "logic_bearing"


def has_condition_marker(words: list[dict]) -> Optional[str]:
    for w in words[:4]:
        p = strip_taamim_and_points(w["he_plain"].replace("/", ""))
        if p in ("אם", "ואם", "כי", "וכי", "הן"):
            return p
    return None


def mekh_samples(max_paras: int = 3) -> list[dict]:
    if not MEKH_HE.exists():
        return []
    try:
        data = json.loads(MEKH_HE.read_text(encoding="utf-8"))
    except Exception:
        return []
    text = data.get("text") or data
    out: list[dict] = []

    def walk(o, section: str):
        if len(out) >= max_paras:
            return
        if isinstance(o, str) and o.strip():
            out.append({"section": section, "he": o.strip()[:240]})
            return
        if isinstance(o, list):
            for x in o:
                walk(x, section)
                if len(out) >= max_paras:
                    return
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(v, str(k)[:80])
                if len(out) >= max_paras:
                    return

    walk(text, "Mekhilta")
    return out


def emit_unit(unit_id: str, phase: str) -> Path:
    path = UNITS / f"{unit_id}.yaml"
    if not path.exists():
        raise FileNotFoundError(path)
    old = path.read_text(encoding="utf-8")
    meta = extract_meta_block(old)
    refs = meta.get("refs") or ""
    # fix refs if quoted leftovers
    refs = str(refs).strip().strip('"')
    ch_s, v_s, ch_e, v_e = parse_refs(refs)
    verses = verse_list(ch_s, v_s, ch_e, v_e)
    genre = str(meta.get("genre") or "narrative_fsm").strip().strip('"')
    title_en = str(meta.get("title_en") or unit_id)
    title_he = str(meta.get("title_he") or "")
    title_tr = str(meta.get("title_he_translit") or "")
    title_he_en = str(meta.get("title_he_en") or "")
    depends = meta.get("depends_on") or []
    exports = meta.get("exports") or []
    if not exports:
        exports = [
            (
                f"EXPORT_{unit_id}_tree_derived",
                None,
                None,
                f"Tree-derived v1 package for {refs}",
            )
        ]

    # Parse all verses first
    parsed_verses: list[dict[str, Any]] = []
    for ch, v in verses:
        osis = f"Exod.{ch}.{v}"
        try:
            pr = parse_verse(osis)
            arms = top_arms(pr["tree"], pr["words"])
            ascii_t = tree_ascii_string(pr["tree"])
            pure = "false" if ("3-ary" in ascii_t or "n-ary" in ascii_t) else "true"
            cond = has_condition_marker(pr["words"])
            sid = f"STEP_Ex_{ch}_{v}"
            left = arms["left"]
            right = arms["right"]
            # op from first content words
            plain_words = [w["he_plain"].replace("/", "") for w in pr["words"]]
            linear_he = " ".join(plain_words)
            linear_tr = " ".join(translit_plain(w["he_plain"]) for w in pr["words"])
            op = "TREE_CLAIM"
            if cond:
                op = f"COND_{cond}"
            elif any("etnachta" in (w.get("mark_en") or "") for w in pr["words"]):
                op = "ETNACHTA_SPLIT"
            step_en = (
                f"[EN-AID] From top split: LEFT «{left['he'][:80]}» "
                f"/ RIGHT «{right['he'][:80]}». "
                f"Derive claim from Hebrew arms, not English alone. Exod {ch}:{v}."
            )
            step_he = f"{left['he'][:60]} … {right['he'][:60]}" if right["he"] else left["he"][:120]
            step_tr = (
                f"{left['he_translit'][:50]} … {right['he_translit'][:50]}"
                if right["he_translit"]
                else left["he_translit"][:100]
            )
            parsed_verses.append(
                {
                    "ch": ch,
                    "v": v,
                    "osis": osis,
                    "sid": sid,
                    "op": op,
                    "cond": cond,
                    "pr": pr,
                    "arms": arms,
                    "ascii": ascii_t,
                    "pure": pure,
                    "linear_he": linear_he,
                    "linear_tr": linear_tr,
                    "step_he": step_he,
                    "step_tr": step_tr,
                    "step_en": step_en,
                    "words": pr["words"],
                }
            )
        except Exception as e:
            parsed_verses.append(
                {
                    "ch": ch,
                    "v": v,
                    "osis": f"Exod.{ch}.{v}",
                    "sid": f"STEP_Ex_{ch}_{v}",
                    "op": "PARSE_ERROR",
                    "error": str(e),
                    "pr": None,
                }
            )

    lines: list[str] = []
    lines.append("# =============================================================================")
    lines.append(f"# LOGIC UNIT: Exodus {refs} — {title_en}")
    lines.append(f"# TREE-DERIVED v1 (phase {phase}) — steps from ta'amim top splits")
    lines.append("# =============================================================================")
    lines.append("# Experimental model — not binding religious law.")
    lines.append("# Process: tree → arm-cited STEP per verse → maps_to → coverage.")
    lines.append("")
    lines.append("meta:")
    lines.append(f'  id: "{unit_id}"')
    lines.append(f"  title_en: {yaml_quote(title_en)}")
    lines.append(f"  title_he: {yaml_quote(title_he)}")
    lines.append(f"  title_he_translit: {yaml_quote(title_tr)}")
    lines.append(f"  title_he_en: {yaml_quote(title_he_en)}")
    lines.append('  book_he: "שְׁמוֹת"')
    lines.append('  book_he_translit: "Shemot"')
    lines.append('  book_en: "Exodus"')
    lines.append(f'  refs: "{refs}"')
    lines.append("  data_paths_he:")
    lines.append('    - "Data/Exod.xml"')
    lines.append("  status: draft")
    lines.append("  tree_derive_version: tree_derived_v1")
    lines.append(f'  tree_derive_phase: "{phase}"')
    lines.append("  confidence_overall: hypothesis")
    lines.append(f'  genre: "{genre}"')
    lines.append('  build_track: exodus_install')
    lines.append("  depends_on:")
    for d in depends:
        lines.append(f'    - "{d.strip()}"')
    lines.append("  owner_language_note: >")
    lines.append("    English for reading only. Hebrew is the derivation source.")
    lines.append("  oral_policy_note_en: >")
    for chunk in re.findall(r".{1,90}(?:\s|$)", str(meta.get("oral_policy_note_en") or "")):
        lines.append(f"    {chunk.rstrip()}")
    lines.append("  method_note_en: >")
    lines.append("    Tree-derived v1: each verse's top binary split (left/right arms) grounds")
    lines.append("    one STEP_Ex_C_V. Not multi-verse English smear. Not full TIR yet.")
    lines.append("")
    lines.append("derivation_log:")
    lines.append("  - step: A")
    lines.append('    name_en: "Block choice"')
    lines.append("    comment: >")
    lines.append(f"      Reprocess {unit_id} ({refs}, {len(verses)} vv) tree-first phase {phase}.")
    lines.append("    confidence: established")
    lines.append("  - step: B")
    lines.append('    name_en: "Trees"')
    lines.append("    comment: >")
    lines.append("      Every verse via taamim_tree_parse.py v1; full tree_ascii recorded.")
    lines.append("    confidence: tested")
    lines.append('    tags: ["[HE-STRUCT]"]')
    lines.append("  - step: C")
    lines.append('    name_en: "Tree → steps"')
    lines.append("    comment: >")
    lines.append("      One STEP per verse citing left/right top-split arms. English [EN-AID] only.")
    lines.append("      Condition markers (אם/כי) flagged in op when verse-initial.")
    lines.append("    confidence: hypothesis")
    lines.append('    tags: ["[HE-WRITTEN]","[HE-STRUCT]"]')
    lines.append("  - step: D")
    lines.append('    name_en: "Oral dual-track"')
    lines.append("    comment: >")
    lines.append("      Mekhilta samples when available; dual-track only; never silent-merge.")
    lines.append("    confidence: hypothesis")
    lines.append('    tags: ["[ORAL]"]')
    lines.append("")
    lines.append("boot_steps:")
    order = 0
    decision_rows: list[tuple[str, str, str]] = []
    for pv in parsed_verses:
        if pv.get("error"):
            order += 1
            lines.append(f"  - id: {pv['sid']}")
            lines.append(f"    order: {order}")
            lines.append(f'    ref: "Exod.{pv["ch"]}.{pv["v"]}"')
            lines.append("    op: PARSE_ERROR")
            lines.append(f"    en: {yaml_quote('Parse error: ' + pv['error'])}")
            lines.append("    confidence: failed")
            lines.append('    source: "[HE-STRUCT]"')
            lines.append("")
            continue
        order += 1
        left = pv["arms"]["left"]
        right = pv["arms"]["right"]
        lines.append(f"  - id: {pv['sid']}")
        lines.append(f"    order: {order}")
        lines.append(f'    ref: "Exod.{pv["ch"]}.{pv["v"]}"')
        lines.append(f"    op: {pv['op']}")
        lines.append(f"    he: {yaml_quote(pv['step_he'])}")
        lines.append(f"    he_translit: {yaml_quote(pv['step_tr'])}")
        lines.append(f"    en: {yaml_quote(pv['step_en'])}")
        lines.append("    tree_left:")
        lines.append(f"      he: {yaml_quote(left['he'][:200])}")
        lines.append(f"      he_translit: {yaml_quote(left['he_translit'][:200])}")
        lines.append('      en: "Left arm of top binary split [EN-AID]"')
        lines.append("    tree_right:")
        lines.append(f"      he: {yaml_quote(right['he'][:200])}")
        lines.append(f"      he_translit: {yaml_quote(right['he_translit'][:200])}")
        lines.append('      en: "Right arm of top binary split [EN-AID]"')
        lines.append("    comment: >")
        lines.append(
            f"      Top split head mark L={left.get('head_mark') or 'n/a'}; "
            f"R head mark noted in tree. maps_to this verse only."
        )
        lines.append("    confidence: hypothesis")
        lines.append('    source: "[HE-WRITTEN][HE-STRUCT]"')
        lines.append("")
        if pv.get("cond") and genre == "decision_table":
            decision_rows.append(
                (
                    f"ROW_Ex_{pv['ch']}_{pv['v']}",
                    f"Marker {pv['cond']} in Exod {pv['ch']}:{pv['v']} (tree-left/right must be read)",
                    f"Apply claim of {pv['sid']} from Hebrew arms — hypothesis only",
                )
            )

    if genre == "decision_table":
        lines.append("decision_table:")
        lines.append("  comment_en: >")
        lines.append("    Hypothesis rows from tree-flagged condition markers and arm structure.")
        lines.append("    Not binding law. Deepen with Mekhilta dual-track separately.")
        lines.append("  rows:")
        if decision_rows:
            for rid, ifr, thenr in decision_rows:
                lines.append(f"    - id: {rid}")
                lines.append(f"      if_en: {yaml_quote(ifr)}")
                lines.append(f"      then_en: {yaml_quote(thenr)}")
                lines.append("      confidence: hypothesis")
                lines.append('      source: "[HE-WRITTEN][HE-STRUCT]"')
        else:
            lines.append("    - id: ROW_STRUCTURAL")
            lines.append(
                '      if_en: "When this block\'s case conditions hold (read per-verse tree arms)"'
            )
            lines.append(
                '      then_en: "Follow sequential STEP_Ex_* for verses in this unit (hypothesis)"'
            )
            lines.append("      confidence: hypothesis")
            lines.append('      source: "[HE-WRITTEN][HE-STRUCT]"')
        lines.append("")

    # state machine: open + mid + closed
    lines.append("state_machine:")
    lines.append(f'  comment_en: "Coarse states for {unit_id} after tree-derived steps."')
    lines.append("  states:")
    lines.append("    - id: S_block_open")
    lines.append(f'      en: "Entered {refs}"')
    lines.append("    - id: S_block_mid")
    lines.append('      en: "Mid-block after ~half of verse steps"')
    lines.append("    - id: S_block_closed")
    lines.append(f'      en: "Completed tree-derived steps for {refs}"')
    lines.append("  transitions:")
    if parsed_verses:
        mid = parsed_verses[len(parsed_verses) // 2]["sid"]
        last = parsed_verses[-1]["sid"]
        first = parsed_verses[0]["sid"]
        lines.append("    - from: S_block_open")
        lines.append("      to: S_block_mid")
        lines.append(f"      via: {mid}")
        lines.append("    - from: S_block_mid")
        lines.append("      to: S_block_closed")
        lines.append(f"      via: {last}")
        lines.append(f"  # first step: {first}")
    lines.append("")
    lines.append("state_after:")
    lines.append("  - id: AFTER_S_block_closed")
    lines.append(f'    en: "Tree-derived v1 complete for {unit_id}"')
    lines.append("")
    lines.append("exports:")
    for item in exports:
        lines.append(f"  - id: {item[0]}")
        if len(item) > 1 and item[1]:
            lines.append(f"    he: {yaml_quote(item[1])}")
        if len(item) > 2 and item[2]:
            lines.append(f"    he_translit: {yaml_quote(item[2])}")
        lines.append(f"    en: {yaml_quote(item[3] if len(item) > 3 else '')}")
    lines.append(f"  - id: EXPORT_tree_derived_v1_{unit_id}")
    lines.append('    en: "Unit reprocessed tree-first (one STEP per verse, arm-cited)"')
    lines.append("")
    lines.append("oral_notes:")
    lines.append("  - id: ORAL_policy")
    lines.append("    status: observation")
    lines.append('    work_en: "Exodus tree-derive oral policy"')
    lines.append("    comment_en: >")
    lines.append("      Written trees first. Mekhilta dual-track on law; MH possible; never silent-merge.")
    lines.append('    source: "[PROJECT]"')
    if genre == "decision_table" or meta.get("mekh") == "sample":
        for i, s in enumerate(mekh_samples(3), 1):
            lines.append(f"  - id: ORAL_mekhilta_{i}")
            lines.append("    status: dual_track")
            lines.append('    work_en: "Mekhilta"')
            lines.append(f'    locus_en: {yaml_quote("Mekhilta: " + s["section"])}')
            lines.append(f"    he_sample: {yaml_quote(s['he'])}")
            lines.append('    he_translit: "see Hebrew sample in Data/mekhilta_he.json"')
            lines.append(
                '    en_sample: "[EN-AID] Sample only; not derivation source; dual-track."'
            )
            lines.append("    comment_en: >")
            lines.append("      Dual-track sample — does not rewrite Written tree-derived STEPs.")
            lines.append('    source: "[ORAL][MEKHILTA]"')
            lines.append("    confidence: hypothesis")
    else:
        lines.append("  - id: ORAL_possible")
        lines.append("    status: possible_oral")
        lines.append('    work_en: "Midrash / Bavli / MH (named when quoted)"')
        lines.append("    comment_en: Dual-track only; narrative lean Written first.")
        lines.append('    source: "[ORAL]"')
    lines.append("")
    lines.append("scenarios:")
    for i, pv in enumerate(parsed_verses[:8], 1):
        lines.append(f"  - id: S{i}")
        lines.append(f'    title_en: "After Exod {pv["ch"]}:{pv["v"]} ({pv["sid"]})"')
        lines.append(
            f'    expect_en: "State advances via tree-derived {pv["sid"]}; arms cited in boot_steps."'
        )
    if len(parsed_verses) > 8:
        lines.append(f"  - id: S_last")
        last = parsed_verses[-1]
        lines.append(f'    title_en: "After final verse {last["ch"]}:{last["v"]}"')
        lines.append(f'    expect_en: "Block closed via {last["sid"]}."')
    lines.append("")
    lines.append("binary_trees:")
    lines.append("  display_policy_en: >")
    lines.append("    Always he + he_translit + en. Full tree_ascii per verse.")
    lines.append("  method_note_en: >")
    lines.append("    taamim_tree_parse.py v1; STEPs derived from top splits (tree_derived_v1).")
    lines.append('  data_source: "Data/Exod.xml"')
    lines.append('  parser: "taamim_tree_parse.py"')
    lines.append('  rule_set_version: "v1"')
    lines.append('  tags: ["[HE-STRUCT]"]')
    lines.append("  verse_trees:")

    coverage_blocks: list[str] = []
    word_total = 0
    for pv in parsed_verses:
        ch, v = pv["ch"], pv["v"]
        if pv.get("error") or not pv.get("pr"):
            lines.append(f"    Exod_{ch}_{v}:")
            lines.append(f'      verse: "{ch}:{v}"')
            lines.append(f'      osis_id: "{pv["osis"]}"')
            lines.append("      parser_status: error")
            lines.append(f"      error: {yaml_quote(pv.get('error', 'unknown'))}")
            continue
        words = pv["words"]
        arms = pv["arms"]
        wc = len(words)
        word_total += wc
        lines.append(f"    Exod_{ch}_{v}:")
        lines.append(f'      verse: "{ch}:{v}"')
        lines.append(f'      osis_id: "{pv["osis"]}"')
        lines.append(f'      parser_status: {pv["pr"].get("status", "unique")}')
        lines.append(f"      pure_binary: {pv['pure']}")
        lines.append(f"      word_count: {wc}")
        lines.append("      linear:")
        lines.append(f"        he: {yaml_quote(pv['linear_he'])}")
        lines.append(f"        he_translit: {yaml_quote(pv['linear_tr'])}")
        lines.append(
            f'        en: "Free gloss [EN-AID] — structure from Hebrew tree. Exod {ch}:{v}."'
        )
        lines.append("      top_binary_split:")
        lines.append("        comment: >")
        lines.append(f"          Top split ta'amim v1; maps_to ['{pv['sid']}'].")
        lines.append("        left_half:")
        lines.append('          side_en: "Left of top split"')
        lines.append("          head:")
        lines.append(f"            he: {yaml_quote(arms['left']['head_he'])}")
        lines.append(f'            he_translit: "{translit_plain(arms["left"]["head_he"])}"')
        lines.append(f'            en: "left-end leaf {arms["left"]["head_i"]}"')
        lines.append(f"            mark_en: {yaml_quote(arms['left']['head_mark'])}")
        lines.append("          phrase:")
        lines.append(f"            he: {yaml_quote(arms['left']['he'][:200])}")
        lines.append(f"            he_translit: {yaml_quote(arms['left']['he_translit'][:200])}")
        lines.append('            en: "left phrase arm (see tree_ascii)"')
        lines.append("        right_half:")
        lines.append('          side_en: "Right of top split"')
        lines.append("          phrase:")
        lines.append(f"            he: {yaml_quote(arms['right']['he'][:200])}")
        lines.append(f"            he_translit: {yaml_quote(arms['right']['he_translit'][:200])}")
        lines.append('            en: "right phrase arm (see tree_ascii)"')
        lines.append("      tree_ascii: |")
        for al in pv["ascii"].splitlines():
            lines.append(f"        {al}")
        lines.append(f'      maps_to: ["{pv["sid"]}"]')
        lines.append("      confidence: tested")
        lines.append('      source: "[HE-STRUCT][HE-WRITTEN]"')
        lines.append("")
        cov = [f'  - ref: "{pv["osis"]}"', "    words:"]
        for w in words:
            role, kind = role_for_plain(w["he_plain"])
            he_p = w["he_plain"].replace("/", "")
            tr = translit_plain(w["he_plain"])
            cov.append(
                f'      - {{index: {w["index"]}, he: {yaml_quote(he_p)}, he_translit: {yaml_quote(tr)}, '
                f'en: "leaf {w["index"]} ({he_p})", role: {role}, kind: {kind}, feeds: [{pv["sid"]}]}}'
            )
        coverage_blocks.append("\n".join(cov))

    lines.append("tree_coverage:")
    lines.append("  aspiration_en: >")
    lines.append("    100% word use; roles still provisional (glue/person/logic) pending TIR.")
    lines.append(f"  word_total: {word_total}")
    lines.append("  verses:")
    for cb in coverage_blocks:
        lines.append(cb)
    lines.append("")
    lines.append("confidence: hypothesis")
    lines.append("status_note_en: >")
    lines.append(
        f"  Tree-derived v1 (phase {phase}). One STEP per verse from top-split arms. "
        "Not binding religious law. Finer TIR/Oral deepen still open."
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--phase",
        required=True,
        help="Phase id: 1, 2a, 2b, 2c, 2d, 2e, 2f, or all",
    )
    ap.add_argument("--only", help="Single unit id")
    args = ap.parse_args()

    if args.only:
        phase = args.phase if args.phase in PHASES or args.phase == "all" else "manual"
        if args.phase in PHASES:
            phase = args.phase
        p = emit_unit(args.only, phase if phase != "all" else "manual")
        print(f"wrote {p.name}")
        return

    if args.phase == "all":
        # Unique units in spine order; label with first phase that lists them
        units_ph: list[tuple[str, str]] = []
        seen: set[str] = set()
        for ph in ("1", "2a", "2b", "2c", "2d", "2e", "2f"):
            for u in PHASES[ph]:
                if u not in seen:
                    seen.add(u)
                    units_ph.append((ph, u))
        for ph, u in units_ph:
            p = emit_unit(u, ph)
            print(f"phase {ph}: wrote {p.name}")
        print(f"done all units={len(units_ph)}")
        return

    if args.phase not in PHASES:
        print("unknown phase", args.phase, "want", list(PHASES) + ["all"], file=sys.stderr)
        sys.exit(1)
    phase = args.phase
    units = PHASES[phase]
    for u in units:
        p = emit_unit(u, phase)
        print(f"phase {phase}: wrote {p.name}")
    print(f"done phase={phase} units={len(units)}")


if __name__ == "__main__":
    main()
