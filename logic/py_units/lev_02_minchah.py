#!/usr/bin/env python3
# =============================================================================
# lev_02_minchah — 2:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_02_minchah.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Minchah grain offerings: flour, oven, pan, firstfruits (2:1–16)"""
from machine import Machine

m = Machine("lev_02_minchah")

# -------------------------- Lev.2.1 · COND_כי (“that”) ---------------------
# ‹ונפש כי תקריב› (“and-living-being that bring-near”)
# ‹קרבן מנחה ליהוה› (“offering grain-offering to-YHWH”)
# ‹סלת יהיה קרבנו› (“flour be offering-him/its”)
# ‹… ויצק עליה שמן› (“and-pour-out over-her/its oil”)
# ‹ונתן עליה לבנה› (“and-set over-her/its frankincense”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:1."
m.step("Lev.2.1")
# witness-tier presupposed read: menu_closed_at_incense on single_caller —
# read, not installed
m.witness_read("single_caller", "menu_closed_at_incense",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 8 2", "Sifra, Vayikra Dibbura DeNedavah, Section 8 3", "Sifra, Vayikra Dibbura DeNedavah, Section 8 5", "Sifra, Vayikra Dibbura DeNedavah, Section 8 7", "Sifra, Vayikra Dibbura DeNedavah, Section 8 8", "Sifra, Vayikra Dibbura DeNedavah, Section 8 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 8", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 12", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 13"])
# witness-tier presupposed read: placement_follows_sample on two_adjuncts —
# read, not installed
m.witness_read("two_adjuncts", "placement_follows_sample",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 10 14", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 16", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 17", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 18", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 19", "Sifra, Vayikra Dibbura DeNedavah, Section 9 2"])
# witness-tier presupposed read: answer_sheet_by_topic on minchah_vow_parser
# — read, not installed
m.witness_read("minchah_vow_parser", "answer_sheet_by_topic",
                cites=["Mishnah Menachot 12:3", "Mishnah Menachot 12:4", "Mishnah Menachot 12:5", "Mishnah Menachot 13:1", "Mishnah Menachot 13:2", "Mishnah Menachot 13:3", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 6", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 7", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 13", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 18"])

# -------------------------- Lev.2.2 · ETNACHTA_SPLIT -----------------------
# ‹והביאה אל בני› (“and-come/bring-her/its to son”)
# ‹אהרן הכהנים וקמץ› (“Aaron the-priest and-grasp-with-the-hand”)
# ‹משם מלא קמצו› (“from-there fulness grasp-him/its”)
# ‹מסלתה ומשמנה על› (“from-flour-her/its and-from-oil-her/its over”)
# ‹… והקטיר הכהן את› (“and-smoke the-priest obj-marker”)
# ‹אזכרתה המזבחה אשה› (“reminder-her/its the-altar-ward fire-offering”)
# ‹ריח ניחח ליהוה› (“odor restful to-YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:2."
m.step("Lev.2.2")
# witness-tier presupposed read: constant_scaling_level_measure on fistful —
# read, not installed
m.witness_read("fistful", "constant_scaling_level_measure",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 9 3", "Sifra, Vayikra Dibbura DeNedavah, Section 9 5", "Sifra, Vayikra Dibbura DeNedavah, Section 9 6", "Sifra, Vayikra Dibbura DeNedavah, Section 9 7", "Sifra, Vayikra Dibbura DeNedavah, Section 9 9", "Sifra, Vayikra Dibbura DeNedavah, Section 9 10"])
# witness-tier presupposed read: tenth_and_log_full on quantity_floors —
# read, not installed
m.witness_read("quantity_floors", "tenth_and_log_full",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 9 8", "Sifra, Vayikra Dibbura DeNedavah, Section 9 11", "Sifra, Vayikra Dibbura DeNedavah, Section 9 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 11 1"])

# -------------------------- Lev.2.3 · ETNACHTA_SPLIT -----------------------
# ‹והנותרת מן המנחה› (“and-the-jut-over from the-grain-offering”)
# ‹לאהרן ולבניו … קדש› (“to-Aaron and-to-son-him/its … holiness”)
# ‹קדשים מאשי יהוה› (“holiness from-fire-offering YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:3."
m.step("Lev.2.3")

# -------------------------- Lev.2.4 · COND_וכי (“and-that”) ----------------
# ‹וכי תקרב קרבן› (“and-that bring-near offering”)
# ‹מנחה מאפה תנור› (“grain-offering something-baked fire-pot”)
# ‹… סלת חלות מצת› (“flour cake sweetness”)
# ‹בלולת בשמן ורקיקי› (“overflow in-oil and-thin-cake”)
# ‹מצות משחים בשמן› (“sweetness rub-with-oil in-oil”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:4."
m.step("Lev.2.4")
# witness-tier presupposed read: normalize_or_void on vow_parser — read, not
# installed
m.witness_read("vow_parser", "normalize_or_void",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 10 6", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 7", "Sifra, Vayikra Dibbura DeNedavah, Section 10 1", "Sifra, Vayikra Dibbura DeNedavah, Section 10 2", "Sifra, Vayikra Dibbura DeNedavah, Section 10 3"])

# -------------------------- Lev.2.5 · COND_ואם (“and-if”) ------------------
# ‹ואם מנחה על› (“and-if grain-offering over”)
# ‹המחבת קרבנך … סלת› (“the-pan-for-baking-in offering-you/your … flour”)
# ‹בלולה בשמן מצה› (“overflow in-oil sweetness”)
# ‹תהיה› (“be”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:5."
m.step("Lev.2.5")

# -------------------------- Lev.2.6 · ETNACHTA_SPLIT -----------------------
# ‹פתות אתה פתים› (“open obj-marker-her/its bit”)
# ‹ויצקת עליה שמן› (“and-pour-out over-her/its oil”)
# ‹… מנחה הוא› (“grain-offering he/it”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:6."
m.step("Lev.2.6")
# witness-tier presupposed read: three_by_caller_class on folding_paths —
# read, not installed
m.witness_read("folding_paths", "three_by_caller_class",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 12 3", "Sifra, Vayikra Dibbura DeNedavah, Chapter 12 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 12 5", "Sifra, Vayikra Dibbura DeNedavah, Chapter 12 7"])

# -------------------------- Lev.2.7 · COND_ואם (“and-if”) ------------------
# ‹ואם מנחת מרחשת› (“and-if grain-offering stewpan”)
# ‹קרבנך … סלת בשמן› (“offering-you/your … flour in-oil”)
# ‹תעשה› (“make”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:7."
m.step("Lev.2.7")

# -------------------------- Lev.2.8 · ETNACHTA_SPLIT -----------------------
# ‹והבאת את המנחה› (“and-come/bring obj-marker the-grain-offering”)
# ‹אשר יעשה מאלה› (“which make from-these”)
# ‹ליהוה … והקריבה אל› (“to-YHWH … and-bring-near-her/its to”)
# ‹הכהן והגישה אל› (“the-priest and-be-her/its to”)
# ‹המזבח› (“the-altar”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:8."
m.step("Lev.2.8")

# -------------------------- Lev.2.9 · ETNACHTA_SPLIT -----------------------
# ‹והרים הכהן מן› (“and-rise-high the-priest from”)
# ‹המנחה את אזכרתה› (“the-grain-offering obj-marker reminder-her/its”)
# ‹והקטיר המזבחה … אשה› (“and-smoke the-altar-ward … fire-offering”)
# ‹ריח ניחח ליהוה› (“odor restful to-YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:9."
m.step("Lev.2.9")

# -------------------------- Lev.2.10 · ETNACHTA_SPLIT ----------------------
# ‹והנותרת מן המנחה› (“and-the-jut-over from the-grain-offering”)
# ‹לאהרן ולבניו … קדש› (“to-Aaron and-to-son-him/its … holiness”)
# ‹קדשים מאשי יהוה› (“holiness from-fire-offering YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:10."
m.step("Lev.2.10")

# -------------------------- Lev.2.11 · ETNACHTA_SPLIT ----------------------
# ‹כל המנחה אשר› (“all the-grain-offering which”)
# ‹תקריבו ליהוה לא› (“bring-near to-YHWH not”)
# ‹תעשה חמץ … כי› (“make ferment … that”)
# ‹כל שאר וכל› (“all barm and-all”)
# ‹דבש לא תקטירו› (“honey not smoke”)
# ‹ממנו אשה ליהוה› (“from-us/our fire-offering to-YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:11."
m.step("Lev.2.11")
# witness-tier presupposed read: per_step_liability on leaven_ban — read,
# not installed
m.witness_read("leaven_ban", "per_step_liability",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 12 1", "Sifra, Vayikra Dibbura DeNedavah, Section 12 3", "Sifra, Vayikra Dibbura DeNedavah, Section 12 4", "Sifra, Vayikra Dibbura DeNedavah, Section 12 5", "Sifra, Vayikra Dibbura DeNedavah, Section 12 6"])

# -------------------------- Lev.2.12 · ETNACHTA_SPLIT ----------------------
# ‹קרבן ראשית תקריבו› (“offering beginning bring-near”)
# ‹אתם ליהוה … ואל› (“obj-marker-them/their to-YHWH … and-to”)
# ‹המזבח לא יעלו› (“the-altar not go-up”)
# ‹לריח ניחח› (“to-odor restful”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:12."
m.step("Lev.2.12")

# -------------------------- Lev.2.13 · ETNACHTA_SPLIT ----------------------
# ‹וכל קרבן מנחתך› (“and-all offering grain-offering-you/your”)
# ‹במלח תמלח ולא› (“in-powder rub-to-pieces and-not”)
# ‹תשבית מלח ברית› (“cease powder covenant”)
# ‹אלהיך מעל מנחתך› (“God-you/your from-over grain-offering-you/your”)
# ‹… על כל קרבנך› (“over all offering-you/your”)
# ‹תקריב מלח› (“bring-near powder”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:13."
m.step("Lev.2.13")
# witness-tier presupposed read: overrides_schedulers on salt_covenant —
# read, not installed
m.witness_read("salt_covenant", "overrides_schedulers",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 14 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 14 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 14 7", "Onkelos Lev 2:13"])

# -------------------------- Lev.2.14 · COND_ואם (“and-if”) -----------------
# ‹ואם תקריב מנחת› (“and-if bring-near grain-offering”)
# ‹בכורים ליהוה … אביב› (“first-fruits-of-the-crop to-YHWH … green”)
# ‹קלוי באש גרש› (“toast in-fire kernel”)
# ‹כרמל תקריב את› (“planted-field bring-near obj-marker”)
# ‹מנחת בכוריך› (“grain-offering first-fruits-of-the-crop-you/your”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:14."
m.step("Lev.2.14")
# witness-tier presupposed read: barley_word_order_if_grading on omer —
# read, not installed
m.witness_read("omer", "barley_word_order_if_grading",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 13 4", "Sifra, Vayikra Dibbura DeNedavah, Section 13 7", "Sifra, Vayikra Dibbura DeNedavah, Section 13 3", "Sifra, Vayikra Dibbura DeNedavah, Section 13 2", "Sifra, Vayikra Dibbura DeNedavah, Section 13 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 2", "Onkelos Lev 2:14"])

# -------------------------- Lev.2.15 · ETNACHTA_SPLIT ----------------------
# ‹ונתת עליה שמן› (“and-set over-her/its oil”)
# ‹ושמת עליה לבנה› (“and-put/set over-her/its frankincense”)
# ‹… מנחה הוא› (“grain-offering he/it”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:15."
m.step("Lev.2.15")
# witness-tier presupposed read: closed_member_by_member on adjunct_matrix —
# read, not installed
m.witness_read("adjunct_matrix", "closed_member_by_member",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 15 3", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 5", "Sifra, Vayikra Dibbura DeNedavah, Section 12 7", "Sifra, Vayikra Dibbura DeNedavah, Section 12 9"])

# -------------------------- Lev.2.16 · ETNACHTA_SPLIT ----------------------
# ‹והקטיר הכהן את› (“and-smoke the-priest obj-marker”)
# ‹אזכרתה מגרשה ומשמנה› (“reminder-her/its from-kernel-her/its and-from-oil-
# her/its”)
# ‹על כל לבנתה› (“over all frankincense-her/its”)
# ‹… אשה ליהוה› (“fire-offering to-YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 2:16."
m.step("Lev.2.16")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('single_caller', 'menu_closed_at_incense'), ('two_adjuncts', 'placement_follows_sample'), ('minchah_vow_parser', 'answer_sheet_by_topic'), ('fistful', 'constant_scaling_level_measure'), ('quantity_floors', 'tenth_and_log_full'), ('vow_parser', 'normalize_or_void'), ('folding_paths', 'three_by_caller_class'), ('leaven_ban', 'per_step_liability'), ('salt_covenant', 'overrides_schedulers'), ('omer', 'barley_word_order_if_grading'), ('adjunct_matrix', 'closed_member_by_member')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 8 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 8', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 8', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 12', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 13']
    assert all('menu_closed_at_incense' not in f for f in m.WORLD["facts"])
    assert 'single_caller' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 10 14', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 16', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 17', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 18', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 19', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 2']
    assert all('placement_follows_sample' not in f for f in m.WORLD["facts"])
    assert 'two_adjuncts' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Mishnah Menachot 12:3', 'Mishnah Menachot 12:4', 'Mishnah Menachot 12:5', 'Mishnah Menachot 13:1', 'Mishnah Menachot 13:2', 'Mishnah Menachot 13:3', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 6', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 7', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 13', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 18']
    assert all('answer_sheet_by_topic' not in f for f in m.WORLD["facts"])
    assert 'minchah_vow_parser' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 9 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 6', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 9', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 10']
    assert all('constant_scaling_level_measure' not in f for f in m.WORLD["facts"])
    assert 'fistful' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 9 8', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 11', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 11 1']
    assert all('tenth_and_log_full' not in f for f in m.WORLD["facts"])
    assert 'quantity_floors' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 10 6', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 10 1', 'Sifra, Vayikra Dibbura DeNedavah, Section 10 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 10 3']
    assert all('normalize_or_void' not in f for f in m.WORLD["facts"])
    assert 'vow_parser' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 12 3', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 12 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 12 5', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 12 7']
    assert all('three_by_caller_class' not in f for f in m.WORLD["facts"])
    assert 'folding_paths' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 12 1', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 4', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 6']
    assert all('per_step_liability' not in f for f in m.WORLD["facts"])
    assert 'leaven_ban' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 14 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 14 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 14 7', 'Onkelos Lev 2:13']
    assert all('overrides_schedulers' not in f for f in m.WORLD["facts"])
    assert 'salt_covenant' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 13 4', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 2', 'Onkelos Lev 2:14']
    assert all('barley_word_order_if_grading' not in f for f in m.WORLD["facts"])
    assert 'omer' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 15 3', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 9']
    assert all('closed_member_by_member' not in f for f in m.WORLD["facts"])
    assert 'adjunct_matrix' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
