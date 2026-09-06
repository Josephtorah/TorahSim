#!/usr/bin/env python3
# =============================================================================
# lev_17_blood_center — 17:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_17_blood_center.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Slaughter at Tent; blood is life; no eating blood/neveilah (17:1–16)"""
from machine import Machine

m = Machine("lev_17_blood_center")

# -------------------------- Lev.17.1 · TREE_CLAIM --------------------------
# ‹וידבר יהוה … אל› (“and-speak YHWH … to”)
# ‹משה לאמר› (“Moses to-say”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:1."
m.step("Lev.17.1")

# -------------------------- Lev.17.2 · ETNACHTA_SPLIT ----------------------
# ‹דבר אל אהרן› (“speak to Aaron”)
# ‹ואל בניו ואל› (“and-to son-him/its and-to”)
# ‹כל בני ישראל› (“all son Israel”)
# ‹ואמרת אליהם … זה› (“and-say to-them/their … this”)
# ‹הדבר אשר צוה› (“the-word/thing which command”)
# ‹יהוה לאמר› (“YHWH to-say”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:2."
m.step("Lev.17.2")

# -------------------------- Lev.17.3 · ETNACHTA_SPLIT ----------------------
# ‹איש איש מבית› (“man man from-house”)
# ‹ישראל אשר ישחט› (“Israel which slaughter”)
# ‹שור או כשב› (“bullock or young-sheep”)
# ‹או עז במחנה› (“or she-goat in-camp”)
# ‹… או אשר ישחט› (“or which slaughter”)
# ‹מחוץ למחנה› (“from-outside to-camp”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:3."
m.step("Lev.17.3")
# witness-tier presupposed read: outside_slaughter_scope on asher_yishchat —
# read, not installed
m.witness_read("asher_yishchat", "outside_slaughter_scope",
                cites=["Sifra, Acharei Mot, Section 6 1", "Sifra, Acharei Mot, Section 6 3", "Sifra, Acharei Mot, Section 6 4", "Sifra, Acharei Mot, Section 6 5", "Sifra, Acharei Mot, Section 6 6", "Sifra, Acharei Mot, Section 6 7"])

# -------------------------- Lev.17.4 · ETNACHTA_SPLIT ----------------------
# ‹ואל פתח אהל› (“and-to opening tent”)
# ‹מועד לא הביאו› (“seasons not come/bring-him/its”)
# ‹להקריב קרבן ליהוה› (“to-bring-near offering to-YHWH”)
# ‹לפני משכן יהוה› (“to-face tabernacle YHWH”)
# ‹… דם יחשב לאיש› (“blood plait to-man”)
# ‹ההוא דם שפך› (“that blood spill-forth”)
# ‹ונכרת האיש ההוא› (“and-cut the-man that”)
# ‹מקרב עמו› (“from-nearest-part people-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:4."
m.step("Lev.17.4")
# witness-tier presupposed read: blood_reckoned on dam_yechashev — read, not
# installed
m.witness_read("dam_yechashev", "blood_reckoned",
                cites=["Sifra, Acharei Mot, Chapter 9 1", "Sifra, Acharei Mot, Chapter 9 2", "Sifra, Acharei Mot, Chapter 9 3", "Onkelos Lev 17:4"])

# -------------------------- Lev.17.5 · ETNACHTA_SPLIT ----------------------
# ‹למען אשר יביאו› (“so-that which come/bring”)
# ‹בני ישראל את› (“son Israel obj-marker”)
# ‹זבחיהם אשר הם› (“sacrifice-them/their which they”)
# ‹זבחים על פני› (“slaughter-an-animal over face”)
# ‹השדה … וזבחו זבחי› (“the-field … and-slaughter-an-animal sacrifice”)
# ‹שלמים ליהוה אותם› (“requital to-YHWH obj-marker-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:5."
m.step("Lev.17.5")
# witness-tier presupposed read: the_platform_table on al_pnei_hasadeh —
# read, not installed
m.witness_read("al_pnei_hasadeh", "the_platform_table",
                cites=["Sifra, Acharei Mot, Chapter 9 4", "Sifra, Acharei Mot, Chapter 9 5", "Sifra, Acharei Mot, Chapter 9 6", "Sifra, Acharei Mot, Chapter 9 7", "Onkelos Lev 17:6"])

# -------------------------- Lev.17.6 · ETNACHTA_SPLIT ----------------------
# ‹וזרק הכהן את› (“and-sprinkle the-priest obj-marker”)
# ‹הדם על מזבח› (“the-blood over altar”)
# ‹יהוה פתח אהל› (“YHWH opening tent”)
# ‹מועד … והקטיר החלב› (“seasons … and-smoke the-fat”)
# ‹לריח ניחח ליהוה› (“to-odor restful to-YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:6."
m.step("Lev.17.6")

# -------------------------- Lev.17.7 · ETNACHTA_SPLIT ----------------------
# ‹ולא יזבחו עוד› (“and-not slaughter-an-animal still/again”)
# ‹את זבחיהם לשעירם› (“obj-marker sacrifice-them/their to-shaggy”)
# ‹אשר הם זנים› (“which they commit-adultery”)
# ‹אחריהם … חקת עולם› (“after-them/their … statute forever”)
# ‹תהיה זאת להם› (“be this to-them/their”)
# ‹לדרתם› (“to-generation-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:7."
m.step("Lev.17.7")
# witness-tier presupposed read: the_demons on laseirim — read, not
# installed
m.witness_read("laseirim", "the_demons",
                cites=["Sifra, Acharei Mot, Chapter 9 8", "Sifra, Acharei Mot, Chapter 9 9", "Onkelos Lev 17:7"])

# -------------------------- Lev.17.8 · ETNACHTA_SPLIT ----------------------
# ‹ואלהם תאמר איש› (“and-to-them/their say man”)
# ‹איש מבית ישראל› (“man from-house Israel”)
# ‹ומן הגר אשר› (“and-from the-sojourner which”)
# ‹יגור בתוכם … אשר› (“turn-aside-from-the-road in-midst-them/their …
# which”)
# ‹יעלה עלה או› (“go-up burnt-offering or”)
# ‹זבח› (“sacrifice”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:8."
m.step("Lev.17.8")
# witness-tier presupposed read: the_completion_rule on asher_yaaleh — read,
# not installed
m.witness_read("asher_yaaleh", "the_completion_rule",
                cites=["Sifra, Acharei Mot, Chapter 10 2", "Sifra, Acharei Mot, Chapter 10 3", "Sifra, Acharei Mot, Chapter 10 4", "Sifra, Acharei Mot, Chapter 10 5", "Sifra, Acharei Mot, Chapter 10 8", "Sifra, Acharei Mot, Chapter 10 9", "Sifra, Acharei Mot, Chapter 10 10", "Sifra, Acharei Mot, Chapter 10 11"])

# -------------------------- Lev.17.9 · ETNACHTA_SPLIT ----------------------
# ‹ואל פתח אהל› (“and-to opening tent”)
# ‹מועד לא יביאנו› (“seasons not come/bring-him/its”)
# ‹לעשות אתו ליהוה› (“to-make obj-marker-him/its to-YHWH”)
# ‹… ונכרת האיש ההוא› (“and-cut the-man that”)
# ‹מעמיו› (“from-people-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:9."
m.step("Lev.17.9")

# -------------------------- Lev.17.10 · ETNACHTA_SPLIT ---------------------
# ‹ואיש איש מבית› (“and-man man from-house”)
# ‹ישראל ומן הגר› (“Israel and-from the-sojourner”)
# ‹הגר בתוכם אשר› (“the-turn-aside-from-the-road in-midst-them/their which”)
# ‹יאכל כל דם› (“eat all blood”)
# ‹… ונתתי פני בנפש› (“and-set face-me/my in-living-being”)
# ‹האכלת את הדם› (“the-eat obj-marker the-blood”)
# ‹והכרתי אתה מקרב› (“and-cut obj-marker-her/its from-nearest-part”)
# ‹עמה› (“people-her/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:10."
m.step("Lev.17.10")
# witness-tier presupposed read: the_blood_ban on kol_dam — read, not
# installed
m.witness_read("kol_dam", "the_blood_ban",
                cites=["Sifra, Acharei Mot, Section 7 3", "Sifra, Acharei Mot, Section 7 4", "Sifra, Acharei Mot, Section 7 5", "Sifra, Acharei Mot, Section 7 6", "Sifra, Acharei Mot, Section 7 7", "Onkelos Lev 17:11"])

# -------------------------- Lev.17.11 · COND_כי (“that”) -------------------
# ‹כי נפש הבשר› (“that living-being the-flesh”)
# ‹בדם הוא ואני› (“in-blood he/it and-I”)
# ‹נתתיו לכם על› (“set-him/its to-you/your(pl) over”)
# ‹המזבח לכפר על› (“the-altar to-atone over”)
# ‹נפשתיכם … כי הדם› (“living-being-you/your(pl) … that the-blood”)
# ‹הוא בנפש יכפר› (“he/it in-living-being atone”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:11."
m.step("Lev.17.11")

# -------------------------- Lev.17.12 · ETNACHTA_SPLIT ---------------------
# ‹על כן אמרתי› (“over so say”)
# ‹לבני ישראל כל› (“to-son Israel all”)
# ‹נפש מכם לא› (“living-being from-you/your(pl) not”)
# ‹תאכל דם … והגר› (“eat blood … and-the-sojourner”)
# ‹הגר בתוככם לא› (“the-turn-aside-from-the-road in-midst-you/your(pl) not”)
# ‹יאכל דם› (“eat blood”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:12."
m.step("Lev.17.12")

# -------------------------- Lev.17.13 · ETNACHTA_SPLIT ---------------------
# ‹ואיש איש מבני› (“and-man man from-son”)
# ‹ישראל ומן הגר› (“Israel and-from the-sojourner”)
# ‹הגר בתוכם אשר› (“the-turn-aside-from-the-road in-midst-them/their which”)
# ‹יצוד ציד חיה› (“lie-alongside chase living”)
# ‹או עו … ושפך› (“or ? … and-spill-forth”)
# ‹את דמו וכסהו› (“obj-marker blood-him/its and-plump-him/its”)
# ‹בעפר› (“in-dust”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:13."
m.step("Lev.17.13")
# witness-tier presupposed read: the_covering_machine on veshafach_vechisahu
# — read, not installed
m.witness_read("veshafach_vechisahu", "the_covering_machine",
                cites=["Sifra, Acharei Mot, Chapter 11 2", "Sifra, Acharei Mot, Chapter 11 4", "Sifra, Acharei Mot, Chapter 11 5", "Sifra, Acharei Mot, Chapter 11 6", "Sifra, Acharei Mot, Chapter 11 7", "Sifra, Acharei Mot, Chapter 11 8", "Sifra, Acharei Mot, Chapter 11 10", "Sifra, Acharei Mot, Chapter 11 11", "Onkelos Lev 17:13"])
# witness-tier presupposed read: two_clauses_two_nouns_one_dust on
# the_fitness_path_and_the_covering — read, not installed
m.witness_read("the_fitness_path_and_the_covering", "two_clauses_two_nouns_one_dust",
                cites=["Mishnah Zevachim 13:7", "Mishnah Zevachim 13:1", "Mishnah Zevachim 13:3", "Mishnah Zevachim 13:8", "Mishnah Zevachim 14:3", "Mishnah Chullin 6:1", "Mishnah Chullin 6:4", "Mishnah Chullin 6:7", "Sifra, Acharei Mot, Section 6 4", "Sifra, Acharei Mot, Chapter 10 5", "Sifra, Acharei Mot, Chapter 12 10", "Sifra, Acharei Mot, Chapter 9 1", "Sifra, Acharei Mot, Chapter 11 8", "Sifra, Acharei Mot, Chapter 11 10", "Sifra, Acharei Mot, Chapter 11 11", "Onkelos Lev 17:13"])

# -------------------------- Lev.17.14 · COND_כי (“that”) -------------------
# ‹כי נפש כל› (“that living-being all”)
# ‹בשר דמו בנפשו› (“flesh blood-him/its in-living-being-him/its”)
# ‹הוא ואמר לבני› (“he/it and-say to-son”)
# ‹ישראל דם כל› (“Israel blood all”)
# ‹בשר לא תאכ› (“flesh not ?”)
# ‹… כי נפש כל› (“that living-being all”)
# ‹בשר דמו הוא› (“flesh blood-him/its he/it”)
# ‹כל אכליו יכרת› (“all eat-him/its cut”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:14."
m.step("Lev.17.14")

# -------------------------- Lev.17.15 · ETNACHTA_SPLIT ---------------------
# ‹וכל נפש אשר› (“and-all living-being which”)
# ‹תאכל נבלה וטרפה› (“eat flabby-thing and-prey”)
# ‹באזרח ובגר … וכבס› (“in-spontaneous-growth and-in-sojourner … and-
# trample”)
# ‹בגדיו ורחץ במים› (“garment-him/its and-lave in-waters”)
# ‹וטמא עד הערב› (“and-be-foul until the-evening”)
# ‹וטהר› (“and-be-pure”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:15."
m.step("Lev.17.15")
# witness-tier presupposed read: the_swallow_house on nevelah_utrefah —
# read, not installed
m.witness_read("nevelah_utrefah", "the_swallow_house",
                cites=["Sifra, Acharei Mot, Chapter 12 2", "Sifra, Acharei Mot, Chapter 12 3", "Sifra, Acharei Mot, Chapter 12 4", "Sifra, Acharei Mot, Chapter 12 5", "Sifra, Acharei Mot, Chapter 12 7", "Sifra, Acharei Mot, Chapter 12 9", "Sifra, Acharei Mot, Chapter 12 13", "Onkelos Lev 17:15", "Onkelos Lev 17:16"])

# -------------------------- Lev.17.16 · COND_ואם (“and-if”) ----------------
# ‹ואם לא יכבס› (“and-if not trample”)
# ‹ובשרו לא ירחץ› (“and-flesh-him/its not lave”)
# ‹… ונשא עונו› (“and-lift/carry perversity-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 17:16."
m.step("Lev.17.16")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('asher_yishchat', 'outside_slaughter_scope'), ('dam_yechashev', 'blood_reckoned'), ('al_pnei_hasadeh', 'the_platform_table'), ('laseirim', 'the_demons'), ('asher_yaaleh', 'the_completion_rule'), ('kol_dam', 'the_blood_ban'), ('veshafach_vechisahu', 'the_covering_machine'), ('the_fitness_path_and_the_covering', 'two_clauses_two_nouns_one_dust'), ('nevelah_utrefah', 'the_swallow_house')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Acharei Mot, Section 6 1', 'Sifra, Acharei Mot, Section 6 3', 'Sifra, Acharei Mot, Section 6 4', 'Sifra, Acharei Mot, Section 6 5', 'Sifra, Acharei Mot, Section 6 6', 'Sifra, Acharei Mot, Section 6 7']
    assert all('outside_slaughter_scope' not in f for f in m.WORLD["facts"])
    assert 'asher_yishchat' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Acharei Mot, Chapter 9 1', 'Sifra, Acharei Mot, Chapter 9 2', 'Sifra, Acharei Mot, Chapter 9 3', 'Onkelos Lev 17:4']
    assert all('blood_reckoned' not in f for f in m.WORLD["facts"])
    assert 'dam_yechashev' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Acharei Mot, Chapter 9 4', 'Sifra, Acharei Mot, Chapter 9 5', 'Sifra, Acharei Mot, Chapter 9 6', 'Sifra, Acharei Mot, Chapter 9 7', 'Onkelos Lev 17:6']
    assert all('the_platform_table' not in f for f in m.WORLD["facts"])
    assert 'al_pnei_hasadeh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Acharei Mot, Chapter 9 8', 'Sifra, Acharei Mot, Chapter 9 9', 'Onkelos Lev 17:7']
    assert all('the_demons' not in f for f in m.WORLD["facts"])
    assert 'laseirim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Acharei Mot, Chapter 10 2', 'Sifra, Acharei Mot, Chapter 10 3', 'Sifra, Acharei Mot, Chapter 10 4', 'Sifra, Acharei Mot, Chapter 10 5', 'Sifra, Acharei Mot, Chapter 10 8', 'Sifra, Acharei Mot, Chapter 10 9', 'Sifra, Acharei Mot, Chapter 10 10', 'Sifra, Acharei Mot, Chapter 10 11']
    assert all('the_completion_rule' not in f for f in m.WORLD["facts"])
    assert 'asher_yaaleh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Acharei Mot, Section 7 3', 'Sifra, Acharei Mot, Section 7 4', 'Sifra, Acharei Mot, Section 7 5', 'Sifra, Acharei Mot, Section 7 6', 'Sifra, Acharei Mot, Section 7 7', 'Onkelos Lev 17:11']
    assert all('the_blood_ban' not in f for f in m.WORLD["facts"])
    assert 'kol_dam' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Acharei Mot, Chapter 11 2', 'Sifra, Acharei Mot, Chapter 11 4', 'Sifra, Acharei Mot, Chapter 11 5', 'Sifra, Acharei Mot, Chapter 11 6', 'Sifra, Acharei Mot, Chapter 11 7', 'Sifra, Acharei Mot, Chapter 11 8', 'Sifra, Acharei Mot, Chapter 11 10', 'Sifra, Acharei Mot, Chapter 11 11', 'Onkelos Lev 17:13']
    assert all('the_covering_machine' not in f for f in m.WORLD["facts"])
    assert 'veshafach_vechisahu' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Mishnah Zevachim 13:7', 'Mishnah Zevachim 13:1', 'Mishnah Zevachim 13:3', 'Mishnah Zevachim 13:8', 'Mishnah Zevachim 14:3', 'Mishnah Chullin 6:1', 'Mishnah Chullin 6:4', 'Mishnah Chullin 6:7', 'Sifra, Acharei Mot, Section 6 4', 'Sifra, Acharei Mot, Chapter 10 5', 'Sifra, Acharei Mot, Chapter 12 10', 'Sifra, Acharei Mot, Chapter 9 1', 'Sifra, Acharei Mot, Chapter 11 8', 'Sifra, Acharei Mot, Chapter 11 10', 'Sifra, Acharei Mot, Chapter 11 11', 'Onkelos Lev 17:13']
    assert all('two_clauses_two_nouns_one_dust' not in f for f in m.WORLD["facts"])
    assert 'the_fitness_path_and_the_covering' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Acharei Mot, Chapter 12 2', 'Sifra, Acharei Mot, Chapter 12 3', 'Sifra, Acharei Mot, Chapter 12 4', 'Sifra, Acharei Mot, Chapter 12 5', 'Sifra, Acharei Mot, Chapter 12 7', 'Sifra, Acharei Mot, Chapter 12 9', 'Sifra, Acharei Mot, Chapter 12 13', 'Onkelos Lev 17:15', 'Onkelos Lev 17:16']
    assert all('the_swallow_house' not in f for f in m.WORLD["facts"])
    assert 'nevelah_utrefah' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
