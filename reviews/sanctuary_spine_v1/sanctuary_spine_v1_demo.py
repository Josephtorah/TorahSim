#!/usr/bin/env python3
"""
Sanctuary spine V1 — educational code example (not a law engine).

Demonstrates the demo package in `reviews/sanctuary_spine_v1/`:
  Exodus INSTALL → Lev 1 OPERATE → Num cloud OPS → Deut RECOMPILE

What this script does:
  - Holds the frozen free-name WRITE/USE tables as data
  - Dry-runs name resolve (PASS / INSTALL_ONLY / PASS_recompile / …)
  - Prints the cattle olah procedure (Lev 1:1–9) as ordered steps
  - Simulates the cloud stay/go FSM with the Num 10:11–13 instance
  - Optionally parses key verses with taamim_tree_parse.py (if run from repo)

What this script does NOT do:
  - Invent binding religious law
  - Replace Hebrew derivation (data is a frozen teaching dump of the demo docs)
  - Full Torah interpreter / world VM

Usage (from repo root):
  python3 reviews/sanctuary_spine_v1/sanctuary_spine_v1_demo.py
  python3 reviews/sanctuary_spine_v1/sanctuary_spine_v1_demo.py --trees
  python3 reviews/sanctuary_spine_v1/sanctuary_spine_v1_demo.py --resolve-only

See also: TUTORIAL_BEGINNERS_*.md · TUTORIAL_FULLSTACK_*.md · DEMO_*_HUB_*.md
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[2]  # Torah_Grok/
DEMO_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Domain: free names (he + translit + en always)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class HeTriple:
    """Never bare Hebrew: surface + how to say + English gloss."""

    he: str
    he_translit: str
    en: str

    def show(self) -> str:
        return f'{self.he} / *{self.he_translit}* / "{self.en}"'


class ResolveResult(str, Enum):
    PASS = "PASS"
    PASS_ALIAS = "PASS_alias"
    PASS_RECOMPILE = "PASS_recompile"
    INSTALL_ONLY = "INSTALL_ONLY"
    LOCAL = "LOCAL"
    OPEN = "OPEN"


@dataclass
class WriteSite:
    """Where Exodus (or none) installs a symbol for V1."""

    ref: str  # e.g. Exod.28.1
    op: str  # DECLARE_GOAL, ACTIVATE, …
    note_en: str = ""


@dataclass
class UseSite:
    """Where a later book reads the free name."""

    ref: str
    surface: HeTriple
    path: str = ""  # ta'amim path prefix when known
    note_en: str = ""


@dataclass
class Symbol:
    handle: str
    name: HeTriple
    writes: list[WriteSite] = field(default_factory=list)
    uses: list[UseSite] = field(default_factory=list)
    result: ResolveResult = ResolveResult.OPEN
    confidence: str = "hypothesis"  # tested | hypothesis | open


# ---------------------------------------------------------------------------
# Frozen V1 data (mirrors CHARTER + WRITES + USES docs)
# ---------------------------------------------------------------------------


def build_symbol_table() -> list[Symbol]:
    """Install free names from the V1 demo package."""
    return [
        Symbol(
            handle="SYM_mikdash",
            name=HeTriple("מִקְדָּשׁ", "mikdash", "sanctuary"),
            writes=[WriteSite("Exod.25.8", "DECLARE_GOAL", "make Me a sanctuary; I will dwell among them")],
            uses=[],
            result=ResolveResult.INSTALL_ONLY,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_tavnit",
            name=HeTriple("תַּבְנִית", "tavnit", "pattern / blueprint"),
            writes=[WriteSite("Exod.25.9", "DECLARE_PATTERN", "pattern of mishkan and vessels")],
            uses=[],
            result=ResolveResult.INSTALL_ONLY,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_mishkan",
            name=HeTriple("מִשְׁכָּן", "mishkan", "dwelling / Tabernacle"),
            writes=[
                WriteSite("Exod.25.9", "DECLARE", "as pattern object"),
                WriteSite("Exod.40.34", "FILL", "glory fills the mishkan"),
            ],
            uses=[
                UseSite(
                    "Num.9.15",
                    HeTriple("הַמִּשְׁכָּן", "ha-mishkan", "the dwelling"),
                    note_en="cloud covers mishkan",
                ),
                UseSite(
                    "Num.10.11",
                    HeTriple("מִשְׁכַּן הָעֵדֻת", "mishkan ha-edut", "dwelling of the testimony"),
                    path="RRRL",
                    note_en="cloud lifts from mishkan",
                ),
            ],
            result=ResolveResult.PASS,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_ohel_moed",
            name=HeTriple("אֹהֶל מוֹעֵד", "ohel mo'ed", "Tent of Meeting"),
            writes=[
                WriteSite("Exod.27.21", "NAME", "first clear ohel mo'ed in Torah"),
                WriteSite("Exod.40.34", "ACTIVATE_SITE", "cloud covers Tent"),
            ],
            uses=[
                UseSite(
                    "Lev.1.1",
                    HeTriple("מֵאֹהֶל מוֹעֵד", "me-ohel mo'ed", "from the Tent of Meeting"),
                    path="RRL",
                    note_en="speech FROM Tent",
                ),
                UseSite(
                    "Num.9.17",
                    HeTriple("הָאֹהֶל", "ha-ohel", "the tent (alias)"),
                    note_en="cloud lifts from the tent",
                ),
            ],
            result=ResolveResult.PASS,  # primary; Num is alias
            confidence="tested",
        ),
        Symbol(
            handle="SYM_petach_ohel",
            name=HeTriple("פֶּתַח אֹהֶל מוֹעֵד", "petach ohel mo'ed", "entrance of the Tent of Meeting"),
            writes=[
                WriteSite("Exod.29.4", "DECLARE_PLACE", "bring Aaron/sons to entrance"),
                WriteSite("Exod.29.42", "BIND_FUNCTION", "meet/speak at entrance"),
                WriteSite("Exod.40.6", "PLACE", "olah altar before entrance"),
            ],
            uses=[
                UseSite(
                    "Lev.1.3",
                    HeTriple("פֶּתַח אֹהֶל מוֹעֵד", "petach ohel mo'ed", "entrance of the Tent"),
                    path="RLL",
                    note_en="bring cattle olah here",
                ),
                UseSite(
                    "Lev.1.5",
                    HeTriple("פֶּתַח אֹהֶל מוֹעֵד", "petach ohel mo'ed", "entrance of the Tent"),
                    path="RRR",
                    note_en="altar blood site at entrance",
                ),
            ],
            result=ResolveResult.PASS,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_mizbeach",
            name=HeTriple("מִזְבֵּחַ", "mizbeach", "altar"),
            writes=[
                WriteSite("Exod.27.1", "DESIGN", "make the altar"),
                WriteSite("Exod.40.6", "PLACE", "mizbach ha-olah before entrance"),
            ],
            uses=[
                UseSite("Lev.1.5", HeTriple("הַמִּזְבֵּחַ", "ha-mizbeach", "the altar"), path="RRLLC4"),
                UseSite("Lev.1.7", HeTriple("הַמִּזְבֵּחַ", "ha-mizbeach", "the altar"), path="LRR"),
                UseSite("Lev.1.8", HeTriple("הַמִּזְבֵּחַ", "ha-mizbeach", "the altar"), path="RRRR"),
                UseSite(
                    "Lev.1.9",
                    HeTriple("הַמִּזְבֵּחָה", "ha-mizbechah", "onto the altar"),
                    path="RLR",
                ),
            ],
            result=ResolveResult.PASS,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_benei_aharon",
            name=HeTriple("בְּנֵי אַהֲרֹן", "benei Aharon", "sons of Aaron"),
            writes=[WriteSite("Exod.28.1", "APPOINT", "named sons to priest for Me")],
            uses=[
                UseSite(
                    "Lev.1.5",
                    HeTriple("בְּנֵי אַהֲרֹן הַכֹּהֲנִים", "benei Aharon ha-kohanim", "sons of Aaron the priests"),
                    path="RLLRC",
                ),
                UseSite("Lev.1.7", HeTriple("בְּנֵי אַהֲרֹן", "benei Aharon", "sons of Aaron"), path="LLLRC"),
                UseSite(
                    "Lev.1.8",
                    HeTriple("בְּנֵי אַהֲרֹן הַכֹּהֲנִים", "benei Aharon ha-kohanim", "sons of Aaron the priests"),
                    path="LLR",
                ),
            ],
            result=ResolveResult.PASS,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_kohen",
            name=HeTriple("כֹּהֵן", "kohen", "priest"),
            writes=[WriteSite("Exod.28.1", "APPOINT", "le-khahano li — to priest for Me")],
            uses=[
                UseSite("Lev.1.5", HeTriple("הַכֹּהֲנִים", "ha-kohanim", "the priests"), path="RLLRC2"),
                UseSite("Lev.1.7", HeTriple("הַכֹּהֵן", "ha-kohen", "the priest"), path="LLLRC2"),
                UseSite("Lev.1.9", HeTriple("הַכֹּהֵן", "ha-kohen", "the priest"), path="RLLC1"),
            ],
            result=ResolveResult.PASS,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_anan",
            name=HeTriple("עָנָן", "anan", "cloud"),
            writes=[WriteSite("Exod.40.34", "ACTIVATE", "cloud covers Tent at go-live")],
            uses=[
                UseSite(
                    "Num.9.17",
                    HeTriple("הֶעָנָן", "he-anan", "the cloud"),
                    note_en="lift → journey; dwell → camp",
                ),
                UseSite(
                    "Num.10.11",
                    HeTriple("הֶעָנָן", "he-anan", "the cloud"),
                    path="RLR",
                    note_en="instance lift at Sinai",
                ),
            ],
            result=ResolveResult.PASS,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_kavod",
            name=HeTriple("כָּבוֹד", "kavod", "glory (of YHWH)"),
            writes=[WriteSite("Exod.40.34", "ACTIVATE", "glory fills mishkan")],
            uses=[],
            result=ResolveResult.INSTALL_ONLY,
            confidence="tested",
        ),
        Symbol(
            handle="SYM_makom_yivchar",
            name=HeTriple(
                "הַמָּקוֹם אֲשֶׁר־יִבְחַר",
                "ha-makom asher-yivchar",
                "the place that He will choose",
            ),
            writes=[],  # not an Exodus string write
            uses=[
                UseSite("Deut.12.5", HeTriple("הַמָּקוֹם אֲשֶׁר יִבְחַר", "ha-makom asher yivchar", "the place He will choose"), path="LL"),
                UseSite("Deut.12.11", HeTriple("הַמָּקוֹם אֲשֶׁר יִבְחַר", "ha-makom asher yivchar", "the place He will choose"), path="LL"),
                UseSite("Deut.12.14", HeTriple("בַּמָּקוֹם אֲשֶׁר יִבְחַר", "ba-makom asher yivchar", "in the place He will choose"), path="LL"),
            ],
            result=ResolveResult.PASS_RECOMPILE,
            confidence="hypothesis",
        ),
    ]


# ---------------------------------------------------------------------------
# Cattle olah procedure (Lev 1:1–9) — teaching steps only
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class OlahStep:
    order: int
    ref: str
    op: str
    agent: str  # speech | bringer | priests | system
    he_summary: HeTriple
    tree_note_en: str
    env_reads: tuple[str, ...] = ()


OLAH_CATTLE_STEPS: list[OlahStep] = [
    OlahStep(
        0,
        "Lev.1.1",
        "OPEN_ORACLE",
        "system",
        HeTriple("מֵאֹהֶל מוֹעֵד", "me-ohel mo'ed", "from the Tent of Meeting"),
        "Top R: speech from Tent (not call-to-Moses half)",
        ("SYM_ohel_moed",),
    ),
    OlahStep(
        1,
        "Lev.1.2",
        "OPEN_MENU",
        "system",
        HeTriple("קָרְבָּן", "korban", "offering (local type word)"),
        "Top L: person brings korban to YHWH; Top R: from cattle/flock",
        (),
    ),
    OlahStep(
        2,
        "Lev.1.3",
        "CASE_OPEN",
        "bringer",
        HeTriple("אִם עֹלָה … מִן הַבָּקָר", "im olah … min ha-bakar", "if burnt offering from cattle"),
        "Top L: IF + guards (male, unblemished)",
        (),
    ),
    OlahStep(
        3,
        "Lev.1.3",
        "BRING_TO_PLACE",
        "bringer",
        HeTriple("פֶּתַח אֹהֶל מוֹעֵד", "petach ohel mo'ed", "entrance of the Tent"),
        "Top R: bring to entrance before YHWH",
        ("SYM_petach_ohel",),
    ),
    OlahStep(
        4,
        "Lev.1.4",
        "LEAN_HAND",
        "bringer",
        HeTriple("וְסָמַךְ יָדוֹ עַל רֹאשׁ הָעֹלָה", "ve-samakh yado al rosh ha-olah", "lean hand on head of olah"),
        "Top L: lean on olah; Top R: acceptance / kipper aim",
        ("SYM_olah",),
    ),
    OlahStep(
        5,
        "Lev.1.5",
        "SLAUGHTER",
        "bringer",
        HeTriple("וְשָׁחַט … לִפְנֵי יְהוָה", "ve-shahat … lifnei YHWH", "slaughter before YHWH"),
        "Top L only — agent split",
        (),
    ),
    OlahStep(
        6,
        "Lev.1.5",
        "DASH_BLOOD",
        "priests",
        HeTriple("וְזָרְקוּ … עַל הַמִּזְבֵּחַ", "ve-zarku … al ha-mizbeach", "dash blood on the altar"),
        "Top R: priests + blood + altar + petach",
        ("SYM_benei_aharon", "SYM_kohen", "SYM_mizbeach", "SYM_petach_ohel"),
    ),
    OlahStep(
        7,
        "Lev.1.6",
        "FLAY_AND_CUT",
        "bringer",
        HeTriple("וְהִפְשִׁיט … וְנִתַּח", "ve-hifshit … ve-nittah", "flay and cut in pieces"),
        "Top L flay / Top R cut",
        (),
    ),
    OlahStep(
        8,
        "Lev.1.7",
        "FIRE_AND_WOOD",
        "priests",
        HeTriple("אֵשׁ עַל הַמִּזְבֵּחַ", "esh al ha-mizbeach", "fire on the altar"),
        "Top L fire on altar / Top R wood on fire",
        ("SYM_mizbeach", "SYM_benei_aharon"),
    ),
    OlahStep(
        9,
        "Lev.1.8",
        "ARRANGE_PARTS",
        "priests",
        HeTriple("עָרְכוּ … עַל הָעֵצִים", "arkhu … al ha-etsim", "arrange pieces on the wood"),
        "Top L pieces; Top R on wood/fire/altar",
        ("SYM_mizbeach", "SYM_kohen"),
    ),
    OlahStep(
        10,
        "Lev.1.9",
        "WASH_AND_SMOKE",
        "bringer+priests",
        HeTriple("יִרְחַץ … וְהִקְטִיר", "yirhats … ve-hiqtir", "wash; priest turns to smoke"),
        "Top L wash / Top R priest smoke + formula",
        ("SYM_kohen", "SYM_mizbeach"),
    ),
]


# ---------------------------------------------------------------------------
# Cloud FSM
# ---------------------------------------------------------------------------


class CloudState(str, Enum):
    CAMPED = "CAMPED"
    LIFTING = "LIFTING"
    MARCHING = "MARCHING"
    SETTLED = "SETTLED"  # intermediate before CAMPED at new place


@dataclass
class CloudEvent:
    kind: str  # cover | lift | dwell | prolonged
    ref: str
    place: Optional[str] = None
    note_en: str = ""


@dataclass
class CloudFSM:
    """Educational FSM only — states from Num 9; not a full wilderness engine."""

    state: CloudState = CloudState.CAMPED
    place: str = "mishkan_site"
    log: list[str] = field(default_factory=list)

    def apply(self, event: CloudEvent) -> None:
        if event.kind == "cover":
            self.state = CloudState.CAMPED
            self.log.append(f"{event.ref}: cover → {self.state.value} ({event.note_en})")
        elif event.kind == "lift":
            self.state = CloudState.LIFTING
            self.log.append(f"{event.ref}: lift → {self.state.value} ({event.note_en})")
            self.state = CloudState.MARCHING
            self.log.append(f"{event.ref}: after lift → {self.state.value}")
        elif event.kind == "dwell":
            if event.place:
                self.place = event.place
            self.state = CloudState.SETTLED
            self.log.append(f"{event.ref}: dwell at {self.place} → {self.state.value}")
            self.state = CloudState.CAMPED
            self.log.append(f"{event.ref}: camped at {self.place}")
        elif event.kind == "prolonged":
            self.state = CloudState.CAMPED
            self.log.append(
                f"{event.ref}: prolonged dwell → stay {self.state.value} (no march) ({event.note_en})"
            )
        else:
            self.log.append(f"{event.ref}: unknown event {event.kind} (ignored)")


def num9_rule_events() -> list[CloudEvent]:
    return [
        CloudEvent("cover", "Num.9.15", note_en="cloud covers mishkan on day of erecting"),
        CloudEvent("lift", "Num.9.17", note_en="when cloud lifts from tent → journey"),
        CloudEvent("dwell", "Num.9.17", place="where_cloud_settles", note_en="where cloud dwells → camp"),
        CloudEvent("prolonged", "Num.9.19", note_en="many days on mishkan → do not journey"),
        CloudEvent("lift", "Num.9.22", note_en="when taken up → journey (any duration)"),
    ]


def num10_instance_events() -> list[CloudEvent]:
    return [
        CloudEvent("lift", "Num.10.11", note_en="cloud lifted from mishkan ha-edut (dated)"),
        CloudEvent("dwell", "Num.10.12", place="wilderness_of_Paran", note_en="march from Sinai; cloud in Paran"),
    ]


# ---------------------------------------------------------------------------
# Resolve dry-run
# ---------------------------------------------------------------------------


def resolve_report(symbols: list[Symbol]) -> list[dict[str, Any]]:
    rows = []
    for s in symbols:
        ok = True
        reason = ""
        if s.result == ResolveResult.PASS:
            ok = bool(s.writes) and bool(s.uses)
            reason = "has WRITE and USE" if ok else "PASS requires both WRITE and USE"
        elif s.result == ResolveResult.PASS_ALIAS:
            ok = bool(s.writes) and bool(s.uses)
            reason = "alias USE of installed name"
        elif s.result == ResolveResult.PASS_RECOMPILE:
            ok = not s.writes and bool(s.uses)
            reason = "USE only; role recompile (no Exod string WRITE)"
        elif s.result == ResolveResult.INSTALL_ONLY:
            ok = bool(s.writes) and not s.uses
            reason = "WRITE only in V1 slice"
        elif s.result == ResolveResult.LOCAL:
            ok = bool(s.uses)
            reason = "local declare at use"
        else:
            ok = False
            reason = "OPEN"
        rows.append(
            {
                "handle": s.handle,
                "name": s.name.show(),
                "result": s.result.value,
                "writes": [w.ref for w in s.writes],
                "uses": [u.ref for u in s.uses],
                "ok": ok,
                "reason": reason,
                "confidence": s.confidence,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# Optional live trees
# ---------------------------------------------------------------------------


def try_parse_tree(osis: str) -> Optional[str]:
    sys.path.insert(0, str(ROOT))
    try:
        from taamim_tree_parse import parse_verse, tree_ascii_string  # type: ignore
    except Exception as e:
        return f"(parser unavailable: {e})"
    try:
        pr = parse_verse(osis)
        head = tree_ascii_string(pr["tree"])
        lines = head.splitlines()
        preview = "\n".join(lines[:12])
        more = f"\n  … ({len(lines)} lines total)" if len(lines) > 12 else ""
        return f"status={pr.get('status')} rule={pr.get('rule_set_version')}\n{preview}{more}"
    except Exception as e:
        return f"(parse failed for {osis}: {e})"


# ---------------------------------------------------------------------------
# CLI presentation
# ---------------------------------------------------------------------------


def hr(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def print_banner() -> None:
    print("Sanctuary spine V1 — educational dry-run")
    print("Not binding religious law. Hebrew is source; English is [EN-AID].")
    print(f"Demo docs: {DEMO_DIR.relative_to(ROOT)}")
    print(f"Repo root: {ROOT}")


def print_resolve(symbols: list[Symbol]) -> None:
    hr("1) FREE-NAME RESOLVE DRY-RUN")
    rows = resolve_report(symbols)
    passed = sum(1 for r in rows if r["ok"])
    for r in rows:
        flag = "OK " if r["ok"] else "!! "
        print(f"{flag} {r['handle']:22} {r['result']:16} conf={r['confidence']}")
        print(f"     {r['name']}")
        print(f"     WRITE {r['writes'] or '—'}  USE {r['uses'] or '—'}")
        print(f"     {r['reason']}")
    print()
    print(f"Summary: {passed}/{len(rows)} rows consistent with declared result enum")
    print("Note: PASS_recompile has no Exod WRITE by design (Deut place key).")


def print_olah() -> None:
    hr("2) CATTLE OLAH PROCEDURE (Lev 1:1–9)")
    print("Environment required: ohel_moed, petach_ohel, mizbeach, kohanim (Exod install)")
    print()
    for step in OLAH_CATTLE_STEPS:
        env = f"  reads {list(step.env_reads)}" if step.env_reads else ""
        print(f"[{step.order:02d}] {step.ref:8}  {step.op:16}  agent={step.agent}{env}")
        print(f"     {step.he_summary.show()}")
        print(f"     tree: {step.tree_note_en}")


def print_cloud() -> None:
    hr("3) CLOUD STAY/GO FSM")
    print("WRITE: Exod.40.34–35 cloud ONLINE on sanctuary")
    print("Rules: Num.9.15–23  ·  Instance: Num.10.11–13")
    print()
    fsm = CloudFSM()
    print("--- apply Num 9 rule events ---")
    for e in num9_rule_events():
        fsm.apply(e)
    for line in fsm.log:
        print(" ", line)
    print(f"  state={fsm.state.value} place={fsm.place}")

    print()
    print("--- apply Num 10 Sinai depart instance ---")
    fsm2 = CloudFSM(state=CloudState.CAMPED, place="Sinai")
    for e in num10_instance_events():
        fsm2.apply(e)
    for line in fsm2.log:
        print(" ", line)
    print(f"  state={fsm2.state.value} place={fsm2.place}")


def print_interlock() -> None:
    hr("4) INTERLOCK ONE-LINER")
    print(
        """
  Exodus INSTALLS  tent/altar/priests/cloud
       → Leviticus OPERATES cattle olah using those free names
       → Numbers   MOVES when cloud lifts / camps when it dwells
       → Deuteronomy RECOMPILES place language for the land
         (makom yivchar ≠ ohel mo'ed string; role link is hypothesis)
""".strip(
            "\n"
        )
    )


def print_trees() -> None:
    hr("5) LIVE TA'AMIM TREES (optional)")
    for osis in ("Exod.40.34", "Lev.1.5", "Num.9.17", "Deut.12.5"):
        print(f"\n--- {osis} ---")
        print(try_parse_tree(osis))


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Sanctuary spine V1 educational dry-run")
    ap.add_argument("--resolve-only", action="store_true", help="Only free-name resolve table")
    ap.add_argument("--olah-only", action="store_true", help="Only cattle olah steps")
    ap.add_argument("--cloud-only", action="store_true", help="Only cloud FSM")
    ap.add_argument("--trees", action="store_true", help="Also parse key verses with taamim_tree_parse")
    args = ap.parse_args(argv)

    print_banner()
    symbols = build_symbol_table()

    only = args.resolve_only or args.olah_only or args.cloud_only
    if args.resolve_only or not only:
        print_resolve(symbols)
    if args.olah_only or not only:
        print_olah()
    if args.cloud_only or not only:
        print_cloud()
    if not only:
        print_interlock()
    if args.trees:
        print_trees()

    hr("DONE")
    print("Docs: README.md · TUTORIAL_* · DEMO_*_HUB_*.md in this folder")
    print("This code is a teaching dump of the demo tables — re-derive from Hebrew for real work.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
