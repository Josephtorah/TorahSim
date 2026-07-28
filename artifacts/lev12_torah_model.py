#!/usr/bin/env python3
"""
lev12_torah_model.py

Justified layered representation:
  Ta'amim tree → Torah declaration → Mishnah operationalization → Talmud derivation

Representation only — not autonomous law generation.
Every step traceable to Written Torah, ta'amim structure, or a named Oral source.

Provenance: web Grok recovery batch + local fix so female path matches Lev 12:5
and torah_test_scenarios.json.

Run:
  python3 artifacts/lev12_torah_model.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Step 1: Ta'amim tree structure
# Strong disjunctive pivot near "zachar" / parallel female block (Lev 12:5)
# ---------------------------------------------------------------------------
def make_tree(child_gender: str) -> dict[str, Any]:
    gender = child_gender if child_gender in ("male", "female") else "male"
    # Lev 12:2 male = 7 days; Lev 12:5 female = 14 days
    impurity_days = 7 if gender == "male" else 14
    return {
        "condition": {
            "birth_event": True,
            "child_gender": gender,  # pivot from ta'amim-delimited gender phrase
        },
        "consequence": {
            "impurity_days": impurity_days,  # consequence subtree
            "reference": "niddah",
        },
        "implication": "impure",
    }


# Default tree as in web recovery (male)
taamim_tree = make_tree("male")


def torah_rule(tree: dict[str, Any]) -> dict[str, Any] | None:
    """Lev 12:2 / 12:5 — base declaration from condition + consequence phrases."""
    cond = tree.get("condition") or {}
    if not cond.get("birth_event"):
        return None
    gender = cond.get("child_gender")
    if gender not in ("male", "female"):
        return None
    cons = tree["consequence"]
    # Purification durations from Lev 12:4–5 (chapter context)
    purification_days = 33 if gender == "male" else 66
    return {
        "child_gender": gender,
        "impurity_days": cons["impurity_days"],
        "purification_days": purification_days,
        "status": tree["implication"],
        "reference": cons["reference"],
        "source": "Leviticus 12:2-5",
    }


def mishnah_apply(torah_output: dict[str, Any] | None) -> dict[str, Any] | None:
    """Mishnah Niddah-style operational rules (practical counting, status)."""
    if not torah_output:
        return None
    return {
        **torah_output,
        "counting_method": "daily examination from day 1",
        "restrictions": "no holy things or sanctuary",
        "final_status": "pure after purification period + offering (Lev 12:6-8)",
        "mishnah_layer": "Niddah operationalization (counting / status)",
    }


def talmud_derive(
    mishnah_output: dict[str, Any] | None, child_gender: str
) -> dict[str, Any] | None:
    """Talmud Niddah 31a deeper reason (representation of named sugya)."""
    if not mishnah_output:
        return None
    if child_gender == "female":
        reason = (
            "Doubled period due to slower remorse from oath made in labor pain "
            "(Niddah 31a)"
        )
        remorse_days = 14
    else:
        reason = "Quicker remorse for male birth (Niddah 31a)"
        remorse_days = 7
    return {
        **mishnah_output,
        "talmud_reason": reason,
        "remorse_days": remorse_days,
        "talmud_source": "Niddah 31a",
    }


def run_scenario(gender: str = "male") -> dict[str, Any] | None:
    """Simple scenario runner (web recovery + female path fix)."""
    tree = make_tree(gender)
    return talmud_derive(mishnah_apply(torah_rule(tree)), gender)


def load_scenarios() -> list[dict[str, Any]]:
    path = Path(__file__).with_name("torah_test_scenarios.json")
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("scenarios") or [])


def main() -> None:
    print("=== run_scenario('female') ===")
    print(json.dumps(run_scenario("female"), indent=2, ensure_ascii=False))

    print("\n=== run_scenario('male') ===")
    print(json.dumps(run_scenario("male"), indent=2, ensure_ascii=False))

    scenarios = load_scenarios()
    if not scenarios:
        return

    print("\n=== Scenarios from torah_test_scenarios.json ===")
    for s in scenarios:
        inp = s.get("input") or {}
        if not inp.get("birth_event"):
            print(f"- {s.get('id')}: skipped (no birth_event)")
            continue
        gender = inp.get("child_gender", "male")
        out = run_scenario(gender)
        expected = s.get("expected") or {}
        exp_days = expected.get("impurity_days")
        got_days = out.get("impurity_days") if out else None
        ok = exp_days is None or got_days == exp_days
        print(
            f"- {s.get('id')}: impurity_days={got_days} "
            f"(expected {exp_days}) {'OK' if ok else 'CHECK'}"
        )
        if "economic_status" in inp:
            print(
                f"    note: poor offering is Lev 12:8 ritual branch "
                f"(not impurity duration); expected offering_type="
                f"{expected.get('offering_type')}"
            )


if __name__ == "__main__":
    main()
