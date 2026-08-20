#!/usr/bin/env python3
"""
Ta'amim tree parser — interprets versioned rules under logic/taamim_rules/.

Does NOT invent Torah legal logic. Builds phrase trees from cantillation marks only.
See logic/TAAMIM_TREE_PARSER.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
RULES_ROOT = ROOT / "logic" / "taamim_rules"
DATA = ROOT / "shelf" / "sources"

# Unicode block for Hebrew cantillation + related
TAAM_RE = re.compile(
    r"[\u0591-\u05AF\u05BD\u05C0]"
)
SOF_PASUQ = "\u05C3"
POETRY_BOOKS = {"Ps", "Prov", "Job", "Pss"}
# Job narrative frame uses prose accents (standard exception)
JOB_PROSE_FRAME_CHAPTERS = {1, 2, 42}


@dataclass
class MarkInfo:
    id: str
    kind: str
    rank: int
    en_name: str
    he_name: str = ""
    he_name_translit: str = ""


@dataclass
class WordTok:
    index: int
    he: str
    he_plain: str
    mark_id: str
    mark_en: str
    mark_kind: str  # disjunctive | conjunctive
    rank: int
    oshb_n: Optional[str] = None


@dataclass
class Node:
    kind: str  # leaf | phrase
    words: list[int] = field(default_factory=list)
    children: list["Node"] = field(default_factory=list)
    he: Optional[str] = None
    mark_id: Optional[str] = None
    mark_en: Optional[str] = None
    rank: Optional[int] = None

    def to_dict(self, toks: list[WordTok]) -> dict[str, Any]:
        if self.kind == "leaf":
            idxs = list(self.words)
            w_last = toks[idxs[-1]]
            he_parts = [toks[i].he for i in idxs]
            plain_parts = [toks[i].he_plain for i in idxs]
            return {
                "kind": "leaf",
                "word_index": idxs[0],  # first word (compat)
                "word_indices": idxs,  # full glue brick (v2)
                "he": " ".join(he_parts),
                "he_plain": " ".join(plain_parts),
                "mark_id": w_last.mark_id,
                "mark_en": w_last.mark_en,
                "rank": w_last.rank,
                "oshb_n": w_last.oshb_n,
                "glue": len(idxs) > 1,
            }
        return {
            "kind": "phrase",
            "word_indices": list(self.words),
            "he_span": " ".join(toks[i].he for i in self.words),
            "children": [c.to_dict(toks) for c in self.children],
            "arity": len(self.children),
        }


def load_active_version() -> str:
    cur = (RULES_ROOT / "CURRENT").read_text(encoding="utf-8").strip()
    if not cur:
        raise SystemExit("logic/taamim_rules/CURRENT is empty")
    return cur


def load_ranks(version: str, system: str = "prose") -> dict[str, Any]:
    """Load ranks_prose.yaml or ranks_poetry.yaml for the rule version."""
    fname = "ranks_poetry.yaml" if system == "poetry" else "ranks_prose.yaml"
    path = RULES_ROOT / version / fname
    if not path.exists():
        # Older packages (v1/v2) have prose only
        if system == "poetry":
            raise SystemExit(
                f"Missing poetry ranks: {path}. "
                f"Need version with ranks_poetry.yaml (v3+)."
            )
        path = RULES_ROOT / version / "ranks_prose.yaml"
    if not path.exists():
        raise SystemExit(f"Missing ranks file: {path}")
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(text)
    return _minimal_yaml_load(text)


def select_system(osis_id: str) -> str:
    """Return 'prose' or 'poetry' for this verse (Job frame = prose)."""
    parts = osis_id.split(".")
    book = parts[0]
    if book in ("Ps", "Pss", "Prov"):
        return "poetry"
    if book == "Job":
        try:
            ch = int(parts[1])
        except (IndexError, ValueError):
            return "poetry"
        if ch in JOB_PROSE_FRAME_CHAPTERS:
            return "prose"
        return "poetry"
    return "prose"


def _minimal_yaml_load(text: str) -> dict[str, Any]:
    """Tiny fallback if PyYAML missing: only supports our ranks file shape badly.
    Prefer PyYAML. For fallback, use json sidecar if present.
    """
    # Encode marks as JSON companion preferred; here parse simply via eval-unsafe avoided.
    # Require PyYAML for full support.
    raise SystemExit(
        "PyYAML is required. Install with: pip install pyyaml\n"
        f"(tried to load ranks without yaml)"
    )


def build_mark_table(ranks_doc: dict[str, Any]) -> tuple[dict[str, MarkInfo], MarkInfo]:
    table: dict[str, MarkInfo] = {}
    for ch, meta in ranks_doc["marks"].items():
        table[ch] = MarkInfo(
            id=meta["id"],
            kind=meta["kind"],
            rank=int(meta["rank"]),
            en_name=meta["en_name"],
            he_name=meta.get("he_name", ""),
            he_name_translit=meta.get("he_name_translit", ""),
        )
    z = ranks_doc["zero_conjunctive"]
    zero = MarkInfo(
        id=z["id"],
        kind=z["kind"],
        rank=int(z["rank"]),
        en_name=z["en_name"],
        he_name=z.get("he_name", ""),
        he_name_translit=z.get("he_name_translit", ""),
    )
    return table, zero


def strip_taamim_and_points(he: str) -> str:
    # Keep letters + maqqef-ish; drop nikkud and ta'amim for plain form
    return re.sub(r"[\u0591-\u05C7]", "", he)


def classify_word(
    he: str,
    is_last_word: bool,
    table: dict[str, MarkInfo],
    zero: MarkInfo,
) -> tuple[MarkInfo, list[str]]:
    found = TAAM_RE.findall(he)
    unknown = []
    disj: list[MarkInfo] = []
    conj: list[MarkInfo] = []
    for ch in found:
        info = table.get(ch)
        if info is None:
            unknown.append(f"U+{ord(ch):04X}")
            continue
        if info.kind == "ignore":
            continue
        if info.kind == "special_silluq_meteg":
            if is_last_word:
                disj.append(
                    MarkInfo(
                        id="silluq",
                        kind="disjunctive",
                        rank=1,
                        en_name="silluq (verse-end emperor)",
                        he_name="סִלּוּק",
                        he_name_translit="silluq",
                    )
                )
            # else meteg: ignore for structure
            continue
        if info.kind == "disjunctive":
            disj.append(info)
        elif info.kind == "conjunctive":
            conj.append(info)
    if unknown:
        raise ValueError(f"unknown ta'amim codepoints {unknown} in word {he!r}")
    if disj:
        best = min(disj, key=lambda m: m.rank)
        return best, found
    if conj:
        return conj[0], found
    return zero, found


def load_verse_words(book_file: Path, osis_id: str) -> list[tuple[str, Optional[str]]]:
    """Return list of (he, oshb_n) for verse.

    Uses ElementTree so nested markup and attribute order do not break word order.
    Every OSHB ``<w>`` becomes one terminal leaf candidate (v1 policy).
    """
    import xml.etree.ElementTree as ET

    try:
        root = ET.parse(book_file).getroot()
    except ET.ParseError as e:
        raise FileNotFoundError(f"Cannot parse XML {book_file}: {e}") from e

    # OSIS namespace (OSHB uses 2003/OSIS)
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0].strip("{")
    V = f"{{{ns}}}verse" if ns else "verse"
    W = f"{{{ns}}}w" if ns else "w"

    verse_el = None
    for v in root.iter(V):
        if v.get("osisID") == osis_id:
            verse_el = v
            break
    if verse_el is None:
        raise FileNotFoundError(f"Verse not found: {osis_id} in {book_file}")

    words: list[tuple[str, Optional[str]]] = []
    for w in verse_el.iter(W):
        # OSHB puts surface form in element text; fall back to all text if nested.
        he = w.text if w.text is not None else "".join(w.itertext())
        words.append((he or "", w.get("n")))
    return words


def book_file_for_osis(osis_id: str) -> Path:
    """Resolve OSHB book XML for an osis id.

    Search order:
      1. Data/{Book}.xml (Torah in this repo)
      2. MORPHHB_WLC env or /tmp/morphhb/wlc/{Book}.xml (full Tanakh when present)
    """
    book = osis_id.split(".")[0]
    # Standard morphhb short names
    mapping = {
        "Gen": "Gen.xml",
        "Exod": "Exod.xml",
        "Lev": "Lev.xml",
        "Num": "Num.xml",
        "Deut": "Deut.xml",
        "Josh": "Josh.xml",
        "Judg": "Judg.xml",
        "1Sam": "1Sam.xml",
        "2Sam": "2Sam.xml",
        "1Kgs": "1Kgs.xml",
        "2Kgs": "2Kgs.xml",
        "Isa": "Isa.xml",
        "Jer": "Jer.xml",
        "Ezek": "Ezek.xml",
        "Hos": "Hos.xml",
        "Joel": "Joel.xml",
        "Amos": "Amos.xml",
        "Obad": "Obad.xml",
        "Jonah": "Jonah.xml",
        "Mic": "Mic.xml",
        "Nah": "Nah.xml",
        "Hab": "Hab.xml",
        "Zeph": "Zeph.xml",
        "Hag": "Hag.xml",
        "Zech": "Zech.xml",
        "Mal": "Mal.xml",
        "Ps": "Ps.xml",
        "Job": "Job.xml",
        "Prov": "Prov.xml",
        "Ruth": "Ruth.xml",
        "Song": "Song.xml",
        "Eccl": "Eccl.xml",
        "Lam": "Lam.xml",
        "Esth": "Esth.xml",
        "Dan": "Dan.xml",
        "Ezra": "Ezra.xml",
        "Neh": "Neh.xml",
        "1Chr": "1Chr.xml",
        "2Chr": "2Chr.xml",
    }
    fname = mapping.get(book)
    if not fname:
        raise FileNotFoundError(
            f"Unknown book code {book!r} in {osis_id}. Extend book_file_for_osis mapping."
        )
    local = DATA / fname
    if local.exists():
        return local
    import os

    morph_root = Path(os.environ.get("MORPHHB_WLC", "/tmp/morphhb/wlc"))
    remote = morph_root / fname
    if remote.exists():
        return remote
    raise FileNotFoundError(
        f"No OSHB XML for {book}: tried {local} and {remote}. "
        f"Add Data/{fname} or set MORPHHB_WLC."
    )


def collect_leaf_indices(node: dict[str, Any]) -> list[int]:
    """In-order word indices covered by every leaf (must equal 0..n-1).

    v2 leaves may cover **multiple** words (glue brick); flatten those indices.
    """
    if node.get("kind") == "leaf":
        # multi-word brick: word_indices preferred; legacy single word_index
        if "word_indices" in node and node["word_indices"] is not None:
            return [int(i) for i in node["word_indices"]]
        return [int(node["word_index"])]
    out: list[int] = []
    for c in node.get("children") or []:
        out.extend(collect_leaf_indices(c))
    return out


def leaf_complete(result: dict[str, Any]) -> bool:
    """True if every word appears exactly once under some leaf (L→R order)."""
    tree = result.get("tree")
    words = result.get("words") or []
    if not tree or result.get("status") != "unique":
        return False
    leaves = collect_leaf_indices(tree)
    return leaves == list(range(len(words)))


def pure_binary_tree(node: dict[str, Any]) -> bool:
    """v2 invariant: every phrase has exactly 2 children; leaves are terminals."""
    if node.get("kind") == "leaf":
        return True
    kids = node.get("children") or []
    if len(kids) != 2:
        return False
    return all(pure_binary_tree(c) for c in kids)


@dataclass
class Brick:
    """Terminal glue unit: one or more words ending in a disjunctive (v2)."""

    word_indices: list[int]
    end_rank: int
    end_mark_id: str
    end_mark_en: str


def glue_bricks(toks: list[WordTok]) -> list[Brick]:
    """Layer A: conjunctives/zero glue until a disjunctive closes the brick."""
    if not toks:
        return []
    bricks: list[Brick] = []
    cur: list[int] = []
    for t in toks:
        cur.append(t.index)
        if t.mark_kind == "disjunctive":
            bricks.append(
                Brick(
                    word_indices=list(cur),
                    end_rank=t.rank,
                    end_mark_id=t.mark_id,
                    end_mark_en=t.mark_en,
                )
            )
            cur = []
    if cur:
        # Trailing conjunctives without disjunctive head (rare / corrupt marks)
        last = toks[cur[-1]]
        bricks.append(
            Brick(
                word_indices=list(cur),
                end_rank=last.rank,
                end_mark_id=last.mark_id,
                end_mark_en=last.mark_en,
            )
        )
    return bricks


def tokenize_verse(
    osis_id: str,
    table: dict[str, MarkInfo],
    zero: MarkInfo,
) -> list[WordTok]:
    path = book_file_for_osis(osis_id)
    raw = load_verse_words(path, osis_id)
    toks: list[WordTok] = []
    n = len(raw)
    for i, (he, oshb_n) in enumerate(raw):
        is_last = i == n - 1
        info, _ = classify_word(he, is_last, table, zero)
        kind = "disjunctive" if info.kind == "disjunctive" else "conjunctive"
        toks.append(
            WordTok(
                index=i,
                he=he,
                he_plain=strip_taamim_and_points(he),
                mark_id=info.id,
                mark_en=info.en_name,
                mark_kind=kind,
                rank=info.rank,
                oshb_n=oshb_n,
            )
        )
    return toks


def parse_span_bricks(toks: list[WordTok], bricks: list[Brick], lo: int, hi: int) -> Node:
    """Parse bricks[lo:hi] (half-open) with continuous binary dichotomy (v2).

    Leaves are glue bricks (1+ words). Internal nodes are always binary.
    """
    if hi <= lo:
        raise ValueError("empty brick span")
    if hi - lo == 1:
        b = bricks[lo]
        last = toks[b.word_indices[-1]]
        return Node(
            kind="leaf",
            words=list(b.word_indices),
            he=" ".join(toks[i].he for i in b.word_indices),
            mark_id=last.mark_id,
            mark_en=last.mark_en,
            rank=last.rank,
        )
    # Interior brick ends are split candidates (0 .. hi-lo-2 relative → lo .. hi-2)
    candidates = list(range(lo, hi - 1))
    best_rank = min(bricks[i].end_rank for i in candidates)
    k = next(i for i in candidates if bricks[i].end_rank == best_rank)  # leftmost
    left = parse_span_bricks(toks, bricks, lo, k + 1)
    right = parse_span_bricks(toks, bricks, k + 1, hi)
    word_ids: list[int] = []
    for i in range(lo, hi):
        word_ids.extend(bricks[i].word_indices)
    return Node(
        kind="phrase",
        words=word_ids,
        children=[left, right],
    )


def parse_span(
    toks: list[WordTok],
    lo: int,
    hi: int,
    version: Optional[str] = None,
) -> Node:
    """Parse toks[lo:hi] half-open.

    v2+ (default CURRENT): glue bricks first, then binary dichotomy on bricks.
    Never returns flat n-ary conjunctive chains of single-word leaves.
    """
    if hi <= lo:
        raise ValueError("empty span")
    version = version or load_active_version()
    # v1 path retained for --version v1 regression only
    if version == "v1":
        return _parse_span_v1_words(toks, lo, hi)
    span_toks = toks[lo:hi]
    # Brick word indices stay absolute (from WordTok.index)
    bricks = glue_bricks(span_toks)
    if not bricks:
        raise ValueError("no bricks")
    return parse_span_bricks(toks, bricks, 0, len(bricks))


def _parse_span_v1_words(toks: list[WordTok], lo: int, hi: int) -> Node:
    """Legacy v1: word-level dichotomy (may emit n-ary conj chains)."""
    if hi <= lo:
        raise ValueError("empty span")
    if hi - lo == 1:
        w = toks[lo]
        return Node(
            kind="leaf",
            words=[lo],
            he=w.he,
            mark_id=w.mark_id,
            mark_en=w.mark_en,
            rank=w.rank,
        )
    candidates = [
        i for i in range(lo, hi - 1) if toks[i].mark_kind == "disjunctive"
    ]
    if not candidates:
        kids = [_parse_span_v1_words(toks, i, i + 1) for i in range(lo, hi)]
        return Node(kind="phrase", words=list(range(lo, hi)), children=kids)
    best_rank = min(toks[i].rank for i in candidates)
    k = next(i for i in candidates if toks[i].rank == best_rank)
    left = _parse_span_v1_words(toks, lo, k + 1)
    right = _parse_span_v1_words(toks, k + 1, hi)
    return Node(
        kind="phrase",
        words=list(range(lo, hi)),
        children=[left, right],
    )


def poetry_book(osis_id: str) -> bool:
    """True if verse uses poetry system (not Job prose frame)."""
    return select_system(osis_id) == "poetry"


def parse_verse(
    osis_id: str,
    version: Optional[str] = None,
    force_prose: bool = False,
    force_poetry: bool = False,
) -> dict[str, Any]:
    version = version or load_active_version()
    if force_prose and force_poetry:
        return {
            "osis_id": osis_id,
            "rule_set_version": version,
            "system": "fail",
            "status": "fail",
            "tree": None,
            "words": [],
            "notes": ["Cannot set both force_prose and force_poetry"],
        }
    if force_prose:
        system = "prose"
    elif force_poetry:
        system = "poetry"
    else:
        system = select_system(osis_id)

    # Pre-v3 packages have no poetry ranks
    ranks_path = RULES_ROOT / version / (
        "ranks_poetry.yaml" if system == "poetry" else "ranks_prose.yaml"
    )
    if system == "poetry" and not ranks_path.exists():
        return {
            "osis_id": osis_id,
            "rule_set_version": version,
            "system": "poetry",
            "status": "fail",
            "tree": None,
            "words": [],
            "notes": [
                f"Poetry ranks not in {version}. Use v3+ or --force-prose (debug only)."
            ],
        }

    try:
        ranks_doc = load_ranks(version, system=system)
    except SystemExit as e:
        return {
            "osis_id": osis_id,
            "rule_set_version": version,
            "system": system,
            "status": "fail",
            "tree": None,
            "words": [],
            "notes": [str(e)],
        }
    table, zero = build_mark_table(ranks_doc)

    try:
        toks = tokenize_verse(osis_id, table, zero)
    except Exception as e:
        return {
            "osis_id": osis_id,
            "rule_set_version": version,
            "system": system,
            "status": "fail",
            "tree": None,
            "words": [],
            "notes": [str(e)],
        }

    if not toks:
        return {
            "osis_id": osis_id,
            "rule_set_version": version,
            "system": system,
            "status": "fail",
            "tree": None,
            "words": [],
            "notes": ["empty verse"],
        }

    # Glue+binary for v2+; v1 word-level only when version is v1
    tree = parse_span(toks, 0, len(toks), version=version)
    words_out = [
        {
            "index": t.index,
            "he": t.he,
            "he_plain": t.he_plain,
            "mark_id": t.mark_id,
            "mark_en": t.mark_en,
            "mark_kind": t.mark_kind,
            "rank": t.rank,
            "oshb_n": t.oshb_n,
        }
        for t in toks
    ]
    tree_dict = tree.to_dict(toks)
    leaves = collect_leaf_indices(tree_dict)
    complete = leaves == list(range(len(toks)))
    bricks = glue_bricks(toks)
    pure_bin = pure_binary_tree(tree_dict) if version != "v1" else None
    notes: list[str] = []
    if not complete:
        notes.append(
            f"LEAF_INCOMPLETE: expected indices 0..{len(toks)-1}, got {leaves}"
        )
    if version != "v1" and pure_bin is False:
        notes.append("NOT_PURE_BINARY: v2 requires binary phrases only after glue")
    return {
        "osis_id": osis_id,
        "rule_set_version": version,
        "system": system,
        "status": "unique",
        "tree": tree_dict,
        "words": words_out,
        "bricks": [
            {
                "word_indices": b.word_indices,
                "he_plain": " ".join(toks[i].he_plain for i in b.word_indices),
                "end_mark_id": b.end_mark_id,
                "end_mark_en": b.end_mark_en,
                "end_rank": b.end_rank,
            }
            for b in bricks
        ],
        "brick_count": len(bricks),
        "leaf_indices": leaves,
        "leaf_complete": complete,
        "pure_binary": pure_bin,
        "word_count": len(toks),
        "notes": notes,
    }


def tree_bracket_string(node: dict[str, Any]) -> str:
    if node["kind"] == "leaf":
        return node["he"]
    return "[" + " ".join(tree_bracket_string(c) for c in node["children"]) + "]"


def _tree_node_label(node: dict[str, Any], max_span: int = 48) -> str:
    """One-line label for a tree node (English-friendly meta + Hebrew)."""
    if node.get("kind") == "leaf":
        he = node.get("he") or ""
        mark = node.get("mark_en") or node.get("mark_id") or ""
        rank = node.get("rank")
        idxs = node.get("word_indices") or (
            [node["word_index"]] if node.get("word_index") is not None else []
        )
        if len(idxs) == 1:
            idx_s = f"[{idxs[0]}]"
        elif idxs:
            idx_s = f"[{idxs[0]}-{idxs[-1]}]"
        else:
            idx_s = "leaf"
        glue = " GLUE" if node.get("glue") or len(idxs) > 1 else ""
        parts = [f"{idx_s}{glue}", he]
        if mark:
            parts.append(f"({mark}")
            if rank is not None:
                parts[-1] = parts[-1] + f", rank={rank})"
            else:
                parts[-1] = parts[-1] + ")"
        elif rank is not None:
            parts.append(f"(rank={rank})")
        return " ".join(parts)

    # phrase / internal node — higher in the hierarchy
    span = node.get("he_span") or ""
    if len(span) > max_span:
        span = span[: max_span - 1] + "…"
    n_words = len(node.get("word_indices") or [])
    kids = node.get("children") or []
    shape = "binary" if len(kids) == 2 else f"{len(kids)}-ary" if kids else "empty"
    bits = ["PHRASE", f"({shape}", f"{n_words}w)"]
    if span:
        bits.append(span)
    return " ".join(bits)


def tree_ascii(
    node: dict[str, Any],
    *,
    prefix: str = "",
    is_last: bool = True,
    is_root: bool = True,
) -> list[str]:
    """
    PERMANENT tree display model (owner lock — logic/TREE_DISPLAY.md).

    Top-down ASCII tree: highest (root) first, then children below.
    Root is printed first; leaves are lowest in the display.
    Same string is stored as unit binary_trees.*.tree_ascii.
    """
    lines: list[str] = []
    label = _tree_node_label(node)
    if is_root:
        lines.append(label)
        child_prefix = ""
    else:
        branch = "└── " if is_last else "├── "
        lines.append(prefix + branch + label)
        child_prefix = prefix + ("    " if is_last else "│   ")

    children = node.get("children") or []
    for i, child in enumerate(children):
        last = i == len(children) - 1
        lines.extend(
            tree_ascii(
                child,
                prefix=child_prefix,
                is_last=last,
                is_root=False,
            )
        )
    return lines


def tree_ascii_string(node: dict[str, Any]) -> str:
    """Highest → lowest (root at top)."""
    return "\n".join(tree_ascii(node))


def run_golden_tests(version: Optional[str] = None) -> int:
    version = version or load_active_version()
    path = RULES_ROOT / version / "tests" / "golden.json"
    if not path.exists():
        print(f"No golden file at {path}", file=sys.stderr)
        return 1
    cases = json.loads(path.read_text(encoding="utf-8"))
    failed = 0
    for case in cases:
        osis = case["osis_id"]
        result = parse_verse(
            osis,
            version=version,
            force_prose=case.get("force_prose", False),
            force_poetry=case.get("force_poetry", False),
        )
        exp_status = case.get("expect_status", "unique")
        if result["status"] != exp_status:
            print(f"FAIL {osis}: status {result['status']} != {exp_status} notes={result['notes']}")
            failed += 1
            continue
        if "expect_system" in case and result.get("system") != case["expect_system"]:
            print(
                f"FAIL {osis}: system {result.get('system')} != {case['expect_system']}"
            )
            failed += 1
            continue
        if exp_status != "unique":
            print(f"OK   {osis}: status={exp_status}")
            continue
        # Check mark sequence
        if "expect_mark_ids" in case:
            got = [w["mark_id"] for w in result["words"]]
            if got != case["expect_mark_ids"]:
                print(f"FAIL {osis}: marks {got} != {case['expect_mark_ids']}")
                failed += 1
                continue
        # Optional bracket structure on plain forms
        if "expect_bracket_plain" in case:
            # build plain bracket from tree (leaf may be multi-word brick)
            def plain_br(n: dict) -> str:
                if n["kind"] == "leaf":
                    return re.sub(r"[\u0591-\u05C7]", "", n["he"]).strip()
                return "[" + " ".join(plain_br(c) for c in n["children"]) + "]"

            got_b = plain_br(result["tree"])
            if got_b != case["expect_bracket_plain"]:
                print(f"FAIL {osis}: tree\n  got:  {got_b}\n  want: {case['expect_bracket_plain']}")
                failed += 1
                continue
        # Every word must appear exactly once under leaves (full depth)
        if case.get("expect_leaf_complete", True) and exp_status == "unique":
            if not result.get("leaf_complete"):
                print(
                    f"FAIL {osis}: leaf_complete=False "
                    f"leaves={result.get('leaf_indices')} n={result.get('word_count')}"
                )
                failed += 1
                continue
            if "expect_word_count" in case:
                if result.get("word_count") != case["expect_word_count"]:
                    print(
                        f"FAIL {osis}: word_count {result.get('word_count')} "
                        f"!= {case['expect_word_count']}"
                    )
                    failed += 1
                    continue
        if case.get("expect_pure_binary") and exp_status == "unique":
            if not result.get("pure_binary"):
                print(f"FAIL {osis}: pure_binary=False (n-ary phrase remains)")
                failed += 1
                continue
        if "expect_brick_count" in case and exp_status == "unique":
            if result.get("brick_count") != case["expect_brick_count"]:
                print(
                    f"FAIL {osis}: brick_count {result.get('brick_count')} "
                    f"!= {case['expect_brick_count']}"
                )
                failed += 1
                continue
        print(f"OK   {osis} (v={version})")
    if failed:
        print(f"{failed} failed")
        return 1
    print(f"All {len(cases)} golden tests passed ({version})")
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Parse ta'amim trees under versioned rules")
    p.add_argument("osis_id", nargs="?", help="e.g. Lev.12.2")
    p.add_argument("--version", help="rule set version (default: CURRENT)")
    p.add_argument("--test", action="store_true", help="run golden tests")
    p.add_argument(
        "--force-prose",
        action="store_true",
        help="force prose ranks (debug on poetry books)",
    )
    p.add_argument(
        "--force-poetry",
        action="store_true",
        help="force poetry ranks (debug on non-poetry verses)",
    )
    p.add_argument(
        "--bracket",
        action="store_true",
        help="print flat bracket string of the tree",
    )
    p.add_argument(
        "--tree",
        action="store_true",
        help=(
            "print PERMANENT top-down tree model "
            "(root first; binary PHRASE + GLUE; see logic/TREE_DISPLAY.md)"
        ),
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="also print full JSON (default when neither --tree nor --bracket)",
    )
    p.add_argument(
        "--leaves",
        action="store_true",
        help="print every leaf: index, plain he, mark, rank (full depth check)",
    )
    p.add_argument("--pretty", action="store_true", default=True)
    args = p.parse_args(argv)

    if args.test:
        return run_golden_tests(args.version)

    if not args.osis_id:
        p.print_help()
        return 2

    result = parse_verse(
        args.osis_id,
        version=args.version,
        force_prose=args.force_prose,
        force_poetry=args.force_poetry,
    )
    tree = result.get("tree")
    printed_view = False
    if args.tree and tree:
        print(tree_ascii_string(tree))
        printed_view = True
    if args.bracket and tree:
        print(tree_bracket_string(tree))
        printed_view = True
    if args.leaves and result.get("status") == "unique":
        print(
            f"# bricks/leaves osis={result.get('osis_id')} "
            f"words={result.get('word_count')} bricks={result.get('brick_count')} "
            f"leaf_complete={result.get('leaf_complete')} "
            f"pure_binary={result.get('pure_binary')} "
            f"status={result.get('status')} v={result.get('rule_set_version')}"
        )
        # Prefer brick list (glue units); fall back to word rows
        bricks = result.get("bricks") or []
        if bricks:
            for bi, b in enumerate(bricks):
                print(
                    f"  brick {bi:02d}  words={b['word_indices']}  "
                    f"{b['he_plain']!s:40s}  "
                    f"end={b['end_mark_id']} rank={b['end_rank']}"
                )
        else:
            for w in result.get("words") or []:
                print(
                    f"{w['index']:3d}  {w['he_plain']:20s}  "
                    f"{w['mark_id']:20s}  rank={w['rank']}  {w['mark_kind']}"
                )
        printed_view = True
    # Default: JSON. With --tree/--bracket/--leaves only, skip JSON unless --json.
    if args.json or not printed_view:
        print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    ok = result["status"] == "unique" and result.get("leaf_complete", True)
    if result.get("rule_set_version") not in (None, "v1"):
        ok = ok and result.get("pure_binary", True) is not False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
