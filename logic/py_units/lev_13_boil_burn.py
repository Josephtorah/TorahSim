#!/usr/bin/env python3
# =============================================================================
# lev_13_boil_burn — 13:18-28
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_13_boil_burn.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Skin disease after boil or burn (13:18–28)"""
from machine import Machine

m = Machine("lev_13_boil_burn")

# -------------------------- Lev.13.18 · COND_כי ----------------------------
# ובשר כי יהיה בו בערו שחין
# "[EN-AID] From top split: LEFT «ובשר כי יהיה בו בערו שחין» / RIGHT «».
# Derive claim from Hebrew arms. Lev 13:18."
m.step("Lev.13.18")
# witness-tier presupposed read: the_heat_source_classifier on shechin —
# read, not installed
m.witness_read("shechin", "the_heat_source_classifier",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 6 6", "Sifra, Tazria Parashat Nega'im, Chapter 7 4"])

# -------------------------- Lev.13.19 · ETNACHTA_SPLIT ---------------------
# והיה במקום השחין שאת לבנה או בהרת לבנה אדמדמת … ונראה אל הכהן
# "[EN-AID] From top split: LEFT «והיה במקום השחין שאת לבנה או בהרת לבנה
# אדמדמת» / RIGHT «ונראה אל הכהן». Derive claim from Hebrew arms. Lev
# 13:19."
m.step("Lev.13.19")
# witness-tier presupposed read: crust_and_precedence on bimkom_hashechin —
# read, not installed
m.witness_read("bimkom_hashechin", "crust_and_precedence",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 6 5", "Sifra, Tazria Parashat Nega'im, Chapter 6 7", "Sifra, Tazria Parashat Nega'im, Section 4 1", "Sifra, Tazria Parashat Nega'im, Section 4 2", "Sifra, Tazria Parashat Nega'im, Chapter 7 3"])

# -------------------------- Lev.13.20 · ETNACHTA_SPLIT ---------------------
# וראה הכהן והנה מראה שפל מן העור ושערה הפך לבן … וטמאו הכהן נגע צרעת הוא
# בשחין פרחה
# "[EN-AID] From top split: LEFT «וראה הכהן והנה מראה שפל מן העור ושערה הפך
# לבן» / RIGHT «וטמאו הכהן נגע צרעת הוא בשחין פרחה». Derive claim from
# Hebrew arms. Lev 13:20."
m.step("Lev.13.20")

# -------------------------- Lev.13.21 · COND_ואם ---------------------------
# ואם יראנה הכהן והנה אין בה שער לבן ושפלה איננה מן העור והיא  … והסגירו
# הכהן שבעת ימים
# "[EN-AID] From top split: LEFT «ואם יראנה הכהן והנה אין בה שער לבן ושפלה
# איננה מן העור והיא כהה» / RIGHT «והסגירו הכהן שבעת ימים». Derive claim
# from Hebrew arms. Lev 13:21."
m.step("Lev.13.21")

# -------------------------- Lev.13.22 · COND_ואם ---------------------------
# ואם פשה תפשה בעור … וטמא הכהן אתו נגע הוא
# "[EN-AID] From top split: LEFT «ואם פשה תפשה בעור» / RIGHT «וטמא הכהן אתו
# נגע הוא». Derive claim from Hebrew arms. Lev 13:22."
m.step("Lev.13.22")
# witness-tier presupposed read: the_doubt_polarity on vetime_oto — read,
# not installed
m.witness_read("vetime_oto", "the_doubt_polarity",
                cites=["Sifra, Tazria Parashat Nega'im, Section 4 8", "Sifra, Tazria Parashat Nega'im, Section 4 9", "Sifra, Tazria Parashat Nega'im, Section 4 6", "Sifra, Tazria Parashat Nega'im, Section 4 7"])

# -------------------------- Lev.13.23 · COND_ואם ---------------------------
# ואם תחתיה תעמד הבהרת לא פשתה צרבת השחין הוא … וטהרו הכהן
# "[EN-AID] From top split: LEFT «ואם תחתיה תעמד הבהרת לא פשתה צרבת השחין
# הוא» / RIGHT «וטהרו הכהן». Derive claim from Hebrew arms. Lev 13:23."
m.step("Lev.13.23")
# witness-tier presupposed read: region_scoped_spread on tachteha_taamod —
# read, not installed
m.witness_read("tachteha_taamod", "region_scoped_spread",
                cites=["Sifra, Tazria Parashat Nega'im, Section 4 4", "Sifra, Tazria Parashat Nega'im, Section 4 5", "Sifra, Tazria Parashat Nega'im, Chapter 7 1", "Sifra, Tazria Parashat Nega'im, Chapter 7 2"])

# -------------------------- Lev.13.24 · COND_כי ----------------------------
# או בשר כי יהיה בערו מכות אש … והיתה מחית המכוה בהרת לבנה אדמדמת או לבנה
# "[EN-AID] From top split: LEFT «או בשר כי יהיה בערו מכות אש» / RIGHT
# «והיתה מחית המכוה בהרת לבנה אדמדמת או לבנה». Derive claim from Hebrew
# arms. Lev 13:24."
m.step("Lev.13.24")

# -------------------------- Lev.13.25 · ETNACHTA_SPLIT ---------------------
# וראה אתה הכהן והנה נהפך שער לבן בבהרת ומראה עמק מן העור צרעת … וטמא אתו
# הכהן נגע צרעת הוא
# "[EN-AID] From top split: LEFT «וראה אתה הכהן והנה נהפך שער לבן בבהרת
# ומראה עמק מן העור צרעת הוא במכוה פרחה» / RIGHT «וטמא אתו הכהן נגע צרעת
# הוא». Derive claim from Hebrew arms. Lev 13:25."
m.step("Lev.13.25")

# -------------------------- Lev.13.26 · COND_ואם ---------------------------
# ואם יראנה הכהן והנה אין בבהרת שער לבן ושפלה איננה מן העור וה … והסגירו
# הכהן שבעת ימים
# "[EN-AID] From top split: LEFT «ואם יראנה הכהן והנה אין בבהרת שער לבן
# ושפלה איננה מן העור והוא כהה» / RIGHT «והסגירו הכהן שבעת ימים». Derive
# claim from Hebrew arms. Lev 13:26."
m.step("Lev.13.26")

# -------------------------- Lev.13.27 · ETNACHTA_SPLIT ---------------------
# וראהו הכהן ביום השביעי … אם פשה תפשה בעור וטמא הכהן אתו נגע צרעת הוא
# "[EN-AID] From top split: LEFT «וראהו הכהן ביום השביעי» / RIGHT «אם פשה
# תפשה בעור וטמא הכהן אתו נגע צרעת הוא». Derive claim from Hebrew arms. Lev
# 13:27."
m.step("Lev.13.27")

# -------------------------- Lev.13.28 · COND_ואם ---------------------------
# ואם תחתיה תעמד הבהרת לא פשתה בעור והוא כהה שאת המכוה הוא … וטהרו הכהן כי
# צרבת המכוה הוא
# "[EN-AID] From top split: LEFT «ואם תחתיה תעמד הבהרת לא פשתה בעור והוא כהה
# שאת המכוה הוא» / RIGHT «וטהרו הכהן כי צרבת המכוה הוא». Derive claim from
# Hebrew arms. Lev 13:28."
m.step("Lev.13.28")
# witness-tier presupposed read: the_token_accounting on hi_hi_hi — read,
# not installed
m.witness_read("hi_hi_hi", "the_token_accounting",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 7 9"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('shechin', 'the_heat_source_classifier'), ('bimkom_hashechin', 'crust_and_precedence'), ('vetime_oto', 'the_doubt_polarity'), ('tachteha_taamod', 'region_scoped_spread'), ('hi_hi_hi', 'the_token_accounting')]
    assert m.WITNESS_READS[0]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 6 6", "Sifra, Tazria Parashat Nega'im, Chapter 7 4"]
    assert all('the_heat_source_classifier' not in f for f in m.WORLD["facts"])
    assert 'shechin' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 6 5", "Sifra, Tazria Parashat Nega'im, Chapter 6 7", "Sifra, Tazria Parashat Nega'im, Section 4 1", "Sifra, Tazria Parashat Nega'im, Section 4 2", "Sifra, Tazria Parashat Nega'im, Chapter 7 3"]
    assert all('crust_and_precedence' not in f for f in m.WORLD["facts"])
    assert 'bimkom_hashechin' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ["Sifra, Tazria Parashat Nega'im, Section 4 8", "Sifra, Tazria Parashat Nega'im, Section 4 9", "Sifra, Tazria Parashat Nega'im, Section 4 6", "Sifra, Tazria Parashat Nega'im, Section 4 7"]
    assert all('the_doubt_polarity' not in f for f in m.WORLD["facts"])
    assert 'vetime_oto' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ["Sifra, Tazria Parashat Nega'im, Section 4 4", "Sifra, Tazria Parashat Nega'im, Section 4 5", "Sifra, Tazria Parashat Nega'im, Chapter 7 1", "Sifra, Tazria Parashat Nega'im, Chapter 7 2"]
    assert all('region_scoped_spread' not in f for f in m.WORLD["facts"])
    assert 'tachteha_taamod' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 7 9"]
    assert all('the_token_accounting' not in f for f in m.WORLD["facts"])
    assert 'hi_hi_hi' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
