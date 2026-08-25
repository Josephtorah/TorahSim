#!/usr/bin/env python3
"""
enumerate_blocks.py — the pre-enumeration pass (THE_STEPS Step 3, speed
ruling of 2026-08-25): compute ahead, for every remaining Genesis block,
the full enumeration and register classification, so each reading sitting
starts with its declared list already printed.

Per block (gen_09..gen_73): every distinct linked source in the span
(data/derivation.sqlite, export_links), classified by the approved
provenance register (logic/oral_provenance/v1/works.yaml — ordered
prefix rules, FIRST match wins), the declared set (chain_primary +
Onkelos per-verse), standing-verdict credits from all prior triage
ledgers, and cross-block duplicate notes at the parashah grain (one
reading pass covers them all). Output: one prep file per parashah in
logic/oral_triage/prep/ plus an index. Prep files are working plans,
not ledgers — the sitting's ledger remains the record.

Validation anchors (workshop numbers, corrected + register-amended
2026-08-25): gen_08 enumerates 3,968 · gen_09 enumerates 1,972 and
declares 83 = 75 chain primaries (incl. the four Tosefta refs the
owner-approved register amendment brought into scope) + 8 Onkelos.

Run from the repo root: python3 press/enumerate_blocks.py
"""
import re, sqlite3, sys, collections
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "vendor"))
import yaml

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "derivation.sqlite"
REGISTER = ROOT / "logic" / "oral_provenance" / "v1" / "works.yaml"
UNITS = ROOT / "logic" / "units"
OUT = ROOT / "logic" / "oral_triage" / "prep"
DATE = "2026-08-25"

# The twelve weekly portions of Genesis — the reading grain.
PARASHIYOT = [
    ("Bereshit",    (1, 1),   (6, 8)),
    ("Noach",       (6, 9),   (11, 32)),
    ("Lech Lecha",  (12, 1),  (17, 27)),
    ("Vayera",      (18, 1),  (22, 24)),
    ("Chayei Sarah",(23, 1),  (25, 18)),
    ("Toledot",     (25, 19), (28, 9)),
    ("Vayetze",     (28, 10), (32, 3)),
    ("Vayishlach",  (32, 4),  (36, 43)),
    ("Vayeshev",    (37, 1),  (40, 23)),
    ("Miketz",      (41, 1),  (44, 17)),
    ("Vayigash",    (44, 18), (47, 27)),
    ("Vayechi",     (47, 28), (50, 26)),
]

# Bare-tractate prefix rules can catch liturgy volumes ("Shabbat Siddur
# Sefard Linear" — twice excluded with cause in the ledgers already).
FALSE_POSITIVE_MARKS = ("Siddur", "Machzor", "Haggadah")


def load_rules():
    reg = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))
    return [(r["prefix"], r["status"]) for r in reg["rules"]]


def classify(work, rules):
    for prefix, status in rules:
        if work.startswith(prefix):
            if status == "chain_primary" and any(m in work for m in FALSE_POSITIVE_MARKS):
                return "EXCLUDED_false_positive"
            return status
    return "unmatched"


def block_spans():
    """gen_NN unit id -> ordered list of (chapter, verse) in its span."""
    cx = sqlite3.connect(ROOT / "data" / "tanakh.sqlite")
    vmax = dict(cx.execute(
        "SELECT chapter, MAX(verse) FROM verses WHERE book='Gen' GROUP BY chapter"))
    cx.close()
    spans = {}
    for path in sorted(UNITS.glob("gen_*.yaml")):
        uid = path.stem
        num = int(uid.split("_")[1])
        if num < 9:
            continue
        m = re.search(r'refs:\s*"?(\d+):(\d+)-(?:(\d+):)?(\d+)"?', path.read_text(encoding="utf-8"))
        c1, v1 = int(m.group(1)), int(m.group(2))
        c2 = int(m.group(3)) if m.group(3) else c1
        v2 = int(m.group(4))
        verses = []
        for ch in range(c1, c2 + 1):
            lo = v1 if ch == c1 else 1
            hi = v2 if ch == c2 else vmax[ch]
            verses += [(ch, v) for v in range(lo, hi + 1)]
        spans[uid] = verses
    return spans


def parashah_of(ch, v):
    for name, (c1, v1), (c2, v2) in PARASHIYOT:
        if (ch, v) >= (c1, v1) and (ch, v) <= (c2, v2):
            return name
    raise KeyError((ch, v))


def main():
    rules = load_rules()
    spans = block_spans()
    cx = sqlite3.connect(DB)

    # standing verdicts from every prior ledger (the credit registry)
    credits = {}
    for ref, unit, cls in cx.execute(
            "SELECT source_ref, unit, verdict_class FROM triage"):
        credits.setdefault(ref, (unit, cls))

    blocks = {}       # uid -> dict of computed facts
    by_parashah = collections.defaultdict(list)
    for uid, verses in spans.items():
        ch_set = collections.defaultdict(set)
        for ch, v in verses:
            ch_set[ch].add(v)
        refs = {}     # source_ref -> work
        onkelos = set()
        for ch, vs in ch_set.items():
            q = (f"SELECT DISTINCT source_ref, source_work FROM export_links "
                 f"WHERE anchor_book='Gen' AND anchor_chapter={ch} "
                 f"AND anchor_verse IN ({','.join(map(str, sorted(vs)))})")
            for ref, work in cx.execute(q):
                if work.startswith("Onkelos"):
                    onkelos.add(ref)
                else:
                    refs[ref] = work
        classed = collections.defaultdict(list)
        for ref, work in sorted(refs.items()):
            classed[classify(work, rules)].append(ref)
        primaries = classed.get("chain_primary", [])
        pre = [(r, *credits[r]) for r in primaries if r in credits]
        fresh = [r for r in primaries if r not in credits]
        para = parashah_of(*verses[0])
        end_para = parashah_of(*verses[-1])
        blocks[uid] = dict(
            verses=verses, para=para, crosses=(para != end_para),
            enumerated=len(refs) + len(onkelos), classed=classed,
            onkelos=sorted(onkelos), primaries=primaries,
            pre=pre, fresh=fresh)
        by_parashah[para].append(uid)

    # cross-block duplicates at the parashah grain
    for para, uids in by_parashah.items():
        seen = collections.defaultdict(list)
        for uid in uids:
            for r in blocks[uid]["primaries"]:
                seen[r].append(uid)
        for uid in uids:
            blocks[uid]["also"] = {
                r: [u for u in seen[r] if u != uid]
                for r in blocks[uid]["primaries"] if len(seen[r]) > 1}

    OUT.mkdir(exist_ok=True)
    index_lines = [
        f"# PRE-ENUMERATION INDEX — the Genesis walk ({DATE})",
        "",
        "Computed per the speed ruling (THE_STEPS Step 3). One prep file",
        "per parashah; ledgers per block remain the record of reading.",
        "Declared = register chain_primary + Onkelos per-verse. Credits =",
        "standing verdicts from prior triage ledgers, never re-read.",
        "",
        "| parashah | blocks | enumerated | declared | credited | fresh to read |",
        "|---|---|---|---|---|---|",
    ]
    tot = collections.Counter()
    for pi, (para, _, _) in enumerate(PARASHIYOT, 1):
        uids = by_parashah.get(para)
        if not uids:
            continue
        fname = f"PREP_{pi:02d}_{para.replace(' ', '_')}_{DATE}.md"
        lines = [
            f"# PREP — parashat {para} ({DATE})",
            "",
            f"Blocks: {', '.join(uids)}. One sequential reading pass over this",
            "portion's primaries covers every block below (speed ruling (a));",
            "each block still gets its own ledger.",
            "",
        ]
        for uid in uids:
            b = blocks[uid]
            v0, v1_ = b["verses"][0], b["verses"][-1]
            span = f"{v0[0]}:{v0[1]}-{v1_[0]}:{v1_[1]}" if v0[0] != v1_[0] else f"{v0[0]}:{v0[1]}-{v1_[1]}"
            declared = len(b["primaries"]) + len(b["onkelos"])
            lines += [
                f"## {uid} — Genesis {span}",
                "",
                f"- enumerated: {b['enumerated']} distinct linked sources",
                f"- declared: {declared} = {len(b['primaries'])} chain primaries + {len(b['onkelos'])} Onkelos verses",
                f"- credited (standing verdicts): {len(b['pre'])} · FRESH TO READ: {len(b['fresh'])}",
            ]
            if b["crosses"]:
                lines.append("- NOTE: span crosses a parashah boundary — read both portions' runs")
            excl = b["classed"].get("EXCLUDED_false_positive", [])
            if excl:
                lines.append(f"- excluded with cause (register false positive): {' · '.join(excl)}")
            outside = b["enumerated"] - declared - len(excl)
            lines += [
                f"- outside declared scope (open narrowing, per the standing default): {outside}",
                "",
                "| # | source | status |",
                "|---|--------|--------|",
            ]
            n = 0
            for r in b["primaries"]:
                n += 1
                if any(r == p[0] for p in b["pre"]):
                    unit, cls = credits[r]
                    note = f"CREDIT — {cls} at {unit}"
                elif b["also"].get(r):
                    note = "fresh · also in " + ", ".join(b["also"][r])
                else:
                    note = "fresh"
                lines.append(f"| {n} | {r} | {note} |")
            lines.append(f"| — | Onkelos Genesis {span} ({len(b['onkelos'])} verses) | derive-time credit (foundation layer) |")
            lines.append("")
            tot.update(enumerated=b["enumerated"], declared=declared,
                       credited=len(b["pre"]), fresh=len(b["fresh"]))
        (OUT / fname).write_text("\n".join(lines), encoding="utf-8")
        pe = sum(blocks[u]["enumerated"] for u in uids)
        pd = sum(len(blocks[u]["primaries"]) + len(blocks[u]["onkelos"]) for u in uids)
        pc = sum(len(blocks[u]["pre"]) for u in uids)
        pf = sum(len(blocks[u]["fresh"]) for u in uids)
        index_lines.append(f"| {para} | {len(uids)} | {pe} | {pd} | {pc} | {pf} |")
        print(f"{fname}: {len(uids)} blocks, {pd} declared, {pf} fresh")
    index_lines += [
        f"| TOTAL | 65 | {tot['enumerated']} | {tot['declared']} | {tot['credited']} | {tot['fresh']} |",
        "",
    ]
    (OUT / f"PREP_00_INDEX_{DATE}.md").write_text("\n".join(index_lines), encoding="utf-8")

    # validation anchors
    g9 = blocks["gen_09_helper_woman_first_speech"]
    print(f"\nVALIDATION gen_09: enumerated {g9['enumerated']} (expect 1972), "
          f"declared {len(g9['primaries'])}+{len(g9['onkelos'])} (expect 75+8)")
    hebrew = re.compile(r"[א-ת]")
    for uid, b in blocks.items():
        for r in b["primaries"]:
            assert not hebrew.search(r), f"Hebrew in declared row ({uid}): {r}"
    print("declared rows: no un-glossed Hebrew — gloss-lint safe")


if __name__ == "__main__":
    main()
