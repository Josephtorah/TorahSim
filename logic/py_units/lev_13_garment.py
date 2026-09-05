#!/usr/bin/env python3
# =============================================================================
# lev_13_garment — 13:47-59
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_13_garment.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Garment nega: wool linen leather (13:47–59)"""
from machine import Machine

m = Machine("lev_13_garment")

# -------------------------- Lev.13.47 · COND_כי (“that”) -------------------
# ‹והבגד כי יהיה› (“and-the-garment that be”)
# ‹בו נגע צרעת› (“in-him/its blow leprosy”)
# ‹… בבגד צמר או› (“in-garment wool or”)
# ‹בבגד פשתים› (“in-garment linen”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:47."
m.step("Lev.13.47")
# witness-tier presupposed read: species_and_work_gate on
# beged_tzemer_o_fishtim — read, not installed
m.witness_read("beged_tzemer_o_fishtim", "species_and_work_gate",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 13 1", "Sifra, Tazria Parashat Nega'im, Chapter 13 2", "Sifra, Tazria Parashat Nega'im, Chapter 13 3", "Sifra, Tazria Parashat Nega'im, Chapter 13 7", "Sifra, Tazria Parashat Nega'im, Chapter 13 9", "Sifra, Tazria Parashat Nega'im, Chapter 13 12", "Sifra, Tazria Parashat Nega'im, Chapter 14 1"])

# -------------------------- Lev.13.48 · ETNACHTA_SPLIT ---------------------
# ‹או בשתי או› (“or in-fixture or”)
# ‹בערב לפשתים ולצמר› (“in-web to-linen and-to-wool”)
# ‹… או בעור או› (“or in-skin or”)
# ‹בכל מלאכת עור› (“in-all work skin”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:48."
m.step("Lev.13.48")

# -------------------------- Lev.13.49 · ETNACHTA_SPLIT ---------------------
# ‹והיה הנגע ירקרק› (“and-be the-blow yellowishness”)
# ‹או אדמדם בבגד› (“or reddish in-garment”)
# ‹או בעור או› (“or in-skin or”)
# ‹בשתי או בערב› (“in-fixture or in-web”)
# ‹או בכל … והראה› (“or in-all … and-see”)
# ‹את הכהן› (“obj-marker the-priest”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:49."
m.step("Lev.13.49")
# witness-tier presupposed read: intensest_shades on yerakrak_adamdam —
# read, not installed
m.witness_read("yerakrak_adamdam", "intensest_shades",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 14 2", "Sifra, Tazria Parashat Nega'im, Chapter 14 3", "Sifra, Tazria Parashat Nega'im, Chapter 14 4-6"])

# -------------------------- Lev.13.50 · ETNACHTA_SPLIT ---------------------
# ‹וראה הכהן את› (“and-see the-priest obj-marker”)
# ‹הנגע … והסגיר את› (“the-blow … and-shut-up obj-marker”)
# ‹הנגע שבעת ימים› (“the-blow seven day”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:50."
m.step("Lev.13.50")

# -------------------------- Lev.13.51 · ETNACHTA_SPLIT ---------------------
# ‹וראה את הנגע› (“and-see obj-marker the-blow”)
# ‹ביום השביעי כי› (“in-day the-seventh that”)
# ‹פשה הנגע בבגד› (“spread the-blow in-garment”)
# ‹או בשתי או› (“or in-fixture or”)
# ‹בערב או … צרעת› (“in-web or … leprosy”)
# ‹ממארת הנגע טמא› (“be-bitter the-blow foul-in-a-religious-sense”)
# ‹הוא› (“he/it”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:51."
m.step("Lev.13.51")
# witness-tier presupposed read: the_benefit_ban on tzaraat_mameret — read,
# not installed
m.witness_read("tzaraat_mameret", "the_benefit_ban",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 14 11", "Sifra, Tazria Parashat Nega'im, Chapter 14 9", "Sifra, Tazria Parashat Nega'im, Chapter 14 10", "Onkelos Lev 13:51", "Onkelos Lev 13:52"])

# -------------------------- Lev.13.52 · ETNACHTA_SPLIT ---------------------
# ‹ושרף את הבגד› (“and-be-on-fire obj-marker the-garment”)
# ‹או את השתי› (“or obj-marker the-fixture”)
# ‹או את הערב› (“or obj-marker the-web”)
# ‹בצמר או בפשתים› (“in-wool or in-linen”)
# ‹או את כל› (“or obj-marker all”)
# ‹כ … כי צרעת› (“? … that leprosy”)
# ‹ממארת הוא באש› (“be-bitter he/it in-fire”)
# ‹תשרף› (“be-on-fire”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:52."
m.step("Lev.13.52")

# -------------------------- Lev.13.53 · COND_ואם (“and-if”) ----------------
# ‹ואם יראה הכהן› (“and-if see the-priest”)
# ‹והנה לא פשה› (“and-behold not spread”)
# ‹הנגע בבגד או› (“the-blow in-garment or”)
# ‹בשתי או בערב› (“in-fixture or in-web”)
# ‹… או בכל כלי› (“or in-all vessel”)
# ‹עור› (“skin”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:53."
m.step("Lev.13.53")

# -------------------------- Lev.13.54 · ETNACHTA_SPLIT ---------------------
# ‹וצוה הכהן וכבסו› (“and-command the-priest and-trample”)
# ‹את אשר בו› (“obj-marker which in-him/its”)
# ‹הנגע … והסגירו שבעת› (“the-blow … and-shut-up-him/its seven”)
# ‹ימים שנית› (“day second”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:54."
m.step("Lev.13.54")

# -------------------------- Lev.13.55 · ETNACHTA_SPLIT ---------------------
# ‹וראה הכהן אחרי› (“and-see the-priest after”)
# ‹הכבס את הנגע› (“trample obj-marker the-blow”)
# ‹והנה לא הפך› (“and-behold not turn-about”)
# ‹הנגע את עינו› (“the-blow obj-marker eye-him/its”)
# ‹והנגע ל … פחתת› (“and-the-blow ? … hole”)
# ‹הוא בקרחתו או› (“he/it in-bald-spot-him/its or”)
# ‹בגבחתו› (“in-baldness-in-the-forehead-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:55."
m.step("Lev.13.55")
# witness-tier presupposed read: standing_burns on lo_hafach_velo_pasah —
# read, not installed
m.witness_read("lo_hafach_velo_pasah", "standing_burns",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 2* 8", "Sifra, Tazria Parashat Nega'im, Chapter 15 7", "Sifra, Tazria Parashat Nega'im, Chapter 15 9", "Sifra, Tazria Parashat Nega'im, Chapter 16 1", "Sifra, Tazria Parashat Nega'im, Chapter 16 4", "Sifra, Tazria Parashat Nega'im, Chapter 16 5", "Sifra, Tazria Parashat Nega'im, Chapter 16 9", "Onkelos Lev 13:55"])

# -------------------------- Lev.13.56 · COND_ואם (“and-if”) ----------------
# ‹ואם ראה הכהן› (“and-if see the-priest”)
# ‹והנה כהה הנגע› (“and-behold feeble the-blow”)
# ‹אחרי הכבס אתו› (“after trample obj-marker-him/its”)
# ‹… וקרע אתו מן› (“and-rend obj-marker-him/its from”)
# ‹הבגד או מן› (“the-garment or from”)
# ‹העור או מן› (“the-skin or from”)
# ‹השתי או מן› (“the-fixture or from”)
# ‹הערב› (“the-web”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:56."
m.step("Lev.13.56")

# -------------------------- Lev.13.57 · COND_ואם (“and-if”) ----------------
# ‹ואם תראה עוד› (“and-if see still/again”)
# ‹בבגד או בשתי› (“in-garment or in-fixture”)
# ‹או בערב או› (“or in-web or”)
# ‹בכל כלי עור› (“in-all vessel skin”)
# ‹פרחת הוא … באש› (“break-forth-as-a-bud he/it … in-fire”)
# ‹תשרפנו את אשר› (“be-on-fire-him/its obj-marker which”)
# ‹בו הנגע› (“in-him/its the-blow”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:57."
m.step("Lev.13.57")

# -------------------------- Lev.13.58 · ETNACHTA_SPLIT ---------------------
# ‹והבגד או השתי› (“and-the-garment or the-fixture”)
# ‹או הערב או› (“or the-web or”)
# ‹כל כלי העור› (“all vessel the-skin”)
# ‹אשר תכבס וסר› (“which trample and-turn-aside”)
# ‹מהם הנגע … וכבס› (“from-them/their the-blow … and-trample”)
# ‹שנית וטהר› (“second and-be-pure”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:58."
m.step("Lev.13.58")

# -------------------------- Lev.13.59 · ETNACHTA_SPLIT ---------------------
# ‹זאת תורת נגע› (“this precept blow”)
# ‹צרעת בגד הצמר› (“leprosy garment the-wool”)
# ‹או הפשתים או› (“or the-linen or”)
# ‹השתי או הערב› (“the-fixture or the-web”)
# ‹או כל כ› (“or all ?”)
# ‹… לטהרו או לטמאו› (“to-be-pure-him/its or to-be-foul-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:59."
m.step("Lev.13.59")
# witness-tier presupposed read: the_close on zot_torat — read, not
# installed
m.witness_read("zot_torat", "the_close",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 16 10", "Sifra, Tazria Parashat Nega'im, Chapter 16 11", "Sifra, Tazria Parashat Nega'im, Chapter 16 12", "Sifra, Tazria Parashat Nega'im, Chapter 16 13"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 0
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('beged_tzemer_o_fishtim', 'species_and_work_gate'), ('yerakrak_adamdam', 'intensest_shades'), ('tzaraat_mameret', 'the_benefit_ban'), ('lo_hafach_velo_pasah', 'standing_burns'), ('zot_torat', 'the_close')]
    assert m.WITNESS_READS[0]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 13 1", "Sifra, Tazria Parashat Nega'im, Chapter 13 2", "Sifra, Tazria Parashat Nega'im, Chapter 13 3", "Sifra, Tazria Parashat Nega'im, Chapter 13 7", "Sifra, Tazria Parashat Nega'im, Chapter 13 9", "Sifra, Tazria Parashat Nega'im, Chapter 13 12", "Sifra, Tazria Parashat Nega'im, Chapter 14 1"]
    assert all('species_and_work_gate' not in f for f in m.WORLD["facts"])
    assert 'beged_tzemer_o_fishtim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 14 2", "Sifra, Tazria Parashat Nega'im, Chapter 14 3", "Sifra, Tazria Parashat Nega'im, Chapter 14 4-6"]
    assert all('intensest_shades' not in f for f in m.WORLD["facts"])
    assert 'yerakrak_adamdam' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 14 11", "Sifra, Tazria Parashat Nega'im, Chapter 14 9", "Sifra, Tazria Parashat Nega'im, Chapter 14 10", 'Onkelos Lev 13:51', 'Onkelos Lev 13:52']
    assert all('the_benefit_ban' not in f for f in m.WORLD["facts"])
    assert 'tzaraat_mameret' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 2* 8", "Sifra, Tazria Parashat Nega'im, Chapter 15 7", "Sifra, Tazria Parashat Nega'im, Chapter 15 9", "Sifra, Tazria Parashat Nega'im, Chapter 16 1", "Sifra, Tazria Parashat Nega'im, Chapter 16 4", "Sifra, Tazria Parashat Nega'im, Chapter 16 5", "Sifra, Tazria Parashat Nega'im, Chapter 16 9", 'Onkelos Lev 13:55']
    assert all('standing_burns' not in f for f in m.WORLD["facts"])
    assert 'lo_hafach_velo_pasah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 16 10", "Sifra, Tazria Parashat Nega'im, Chapter 16 11", "Sifra, Tazria Parashat Nega'im, Chapter 16 12", "Sifra, Tazria Parashat Nega'im, Chapter 16 13"]
    assert all('the_close' not in f for f in m.WORLD["facts"])
    assert 'zot_torat' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
