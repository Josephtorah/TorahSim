#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# LAW ERA v2 — CHAPTER ASSEMBLY (pre-freeze DRAFT)
# exo_21_v2: Exodus 21:1-37 — the full span of frozen unit
# exo_21_the_ordinances, assembled from the three block machines:
#
#   block 1 (21:1-11)  block1.py — slave-term laws
#   block 2 (21:12-27) block2.py — homicide & injury
#   block 3 (21:28-37) block3.py — goring ox, pit, tariff
#
# Assembled 2026-08-12. Scan side: chapter ledger 4,903 rows = census EXACT,
# EXOD 21 CHAPTER GATE GREEN. Witness layer: the three claims manifests
# (law01: 39, law02: 43, law03: 35 = 117 claims) in scans/manifests/.
#
# WHAT ASSEMBLY ADDS (nothing in the blocks is changed — they are imported):
#   1. World — the statute-0 runtime (21:1's ordained forum) as a persistent
#      state object: slave clocks, ox registries, standing verdicts. The
#      tanakh-run pass-2 REPLAY folds events over ONE World instance.
#   2. The SEAMS — laws that exist only ACROSS blocks, asserted here.
#   3. The CHAPTER dependency proof — the three DEPENDS tables merged;
#      edges pointing INSIDE 21:1-37 reclassified INTERNAL (self-supplied).
#
# STATUS: DRAFT. Freeze on owner word under the forward-era mechanical
# gates. Experimental model — not binding religious law.
# =============================================================================
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))

def _load(modname):
    spec = importlib.util.spec_from_file_location(
        modname, os.path.join(_HERE, modname + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

b1 = _load("block1")
b2 = _load("block2")
b3 = _load("block3")

SPAN = ("Exodus", 21, 1, 21, 37)     # the chapter machine's own territory

# ---------------------------------------------------------------------------
# THE WORLD — statute-0 as a runtime object                       [b1 L1-*]
# ואלה המשפטים אשר תשים לפניהם ("and these are the ordinances which you
# shall set before them"): the ordained forum carrying persistent state.
# Verdicts are per-scene; FACTS ARE SEQUENTIAL — the state layer the
# tanakh-run replay executor folds events over.
# ---------------------------------------------------------------------------
class World:
    def __init__(self):
        self.runtime = dict(b1.RUNTIME)   # the forum flags travel chapter-wide
        self.day = 0
        self.slaves = {}                  # sid -> block-1 slave record
        self.oxen = {}                    # oid -> block-3 ox record
        self.standing_verdicts = []       # state-writes at גמר דין (verdict)
        self._n = 0

    def _id(self, prefix):
        self._n += 1
        return "%s%d" % (prefix, self._n)

    def advance(self, days):
        self.day += days
        return self.day

    # -- block-1 events: the slave clock runs on WORLD time ---------------
    def enslave_by_court(self, theft, worth_six_years_labor, **kw):
        rec, why = b1.court_sale(theft, worth_six_years_labor, **kw)
        if rec is None:
            return None, why
        rec["term_start_day"] = self.day
        sid = self._id("slave")
        self.slaves[sid] = rec
        return sid, why

    def slave_status(self, sid):
        rec = self.slaves[sid]
        return b1.term_status(rec, self.day - rec["term_start_day"])

    # -- block-3 events: the ox state machine runs on WORLD time ----------
    def register_ox(self, owner):
        oid = self._id("ox")
        self.oxen[oid] = b3.new_ox(owner)
        return oid

    def goring(self, oid, species="ox", context="weekday",
               owner_present_testimony=False):
        b3.record_goring(self.oxen[oid], self.day, species, context,
                         owner_present_testimony)

    def petting_day(self, oid):
        b3.record_clean_petting_day(self.oxen[oid])

    def ox_status(self, oid, **kw):
        return b3.status(self.oxen[oid], **kw)

    # -- verdicts are STATE-WRITES: the benefit-ban rides the standing
    #    verdict, not the stones (Keritot 6:2) [b3 L28-05] ----------------
    def condemn(self, oid):
        self.oxen[oid]["condemned"] = True
        self.standing_verdicts.append(("stoning", oid, self.day))

    def dissolve_verdict(self, oid):
        self.oxen[oid]["condemned"] = False

    def execute(self, oid):
        self.oxen[oid]["executed"] = True
        self.dissolve_verdict(oid)      # the verdict is spent by execution

    def ox_benefit(self, oid):
        ox = self.oxen[oid]
        return b3.benefit_status(ox.get("condemned", False),
                                 ox.get("executed", False))

    def snapshot(self):
        """The replay scrubber's read-model (pass-2 web app)."""
        return {"day": self.day,
                "slaves": {s: self.slave_status(s) for s in self.slaves},
                "oxen": {o: self.ox_status(o) for o in self.oxen},
                "standing_verdicts": list(self.standing_verdicts)}

# ---------------------------------------------------------------------------
# THE SEAMS — chapter-level law that exists only ACROSS the blocks
# ---------------------------------------------------------------------------
def seam_man_vs_ox():
    """Mishnah BK 8:2: 'this is stricter in MAN than in OX' — the human
    injurer pays five heads + fetus-value; the ox pays nezek (damage) only
    and is clear of fetus-value (ובעל השור נקי 'and the ox's owner is
    clear'). [b2 L19-01 x b3 L28-06]"""
    man = b2.five_heads_award(shamed=True, intended_shame=True)
    return {"man_heads": len(man), "ox_heads": 1,
            "fetus_payer": {"man": "the conception-husband [b2 L22-02]",
                            "ox": "EXEMPT — naki [b3 L28-06]"}}

def seam_forewarned_templates():
    """The mu'ad-template isomorphism [b3 L0-01]: MAN is born forewarned —
    אדם מועד לעולם ('man is forever forewarned'), nezek even for the shogeg
    — while the OX must ACQUIRE the state (3 gorings / 3 days / owner
    present)."""
    man_shogeg = b2.five_heads_award(mens_rea="shogeg")
    fresh_ox = b3.new_ox()
    return {"man": "nezek" in man_shogeg and list(man_shogeg) == ["nezek"],
            "ox_starts": b3.status(fresh_ox)}

def seam_slave_victim():
    """One victim, two tracks: the MASTER who kills his slave meets the
    sword (block 2's window aside); the OX that kills a slave costs its
    owner the flat 30 (kapparah money). [b2 L20-* x b3 L32-01]"""
    master = b2.slave_homicide(survived_hours=10)          # within the window
    ox = b3.owner_liability("muad", "slave")
    return {"master": master["verdict"], "ox_owner_pays": ox["slave_fine"]}

def seam_manumission_actor():
    """Mishnah BK 3:10's chiasmus, leg 1: the MASTER's own blow frees the
    slave's eye; his OX's blow frees no one — the exit needs a human act
    with intent at the organ (an ox has neither). [b2 L26-01]"""
    by_master = b2.manumission()
    by_ox = b2.manumission(act_on_organ=True, intent_at_organ=False)
    return {"master_frees": by_master["free"], "ox_frees": by_ox["free"]}

def seam_parent_victim():
    """BK 3:10, leg 2: the ox that WOUNDS a parent pays (money track);
    the son himself is capital — and his payment is ABSORBED (kim leih).
    [b2 L15-01, L12-05]"""
    son = b2.parent_strike()
    absorbed = b2.kim_leih(death_class=True)
    return {"son": son["verdict"], "son_payment": absorbed["payment"],
            "ox": "pays nezek — no capital track for beast-wounding"}

def seam_tachat_anchor():
    """Rav Ashi's תחת↔תחת ('in place of' ↔ 'in place of') gezerah shavah:
    block 2's eye-for-eye money-reading draws on שור תחת השור ('ox in
    place of ox', 21:36) — a BLOCK-3 verse. Inside the assembled chapter
    the proof-anchor is SELF-SUPPLIED. [b2 L24-01 x b3 L36-01]"""
    eye = b2.tachat_payment("eye")
    anchor = ("Exodus", 21, 36)
    inside = (anchor[0] == SPAN[0] and (SPAN[1], SPAN[2]) <=
              (anchor[1], anchor[2]) <= (SPAN[3], SPAN[4]))
    return {"eye_mode": eye["mode"], "anchor_internal": inside}

def seam_statute0_parity():
    """Statute-0's gender-parity flag [b1 L1-06] instantiated in all three
    blocks: the woman striker is liable (block 2), the woman thief pays
    the tariff (block 3), the runtime carries the flag (block 1)."""
    return {"runtime_flag": b1.RUNTIME["gender_parity_all_monetary_law"],
            "woman_striker": b2.homicide_verdict("mezid",
                                                 striker="woman")["track"],
            "woman_thief": b3.theft_tariff("ox")["woman_thief_liable"]}

# ---------------------------------------------------------------------------
# THE CHAPTER DEPENDENCY PROOF — three tables merged, seams internalized
# ---------------------------------------------------------------------------
def _inside_span(book, ch, vs):
    return (book == SPAN[0] and
            (SPAN[1], SPAN[2]) <= (ch, vs) <= (SPAN[3], SPAN[4]))

def chapter_dependency_proof(verbose=True):
    spans = b3._frozen_spans()          # same resolver all blocks use
    def resolve(book, ch, vs):
        for b, c1, v1, c2, v2, uid in spans:
            if b == book and (c1, v1) <= (ch, vs) <= (c2, v2):
                return uid
        return None
    internal, resolved, forward = [], [], []
    seen_rows = set()
    for blkname, blk in (("b1", b1), ("b2", b2), ("b3", b3)):
        for elem, book, ch, vs, expect, claim, what in blk.DEPENDS:
            key = (blkname, elem, book, ch, vs)
            if key in seen_rows:
                continue
            seen_rows.add(key)
            row = (blkname, elem, "%s %d:%d" % (book, ch, vs), claim)
            if _inside_span(book, ch, vs):
                internal.append(row)    # the seam is now self-supplied
                continue
            uid = resolve(book, ch, vs)
            if uid:
                resolved.append(row + (uid,))
            else:
                forward.append(row)
            # every external edge must still match its block's declaration
            assert (uid is not None) == (expect == "back"), \
                "dependency misdeclared: %s %s" % (blkname, elem)
    uniq = lambda rows, i: len({r[i] for r in rows})
    if verbose:
        total = len(internal) + len(resolved) + len(forward)
        print("\nCHAPTER DEPENDENCY PROOF — %d edges from 3 block tables:"
              % total)
        print("  INTERNAL (seam edges inside 21:1-37, self-supplied): %d"
              % len(internal))
        for blk, elem, ref, claim in internal:
            print("    %-36s <- %-14s [%s] (%s)" % (elem[:36], ref, claim, blk))
        print("  RESOLVED (external verse inside a frozen unit): %d across %d"
              " unique verses" % (len(resolved), uniq(resolved, 2)))
        for blk, elem, ref, claim, uid in resolved:
            print("    %-36s <- %-14s [%s] unit=%s" % (elem[:36], ref, claim, uid))
        print("  FORWARD demands (external verse NOT yet derived): %d across"
              " %d unique verses" % (len(forward), uniq(forward, 2)))
        for blk, elem, ref, claim in forward:
            print("    %-36s <- %-14s [%s] OPEN" % (elem[:36], ref, claim))
    return internal, resolved, forward

# ===========================================================================
# THE RUN — all three block batteries + the seams + a World replay demo
# ===========================================================================
def run():
    print("=== block batteries ===")
    b1.run()
    b2.run()
    b3.run()

    print("\n=== chapter seams ===")
    mvo = seam_man_vs_ox()
    assert mvo["man_heads"] == 5 and mvo["ox_heads"] == 1, \
        "BK 8:2: five heads in man, nezek alone in ox"
    assert "EXEMPT" in mvo["fetus_payer"]["ox"], \
        "the ox's owner is clear of fetus-value"

    tpl = seam_forewarned_templates()
    assert tpl["man"] is True and tpl["ox_starts"] == "tam", \
        "man is born forewarned; the ox must acquire the state"

    sv = seam_slave_victim()
    assert sv["master"] == "death" and sv["ox_owner_pays"] == 30, \
        "one victim, two tracks: the sword vs the flat thirty"

    ma = seam_manumission_actor()
    assert ma["master_frees"] and not ma["ox_frees"], \
        "BK 3:10: the master's blow frees; his ox's blow frees no one"

    pv = seam_parent_victim()
    assert pv["son"] == "death" and pv["son_payment"] == "absorbed", \
        "BK 3:10: the ox pays the parent; the son is capital, money absorbed"

    ta = seam_tachat_anchor()
    assert ta["eye_mode"] == "money" and ta["anchor_internal"], \
        "Rav Ashi's anchor (21:36) is self-supplied inside the chapter"

    sp = seam_statute0_parity()
    assert sp["runtime_flag"] and sp["woman_striker"] == "death" \
        and sp["woman_thief"], "statute-0 gender parity holds in all blocks"
    print("seams: man-vs-ox / templates / slave-victim / manumission-actor /"
          " parent-victim / tachat-anchor / statute-0 parity — OK")

    print("\n=== World replay demo (the pass-2 state layer) ===")
    w = World()
    # the ox line: three gorings on three world-days vest the state
    ox = w.register_ox("reuven")
    for _ in range(3):
        w.advance(1)
        w.goring(ox, owner_present_testimony=True)
    assert w.ox_status(ox) == "muad", "vested on world time"
    w.condemn(ox)
    assert w.ox_benefit(ox).startswith("FORBIDDEN"), \
        "the ban rides the STANDING verdict [b3 L28-05]"
    w.execute(ox)
    assert w.ox_benefit(ox) == "permitted — carcass", \
        "executed: the verdict is spent"
    # the slave line: the six-year clock runs on the SAME world clock
    sid, _ = w.enslave_by_court(theft=1000, worth_six_years_labor=500)
    assert w.slave_status(sid) == "SERVING"
    w.advance(6 * 365)
    assert w.slave_status(sid) == "FREE", "the term ends, he walks — חנם "\
        "('for nothing') [b1 L2-05]"
    # hysteresis on world time: one petting day reverts a fresh mu'ad
    ox2 = w.register_ox("shimon")
    for _ in range(3):
        w.advance(1)
        w.goring(ox2, owner_present_testimony=True)
    w.petting_day(ox2)
    assert w.ox_status(ox2) == "tam", "one clean day breaks the vested state"
    snap = w.snapshot()
    assert snap["slaves"][sid] == "FREE" and len(snap["standing_verdicts"]) == 1
    print("World: ox vesting / verdict state-writes / slave clock /"
          " hysteresis / snapshot — OK")

    print("\nCHAPTER ASSEMBLY exo_21_v2 DRAFT: ALL GREEN "
          "(3 block batteries + 7 seams + World).")

if __name__ == "__main__":
    run()
    chapter_dependency_proof()
