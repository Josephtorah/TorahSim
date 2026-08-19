#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# LAW ERA v2 DERIVATION — DRAFT (pre-freeze)
# exo_21 block 1: Exodus 21:1-11 — the slave-term laws
#
# Derived 2026-08-11 from the COMPLETE oral inversion (84 bites, 1,962/1,962
# listings, BLOCK-1 GATE GREEN). Witness layer:
#   scans/manifests/law01_exo_21_1_11_claims.json  (claims L1..L11)
# Every rule below carries its claim-ID; every claim carries its sources.
#
# STATUS: DRAFT. The frozen unit exo_21_the_ordinances spans 21:1-37; the
# freeze-ritual's oral-coverage gate is chapter-wide and stays FAIL until
# blocks 2-3 (21:12-37) are scanned. This file is the block-1 slice of the
# v2 machine, runnable now; the v2 YAML + freeze land after block 3.
# Experimental model — not binding religious law.
# =============================================================================

# ---------------------------------------------------------------------------
# STATUTE 0 — THE HEADER (21:1): the runtime environment          [L1-01..07]
# ואלה המשפטים אשר תשים לפניהם ("and these are the ordinances which you
# shall set before them")
# ---------------------------------------------------------------------------
RUNTIME = {
    "forum": "ordained-chain-to-Moses",      # [L1-01] lifnehem: never gentile
    "gentile_court_even_same_law": False,     #   courts — outcome-identity does
    "layman_curable_by_consent": True,        #   not license the forum; laymen
    "gentile_curable_by_consent": False,      #   cured by consent, gentiles never
    "coercion_requires_ordination": True,     # [L1-02] the judgment/coercion split
    "promulgation_is_precondition": True,     # [L1-03] a release-right unpublished
    "gender_parity_all_monetary_law": True,   # [L1-06]        is void
    "compromise_offered_before_verdict": True # [L1-07]
}

# The module dependency: the whole block runs only while yovel runs. [L2-08]
YOVEL_OPERATES = True          # historical runtime flag (dormant today)
YOVEL_YEAR = 50                # the epoch-constant: le-olam = to the yovel

TERM_YEARS = 6                 # the non-derivable constant: the week's
                               # theology run as penology [L11-04]
CHILD_SUPPORT_YEARS = 6        # derived FROM the term-length [L3-02]

# ---------------------------------------------------------------------------
# CASE 1 — כי תקנה עבד עברי ("when you acquire a Hebrew slave"), 21:2
# ---------------------------------------------------------------------------
def court_sale(theft, worth_six_years_labor, male=True, insolvent=True,
               by_witnesses=True, victim_consents_to_sale=True):
    """Entry path 1: the court-sold thief. Returns a slave-record or a
    rejection (reason). The self-seller (Lev 25) is a DIFFERENT class. [L2-01]"""
    if not YOVEL_OPERATES:
        return None, "module dormant: eved ivri runs only while yovel runs [L2-08]"
    if not male:
        return None, "bi-gnevato ve-lo bi-gnevatah: a woman is never sold [L2-01]"
    if not by_witnesses:
        return None, "no confession-sale: witnesses required [L2-01]"
    if not insolvent:
        return None, "assets exist: forced payment, sale invalid [L2-01]"
    # THE PROPORTIONALITY GATE [L2-02]: sold whole, never half.
    if theft < worth_six_years_labor:
        return None, "nimkar kullo ve-lo chetzyo: labor impounded, freedom untouched [L2-02]"
    if not victim_consents_to_sale:
        return None, "the victim's option: a promissory note instead [L2-02]"
    return {
        "class": "eved_ivri", "entry": "court_sale",
        "term_start_day": 0,                       # the SALE-clock, me'et le'et:
        "term_days": TERM_YEARS * 365,             # anniversary years, never the
        "clock": "sale-anniversary",               # calendar shemittah [L2-03]
        "served_days": 0, "sick_days": 0, "fled_days": 0,
        "married_at_entry": None, "pierced": False,
        "dignity": DIGNITY_FLOOR,                  # [L2-07]
    }, "sold for the PRINCIPAL only, never the fine [L2-01]"

DIGNITY_FLOOR = {
    "status_word_is_tag_not_insult": True,   # "the Torah called him slave
    "slave_customs_banned": ["foot-washing", "sandal-carrying",   # against its
                             "litter", "bathhouse-gear"],         # will" [L2-07]
    "trade_switch_banned": True, "public_serving_trade_banned": True,
    "equality": "food, drink, bedding equal to the master's",
    "one_bed_case": "the slave gets the bed (kofin al middat Sedom)",
}

# ---------------------------------------------------------------------------
# HANDLER — the timer semantics (fault-typed)                         [L2-04]
# ---------------------------------------------------------------------------
def term_status(slave, elapsed_days):
    """The runaway completes; the sick exit ON TIME unless idle a majority
    of the term (light-duty 'needle-work' capability keeps the clock)."""
    effective = elapsed_days - slave["fled_days"]      # flight tolls the clock
    sick_years = slave["sick_days"] / 365.0
    must_complete = sick_years >= 4                    # sick 4+ = completes;
    if effective >= slave["term_days"] and not must_complete:
        return "FREE"                                  # sick <=3 exits on time
    return "SERVING"

def exit_cost(medical_outlays_by_master):
    """חנם ('for nothing'): no document, no payment, no repayment of idle
    time, food, or medicine. Auto-expiry — the term ends, he walks. [L2-05]"""
    return 0

def heir_service(slave, master_has_son):
    """The term passes to the SON only; the pierced and the amah serve no
    heir (causal-lapse: the love was person-specific). [L2-06, L6-03]"""
    if slave.get("pierced") or slave["class"] == "amah":
        return "FREE at master's death"
    return "serves the SON" if master_has_son else "FREE (no other heir)"

# ---------------------------------------------------------------------------
# HANDLER — maintenance: the substitution model (21:3)          [L3-01, L3-02]
# אם בעל אשה הוא ויצאה אשתו עמו ("if he is a husband, his wife goes out
# with him" — was SHE sold?! → the master owes her keep)
# ---------------------------------------------------------------------------
def master_owes_maintenance(dependent):
    kind, status, age = dependent          # ("wife", fitness, None) / ("child", None, age)
    if kind == "wife":
        return status in ("married-with-him",)     # excludes the betrothed
        # (not 'with him'), the levirate-widow, forbidden unions [L3-01]
    if kind == "child":
        return age < CHILD_SUPPORT_YEARS           # the six-year floor, derived
    return False                                   # from the term-length [L3-02]

# ---------------------------------------------------------------------------
# HANDLER — the shifchah provision (21:4): anti-retention engineering [L4-01]
# ---------------------------------------------------------------------------
def may_receive_shifchah(slave):
    """Master's grant only to the MARRIED slave (wife at ENTRY) — the ban on
    golden-handcuffs retention; the union exclusive, one to one."""
    return slave["entry"] == "court_sale" and slave["married_at_entry"] is True

def child_status(mother_class):
    """האשה וילדיה תהיה לאדוניה — the matrilineal branch: where kiddushin
    cannot hold, the child follows the MOTHER (incl. tumtum/androginos). [L4-02]"""
    return "follows-mother (master's)" if mother_class == "shifchah" else "follows-father"

# ---------------------------------------------------------------------------
# CASE 2 — the declaration and the awl (21:5-6)
# ואם אמר יאמר העבד אהבתי את אדוני ("and if the slave shall SAY, SAY:
# I love my master...")
# ---------------------------------------------------------------------------
def piercing(said_count, said_within_last_perutah, still_slave,
             slave_has_family, master_has_family, mutual_love,
             slave_healthy, master_healthy, slave_is_kohen):
    """The full protocol. R. Yishmael's conditions-gate encoded (R. Akiva's
    'either way' preserved in the manifest). [L5-01, L5-02, L6-01]"""
    if slave_is_kohen:
        return "NOT PIERCED: a kohen is never pierced (the blemish bars his return) [L6-01]"
    if said_count < 2 or not said_within_last_perutah or not still_slave:
        return "NOT PIERCED: two sayings inside the last-perutah window, as a slave [L5-01]"
    checklist = (slave_has_family and master_has_family and mutual_love
                 and slave_healthy and master_healthy)      # both-sick = teyku
    if not checklist:
        return "NOT PIERCED: the bilateral checklist failed [L5-02]"
    return PIERCING_RITE

PIERCING_RITE = {
    "presentation": "to the judges — his sellers; the court rebukes first [L6-01]",
    "site": "standing mounted DOOR (the two-witness assembly: no door "
            "without its post); presentation may use the doorpost [L6-01]",
    "ear": "RIGHT (azen-azen from the metzora — the parameter server) [L6-01]",
    "instrument": "the Torah said AWL — the halakhah: ANYTHING "
                  "(the override registry's canonical third) [L6-02]",
    "actor": "the MASTER personally — no agent, no son, no court officer; "
             "no batching (body-title cannot vest by halves) [L6-01]",
    "result": "serves to YOVEL or the master's death — le-olam = the bounded "
              "forever; serves no heir [L6-03]",
}

# ---------------------------------------------------------------------------
# CASE 3 — וכי ימכור איש את בתו לאמה ("and when a man sells his daughter
# as a maidservant"), 21:7-11
# ---------------------------------------------------------------------------
def father_sale(seller_is_father, daughter_is_minor, father_destitute,
                inheritance_already_sold, buyer_can_marry_her):
    """Entry path 2: marriage-track by design. [L7-01]"""
    if not seller_is_father:
        return None, "only the father sells — not mother, not self [L7-01]"
    if not daughter_is_minor:
        return None, "the sale-window closes at signs (the already-sold exits "\
                     "at signs — a fortiori the unsold cannot enter) [L7-01]"
    if not (father_destitute and inheritance_already_sold):
        return None, "the poverty gate: house, land, last shirt first [L7-01]"
    if not buyer_can_marry_her:
        return None, "sale valid only where yiud can operate — no purchase "\
                     "without a working exit [L8-02]"
    return {
        "class": "amah", "entry": "father_sale",
        "term_days": TERM_YEARS * 365, "clock": "sale-anniversary",
        "purchase_price": None, "served_days": 0,
        "designated": False,            # yiud = the sale's DEFAULT state
        "dignity": "indoor work only — never sent to the market "
                   "(lo tetze ke-tzet ha-avadim, the Mahari Bruna rule) [L7-02]",
    }, "the sale is marriage-track by design [L7-01]"

def yiud(amah, her_consent, his_will, to_son=False, son_is_adult_assenting=True):
    """Designation = EIRUSIN by the ORIGINAL purchase-money; her consent AND
    his (qere = his refusal, ketiv = her veto); unwaivable by contract;
    yiud PRECEDES redemption in the priority ladder. [L8-01, L9-01]"""
    if to_son and not son_is_adult_assenting:
        return "NO YIUD: the son's own assent required (and never the brother) [L9-01]"
    if not (her_consent and his_will):
        return "NO YIUD: consent-symmetry failed → the redemption duty fires [L8-01]"
    amah["designated"] = True           # THE ABSORBING BRANCH: she is a wife;
    amah["exits"] = ["get"]             # signs/six/yovel no longer free her
    return "EIRUSIN by the first monies; her rights = ke-mishpat ha-banot [L9-02]"

def redemption_price(purchase_price, years_served):
    """FLAT pro-rata at the ORIGINAL per-year rate — deduction at cost, not
    market (she is worth MORE now: the master subsidizes; anti-appraisal
    explicit). The master must cooperate and accept assessment. [L8-02]"""
    assert 0 <= years_served <= TERM_YEARS
    return purchase_price * (TERM_YEARS - years_served) / TERM_YEARS

def resale(actor):
    """le-am nokhri lo yimshol: the one-way door — nobody resells, ever."""
    return "VOID (not lashable): master never had the power; the father "\
           "after betrayal never regains it [L8-03]"

# ---------------------------------------------------------------------------
# STATUTE — the triad (21:10): שארה כסותה ועונתה לא יגרע
# ("her food, her clothing, her marital rights he shall not diminish")
# ---------------------------------------------------------------------------
TRIAD = {
    "fields": ("she'er — her food", "kesut — her clothing", "onah — her time"),
    "permutation_table_preserved": True,        # every field migrates across
    "parameters": {                             # the tannaim [L10-01]
        "clothing": "by her age and the season (new in the rains)",
        "food": "the locale's median, scaled by his wealth; rises with him, "
                "never descends (the station-ratchet)",
        "onah": "by occupation — idle nightly; workers 2/wk; donkey-drivers "
                "weekly; camel-drivers monthly; sailors 6-monthly; "
                "scholars Shabbat-eve — and by health",
    },
    "waivability": {"she'er": "waivable by her", "kesut": "waivable by her",
                    "onah": "NEVER (tzaara de-gufa — body-rights bind)"},  # [L10-02]
    "vow_proof": "his vow cannot defeat the duty — the prior lien wins",
    "enforcement": "no lashes (actless lav); the rebellion-fines (+36 barley-"
                   "weights weekly) and the compelled divorce run on it",
    "source_inversion": "written of the AMAH, taught to ALL daughters — "
                        "ba lelamed ve-nimtza lamed [L9-02]",
}

# ---------------------------------------------------------------------------
# HANDLER — the exits: min() over events (21:11)            [L11-01..03]
# ---------------------------------------------------------------------------
def amah_exit(amah, elapsed_years, signs, yovel_arrived, master_died,
              redeemed):
    """'Whichever comes first precedes to free her.' Post-yiud the machine
    switches: wife — get only."""
    if amah["designated"]:
        return "WIFE: exits only by get (chinam min ha-kesef, lo min ha-get)"
    events = []
    if elapsed_years >= TERM_YEARS: events.append("six years")
    if signs:                       events.append("signs (naarut — ein kasef)")
    if yovel_arrived:               events.append("yovel")
    if master_died:                 events.append("master's death (no heir-service)")
    if redeemed:                    events.append("graduated redemption")
    return ("FREE: " + events[0] + " — no money to THIS master (there IS for "
            "another master: the father)") if events else "SERVING"

SEVERANCE = {   # the eligibility table [L11-02]
    "six-years": True, "yovel": True, "master's death": True, "signs": True,
    "flight": False, "deduction-exit": False,   # 'his sending is not from you'
    "fork": "R. Meir flips the deduction-exiter to eligible",
}

# ===========================================================================
# TEST VECTORS — the tradition's own worked examples
# ===========================================================================
def run():
    # -- proportionality gate [L2-02]: the 1000/500 table
    s, why = court_sale(theft=1000, worth_six_years_labor=500)
    assert s is not None                       # theft >= worth → sold
    s2, why2 = court_sale(theft=500, worth_six_years_labor=1000)
    assert s2 is None and "chetzyo" in why2    # sold whole, never half
    s3, why3 = court_sale(theft=1000, worth_six_years_labor=500, male=False)
    assert s3 is None                          # a woman is never sold
    s4, why4 = court_sale(1000, 500, victim_consents_to_sale=False)
    assert s4 is None and "note" in why4       # the victim's veto

    # -- timer semantics [L2-04]: the illness table
    sl, _ = court_sale(1000, 500)
    sl["sick_days"] = 3 * 365                  # sick three years —
    assert term_status(sl, 6 * 365) == "FREE"  #   exits on time
    sl["sick_days"] = 4 * 365                  # sick four —
    assert term_status(sl, 6 * 365) == "SERVING"   # completes
    sl["sick_days"] = 0; sl["fled_days"] = 200     # the runaway
    assert term_status(sl, 6 * 365) == "SERVING"   # completes his flight
    assert term_status(sl, 6 * 365 + 200) == "FREE"
    assert exit_cost(medical_outlays_by_master=300) == 0   # chinam [L2-05]

    # -- maintenance [L3-01..02]
    assert master_owes_maintenance(("wife", "married-with-him", None))
    assert not master_owes_maintenance(("wife", "betrothed", None))
    assert master_owes_maintenance(("child", None, 5))
    assert not master_owes_maintenance(("child", None, 7))   # the six-floor

    # -- shifchah [L4-01..02]: anti-retention
    m, _ = court_sale(1000, 500); m["married_at_entry"] = True
    b, _ = court_sale(1000, 500); b["married_at_entry"] = False
    assert may_receive_shifchah(m) and not may_receive_shifchah(b)
    assert child_status("shifchah").startswith("follows-mother")

    # -- the declaration window [L5-01..02] and the kohen bar
    ok = piercing(2, True, True, True, True, True, True, True, False)
    assert ok is PIERCING_RITE
    assert "window" in piercing(2, False, True, True, True, True, True, True, False)
    assert "checklist" in piercing(2, True, True, True, False, True, True, True, False)
    assert "kohen" in piercing(2, True, True, True, True, True, True, True, True)
    assert heir_service({"class": "eved_ivri", "pierced": True}, True).startswith("FREE")
    assert heir_service({"class": "eved_ivri", "pierced": False}, True) == "serves the SON"

    # -- amah entry gates [L7-01]
    a, _ = father_sale(True, True, True, True, True)
    assert a is not None
    assert father_sale(True, False, True, True, True)[0] is None   # minor only
    assert father_sale(True, True, False, True, True)[0] is None   # poverty gate
    assert father_sale(True, True, True, True, False)[0] is None   # yiud-operable

    # -- redemption arithmetic [L8-02]: the codes' three vectors
    assert redemption_price(60, 3) == 30      # Chinukh 44: 60 din./6yr, worked 3
    assert redemption_price(60, 4) == 20      # SMaG: 60/4yr remaining → 20
    assert abs(redemption_price(100, 2) - 100 * 4 / 6) < 1e-9   # Rashi: maneh,
                                              # worked 2 → refund two-thirds
    # -- the exits: min() and the absorbing branch [L11-01..03]
    a["served_days"] = 0
    assert amah_exit(a, 2, signs=True, yovel_arrived=False,
                     master_died=False, redeemed=False).startswith("FREE: signs")
    assert amah_exit(a, 2, False, False, True, False).startswith("FREE: master")
    a2, _ = father_sale(True, True, True, True, True)
    a2["purchase_price"] = 60
    msg = yiud(a2, her_consent=True, his_will=True)
    assert msg.startswith("EIRUSIN")
    assert amah_exit(a2, 7, True, True, True, False).startswith("WIFE")  # absorbing
    a3, _ = father_sale(True, True, True, True, True)
    assert "redemption duty" in yiud(a3, her_consent=False, his_will=True)
    assert "VOID" in resale("master") and "VOID" in resale("father")

    # -- the triad [L10-01..02]
    assert TRIAD["waivability"]["onah"].startswith("NEVER")
    assert SEVERANCE["deduction-exit"] is False and SEVERANCE["signs"] is True

    print("exo_21 v2 block-1 DRAFT: all assertions hold.")
    print("  39 witnessed claims | gates: proportionality, poverty, consent-")
    print("  symmetry, bilateral checklist | clocks: sale-anniversary, yovel")
    print("  | exits: min() over events, one absorbing branch (yiud) |")
    print("  overrides: awl->anything (the registry) | triad: 3 fields,")
    print("  parameterized, onah unwaivable. Freeze waits on blocks 2-3.")


# ===========================================================================
# CROSS-VERSE DEPENDENCY PROOF                        [owner ask, 2026-08-11]
# The machine's imports declared as edges and VERIFIED against the corpus:
# an edge is RESOLVED if its source verse lies inside a FROZEN unit
# (data/units_index.json, the shipped index of derived units), else it is a
# FORWARD demand — a constant consumed from a verse not yet derived.
# ===========================================================================
DEPENDS = [
    # (machine element, book, chap, verse, expect, claim, what is imported)
    ("TERM_YEARS six-and-one frame", "Genesis", 1, 31, "back", "L11-04",
     "the creation week — the seventh-frees shape (its third scale)"),
    ("TERM_YEARS six-and-one frame", "Exodus", 16, 26, "back", "L11-04",
     "the manna week — six gather, the seventh rests"),
    ("TERM_YEARS six-and-one frame", "Exodus", 20, 9, "back", "L11-04",
     "the Shabbat command — six days' labor, the seventh holy"),
    ("PIERCING_RITE: the awl's 400", "Genesis", 15, 13, "back", "L6-04",
     "the decreed 400 years — the awl's gematria re-enters the closed term"),
    ("PIERCING_RITE: door+post witnesses", "Exodus", 12, 7, "back", "L6-04",
     "the Passover blood on the two doorposts — the Egypt witnesses"),
    ("PIERCING_RITE: the ear that heard", "Exodus", 20, 13, "back", "L6-04",
     "the Decalogue's theft-ban (property-theft nested in the headline)"),
    ("court_sale: national precedent", "Genesis", 37, 28, "back", "L11-05",
     "the Joseph-sale — the nation itself sold for a theft, then freed"),
    ("court_sale: mitzvah-sale carve", "Genesis", 29, 18, "back", "L11-05",
     "Jacob's seven years — self-hire beyond the cap, for marriage"),
    ("resale: the no-degradation ban", "Genesis", 16, 6, "back", "L11-05",
     "Hagar — 'having made her a mistress we cannot re-enslave her'"),
    ("yiud: the betrayal lexeme", "Genesis", 31, 15, "back", "L8-03",
     "Rachel and Leah — 'he has SOLD us; are we not foreigners to him?'"),
    ("TRIAD: the vow-parallel", "Genesis", 28, 20, "back", "L10-01",
     "Jacob's vow — bread, garment, and the LORD-with-me = the three fields"),
    ("RUNTIME: lifnehem's antecedent", "Exodus", 18, 21, "back", "L1-01",
     "Yitro's court-pyramid — the judges the header addresses"),
    ("RUNTIME: the Marah generalities", "Exodus", 15, 25, "back", "L1-04",
     "sham sam lo chok u-mishpat — the klal this pericope details"),
    ("RUNTIME: the altar adjacency", "Exodus", 20, 23, "back", "L1-05",
     "no steps upon My altar — the bench beside the altar, deliberate"),
    # ---- forward demands: constants consumed from verses NOT yet derived --
    ("YOVEL_YEAR = 50; le-olam bound", "Leviticus", 25, 10, "fwd", "L6-03",
     "the yovel proclamation — the epoch that bounds every 'forever'"),
    ("court_sale: the class split", "Leviticus", 25, 39, "fwd", "L2-01",
     "the self-seller's own pericope — the other entry path"),
    ("the sugya-anchor of the block", "Leviticus", 25, 55, "fwd", "L6-04",
     "'for MINE are the children of Israel as slaves' — the prior lien"),
    ("master_owes_maintenance: children", "Leviticus", 25, 41, "fwd", "L3-01",
     "'he and his children with him' — the children's-board parent verse"),
    ("PIERCING_RITE: right-ear source", "Leviticus", 14, 14, "fwd", "L6-01",
     "the metzora's right ear — the azen-azen parameter server"),
    ("shifchah interface", "Leviticus", 19, 20, "back", "L4-01",
     "the shifchah charufah — defined BY our 21:4 provision"),
    ("heir_service: the category pair", "Leviticus", 22, 10, "fwd", "L2-06",
     "toshav=pierced / sachir=six-year in the terumah law"),
    ("SEVERANCE table; the parallel law", "Deuteronomy", 15, 12, "fwd", "L11-02",
     "the haanakah grant + the Re'eh restatement (the diff-pass)"),
]

def _frozen_spans():
    import json, re, os
    path = os.path.join(os.path.dirname(__file__),
                        "..", "..", "data", "units_index.json")
    spans = []
    with open(path, encoding="utf-8") as f:
        units = json.load(f)["units"]
    for u in units:
        m = re.match(r"^(\d+):(\d+)-(?:(\d+):)?(\d+)$", u["refs"].strip())
        if not m:
            continue
        c1, v1 = int(m.group(1)), int(m.group(2))
        c2 = int(m.group(3)) if m.group(3) else c1
        v2 = int(m.group(4))
        spans.append((u["book"], c1, v1, c2, v2, u["unit_id"]))
    return spans

def verify_dependencies(verbose=True):
    spans = _frozen_spans()
    def resolve(book, ch, vs):
        for b, c1, v1, c2, v2, uid in spans:
            if b != book: continue
            if (ch, vs) >= (c1, v1) and (ch, vs) <= (c2, v2):
                return uid
        return None
    resolved, forward = [], []
    for elem, book, ch, vs, expect, claim, what in DEPENDS:
        uid = resolve(book, ch, vs)
        row = (elem, "%s %d:%d" % (book, ch, vs), claim, what, uid)
        if uid: resolved.append(row)
        else:   forward.append(row)
        # the PROOF: every declared-backward edge must land in a frozen unit,
        # and every declared-forward edge must NOT (else the declaration lies)
        assert (uid is not None) == (expect == "back"), \
            "dependency misdeclared: %s <- %s (%s)" % (elem, row[1], uid)
    if verbose:
        print("\nDEPENDENCY PROOF — %d edges verified against units_index.json:"
              % len(DEPENDS))
        print("  RESOLVED (source verse inside a frozen unit): %d" % len(resolved))
        for elem, ref, claim, what, uid in resolved:
            print("    %-36s <- %-14s [%s] unit=%s" % (elem[:36], ref, claim, uid))
        print("  FORWARD demands (source verse NOT yet derived): %d" % len(forward))
        for elem, ref, claim, what, uid in forward:
            print("    %-36s <- %-14s [%s] OPEN" % (elem[:36], ref, claim))
    return resolved, forward

if __name__ == "__main__":
    run()
    verify_dependencies()
