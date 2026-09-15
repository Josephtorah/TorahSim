#!/usr/bin/env python3
"""RE-TEST: does the event stream carry movement?

RESUME.md recorded, before the 2026-08-30 compaction:
    "Zero movement verbs in the event stream; 3 of 557 events have a
     place-like theme."

That is a report of ZERO, and under THE_STEPS Step 4 a report of zero is worth
only the coverage line above it. This re-runs it by ENUMERATING every distinct
event-verb label and classifying all of them, so the negative (if it is one) is
auditable and the positive (if it is one) is counted.

PROBE: the classifier must fire on labels known to be present. If the probe
does not fire, the run refuses to report.
"""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sqlite3
from collections import Counter

WORLD = ((_ROOT + '/World') + "/world.sqlite")

# Classified by hand from the FULL enumeration below — the enumeration is
# measured, the classification is a judgement, same contract as VERB_REVIEW.md.
MOVE = {
    # self-locomotion
    "come", "go", "go_out", "go_up", "return", "descend", "journey", "flee",
    "pursue", "pass", "arrive", "enter", "depart", "walk", "run", "cross",
    "come_out", "go_down", "went", "travel", "wander", "approach", "met",
    # caused motion — something or someone is moved
    "take", "bring", "send", "send_away", "bring_out", "cast_out", "drive",
    "carry", "lead", "put", "place", "station", "set", "cast_sleep", "expel",
    # position / tenure — being somewhere
    "dwell", "settle", "tent", "sojourn", "encamp", "stand", "sit", "lie",
    "bury", "remain", "stay",
}
PROBE = {"come", "go_out", "dwell", "return"}   # seen in the enumeration


def main():
    c = sqlite3.connect(WORLD)
    labels = Counter(v for (v,) in c.execute("select verb from events"))
    total = sum(labels.values())
    print(f"SCANNED: {total} events, {len(labels)} distinct verb labels, "
          f"from world.sqlite (97 units, all of Genesis)")

    # ---- probe
    hit = {p for p in PROBE if p in labels}
    print(f"PROBE  : {len(hit)} of {len(PROBE)} probe labels present in the data "
          f"-> {sorted(hit)}")
    if not hit:
        raise SystemExit("PROBE DID NOT FIRE — refusing to report.")

    moving = {v: n for v, n in labels.items() if v in MOVE}
    nmov = sum(moving.values())
    unknown = labels.get("?", 0)
    print(f"\nRESULT")
    print(f"  events whose verb is a MOVEMENT verb : {nmov} of {total} "
          f"({100 * nmov / total:.0f}%)")
    print(f"  distinct movement labels             : {len(moving)} of {len(labels)}")
    print(f"  events with an unresolved verb ('?')  : {unknown}")
    print(f"\n  THE RECORDED CLAIM WAS 'ZERO MOVEMENT VERBS'. "
          f"{'REFUTED.' if nmov else 'confirmed.'}")

    print(f"\nEVERY MOVEMENT LABEL, counted")
    for v, n in sorted(moving.items(), key=lambda x: -x[1]):
        print(f"  {n:>3}  {v}")

    print(f"\nNOT CLASSIFIED AS MOVEMENT — the full remainder, so the "
          f"negative is auditable")
    rest = sorted(((n, v) for v, n in labels.items() if v not in MOVE),
                  reverse=True)
    print("  " + " · ".join(f"{v}({n})" for n, v in rest))

    # ---- the second half of the claim: place-like themes
    print(f"\nTHE OTHER HALF OF THE CLAIM — '3 of 557 events have a "
          f"place-like theme'")
    themes = Counter(t for (t,) in c.execute("select theme from event_themes"))
    print(f"  {sum(themes.values())} theme rows on "
          f"{len(set(s for (s,) in c.execute('select seq from event_themes')))}"
          f" distinct events; {len(themes)} distinct themes")
    gaz_like = [t for t in themes if any(
        k in t for k in ("eretz", "aretz", "maqom", "har_", "ir_", "beer",
                         "mitzrayim", "kenaan", "sedom", "charan", "bet_el",
                         "gilad", "shekhem", "goshen", "machanayim", "peniel"))]
    print(f"  themes whose NAME looks place-like: {len(gaz_like)} distinct "
          f"-> {sorted(gaz_like)[:16]}")
    n = sum(themes[t] for t in gaz_like)
    print(f"  theme rows on those: {n}")


main()
