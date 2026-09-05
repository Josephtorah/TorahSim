#!/usr/bin/env python3
# =============================================================================
# lev_13_skin_initial — 13:1-17
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_13_skin_initial.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Skin disease initial cases: rising, scab, bright spot (13:1–17)"""
from machine import Machine

m = Machine("lev_13_skin_initial")

# -------------------------- Lev.13.1 · TREE_CLAIM --------------------------
# וידבר יהוה … אל משה ואל אהרן לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה ואל אהרן
# לאמר». Derive claim from Hebrew arms. Lev 13:1."
m.step("Lev.13.1")

# -------------------------- Lev.13.2 · COND_כי -----------------------------
# אדם כי יהיה בעור בשרו שאת או ספחת או בהרת והיה בעור בשרו לנג … והובא אל
# אהרן הכהן או אל אחד מבניו הכהנים
# "[EN-AID] From top split: LEFT «אדם כי יהיה בעור בשרו שאת או ספחת או בהרת
# והיה בעור בשרו לנגע צרעת» / RIGHT «והובא אל אהרן הכהן או אל אחד מבניו
# הכהנים». Derive claim from Hebrew arms. Lev 13:2."
m.step("Lev.13.2")

# -------------------------- Lev.13.3 · ETNACHTA_SPLIT ----------------------
# וראה הכהן את הנגע בעור הבשר ושער בנגע הפך לבן ומראה הנגע עמק … וראהו הכהן
# וטמא אתו
# "[EN-AID] From top split: LEFT «וראה הכהן את הנגע בעור הבשר ושער בנגע הפך
# לבן ומראה הנגע עמק מעור בשרו נגע צרעת » / RIGHT «וראהו הכהן וטמא אתו».
# Derive claim from Hebrew arms. Lev 13:3."
m.step("Lev.13.3")

# -------------------------- Lev.13.4 · COND_ואם ----------------------------
# ואם בהרת לבנה הוא בעור בשרו ועמק אין מראה מן העור ושערה לא ה … והסגיר הכהן
# את הנגע שבעת ימים
# "[EN-AID] From top split: LEFT «ואם בהרת לבנה הוא בעור בשרו ועמק אין מראה
# מן העור ושערה לא הפך לבן» / RIGHT «והסגיר הכהן את הנגע שבעת ימים». Derive
# claim from Hebrew arms. Lev 13:4."
m.step("Lev.13.4")

# -------------------------- Lev.13.5 · ETNACHTA_SPLIT ----------------------
# וראהו הכהן ביום השביעי והנה הנגע עמד בעיניו לא פשה הנגע בעור … והסגירו
# הכהן שבעת ימים שנית
# "[EN-AID] From top split: LEFT «וראהו הכהן ביום השביעי והנה הנגע עמד
# בעיניו לא פשה הנגע בעור» / RIGHT «והסגירו הכהן שבעת ימים שנית». Derive
# claim from Hebrew arms. Lev 13:5."
m.step("Lev.13.5")

# -------------------------- Lev.13.6 · ETNACHTA_SPLIT ----------------------
# וראה הכהן אתו ביום השביעי שנית והנה כהה הנגע ולא פשה הנגע בע … וטהרו הכהן
# מספחת היא וכבס בגדיו וטהר
# "[EN-AID] From top split: LEFT «וראה הכהן אתו ביום השביעי שנית והנה כהה
# הנגע ולא פשה הנגע בעור» / RIGHT «וטהרו הכהן מספחת היא וכבס בגדיו וטהר».
# Derive claim from Hebrew arms. Lev 13:6."
m.step("Lev.13.6")

# -------------------------- Lev.13.7 · COND_ואם ----------------------------
# ואם פשה תפשה המספחת בעור אחרי הראתו אל הכהן לטהרתו … ונראה שנית אל הכהן
# "[EN-AID] From top split: LEFT «ואם פשה תפשה המספחת בעור אחרי הראתו אל
# הכהן לטהרתו» / RIGHT «ונראה שנית אל הכהן». Derive claim from Hebrew arms.
# Lev 13:7."
m.step("Lev.13.7")

# -------------------------- Lev.13.8 · ETNACHTA_SPLIT ----------------------
# וראה הכהן והנה פשתה המספחת בעור … וטמאו הכהן צרעת הוא
# "[EN-AID] From top split: LEFT «וראה הכהן והנה פשתה המספחת בעור» / RIGHT
# «וטמאו הכהן צרעת הוא». Derive claim from Hebrew arms. Lev 13:8."
m.step("Lev.13.8")

# -------------------------- Lev.13.9 · COND_כי -----------------------------
# נגע צרעת כי תהיה באדם … והובא אל הכהן
# "[EN-AID] From top split: LEFT «נגע צרעת כי תהיה באדם» / RIGHT «והובא אל
# הכהן». Derive claim from Hebrew arms. Lev 13:9."
m.step("Lev.13.9")

# -------------------------- Lev.13.10 · ETNACHTA_SPLIT ---------------------
# וראה הכהן והנה שאת לבנה בעור והיא הפכה שער לבן … ומחית בשר חי בשאת
# "[EN-AID] From top split: LEFT «וראה הכהן והנה שאת לבנה בעור והיא הפכה שער
# לבן» / RIGHT «ומחית בשר חי בשאת». Derive claim from Hebrew arms. Lev
# 13:10."
m.step("Lev.13.10")
# witness-tier presupposed read: the_geometry_row on michyat_basar_chai —
# read, not installed
m.witness_read("michyat_basar_chai", "the_geometry_row",
                cites=["Sifra, Tazria Parashat Nega'im, Section 3 4", "Sifra, Tazria Parashat Nega'im, Section 3 8", "Sifra, Tazria Parashat Nega'im, Section 3 10", "Sifra, Tazria Parashat Nega'im, Section 3 11", "Sifra, Tazria Parashat Nega'im, Chapter 3 1", "Sifra, Tazria Parashat Nega'im, Chapter 3 2"])

# -------------------------- Lev.13.11 · ETNACHTA_SPLIT ---------------------
# צרעת נושנת הוא בעור בשרו וטמאו הכהן … לא יסגרנו כי טמא הוא
# "[EN-AID] From top split: LEFT «צרעת נושנת הוא בעור בשרו וטמאו הכהן» /
# RIGHT «לא יסגרנו כי טמא הוא». Derive claim from Hebrew arms. Lev 13:11."
m.step("Lev.13.11")
# witness-tier presupposed read: the_state_guard on lo_yasgirenu — read, not
# installed
m.witness_read("lo_yasgirenu", "the_state_guard",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 2 6", "Sifra, Tazria Parashat Nega'im, Chapter 2 7", "Sifra, Tazria Parashat Nega'im, Chapter 2 8", "Sifra, Tazria Parashat Nega'im, Chapter 3 3"])

# -------------------------- Lev.13.12 · COND_ואם ---------------------------
# ואם פרוח תפרח הצרעת בעור וכסתה הצרעת את כל עור הנגע מראשו וע … לכל מראה
# עיני הכהן
# "[EN-AID] From top split: LEFT «ואם פרוח תפרח הצרעת בעור וכסתה הצרעת את כל
# עור הנגע מראשו ועד רגליו» / RIGHT «לכל מראה עיני הכהן». Derive claim from
# Hebrew arms. Lev 13:12."
m.step("Lev.13.12")
# witness-tier presupposed read: the_posture_protocol on
# lechol_mareh_einei_hakohen — read, not installed
m.witness_read("lechol_mareh_einei_hakohen", "the_posture_protocol",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 4 2", "Sifra, Tazria Parashat Nega'im, Chapter 4 3", "Sifra, Tazria Parashat Nega'im, Chapter 4 4", "Sifra, Tazria Parashat Nega'im, Chapter 4 5"])

# -------------------------- Lev.13.13 · ETNACHTA_SPLIT ---------------------
# וראה הכהן והנה כסתה הצרעת את כל בשרו וטהר את הנגע … כלו הפך לבן טהור הוא
# "[EN-AID] From top split: LEFT «וראה הכהן והנה כסתה הצרעת את כל בשרו וטהר
# את הנגע» / RIGHT «כלו הפך לבן טהור הוא». Derive claim from Hebrew arms.
# Lev 13:13."
m.step("Lev.13.13")
# witness-tier presupposed read: bloom_purifies on kulo_hafach_lavan — read,
# not installed
m.witness_read("kulo_hafach_lavan", "bloom_purifies",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 3 5", "Sifra, Tazria Parashat Nega'im, Chapter 3 6", "Sifra, Tazria Parashat Nega'im, Chapter 3 7", "Sifra, Tazria Parashat Nega'im, Chapter 4 1", "Sifra, Tazria Parashat Nega'im, Chapter 4 6", "Sifra, Tazria Parashat Nega'im, Chapter 4 7", "Sifra, Tazria Parashat Nega'im, Chapter 6 4"])

# -------------------------- Lev.13.14 · TREE_CLAIM -------------------------
# וביום הראות בו בשר חי
# "[EN-AID] From top split: LEFT «וביום הראות בו בשר חי» / RIGHT «». Derive
# claim from Hebrew arms. Lev 13:14."
m.step("Lev.13.14")
# witness-tier presupposed read: kings_decree_and_grace_days on uvyom_heraot
# — read, not installed
m.witness_read("uvyom_heraot", "kings_decree_and_grace_days",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 5 1", "Sifra, Tazria Parashat Nega'im, Chapter 5 2", "Sifra, Tazria Parashat Nega'im, Chapter 2 9"])

# -------------------------- Lev.13.15 · ETNACHTA_SPLIT ---------------------
# וראה הכהן את הבשר החי וטמאו … הבשר החי טמא הוא צרעת הוא
# "[EN-AID] From top split: LEFT «וראה הכהן את הבשר החי וטמאו» / RIGHT «הבשר
# החי טמא הוא צרעת הוא». Derive claim from Hebrew arms. Lev 13:15."
m.step("Lev.13.15")

# -------------------------- Lev.13.16 · COND_כי ----------------------------
# או כי ישוב הבשר החי ונהפך ללבן … ובא אל הכהן
# "[EN-AID] From top split: LEFT «או כי ישוב הבשר החי ונהפך ללבן» / RIGHT
# «ובא אל הכהן». Derive claim from Hebrew arms. Lev 13:16."
m.step("Lev.13.16")
# witness-tier presupposed read: the_loop_rule on ki_yashuv — read, not
# installed
m.witness_read("ki_yashuv", "the_loop_rule",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 6 1", "Sifra, Tazria Parashat Nega'im, Chapter 6 2", "Sifra, Tazria Parashat Nega'im, Chapter 5 4", "Sifra, Tazria Parashat Nega'im, Chapter 5 5"])

# -------------------------- Lev.13.17 · ETNACHTA_SPLIT ---------------------
# וראהו הכהן והנה נהפך הנגע ללבן … וטהר הכהן את הנגע טהור הוא
# "[EN-AID] From top split: LEFT «וראהו הכהן והנה נהפך הנגע ללבן» / RIGHT
# «וטהר הכהן את הנגע טהור הוא». Derive claim from Hebrew arms. Lev 13:17."
m.step("Lev.13.17")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('michyat_basar_chai', 'the_geometry_row'), ('lo_yasgirenu', 'the_state_guard'), ('lechol_mareh_einei_hakohen', 'the_posture_protocol'), ('kulo_hafach_lavan', 'bloom_purifies'), ('uvyom_heraot', 'kings_decree_and_grace_days'), ('ki_yashuv', 'the_loop_rule')]
    assert m.WITNESS_READS[0]["cites"] == ["Sifra, Tazria Parashat Nega'im, Section 3 4", "Sifra, Tazria Parashat Nega'im, Section 3 8", "Sifra, Tazria Parashat Nega'im, Section 3 10", "Sifra, Tazria Parashat Nega'im, Section 3 11", "Sifra, Tazria Parashat Nega'im, Chapter 3 1", "Sifra, Tazria Parashat Nega'im, Chapter 3 2"]
    assert all('the_geometry_row' not in f for f in m.WORLD["facts"])
    assert 'michyat_basar_chai' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 2 6", "Sifra, Tazria Parashat Nega'im, Chapter 2 7", "Sifra, Tazria Parashat Nega'im, Chapter 2 8", "Sifra, Tazria Parashat Nega'im, Chapter 3 3"]
    assert all('the_state_guard' not in f for f in m.WORLD["facts"])
    assert 'lo_yasgirenu' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 4 2", "Sifra, Tazria Parashat Nega'im, Chapter 4 3", "Sifra, Tazria Parashat Nega'im, Chapter 4 4", "Sifra, Tazria Parashat Nega'im, Chapter 4 5"]
    assert all('the_posture_protocol' not in f for f in m.WORLD["facts"])
    assert 'lechol_mareh_einei_hakohen' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 3 5", "Sifra, Tazria Parashat Nega'im, Chapter 3 6", "Sifra, Tazria Parashat Nega'im, Chapter 3 7", "Sifra, Tazria Parashat Nega'im, Chapter 4 1", "Sifra, Tazria Parashat Nega'im, Chapter 4 6", "Sifra, Tazria Parashat Nega'im, Chapter 4 7", "Sifra, Tazria Parashat Nega'im, Chapter 6 4"]
    assert all('bloom_purifies' not in f for f in m.WORLD["facts"])
    assert 'kulo_hafach_lavan' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 5 1", "Sifra, Tazria Parashat Nega'im, Chapter 5 2", "Sifra, Tazria Parashat Nega'im, Chapter 2 9"]
    assert all('kings_decree_and_grace_days' not in f for f in m.WORLD["facts"])
    assert 'uvyom_heraot' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 6 1", "Sifra, Tazria Parashat Nega'im, Chapter 6 2", "Sifra, Tazria Parashat Nega'im, Chapter 5 4", "Sifra, Tazria Parashat Nega'im, Chapter 5 5"]
    assert all('the_loop_rule' not in f for f in m.WORLD["facts"])
    assert 'ki_yashuv' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
