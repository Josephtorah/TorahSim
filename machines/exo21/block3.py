#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# LAW ERA v2 DERIVATION — DRAFT (pre-freeze)
# exo_21 block 3 (+tail): Exodus 21:28-37 — goring ox, pit, ox-vs-ox, theft
#
# Derived 2026-08-12 from the COMPLETE oral inversion (block 3: 23 clips,
# 1,130/1,130 rows; tail 21:37: 4 clips, 172/172 rows — chapter ledger 4,903
# = census EXACT, EXOD 21 CHAPTER GATE GREEN). Witness layer:
#   scans/manifests/law03_exo_21_28_37_claims.json (L28..L37, L0)
# Every rule below carries its claim-ID; every claim carries its sources.
#
# STATUS: DRAFT. Chapter scan gate is GREEN; the v2 YAML + freeze land after
# the block-2 coding day + chapter assembly. Experimental model — not binding
# religious law.
# =============================================================================

# ---------------------------------------------------------------------------
# CONSTANTS — the block's numbers (each with its derivation status)
# ---------------------------------------------------------------------------
MUAD_GORINGS = 3        # three gorings vest the forewarned state    [L29-01]
MUAD_DAYS_RULE = True   # R. Yehudah: on three DAYS (halakhah)       [L29-01]
REVERSION_CLEAN_DAYS = 1  # hysteresis: ONE petting-day reverts      [L29-01]
PIT_DEATH_DEPTH = 10    # handbreadths; the hevel (vapor) pit        [L33-01]
PIT_INJURY_DEPTH = 9    # liable for injury only — the missing ומת   [L33-01]
PIT_IMPACT_DEPTH = 6    # chavata (impact) floor: belly rides 4 off  [L33-01]
SLAVE_TARIFF = 30       # shekels, flat, kapparah not price          [L32-01/02]
OX_TARIFF = 5           # gezerat melekh + four derivations          [L37-05]
SHEEP_TARIFF = 4        #   (double-of-double+labor / decree-minus-  [L37-05]
KEFEL = 2               #    dignity / breeding / trouble-pity)
COURT_SIZE = 23         # the ox gets the court, not the mercies     [L28-03]
CONVICT_MARGIN_OX = 1   # convictable by ONE vote (man needs two)    [L28-03]

# ---------------------------------------------------------------------------
# CASE — the forewarned-state machine (21:28-29)                [L29-01..05]
# תם ("innocent") -> מועד ("forewarned"), context-indexed, with hysteresis
# ---------------------------------------------------------------------------
def new_ox(owner="reuven"):
    return {"owner": owner, "gorings": [],       # (day, species, context)
            "warned_in_owner_presence": False,   # והועד בבעליו [L29-03]
            "clean_pet_days": 0}

def record_goring(ox, day, species="ox", context="weekday",
                  owner_present_testimony=False):
    ox["gorings"].append((day, species, context))
    ox["clean_pet_days"] = 0
    if owner_present_testimony:
        ox["warned_in_owner_presence"] = True
    return ox

def record_clean_petting_day(ox):
    """Children pet it un-gored: ONE day breaks the vested state —
    acquiring a habit is slow, breaking it is proof. [L29-01]"""
    ox["clean_pet_days"] += 1
    return ox

def status(ox, species="ox", context="weekday", victim_is_man=False):
    """Context-indexed forewarning. Mu'ad-for-beasts is NOT mu'ad-for-man
    (אדם אית ליה מזלא — man's protection blocks the transfer). [L28-01,L29-01]"""
    if ox["clean_pet_days"] >= REVERSION_CLEAN_DAYS:
        return "tam"
    hits = [g for g in ox["gorings"] if g[2] == context]
    if victim_is_man:
        hits = [g for g in hits if g[1] == "man"]   # beast-kills don't vest
    if len(hits) < MUAD_GORINGS:
        return "tam"
    if MUAD_DAYS_RULE and len({d for d, s, c in hits}) < MUAD_GORINGS:
        return "tam"                                 # 3 DAYS, not 3 events
    if not ox["warned_in_owner_presence"]:
        return "tam"    # the vesting needs the capital-style process [L29-03]
    return "muad"

def evidence_regime(victim):
    """Two regimes in two words: ox-kills-MAN = והועד (capital-style: no
    umdena, testimony in the owner's presence); ox-kills-OX = נודע
    (money-style: camel-among-camels inference suffices). [L29-03]"""
    return ("hu'ad: owner present, no circumstantial" if victim == "man"
            else "noda: umdena and absent-party testimony suffice")

# ---------------------------------------------------------------------------
# CASE — the stoning (21:28)                                    [L28-02..06]
# ---------------------------------------------------------------------------
def stoning_verdict(victim_is_human, intended_this_victim=True,
                    intended_human=True, goaded=False, terefah_ox=False,
                    judges=COURT_SIZE, has_owner=True):
    """The animal itself is the defendant — ownerless/hekdesh oxen stoned
    too (guilt attaches to the ANIMAL; Gen 9:5 delegated). [L28-02,L28-04]"""
    if not victim_is_human:
        return {"stoned": False, "reason": "capital track is man-only"}
    if judges < COURT_SIZE:
        return {"stoned": False, "reason": "23 required [L28-03]"}
    if goaded:
        return {"stoned": False, "altar_barred": True,
                "reason": "כי יגח — of its own accord, not when they make it gore"}
    if not (intended_this_victim and intended_human):
        return {"stoned": False,
                "reason": "את איש — aimed at a beast, killed a man: exempt"}
    if terefah_ox:
        return {"stoned": False, "reason": "terefah-ox exempt (as its owner would be)"}
    return {"stoned": True, "ownerless_included": not has_owner,
            "benefit": "banned from GMAR DIN (the verdict), hide included via את",
            "reason": "capital process complete"}

def benefit_status(verdict_standing, executed):
    """The issur hangs on a STANDING verdict, not the stones: verdict
    dissolved after execution -> carcass permitted; before -> back to the
    herd. [L28-05]"""
    if verdict_standing:
        return "FORBIDDEN (flesh and hide; slaughter-after-verdict stays forbidden)"
    return "permitted — carcass" if executed else "returns to the herd"

# ---------------------------------------------------------------------------
# CASE — the owner after a killing (21:29-32)                   [L29-04..L32]
# ---------------------------------------------------------------------------
def owner_liability(ox_status, victim, victim_died=True, intentional=True,
                    partners=1, victim_value=100, guarded_reduced=False,
                    body_owner="master"):
    """Returns the owner's ledger. The mu'ad owner 'dies' by HEAVEN (the
    halakhah uproots the verse) and buys himself back with kofer."""
    if ox_status == "tam":
        return {"capital": None, "kofer": 0, "slave_fine": 0,
                "note": "בעל השור נקי — clear even in Heaven's court [L28-06]"}
    if guarded_reduced:
        return {"capital": None, "kofer": 0, "slave_fine": 0,
                "note": "reduced guarding SUFFICES for the mu'ad — "
                        "it has a voice (קלא אית ליה) [L29-05]"}
    if not intentional:
        return {"capital": None, "kofer": 0, "slave_fine": 0,
                "note": "no stoning -> no fine and no kofer "
                        "(Resh Lakish coupling) [L30-02]"}
    if victim == "slave":
        return {"capital": "death by Heaven", "kofer": 0,
                "slave_fine": SLAVE_TARIFF, "paid_to": body_owner,
                "note": "flat 30: kapparah, payable above worth; melog -> "
                        "the WIFE (body beats fruits) [L32-01]"}
    if not victim_died:
        return {"capital": None, "kofer": 0, "slave_fine": 0,
                "note": "kofer only after the victim dies [L30-01]"}
    return {"capital": "death by Heaven [L29-04]",
            "kofer": partners * victim_value,   # FULL kofer per partner
            "kofer_basis": "the VICTIM's value (פדיון נפשו)",
            "rides_on_top": "teshuvah, fasting, charity [L30-01]",
            "heirs": "the woman's kofer to HER heirs (expectancy)",
            "note": "atonement that is also a collectible debt"}

def kofer_admissible(defendant):
    """The boundary: ransom is for the OWNER'S NEGLIGENCE only. [L30-02]"""
    return {"ox_owner": True,
            "human_murderer": False,     # Num 35:31 — no kofer for a life
            "pit_death": False,          # no category: the guilt stays before God
            }[defendant]

# ---------------------------------------------------------------------------
# CASE — ownership continuity (21:36 בעליו, "its owner")         [L36-01]
# ---------------------------------------------------------------------------
def money_claim_survives(ownerless_after_goring, condemned=False):
    if ownerless_after_goring:
        return {"damages": False, "stoning": True,
                "collect_from": "the condemned ox's plow-earnings while it waits"
                if condemned else None,
                "note": "ownership must persist goring -> judgment"}
    return {"damages": True, "stoning": True, "collect_from": "meitav (best land)"}

# ---------------------------------------------------------------------------
# CASE — the pit (21:33-34)                                     [L33-01..04]
# ---------------------------------------------------------------------------
def pit_liability(depth, victim="ox", outcome="death", pit_kind="hevel",
                  covered_properly=False, cover_rotted_within=False,
                  handed_to_public=False, fell_inside=True, completer=None):
    """The depth law hangs on the missing ומת; man and vessels are excluded
    by DECREE; the completer of the tenth handbreadth owns the whole pit."""
    if victim in ("man", "vessels"):
        return {"liable": False,
                "forum": "Heaven — לא תשים דמים בביתך; no money remedy",
                "note": "שור ולא אדם, חמור ולא כלים — gezerat ha-katuv [L33-02]"}
    if handed_to_public:
        return {"liable": False, "note": "Nechunya's rule: dug and handed "
                "to the public — he fulfilled this law [L33-03]"}
    if covered_properly:
        return {"liable": False, "note": "covered -> clear, even if the cover "
                "rotted from within (CM 410:22) [L33-03]"
                if cover_rotted_within else "covered properly [L33-03]"}
    if not fell_inside:
        return {"liable": False,
                "note": "karka olam — the world's ground hurt it [L33-02]"}
    death_floor = PIT_DEATH_DEPTH if pit_kind == "hevel" else PIT_IMPACT_DEPTH
    if outcome == "death" and depth < death_floor:
        return {"liable": False, "injury_track": depth >= PIT_INJURY_DEPTH,
                "note": "nine-handbreadth pit: injury only — the missing "
                        "ומת, handed to the sages [L33-01]"}
    payer = completer or "digger"
    return {"liable": True, "payer": payer,
            "payer_note": "he who fills the tenth handbreadth pays for the "
                          "WHOLE pit (the Gra's plene/defective run) [L33-01]",
            "carcass": "to the VICTIM (halakhah; peshat to the damager — "
                       "the split stated openly) [L34-01]",
            "hauling": "the pit-owner pays the lift-out (Ralbag) [L34-01]",
            "heir_transfer": False,   # the Rogatchover: no yerushah on a
            "buyer_donee_transfer": True,  # liability without substance [L33-04]
            "gendered": False}   # בעל הבור ("pit-owner") ungendered [L33-04]

# ---------------------------------------------------------------------------
# CASE — ox vs ox (21:35-36)                                    [L35, L36]
# ---------------------------------------------------------------------------
def ox_vs_ox(gorer_status, gorer_live_value, gored_value, carcass_value,
             victim_owner="commoner", gorer_owner="commoner"):
    """The tam split (sell the LIVE ox, halve), the three-case table, the
    no-profit fence; the mu'ad pays in full from the best."""
    # hekdesh asymmetry [L36-02]
    if gorer_owner == "hekdesh":
        return {"pays": 0, "note": "hekdesh ox gored a commoner's: EXEMPT"}
    if victim_owner == "hekdesh":
        return {"pays": gored_value - carcass_value,
                "note": "commoner's ox gored hekdesh: FULL even as tam"}
    if victim_owner == "gentile_lawless":
        return {"pays": gored_value - carcass_value, "kenas": True,
                "note": "רעהו forfeiture: full even as tam — and nations "
                        "keeping the seven are judged as Israel [L36-02]"}
    damage = gored_value - carcass_value
    if gorer_status == "muad":
        return {"pays": damage, "source": "meitav — best land [L36-01]",
                "carcass": "offsets, to the victim"}
    half = damage / 2.0
    pays = min(half, gorer_live_value)      # from the BODY only [L29-02]
    return {"pays": pays, "source": "the tam's own body (sell the live ox)",
            "classification": "KENAS — palga nizka is a fine [L35-02]",
            "babylonia_collectible": False,  # fines need ordination
            "babylonia_remedies": ["victim's seizure stands",
                                   "summons to the Land",
                                   "excommunication until the hazard is removed"],
            "no_profit_cap": min(half, damage),   # owners pay, never collect
            "partnership": "victim becomes part-owner of the living tam "
                           "(sale-and-split protects him from co-holding "
                           "with his damager) [L35-03]"}

def three_case_table():
    """Yalkut 341:19: 100 gores 200 -> the whole gorer; 200 gores 100 -> a
    quarter; equals -> half. [L35-01]"""
    out = {}
    for gorer, gored in ((100, 200), (200, 100), (200, 200)):
        damage = gored          # total loss cases in the paradigm
        half = damage / 2.0
        out[(gorer, gored)] = min(half, gorer)
    return out

# ---------------------------------------------------------------------------
# CASE — the theft tariff (21:37)                               [L37-01..06]
# ---------------------------------------------------------------------------
def theft_tariff(animal, disposed=True, disposal="slaughter", whole=True,
                 irreversible=True, act_causes_prohibition=False,
                 via_agent=False, thief_owned_first=False,
                 owner="commoner", confessed_in_court=False,
                 courts_ordained=True, thief_is_woman=False):
    """Returns the multiplier owed (including the principal: 'four and it').
    The 4/5 CONTAINS the double — where the double dies, everything dies."""
    if animal not in ("ox", "sheep"):
        return {"multiplier": KEFEL,
                "note": "ox and sheep only — the redundancy geometry [L37-01]"}
    if owner in ("hekdesh", "gentile"):
        return {"multiplier": 0,
                "note": "the double dies (מבית האיש / רעהו) -> 'not "
                        "three-and-four': total collapse [L37-04]"}
    if confessed_in_court and courts_ordained:
        return {"multiplier": 1,
                "note": "self-confession kills fines — the principle "
                        "restored unasked (Hirsch); principal only [L37-06]"}
    if not courts_ordained:
        return {"multiplier": 1, "fine_uncollectable": True,
                "note": "jurisdiction decay: no fines-courts -> no fine, "
                        "and no confession-exemption either (Tur 348:8); "
                        "the flying scroll enforces from Heaven [L37-06]"}
    if not disposed:
        return {"multiplier": KEFEL, "note": "theft alone: the double"}
    if thief_owned_first:
        return {"multiplier": KEFEL,
                "note": "inherited/consecrated-first or change-of-form: he "
                        "slaughters HIS OWN — no 4/5 [L37-04]"}
    if not (whole and irreversible) or act_causes_prohibition:
        return {"multiplier": KEFEL,
                "note": "וטבחו all-of-it; sale irreversible; the act must "
                        "not CAUSE the prohibition (Shabbat-slaughter "
                        "exempt, tereifah liable) [L37-02]"}
    mult = OX_TARIFF if animal == "ox" else SHEEP_TARIFF
    return {"multiplier": mult,
            "composition": "kefel + increment; includes the principal "
                           "('four and it') [L37-04]",
            "agency": "slaughter-by-agent convicts the THIEF — the lone "
                      "agent-for-sin liability, fenced by "
                      "two-verses-as-one [L37-03]" if via_agent else None,
            "woman_thief_liable": True,   # ישלם covers her [L37-01]
            "payment_quality": "each beast must STAND IN PLACE of the "
                               "stolen one — no five wasted negidin [L37-04]"}

# ===========================================================================
# THE RUN — assertion battery
# ===========================================================================
def run():
    # --- the state machine ------------------------------------------------
    ox = new_ox()
    for day in (1, 2):
        record_goring(ox, day, owner_present_testimony=True)
    assert status(ox) == "tam", "two gorings: still tam"
    record_goring(ox, 2, owner_present_testimony=True)
    assert status(ox) == "tam", "R. Yehudah: three DAYS, not three events"
    record_goring(ox, 3, owner_present_testimony=True)
    assert status(ox) == "muad", "3 gorings / 3 days / owner-present: vested"
    record_clean_petting_day(ox)
    assert status(ox) == "tam", "hysteresis: ONE petting day reverts [L29-01]"

    sab = new_ox()
    for day in (7, 14, 21):
        record_goring(sab, day, context="sabbath", owner_present_testimony=True)
    assert status(sab, context="sabbath") == "muad", "mu'ad for Sabbaths"
    assert status(sab, context="weekday") == "tam", "tame on weekdays [L29-01]"

    beast_killer = new_ox()
    for day in (1, 2, 3):
        record_goring(beast_killer, day, species="ox",
                      owner_present_testimony=True)
    assert status(beast_killer, victim_is_man=True) == "tam", \
        "mu'ad-for-beasts is NOT mu'ad-for-man (mazal) [L28-01]"

    unwitnessed = new_ox()
    for day in (1, 2, 3):
        record_goring(unwitnessed, day)      # no owner-present testimony
    assert status(unwitnessed) == "tam", \
        "והועד בבעליו: no vesting absent the owner (Yannai's clause) [L0-02]"
    assert "owner present" in evidence_regime("man")
    assert "umdena" in evidence_regime("ox")

    # --- the stoning --------------------------------------------------------
    v = stoning_verdict(victim_is_human=True, has_owner=False)
    assert v["stoned"] and v["ownerless_included"], \
        "the wilderness ox is stoned — guilt attaches to the ANIMAL [L28-02]"
    assert not stoning_verdict(True, goaded=True)["stoned"], "stadium ox"
    assert stoning_verdict(True, goaded=True)["altar_barred"], \
        "un-stoned yet barred from the altar [L28-04]"
    assert not stoning_verdict(True, intended_human=False)["stoned"], \
        "aimed at a beast, killed a man: exempt [L28-04]"
    assert benefit_status(True, False).startswith("FORBIDDEN")
    assert benefit_status(False, True) == "permitted — carcass", \
        "verdict dissolved after execution [L28-05]"
    assert benefit_status(False, False) == "returns to the herd", \
        "verdict dissolved before stoning [L28-05]"

    # --- the owner ----------------------------------------------------------
    tam_kill = owner_liability("tam", "free_man")
    assert tam_kill["kofer"] == 0 and "נקי" in tam_kill["note"]
    muad_kill = owner_liability("muad", "free_man", victim_value=200, partners=2)
    assert muad_kill["kofer"] == 400, "FULL kofer per partner [L30-01]"
    assert muad_kill["capital"].startswith("death by Heaven")
    slave_kill = owner_liability("muad", "slave", body_owner="the wife (melog)")
    assert slave_kill["slave_fine"] == 30 and slave_kill["paid_to"].startswith("the wife")
    assert owner_liability("muad", "free_man", intentional=False)["kofer"] == 0, \
        "no stoning -> no kofer (Resh Lakish) [L30-02]"
    assert owner_liability("muad", "free_man", guarded_reduced=True)["kofer"] == 0, \
        "reduced guarding suffices for the mu'ad [L29-05]"
    assert kofer_admissible("ox_owner") and not kofer_admissible("human_murderer")
    assert not kofer_admissible("pit_death"), "money cannot reach it [L30-02]"
    half_slave = SLAVE_TARIFF / 2
    assert half_slave == 15, "the half-slave: 15 kenas + half-kofer [L32-01]"

    # --- ownership continuity ----------------------------------------------
    aband = money_claim_survives(ownerless_after_goring=True, condemned=True)
    assert not aband["damages"] and aband["stoning"]
    assert "plow-earnings" in aband["collect_from"], "R. Akiva Eiger's answer"

    # --- the pit ------------------------------------------------------------
    assert not pit_liability(10, victim="man")["liable"], "שור ולא אדם [L33-02]"
    assert not pit_liability(10, victim="vessels")["liable"], "חמור ולא כלים"
    nine = pit_liability(9, outcome="death")
    assert not nine["liable"] and nine["injury_track"], \
        "the nine-pit: injury only — the missing ומת [L33-01]"
    assert pit_liability(10)["liable"], "the ten-pit kills"
    assert pit_liability(6, pit_kind="impact")["liable"], \
        "impact-pit: six suffice (belly rides four off the ground) [L33-01]"
    assert not pit_liability(10, covered_properly=True,
                             cover_rotted_within=True)["liable"], \
        "the worm-eaten cover: still clear (CM 410:22) [L33-03]"
    assert not pit_liability(10, handed_to_public=True)["liable"], "Nechunya"
    assert not pit_liability(10, fell_inside=False)["liable"], "karka olam"
    comp = pit_liability(10, completer="the tenth-handbreadth digger")
    assert comp["payer"] == "the tenth-handbreadth digger", "the Gra's run"
    assert comp["heir_transfer"] is False and comp["buyer_donee_transfer"], \
        "the Rogatchover's uninheritable pit [L33-04]"
    assert comp["gendered"] is False, "בעל הבור binds both sexes [L33-04]"
    assert pit_liability(10, victim="chicken")["liable"], \
        "the fill of the faller — even a chicken [L33-02]"

    # --- ox vs ox -----------------------------------------------------------
    t = three_case_table()
    assert t[(100, 200)] == 100, "victim takes the WHOLE gorer"
    assert t[(200, 100)] == 50, "a quarter"
    assert t[(200, 200)] == 100, "equals: half [L35-01]"
    tam_case = ox_vs_ox("tam", 200, 200, 0)
    assert tam_case["pays"] == 100 and not tam_case["babylonia_collectible"], \
        "palga nizka is a FINE — not collected in Babylonia [L35-02]"
    assert "seizure" in tam_case["babylonia_remedies"][0]
    muad_case = ox_vs_ox("muad", 200, 200, 50)
    assert muad_case["pays"] == 150 and "meitav" in muad_case["source"]
    assert ox_vs_ox("tam", 200, 200, 0, gorer_owner="hekdesh")["pays"] == 0
    assert ox_vs_ox("tam", 200, 200, 0, victim_owner="hekdesh")["pays"] == 200, \
        "the hekdesh asymmetry [L36-02]"

    # --- the theft tariff ---------------------------------------------------
    assert theft_tariff("ox")["multiplier"] == 5
    assert theft_tariff("sheep")["multiplier"] == 4, \
        "Nathan's lamb: ארבעתים — the catalog's flagship constant [L37-04]"
    assert theft_tariff("camel")["multiplier"] == 2, "ox and sheep only"
    assert theft_tariff("ox", owner="hekdesh")["multiplier"] == 0, \
        "'not three-and-four': the composed tariff collapses [L37-04]"
    assert theft_tariff("ox", disposed=False)["multiplier"] == 2
    assert theft_tariff("ox", whole=False)["multiplier"] == 2, "כולו בעינן"
    assert theft_tariff("ox", act_causes_prohibition=True)["multiplier"] == 2, \
        "Shabbat-slaughter exempt; tereifah stays liable [L37-02]"
    assert theft_tariff("ox", thief_owned_first=True)["multiplier"] == 2, \
        "the lamb grown to a ram: he slaughters his own [L37-04]"
    agent = theft_tariff("ox", via_agent=True)
    assert agent["multiplier"] == 5 and "agent-for-sin" in agent["agency"], \
        "the lone agency exception [L37-03]"
    assert theft_tariff("ox", confessed_in_court=True)["multiplier"] == 1, \
        "confession kills the fine — Hirsch's derivation [L37-06]"
    today = theft_tariff("ox", courts_ordained=False)
    assert today["multiplier"] == 1 and today["fine_uncollectable"], \
        "jurisdiction decay (Tur 348:8) [L37-06]"
    assert OX_TARIFF == SHEEP_TARIFF + 1 == KEFEL * KEFEL + 1, \
        "R. Meir's arithmetic: double-of-double, +1 for the labor [L37-05]"

    print("BLOCK 3 (+21:37 tail) DRAFT: all asserts GREEN.")
    print("state machine / stoning / kofer / pit / ox-vs-ox / tariff: OK")

# ===========================================================================
# CROSS-VERSE DEPENDENCY PROOF (block-1 pattern)
# ===========================================================================
DEPENDS = [
    ("stoning charter (beast answerable)", "Genesis", 9, 5, "back", "L28-02",
     "מיד כל חיה אדרשנו — the Noahide demand the stoning delegates"),
    ("pit precedent: the open pit", "Genesis", 37, 24, "back", "L33-01",
     "Joseph's pit — empty, no water; the human-victim branch runs to Heaven"),
    ("Sinai runs the protocol", "Exodus", 19, 13, "back", "L28-02",
     "beast or man that touches the mountain is stoned — pre-statute deploy"),
    ("KEFEL's parent ban", "Exodus", 20, 13, "back", "L37-06",
     "the Decalogue's theft-ban — the double's constitutional layer"),
    ("the stoning verb's register", "Exodus", 8, 22, "back", "L28-02",
     "הן נזבח ולא יסקלנו (\"let us slaughter, not stone him\") — the "
     "mob-execution verb"),
    ("the tariff's own verse", "Exodus", 21, 37, "back", "L37-04",
     "inside frozen unit exo_21_the_ordinances (21:1-37, FWD-8)"),
    # ---- forward demands: constants consumed from verses NOT yet derived --
    ("kofer BAN for the murderer", "Numbers", 35, 31, "fwd", "L30-02",
     "לא תקחו כפר לנפש רצח — the complement that bounds 21:30"),
    ("beast-restitution restatement", "Leviticus", 24, 18, "fwd", "L34-01",
     "נפש תחת נפש for beasts — the block's tanakh-close verse"),
    ("the Arakhin table behind the 30", "Leviticus", 27, 4, "fwd", "L32-02",
     "the woman's thirty — the erekh the slave-tariff borrows"),
    ("the double's own pericope", "Exodus", 22, 3, "fwd", "L37-04",
     "חיים שנים ישלם — the kefel component the 4/5 contains"),
    ("burglar-clause border", "Exodus", 22, 1, "fwd", "L37-06",
     "אין לו דמים — block-4 territory, ledgered in the tail close"),
    ("the thirty as shepherd's wage", "Zechariah", 11, 12, "fwd", "L32-02",
     "וישקלו את שכרי שלשים כסף — the tariff constant in prophecy"),
    ("the fourfold executed", "II Samuel", 12, 6, "fwd", "L37-05",
     "ארבעתים — Nathan's verdict, the chapter ledger's final row"),
    ("the kofer disjunction in narrative", "I Kings", 20, 39, "fwd", "L30-01",
     "נפשך תחת נפשו או ככר כסף — the life-or-money fork as parable"),
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
            if b != book:
                continue
            if (ch, vs) >= (c1, v1) and (ch, vs) <= (c2, v2):
                return uid
        return None
    resolved, forward = [], []
    for elem, book, ch, vs, expect, claim, what in DEPENDS:
        uid = resolve(book, ch, vs)
        row = (elem, "%s %d:%d" % (book, ch, vs), claim, what, uid)
        if uid:
            resolved.append(row)
        else:
            forward.append(row)
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
