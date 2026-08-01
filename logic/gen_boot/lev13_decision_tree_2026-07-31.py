#!/usr/bin/env python3
"""lev13_decision_tree_2026-07-31.py — Leviticus 13:1-8 as branching code.

LEARNING EXERCISE (owner request: "I don't see if statements in the python").
Here they are — and they are the TEXT'S OWN. The law genre writes its
branches as particles, DB-measured 2026-07-31 across Leviticus 13:

    ki  ("when")  x13  — opens a main case   (= the function head)
    im  ("if")    x15  — opens a sub-case    (= elif)
    ve-hineh ("and behold")  x20 — the inspection result marker
    ba-yom ha-shevi'i ("on THE seventh day") — the re-inspection date
    ve-hisgir ("he shall confine") x9 — the quarantine call

So the if-statements below are not imposed on the text; they are
TRANSLITERATED from it. Each branch cites its verse. Status: UNDERIVED —
this is a provisional rendering ahead of the Lev 13 derivation (the frozen
YAML unit, when the owner orders it, is where the logic will actually
live); the clause structure was read from our own DB dump of 13:1-8.
Every Hebrew term glossed inline — absolute rule.

Scope note (honest): this file renders the chapter's FIRST procedure
(13:1-8, the se'et/sapachat/baheret intake). Mixed predicate cases
(e.g. deep but hair not white) route to the chapter's later paragraphs
(13:9-46) — represented here as an explicit hand-off, not invented logic.

Run:  python3 logic/gen_boot/lev13_decision_tree_2026-07-31.py
"""


class Inspection:
    """What the priest observes when he looks — the verses' own predicates."""
    def __init__(self, hair_white=False, deeper_than_skin=False,
                 stood=False, faded=False, spread=False):
        self.hair_white = hair_white            # se'ar hafakh lavan ("hair turned white")
        self.deeper_than_skin = deeper_than_skin  # amok min ha-or ("deeper than the skin")
        self.stood = stood                      # amad be-einav ("stood in its appearance")
        self.faded = faded                      # kehah ("dim/faded")
        self.spread = spread                    # pasah ("spread")


class Case:
    """One person's mark, with what each successive inspection will find."""
    def __init__(self, name, inspections, spreads_after_release=False):
        self.name = name
        self._queue = list(inspections)
        self.spreads_after_release = spreads_after_release
        self.day = 0

    def inspect(self):
        return self._queue.pop(0)


def log(day, verse, msg):
    print("    day %2d  [%s]  %s" % (day, verse, msg))


def priest_procedure(case):
    """Lev 13:2-8 — the intake procedure, branch for branch."""
    print("\nCASE: %s" % case.name)

    # 13:2 — adam KI yihyeh ve-or besaro se'et o sapachat o baheret
    #        ("a human, WHEN there is in the skin of his flesh a swelling
    #        or a scab or a bright spot") — the KI case-opener: intake.
    #        ve-huva el ha-kohen — "he shall be BROUGHT to the priest".
    log(case.day, "13:2", "ki (when): mark on the skin of the flesh -> brought to the priest")

    # 13:3 — first inspection: ve-ra'ah ha-kohen ("the priest shall SEE")
    obs = case.inspect()
    if obs.hair_white and obs.deeper_than_skin:
        # 13:3 — "hair in the mark turned white, and its appearance deeper
        #         than the skin: nega tzara'at hu — ve-timme'o"
        log(case.day, "13:3", "hair WHITE and DEEPER than skin -> it IS tzara'at")
        log(case.day, "13:3", "STATUS WRITE: ve-timme'o ('he shall declare him IMPURE')")
        return "TAMEI"

    elif not obs.hair_white and not obs.deeper_than_skin:
        # 13:4 — ve-IM ("and IF") bright spot white, NOT deeper, hair NOT
        #         turned: ve-hisgir... shivat yamim — the quarantine call.
        log(case.day, "13:4", "im (if): white but NOT deeper, hair NOT turned"
                              " -> ve-hisgir: CONFINE seven days")
        case.day += 7

        # 13:5 — ba-yom ha-shevi'i ("on THE seventh day") re-inspection,
        #         result marked ve-hineh ("and behold") — day 7's definite
        #         label from the frozen week, running as the loop clock.
        obs = case.inspect()
        if obs.spread:
            # the chapter's spread rule (13:8 pattern): spread => impure
            log(case.day, "13:5/8", "ve-hineh: SPREAD during confinement -> TAMEI")
            return "TAMEI"
        if obs.stood:
            # 13:5 — "the mark STOOD in its appearance, did not spread:
            #         confine seven days SHENIT ('a second time')" — the
            #         loop's second (and per the letter, final) iteration.
            log(case.day, "13:5", "ve-hineh: mark STOOD, no spread"
                                  " -> confine seven days SHENIT (second time)")
            case.day += 7

            # 13:6 — second seventh-day inspection
            obs = case.inspect()
            if obs.faded and not obs.spread:
                # 13:6 — "ve-hineh the mark FADED and did not spread:
                #         ve-tiharo — mispachat hi; wash clothes; ve-taher"
                log(case.day, "13:6", "ve-hineh: FADED, no spread -> it is a mispachat (scab)")
                log(case.day, "13:6", "STATUS WRITE: ve-tiharo ('he shall declare him PURE')"
                                      " + wash garments")
                # 13:7 — ve-IM: the post-release trigger stays ARMED:
                #         "but IF the scab SPREADS after he was shown to
                #         the priest for his purification — appear AGAIN"
                if case.spreads_after_release:
                    log(case.day + 1, "13:7", "im (if): spread AFTER release -> reappear before the priest")
                    # 13:8 — ve-hineh spread -> ve-timme'o: tzara'at hi
                    log(case.day + 1, "13:8", "ve-hineh: spread confirmed -> STATUS WRITE:"
                                              " ve-timme'o — tzara'at hi")
                    return "TAHOR, then re-opened -> TAMEI"
                return "TAHOR"
            elif obs.spread:
                # 13:8 — spread at the second check => impure
                log(case.day, "13:8", "ve-hineh: SPREAD -> STATUS WRITE: ve-timme'o — tzara'at hi")
                return "TAMEI"
            else:
                log(case.day, "13:6ff", "neither faded nor spread — the chapter's later"
                                        " paragraphs take the case (outside 13:1-8)")
                return "HANDED OFF (13:9ff)"

    # mixed predicates (deep but hair not white, etc.): the chapter routes
    # these to its later case paragraphs — an explicit hand-off, not a gap
    # in the law: 13:9-46 continues the dispatch (se'et with michyah 'raw
    # flesh', the boil, the burn, the head/beard, the bald cases...).
    log(case.day, "13:9ff", "mixed predicates -> the chapter's next ki-paragraph takes over")
    return "HANDED OFF (13:9ff)"


def main():
    print("LEVITICUS 13:1-8 AS BRANCHING CODE — the text's own if-tree")
    print("(ki 'when' x13 / im 'if' x15 in the chapter, DB-measured;")
    print(" every branch below cites the verse it transliterates)")

    verdicts = []

    # Path 1 — the immediate verdict (13:3)
    verdicts.append(priest_procedure(Case(
        "A — white hair, deeper than skin at intake",
        [Inspection(hair_white=True, deeper_than_skin=True)])))

    # Path 2 — the full quarantine loop to a clean release (13:4 -> 5 -> 6)
    verdicts.append(priest_procedure(Case(
        "B — shallow and unturned; stands week one; fades week two",
        [Inspection(),                          # intake: not white, not deep
         Inspection(stood=True),                # day 7: stood, no spread
         Inspection(faded=True)])))             # day 14: faded

    # Path 3 — released, then the armed trigger fires (13:7-8)
    verdicts.append(priest_procedure(Case(
        "C — as B, but the scab spreads after purification",
        [Inspection(), Inspection(stood=True), Inspection(faded=True)],
        spreads_after_release=True)))

    # Path 4 — spread caught at the first re-inspection
    verdicts.append(priest_procedure(Case(
        "D — shallow at intake; spread found on day 7",
        [Inspection(), Inspection(spread=True)])))

    print("\nVERDICTS: %s" % " | ".join(verdicts))
    print("\nWhat the week supplied to this tree (frozen units): the inspector's")
    print("syntax (ra'ah + ve-hineh + verdict = 1:31's test instrument), the")
    print("clock (shivat yamim; re-checks on yom ha-shevi'i, THE seventh day),")
    print("and the status-write device (day 7's kadosh -> ve-timme'o/ve-tiharo).")
    print("What the gaps supplied: or (skin, Gen 3:21), basar (flesh, Gen 2:21),")
    print("nega (mark, Gen 12:17), hisgir (confine <- sagar, Gen 2:21/7:16),")
    print("tahor/tamei (Gen 7:2 / 34:5), the priest (Exod 28), the ki/im rule")
    print("genre itself (Gen 2:16-17). The branches are new; the machine is not.")


if __name__ == "__main__":
    main()
