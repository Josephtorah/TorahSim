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

# -------------------------- Lev.13.18 · COND_כי (“that”) -------------------
# ‹ובשר כי יהיה› (“and-flesh that be”)
# ‹בו בערו שחין› (“in-him/its in-skin-him/its inflammation”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «». Derive claim from Hebrew
# arms. Lev 13:18."
m.step("Lev.13.18")
# witness-tier presupposed read: the_heat_source_classifier on shechin —
# read, not installed
m.witness_read("shechin", "the_heat_source_classifier",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 6 6", "Sifra, Tazria Parashat Nega'im, Chapter 7 4"])

# -------------------------- Lev.13.19 · ETNACHTA_SPLIT ---------------------
# ‹והיה במקום השחין› (“and-be in-place the-inflammation”)
# ‹שאת לבנה או› (“Most-High white or”)
# ‹בהרת לבנה אדמדמת› (“whitish-spot-on-the-skin white reddish”)
# ‹… ונראה אל הכהן› (“and-see to the-priest”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:19."
m.step("Lev.13.19")
# witness-tier presupposed read: crust_and_precedence on bimkom_hashechin —
# read, not installed
m.witness_read("bimkom_hashechin", "crust_and_precedence",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 6 5", "Sifra, Tazria Parashat Nega'im, Chapter 6 7", "Sifra, Tazria Parashat Nega'im, Section 4 1", "Sifra, Tazria Parashat Nega'im, Section 4 2", "Sifra, Tazria Parashat Nega'im, Chapter 7 3"])

# -------------------------- Lev.13.20 · ETNACHTA_SPLIT ---------------------
# ‹וראה הכהן והנה› (“and-see the-priest and-behold”)
# ‹מראה שפל מן› (“appearance-her/its afflicted from”)
# ‹העור ושערה הפך› (“the-skin and-hair-her/its turn-about”)
# ‹לבן … וטמאו הכהן› (“white … and-be-foul-him/its the-priest”)
# ‹נגע צרעת הוא› (“blow leprosy he/it”)
# ‹בשחין פרחה› (“in-inflammation break-forth-as-a-bud”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:20."
m.step("Lev.13.20")

# -------------------------- Lev.13.21 · COND_ואם (“and-if”) ----------------
# ‹ואם יראנה הכהן› (“and-if see-her/its the-priest”)
# ‹והנה אין בה› (“and-behold there-is-not in-her/its”)
# ‹שער לבן ושפלה› (“hair white and-afflicted”)
# ‹איננה מן העור› (“there-is-not-her/its from the-skin”)
# ‹והיא … והסגירו הכהן› (“and-he/it … and-shut-up-him/its the-priest”)
# ‹שבעת ימים› (“seven day”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:21."
m.step("Lev.13.21")

# -------------------------- Lev.13.22 · COND_ואם (“and-if”) ----------------
# ‹ואם פשה תפשה› (“and-if spread spread”)
# ‹בעור … וטמא הכהן› (“in-skin … and-be-foul the-priest”)
# ‹אתו נגע הוא› (“obj-marker-him/its blow he/it”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:22."
m.step("Lev.13.22")
# witness-tier presupposed read: the_doubt_polarity on vetime_oto — read,
# not installed
m.witness_read("vetime_oto", "the_doubt_polarity",
                cites=["Sifra, Tazria Parashat Nega'im, Section 4 8", "Sifra, Tazria Parashat Nega'im, Section 4 9", "Sifra, Tazria Parashat Nega'im, Section 4 6", "Sifra, Tazria Parashat Nega'im, Section 4 7"])

# -------------------------- Lev.13.23 · COND_ואם (“and-if”) ----------------
# ‹ואם תחתיה תעמד› (“and-if under-her/its stand”)
# ‹הבהרת לא פשתה› (“the-whitish-spot-on-the-skin not spread”)
# ‹צרבת השחין הוא› (“conflagration the-inflammation he/it”)
# ‹… וטהרו הכהן› (“and-be-pure-him/its the-priest”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:23."
m.step("Lev.13.23")
# witness-tier presupposed read: region_scoped_spread on tachteha_taamod —
# read, not installed
m.witness_read("tachteha_taamod", "region_scoped_spread",
                cites=["Sifra, Tazria Parashat Nega'im, Section 4 4", "Sifra, Tazria Parashat Nega'im, Section 4 5", "Sifra, Tazria Parashat Nega'im, Chapter 7 1", "Sifra, Tazria Parashat Nega'im, Chapter 7 2"])

# -------------------------- Lev.13.24 · COND_כי (“that”) -------------------
# ‹או בשר כי› (“or flesh that”)
# ‹יהיה בערו מכות› (“be in-skin-him/its burn”)
# ‹אש … והיתה מחית› (“fire … and-be preservation-of-life”)
# ‹המכוה בהרת לבנה› (“the-burn whitish-spot-on-the-skin white”)
# ‹אדמדמת או לבנה› (“reddish or white”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:24."
m.step("Lev.13.24")

# -------------------------- Lev.13.25 · ETNACHTA_SPLIT ---------------------
# ‹וראה אתה הכהן› (“and-see obj-marker-her/its the-priest”)
# ‹והנה נהפך שער› (“and-behold turn-about hair”)
# ‹לבן בבהרת ומראה› (“white in-whitish-spot-on-the-skin and-appearance-
# her/its”)
# ‹עמק מן העור› (“deep from the-skin”)
# ‹צרעת … וטמא אתו› (“leprosy … and-be-foul obj-marker-him/its”)
# ‹הכהן נגע צרעת› (“the-priest blow leprosy”)
# ‹הוא› (“he/it”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:25."
m.step("Lev.13.25")

# -------------------------- Lev.13.26 · COND_ואם (“and-if”) ----------------
# ‹ואם יראנה הכהן› (“and-if see-her/its the-priest”)
# ‹והנה אין בבהרת› (“and-behold there-is-not in-whitish-spot-on-the-skin”)
# ‹שער לבן ושפלה› (“hair white and-afflicted”)
# ‹איננה מן העור› (“there-is-not-her/its from the-skin”)
# ‹וה … והסגירו הכהן› (“? … and-shut-up-him/its the-priest”)
# ‹שבעת ימים› (“seven day”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:26."
m.step("Lev.13.26")

# -------------------------- Lev.13.27 · ETNACHTA_SPLIT ---------------------
# ‹וראהו הכהן ביום› (“and-see-him/its the-priest in-day”)
# ‹השביעי … אם פשה› (“the-seventh … if spread”)
# ‹תפשה בעור וטמא› (“spread in-skin and-be-foul”)
# ‹הכהן אתו נגע› (“the-priest obj-marker-him/its blow”)
# ‹צרעת הוא› (“leprosy he/it”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:27."
m.step("Lev.13.27")

# -------------------------- Lev.13.28 · COND_ואם (“and-if”) ----------------
# ‹ואם תחתיה תעמד› (“and-if under-her/its stand”)
# ‹הבהרת לא פשתה› (“the-whitish-spot-on-the-skin not spread”)
# ‹בעור והוא כהה› (“in-skin and-he/it feeble”)
# ‹שאת המכוה הוא› (“Most-High the-burn he/it”)
# ‹… וטהרו הכהן כי› (“and-be-pure-him/its the-priest that”)
# ‹צרבת המכוה הוא› (“conflagration the-burn he/it”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 13:28."
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
