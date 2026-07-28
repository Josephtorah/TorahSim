#!/usr/bin/env python3
"""
Generate Exodus Pre-Code logic units (one thorough block at a time).
Interpreter only: taamim trees from parser; logic content from BLOCKS (Written-first notes).
Mekhilta dual-track samples for law-spine chapters. Not binding religious law.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from taamim_tree_parse import parse_verse, tree_ascii_string, strip_taamim_and_points  # noqa: E402

UNITS = ROOT / "logic" / "units"
MEKH_EN = ROOT / "Data" / "mekhilta_en.json"
MEKH_HE = ROOT / "Data" / "mekhilta_he.json"

# ---------------------------------------------------------------------------
# Block schedule (matches EXODUS_BUILD thorough map; skip 01–02 already done)
# ---------------------------------------------------------------------------

BLOCKS: list[dict[str, Any]] = [
    # --- Phase A ---
    {
        "id": "exo_03_bush_call",
        "refs": "3:1-22",
        "ch_start": 3, "v_start": 1, "ch_end": 3, "v_end": 22,
        "title_en": "Burning bush call: Horeb, name, send Moses (3:1–22)",
        "title_he": "הַסְּנֶה — קְרִיאַת מֹשֶׁה",
        "title_he_translit": "ha-seneh — keri'at moshe",
        "title_he_en": "The bush — call of Moses",
        "depends_on": ["exo_02_moses_midian"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Moses shepherd at Horeb; bush burns unconsumed — attention trap. "
            "(2) Holy ground; God of Abraham/Isaac/Jacob — covenant import from Gen. "
            "(3) Cry heard; send Moses to Pharaoh; land promise. "
            "(4) Name: Ehyeh asher Ehyeh / YHWH. "
            "(5) Elders + request three days; Egypt will not let go; plunder forecast."
        ),
        "steps": [
            ("STEP_E3_A1", "3:1-6", "BUSH_THEOPHANY",
             "וּמֹשֶׁה הָיָה רֹעֶה … הַסְּנֶה … הַר הָאֱלֹהִים חֹרֵבָה",
             "u-moshe hayah ro'eh … ha-seneh … har ha-Elohim chorevah",
             "Moses shepherds flock of Jethro to Horeb; angel/YHWH in flame of bush; bush burns unconsumed; Moses turns aside; do not approach; remove sandals; holy ground; God of fathers."),
            ("STEP_E3_B1", "3:7-12", "COMMISSION_SEND",
             "רָאֹה רָאִיתִי … וָאֵרֵד לְהַצִּילוֹ … לְכָה וְאֶשְׁלָחֲךָ",
             "ra'oh ra'iti … va-ered le-hatzilo … lekhah ve-eshlachakha",
             "God has seen affliction, heard cry, knows pains; come down to save to good land; send Moses to Pharaoh; who am I; sign = serve God on this mountain after bringing out."),
            ("STEP_E3_C1", "3:13-15", "NAME_REVEAL",
             "אֶהְיֶה אֲשֶׁר אֶהְיֶה … יְהוָה אֱלֹהֵי אֲבֹתֵיכֶם",
             "ehyeh asher ehyeh … YHWH elohei avoteikhem",
             "Moses asks name for Israel; Ehyeh asher Ehyeh; say Ehyeh sent me; YHWH God of Abraham Isaac Jacob — this is my name forever."),
            ("STEP_E3_D1", "3:16-22", "PLAN_ELDERS_SPOIL",
             "לֵךְ וְאָסַפְתָּ אֶת־זִקְנֵי … שְׁלֹשֶׁת יָמִים … וְנִצַּלְתֶּם",
             "lekh ve-asafta et-ziknei … sheloshet yamim … ve-nitzaltem",
             "Gather elders; announce visitation and land; go to king; three-day wilderness feast request; king will not let go; smite Egypt; favor; silver/gold/clothing spoil of Egypt."),
        ],
        "states": [
            ("S_midian_shepherd", "Moses still Midian shepherd"),
            ("S_bush_encounter", "Theophany at bush; holy ground"),
            ("S_commissioned", "Sent to Pharaoh with name and plan"),
            ("S_plan_spoken", "Elders path + spoil forecast loaded"),
        ],
        "exports": [
            ("EXPORT_ehyeh_name", "אֶהְיֶה אֲשֶׁר אֶהְיֶה", "ehyeh asher ehyeh", "Divine name formula at call"),
            ("EXPORT_holy_ground_horeb", "אַדְמַת־קֹדֶשׁ", "admat-kodesh", "Holy ground at Horeb"),
            ("EXPORT_send_to_pharaoh", None, None, "Moses commissioned to Egypt/Pharaoh"),
        ],
    },
    {
        "id": "exo_04_signs_return",
        "refs": "4:1-31",
        "ch_start": 4, "v_start": 1, "ch_end": 4, "v_end": 31,
        "title_en": "Signs, speech help, Zipporah, Aaron meets, elders believe (4:1–31)",
        "title_he": "הָאֹתוֹת וְשׁוּב לְמִצְרַיִם",
        "title_he_translit": "ha-otot ve-shuv le-mitzrayim",
        "title_he_en": "The signs and return to Egypt",
        "depends_on": ["exo_03_bush_call"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Three signs for unbelieving Israel: staff-snake, leprous hand, Nile-blood. "
            "(2) Moses claims heavy mouth; Aaron as mouth; staff in hand. "
            "(3) Return Egypt; all seekers of Moses's life dead. "
            "(4) Zipporah circumcision crisis at lodging. "
            "(5) Aaron meets at mountain; signs before people; people believe and bow."
        ),
        "steps": [
            ("STEP_E4_A1", "4:1-9", "THREE_SIGNS",
             "מַה־זֶּה בְיָדֶךָ … נָחָשׁ … מְצֹרַעַת … דָּם",
             "mah-zeh be-yadekha … nachash … metzora'at … dam",
             "Staff becomes snake and returns; hand leprous as snow then healed; water of Nile on dry land becomes blood — signs if they disbelieve."),
            ("STEP_E4_B1", "4:10-17", "AARON_MOUTH",
             "לֹא אִישׁ דְּבָרִים … אַהֲרֹן אָחִיךָ … וְשַׂמְתָּ אֶת־הַדְּבָרִים",
             "lo ish devarim … aharon achikha … ve-samta et-ha-devarim",
             "Moses not a man of words; YHWH makes mouth; Aaron the Levite will speak; Moses puts words in Aaron's mouth; staff for signs."),
            ("STEP_E4_C1", "4:18-23", "RETURN_ORDER",
             "אֵלְכָה נָּא … שׁוּב מִצְרָיִם … בְּנִי בְכֹרִי יִשְׂרָאֵל",
             "elkhah na … shuv mitzrayim … beni vekhori yisrael",
             "Leave Jethro; return Egypt; wonders before Pharaoh; harden heart; Israel firstborn son; let son go or kill your firstborn."),
            ("STEP_E4_D1", "4:24-26", "ZIPPORAH_CIRCUMCISION",
             "וַיְבַקֵּשׁ הֲמִיתוֹ … צִפֹּרָה … חֲתַן דָּמִים",
             "va-yevakesh hamito … tzipporah … chatan damim",
             "At lodging YHWH seeks to kill him; Zipporah circumcises son; chatan damim — bridegroom of blood."),
            ("STEP_E4_E1", "4:27-31", "AARON_ELDERS_BELIEVE",
             "לֵךְ לִקְרַאת מֹשֶׁה … וַיַּאֲמֵן הָעָם … וַיִּשְׁתַּחֲוּוּ",
             "lekh likrat moshe … va-ya'amen ha-am … va-yishtachavu",
             "Aaron meets Moses at mountain of God; speak to elders; signs done; people believe; heard YHWH visited; bow and worship."),
        ],
        "states": [
            ("S_signs_given", "Staff/hand/Nile signs authorized"),
            ("S_aaron_paired", "Aaron as mouth; staff for signs"),
            ("S_return_path", "En route Egypt; firstborn threat loaded"),
            ("S_people_believe", "Elders/people believe and bow"),
        ],
        "exports": [
            ("EXPORT_three_signs", None, None, "Staff-snake, hand, Nile-blood"),
            ("EXPORT_aaron_mouth", "אַהֲרֹן", "aharon", "Aaron speaks for Moses"),
            ("EXPORT_people_believe", None, None, "Israel believes visitation"),
        ],
    },
    {
        "id": "exo_05_bricks_worse",
        "refs": "5:1-23",
        "ch_start": 5, "v_start": 1, "ch_end": 5, "v_end": 23,
        "title_en": "First audience: no straw, heavier labor, Moses complains (5:1–23)",
        "title_he": "תֶּבֶן אֵין — הָעֲבֹדָה כָּבְדָה",
        "title_he_translit": "teven ein — ha-avodah kavedah",
        "title_he_en": "No straw — labor grows heavy",
        "depends_on": ["exo_04_signs_return"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Let my people go feast — Pharaoh does not know YHWH. "
            "(2) Straw withheld; brick quota same; officers beaten. "
            "(3) Israel officers blame Moses/Aaron. "
            "(4) Moses returns to YHWH: why harm; not delivered."
        ),
        "steps": [
            ("STEP_E5_A1", "5:1-5", "FIRST_DEMAND",
             "שַׁלַּח אֶת־עַמִּי … לֹא יָדַעְתִּי אֶת־יְהוָה",
             "shalach et-ami … lo yadati et-YHWH",
             "Moses/Aaron to Pharaoh: send my people to feast; who is YHWH; I will not send; why stop the people from work."),
            ("STEP_E5_B1", "5:6-14", "NO_STRAW",
             "לֹא תֹאסִפוּן לָתֵת תֶּבֶן … תֹּכֶן לְבֵנִים",
             "lo to'sifun latet teven … tokhen levenim",
             "No more straw given; gather straw yourselves; same brick count; taskmasters press; officers of Israel beaten."),
            ("STEP_E5_C1", "5:15-21", "OFFICERS_CRY",
             "לָמָּה תַעֲשֶׂה … נִבְאַשְׁתֶּם … יֵרֶא יְהוָה עֲלֵיכֶם",
             "lamah ta'aseh … niv'ashtem … yere YHWH aleikhem",
             "Officers appeal to Pharaoh; you are idle; meet Moses/Aaron: you made us stink; YHWH look on you and judge."),
            ("STEP_E5_D1", "5:22-23", "MOSES_COMPLAIN",
             "לָמָה הֲרֵעֹתָה … וְהַצֵּל לֹא־הִצַּלְתָּ",
             "lamah hare'ota … ve-hatzel lo-hitzalta",
             "Moses to YHWH: why harm this people; why send me; since I came to Pharaoh, harm only; you have not delivered."),
        ],
        "states": [
            ("S_demand_refused", "Pharaoh refuses; does not know YHWH"),
            ("S_labor_worsened", "No straw; quota held"),
            ("S_israel_against_moses", "Officers blame leaders"),
            ("S_moses_complaint", "Complaint registered; handoff to ch.6"),
        ],
        "exports": [
            ("EXPORT_pharaoh_unknown_yhwh", "לֹא יָדַעְתִּי אֶת־יְהוָה", "lo yadati et-YHWH", "Pharaoh claims not to know YHWH"),
            ("EXPORT_labor_harder", None, None, "Bondage intensifies after first demand"),
        ],
    },
    {
        "id": "exo_06_name_roster",
        "refs": "6:1-30",
        "ch_start": 6, "v_start": 1, "ch_end": 6, "v_end": 30,
        "title_en": "YHWH name assurance, four verbs, Levi roster, Moses uncircumcised lips (6:1–30)",
        "title_he": "אֲנִי יְהוָה — רֹאשֵׁי בֵית אָבוֹת",
        "title_he_translit": "ani YHWH — rashei veit avot",
        "title_he_en": "I am YHWH — heads of fathers' houses",
        "depends_on": ["exo_05_bricks_worse"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Now you will see: strong hand forces send-out. "
            "(2) El Shaddai to fathers; name YHWH not made known that way; berit land. "
            "(3) Four redemption verbs; take as people; be God. "
            "(4) Israel does not listen — short spirit, hard slavery. "
            "(5) Levi genealogy to Moses/Aaron; charge restated; uncircumcised lips."
        ),
        "steps": [
            ("STEP_E6_A1", "6:1-8", "NAME_AND_FOUR_VERBS",
             "אֲנִי יְהוָה … וְהוֹצֵאתִי … וְהִצַּלְתִּי … וְגָאַלְתִּי … וְלָקַחְתִּי",
             "ani YHWH … ve-hotzeti … ve-hitzalti … ve-ga'alti … ve-lakachti",
             "I am YHWH; El Shaddai to patriarchs; berit to give land; heard groan; remember berit; four verbs bring out/save/redeem/take; I am YHWH."),
            ("STEP_E6_B1", "6:9-13", "ISRAEL_WONT_HEAR",
             "וְלֹא שָׁמְעוּ … מִקֹּצֶר רוּחַ … דַּבֵּר אֶל־פַּרְעֹה",
             "ve-lo sham'u … mi-kotzer ruach … dabber el-par'oh",
             "Moses speaks; Israel will not hear — shortness of spirit and hard slavery; Moses: uncircumcised lips; charge Moses/Aaron to bring Israel out."),
            ("STEP_E6_C1", "6:14-27", "LEVI_ROSTER",
             "רָאשֵׁי בֵית־אֲבֹתָם … לֵוִי … עַמְרָם … מֹשֶׁה וְאַהֲרֹן",
             "rashei veit-avotam … levi … amram … moshe ve-aharon",
             "Heads of houses: Reuben, Simeon, Levi lines; Kohath; Amram takes Jochebed; Aaron/Moses; this is Aaron and Moses who spoke to Pharaoh."),
            ("STEP_E6_D1", "6:28-30", "CHARGE_REPLAY",
             "אֲנִי יְהוָה … הֵן אֲנִי עֲרַל שְׂפָתַיִם",
             "ani YHWH … hen ani arel sefatayim",
             "On day YHWH spoke in Egypt: speak all I speak to Pharaoh; Moses: uncircumcised lips — how will Pharaoh hear."),
        ],
        "states": [
            ("S_name_assured", "YHWH name + four verbs spoken"),
            ("S_israel_deaf", "People will not hear Moses"),
            ("S_levi_identity", "Moses/Aaron lineage fixed"),
            ("S_ready_plagues", "Charge restated; bridge to staff/blood"),
        ],
        "exports": [
            ("EXPORT_four_redemption_verbs", "וְהוֹצֵאתִי וְהִצַּלְתִּי וְגָאַלְתִּי וְלָקַחְתִּי",
             "ve-hotzeti ve-hitzalti ve-ga'alti ve-lakachti", "Four redemption verbs"),
            ("EXPORT_arel_lips", "עֲרַל שְׂפָתָיִם", "arel sefatayim", "Moses uncircumcised lips claim"),
        ],
    },
    {
        "id": "exo_07_staff_blood",
        "refs": "7:1-29",
        "ch_start": 7, "v_start": 1, "ch_end": 7, "v_end": 29,
        "title_en": "God to Pharaoh: staffs, blood plague (7:1–29)",
        "title_he": "מַטֶּה — דָּם בַּיְאֹר",
        "title_he_translit": "matteh — dam ba-ye'or",
        "title_he_en": "Staff — blood in the Nile",
        "depends_on": ["exo_06_name_roster"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Moses as god to Pharaoh; Aaron prophet; harden heart for signs multiply. "
            "(2) Staff-snake contest; Aaron's swallows. "
            "(3) Blood: Nile and waters strike; magicians do so; dig for water."
        ),
        "steps": [
            ("STEP_E7_A1", "7:1-7", "ROLES_SET",
             "נְתַתִּיךָ אֱלֹהִים לְפַרְעֹה … אַהֲרֹן אָחִיךָ יִהְיֶה נְבִיאֶךָ",
             "netatikha elohim le-par'oh … aharon achikha yihyeh nevi'ekha",
             "Moses made god to Pharaoh; Aaron prophet; speak all; harden heart; know I am YHWH; Moses 80 Aaron 83."),
            ("STEP_E7_B1", "7:8-13", "STAFF_SNAKES",
             "קַח אֶת־מַטְּךָ … וַיְהִי לְתַנִּין … וַיִּבְלַע מַטֵּה־אַהֲרֹן",
             "kach et-mattekha … va-yehi le-tanin … va-yivla matteh-aharon",
             "Staff becomes tanin; magicians do likewise; Aaron's staff swallows theirs; heart hard."),
            ("STEP_E7_C1", "7:14-25", "BLOOD_PLAGUE",
             "הִנֵּה אָנֹכִי מַכֶּה … וְנֶהֶפְכוּ לְדָם … שִׁבְעַת יָמִים",
             "hineh anokhi makkeh … ve-nehefkhu le-dam … shiv'at yamim",
             "Strike Nile; fish die; river stinks; blood throughout; magicians copy; Pharaoh heart hard; seven days fulfilled."),
            ("STEP_E7_D1", "7:26-29", "FROGS_WARN",
             "שַׁלַּח אֶת־עַמִּי … אִם־מָאֵן … בַּצְפַרְדְּעִים",
             "shalach et-ami … im-me'en … ba-tzefarde'im",
             "Warning of frogs if refuse to send (bridge into ch.8 numbering)."),
        ],
        "states": [
            ("S_roles_public", "Moses/Aaron roles before Pharaoh"),
            ("S_staff_won", "Aaron staff swallowed magicians"),
            ("S_blood_done", "Nile blood plague executed"),
            ("S_frogs_warned", "Frogs threat spoken"),
        ],
        "exports": [
            ("EXPORT_plague_blood", "דָּם", "dam", "First plague blood"),
            ("EXPORT_harden_pattern", None, None, "Heart-harden pattern active"),
        ],
    },
    {
        "id": "exo_08_frogs_to_swarm",
        "refs": "8:1-28",
        "ch_start": 8, "v_start": 1, "ch_end": 8, "v_end": 28,
        "title_en": "Frogs, lice, swarm; Goshen distinction (8:1–28)",
        "title_he": "צְפַרְדְּעִים — כִּנִּים — עָרֹב",
        "title_he_translit": "tzefarde'im — kinim — arov",
        "title_he_en": "Frogs — lice — swarm",
        "depends_on": ["exo_07_staff_blood"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Frogs; magicians copy; Pharaoh bargains then hardens. "
            "(2) Lice from dust; magicians fail — finger of God. "
            "(3) Swarm; Goshen set apart; sacrifice in land vs three days."
        ),
        "steps": [
            ("STEP_E8_A1", "8:1-11", "FROGS",
             "הַצְּפַרְדְּעִים … וַיֵּצֵא הַצְּפַרְדֵּעַ … הַמְתִירוּ",
             "ha-tzefarde'im … va-yetze ha-tzefardea … hamtiru",
             "Frogs cover Egypt; magicians copy; Pharaoh asks relief tomorrow; frogs die; heaps stink; hardens."),
            ("STEP_E8_B1", "8:12-15", "LICE",
             "הַךְ אֶת־עֲפַר … לְכִנִּם … אֶצְבַּע אֱלֹהִים הִוא",
             "hakh et-afar … le-kinim … etzba Elohim hi",
             "Dust becomes lice; magicians cannot; finger of God; heart hard."),
            ("STEP_E8_C1", "8:16-28", "SWARM_GOSHEN",
             "הֶעָרֹב … וְהִפְלֵיתִי … בְּאֶרֶץ גֹּשֶׁן",
             "he-arov … ve-hifleti … be-eretz goshen",
             "Swarm; distinction Goshen; Pharaoh: sacrifice in land; Moses: abomination; three days; he hardens after relief."),
        ],
        "states": [
            ("S_frogs_done", "Frogs plague cycle complete"),
            ("S_magicians_fail", "Lice: magicians cannot copy"),
            ("S_goshen_set", "Goshen distinction introduced"),
        ],
        "exports": [
            ("EXPORT_finger_of_god", "אֶצְבַּע אֱלֹהִים", "etzba Elohim", "Magicians confess finger of God"),
            ("EXPORT_goshen_distinction", "גֹּשֶׁן", "goshen", "Israel set apart in Goshen"),
        ],
    },
    {
        "id": "exo_09_livestock_hail",
        "refs": "9:1-35",
        "ch_start": 9, "v_start": 1, "ch_end": 9, "v_end": 35,
        "title_en": "Livestock death, boils, hail; fearers of word (9:1–35)",
        "title_he": "דֶּבֶר — שְׁחִין — בָּרָד",
        "title_he_translit": "dever — shechin — barad",
        "title_he_en": "Pestilence — boils — hail",
        "depends_on": ["exo_08_frogs_to_swarm"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Livestock of Egypt die; Israel livestock spared. "
            "(2) Boils on man and beast; magicians cannot stand. "
            "(3) Hail with fire; warn servants; those who fear word shelter livestock; flax/barley struck; wheat/spelt later."
        ),
        "steps": [
            ("STEP_E9_A1", "9:1-7", "LIVESTOCK",
             "יַד־יְהוָה הוֹיָה … בְּמִקְנְךָ … וּמִמִּקְנֵה יִשְׂרָאֵל לֹא־מֵת",
             "yad-YHWH hoyah … be-miknekha … u-mi-mikneh yisrael lo-met",
             "Hand of YHWH on livestock; all Egypt livestock die; of Israel none die; heart hard."),
            ("STEP_E9_B1", "9:8-12", "BOILS",
             "פִּיחַ כִּבְשָׁן … לִשְׁחִין … לֹא־יָכְלוּ הַחַרְטֻמִּים",
             "piach kivshan … li-shechin … lo-yakhelu ha-chartumim",
             "Furnace soot becomes boils; magicians cannot stand before Moses; YHWH hardens heart."),
            ("STEP_E9_C1", "9:13-35", "HAIL",
             "בָּרָד כָּבֵד … הַיָּרֵא … הַפִּשְׁתָּה וְהַשְּׂעֹרָה",
             "barad kaved … ha-yare … ha-pishtah ve-ha-se'orah",
             "Hail plague; purpose to show power; fearers of word bring in servants/livestock; hail fire; flax barley struck; Pharaoh admits sin then hardens."),
        ],
        "states": [
            ("S_livestock_dead", "Egypt livestock struck"),
            ("S_boils_done", "Boils; magicians out"),
            ("S_hail_split_response", "Some fear word; some ignore"),
        ],
        "exports": [
            ("EXPORT_fearers_of_word", "הַיָּרֵא אֶת־דְּבַר יְהוָה", "ha-yare et-devar YHWH", "Those who fear the word shelter"),
            ("EXPORT_plague_hail", "בָּרָד", "barad", "Hail plague"),
        ],
    },
    {
        "id": "exo_10_locust_dark",
        "refs": "10:1-29",
        "ch_start": 10, "v_start": 1, "ch_end": 10, "v_end": 29,
        "title_en": "Locusts and darkness; who may go (10:1–29)",
        "title_he": "אַרְבֶּה — חֹשֶׁךְ",
        "title_he_translit": "arbeh — choshekh",
        "title_he_en": "Locust — darkness",
        "depends_on": ["exo_09_livestock_hail"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) Signs for storytelling to children. "
            "(2) Locusts; servants urge send; who goes — only men vs all; locusts cover eye of land. "
            "(3) Darkness felt three days; Israel had light; Pharaoh: go without flocks; Moses refuses; see my face no more."
        ),
        "steps": [
            ("STEP_E10_A1", "10:1-20", "LOCUSTS",
             "הָאַרְבֶּה … מִ י וָמִי הַהֹלְכִים … כָּל־מַאֲכַל הָעֵץ",
             "ha-arbeh … mi va-mi ha-holkhim … kol-ma'akhal ha-etz",
             "Locust warning; who goes negotiation; east wind locusts; cover land; Pharaoh: I sinned; west wind removes; harden."),
            ("STEP_E10_B1", "10:21-29", "DARKNESS",
             "יְהִי חֹשֶׁךְ … שְׁלֹשֶׁת יָמִים … לֵךְ מֵעָלַי",
             "yehi choshekh … sheloshet yamim … lekh me-alai",
             "Darkness three days; Israel light in dwellings; go without flocks refused; Pharaoh: see my face no more; Moses agrees he will not see face again."),
        ],
        "states": [
            ("S_locusts_done", "Locust plague complete"),
            ("S_darkness_done", "Darkness; flock standoff"),
            ("S_face_ban", "Pharaoh bans Moses face — prelude death of firstborn"),
        ],
        "exports": [
            ("EXPORT_darkness", "חֹשֶׁךְ", "choshekh", "Darkness plague"),
            ("EXPORT_face_ban", None, None, "Moses will not see Pharaoh face again"),
        ],
    },
    {
        "id": "exo_11_last_warning",
        "refs": "11:1-10",
        "ch_start": 11, "v_start": 1, "ch_end": 11, "v_end": 10,
        "title_en": "One more blow: firstborn death forecast; favor; Moses hot anger (11:1–10)",
        "title_he": "נֶגַע אֶחָד עוֹד — בְּכוֹר",
        "title_he_translit": "nega echad od — bekhor",
        "title_he_en": "One more plague — firstborn",
        "depends_on": ["exo_10_locust_dark"],
        "genre": "narrative_fsm",
        "mekh": "thin",
        "learn": (
            "(1) One more plague then full send with drive-out. "
            "(2) Favor of Egypt; silver/gold. "
            "(3) About midnight firstborn die; great cry; dog not sharpen tongue at Israel. "
            "(4) Servants will bow; Moses leaves in hot anger; wonders multiplied; heart hard."
        ),
        "steps": [
            ("STEP_E11_A1", "11:1-3", "ONE_MORE_FAVOR",
             "עוֹד נֶגַע אֶחָד … כְּשַׁלְּחוֹ כָּלָה … חֵן … כְּלֵי־כֶסֶף",
             "od nega echad … ke-shalcho kalah … chen … kelei-kesef",
             "One more plague; then he will send completely; ask silver/gold; Moses very great in Egypt."),
            ("STEP_E11_B1", "11:4-8", "FIRSTBORN_FORECAST",
             "כַּחֲצֹת הַלַּיְלָה … כָּל־בְּכוֹר … צְעָקָה גְדֹלָה … וַיֵּצֵא … בָּחֳרִי־אָף",
             "ka-chatzot ha-lailah … kol-bekhor … tze'akah gedolah … va-yetze … ba-chori-af",
             "Midnight all firstborn die; cry; not a dog against Israel; servants bow; Moses exits hot anger."),
            ("STEP_E11_C1", "11:9-10", "HARDEN_SUMMARY",
             "לֹא־יִשְׁמַע … לְמַעַן רְבוֹת מוֹפְתַי",
             "lo-yishma … lema'an revot moftai",
             "Pharaoh will not hear so wonders multiply; Moses/Aaron did wonders; YHWH hardened heart; did not send Israel."),
        ],
        "states": [
            ("S_last_blow_announced", "Firstborn death announced"),
            ("S_ready_pesach", "Handoff to 12 Pesach law/narrative"),
        ],
        "exports": [
            ("EXPORT_firstborn_threat", "כָּל־בְּכוֹר", "kol-bekhor", "All firstborn will die"),
            ("EXPORT_bridge_to_pesach", None, None, "Bridge into Exodus 12 Pesach / Mekhilta spine"),
        ],
    },
    # --- Phase B Mekhilta spine (abbreviated steps; mekh primary) ---
    {
        "id": "exo_12_pesach_command",
        "refs": "12:1-28",
        "ch_start": 12, "v_start": 1, "ch_end": 12, "v_end": 28,
        "title_en": "Pesach command: month, lamb, blood, matzot, firstborn pass (12:1–28)",
        "title_he": "הַחֹדֶשׁ הַזֶּה — פֶּסַח",
        "title_he_translit": "ha-chodesh ha-zeh — pesach",
        "title_he_en": "This month — Pesach",
        "depends_on": ["exo_11_last_warning"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [12],
        "learn": (
            "(1) This month head of months. (2) Lamb 10th–14th; blood on doorposts. "
            "(3) Roast; matzot; bitter; no leftover. (4) YHWH strikes Egypt; pass over. "
            "(5) Memorial statute; unleavened seven days. Mekhilta primary decoder."
        ),
        "steps": [
            ("STEP_E12a_A1", "12:1-14", "PESACH_NIGHT_RULES",
             "הַחֹדֶשׁ הַזֶּה … שֶׂה … דָּם … פֶּסַח הוּא לַיהוָה",
             "ha-chodesh ha-zeh … seh … dam … pesach hu la-YHWH",
             "New year month; lamb per house; 14th dusk kill; blood posts; roast fire; matzot maror; eat haste; pass-over plague night; memorial."),
            ("STEP_E12a_B1", "12:15-20", "MATZOT_SEVEN",
             "שִׁבְעַת יָמִים מַצּוֹת … כָּל־מַחְמֶצֶת",
             "shiv'at yamim matzot … kol-machmetzet",
             "Seven days matzot; cut off if leaven; holy assemblies day 1 and 7; no work except food."),
            ("STEP_E12a_C1", "12:21-28", "BLOOD_APPLY_TEACH",
             "מִשְׁכוּ וּקְחוּ … וְהִגַּעְתֶּם … וְשָׁמְרתֶּם … וַיִּקֹּד הָעָם",
             "mishkhu u-kechu … ve-higatem … ve-shmartem … va-yikod ha-am",
             "Elders take flock; blood hyssop; none out till morning; statute forever; children ask; people bow and do."),
        ],
        "states": [
            ("S_pesach_commanded", "Pesach night rules issued"),
            ("S_matzot_statute", "Seven-day matzot statute"),
            ("S_people_obey", "People bow and perform"),
        ],
        "exports": [
            ("EXPORT_pesach_blood", "דָּם עַל־הַמְּזוּזֹת", "dam al-ha-mezuzot", "Blood on doorposts"),
            ("EXPORT_matzot_statute", "מַצּוֹת", "matzot", "Unleavened statute"),
            ("EXPORT_head_of_months", "רֹאשׁ חֳדָשִׁים", "rosh chodashim", "This month head of months"),
        ],
        "decision_hints": [
            ("IF lamb selected on 10th AND kept to 14th", "THEN kill at dusk between evenings"),
            ("IF blood on two posts and lintel", "THEN destroyer passes house"),
            ("IF leaven found in seven days", "THEN soul cut off from Israel"),
        ],
    },
    {
        "id": "exo_12_midnight_leave",
        "refs": "12:29-51",
        "ch_start": 12, "v_start": 29, "ch_end": 12, "v_end": 51,
        "title_en": "Midnight firstborn; drive-out; mixed multitude; pesach statute (12:29–51)",
        "title_he": "וַיְהִי בַּחֲצִי הַלַּיְלָה — יְצִיאָה",
        "title_he_translit": "va-yehi ba-chatzi ha-lailah — yetzi'ah",
        "title_he_en": "At midnight — going out",
        "depends_on": ["exo_12_pesach_command"],
        "genre": "narrative_fsm",
        "mekh": "primary",
        "mekh_chapters": [12],
        "learn": (
            "(1) Midnight strike firstborn. (2) Pharaoh drives out. (3) Dough unrisen; spoil. "
            "(4) 430 years; night of watching. (5) Foreigner rules for pesach; one law."
        ),
        "steps": [
            ("STEP_E12b_A1", "12:29-36", "MIDNIGHT_DRIVE",
             "וַיְהִי בַּחֲצִי הַלַּיְלָה … קוּמוּ צְּאוּ … וַיְנַצְּלוּ",
             "va-yehi ba-chatzi ha-lailah … kumu tze'u … va-yetzatzelu",
             "Midnight firstborn die; cry; Pharaoh: go serve; also flocks; Egyptians urgent; silver gold clothing favor."),
            ("STEP_E12b_B1", "12:37-42", "LEAVE_430",
             "מֵרַעְמְסֵס סֻכֹּתָה … שְׁלֹשִׁים שָׁנָה וְאַרְבַּע מֵאוֹת",
             "me-ra'meses sukkotah … sheloshim shanah ve-arba me'ot",
             "Rameses to Succoth; 600k men + mixed multitude; dough cakes; sojourn 430 years; night of watching for YHWH."),
            ("STEP_E12b_C1", "12:43-51", "PESACH_FOREIGNER",
             "זֹאת חֻקַּת הַפָּסַח … כָּל־עֶרֶל לֹא־יֹאכַל … תּוֹרָה אַחַת",
             "zot chukat ha-pasach … kol-arel lo-yokhal … torah achat",
             "Pesach statute: no foreigner uncircumcised; slave circumcised may eat; one law for native and ger; that day YHWH brought hosts out."),
        ],
        "states": [
            ("S_firstborn_struck", "Egypt firstborn dead"),
            ("S_israel_out", "Israel leaving Egypt"),
            ("S_pesach_boundary_rules", "Who may eat pesach defined"),
        ],
        "exports": [
            ("EXPORT_exodus_event", "יְצִיאַת מִצְרַיִם", "yetzi'at mitzrayim", "Exodus event"),
            ("EXPORT_430_years", "שְׁלֹשִׁים שָׁנָה וְאַרְבַּע מֵאוֹת", "sheloshim shanah ve-arba me'ot", "430 years sojourn note"),
            ("EXPORT_one_torah_ger", "תּוֹרָה אַחַת", "torah achat", "One law native and sojourner"),
        ],
    },
    {
        "id": "exo_13_firstborn_matzot",
        "refs": "13:1-16",
        "ch_start": 13, "v_start": 1, "ch_end": 13, "v_end": 16,
        "title_en": "Sanctify firstborn; matzot teaching; hand/forehead signs (13:1–16)",
        "title_he": "קַדֶּשׁ־לִי כָל־בְּכוֹר",
        "title_he_translit": "kadesh-li khol-bekhor",
        "title_he_en": "Sanctify to me every firstborn",
        "depends_on": ["exo_12_midnight_leave"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [13],
        "learn": (
            "(1) Sanctify firstborn man and beast. (2) Matzot memorial teaching to child. "
            "(3) Firstborn donkey redeem or neck; human firstborn redeem. (4) Sign on hand and between eyes."
        ),
        "steps": [
            ("STEP_E13a_A1", "13:1-10", "FIRSTBORN_MATZOT_TEACH",
             "קַדֶּשׁ־לִי … מַצּוֹת יֵאָכֵל … וְהִגַּדְתָּ לְבִנְךָ",
             "kadesh-li … matzot ye'akhel … ve-higadta le-vinkha",
             "Sanctify firstborn; remember exit; matzot seven; tell son; sign on hand; memorial between eyes."),
            ("STEP_E13a_B1", "13:11-16", "REDEEM_FIRSTBORN",
             "וְהַעֲבַרְתָּ … פֶּטֶר חֲמֹר תִּפְדֶּה … וְכֹל בְּכוֹר אָדָם",
             "ve-ha'avarta … peter chamor tifdeh … ve-khol bekhor adam",
             "When in land: every womb-opener to YHWH; donkey redeem with lamb or break neck; human firstborn redeem; teaching for son; sign hand/eyes."),
        ],
        "states": [
            ("S_firstborn_sanctified", "Firstborn claim active"),
            ("S_signs_hand_eyes", "Hand/forehead memorial signs"),
        ],
        "exports": [
            ("EXPORT_sanctify_firstborn", "קַדֶּשׁ־לִי כָל־בְּכוֹר", "kadesh-li khol-bekhor", "Sanctify firstborn"),
            ("EXPORT_tefillin_seed", "אוֹת עַל־יָדְךָ", "ot al-yadekha", "Sign on hand (tefillin seed dual-track)"),
        ],
        "decision_hints": [
            ("IF firstborn of donkey", "THEN redeem with lamb OR break neck"),
            ("IF firstborn human son", "THEN redeem"),
        ],
    },
    {
        "id": "exo_13_route_pillar",
        "refs": "13:17-22",
        "ch_start": 13, "v_start": 17, "ch_end": 13, "v_end": 22,
        "title_en": "Route not Philistine; bones of Joseph; pillar cloud/fire (13:17–22)",
        "title_he": "עַמּוּד עָנָן — עַמּוּד אֵשׁ",
        "title_he_translit": "amud anan — amud esh",
        "title_he_en": "Pillar of cloud — pillar of fire",
        "depends_on": ["exo_13_firstborn_matzot"],
        "genre": "narrative_fsm",
        "mekh": "medium",
        "mekh_chapters": [13],
        "learn": (
            "(1) Not way of Philistines lest return. (2) Round by wilderness sea. "
            "(3) Joseph bones. (4) Pillar cloud day / fire night."
        ),
        "steps": [
            ("STEP_E13b_A1", "13:17-19", "ROUTE_JOSEPH",
             "לֹא־נָחָם אֱלֹהִים דֶּרֶךְ אֶרֶץ פְּלִשְׁתִּים … עַצְמוֹת יוֹסֵף",
             "lo-nacham Elohim derekh eretz pelishtim … atzmot yosef",
             "God not lead Philistine road; armed; bones of Joseph taken (Gen oath)."),
            ("STEP_E13b_B1", "13:20-22", "PILLARS",
             "סֻכֹּתָה אֵתָם … עַמּוּד עָנָן … עַמּוּד אֵשׁ",
             "sukkotah etam … amud anan … amud esh",
             "Succoth to Etham; YHWH goes before in pillar cloud by day and fire by night; does not remove."),
        ],
        "states": [
            ("S_route_wilderness", "Wilderness sea route chosen"),
            ("S_pillars_lead", "Cloud/fire pillars guide"),
        ],
        "exports": [
            ("EXPORT_pillar_cloud_fire", "עַמּוּד עָנָן / אֵשׁ", "amud anan / esh", "Guiding pillars"),
            ("EXPORT_joseph_bones", "עַצְמוֹת יוֹסֵף", "atzmot yosef", "Joseph bones carried"),
        ],
    },
    {
        "id": "exo_14_sea",
        "refs": "14:1-31",
        "ch_start": 14, "v_start": 1, "ch_end": 14, "v_end": 31,
        "title_en": "Sea crossing: trap, split, drown Egypt (14:1–31)",
        "title_he": "קְרִיעַת יַם־סוּף",
        "title_he_translit": "keri'at yam-suf",
        "title_he_en": "Splitting of the Sea of Reeds",
        "depends_on": ["exo_13_route_pillar"],
        "genre": "narrative_fsm",
        "mekh": "strong",
        "mekh_chapters": [14],
        "learn": (
            "(1) Camp by sea; Pharaoh pursues. (2) Fear; stand see salvation. "
            "(3) Staff split sea; wall of water; Egypt follow. (4) Waters return; Israel faith."
        ),
        "steps": [
            ("STEP_E14_A1", "14:1-14", "TRAP_FEAR",
             "לִפְנֵי פִּי הַחִירֹת … מַה־תִּצְעַק … הִתְיַצְּבוּ וּרְאוּ",
             "lifnei pi ha-chirot … mah-titz'ak … hityatzvu u-re'u",
             "Camp instructions; Pharaoh pursues; Israel fears; stand and see YHWH salvation; YHWH will fight."),
            ("STEP_E14_B1", "14:15-25", "SPLIT_CROSS",
             "הָרֵם אֶת־מַטְּךָ … וַיִּבָּקְעוּ הַמָּיִם … חוֹמָה",
             "harem et-mattekha … va-yibake'u ha-mayim … chomah",
             "Lift staff; east wind; sea splits; dry ground; walls of water; angel/cloud moves; Egypt troubled."),
            ("STEP_E14_C1", "14:26-31", "WATERS_RETURN",
             "נְטֵה … וַיָּשֻׁבוּ הַמַּיִם … וַיַּאֲמִינוּ בַּיהוָה",
             "nete … va-yashuvu ha-mayim … va-ya'aminu ba-YHWH",
             "Waters return; Egypt dead on shore; Israel see great hand; fear YHWH; believe in YHWH and Moses."),
        ],
        "states": [
            ("S_pursued", "Egypt pursues to sea"),
            ("S_sea_split", "Israel on dry ground"),
            ("S_egypt_drowned", "Egypt destroyed; faith"),
        ],
        "exports": [
            ("EXPORT_sea_salvation", "יְשׁוּעַת יְהוָה", "yeshu'at YHWH", "YHWH salvation at sea"),
            ("EXPORT_believe_moses", None, None, "People believe in YHWH and Moses"),
        ],
    },
    {
        "id": "exo_15_song",
        "refs": "15:1-21",
        "ch_start": 15, "v_start": 1, "ch_end": 15, "v_end": 21,
        "title_en": "Song of the Sea; Miriam's chorus (15:1–21)",
        "title_he": "אָז יָשִׁיר מֹשֶׁה",
        "title_he_translit": "az yashir moshe",
        "title_he_en": "Then Moses sang",
        "depends_on": ["exo_14_sea"],
        "genre": "narrative_fsm",
        "mekh": "strong",
        "mekh_chapters": [15],
        "learn": (
            "(1) Song: horse and rider; YHWH man of war; depths. "
            "(2) Peoples hear and melt; plant in mountain inheritance; sanctuary. "
            "(3) Miriam prophetess tambourine chorus."
        ),
        "steps": [
            ("STEP_E15a_A1", "15:1-18", "SONG_SEA",
             "אָשִׁירָה לַיהוָה … יְהוָה אִישׁ מִלְחָמָה … תְּבִאֵמוֹ וְתִטָּעֵמוֹ",
             "ashirah la-YHWH … YHWH ish milchamah … tevi'emo ve-titta'emo",
             "Song of the Sea: triumph over horse/rider; warrior; enemy sunk; nations tremble; bring plant sanctuary; YHWH reigns forever."),
            ("STEP_E15a_B1", "15:19-21", "MIRIAM",
             "מִרְיָם הַנְּבִיאָה … שִׁירוּ לַיהוָה",
             "miryam ha-nevi'ah … shiru la-YHWH",
             "Miriam prophetess with tambourines; answer: sing to YHWH for he is highly exalted."),
        ],
        "states": [
            ("S_song_sung", "Sea song performed"),
            ("S_miriam_chorus", "Miriam leads women"),
        ],
        "exports": [
            ("EXPORT_song_of_sea", "שִׁירַת הַיָּם", "shirat ha-yam", "Song of the Sea"),
            ("EXPORT_sanctuary_plant_seed", "מָכוֹן לְשִׁבְתְּךָ", "makhon le-shivtekha", "Sanctuary dwelling seed in song"),
        ],
    },
    {
        "id": "exo_15_marah",
        "refs": "15:22-27",
        "ch_start": 15, "v_start": 22, "ch_end": 15, "v_end": 27,
        "title_en": "Marah bitter water; statute and ordinance; Elim (15:22–27)",
        "title_he": "מָרָה — חֹק וּמִשְׁפָּט",
        "title_he_translit": "marah — chok u-mishpat",
        "title_he_en": "Marah — statute and ordinance",
        "depends_on": ["exo_15_song"],
        "genre": "narrative_fsm",
        "mekh": "strong",
        "mekh_chapters": [15],
        "learn": (
            "(1) Three days no water; Marah bitter; tree sweetens. "
            "(2) Statute/ordinance; if heed no Egypt diseases. (3) Elim twelve springs seventy palms."
        ),
        "steps": [
            ("STEP_E15b_A1", "15:22-26", "MARAH_STATUTE",
             "וַיָּבֹאוּ מָרָתָה … וַיּוֹרֵהוּ עֵץ … חֹק וּמִשְׁפָּט",
             "va-yavo'u maratah … va-yorehu etz … chok u-mishpat",
             "Bitter water; people grumble; tree cast; waters sweet; there he set statute and ordinance and tested; heal if obey."),
            ("STEP_E15b_B1", "15:27", "ELIM",
             "אֵילִמָה … שְׁתֵּים עֶשְׂרֵה עֵינֹת … שִׁבְעִים תְּמָרִים",
             "elimah … shteim esreh einot … shiv'im temarim",
             "Elim: twelve springs, seventy palms; camp there."),
        ],
        "states": [
            ("S_marah_healed", "Water sweetened; statute set"),
            ("S_elim_camp", "Camp at Elim"),
        ],
        "exports": [
            ("EXPORT_chok_mishpat_marah", "חֹק וּמִשְׁפָּט", "chok u-mishpat", "Statute and ordinance seed at Marah"),
        ],
    },
    {
        "id": "exo_16_manna_shabbat",
        "refs": "16:1-36",
        "ch_start": 16, "v_start": 1, "ch_end": 16, "v_end": 36,
        "title_en": "Manna and quail; double Friday; Shabbat rest (16:1–36)",
        "title_he": "מָן — שַׁבָּתוֹן",
        "title_he_translit": "man — shabbaton",
        "title_he_en": "Manna — sabbath rest",
        "depends_on": ["exo_15_marah"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [16],
        "learn": (
            "(1) Grumble; bread from heaven test. (2) Quail evening; manna morning. "
            "(3) Omer measure; no leftover except Friday double. (4) Shabbat no gather; jar memorial."
        ),
        "steps": [
            ("STEP_E16_A1", "16:1-15", "MANNA_QUAIL",
             "בֹּאוּ אֶל־מִדְבַּר סִין … לֶחֶם מִן־הַשָּׁמָיִם … מָן הוּא",
             "bo'u el-midbar sin … lechem min-ha-shamayim … man hu",
             "Wilderness of Sin; grumble; glory appears; quail and manna; what is it — man."),
            ("STEP_E16_B1", "16:16-27", "OMER_DOUBLE_SHABBAT",
             "עֹמֶר לַגֻּלְגֹּלֶת … בַּיּוֹם הַשִּׁשִּׁי לֶחֶם מִשְׁנֶה … שַׁבָּתוֹן",
             "omer la-gulgolet … ba-yom ha-shishi lechem mishneh … shabbaton",
             "Omer each; leftover breeds worms; Friday double; seventh day rest holy Shabbat; some go out find none."),
            ("STEP_E16_C1", "16:28-36", "JAR_MEMORIAL",
             "עַד־אָנָה מֵאַנְתֶּם … צִנְצֶנֶת … לְדֹרֹתֵיכֶם",
             "ad-anah me'antem … tzintzenet … le-doroteikhem",
             "How long refuse mitzvot; eat Shabbat portion; jar of man before testimony; forty years; omer tenth ephah."),
        ],
        "states": [
            ("S_manna_given", "Daily manna regime"),
            ("S_shabbat_manna_rule", "Double Friday / no seventh gather"),
        ],
        "exports": [
            ("EXPORT_manna", "מָן", "man", "Manna bread from heaven"),
            ("EXPORT_shabbat_manna", "שַׁבָּתוֹן", "shabbaton", "Shabbat rest via manna rules"),
        ],
        "decision_hints": [
            ("IF day 1-5", "THEN gather daily omer; none left overnight"),
            ("IF day 6", "THEN double portion; keep overnight ok"),
            ("IF day 7", "THEN do not gather; eat stored"),
        ],
    },
    {
        "id": "exo_17_water_amalek",
        "refs": "17:1-16",
        "ch_start": 17, "v_start": 1, "ch_end": 17, "v_end": 16,
        "title_en": "Water from rock; Amalek war; hands of Moses (17:1–16)",
        "title_he": "מַסָּה וּמְרִיבָה — עֲמָלֵק",
        "title_he_translit": "massah u-merivah — amalek",
        "title_he_en": "Massah and Meribah — Amalek",
        "depends_on": ["exo_16_manna_shabbat"],
        "genre": "narrative_fsm",
        "mekh": "strong",
        "mekh_chapters": [17],
        "learn": (
            "(1) No water; Massah/Meribah; staff rock water. "
            "(2) Amalek fights; Joshua; hands up/down. (3) Write memorial; war YHWH vs Amalek."
        ),
        "steps": [
            ("STEP_E17_A1", "17:1-7", "ROCK_WATER",
             "תְּנוּ־לָנוּ מַיִם … מַסָּה וּמְרִיבָה … הֲיֵשׁ יְהוָה בְּקִרְבֵּנוּ",
             "tenu-lanu mayim … massah u-merivah … ha-yesh YHWH be-kirbenu",
             "No water Rephidim; quarrel; strike rock Horeb; Massah Meribah naming."),
            ("STEP_E17_B1", "17:8-16", "AMALEK",
             "וַיָּבֹא עֲמָלֵק … כַּאֲשֶׁר יָרִים מֹשֶׁה יָדוֹ … מִלְחָמָה לַיהוָה",
             "va-yavo amalek … ka'asher yarim moshe yado … milchamah la-YHWH",
             "Amalek war; Joshua fights; hands of Moses; write memorial; altar YHWH nissi; war with Amalek forever."),
        ],
        "states": [
            ("S_water_given", "Rock water at Massah/Meribah"),
            ("S_amalek_war", "Amalek conflict recorded"),
        ],
        "exports": [
            ("EXPORT_massah_meribah", "מַסָּה וּמְרִיבָה", "massah u-merivah", "Test and quarrel water site"),
            ("EXPORT_amalek_war", "עֲמָלֵק", "amalek", "Amalek perpetual war note"),
        ],
    },
    {
        "id": "exo_18_yitro",
        "refs": "18:1-27",
        "ch_start": 18, "v_start": 1, "ch_end": 18, "v_end": 27,
        "title_en": "Jethro arrives; judges hierarchy (18:1–27)",
        "title_he": "יִתְרוֹ — שָׂרֵי אֲלָפִים",
        "title_he_translit": "yitro — sarei alafim",
        "title_he_en": "Jethro — chiefs of thousands",
        "depends_on": ["exo_17_water_amalek"],
        "genre": "narrative_fsm",
        "mekh": "strong",
        "mekh_chapters": [18],
        "learn": (
            "(1) Jethro hears; brings Zipporah/sons; blessed be YHWH. "
            "(2) Moses judges alone; Jethro: teach statutes; appoint chiefs of thousands/hundreds/fifties/tens."
        ),
        "steps": [
            ("STEP_E18_A1", "18:1-12", "JETHRO_ARRIVES",
             "וַיִּשְׁמַע יִתְרוֹ … בָּרוּךְ יְהוָה … עֹלָה וּזְבָחִים",
             "va-yishma yitro … barukh YHWH … olah u-zevachim",
             "Jethro hears; reunites family; Moses recounts; Jethro rejoices blesses YHWH; sacrifice; Aaron elders eat bread."),
            ("STEP_E18_B1", "18:13-27", "JUDGES_SYSTEM",
             "לֹא־טוֹב הַדָּבָר … שָׂרֵי אֲלָפִים … וְהָקֵל מֵעָלֶיךָ",
             "lo-tov ha-davar … sarei alafim … ve-hakel me-alekha",
             "All-day judging bad; teach laws; able men fear God; hierarchy; hard cases to Moses; Jethro returns."),
        ],
        "states": [
            ("S_jethro_joined", "Jethro blesses YHWH"),
            ("S_courts_delegated", "Judge hierarchy installed"),
        ],
        "exports": [
            ("EXPORT_judge_hierarchy", "שָׂרֵי אֲלָפִים", "sarei alafim", "Delegated court system"),
        ],
    },
    {
        "id": "exo_19_sinai_prep",
        "refs": "19:1-25",
        "ch_start": 19, "v_start": 1, "ch_end": 19, "v_end": 25,
        "title_en": "Sinai arrival: treasure people; three days; bounds (19:1–25)",
        "title_he": "סְגֻלָּה — הַר סִינַי",
        "title_he_translit": "segulah — har sinai",
        "title_he_en": "Treasured possession — Mount Sinai",
        "depends_on": ["exo_18_yitro"],
        "genre": "narrative_fsm",
        "mekh": "primary",
        "mekh_chapters": [19],
        "learn": (
            "(1) Third month; if heed — segulah kingdom of priests holy nation. "
            "(2) Three-day prep; wash; bounds; death if touch. (3) Thunder smoke; Moses goes up."
        ),
        "steps": [
            ("STEP_E19_A1", "19:1-8", "SEGULAH_OFFER",
             "אַתֶּם רְאִיתֶם … סְגֻלָּה … מַמְלֶכֶת כֹּהֲנִים … נַעֲשֶׂה",
             "atem re'item … segulah … mamlekhet kohanim … na'aseh",
             "Sinai wilderness; if heed covenant then treasure; kingdom of priests; people answer we will do."),
            ("STEP_E19_B1", "19:9-15", "THREE_DAY_PREP",
             "הֱיוּ נְכֹנִים לִשְׁלֹשֶׁת יָמִים … הַגְבֵּל … אַל־תִּגְּשׁוּ",
             "heyu nekhonom li-sheloshet yamim … hagbel … al-tigshu",
             "Cloud so people hear; consecrate; wash garments; bounds; no touch mountain; no approach woman."),
            ("STEP_E19_C1", "19:16-25", "THEOPHANY_BOUNDS",
             "קֹלֹת וּבְרָקִים … עָשָׁן … קוֹל שֹׁפָר … רֶד הָעֵד",
             "kolot u-verakim … ashan … kol shofar … red ha'ed",
             "Third day thunder lightning cloud shofar; Moses speaks God answers; warn not break through; priests consecrate; Aaron with Moses."),
        ],
        "states": [
            ("S_segulah_accepted", "People accept covenant offer"),
            ("S_bounds_set", "Mountain bounds active"),
            ("S_ready_decalogue", "Ready for words of ch.20"),
        ],
        "exports": [
            ("EXPORT_segulah", "סְגֻלָּה", "segulah", "Treasured people status"),
            ("EXPORT_kingdom_priests", "מַמְלֶכֶת כֹּהֲנִים", "mamlekhet kohanim", "Kingdom of priests"),
        ],
    },
    {
        "id": "exo_20_decalogue_altar",
        "refs": "20:1-26",
        "ch_start": 20, "v_start": 1, "ch_end": 20, "v_end": 26,
        "title_en": "Ten Words; fear; altar of earth/stone (20:1–26)",
        "title_he": "עֲשֶׂרֶת הַדְּבָרִים — מִזְבַּח אֲדָמָה",
        "title_he_translit": "aseret ha-devarim — mizbach adamah",
        "title_he_en": "The Ten Words — altar of earth",
        "depends_on": ["exo_19_sinai_prep"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [20],
        "learn": (
            "(1) Ten Words: no other gods; idol; name; Shabbat; parents; murder; adultery; steal; false witness; covet. "
            "(2) People fear; Moses mediates. (3) Altar earth/uncut stone; no steps nakedness."
        ),
        "steps": [
            ("STEP_E20_A1", "20:1-14", "TEN_WORDS",
             "אָנֹכִי יְהוָה … לֹא יִהְיֶה … שַׁבָּת … לֹא תִרְצָח",
             "anokhi YHWH … lo yihyeh … shabbat … lo tirtzach",
             "Ten Words spoken; exclusive loyalty; Shabbat; social prohibitions."),
            ("STEP_E20_B1", "20:15-18", "FEAR_MEDIATE",
             "וַיַּרְא הָעָם … דַּבֵּר־אַתָּה … לְבַעֲבוּר נַסּוֹת",
             "va-yar ha-am … dabber-attah … le-va'avur nasot",
             "People fear thunder; stand far; Moses draws near; God tests so fear of him be on faces."),
            ("STEP_E20_C1", "20:19-26", "ALTAR_RULES",
             "מִזְבַּח אֲדָמָה … אֲבָנִים … לֹא־תִבְנֶה גָזִית … לֹא־תַעֲלֶה בְמַעֲלֹת",
             "mizbach adamah … avanim … lo-tivneh gazit … lo-ta'aleh be-ma'alot",
             "Altar of earth; if stones not hewn; no steps lest nakedness exposed."),
        ],
        "states": [
            ("S_decalogue_given", "Ten Words public"),
            ("S_mediate_fear", "People request mediation"),
            ("S_altar_rules", "Simple altar rules given"),
        ],
        "exports": [
            ("EXPORT_ten_words", "עֲשֶׂרֶת הַדְּבָרִים", "aseret ha-devarim", "Ten Words"),
            ("EXPORT_altar_earth", "מִזְבַּח אֲדָמָה", "mizbach adamah", "Earth altar"),
        ],
        "decision_hints": [
            ("IF altar of stones", "THEN do not build with hewn stone (gazit)"),
            ("IF approach altar", "THEN no steps exposing nakedness"),
        ],
    },
    {
        "id": "exo_21_slave_person",
        "refs": "21:1-27",
        "ch_start": 21, "v_start": 1, "ch_end": 21, "v_end": 27,
        "title_en": "Mishpatim open: Hebrew slave; homicide; injury; eye (21:1–27)",
        "title_he": "וְאֵלֶּה הַמִּשְׁפָּטִים — עֶבֶד עִבְרִי",
        "title_he_translit": "ve-eleh ha-mishpatim — eved ivri",
        "title_he_en": "And these are the judgments — Hebrew slave",
        "depends_on": ["exo_20_decalogue_altar"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [21],
        "learn": (
            "Case law open: slave terms; death/asylum; parent strike/curse; fight injury; slave eye/tooth free. Mekhilta heavy."
        ),
        "steps": [
            ("STEP_E21a_A1", "21:1-11", "SLAVE_RULES",
             "כִּי תִקְנֶה עֶבֶד עִבְרִי … בְּאַפָּהּ … שְׁאֵרָהּ כְּסוּתָהּ",
             "ki tikneh eved ivri … be-appah … she'erah kesutah",
             "Hebrew slave six years; forever at door; daughter sale rules; food clothing conjugal rights."),
            ("STEP_E21a_B1", "21:12-21", "HOMICIDE_STRIKE",
             "מַכֵּה אִישׁ וָמֵת … עָרֵי מִקְלָט … מַכֵּה אָבִיו",
             "makkeh ish va-met … arei miklat … makkeh aviv",
             "Killer dies; asylum for accident; parent strike/curse death; kidnap death; slave survive day — not avenged as free."),
            ("STEP_E21a_C1", "21:22-27", "INJURY_EYE",
             "וְכִי־יִנָּצוּ … עַיִן תַּחַת עַיִן … שֵׁן עַבְדּוֹ",
             "ve-khi-yinatzu … ayin tachat ayin … shen avdo",
             "Fight miscarriage fine; life for life eye for eye; slave eye/tooth → free."),
        ],
        "states": [
            ("S_mishpatim_open", "Case-law registry open"),
            ("S_person_injury_rules", "Person-harm cases loaded"),
        ],
        "exports": [
            ("EXPORT_mishpatim", "הַמִּשְׁפָּטִים", "ha-mishpatim", "Judgments case registry"),
            ("EXPORT_eye_for_eye", "עַיִן תַּחַת עַיִן", "ayin tachat ayin", "Measure-for-measure injury"),
        ],
        "decision_hints": [
            ("IF Hebrew slave six years served", "THEN go free in seventh"),
            ("IF master blinds slave eye OR knocks tooth", "THEN slave goes free for eye/tooth"),
            ("IF strikes parent OR curses parent", "THEN death"),
        ],
    },
    {
        "id": "exo_21_ox_pit",
        "refs": "21:28-37",
        "ch_start": 21, "v_start": 28, "ch_end": 21, "v_end": 37,
        "title_en": "Ox goring; pit; ox vs ox; theft open (21:28–37)",
        "title_he": "שׁוֹר נַגָּח — בּוֹר",
        "title_he_translit": "shor naggach — bor",
        "title_he_en": "Goring ox — pit",
        "depends_on": ["exo_21_slave_person"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [21],
        "learn": "Goring ox first/second time; pit; ox kills ox; theft ox/sheep restitution — Mekhilta case decoder.",
        "steps": [
            ("STEP_E21b_A1", "21:28-32", "GORING_OX",
             "וְכִי־יִגַּח שׁוֹר … שׁוֹר נַגָּח הוּא … שְׁלֹשִׁים שְׁקָלִים",
             "ve-khi-yigach shor … shor naggach hu … sheloshim shekalim",
             "Ox kills person: stone ox; if known gorer warn owner — death or ransom; slave 30 shekels."),
            ("STEP_E21b_B1", "21:33-37", "PIT_OX_THEFT",
             "כִּי־יִפְתַּח אִישׁ בּוֹר … אוֹ־נוֹדַע … חֲמִשָּׁה בָקָר",
             "ki-yiftach ish bor … o-noda … chamishah vakar",
             "Open pit pays; ox kills ox live/dead split or full if known gorer; theft ox 5 cattle sheep 4."),
        ],
        "states": [
            ("S_animal_damage_rules", "Animal/pit damage cases"),
        ],
        "exports": [
            ("EXPORT_goring_ox", "שׁוֹר נַגָּח", "shor naggach", "Known goring ox rules"),
        ],
        "decision_hints": [
            ("IF ox gores person first time", "THEN ox stoned; owner clear"),
            ("IF known gorer and owner warned AND kills", "THEN ox and owner liable (death/ransom)"),
            ("IF steals ox AND slaughters/sells", "THEN repay five cattle"),
        ],
    },
    {
        "id": "exo_22_property_social",
        "refs": "22:1-30",
        "ch_start": 22, "v_start": 1, "ch_end": 22, "v_end": 30,
        "title_en": "Theft deposit injury; social protect; firstfruits (22:1–30)",
        "title_he": "גַּנָּב — גֵּר יָתוֹם אַלְמָנָה",
        "title_he_translit": "gannav — ger yatom almanah",
        "title_he_en": "Thief — sojourner orphan widow",
        "depends_on": ["exo_21_ox_pit"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [22],
        "learn": "Burglary; deposit; grazing fire; loans interest; ger/orphan/widow; first produce blood meat — Mekhilta.",
        "steps": [
            ("STEP_E22_A1", "22:1-14", "THEFT_DEPOSIT",
             "אִם־בַּמַּחְתֶּרֶת … כֶּסֶף אוֹ־כֵלִים … אִם־טָרֹף יִטָּרֵף",
             "im-ba-machteret … kesef o-kelim … im-tarof yitaref",
             "Tunnel thief; double restitution; deposit disputes oath; borrow/hire damage rules."),
            ("STEP_E22_B1", "22:15-26", "SOCIAL_PROTECT",
             "כִּי־יְפַתֶּה … גֵּר לֹא־תוֹנֶה … אַלְמָנָה וְיָתוֹם … חֲבֹל",
             "ki-yefateh … ger lo-toneh … almanah ve-yatom … chavol",
             "Seduction; sorceress; bestiality; sacrifice other gods; ger orphan widow; lend poor no interest; garment pledge return."),
            ("STEP_E22_C1", "22:27-30", "GOD_CHIEFS_FIRST",
             "אֱלֹהִים לֹא תְקַלֵּל … מְלֵאָתְךָ וְדִמְעֲךָ … טְרֵפָה",
             "elohim lo tekallel … mele'atkha ve-dim'akha … terefah",
             "Do not curse God or chief; first produce; firstborn sons; holy men; torn flesh to dogs."),
        ],
        "states": [
            ("S_property_cases", "Property/deposit cases"),
            ("S_social_protections", "Ger/orphan/widow/loan rules"),
        ],
        "exports": [
            ("EXPORT_ger_protect", "גֵּר לֹא־תוֹנֶה", "ger lo-toneh", "Do not wrong the sojourner"),
        ],
        "decision_hints": [
            ("IF thief found tunneling by day AND dies", "THEN no bloodguilt for defender (night different)"),
            ("IF lend to poor", "THEN no interest; return night garment pledge"),
        ],
    },
    {
        "id": "exo_23_justice_calendar",
        "refs": "23:1-19",
        "ch_start": 23, "v_start": 1, "ch_end": 23, "v_end": 19,
        "title_en": "Court ethics; sabbath year; three feasts; firstfruits (23:1–19)",
        "title_he": "לֹא תִשָּׂא שֵׁמַע שָׁוְא — שָׁלֹשׁ רְגָלִים",
        "title_he_translit": "lo tissa shema shav — shalosh regalim",
        "title_he_en": "Do not bear false report — three pilgrimage times",
        "depends_on": ["exo_22_property_social"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [23],
        "learn": "False report; majority; enemy animal; bribes; seventh year; Shabbat; three feasts; no blood/chametz; kid milk.",
        "steps": [
            ("STEP_E23a_A1", "23:1-9", "JUSTICE_ETHICS",
             "לֹא תִשָּׂא שֵׁמַע שָׁוְא … לֹא־תִהְיֶה אַחֲרֵי־רַבִּים … וְגֵר לֹא תִלְחָץ",
             "lo tissa shema shav … lo-tihyeh acharei-rabbim … ve-ger lo tilchatz",
             "False report; majority for evil; enemy ox; bribe blinds; do not oppress ger."),
            ("STEP_E23a_B1", "23:10-19", "CALENDAR_FEASTS",
             "וְשֵׁשׁ שָׁנִים … הַשְּׁבִיעִת … שָׁלֹשׁ רְגָלִים … לֹא־תְבַשֵּׁל גְּדִי",
             "ve-shesh shanim … ha-shevi'it … shalosh regalim … lo-tevashshel gedi",
             "Seventh year release land; Shabbat rest; three feasts; blood not with chametz; fat not overnight; firstfruits house; kid not in mother milk."),
        ],
        "states": [
            ("S_court_ethics", "Court ethics loaded"),
            ("S_calendar_feasts", "Seventh year + three feasts"),
        ],
        "exports": [
            ("EXPORT_three_regalim", "שָׁלֹשׁ רְגָלִים", "shalosh regalim", "Three pilgrimage festivals"),
            ("EXPORT_kid_milk", "לֹא־תְבַשֵּׁל גְּדִי בַּחֲלֵב אִמּוֹ", "lo-tevashshel gedi ba-chalav immo", "Kid in mother milk ban"),
        ],
        "decision_hints": [
            ("IF year 7 of land cycle", "THEN let land rest; poor eat"),
            ("IF festival", "THEN appear; not empty-handed pattern continues later"),
        ],
    },
    {
        "id": "exo_23_escort_land",
        "refs": "23:20-33",
        "ch_start": 23, "v_start": 20, "ch_end": 23, "v_end": 33,
        "title_en": "Angel escort; conquest bounds; no covenant with land gods (23:20–33)",
        "title_he": "הִנֵּה אָנֹכִי שֹׁלֵחַ מַלְאָךְ",
        "title_he_translit": "hineh anokhi sholeach mal'akh",
        "title_he_en": "Behold I send an angel",
        "depends_on": ["exo_23_justice_calendar"],
        "genre": "narrative_fsm",
        "mekh": "strong",
        "mekh_chapters": [23],
        "learn": "Angel before; heed voice; enemies; borders; no bow to gods; no covenant residents; snare.",
        "steps": [
            ("STEP_E23b_A1", "23:20-26", "ANGEL_BLESS",
             "מַלְאָךְ לְפָנֶיךָ … הִשָּׁמֶר מִפָּנָיו … וַעֲבַדְתֶּם אֶת־יְהוָה",
             "mal'akh lefanekha … hishamer mi-panav … va-avadtem et-YHWH",
             "Angel leads; name in him; if heed — enemy of enemies; serve YHWH; bread water bless; remove sickness."),
            ("STEP_E23b_B1", "23:27-33", "CONQUEST_BAN",
             "אֶת־אֵימָתִי … מְעַט מְעָט … לֹא־תִכְרֹת … פֶּן־יַחֲטִיאוּ",
             "et-eimati … me'at me'at … lo-tikhrot … pen-yachti'u",
             "Terror; hornet; little by little; bounds sea to desert; no covenant with them or gods; they shall not dwell — snare."),
        ],
        "states": [
            ("S_angel_escort", "Angel escort promised"),
            ("S_land_ban_covenant", "No covenant with land peoples/gods"),
        ],
        "exports": [
            ("EXPORT_angel_escort", "מַלְאָךְ לְפָנֶיךָ", "mal'akh lefanekha", "Guiding angel"),
        ],
    },
    {
        "id": "exo_24_covenant_ascent",
        "refs": "24:1-18",
        "ch_start": 24, "v_start": 1, "ch_end": 24, "v_end": 18,
        "title_en": "Covenant blood; na'aseh ve-nishma; Moses forty days (24:1–18)",
        "title_he": "נַעֲשֶׂה וְנִשְׁמָע — דַּם הַבְּרִית",
        "title_he_translit": "na'aseh ve-nishma — dam ha-berit",
        "title_he_en": "We will do and we will hear — blood of the covenant",
        "depends_on": ["exo_23_escort_land"],
        "genre": "narrative_fsm",
        "mekh": "medium",
        "mekh_chapters": [24],
        "learn": (
            "(1) Ascent elders. (2) Book of covenant read; na'aseh ve-nishma. "
            "(3) Blood people. (4) Sapphire pavement vision. (5) Moses 40 days cloud."
        ),
        "steps": [
            ("STEP_E24_A1", "24:1-8", "COVENANT_BLOOD",
             "סֵפֶר הַבְּרִית … נַעֲשֶׂה וְנִשְׁמָע … דַּם־הַבְּרִית",
             "sefer ha-berit … na'aseh ve-nishma … dam-ha-berit",
             "Build altar twelve pillars; offerings; read book; people: we will do and hear; blood on people — blood of covenant."),
            ("STEP_E24_B1", "24:9-18", "VISION_FORTY",
             "וַיִּרְאוּ אֵת אֱלֹהֵי יִשְׂרָאֵל … כְּמַעֲשֵׂה לִבְנַת הַסַּפִּיר … אַרְבָּעִים יוֹם",
             "va-yir'u et elohei yisrael … ke-ma'aseh livnat ha-sappir … arba'im yom",
             "Nobles see God; eat drink; Moses called up; cloud glory; six days; seventh call; forty days nights."),
        ],
        "states": [
            ("S_covenant_sealed", "Blood covenant sealed"),
            ("S_moses_on_mountain", "Moses 40 days — handoff mishkan specs"),
        ],
        "exports": [
            ("EXPORT_naaseh_nishma", "נַעֲשֶׂה וְנִשְׁמָע", "na'aseh ve-nishma", "We will do and we will hear"),
            ("EXPORT_dam_berit", "דַּם הַבְּרִית", "dam ha-berit", "Blood of the covenant"),
        ],
    },
]

# Phase C–E blocks (mishkan + calf + build) appended below for file size management
BLOCKS_CDE: list[dict[str, Any]] = [
    {
        "id": "exo_25_ark_table_menorah",
        "refs": "25:1-40",
        "ch_start": 25, "v_start": 1, "ch_end": 25, "v_end": 40,
        "title_en": "Terumah: gifts; ark; table; menorah (25:1–40)",
        "title_he": "וְיִקְחוּ־לִי תְּרוּמָה — אָרוֹן שֻׁלְחָן מְנֹרָה",
        "title_he_translit": "ve-yikchu-li terumah — aron shulchan menorah",
        "title_he_en": "Take for me a contribution — ark table menorah",
        "depends_on": ["exo_24_covenant_ascent"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Gifts list; make sanctuary dwell among them; ark keruvim; table bread; pure gold menorah pattern shown.",
        "steps": [
            ("STEP_E25_A1", "25:1-9", "TERUMAH_DWELL",
             "תְּרוּמָה … וְעָשׂוּ לִי מִקְדָּשׁ וְשָׁכַנְתִּי בְּתוֹכָם",
             "terumah … ve-asu li mikdash ve-shakhanti be-tokham",
             "Willing gifts materials; make sanctuary that I may dwell among them; make by the pattern."),
            ("STEP_E25_B1", "25:10-22", "ARK",
             "אֲרוֹן עֲצֵי שִׁטִּים … כַּפֹּרֶת … כְּרֻבִים",
             "aron atzei shittim … kapporet … keruvim",
             "Ark acacia gold; poles; testimony inside; kapporet keruvim; speak from between keruvim."),
            ("STEP_E25_C1", "25:23-40", "TABLE_MENORAH",
             "שֻׁלְחָן … לֶחֶם פָּנִים … מְנֹרַת זָהָב … כַּמַּרְאֶה",
             "shulchan … lechem panim … menorat zahav … ka-mar'eh",
             "Table showbread; menorah cups flowers; tongs; see and make by their pattern on the mountain."),
        ],
        "states": [
            ("S_mikdash_commanded", "Sanctuary dwell command"),
            ("S_furniture_specs_1", "Ark table menorah specified"),
        ],
        "exports": [
            ("EXPORT_mikdash_dwell", "מִקְדָּשׁ וְשָׁכַנְתִּי", "mikdash ve-shakhanti", "Sanctuary so I dwell among them"),
            ("EXPORT_pattern_mountain", "כְּתַבְנִיתָם", "ke-tavnitam", "Pattern shown on mountain"),
        ],
    },
    {
        "id": "exo_26_curtains_boards",
        "refs": "26:1-37",
        "ch_start": 26, "v_start": 1, "ch_end": 26, "v_end": 37,
        "title_en": "Tabernacle curtains, boards, veil, screen (26:1–37)",
        "title_he": "יְרִיעֹת — קְרָשִׁים — פָּרֹכֶת",
        "title_he_translit": "yeri'ot — kerashim — parokhet",
        "title_he_en": "Curtains — boards — veil",
        "depends_on": ["exo_25_ark_table_menorah"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Ten curtains; goats; skins; boards sockets; middle bar; veil holy of holies; entrance screen.",
        "steps": [
            ("STEP_E26_A1", "26:1-14", "CURTAINS_COVERS",
             "יְרִיעֹת שֵׁשׁ … עִזִּים … עֹרֹת אֵילִם … תְּחָשִׁים",
             "yeri'ot shesh … izzim … orot eilim … techashim",
             "Linen curtains cherubim; goat curtains; ram skins; tachash cover."),
            ("STEP_E26_B1", "26:15-30", "BOARDS",
             "קְּרָשִׁים … אַדָנִים … בְּרִיחַ הַתִּיכֹן",
             "kerashim … adanim … beriach ha-tikhon",
             "Acacia boards silver sockets; bars; middle bar through; raise by pattern."),
            ("STEP_E26_C1", "26:31-37", "VEIL_SCREEN",
             "פָּרֹכֶת … קֹדֶשׁ הַקֳּדָשִׁים … מָסָךְ",
             "parokhet … kodesh ha-kodashim … masakh",
             "Veil divides holy/most holy; ark behind veil; table north menorah south; entrance screen."),
        ],
        "states": [("S_structure_specs", "Shell and veil specified")],
        "exports": [
            ("EXPORT_parokhet", "פָּרֹכֶת", "parokhet", "Veil before most holy"),
            ("EXPORT_kodesh_kodashim", "קֹדֶשׁ הַקֳּדָשִׁים", "kodesh ha-kodashim", "Holy of holies zone"),
        ],
    },
    {
        "id": "exo_27_altar_court",
        "refs": "27:1-21",
        "ch_start": 27, "v_start": 1, "ch_end": 27, "v_end": 21,
        "title_en": "Outer altar; court; oil lamp eternal (27:1–21)",
        "title_he": "מִזְבַּח הָעֹלָה — חָצֵר — נֵר תָּמִיד",
        "title_he_translit": "mizbach ha-olah — chatzer — ner tamid",
        "title_he_en": "Burnt-offering altar — court — continual lamp",
        "depends_on": ["exo_26_curtains_boards"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Bronze altar horns; utensils; court hangings pillars; pure oil ner tamid by Aaron sons.",
        "steps": [
            ("STEP_E27_A1", "27:1-8", "BRONZE_ALTAR",
             "מִזְבֵּחַ עֲצֵי שִׁטִּים … נְחֹשֶׁת … כַּאֲשֶׁר הֶרְאָה",
             "mizbeach atzei shittim … nechoshet … ka'asher her'ah",
             "Altar five by five; horns; bronze grate poles; hollow boards as shown."),
            ("STEP_E27_B1", "27:9-19", "COURT",
             "חֲצַר הַמִּשְׁכָּן … קְלָעִים … אַדְנֵי נְחֹשֶׁת",
             "chatzer ha-mishkan … kela'im … adnei nechoshet",
             "Court hangings south north west east; gate screen; bronze sockets pegs."),
            ("STEP_E27_C1", "27:20-21", "NER_TAMID",
             "שֶׁמֶן זַיִת זָךְ … לְהַעֲלֹת נֵר תָּמִיד",
             "shemen zayit zakh … le-ha'alot ner tamid",
             "Pure beaten olive oil for continual lamp; tent of meeting outside veil; statute forever."),
        ],
        "states": [("S_court_altar", "Outer altar and court specified")],
        "exports": [
            ("EXPORT_ner_tamid", "נֵר תָּמִיד", "ner tamid", "Continual lamp"),
            ("EXPORT_mizbeach_nechoshet", "מִזְבַּח נְחֹשֶׁת", "mizbach nechoshet", "Bronze altar"),
        ],
    },
    {
        "id": "exo_28_priest_garments",
        "refs": "28:1-43",
        "ch_start": 28, "v_start": 1, "ch_end": 28, "v_end": 43,
        "title_en": "Priest garments: ephod, breastpiece, robe, tzitz (28:1–43)",
        "title_he": "בִּגְדֵי־קֹדֶשׁ — חֹשֶׁן אֵפוֹד",
        "title_he_translit": "bigdei-kodesh — choshen ephod",
        "title_he_en": "Holy garments — breastpiece ephod",
        "depends_on": ["exo_27_altar_court"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Aaron/sons for priesthood; holy garments; ephod stones; choshen mishpat Urim Tumim; bells; tzitz holy to YHWH; linen breeches.",
        "steps": [
            ("STEP_E28_A1", "28:1-14", "EPHOD",
             "אַהֲרֹן … בִּגְדֵי־קֹדֶשׁ … אֵפוֹד … אַבְנֵי־שֹׁהַם",
             "aharon … bigdei-kodesh … ephod … avnei-shoham",
             "Bring Aaron sons; holy garments glory beauty; ephod gold blue purple scarlet; onyx stones names of tribes."),
            ("STEP_E28_B1", "28:15-30", "CHOSHEN",
             "חֹשֶׁן מִשְׁפָּט … אַרְבָּעָה טוּרִים … אוּרִים וְתֻמִּים",
             "choshen mishpat … arba'ah turim … urim ve-tummim",
             "Breastpiece of judgment twelve stones; chains; Urim and Tumim on heart."),
            ("STEP_E28_C1", "28:31-43", "ROBE_TZITZ_LINEN",
             "מְעִיל … פַּעֲמֹן … צִּיץ … מִכְנְסֵי־בָד",
             "me'il … pa'amon … tzitz … mikhnesei-vad",
             "Blue robe pomegranates bells; gold plate Holy to YHWH; tunic turban sash; linen breeches; statute."),
        ],
        "states": [("S_priest_garments_spec", "Priest garment system specified")],
        "exports": [
            ("EXPORT_choshen_mishpat", "חֹשֶׁן מִשְׁפָּט", "choshen mishpat", "Breastpiece of judgment"),
            ("EXPORT_urim_tummim", "אוּרִים וְתֻמִּים", "urim ve-tummim", "Urim and Tumim"),
            ("EXPORT_kodesh_la-yhwh", "קֹדֶשׁ לַיהוָה", "kodesh la-YHWH", "Holy to YHWH plate"),
        ],
    },
    {
        "id": "exo_29_investiture",
        "refs": "29:1-46",
        "ch_start": 29, "v_start": 1, "ch_end": 29, "v_end": 46,
        "title_en": "Priest investiture seven days; daily tamid; dwell (29:1–46)",
        "title_he": "מִלֻּאִים — עֹלַת תָּמִיד",
        "title_he_translit": "millu'im — olat tamid",
        "title_he_en": "Ordination — continual burnt offering",
        "depends_on": ["exo_28_priest_garments"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Wash clothe anoint; bull rams milluim; seven days consecrate altar; daily lambs; meet dwell among Israel.",
        "steps": [
            ("STEP_E29_A1", "29:1-37", "MILLUIM",
             "לְקַדֵּשׁ אֹתָם … פַּר … אֵיל מִלֻּאִים … שִׁבְעַת יָמִים",
             "le-kadesh otam … par … eil millu'im … shiv'at yamim",
             "Ordination animals; blood ear thumb toe; wave; seven days atone altar most holy."),
            ("STEP_E29_B1", "29:38-46", "TAMID_DWELL",
             "שְׁנַיִם לַיּוֹם תָּמִיד … וְנֹעַדְתִּי שָׁמָּה … וְשָׁכַנְתִּי בְּתוֹךְ",
             "shenayim la-yom tamid … ve-no'adti shammah … ve-shakhanti be-tokh",
             "Two lambs daily continual; flour oil wine; meet at entrance; sanctify tent altar Aaron; dwell among Israel be their God."),
        ],
        "states": [("S_investiture_tamid", "Priest ordination + daily tamid")],
        "exports": [
            ("EXPORT_olat_tamid", "עֹלַת תָּמִיד", "olat tamid", "Continual burnt offering"),
            ("EXPORT_dwell_among", "וְשָׁכַנְתִּי בְּתוֹךְ בְּנֵי יִשְׂרָאֵל", "ve-shakhanti be-tokh benei yisrael", "I will dwell among Israel"),
        ],
    },
    {
        "id": "exo_30_incense_shekel",
        "refs": "30:1-38",
        "ch_start": 30, "v_start": 1, "ch_end": 30, "v_end": 38,
        "title_en": "Incense altar; census shekel; laver; oil; incense (30:1–38)",
        "title_he": "מִזְבַּח קְטֹרֶת — מַחֲצִית הַשֶּׁקֶל",
        "title_he_translit": "mizbach ketoret — machatzit ha-shekel",
        "title_he_en": "Incense altar — half-shekel",
        "depends_on": ["exo_29_investiture"],
        "genre": "decision_table",
        "mekh": "medium",
        "mekh_chapters": [30, 31],
        "learn": "Golden incense altar; atonement money half-shekel; bronze laver; anointing oil formula; incense formula — no private copy.",
        "steps": [
            ("STEP_E30_A1", "30:1-10", "INCENSE_ALTAR",
             "מִזְבַּח מִקְטַר קְטֹרֶת … בַּבֹּקֶר … דַּם הַחַטָּאת",
             "mizbeach miktar ketoret … ba-boker … dam ha-chatat",
             "Incense altar gold; morning evening incense; yearly blood atonement most holy."),
            ("STEP_E30_B1", "30:11-16", "HALF_SHEKEL",
             "כִּי תִשָּׂא … מַחֲצִית הַשֶּׁקֶל … כֹּפֶר נַפְשׁוֹ",
             "ki tissa … machatzit ha-shekel … kofer nafsho",
             "Census: each half-shekel atonement money rich not more poor not less; service tent; memorial."),
            ("STEP_E30_C1", "30:17-38", "LAVER_OIL_INCENSE",
             "כִּיּוֹר נְחֹשֶׁת … שֶׁמֶן מִשְׁחַת־קֹדֶשׁ … קְטֹרֶת",
             "kiyor nechoshet … shemen mishchat-kodesh … ketoret",
             "Laver wash lest die; holy anointing oil formula; incense spices; cut off if private perfume."),
        ],
        "states": [("S_shekel_incense", "Half-shekel + incense systems")],
        "exports": [
            ("EXPORT_machatzit_shekel", "מַחֲצִית הַשֶּׁקֶל", "machatzit ha-shekel", "Half-shekel atonement money"),
            ("EXPORT_shemen_mishchah", "שֶׁמֶן מִשְׁחַת־קֹדֶשׁ", "shemen mishchat-kodesh", "Holy anointing oil"),
        ],
        "decision_hints": [
            ("IF census count", "THEN each twenty-and-up gives half-shekel; rich=poor amount"),
            ("IF make private anointing oil or incense like holy", "THEN cut off"),
        ],
    },
    {
        "id": "exo_31_craftsmen_shabbat",
        "refs": "31:1-18",
        "ch_start": 31, "v_start": 1, "ch_end": 31, "v_end": 18,
        "title_en": "Bezalel Oholiab; Shabbat sign; tablets stone (31:1–18)",
        "title_he": "בְּצַלְאֵל — אַךְ אֶת־שַׁבְּתֹתַי",
        "title_he_translit": "betzalel — akh et-shabtotai",
        "title_he_en": "Bezalel — but my Sabbaths",
        "depends_on": ["exo_30_incense_shekel"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [31, 35],
        "learn": "Spirit-filled craftsmen for all work; keep Shabbat despite build; death for desecrate; two tablets stone finger of God.",
        "steps": [
            ("STEP_E31_A1", "31:1-11", "CRAFTSMEN",
             "בְּצַלְאֵל … רוּחַ אֱלֹהִים … אָהֳלִיאָב … כְּכֹל אֲשֶׁר־צִוִּיתִךָ",
             "betzalel … ruach Elohim … oholiav … ke-khol asher-tzivvitikha",
             "Bezalel filled wisdom understanding knowledge craft; Oholiab; all skilled; make all commanded."),
            ("STEP_E31_B1", "31:12-17", "SHABBAT_SIGN",
             "אַךְ אֶת־שַׁבְּתֹתַי … אוֹת … מְחַלְלֶיהָ מוֹת יוּמָת",
             "akh et-shabtotai … ot … mechalaleha mot yumat",
             "But keep my Sabbaths; sign forever; six days work seventh rest holy; desecrator death; cut off; YHWH made heaven earth rested."),
            ("STEP_E31_C1", "31:18", "TABLETS",
             "שְׁנֵי לֻחֹת הָעֵדֻת … כְּתֻבִים בְּאֶצְבַּע אֱלֹהִים",
             "shenei luchot ha-edut … ketuvim be-etzba Elohim",
             "When finished speaking: two tablets testimony stone written by finger of God."),
        ],
        "states": [
            ("S_craftsmen_named", "Bezalel/Oholiab authorized"),
            ("S_shabbat_over_build", "Shabbat outranks construction"),
            ("S_tablets_given", "Stone tablets received — handoff calf crisis"),
        ],
        "exports": [
            ("EXPORT_betzalel", "בְּצַלְאֵל", "betzalel", "Spirit-filled chief craftsman"),
            ("EXPORT_shabbat_build_priority", "אַךְ אֶת־שַׁבְּתֹתַי", "akh et-shabtotai", "Shabbat even while building"),
            ("EXPORT_luchot", "לֻחֹת הָעֵדֻת", "luchot ha-edut", "Tablets of the testimony"),
        ],
        "decision_hints": [
            ("IF building sanctuary AND day is Shabbat", "THEN rest; do not desecrate — death/cut-off stated"),
        ],
    },
    {
        "id": "exo_32_golden_calf",
        "refs": "32:1-35",
        "ch_start": 32, "v_start": 1, "ch_end": 32, "v_end": 35,
        "title_en": "Golden calf; tablets broken; Levites; plague (32:1–35)",
        "title_he": "עֵגֶל מַסֵּכָה",
        "title_he_translit": "egel massekhah",
        "title_he_en": "Molten calf",
        "depends_on": ["exo_31_craftsmen_shabbat"],
        "genre": "narrative_fsm",
        "mekh": "medium",
        "learn": "People demand gods; calf feast; YHWH anger; Moses intercedes; breaks tablets; grinds calf; who for YHWH; Levites kill; plague.",
        "steps": [
            ("STEP_E32_A1", "32:1-6", "CALF_MADE",
             "קוּם עֲשֵׂה־לָנוּ אֱלֹהִים … עֵגֶל מַסֵּכָה … וַיָּקֻמוּ לְצַחֵק",
             "kum aseh-lanu elohim … egel massekhah … va-yakumu le-tzachek",
             "Moses delayed; make gods; earrings calf; feast tomorrow to YHWH; rise to play."),
            ("STEP_E32_B1", "32:7-14", "INTERCEDE",
             "לֶךְ־רֵד … וְעַתָּה הַנִּיחָה לִּי … וַיִּנָּחֶם יְהוָה",
             "lekh-red … ve-attah hanichah li … va-yinachem YHWH",
             "Go down corrupted; stiff-necked; blot book threat; Moses intercedes; YHWH relents from planned destruction."),
            ("STEP_E32_C1", "32:15-29", "BREAK_LEVI",
             "וַיְשַׁבֵּר … וַיִּטְחַן … מִי לַיהוָה אֵלָי … מִלְאוּ יֶדְכֶם",
             "va-yeshabber … va-yitchan … mi la-YHWH elai … mil'u yedkhem",
             "Break tablets; grind calf water; Aaron excuse; who for YHWH — Levites; kill brothers; fill hand blessing."),
            ("STEP_E32_D1", "32:30-35", "ATONE_PLAGUE",
             "אוּלַי אֲכַפְּרָה … מְחֵנִי נָא … וַיִּגֹּף יְהוָה",
             "ulai akhapperah … mecheni na … va-yigof YHWH",
             "Moses seeks atonement; blot me; YHWH: who sinned blot; angel lead; plague on people."),
        ],
        "states": [
            ("S_calf_breach", "Covenant breach with calf"),
            ("S_tablets_broken", "First tablets broken"),
            ("S_levi_side", "Levites fill hand for YHWH"),
        ],
        "exports": [
            ("EXPORT_egel", "עֵגֶל מַסֵּכָה", "egel massekhah", "Golden calf breach"),
            ("EXPORT_levi_fill_hand", "מִלְאוּ יֶדְכֶם", "mil'u yedkhem", "Levites fill hand"),
        ],
    },
    {
        "id": "exo_33_presence",
        "refs": "33:1-23",
        "ch_start": 33, "v_start": 1, "ch_end": 33, "v_end": 23,
        "title_en": "Tent of meeting outside; favor; show glory (33:1–23)",
        "title_he": "אֹהֶל מוֹעֵד — הַרְאֵנִי נָא כְּבֹדֶךָ",
        "title_he_translit": "ohel mo'ed — har'eni na kevodekha",
        "title_he_en": "Tent of meeting — show me your glory",
        "depends_on": ["exo_32_golden_calf"],
        "genre": "narrative_fsm",
        "mekh": "medium",
        "learn": "Angel only; ornaments off; Moses tent outside camp; face to face; if your presence not go — do not bring us; cleft rock glory back.",
        "steps": [
            ("STEP_E33_A1", "33:1-11", "TENT_OUTSIDE",
             "לֹא אֶעֱלֶה בְּקִרְבְּךָ … אֹהֶל מוֹעֵד … פָּנִים אֶל־פָּנִים",
             "lo e'eleh be-kirbekha … ohel mo'ed … panim el-panim",
             "Go up to land; not in midst stiff-necked; tent outside; cloud pillar; speak face to face as friend; Joshua stays."),
            ("STEP_E33_B1", "33:12-23", "PRESENCE_GLORY",
             "אִם־אֵין פָּנֶיךָ הֹלְכִים … הַרְאֵנִי נָא כְּבֹדֶךָ … אֲחֹרָי",
             "im-ein panekha holkhim … har'eni na kevodekha … achorai",
             "Moses: presence must go; YHWH agrees favor; show glory — goodness name pass; see back not face."),
        ],
        "states": [
            ("S_presence_negotiated", "Presence will go with Israel"),
            ("S_glory_glimpse", "Back of glory granted"),
        ],
        "exports": [
            ("EXPORT_panim_go", "פָּנֶיךָ הֹלְכִים", "panekha holkhim", "Your presence goes"),
            ("EXPORT_ohel_outside", "אֹהֶל מוֹעֵד מִחוּץ", "ohel mo'ed mi-chutz", "Tent of meeting outside camp"),
        ],
    },
    {
        "id": "exo_34_second_tablets",
        "refs": "34:1-35",
        "ch_start": 34, "v_start": 1, "ch_end": 34, "v_end": 35,
        "title_en": "Second tablets; thirteen attributes; covenant renew; shining face (34:1–35)",
        "title_he": "לֻחֹת שֵׁנִית — יְהוָה יְהוָה אֵל רַחוּם",
        "title_he_translit": "luchot shenit — YHWH YHWH el rachum",
        "title_he_en": "Second tablets — YHWH YHWH God compassionate",
        "depends_on": ["exo_33_presence"],
        "genre": "narrative_fsm",
        "mekh": "medium",
        "mekh_chapters": [34],
        "learn": "Hew second tablets; name attributes; covenant: no asherot; feasts; firstborn; no milk kid; Moses face shines veil.",
        "steps": [
            ("STEP_E34_A1", "34:1-9", "ATTRIBUTES",
             "פְּסָל־לְךָ … יְהוָה יְהוָה אֵל רַחוּם וְחַנּוּן … סְלַח",
             "pesal-lekha … YHWH YHWH el rachum ve-channun … selach",
             "Second tablets; YHWH descends proclaims name attributes; Moses bows; forgive iniquity take as inheritance."),
            ("STEP_E34_B1", "34:10-26", "COVENANT_RENEW",
             "הִנֵּה אָנֹכִי כֹּרֵת בְּרִית … שָׁלֹשׁ פְּעָמִים … לֹא־תְבַשֵּׁל גְּדִי",
             "hineh anokhi koret berit … shalosh pe'amim … lo-tevashshel gedi",
             "Renew covenant wonders; no treaty land; smash altars; feasts; firstlings; three times year; kid milk ban restated."),
            ("STEP_E34_C1", "34:27-35", "FACE_SHINE",
             "כְּתָב־לְךָ … קָרַן עוֹר פָּנָיו … מַסְוֶה",
             "ketav-lekha … karan or panav … masveh",
             "Write these words; forty days; face radiates; veil when speaking people; remove before YHWH."),
        ],
        "states": [
            ("S_second_tablets", "Second tablets covenant"),
            ("S_face_veil", "Moses shining face / veil"),
        ],
        "exports": [
            ("EXPORT_thirteen_attributes", "יְהוָה יְהוָה אֵל רַחוּם וְחַנּוּן", "YHWH YHWH el rachum ve-channun", "Compassion attributes proclamation"),
            ("EXPORT_second_luchot", "לֻחֹת שֵׁנִית", "luchot shenit", "Second tablets"),
        ],
    },
    {
        "id": "exo_35_shabbat_donate",
        "refs": "35:1-29",
        "ch_start": 35, "v_start": 1, "ch_end": 35, "v_end": 29,
        "title_en": "Shabbat first; freewill gifts for mishkan (35:1–29)",
        "title_he": "שֵׁשֶׁת יָמִים תֵּעָשֶׂה מְלָאכָה — נְדִיב לֵב",
        "title_he_translit": "sheshet yamim te'aseh melakhah — nediv lev",
        "title_he_en": "Six days work is done — willing heart",
        "depends_on": ["exo_34_second_tablets"],
        "genre": "decision_table",
        "mekh": "primary",
        "mekh_chapters": [35],
        "learn": "Assemble: Shabbat death for work; kindling fire ban; then bring terumah free heart; men and women spin; rulers stones oil.",
        "steps": [
            ("STEP_E35a_A1", "35:1-3", "SHABBAT_FIRE",
             "שֵׁשֶׁת יָמִים … וּבַיּוֹם הַשְּׁבִיעִי … לֹא־תְבַעֲרוּ אֵשׁ",
             "sheshet yamim … u-va-yom ha-shevi'i … lo-teva'aru esh",
             "Six days work; seventh holy Shabbat death for worker; kindle no fire in dwellings."),
            ("STEP_E35a_B1", "35:4-29", "FREEWILL_GIFTS",
             "קְחוּ מֵאִתְּכֶם תְּרוּמָה … כָּל־נְדִיב לִבּוֹ … הֵבִיאוּ",
             "kechu me-ittkhem terumah … kol-nediv libbo … hevi'u",
             "Take contribution; every willing heart; materials listed; wise women spin; freewill for all work of tent."),
        ],
        "states": [
            ("S_shabbat_before_build", "Shabbat restated before construction"),
            ("S_gifts_flowing", "Freewill materials coming"),
        ],
        "exports": [
            ("EXPORT_no_fire_shabbat", "לֹא־תְבַעֲרוּ אֵשׁ", "lo-teva'aru esh", "No kindling fire on Shabbat dwellings"),
            ("EXPORT_nediv_lev", "נְדִיב לֵב", "nediv lev", "Willing heart donor"),
        ],
        "decision_hints": [
            ("IF Shabbat", "THEN no melakhah; no kindling fire in dwellings"),
            ("IF heart willing", "THEN bring terumah materials"),
        ],
    },
    {
        "id": "exo_35_36_work_start",
        "refs": "35:30-36:38",
        "ch_start": 35, "v_start": 30, "ch_end": 36, "v_end": 38,
        "title_en": "Bezalel called; too much gift; curtains boards built (35:30–36:38)",
        "title_he": "וַיֹּאמֶר מֹשֶׁה … הוֹתֵר",
        "title_he_translit": "va-yomer moshe … hoter",
        "title_he_en": "Moses said … leftover excess",
        "depends_on": ["exo_35_shabbat_donate"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Name Bezalel/Oholiab publicly; more than enough materials; stop bringing; build curtains boards veil as specified.",
        "steps": [
            ("STEP_E3536_A1", "35:30-35", "CALL_CRAFTSMEN",
             "רְאוּ קָרָא יְהוָה בְּשֵׁם … בְּצַלְאֵל … אָהֳלִיאָב",
             "re'u kara YHWH be-shem … betzalel … oholiav",
             "YHWH called Bezalel by name; filled spirit; teach; Oholiab; all wise-hearted."),
            ("STEP_E3536_B1", "36:1-7", "TOO_MUCH",
             "וְהַמְּלָאכָה הָיְתָה דַיָּם … וְהוֹתֵר",
             "ve-ha-melakhah hayetah dayyam … ve-hoter",
             "Work enough and excess; Moses proclaims: man and woman stop work of bringing; material restrained."),
            ("STEP_E3536_C1", "36:8-38", "BUILD_SHELL",
             "וַיַּעֲשׂוּ … יְרִיעֹת … קְרָשִׁים … פָּרֹכֶת … מָסָךְ",
             "va-ya'asu … yeri'ot … kerashim … parokhet … masakh",
             "Execute curtains boards bars veil screen — as commanded pattern."),
        ],
        "states": [("S_build_underway", "Construction execution started")],
        "exports": [
            ("EXPORT_enough_material", "דַיָּם וְהוֹתֵר", "dayyam ve-hoter", "Enough and leftover gifts"),
        ],
    },
    {
        "id": "exo_37_furniture_made",
        "refs": "37:1-29",
        "ch_start": 37, "v_start": 1, "ch_end": 37, "v_end": 29,
        "title_en": "Furniture made: ark table menorah incense altar oil (37:1–29)",
        "title_he": "וַיַּעַשׂ בְּצַלְאֵל אֶת־הָאָרֹן",
        "title_he_translit": "va-ya'as betzalel et-ha-aron",
        "title_he_en": "Bezalel made the ark",
        "depends_on": ["exo_35_36_work_start"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Execute ark keruvim table vessels menorah incense altar oil incense — matches ch.25/30 specs.",
        "steps": [
            ("STEP_E37_A1", "37:1-9", "ARK_MADE",
             "וַיַּעַשׂ … אֶת־הָאָרֹן … כַּפֹּרֶת … כְּרֻבִים",
             "va-ya'as … et-ha-aron … kapporet … keruvim",
             "Bezalel makes ark poles kapporet keruvim."),
            ("STEP_E37_B1", "37:10-24", "TABLE_MENORAH",
             "אֶת־הַשֻּׁלְחָן … אֶת־הַמְּנֹרָה",
             "et-ha-shulchan … et-ha-menorah",
             "Table vessels; menorah pure gold branches cups."),
            ("STEP_E37_C1", "37:25-29", "INCENSE_OIL",
             "אֶת־מִזְבַּח הַקְּטֹרֶת … שֶׁמֶן … קְטֹרֶת",
             "et-mizbach ha-ketoret … shemen … ketoret",
             "Incense altar; holy anointing oil; pure incense work of perfumer."),
        ],
        "states": [("S_furniture_built", "Core furniture executed")],
        "exports": [("EXPORT_furniture_done", None, None, "Ark table menorah incense made")],
    },
    {
        "id": "exo_38_court_inventory",
        "refs": "38:1-31",
        "ch_start": 38, "v_start": 1, "ch_end": 38, "v_end": 31,
        "title_en": "Bronze altar laver court; metals inventory (38:1–31)",
        "title_he": "מִזְבַּח הַנְּחֹשֶׁת — פְּקוּדֵי הַמִּשְׁכָּן",
        "title_he_translit": "mizbach ha-nechoshet — pekudei ha-mishkan",
        "title_he_en": "Bronze altar — accountings of the mishkan",
        "depends_on": ["exo_37_furniture_made"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Outer altar; laver from mirrors; court; Ithamar accounting; gold silver bronze weights; half-shekel census link.",
        "steps": [
            ("STEP_E38_A1", "38:1-20", "ALTAR_LAVER_COURT",
             "אֶת־מִזְבַּח הָעֹלָה … הַכִּיּוֹר … אֶת־הֶחָצֵר",
             "et-mizbach ha-olah … ha-kiyor … et-he-chatzer",
             "Bronze altar utensils; laver stands from mirrors of serving women; court hangings pillars."),
            ("STEP_E38_B1", "38:21-31", "INVENTORY",
             "אֵלֶּה פְקוּדֵי הַמִּשְׁכָּן … בֶּקַע לַגֻּלְגֹּלֶת … נְחֹשֶׁת",
             "eleh fekudei ha-mishkan … beka la-gulgolet … nechoshet",
             "Accountings by Ithamar; gold silver from census beka; bronze; sockets pillars pegs."),
        ],
        "states": [("S_court_accounted", "Court built; metals accounted")],
        "exports": [
            ("EXPORT_pekudei", "פְּקוּדֵי הַמִּשְׁכָּן", "pekudei ha-mishkan", "Mishkan inventory account"),
        ],
    },
    {
        "id": "exo_39_garments_done",
        "refs": "39:1-43",
        "ch_start": 39, "v_start": 1, "ch_end": 39, "v_end": 43,
        "title_en": "Priest garments made; all work brought; Moses blesses (39:1–43)",
        "title_he": "וַיַּעֲשׂוּ … כַּאֲשֶׁר צִוָּה יְהוָה — וַיְבָרֶךְ",
        "title_he_translit": "va-ya'asu … ka'asher tzivvah YHWH — va-yevarekh",
        "title_he_en": "They made … as YHWH commanded — and he blessed",
        "depends_on": ["exo_38_court_inventory"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": "Execute ephod choshen robe tzitz linen; refrain as YHWH commanded Moses (refrain); bring all; Moses sees blesses.",
        "steps": [
            ("STEP_E39_A1", "39:1-31", "GARMENTS_MADE",
             "בִּגְדֵי הַשְּׂרָד … אֵפוֹד … חֹשֶׁן … צִּיץ",
             "bigdei ha-serad … ephod … choshen … tzitz",
             "Service garments; ephod stones; breastpiece; robe bells; tunics; plate Holy to YHWH — as commanded."),
            ("STEP_E39_B1", "39:32-43", "PRESENT_BLESS",
             "וַתֵּכֶל כָּל־עֲבֹדַת … וַיַּרְא מֹשֶׁה … וַיְבָרֶךְ אֹתָם",
             "va-tekhel kol-avodat … va-yar moshe … va-yevarekh otam",
             "All mishkan work finished as commanded; bring to Moses; Moses sees they did it; blesses them."),
        ],
        "states": [("S_all_work_done", "All fabrications complete; blessed")],
        "exports": [
            ("EXPORT_work_complete", "וַתֵּכֶל כָּל־עֲבֹדַת", "va-tekhel kol-avodat", "All service of mishkan finished"),
            ("EXPORT_moses_bless_builders", None, None, "Moses blesses the makers"),
        ],
    },
    {
        "id": "exo_40_erect_fill",
        "refs": "40:1-38",
        "ch_start": 40, "v_start": 1, "ch_end": 40, "v_end": 38,
        "title_en": "Erect mishkan first month; anoint; glory fills; cloud guides (40:1–38)",
        "title_he": "בְּיוֹם הַחֹדֶשׁ הָרִאשׁוֹן — כְּבוֹד יְהוָה מָלֵא",
        "title_he_translit": "be-yom ha-chodesh ha-rishon — kevod YHWH male",
        "title_he_en": "On the first month day — glory of YHWH filled",
        "depends_on": ["exo_39_garments_done"],
        "genre": "boot_steps",
        "mekh": "thin",
        "learn": (
            "New year day one erect; place furniture; anoint; dress Aaron sons; cloud covers; glory fills; Moses cannot enter; cloud by day fire night for journeys — "
            "sanctuary free names resolved for Leviticus apps."
        ),
        "steps": [
            ("STEP_E40_A1", "40:1-16", "COMMAND_ERECT",
             "בְּיוֹם־הַחֹדֶשׁ הָרִאשׁוֹן … תָּקִים … וּמָשַׁחְתָּ",
             "be-yom-ha-chodesh ha-rishon … takim … u-mashachta",
             "First month day one raise mishkan; arrange ark veil table menorah incense altar laver court; anoint; dress priests; Moses does."),
            ("STEP_E40_B1", "40:17-33", "EXECUTE_ERECT",
             "בַּחֹדֶשׁ הָרִאשׁוֹן בַּשָּׁנָה הַשֵּׁנִית … וַיָּקֶם מֹשֶׁה",
             "ba-chodesh ha-rishon ba-shanah ha-shenit … va-yakem moshe",
             "Second year first month day one: Moses erects all; finishes work."),
            ("STEP_E40_C1", "40:34-38", "GLORY_CLOUD",
             "וַיְכַס הֶעָנָן … וּכְבוֹד יְהוָה מָלֵא … כִּי עֲנַן יְהוָה",
             "va-yekhas he-anan … u-khvod YHWH male … ki anan YHWH",
             "Cloud covers tent; glory fills mishkan; Moses cannot enter; when cloud lifts journey; fire by night; cloud of YHWH on mishkan in all journeys."),
        ],
        "states": [
            ("S_mishkan_standing", "Mishkan erected and anointed"),
            ("S_glory_filled", "Glory filled; cloud/fire travel mode"),
            ("S_ready_for_lev", "Free names ready for Leviticus applications"),
        ],
        "exports": [
            ("EXPORT_mishkan_filled", "כְּבוֹד יְהוָה מָלֵא אֶת־הַמִּשְׁכָּן", "kevod YHWH male et-ha-mishkan", "Glory filled the mishkan"),
            ("EXPORT_cloud_journey", "עֲנַן יְהוָה עַל־הַמִּשְׁכָּן", "anan YHWH al-ha-mishkan", "Cloud/fire travel signal"),
            ("EXPORT_lev_handoff", None, None, "Sanctuary install complete — Leviticus free names resolve"),
        ],
    },
]

ALL_BLOCKS = BLOCKS + BLOCKS_CDE


def yaml_quote(s: str) -> str:
    if s is None:
        return '""'
    if any(c in s for c in ':"\'\n#{}[]|&*>!%@`') or s == "" or s.strip() != s:
        return json.dumps(s, ensure_ascii=False)
    return s


def verse_list(ch_s: int, v_s: int, ch_e: int, v_e: int) -> list[tuple[int, int]]:
    out = []
    if ch_s == ch_e:
        for v in range(v_s, v_e + 1):
            out.append((ch_s, v))
        return out
    # first chapter
    # need max verses — use generous; parse will fail if missing
    # Better: walk until parse fails... we know counts
    counts = {
        1: 22, 2: 25, 3: 22, 4: 31, 5: 23, 6: 30, 7: 29, 8: 28, 9: 35, 10: 29,
        11: 10, 12: 51, 13: 22, 14: 31, 15: 27, 16: 36, 17: 16, 18: 27, 19: 25,
        20: 26, 21: 37, 22: 30, 23: 33, 24: 18, 25: 40, 26: 37, 27: 21, 28: 43,
        29: 46, 30: 38, 31: 18, 32: 35, 33: 23, 34: 35, 35: 35, 36: 38, 37: 29,
        38: 31, 39: 43, 40: 38,
    }
    for ch in range(ch_s, ch_e + 1):
        lo = v_s if ch == ch_s else 1
        hi = v_e if ch == ch_e else counts[ch]
        for v in range(lo, hi + 1):
            out.append((ch, v))
    return out


def map_step_for_verse(block: dict, ch: int, v: int) -> str:
    for sid, ref, *_ in block["steps"]:
        # ref like "3:1-6" or "35:30-35"
        m = re.match(r"(\d+):(\d+)-(\d+)", ref)
        if m:
            c, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if ch == c and a <= v <= b:
                return sid
        m2 = re.match(r"(\d+):(\d+)-(\d+):(\d+)", ref)
        if m2:
            c1, a, c2, b = map(int, m2.groups())
            if (ch, v) >= (c1, a) and (ch, v) <= (c2, b):
                return sid
        # multi chapter in ref rare in our data
    # fallback first/last step by position
    return block["steps"][0][0]


def role_for_plain(he_plain: str) -> tuple[str, str]:
    glue = {"את", "את־", "אל", "על", "מן", "מ", "ל", "ב", "כ", "ו", "ה", "של", "עם", "או", "אם", "כי", "גם", "רק", "אשר", "מ־", "ל־", "ב־", "כ־"}
    p = he_plain.replace("/", "").replace("־", "")
    # very rough
    if p in ("את", "אל", "על", "מן", "עם", "או", "אם", "כי", "גם", "אשר", "לא", "כל", "זה", "זו", "זאת"):
        return "glue", "glue"
    people = {"משה", "אהרן", "פרעה", "ישראל", "יעקב", "אברהם", "יצחק", "יוסף", "מרים", "יתרו", "בצלאל", "אהליאב"}
    if any(x in p for x in people):
        return "agent_or_person", "logic_bearing"
    places = {"מצרים", "מדין", "סיני", "חרב", "גשן", "ים", "רפידים", "סכות"}
    if any(x in p for x in places):
        return "person_or_place", "logic_bearing"
    return "logic_bearing_leaf", "logic_bearing"


def top_split_fields(tree: dict, words: list[dict]) -> dict:
    children = tree.get("children") or []
    if len(children) >= 2:
        left, right = children[0], children[1]
    elif len(children) == 1:
        left, right = children[0], {"he_span": "", "word_indices": []}
    else:
        left = right = {"he_span": tree.get("he_span", ""), "word_indices": tree.get("word_indices", [])}

    def arm(node: dict, side: str) -> dict:
        idxs = node.get("word_indices") or []
        he_span = node.get("he_span") or ""
        head_he = ""
        head_mark = ""
        head_i = idxs[-1] if idxs else 0
        if idxs:
            # prefer etnachta leaf if present in arm
            for i in idxs:
                w = words[i]
                if "etnachta" in (w.get("mark_en") or ""):
                    head_i = i
                    break
            else:
                head_i = idxs[-1]
            head_he = words[head_i]["he"]
            head_mark = words[head_i].get("mark_en") or ""
        return {
            "side": side,
            "head_he": head_he,
            "head_i": head_i,
            "head_mark": head_mark,
            "he_span": he_span,
        }

    return {"left": arm(left, "left"), "right": arm(right, "right")}


def mekh_samples(chapters: list[int], max_paras: int = 6) -> list[dict]:
    if not MEKH_EN.exists():
        return []
    with open(MEKH_EN, encoding="utf-8") as f:
        en = json.load(f)
    he_text = None
    if MEKH_HE.exists():
        with open(MEKH_HE, encoding="utf-8") as f:
            he_text = json.load(f)["text"]
    notes = []
    for ch in chapters:
        idx = ch - 1
        if idx < 0 or idx >= len(en["text"]):
            continue
        chap = en["text"][idx]
        if not chap:
            continue
        # chap is list of verses -> paragraphs
        count = 0
        for vi, verse_block in enumerate(chap):
            if not verse_block:
                continue
            paras = verse_block if isinstance(verse_block, list) else [verse_block]
            for pi, para in enumerate(paras):
                if not isinstance(para, str) or not para.strip():
                    continue
                he_snip = ""
                try:
                    if he_text and he_text[idx] and he_text[idx][vi]:
                        hp = he_text[idx][vi]
                        if isinstance(hp, list) and pi < len(hp) and isinstance(hp[pi], str):
                            he_snip = hp[pi][:200]
                        elif isinstance(hp, str):
                            he_snip = hp[:200]
                except Exception:
                    pass
                en_snip = re.sub(r"\s+", " ", para)[:400]
                notes.append({
                    "ch": ch,
                    "v": vi + 1,
                    "p": pi + 1,
                    "en": en_snip,
                    "he": he_snip,
                })
                count += 1
                if count >= max_paras:
                    break
            if count >= max_paras:
                break
    return notes


def emit_block(block: dict, only_id: Optional[str] = None) -> Path:
    if only_id and block["id"] != only_id:
        raise SystemExit(0)
    bid = block["id"]
    verses = verse_list(block["ch_start"], block["v_start"], block["ch_end"], block["v_end"])
    step_ids = [s[0] for s in block["steps"]]

    lines: list[str] = []
    lines.append(f"# =============================================================================")
    lines.append(f"# LOGIC UNIT: Exodus {block['refs']} — {block['title_en']}")
    lines.append(f"# Exodus thorough-block schedule ({block.get('mekh', 'thin')} Mekhilta)")
    lines.append(f"# =============================================================================")
    lines.append("# Experimental model — not binding religious law.")
    lines.append("")
    lines.append("meta:")
    lines.append(f'  id: "{bid}"')
    lines.append(f'  title_en: {yaml_quote(block["title_en"])}')
    lines.append(f'  title_he: {yaml_quote(block["title_he"])}')
    lines.append(f'  title_he_translit: {yaml_quote(block["title_he_translit"])}')
    lines.append(f'  title_he_en: {yaml_quote(block["title_he_en"])}')
    lines.append('  book_he: "שְׁמוֹת"')
    lines.append('  book_he_translit: "Shemot"')
    lines.append('  book_en: "Exodus"')
    lines.append(f'  refs: "{block["refs"]}"')
    lines.append("  data_paths_he:")
    lines.append('    - "Data/Exod.xml"')
    lines.append('  status: draft')
    lines.append("  confidence_overall: hypothesis")
    lines.append(f'  genre: "{block["genre"]}"')
    lines.append('  build_track: exodus_install')
    lines.append("  depends_on:")
    for d in block["depends_on"]:
        lines.append(f'    - "{d}"')
    lines.append("  owner_language_note: >")
    lines.append("    English for reading only. Hebrew is the derivation source.")
    lines.append("  oral_policy_note_en: >")
    mekh = block.get("mekh", "thin")
    if mekh in ("primary", "strong"):
        lines.append("    Law/spine block: Written first; open Mekhilta extensively dual-track;")
        lines.append("    never silent-merge. MH endpoints remain possible Oral.")
    else:
        lines.append("    Written first. Mekhilta thin or N/A for this narrative/install strip;")
        lines.append("    midrash/Bavli dual-track when named. Never silent-merge.")
    lines.append("")
    lines.append("derivation_log:")
    lines.append("  - step: A")
    lines.append('    name_en: "Block choice"')
    lines.append("    comment: >")
    lines.append(f"      Thorough block {block['refs']} ({len(verses)} verses). {block['learn']}")
    lines.append("    confidence: established")
    lines.append("  - step: B")
    lines.append('    name_en: "Trees"')
    lines.append("    comment: >")
    lines.append(f"      All verses Exod.{block['refs']} via taamim_tree_parse.py v1; full tree_ascii.")
    lines.append("    confidence: tested")
    lines.append('    tags: ["[HE-STRUCT]"]')
    lines.append("  - step: C")
    lines.append('    name_en: "Learnings"')
    lines.append("    comment: >")
    # wrap learn
    for chunk in re.findall(r".{1,100}(?:\s|$)", block["learn"]):
        lines.append(f"      {chunk.rstrip()}")
    lines.append("    confidence: tested")
    if mekh in ("primary", "strong", "medium"):
        lines.append("  - step: D")
        lines.append('    name_en: "Mekhilta dual-track"')
        lines.append("    comment: >")
        lines.append("      Sampled Mekhilta d'Rabbi Yishmael from local Data/mekhilta_* for this strip;")
        lines.append("      dual-track only; not merged into Written rules.")
        lines.append("    confidence: hypothesis")
        lines.append('    tags: ["[ORAL]"]')
    lines.append("")
    lines.append("boot_steps:")
    for i, (sid, ref, op, he, tr, en) in enumerate(block["steps"], 1):
        lines.append(f"  - id: {sid}")
        lines.append(f"    order: {i}")
        lines.append(f'    ref: "Exod.{ref}"')
        lines.append(f"    op: {op}")
        lines.append(f"    he: {yaml_quote(he)}")
        lines.append(f"    he_translit: {yaml_quote(tr)}")
        lines.append(f"    en: {yaml_quote(en)}")
        lines.append("    confidence: tested")
        lines.append('    source: "[HE-WRITTEN]"')
        lines.append("")

    if block.get("decision_hints"):
        lines.append("decision_table:")
        lines.append("  comment_en: >")
        lines.append("    Hypothesis IF/THEN edges from Written Hebrew case structure; not binding law.")
        lines.append("    Refine with Mekhilta dual-track on disputes.")
        lines.append("  rows:")
        for j, (ifr, thenr) in enumerate(block["decision_hints"], 1):
            lines.append(f"    - id: ROW_{j}")
            lines.append(f"      if_en: {yaml_quote(ifr)}")
            lines.append(f"      then_en: {yaml_quote(thenr)}")
            lines.append("      confidence: hypothesis")
            lines.append('      source: "[HE-WRITTEN]"')
        lines.append("")

    lines.append("state_machine:")
    lines.append(f'  comment_en: "FSM / install states for {bid}."')
    lines.append("  states:")
    for sid, en in block["states"]:
        lines.append(f"    - id: {sid}")
        lines.append(f"      en: {yaml_quote(en)}")
    lines.append("  transitions:")
    for i in range(len(block["states"]) - 1):
        a = block["states"][i][0]
        b = block["states"][i + 1][0]
        via = step_ids[min(i, len(step_ids) - 1)]
        lines.append(f"    - from: {a}")
        lines.append(f"      to: {b}")
        lines.append(f"      via: {via}")
    lines.append("")
    lines.append("state_after:")
    for sid, en in block["states"][-2:] if len(block["states"]) >= 2 else block["states"]:
        lines.append(f"  - id: AFTER_{sid}")
        lines.append(f"    en: {yaml_quote(en)}")
    lines.append("")
    lines.append("exports:")
    for item in block["exports"]:
        eid = item[0]
        he = item[1] if len(item) > 1 else None
        tr = item[2] if len(item) > 2 else None
        en = item[3] if len(item) > 3 else ""
        lines.append(f"  - id: {eid}")
        if he:
            lines.append(f"    he: {yaml_quote(he)}")
        if tr:
            lines.append(f"    he_translit: {yaml_quote(tr)}")
        lines.append(f"    en: {yaml_quote(en)}")
    lines.append("")
    lines.append("oral_notes:")
    lines.append("  - id: ORAL_policy")
    lines.append("    status: observation")
    lines.append(f'    work_en: "Block oral policy ({mekh})"')
    lines.append("    comment_en: >")
    if mekh in ("primary", "strong"):
        lines.append("      Prefer Mekhilta d'Rabbi Yishmael first among Oral for decode;")
        lines.append("      then MH + Bavli. Dual-track only.")
    else:
        lines.append("      Written install/narrative first; Mekhilta only if strip exists;")
        lines.append("      midrash/Bavli dual-track when named.")
    lines.append('    source: "[PROJECT]"')

    mekh_chs = block.get("mekh_chapters") or []
    if mekh in ("primary", "strong", "medium") and mekh_chs:
        samples = mekh_samples(mekh_chs, max_paras=8 if mekh == "primary" else 4)
        for i, s in enumerate(samples, 1):
            lines.append(f"  - id: ORAL_mekhilta_{i}")
            lines.append("    status: dual_track")
            lines.append('    work_en: "Mekhilta d\'Rabbi Yishmael"')
            lines.append(f'    locus_en: "Mekhilta on Exodus ~{s["ch"]}:{s["v"]} (Sefaria ch/v/para {s["ch"]}/{s["v"]}/{s["p"]})"')
            if s["he"]:
                lines.append(f"    he_sample: {yaml_quote(s['he'][:240])}")
                lines.append('    he_translit: "see Hebrew sample; full midrash in Data/mekhilta_he.json"')
            lines.append(f"    en_sample: {yaml_quote(s['en'][:400])}")
            lines.append("    comment_en: >")
            lines.append("      Dual-track sample — does not rewrite Written boot_steps/decision rows.")
            lines.append("      Open full Mekhilta locally for deeper case work on this block.")
            lines.append('    source: "[ORAL][MEKHILTA]"')
            lines.append("    confidence: hypothesis")
    else:
        lines.append("  - id: ORAL_possible")
        lines.append("    status: possible_oral")
        lines.append('    work_en: "Midrash / Bavli / MH endpoints (named when quoted)"')
        lines.append("    comment_en: Dual-track only; MH never ruled out.")
        lines.append('    source: "[ORAL]"')
    lines.append("")
    lines.append("scenarios:")
    for i, (sid, ref, op, *_) in enumerate(block["steps"], 1):
        lines.append(f"  - id: S{i}")
        lines.append(f'    title_en: "After {ref} ({op})"')
        lines.append(f'    expect_en: "State advances via {sid}; see boot_steps."')
    lines.append("")

    # Trees
    lines.append("binary_trees:")
    lines.append("  display_policy_en: >")
    lines.append("    Always he + he_translit + en. Full tree_ascii per verse.")
    lines.append("  method_note_en: >")
    lines.append("    taamim_tree_parse.py v1 on Data/Exod.xml.")
    lines.append('  data_source: "Data/Exod.xml"')
    lines.append('  parser: "taamim_tree_parse.py"')
    lines.append('  rule_set_version: "v1"')
    lines.append('  tags: ["[HE-STRUCT]"]')
    lines.append("  verse_trees:")

    coverage_blocks: list[str] = []
    word_total = 0
    for ch, v in verses:
        osis = f"Exod.{ch}.{v}"
        try:
            parsed = parse_verse(osis)
        except Exception as e:
            lines.append(f"    Exod_{ch}_{v}:")
            lines.append(f'      verse: "{ch}:{v}"')
            lines.append(f'      osis_id: "{osis}"')
            lines.append(f'      parser_status: error')
            lines.append(f"      error: {yaml_quote(str(e))}")
            continue
        words = parsed["words"]
        tree = parsed["tree"]
        status = parsed.get("status", "unique")
        ascii_t = tree_ascii_string(tree)
        plain_words = [w["he_plain"].replace("/", "") for w in words]
        linear_he = " ".join(plain_words)
        wc = len(words)
        word_total += wc
        pure = "true" if all(
            (len(n.get("children") or []) in (0, 2)) or n.get("kind") == "leaf"
            for n in [tree]
        ) else "false"
        # simpler pure_binary: check ascii for 3-ary
        pure = "false" if "3-ary" in ascii_t or "n-ary" in ascii_t else "true"
        step = map_step_for_verse(block, ch, v)
        ts = top_split_fields(tree, words)
        key = f"Exod_{ch}_{v}"
        lines.append(f"    {key}:")
        lines.append(f'      verse: "{ch}:{v}"')
        lines.append(f'      osis_id: "{osis}"')
        lines.append(f"      parser_status: {status}")
        lines.append(f"      pure_binary: {pure}")
        lines.append(f"      word_count: {wc}")
        lines.append("      linear:")
        lines.append(f"        he: {yaml_quote(linear_he)}")
        lines.append(f'        he_translit: {" ".join(f"w{i}" for i in range(wc))!r}')
        lines.append(
            f'        en: "Free gloss [EN-AID] — derive structure from Hebrew tree, not this gloss. Verse {ch}:{v}."'
        )
        lines.append(
            '        en_note: "Free gloss [EN-AID]. Translit leaf-indexed w0..; see tree_coverage."'
        )
        lines.append("      top_binary_split:")
        lines.append("        comment: >")
        lines.append(f"          Top split ta'amim v1; maps_to ['{step}'].")
        lines.append("        left_half:")
        lines.append('          side_en: "Left of top split"')
        lines.append("          head:")
        lines.append(f"            he: {yaml_quote(strip_taamim_and_points(ts['left']['head_he']) if ts['left']['head_he'] else '')}")
        lines.append(f'            he_translit: "w{ts["left"]["head_i"]}"')
        lines.append(f'            en: "left-end leaf {ts["left"]["head_i"]}"')
        lines.append(f"            mark_en: {yaml_quote(ts['left']['head_mark'])}")
        lines.append("          phrase:")
        lines.append(f"            he: {yaml_quote(ts['left']['he_span'][:200])}")
        lines.append('            he_translit: "left_arm"')
        lines.append('            en: "left phrase arm (see tree_ascii)"')
        lines.append("        right_half:")
        lines.append('          side_en: "Right of top split"')
        lines.append("          phrase:")
        lines.append(f"            he: {yaml_quote(ts['right']['he_span'][:200])}")
        lines.append('            he_translit: "right_arm"')
        lines.append('            en: "right phrase arm (see tree_ascii)"')
        lines.append("      tree_ascii: |")
        for al in ascii_t.splitlines():
            lines.append(f"        {al}")
        lines.append(f'      maps_to: ["{step}"]')
        lines.append("      confidence: tested")
        lines.append('      source: "[HE-STRUCT][HE-WRITTEN]"')
        lines.append("")

        # coverage
        cov = [f'  - ref: "{osis}"', "    words:"]
        for w in words:
            role, kind = role_for_plain(w["he_plain"])
            he_p = w["he_plain"].replace("/", "")
            cov.append(
                f'      - {{index: {w["index"]}, he: {yaml_quote(he_p)}, he_translit: "w{w["index"]}", '
                f'en: "leaf {w["index"]} ({he_p})", role: {role}, kind: {kind}, feeds: [{step}]}}'
            )
        coverage_blocks.append("\n".join(cov))

    lines.append("tree_coverage:")
    lines.append("  aspiration_en: >")
    lines.append("    100% word use; roles provisional heuristic pending TIR refinement.")
    lines.append(f"  word_total: {word_total}")
    lines.append("  verses:")
    for cb in coverage_blocks:
        lines.append(cb)

    lines.append("")
    lines.append("confidence: hypothesis")
    lines.append("status_note_en: >")
    lines.append("  Draft thorough-block unit for Exodus install track. Not binding religious law.")
    lines.append('  Trees tested via taamim_tree_parse v1; logic steps hypothesis/tested per comment.')

    out_path = UNITS / f"{bid}.yaml"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="Only this unit id")
    ap.add_argument("--from-id", help="Start from this id inclusive")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    if args.list:
        for b in ALL_BLOCKS:
            print(b["id"], b["refs"], b.get("mekh"))
        return
    started = args.from_id is None
    for b in ALL_BLOCKS:
        if args.only and b["id"] != args.only:
            continue
        if args.from_id and not started:
            if b["id"] == args.from_id:
                started = True
            else:
                continue
        print(f"NEXT: {b['id']} ({b['refs']}) mekh={b.get('mekh')} …", flush=True)
        path = emit_block(b)
        print(f"  wrote {path.relative_to(ROOT)}", flush=True)
        if args.only:
            break
    print("DONE schedule pass.", flush=True)


if __name__ == "__main__":
    main()
