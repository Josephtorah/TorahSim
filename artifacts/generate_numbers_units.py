#!/usr/bin/env python3
"""
Generate Numbers Pre-Code logic units (47-block schedule).
Trees via taamim_tree_parse; Sifrei Bamidbar dual-track samples from
Data/sifrei_bamidbar_he.json. Does not invent binding law.
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
SIFREI_HE = ROOT / "Data" / "sifrei_bamidbar_he.json"

# Hebrew/OSIS Num chapter lengths (Data/Num.xml)
COUNTS = {
    1: 54, 2: 34, 3: 51, 4: 49, 5: 31, 6: 27, 7: 89, 8: 26, 9: 23, 10: 36,
    11: 35, 12: 16, 13: 33, 14: 45, 15: 41, 16: 35, 17: 28, 18: 32, 19: 22, 20: 29,
    21: 35, 22: 41, 23: 30, 24: 25, 25: 19, 26: 65, 27: 23, 28: 31, 29: 39, 30: 17,
    31: 54, 32: 42, 33: 56, 34: 29, 35: 34, 36: 13,
}

SKIP_IDS: set[str] = set()


def B(
    id: str,
    refs: str,
    ch_s: int, v_s: int, ch_e: int, v_e: int,
    title_en: str,
    title_he: str,
    title_tr: str,
    title_he_en: str,
    depends: list[str],
    genre: str,
    sifrei: str,
    learn: str,
    steps: list[tuple],
    states: list[tuple],
    exports: list[tuple],
    decisions: Optional[list[tuple]] = None,
    imports_en: str = "Exod Tent/priests/cloud; Lev purity/korban types as background where used.",
) -> dict[str, Any]:
    return {
        "id": id,
        "refs": refs,
        "ch_start": ch_s, "v_start": v_s, "ch_end": ch_e, "v_end": v_e,
        "title_en": title_en,
        "title_he": title_he,
        "title_he_translit": title_tr,
        "title_he_en": title_he_en,
        "depends_on": depends,
        "genre": genre,
        "sifrei": sifrei,
        "learn": learn,
        "steps": steps,
        "states": states,
        "exports": exports,
        "decision_hints": decisions or [],
        "imports_en": imports_en,
    }


ALL_BLOCKS: list[dict[str, Any]] = [
    # Phase A
    B("num_01_census_command", "1:1-19", 1, 1, 1, 19,
      "Census command in wilderness; chiefs named (1:1–19)",
      "שְׂאוּ אֶת־רֹאשׁ", "se'u et-rosh", "Lift the head (take a census)",
      ["lev_27_vows_valuations", "exo_40_erect_fill"], "boot_steps", "thin",
      "Year 2 month 2 day 1: count males 20+ able war by tribe; one chief per tribe assists; Moses Aaron gather assembly day 1 of second month.",
      [
        ("STEP_N01A_A1", "1:1-4", "CENSUS_OPEN", "שְׂאוּ אֶת־רֹאשׁ … מִבֶּן עֶשְׂרִים", "se'u et-rosh … mi-ben esrim",
         "YHWH to Moses Tent of Meeting wilderness Sinai: count whole congregation by families houses; males head by head from 20 years up all go out to war; you and Aaron; with you one man per tribe each head of fathers house."),
        ("STEP_N01A_B1", "1:5-16", "CHIEFS_NAMED", "וְאֵלֶּה שְׁמוֹת … נְשִׂיאֵי", "ve-eleh shemot … nesi'ei",
         "Names of men who stand with you: Reuben Elizur … through Naphtali Ahira; these called of congregation princes of tribes of fathers heads of thousands of Israel."),
        ("STEP_N01A_C1", "1:17-19", "GATHER_COUNT", "וַיַּקֵּח … וַיַּפְקְדֵם", "va-yikkach … va-yifkedem",
         "Moses Aaron take these named men; assemble whole congregation day 1 of second month; declare births by families houses by name head by head; as YHWH commanded Moses so he counted them in Sinai wilderness."),
      ],
      [("S_census_open", "Census command open"), ("S_chiefs_ready", "Tribal chiefs listed and assembled")],
      [("EXPORT_se_u_rosh", "שְׂאוּ אֶת־רֹאשׁ", "se'u et-rosh", "Census of war-eligible males"),
       ("EXPORT_nasi_tribe", "נָשִׂיא", "nasi", "Tribal prince as census aide")],
      [("IF male 20+ able for war", "THEN include in census by tribe/family/house")]),
    B("num_01_tribe_counts", "1:20-46", 1, 20, 1, 46,
      "Tribe-by-tribe census totals (1:20–46)",
      "פְּקֻדֵיהֶם לְמַטֵּה", "pekudeihem le-matteh", "Their counted ones by tribe",
      ["num_01_census_command"], "boot_steps", "thin",
      "Each tribe: sons of X generations families houses males 20+ war; number N. Sum of all counted 603550.",
      [
        ("STEP_N01B_A1", "1:20-43", "TRIBE_ROLL", "בְּנֵי רְאוּבֵן … נַפְתָּלִי", "benei re'uven … naftali",
         "Roll of each tribe Reuben through Naphtali: family house male 20+ war count (Reuben 46500 … Naphtali 53400)."),
        ("STEP_N01B_B1", "1:44-46", "TOTAL_603550", "אֵלֶּה הַפְּקֻדִים … שֵׁשׁ־מֵאוֹת אֶלֶף", "eleh ha-pekudim … shesh-me'ot elef",
         "These are the counted whom Moses Aaron and twelve princes counted; all counted of Israel males 20+ war: 603550."),
      ],
      [("S_tribe_totals", "Twelve tribe war counts loaded"), ("S_total_603550", "Aggregate 603550")],
      [("EXPORT_pekudei_yisrael", "פְּקוּדֵי יִשְׂרָאֵל", "pekudei yisrael", "Census totals of Israel 603550")]),
    B("num_01_levites_exempt", "1:47-54", 1, 47, 1, 54,
      "Levites not in war census; camp charge of mishkan (1:47–54)",
      "וְהַלְוִיִּם לֹא הָתְפָּקְדוּ", "ve-ha-leviyyim lo hotpakdu", "And the Levites were not counted",
      ["num_01_tribe_counts", "exo_40_erect_fill"], "decision_table", "medium",
      "Levites not counted among them; appointed over mishkan of testimony: carry, serve, camp around; stranger approaching die; Israel camp by banner; Levites guard mishkan lest wrath.",
      [
        ("STEP_N01C_A1", "1:47-54", "LEVI_CHARGE", "וְהַלְוִיִּם … לֹא הָתְפָּקְדוּ … מִשְׁמֶרֶת", "ve-ha-leviyyim … lo hotpakdu … mishmeret",
         "Levites not counted among them as YHWH commanded; appoint Levites over mishkan of testimony all its vessels all that belongs: they carry serve camp around; when mishkan journeys Levites take it down; when camps Levites raise it; stranger who approaches die; Israel camp each by camp banner; Levites camp around mishkan of testimony that there be no wrath on congregation; Israel did all YHWH commanded Moses."),
      ],
      [("S_levi_exempt", "Levites outside war census"), ("S_mishkan_guard", "Levites guard mishkan")],
      [("EXPORT_levi_not_census", "לֹא הָתְפָּקְדוּ", "lo hotpakdu", "Levites not in war census"),
       ("EXPORT_mishmeret_mishkan", "מִשְׁמֶרֶת הַמִּשְׁכָּן", "mishmeret ha-mishkan", "Charge of the Tabernacle")],
      [("IF Levite", "THEN not in war census; appointed to mishkan carry/serve/guard"),
       ("IF stranger approaches mishkan service improperly", "THEN death")],
      imports_en="Exod 40 erect/fill mishkan; Lev priest office background."),
    B("num_02_camp_east_south", "2:1-16", 2, 1, 2, 16,
      "Camp layout: east Yehudah standard; south Reuben (2:1–16)",
      "אִישׁ עַל־דִּגְלוֹ", "ish al-diglo", "Each man by his standard",
      ["num_01_levites_exempt"], "boot_steps", "thin",
      "Camp by standard signs of fathers house facing Tent at distance. East: Yehudah Yissachar Zevulun (186400) first to journey. South: Reuben Shimon Gad (151450) second.",
      [
        ("STEP_N02A_A1", "2:1-9", "EAST_YEHUDAH", "אִישׁ עַל־דִּגְלוֹ … קֵדְמָה מִזְרָחָה", "ish al-diglo … kedmah mizrachah",
         "Camp each by standard signs of fathers house around Tent of Meeting at distance; east side sunrise: standard of camp of Yehudah by armies; Nachshon; Yissachar Nethanel; Zevulun Eliab; all counted of Yehudah camp 186400; they journey first."),
        ("STEP_N02A_B1", "2:10-16", "SOUTH_REUBEN", "דֶּגֶל מַחֲנֵה רְאוּבֵן … תֵּימָנָה", "degel machaneh re'uven … teimanah",
         "South: standard of Reuben; Elizur; Shimon Shelumiel; Gad Eliasaph; total Reuben camp 151450; second to journey."),
      ],
      [("S_east_camp", "East Yehudah triad set"), ("S_south_camp", "South Reuben triad set")],
      [("EXPORT_degel", "דֶּגֶל", "degel", "Tribal camp standard"),
       ("EXPORT_east_yehudah", "מַחֲנֵה יְהוּדָה", "machaneh yehudah", "Yehudah camp leads march")]),
    B("num_02_camp_west_north", "2:17-34", 2, 17, 2, 34,
      "Camp center Levites; west Ephraim; north Dan; march order (2:17–34)",
      "וְנָסַע אֹהֶל מוֹעֵד", "ve-nasa ohel mo'ed", "And the Tent of Meeting shall journey",
      ["num_02_camp_east_south"], "boot_steps", "thin",
      "Tent journeys with Levite camp mid-order. West: Ephraim Menasheh Binyamin (108100) third. North: Dan Asher Naphtali (157600) last. Total 603550; Levites not counted among them. Israel does as commanded.",
      [
        ("STEP_N02B_A1", "2:17", "OHEL_MID", "וְנָסַע אֹהֶל מוֹעֵד … בְּתוֹךְ", "ve-nasa ohel mo'ed … be-tokh",
         "Tent of Meeting journeys with camp of Levites mid the camps; as they camp so they journey each on his side by standards."),
        ("STEP_N02B_B1", "2:18-24", "WEST_EPHRAIM", "דֶּגֶל מַחֲנֵה אֶפְרַיִם יָמָּה", "degel machaneh efrayim yammah",
         "West: Ephraim Elishama; Menasheh Gamliel; Binyamin Avidan; total 108100; third to journey."),
        ("STEP_N02B_C1", "2:25-34", "NORTH_DAN_TOTAL", "דֶּגֶל מַחֲנֵה דָן צָפוֹנָה", "degel machaneh dan tzafonah",
         "North: Dan Achiezer; Asher Pagiel; Naphtali Ahira; total 157600; last by standards; all counted of Israel 603550; Levites not counted among them; as YHWH commanded Moses so they camp by standards and so journey each by families houses."),
      ],
      [("S_camp_layout_complete", "Four-side camp layout complete"), ("S_march_order", "March order by standards set")],
      [("EXPORT_camp_layout", "מַחֲנוֹת", "machanot", "Four-standard camp around Tent"),
       ("EXPORT_march_order", "כֵּן יִסָּעוּ", "ken yissa'u", "March order mirrors camp layout")]),
    B("num_03_aaron_levi_replace", "3:1-13", 3, 1, 3, 13,
      "Aaron sons; Levites given for firstborn (3:1–13)",
      "הַקְרֵב אֶת־מַטֵּה לֵוִי", "hakrev et-matteh levi", "Bring near the tribe of Levi",
      ["num_02_camp_west_north", "exo_28_priest_garments", "exo_32_golden_calf"], "boot_steps", "medium",
      "Generations Aaron Moses; Nadav Avihu die; Eleazar Ithamar serve. Bring Levi tribe; set before Aaron; they guard charge of Aaron and whole edah for mishkan service; given to Aaron from among Israel; Aaron sons anointed priests; stranger who approaches die. I take Levites instead of every firstborn of Israel.",
      [
        ("STEP_N03A_A1", "3:1-4", "AARON_SONS", "וְאֵלֶּה תּוֹלְדֹת אַהֲרֹן", "ve-eleh toldot aharon",
         "These generations of Aaron and Moses day YHWH spoke Moses Sinai; sons of Aaron Nadav Avihu Eleazar Ithamar; anointed priests; Nadav Avihu die before YHWH offering strange fire in Sinai wilderness no sons; Eleazar Ithamar serve as priests before Aaron father."),
        ("STEP_N03A_B1", "3:5-13", "LEVI_FOR_FIRSTBORN", "הַקְרֵב אֶת־מַטֵּה לֵוִי … תַּחַת כָּל־בְּכוֹר", "hakrev et-matteh levi … tachat kol-bekhor",
         "Bring Levi near set before Aaron priest; they keep his charge and charge of whole edah before Tent for service of mishkan; all vessels; given to Aaron and sons from Israel; you appoint Aaron and sons they keep priesthood; stranger who approaches die. I behold take Levites from among Israel instead of every firstborn opener of womb of Israel; Levites are Mine; for every firstborn Mine day I struck every firstborn Egypt I consecrated to Me every firstborn in Israel man and beast Mine I YHWH."),
      ],
      [("S_levi_given", "Levites given to Aaron"), ("S_bekhor_swap", "Levites instead of firstborn")],
      [("EXPORT_levi_netunim", "נְתוּנִים", "netunim", "Levites given to Aaron/sons"),
       ("EXPORT_tachat_bekhor", "תַּחַת כָּל־בְּכוֹר", "tachat kol-bekhor", "Levites in place of firstborn")],
      [("IF non-priest approaches priest office", "THEN death"),
       ("IF firstborn of Israel", "THEN Levites taken instead (principle)")],
      imports_en="Exod priesthood; Exod 32 context for Levi; Exod firstborn Egypt memory."),
    B("num_03_levite_clans_count", "3:14-39", 3, 14, 3, 39,
      "Levite clans Gershon Kehat Merari; camps and charges (3:14–39)",
      "פְּקֹד אֶת־בְּנֵי לֵוִי", "pekod et-benei levi", "Count the sons of Levi",
      ["num_03_aaron_levi_replace"], "boot_steps", "thin",
      "Count Levites by fathers house every male month old+. Gershon west charge curtains; Kehat south charge ark table menorah altars vessels; Eleazar chief of Levite chiefs; Merari north boards bars pillars; Moses Aaron east guard charge of sanctuary; total Levites 22000.",
      [
        ("STEP_N03B_A1", "3:14-26", "GERSHON", "פְּקֹד … גֵרְשׁוֹן", "pekod … gershon",
         "Count Levites in Sinai wilderness males from month old; Gershon Libni Shimei; count 7500; camp west behind mishkan; chief Elyasaph; charge: mishkan tent covering screen of entrance Tent; hangings of court screen of gate ropes for all service."),
        ("STEP_N03B_B1", "3:27-32", "KEHAT", "לִקְהָת … מִשְׁמֶרֶת הַקֹּדֶשׁ", "li-kehat … mishmeret ha-kodesh",
         "Kehat Amram Yitzhar Hebron Uzziel; males month+ 8600 keep charge of holy; camp south; chief Elizaphan; charge: ark table menorah altars holy vessels screen and all service; Eleazar son of Aaron chief of chiefs of Levites oversight of keepers of charge of holy."),
        ("STEP_N03B_C1", "3:33-39", "MERARI_TOTAL", "מְרָרִי … שְׁנַיִם וְעֶשְׂרִים אֶלֶף", "merari … shenayim ve-esrim elef",
         "Merari Machli Mushi; 6200; chief Zuriel; camp north; charge boards bars pillars sockets vessels ropes all service; those camp before mishkan east Moses Aaron sons keeping charge of sanctuary for charge of Israel; stranger who approaches die; all counted Levites Moses Aaron at YHWH word by families every male month+ 22000."),
      ],
      [("S_levi_clans", "Three Levite clans camped and charged"), ("S_levi_22000", "Levite total 22000")],
      [("EXPORT_gershon_kehat_merari", "גֵּרְשׁוֹן קְהָת מְרָרִי", "gershon kehat merari", "Three Levite service clans"),
       ("EXPORT_mishmeret_kodesh", "מִשְׁמֶרֶת הַקֹּדֶשׁ", "mishmeret ha-kodesh", "Charge of the holy (Kehat)")]),
    B("num_03_firstborn_redeem", "3:40-51", 3, 40, 3, 51,
      "Count firstborn; redeem excess over Levites (3:40–51)",
      "פְּדֵה אֶת בְּכוֹר", "pedeh et bekhor", "Redeem the firstborn",
      ["num_03_levite_clans_count", "exo_13_firstborn_matzot"], "decision_table", "medium",
      "Count every firstborn male of Israel month+; take Levites for Me instead of firstborn and Levite cattle instead of cattle. Firstborn of Israel 22273; Levites 22000; redeem the 273 excess five shekels each; give to Aaron sons.",
      [
        ("STEP_N03C_A1", "3:40-43", "COUNT_BEKHOR", "פְּקֹד כָּל־בְּכֹר זָכָר", "pekod kol-bekhor zakhar",
         "Count every firstborn male of Israel month old+; take Levites for Me I YHWH instead of all firstborn of Israel and cattle of Levites instead of all firstborn cattle of Israel; Moses counts as commanded; all firstborn males month+ by name 22273."),
        ("STEP_N03C_B1", "3:44-51", "REDEEM_273", "קַח אֶת־הַלְוִיִּם … פְּדוּיֵי הַשְּׁלֹשָׁה", "kach et-ha-leviyyim … peduyei ha-sheloshah",
         "Take Levites instead of all firstborn of Israel and Levite cattle instead of their cattle Levites Mine; and for the redeemed of the 273 excess of firstborn of Israel over Levites: take five shekels per head by sanctuary shekel twenty gerah; give money to Aaron and sons as redemption of excess; Moses takes redemption money from excess over Levites redeemed; from firstborn of Israel 1365 by sanctuary shekel; Moses gives to Aaron sons at YHWH word."),
      ],
      [("S_bekhor_redeemed", "Excess firstborn redeemed by silver")],
      [("EXPORT_pidyon_bekhor_num", "פִּדְיוֹן בְּכוֹר", "pidyon bekhor", "Firstborn redemption five shekels (excess over Levites)"),
       ("EXPORT_shekel_kodesh", "שֶׁקֶל הַקֹּדֶשׁ", "shekel ha-kodesh", "Sanctuary shekel twenty gerah")],
      [("IF firstborn of Israel exceed Levites", "THEN redeem excess at five sanctuary shekels each to Aaron sons")],
      imports_en="Exod 13 firstborn consecration; Exod shekel."),
    B("num_04_kehat", "4:1-20", 4, 1, 4, 20,
      "Kehat service ages 30–50; packing holy things (4:1–20)",
      "נָשֹׂא אֶת־רֹאשׁ בְּנֵי קְהָת", "naso et-rosh benei kehat", "Lift the head of the sons of Kehat",
      ["num_03_firstborn_redeem", "exo_25_ark_table_menorah"], "boot_steps", "medium",
      "Count Kehat from 30 to 50 for work of Tent. When camp journeys Aaron sons cover ark veil/tachash; table cloths vessels; menorah; gold altar; vessels; copper altar. After Aaron sons finish covering, Kehat come to carry — not touch holy lest die. Eleazar oil incense tamid anointing oil oversight of whole mishkan. Do not cut off Kehat; Aaron sons assign each man his burden; not go in to see when holy swallowed lest die.",
      [
        ("STEP_N04A_A1", "4:1-15", "COVER_CARRY", "נָשֹׂא … קְהָת … וְכִלָּה אַהֲרֹן", "naso … kehat … ve-killah aharon",
         "Count Kehat from Levi 30–50 years for work Tent of Meeting; this service of holy of holies: when camp journeys Aaron sons take down veil cover ark with it; tachash skin blue cloth poles; table: blue cloth dishes etc continual bread scarlet tachash poles; menorah lamps tongs blue tachash poles; gold altar blue tachash poles; vessels of service blue cloth tachash; ash altar purple cloth all vessels tachash poles; when Aaron and sons finished covering holy and all holy vessels when camp to journey then sons of Kehat come to carry but not touch the holy lest die; these burden of Kehat in Tent."),
        ("STEP_N04A_B1", "4:16-20", "ELEAZAR_WATCH", "וּפְקֻדַּת אֶלְעָזָר … אַל־תַּכְרִיתוּ", "u-fekuddat el'azar … al-takhritu",
         "Eleazar charge: oil of light incense of spices continual minchah anointing oil; oversight of whole mishkan all in it holy and vessels. YHWH to Moses Aaron: do not cut off tribe of clans of Kehat from among Levites; do this for them that they live and not die when approach holy of holies: Aaron and sons come assign each man his service and his burden; they shall not go in to see when the holy is swallowed lest they die."),
      ],
      [("S_kehat_protocol", "Kehat carry-only after priest cover"), ("S_eleazar_oversight", "Eleazar oil/incense oversight")],
      [("EXPORT_kehat_burden", "מַשָּׂא בְנֵי קְהָת", "massa benei kehat", "Kehat burden of most holy objects"),
       ("EXPORT_not_touch_kodesh", "לֹא־יִגְּעוּ אֶל־הַקֹּדֶשׁ", "lo-yigge'u el-ha-kodesh", "Do not touch the holy (Kehat)")],
      [("IF camp journeys", "THEN Aaron sons cover holy first; then Kehat carry"),
       ("IF Kehat touches uncovered holy OR sees when swallowed", "THEN death risk")],
      imports_en="Exod 25–27 furniture specs; Exod priest garments."),
    B("num_04_gershon_merari", "4:21-49", 4, 21, 4, 49,
      "Gershon and Merari service 30–50; totals (4:21–49)",
      "נָשֹׂא אֶת־רֹאשׁ בְּנֵי גֵרְשׁוֹן", "naso et-rosh benei gershon", "Lift the head of the sons of Gershon",
      ["num_04_kehat"], "boot_steps", "medium",
      "Gershon 30–50 carry curtains tent coverings screens ropes under Ithamar. Merari 30–50 boards bars pillars sockets pegs under Ithamar. Counts: Kehat 2750; Gershon 2630; Merari 3200; all 8580 assigned by name to burdens.",
      [
        ("STEP_N04B_A1", "4:21-28", "GERSHON_SERVICE", "נָשֹׂא … גֵרְשׁוֹן … עֲבֹדַת", "naso … gershon … avodat",
         "Count Gershon also 30–50; service and burden: curtains of mishkan Tent of Meeting covering tachash covering screen of entrance; hangings of court screen of gate ropes all service; at mouth of Aaron sons all their service; appoint them all burdens; this service of Gershon clans in Tent; charge in hand of Ithamar son of Aaron."),
        ("STEP_N04B_B1", "4:29-33", "MERARI_SERVICE", "בְּנֵי מְרָרִי … קְרָשִׁים", "benei merari … kerashim",
         "Count Merari 30–50; this their burden of all service in Tent: boards of mishkan bars pillars sockets; pillars of court around sockets pegs ropes all vessels all service; by name appoint vessels of charge of their burden; this service of Merari clans all service in Tent in hand of Ithamar."),
        ("STEP_N04B_C1", "4:34-49", "LEVITE_SERVICE_TOTALS", "וַיִּפְקֹד מֹשֶׁה … שְׁמֹנַת אֲלָפִים", "va-yifkod moshe … shemonat alafim",
         "Moses Aaron princes count Kehat 30–50: 2750; Gershon 2630; Merari 3200; all counted of Levites 30–50 all who come to serve work of Tent: 8580; at YHWH mouth they were appointed by Moses each man his service and burden; counted as YHWH commanded Moses."),
      ],
      [("S_levi_service_ages", "Levite service ages 30–50 all clans"), ("S_8580", "Total service Levites 8580")],
      [("EXPORT_avodat_ohel", "עֲבֹדַת אֹהֶל מוֹעֵד", "avodat ohel mo'ed", "Service of Tent of Meeting ages 30–50"),
       ("EXPORT_ithamar_charge", "יַד אִיתָמָר", "yad itamar", "Ithamar oversees Gershon/Merari")]),
    # Phase B
    B("num_05_camp_pure_theft", "5:1-10", 5, 1, 5, 10,
      "Send impure from camp; confession and restitution (5:1–10)",
      "שַׁלְּחוּ מִן־הַמַּחֲנֶה", "shalchu min-ha-machaneh", "Send out from the camp",
      ["num_04_gershon_merari", "lev_13_skin_initial", "lev_15_male_discharge"], "decision_table", "primary",
      "Command Israel send from camp every tzara'at every zav everyone impure for soul (corpse); male and female send outside camp not to defile camp where I dwell among them. When man or woman does any human sin trespass against YHWH that person is guilty; confess sin; restore principal + fifth to whom wronged; if no redeemer to whom restore then to YHWH for priest besides ram of atonement; every terumah of holy things of man to priest his.",
      [
        ("STEP_N05A_A1", "5:1-4", "SEND_IMPURE", "שַׁלְּחוּ מִן־הַמַּחֲנֶה כָּל־צָרוּעַ", "shalchu min-ha-machaneh kol-tzarua",
         "Command Israel: send from camp every tzara'at and every zav and everyone impure for a soul; male and female send outside the camp; send them so they do not defile their camps in whose midst I dwell; Israel did so sent them outside camp as YHWH spoke to Moses."),
        ("STEP_N05A_B1", "5:5-10", "CONFESS_RESTORE", "אִישׁ אוֹ־אִשָּׁה כִּי יַעֲשׂוּ … וְהִתְוַדּוּ", "ish o-ishah ki ya'asu … ve-hitvaddu",
         "When man or woman does any of all sins of humans to trespass trespass against YHWH that soul is guilty; they shall confess their sin that they did; restore his asham in its head and add its fifth to him to whom he was guilty; if man has no goel to restore asham to him the asham restored to YHWH for the priest besides ram of atonements with which he atones for him; every terumah of all holy things of Israel that they bring near to priest shall be his; a man's holy things shall be his; what a man gives to the priest shall be his."),
      ],
      [("S_camp_pure", "Impure sent outside camp"), ("S_asham_restore", "Confess + principal + fifth")],
      [("EXPORT_shalchu_machaneh", "שַׁלְּחוּ מִן־הַמַּחֲנֶה", "shalchu min-ha-machaneh", "Send impure from camp"),
       ("EXPORT_hitvaddu_asham", "וְהִתְוַדּוּ", "ve-hitvaddu", "Confess and restore asham + fifth")],
      [("IF tzarua OR zav OR corpse-impure", "THEN send outside camp"),
       ("IF sin/trespass against YHWH re human harm", "THEN confess; restore principal + fifth; ram atonement")],
      imports_en="Lev 13–15 impurity types; Lev 5 asham restore patterns."),
    B("num_05_sotah", "5:11-31", 5, 11, 5, 31,
      "Sotah: jealousy ordeal of bitter waters (5:11–31)",
      "תּוֹרַת הַקְּנָאֹת", "torat ha-kena'ot", "Law of jealousies",
      ["num_05_camp_pure_theft"], "decision_table", "primary",
      "If wife strays and husband jealous whether true or spirit of jealousy: bring wife offering barley no oil frankincense; priest sets before YHWH; holy water dust of floor; hair loose; oath curse written washed into water; woman drinks; if guilty belly swell thigh fall; if clean free conceive seed. Man free of iniquity; woman bears her iniquity.",
      [
        ("STEP_N05B_A1", "5:11-15", "CASE_OPEN", "אִישׁ אִישׁ כִּי־תִשְׂטֶה אִשְׁתּוֹ", "ish ish ki-tisteh ishto",
         "If any man's wife goes astray and trespasses trespass against him and a man lies with her seed hidden from husband's eyes she concealed defiled no witness not caught; or spirit of jealousy passes on him and he is jealous of wife she defiled or not defiled; man brings wife to priest and offering for her tenth ephah barley flour; not pour oil not put frankincense for it is minchat kena'ot minchat remembrance remembering iniquity."),
        ("STEP_N05B_B1", "5:16-26", "ORDEAL_RITE", "וְהִשְׁקָהּ אֶת־הַמַּיִם", "ve-hishkah et-ha-mayim",
         "Priest brings near sets before YHWH; holy water in earthen vessel dust from floor of mishkan into water; uncover woman's head put minchah on her palms; bitter cursing water in priest hand; adjure woman: if no man lay and not strayed be clean from bitter waters; if strayed and defiled man other than husband — priest adjures with oath of curse: YHWH make you curse and oath in your people YHWH make your thigh fall belly swell; these curse waters enter your bowels to swell belly fall thigh; woman says amen amen; priest writes curses in book wipe into bitter waters; make her drink; priest takes minchah wave before YHWH bring near altar; fistful memorial burn; afterward make woman drink water."),
        ("STEP_N05B_C1", "5:27-31", "OUTCOME", "וְהָיְתָה … אִם־לֹא נִטְמְאָה", "ve-hayetah … im-lo nitme'ah",
         "When he makes her drink: if defiled trespassed against husband waters enter bitter belly swells thigh falls woman becomes curse in her people; if woman not defiled pure she is clean and shall be sown with seed. This torat kena'ot when wife strays defiled or when spirit of jealousy; man free from iniquity woman that bears her iniquity."),
      ],
      [("S_sotah_procedure", "Sotah ordeal procedure loaded")],
      [("EXPORT_sotah", "סֹטָה / תּוֹרַת הַקְּנָאֹת", "sotah / torat ha-kena'ot", "Jealousy ordeal procedure"),
       ("EXPORT_mei_marim", "מֵי הַמָּרִים", "mei ha-marim", "Bitter cursing waters")],
      [("IF husband jealous of wife (defiled OR not proven)", "THEN bring to priest; barley minchah; bitter-water ordeal"),
       ("IF she is clean after ordeal", "THEN free and may conceive")]),
    B("num_06_nazir", "6:1-21", 6, 1, 6, 21,
      "Nazirite vow: abstain, hair, corpse ban, completion offerings (6:1–21)",
      "נֶדֶר נָזִיר", "neder nazir", "Vow of a nazirite",
      ["num_05_sotah", "lev_07_shelamim_types"], "decision_table", "primary",
      "When man or woman vows nazir to separate to YHWH: no wine vinegar grape products; no razor all days of vow; holy grow hair; not come to dead soul even father mother brother sister; if someone dies suddenly beside him defiles head of nazir: shave day7; day8 birds; restart days; when days complete: olah chatat shelamim bread basket; shave head peace offering fire under pot; wave breast thigh. This torat nazir.",
      [
        ("STEP_N06A_A1", "6:1-8", "NAZIR_RULES", "כִּי יַפְלִא … נֶדֶר נָזִיר", "ki yafli … neder nazir",
         "When man or woman does wondrously to vow nazir vow to separate to YHWH: from wine and shekhar separate; vinegar of wine vinegar of shekhar not drink; any grape liquor not drink; grapes moist or dry not eat; all days of nazir from all that is made of grape vine from seeds to skin not eat; all days of vow of nazir razor not pass on head until days full that he separates to YHWH holy shall he be grow locks of hair of his head; all days of separating to YHWH not come upon dead soul; for father mother brother sister not make himself impure for them in their death for crown of God on his head; all days of his nazir he is holy to YHWH."),
        ("STEP_N06A_B1", "6:9-12", "DEFILE_RESTART", "וְכִי־יָמוּת מֵת עָלָיו", "ve-khi-yamut met alav",
         "If a dead dies on him suddenly in an instant and defiles head of his nazir: shave his head on day of his purity day seven he shaves; day eight brings two turtledoves or two young pigeons to priest entrance of Tent; priest makes one chatat one olah atone for him from what he sinned over the soul; he shall sanctify his head that day; separate to YHWH days of his nazir and bring lamb yearling for asham; first days fall for his nazir was defiled."),
        ("STEP_N06A_C1", "6:13-21", "COMPLETION", "וְזֹאת תּוֹרַת הַנָּזִיר … בְּיוֹם מְלֹאת", "ve-zot torat ha-nazir … be-yom melot",
         "This torat nazir: on day days of his nazir full bring him to entrance of Tent; offer his offering to YHWH one male lamb yearling whole olah; one ewe yearling whole chatat; one ram whole shelamim; basket matzot fine flour cakes oil wafers oil and their minchah and nesekh; priest brings before YHWH makes chatat and olah; ram shelamim with basket of matzot; minchah nesekh; nazir shaves head of his nazir at entrance of Tent takes hair of head of his nazir puts on fire under shelamim; priest takes cooked shoulder of ram one matzah cake one wafer puts on palms of nazir after shaving; wave them wave offering before YHWH; holy for priest with wave breast and heave thigh after the nazir may drink wine. This torat nazir who vows his offering to YHWH for his nazir besides what his hand reaches according to vow of his nazir so he does on torat of his nazir."),
      ],
      [("S_nazir_rules", "Nazir abstentions and holiness"), ("S_nazir_complete", "Completion offerings path")],
      [("EXPORT_nazir", "נָזִיר", "nazir", "Nazirite vow system"),
       ("EXPORT_nezer", "נֵזֶר", "nezer", "Crown/separation of hair to YHWH")],
      [("IF nazir vow", "THEN no wine/grape; no razor; no corpse impurity"),
       ("IF nazir defiled by sudden death", "THEN shave day7; birds day8; asham; restart days"),
       ("IF nazir days complete", "THEN olah chatat shelamim bread; shave; then may drink wine")],
      imports_en="Lev shelamim/chatat/olah types; wave breast thigh Lev 7."),
    B("num_06_priest_blessing", "6:22-27", 6, 22, 6, 27,
      "Priestly blessing (birkat kohanim) (6:22–27)",
      "יְבָרֶכְךָ יְהוָה", "yevarekhekha YHWH", "YHWH bless you",
      ["num_06_nazir", "exo_28_priest_garments"], "boot_steps", "medium",
      "Speak to Aaron and sons: thus bless Israel — YHWH bless and keep; shine face and grace; lift face and put shalom. Put My name on Israel I will bless them.",
      [
        ("STEP_N06B_A1", "6:22-27", "BIRKAT_KOHANIM", "כֹּה תְבָרֲכוּ … יָשֵׂם לְךָ שָׁלוֹם", "koh tevarekhu … yasem lekha shalom",
         "YHWH to Moses: speak Aaron and sons: thus shall you bless the children of Israel say to them: YHWH bless you and keep you; YHWH make His face shine toward you and be gracious to you; YHWH lift His face toward you and put for you shalom. They shall put My name on the children of Israel and I will bless them."),
      ],
      [("S_birkat_kohanim", "Priestly blessing formula loaded")],
      [("EXPORT_birkat_kohanim", "בִּרְכַּת כֹּהֲנִים", "birkat kohanim", "Threefold priestly blessing"),
       ("EXPORT_yasem_shalom", "וְיָשֵׂם לְךָ שָׁלוֹם", "ve-yasem lekha shalom", "And put for you peace")]),
    B("num_07_carts_offerings_a", "7:1-47", 7, 1, 7, 47,
      "Dedication day: carts to Levites; first six princes' offerings (7:1–47)",
      "וַיְהִי בְּיוֹם כַּלּוֹת מֹשֶׁה", "va-yehi be-yom kallot moshe", "On the day Moses finished",
      ["num_06_priest_blessing", "exo_40_erect_fill"], "boot_steps", "thin",
      "Day Moses finishes erecting mishkan anoints sanctifies it vessels altar: princes of Israel bring six covered wagons twelve oxen; give to Levites by service — Gershon 2 wagons 4 oxen; Merari 4 wagons 8 oxen; Kehat none (shoulder holy). Princes offer dedication of altar day anointed; one prince per day. Days 1–6: Nachshon through Eliasaph offerings (same pattern: plate silver bowl silver pan gold; minchah; incense; bulls rams lambs goats).",
      [
        ("STEP_N07A_A1", "7:1-9", "WAGONS_LEVITES", "וַיַּקְרִיבוּ … עֶגְלֹת", "va-yakrivu … eglot",
         "Day Moses finishes erecting mishkan anoints sanctifies it all vessels altar utensils; princes of Israel heads of fathers houses princes of tribes standers over counted ones bring offering: six covered wagons twelve oxen wagon for two princes ox for one; bring before mishkan; YHWH to Moses take from them be for serving service of Tent; give to Levites each according to his service; Moses takes wagons oxen gives to Levites; two wagons four oxen to Gershon according to service; four wagons eight oxen to Merari according to service under Ithamar; to Kehat not give for service of holy on shoulder they carry."),
        ("STEP_N07A_B1", "7:10-47", "DAYS_1_TO_6", "וַיַּקְרִיבוּ הַנְּשִׂאִים … בַּיּוֹם", "va-yakrivu ha-nesi'im … ba-yom",
         "Princes bring dedication of altar day it is anointed; princes bring offering before altar; YHWH: one prince a day one prince a day they bring offering for dedication of altar. Day 1 Yehudah Nachshon: silver plate 130 shekels bowl 70 sanctuary shekel both full fine flour oil minchah; gold pan 10 full incense; bull ram lamb yearling olah; goat chatat; two oxen five rams five he-goats five lambs yearling shelamim. Days 2–6: Yissachar Nethanel; Zevulun Eliab; Reuben Elizur; Shimon Shelumiel; Gad Eliasaph — same offering pattern."),
      ],
      [("S_wagons_assigned", "Wagons to Gershon/Merari"), ("S_dedication_half", "First six dedication days")],
      [("EXPORT_chanukkat_mizbeach", "חֲנֻכַּת הַמִּזְבֵּחַ", "chanukkat ha-mizbeach", "Dedication of the altar by princes"),
       ("EXPORT_agalot_levi", "עֶגְלֹת לַלְוִיִּם", "eglot la-leviyyim", "Wagons for Levite transport")]),
    B("num_07_offerings_b_total", "7:48-89", 7, 48, 7, 89,
      "Days 7–12 princes; dedication totals; voice from kaporet (7:48–89)",
      "זֹאת חֲנֻכַּת הַמִּזְבֵּחַ", "zot chanukkat ha-mizbeach", "This is the dedication of the altar",
      ["num_07_carts_offerings_a"], "boot_steps", "thin",
      "Days 7–12: Ephraim Elishama through Naphtali Ahira same offerings. Totals of dedication: silver plates bowls gold pans animals. When Moses enters Tent to speak with Him he hears the Voice from above the kaporet between the keruvim.",
      [
        ("STEP_N07B_A1", "7:48-83", "DAYS_7_TO_12", "בַּיּוֹם הַשְּׁבִיעִי … נַפְתָּלִי", "ba-yom ha-shevi'i … naftali",
         "Day 7 Ephraim Elishama; 8 Menasheh Gamliel; 9 Binyamin Avidan; 10 Dan Achiezer; 11 Asher Pagiel; 12 Naphtali Ahira — each same silver gold animal pattern as day 1."),
        ("STEP_N07B_B1", "7:84-88", "TOTALS", "זֹאת חֲנֻכַּת הַמִּזְבֵּחַ … כָּל־בָּקָר", "zot chanukkat ha-mizbeach … kol-bakar",
         "This dedication of altar on day anointed from princes of Israel: silver plates 12; silver bowls 12; gold pans 12; silver of vessels 2400 sanctuary shekel; gold pans 120; olah animals bulls 12 rams 12 lambs 12 and their minchah; goats chatat 12; shelamim oxen 24 rams 60 he-goats 60 lambs 60; this dedication of altar after it was anointed."),
        ("STEP_N07B_C1", "7:89", "VOICE_KAPORET", "וּבְבֹא מֹשֶׁה … הַקֹּל", "u-vevo moshe … ha-kol",
         "When Moses comes into Tent of Meeting to speak with Him then he hears the Voice speaking to him from above the kaporet that is on the ark of the testimony from between the two keruvim; and He speaks to him."),
      ],
      [("S_dedication_complete", "Twelve-day altar dedication complete"), ("S_voice_kaporet", "Voice from between keruvim")],
      [("EXPORT_twelve_day_dedication", "שְׁנֵים עָשָׂר יוֹם", "sheneim asar yom", "Twelve-day prince dedication"),
       ("EXPORT_voice_between_keruvim", "הַקֹּל … בֵּין שְׁנֵי הַכְּרֻבִים", "ha-kol … bein shenei ha-keruvim", "Voice from between the cherubim")]),
    # Phase C
    B("num_08_menorah_levites", "8:1-26", 8, 1, 8, 26,
      "Menorah lamps; Levite purification and service ages (8:1–26)",
      "בְּהַעֲלֹתְךָ אֶת־הַנֵּרֹת", "be-ha'alotkha et-ha-nerot", "When you raise the lamps",
      ["num_07_offerings_b_total", "lev_24_lamp_bread", "num_03_aaron_levi_replace"], "boot_steps", "medium",
      "Aaron raises seven lamps to face menorah. Pure gold menorah. Take Levites purify: water of chatat; razor whole body; wash clothes; bulls olah chatat; Israel lean; Aaron wave Levites; separate from Israel given to Me instead of firstborn; give Levites to Aaron for service; from 25 years enter work; from 50 retire assist guard not work.",
      [
        ("STEP_N08_A1", "8:1-4", "MENORAH", "בְּהַעֲלֹתְךָ אֶת־הַנֵּרֹת", "be-ha'alotkha et-ha-nerot",
         "Speak Aaron: when you raise the lamps toward face of menorah seven lamps shall give light; Aaron does so; this work of menorah beaten gold to its thigh to its flower beaten work according to the vision YHWH showed Moses so he made the menorah."),
        ("STEP_N08_B1", "8:5-19", "LEVITE_PURIFY", "קַח אֶת־הַלְוִיִּם … וְטִהַרְתָּ", "kach et-ha-leviyyim … ve-tiharta",
         "Take Levites from among Israel purify them: sprinkle water of chatat; pass razor over all flesh; wash clothes purify; take bull olah and minchah and second bull chatat; bring Levites before Tent assemble edah Israel; Israel lean hands on Levites; Aaron waves Levites wave before YHWH from Israel; Levites lean on bulls; make one chatat one olah to atone; set Levites before Aaron sons wave; separate Levites from among Israel Levites Mine; given Me from among Israel instead of openers of every womb firstborn of all Israel I take them to Me; for Mine every firstborn day I struck firstborn Egypt; take Levites; give Levites to Aaron and sons from among Israel to serve service of Israel in Tent to atone for Israel that there be no plague when Israel approach the holy."),
        ("STEP_N08_C1", "8:20-26", "AGES_25_50", "מִבֶּן חָמֵשׁ וְעֶשְׂרִים … וּמִבֶּן חֲמִשִּׁים", "mi-ben chamesh ve-esrim … u-mi-ben chamishim",
         "Moses Aaron all edah do to Levites as commanded; Levites purify wash clothes Aaron waves atones; after Levites come to serve Tent before Aaron sons as YHWH about Levites so to them. YHWH: this for Levites from 25 years up come to army service in work of Tent; from 50 years return from army of service not work more; serve with brothers in Tent to keep charge but work they shall not work; thus do to Levites in their charges."),
      ],
      [("S_levites_installed", "Levites purified and waved into service"), ("S_service_ages", "Service 25–50 (with ch.4 30–50 load)")],
      [("EXPORT_tahar_levi", "טָהֳרַת הַלְוִיִּם", "tohorat ha-leviyyim", "Levite purification and wave"),
       ("EXPORT_avodat_25_50", "מִבֶּן כ״ה עַד חֲמִשִּׁים", "mi-ben 25 ad chamishim", "Levite work ages 25–50")],
      [("IF Levite enters work", "THEN from 25 years; retire work at 50 keep charge with brothers")],
      imports_en="Lev 24 ner tamid; Exod menorah; Num 3–4 Levite charges."),
    B("num_09_pesach_cloud", "9:1-23", 9, 1, 9, 23,
      "Second-year Pesach; Pesach sheni; cloud journey rule (9:1–23)",
      "פֶּסַח בְּמוֹעֲדוֹ — עֲנַן", "pesach be-mo'ado — anan", "Pesach in its time — cloud",
      ["num_08_menorah_levites", "exo_12_pesach_command", "exo_40_erect_fill"], "decision_table", "primary",
      "Year 2 month 1: make Pesach in its time 14th twilight statutes. Men impure for soul cannot; Pesach sheni month 2 day 14 for impure or on distant road; if clean and not on road and skips — cut off. Ger also makes Pesach one statute. Cloud covers mishkan; when lifts Israel journey; where settles camp; by mouth of YHWH camp and journey days many or few.",
      [
        ("STEP_N09_A1", "9:1-5", "PESACH_Y2", "וַיַּעֲשׂוּ … פֶּסַח בָּרִאשׁוֹן", "va-ya'asu … pesach ba-rishon",
         "YHWH in Sinai wilderness year 2 month 1 after leaving Egypt: Israel make the pesach in its appointed time; 14th day of this month twilight you shall make it in its time according to all statutes and all ordinances; Moses speaks Israel to make pesach; they make it in first month 14th twilight in Sinai wilderness all as YHWH commanded Moses."),
        ("STEP_N09_B1", "9:6-14", "PESACH_SHENI", "אֲנַחְנוּ טְמֵאִים … בַּחֹדֶשׁ הַשֵּׁנִי", "anachnu teme'im … ba-chodesh ha-sheni",
         "Men who were impure for soul of man and could not make pesach that day: why withheld not to bring near offering of YHWH in its time among Israel; Moses: stand I hear what YHWH commands. YHWH: any man impure for soul or on distant road of you or generations make pesach to YHWH in second month 14th twilight with matzot and bitter herbs eat; leave none till morning break no bone according to all statute of pesach make it; but the man clean and not on road and ceases to make pesach — that soul cut off from its peoples for offering of YHWH not brought in its time his sin he bears; if ger sojourns and makes pesach to YHWH according to statute of pesach and its ordinance so he makes; one statute for you for ger and for native of land."),
        ("STEP_N09_C1", "9:15-23", "CLOUD_RULE", "וּבְיוֹם הָקִים … עַל־פִּי יְהוָה", "u-ve-yom hakim … al-pi YHWH",
         "Day mishkan erected cloud covers mishkan tent of testimony; evening like appearance of fire until morning; so always cloud covers and fire appearance night; when cloud lifts from over the tent after that Israel journey; in place where cloud settles there Israel camp; at mouth of YHWH Israel journey and at mouth of YHWH they camp all days cloud settles on mishkan they camp; when cloud prolongs many days keep charge of YHWH not journey; when cloud few days at mouth of YHWH camp and at mouth of YHWH journey; two days or month or days when cloud prolongs on mishkan Israel camp not journey; when it lifts they journey; at mouth of YHWH they camp and at mouth of YHWH journey; charge of YHWH they keep at mouth of YHWH by hand of Moses."),
      ],
      [("S_pesach_sheni", "Second-month Pesach path"), ("S_cloud_ops", "Cloud governs camp/journey")],
      [("EXPORT_pesach_sheni", "פֶּסַח שֵׁנִי", "pesach sheni", "Second-month Pesach for impure/distant"),
       ("EXPORT_anan_march", "עַל־פִּי הֶעָנָן", "al-pi he-anan", "Camp and march by the cloud")],
      [("IF impure for corpse OR on distant road at Pesach", "THEN make Pesach month 2 day 14"),
       ("IF clean and not distant and skips Pesach", "THEN cut off"),
       ("IF cloud lifts", "THEN journey; if settles THEN camp")],
      imports_en="Exod 12 Pesach; Exod 40 cloud on mishkan."),
    B("num_10_trumpets_depart", "10:1-36", 10, 1, 10, 36,
      "Silver trumpets; Sinai depart; Hobab; ark song (10:1–36)",
      "חֲצֹצְרֹת כֶּסֶף — וַיִּסְעוּ", "chatzotzrot kesef — va-yis'u", "Silver trumpets — and they journeyed",
      ["num_09_pesach_cloud", "num_02_camp_west_north"], "boot_steps", "medium",
      "Two silver trumpets: summon edah or princes; blow alarms for camps east then south; war alarm remembered; also mo'adim and beginnings of months over olot shelamim. Year 2 month 2 day 20 cloud lifts; depart Sinai to Paran by mouth of YHWH; order of march. Moses to Hobab: go with us; ark journey formula rise YHWH; rest formula return YHWH myriads of Israel.",
      [
        ("STEP_N10_A1", "10:1-10", "TRUMPETS", "עֲשֵׂה לְךָ שְׁתֵּי חֲצֹצְרֹת", "aseh lekha shetei chatzotzrot",
         "Make two trumpets of silver beaten; for calling edah and for journeying camps; when both blown whole edah to entrance of Tent; if one blown princes heads of thousands assemble; blow teruah camps of east journey; second teruah camps of south journey; teruah for journeys; when assembling blow not teruah; sons of Aaron priests blow; statute forever. When war in land against oppressor blow teruah remembered before YHWH saved from enemies; day of joy mo'adim beginnings of months blow trumpets over olot and shelamim memorial before God I YHWH."),
        ("STEP_N10_B1", "10:11-28", "DEPART_SINAI", "בִּשְׁנַת הַשֵּׁנִית … וַיִּסְעוּ", "bi-shenat ha-shenit … va-yis'u",
         "Year 2 month 2 day 20 cloud lifts from over mishkan of testimony; Israel journey from wilderness of Sinai cloud settles wilderness of Paran; first journey at mouth of YHWH by Moses; standard of Yehudah first; mishkan taken down Gershon Merari carrying mishkan journey; standard of Reuben; Kehat carrying holy they erect mishkan by arrival; standard of Ephraim; standard of Dan rear guard; this journeys of Israel by their armies."),
        ("STEP_N10_C1", "10:29-36", "HOBAB_ARK", "קוּמָה יְהוָה … שׁוּבָה יְהוָה", "kumah YHWH … shuvah YHWH",
         "Moses to Hobab son of Reuel Midianite father-in-law: we journey to place YHWH said I give you; go with us good to you for YHWH spoke good on Israel; he: I will not go to my land birthplace; Moses: do not leave us for you know our camping in wilderness be eyes for us; when you go with us the good YHWH does us we do you. Journey from mountain of YHWH three days; ark of covenant of YHWH journeys before them three days way to seek rest for them; cloud of YHWH over them by day in their journeying. When ark journeys Moses says: Rise YHWH let Your enemies scatter let haters flee before You; when it rests he says: Return YHWH myriads of thousands of Israel."),
      ],
      [("S_trumpets", "Trumpet signal system"), ("S_left_sinai", "Left Sinai under cloud"), ("S_ark_formula", "Ark rise/return formulas")],
      [("EXPORT_chatzotzrot", "חֲצֹצְרֹת", "chatzotzrot", "Silver trumpet signal system"),
       ("EXPORT_kumah_shuvah", "קוּמָה / שׁוּבָה", "kumah / shuvah", "Ark journey and rest invocations")]),
    # Phase D narrative
    B("num_11_complaint_quail", "11:1-35", 11, 1, 11, 35,
      "Taberah; meat craving; seventy elders; quail and plague (11:1–35)",
      "וַיְהִי הָעָם כְּמִתְאֹנְנִים — שְׂלָו", "va-yehi ha-am ke-mitonenim — selav", "The people were as complainers — quail",
      ["num_10_trumpets_depart", "exo_16_manna_shabbat"], "narrative_fsm", "thin",
      "People complain; fire of YHWH at edge camp; Taberah. Crave meat weep remember Egypt; manna described; Moses burdened; seventy elders share spirit; two prophesy in camp; quail from sea; while meat between teeth plague; Kivrot ha-Ta'avah; to Chatzerot.",
      [
        ("STEP_N11_A1", "11:1-15", "COMPLAINT_BURDEN", "וַיְהִי הָעָם כְּמִתְאֹנְנִים … הָרֹגֵנִי נָא", "va-yehi ha-am ke-mitonenim … horegeni na",
         "People as complainers evil in ears of YHWH; fire burns among them edge of camp; people cry Moses; Moses prays fire sinks; place named Taberah. Mixed multitude crave; Israel weep: who feeds us meat; remember fish Egypt cucumbers etc; now our soul dry nothing but manna; manna like coriander bdellium; people grind mill or mortar boil make cakes taste of oil cream; when dew night falls manna on it. Moses hears people weep by families doorways anger of YHWH kindles; Moses: why evil Your servant; did I conceive this people; from where meat for all; I cannot alone; if thus do kill me."),
        ("STEP_N11_B1", "11:16-30", "SEVENTY_ELDERS", "אֶסְפָה־לִּי שִׁבְעִים אִישׁ", "esfah-li shiv'im ish",
         "YHWH: gather seventy men of elders of Israel known as elders officers; take to Tent stand there with you; I come down speak with you take of spirit on you put on them they bear with you burden of people not you alone; to people: consecrate tomorrow eat meat month of days until out nostrils loathsome because rejected YHWH among you wept. Moses: 600000 foot and You say meat month; sheep cattle fish? YHWH: hand of YHWH short? Elders gathered; YHWH comes down cloud takes of spirit on seventy they prophesy not again; Eldad Medad remain in camp spirit on them prophesy in camp; lad runs; Joshua jealous; Moses: would that all YHWH's people prophets."),
        ("STEP_N11_C1", "11:31-35", "QUAIL_PLAGUE", "וְרוּחַ נָסַע … הַשְּׂלָו", "ve-ruach nasa … ha-selav",
         "Wind from YHWH brings quail from sea leaves on camp day journey this side and that around camp about two cubits on face of earth; people rise all that day night next day gather least ten homers spread for themselves; while meat still between teeth before cut off anger of YHWH kindles smites people very great plague; name place Kivrot ha-Ta'avah for there buried the people who craved; from Kivrot ha-Ta'avah people journey to Chatzerot are in Chatzerot."),
      ],
      [("S_taberah", "Complaint fire Taberah"), ("S_seventy", "Seventy elders share spirit"), ("S_quail_plague", "Quail craving plague")],
      [("EXPORT_shivim_zaken", "שִׁבְעִים זָקֵן", "shiv'im zaken", "Seventy elders spirit-share"),
       ("EXPORT_kivrot_taavah", "קִבְרוֹת הַתַּאֲוָה", "kivrot ha-ta'avah", "Graves of craving")]),
    B("num_12_miriam", "12:1-16", 12, 1, 12, 16,
      "Miriam and Aaron speak against Moses; Miriam struck (12:1–16)",
      "וַתְּדַבֵּר מִרְיָם וְאַהֲרֹן", "va-tedabber miryam ve-aharon", "Miriam and Aaron spoke",
      ["num_11_complaint_quail"], "narrative_fsm", "thin",
      "Miriam Aaron speak about Cushite wife and claim equal speech with Moses; YHWH: Moses faithful whole house; mouth to mouth; anger; cloud lifts Miriam leprous as snow; Aaron pleads; Moses prays heal; seven days shut outside camp then journey from Chatzerot to Paran.",
      [
        ("STEP_N12_A1", "12:1-9", "CHALLENGE", "הֲרַק אַךְ־בְּמֹשֶׁה", "ha-rak akh-be-moshe",
         "Miriam and Aaron speak against Moses about the Cushite wife he took; they say: has YHWH only spoken with Moses? Has He not spoken also with us? YHWH hears; man Moses very humble more than all face of ground; suddenly YHWH to Moses Aaron Miriam: three of you to Tent; come down in pillar of cloud stand entrance; call Aaron Miriam; hear My words: if your prophet YHWH in vision make Myself known in dream speak; not so My servant Moses in all My house faithful; mouth to mouth I speak with him appearance not riddles likeness of YHWH he beholds; why not fear to speak against My servant Moses? Anger of YHWH kindles against them He goes."),
        ("STEP_N12_B1", "12:10-16", "MIRIAM_SHUT", "וְהִנֵּה מִרְיָם מְצֹרַעַת", "ve-hinneh miryam metzora'at",
         "Cloud turns from over Tent; Miriam leprous as snow; Aaron turns Miriam leprous; Aaron to Moses: do not put on us sin which we did foolishly sinned; let her not be as dead from womb half flesh eaten; Moses cries to YHWH: God please heal her please; YHWH: if her father spit in her face would she not be shamed seven days; shut seven days outside camp after gather in; Miriam shut outside camp seven days people not journey until Miriam gathered; after people journey from Chatzerot camp in wilderness of Paran."),
      ],
      [("S_moshe_unique", "Moses unique prophetic access affirmed"), ("S_miriam_seven", "Miriam shut seven days")],
      [("EXPORT_neeman_bayit", "נֶאֱמָן הוּא", "ne'eman hu", "Moses faithful in all My house"),
       ("EXPORT_peh_el_peh", "פֶּה אֶל־פֶּה", "peh el-peh", "Mouth-to-mouth speech with Moses")]),
    B("num_13_spies_sent", "13:1-33", 13, 1, 13, 33,
      "Twelve spies sent; report of strong land and giants (13:1–33)",
      "שְׁלַח־לְךָ אֲנָשִׁים", "shelach-lekha anashim", "Send for yourself men",
      ["num_12_miriam"], "narrative_fsm", "thin",
      "Send men to spy land of Canaan one per tribe; Moses renames Hoshea Yehoshua; instructions; go up Negev Hebron grapes Eshkol; return 40 days; land flows milk honey; nevertheless strong people fortified; Caleb stills people we can; others: not able; land eats inhabitants; Nephilim Anakim we were as grasshoppers.",
      [
        ("STEP_N13_A1", "13:1-20", "SEND_SPIES", "שְׁלַח־לְךָ … כָּל־נָשִׂיא", "shelach-lekha … kol-nasi",
         "YHWH to Moses: send men to tour land of Canaan which I give Israel; one man one man per tribe of fathers every prince among them; Moses sends from wilderness of Paran at mouth of YHWH all men heads of Israel; names listed; Moses calls Hoshea bin Nun Yehoshua; send to tour land of Canaan; go up Negev go up the mountain; see land what it is people strong or weak few or many; land good or bad cities camps or fortresses; land fat or lean trees or not; strengthen take from fruit of land; days days of first grapes."),
        ("STEP_N13_B1", "13:21-33", "REPORT", "וַיָּשֻׁבוּ … אֶרֶץ אֹכֶלֶת", "va-yashuvu … eretz okhelet",
         "They go up tour from wilderness of Zin to Rechov Lebo-Hamat; go up Negev come to Hebron Ahiman Sheshai Talmai children of Anak; Hebron built seven years before Zoan Egypt; come to wadi Eshkol cut branch one cluster of grapes carry on pole two; pomegranates figs; place called wadi Eshkol for cluster Israel cut; return from touring end of forty days; come to Moses Aaron all edah wilderness of Paran Kadesh; show fruit; recount: came to land you sent us flowing milk honey this its fruit; but people strong cities fortified very great also children of Anak we saw; Amalek Negev Hittite Jebusite Amorite mountain; Canaanite sea Jordan. Caleb stills people to Moses: we go up possess for we can. Men who went with him: we cannot go against people for stronger than we; bring out evil report of land: land we toured land that eats its inhabitants; all people men of measure; there we saw Nephilim sons of Anak of Nephilim; we were in our eyes as grasshoppers so we were in their eyes."),
      ],
      [("S_spies_out", "Twelve spies mission"), ("S_split_report", "Caleb vs evil report")],
      [("EXPORT_meraglim", "מְרַגְּלִים / תָּרִים", "meraglim / tarim", "Spies / land-tourers"),
       ("EXPORT_caleb_alon", "עָלֹה נַעֲלֶה", "aloh na'aleh", "Caleb: we can go up")]),
    B("num_14_rejection", "14:1-45", 14, 1, 14, 45,
      "People reject; intercession; decree forty years; failed ascent (14:1–45)",
      "עַד־מָתַי יְנַאֲצֻנִי", "ad-matai yena'atzuni", "How long will they despise Me",
      ["num_13_spies_sent"], "narrative_fsm", "thin",
      "Whole edah weeps seek return Egypt; Joshua Caleb tear clothes land good do not rebel; assembly stone them; glory appears; Moses intercedes; pardon but this generation not see land except Caleb Joshua; wanderers 40 years by days of tour; ten spies die plague; people mourn try go up without ark/Moses; Amalek Canaanite strike them to Hormah.",
      [
        ("STEP_N14_A1", "14:1-19", "REBEL_INTERCEDE", "לוּ־מַתְנוּ … סְלַח־נָא", "lu-matnu … selach-na",
         "All edah lift voice weep night; all Israel murmur Moses Aaron; whole edah: if only we died in Egypt or this wilderness; why YHWH bring to this land fall by sword wives children plunder; better return Egypt; each to brother give head return Egypt. Moses Aaron fall faces before all assembly; Joshua bin Nun Caleb tear garments; land we toured very very good; if YHWH delights brings us; only do not rebel YHWH do not fear people of land bread for us their shade turned YHWH with us; all edah say stone them with stones; glory of YHWH appears in Tent to all Israel. YHWH to Moses: how long this people despise Me how long not believe in all signs; I smite them pestilence disinherit make you greater. Moses: Egypt will hear… nations say for lack YHWH could not… now let power of my Lord be great as You spoke: YHWH long of face great kindness bearing iniquity… forgive na this people as You bore this people from Egypt until now."),
        ("STEP_N14_B1", "14:20-38", "DECREE_40", "סָלַחְתִּי … אַרְבָּעִים שָׁנָה", "salachti … arba'im shanah",
         "YHWH: I have forgiven as you spoke; but as I live filled glory of YHWH all earth; all men who see My glory and signs Egypt wilderness and test Me these ten times not listen — if they see the land I swore to fathers all who despise Me not see it; My servant Caleb different spirit full after Me I bring to land he came his seed possesses; Amalek Canaanite in valley tomorrow turn journey wilderness way of Sea of Reeds. YHWH to Moses Aaron: how long for this evil edah murmuring; say to them as I live utterance of YHWH as you spoke in My ears so I do to you: in this wilderness your corpses fall all counted of all number from 20 years up who murmured; if you come to land I lifted hand to settle you except Caleb son of Yephunneh and Joshua bin Nun; children you said plunder I bring they know land you rejected; your corpses this wilderness; your sons shepherds in wilderness forty years bear your whoredoms until your corpses finished in wilderness; by number of days you toured the land forty days day for year day for year forty years you bear your iniquities know My opposition; I YHWH speak do this to all this evil edah gathered on Me in this wilderness they finish there they die. Men Moses sent to tour who returned made all edah murmur bringing evil report die plague before YHWH; Joshua bin Nun Caleb son of Yephunneh live of men who went to tour land."),
        ("STEP_N14_C1", "14:39-45", "FAILED_ASCENT", "וַיַּשְׁכִּמוּ … וַיַּכּוּם", "va-yashkimu … va-yakkum",
         "Moses speaks these words to all Israel people mourn greatly; rise early morning go up to head of mountain: we are here we go up to place YHWH said for we sinned; Moses: why this you pass mouth of YHWH it will not succeed; do not go up for YHWH not in your midst not be struck before enemies; for Amalek Canaanite there you fall by sword for you turned from after YHWH YHWH not with you; they presume go up to head of mountain; ark of covenant of YHWH and Moses not move from midst of camp; Amalek Canaanite dwelling in that mountain come down strike them pound them to Hormah."),
      ],
      [("S_decree_40", "Forty-year wilderness decree"), ("S_caleb_joshua_live", "Only Caleb Joshua of spies enter"), ("S_hormah", "Failed ascent to Hormah")],
      [("EXPORT_yom_la-shanah", "יוֹם לַשָּׁנָה", "yom la-shanah", "Day-for-year forty years"),
       ("EXPORT_salachti", "סָלַחְתִּי כִּדְבָרֶךָ", "salachti ki-dvarekha", "I have forgiven as you spoke")]),
    # Phase E
    B("num_15_offerings_laws", "15:1-31", 15, 1, 15, 31,
      "Land-entry nesekh/minchah; challah; unwitting vs high hand (15:1–31)",
      "כִּי תָבֹאוּ אֶל־אֶרֶץ — בְּיָד רָמָה", "ki tavo'u el-aretz — be-yad ramah", "When you come to the land — with a high hand",
      ["num_14_rejection", "lev_02_minchah", "lev_04_chatat_common"], "decision_table", "primary",
      "When come to land and make isheh vow freewill mo'adim: with olah or zevach add minchah and nesekh scaled by animal size; one statute ger and native. When eat bread of land raise challah terumah first of arisah. IF unwitting of edah: bull olah + minchah nesekh + goat chatat. IF one soul unwitting: female goat year chatat. IF high hand native or ger: blasphemes YHWH cut off; word of YHWH despised commandment broken cut off iniquity in it.",
      [
        ("STEP_N15A_A1", "15:1-16", "NESEKH_SCALE", "כִּי תָבֹאוּ … וְהִקְרִיב", "ki tavo'u … ve-hikriv",
         "When you come to land of your dwellings which I give and make isheh to YHWH olah or zevach to separate vow or freewill or in your mo'adim to make pleasant scent to YHWH from cattle or flock: who brings his offering to YHWH bring minchah tenth fine flour mixed quarter hin oil; wine for nesekh quarter hin with olah or zevach for each lamb; for ram two tenths flour third hin oil third hin wine; for bull three tenths flour half hin oil half hin wine isheh pleasant scent. Thus for each ox ram lamb or kid of goats; according to number you do so for each by their number; every native do these thus to bring isheh pleasant scent to YHWH; if ger sojourns or among you generations and makes isheh pleasant scent as you do so he does; assembly one statute for you and for ger statute forever generations as you so ger before YHWH; one torah and one mishpat for you and for ger sojourning with you."),
        ("STEP_N15A_B1", "15:17-21", "CHALLAH", "בְּבֹאֲכֶם … חַלָּה", "be-vo'akhem … challah",
         "When you come to the land I bring you there: when you eat of bread of the land raise a terumah to YHWH; first of your dough challah raise as terumah like terumah of threshing floor so raise it; from first of your dough give to YHWH terumah generations."),
        ("STEP_N15A_C1", "15:22-31", "SHGAGAH_YAD_RAMAH", "וְכִי תִשְׁגּוּ … בְּיָד רָמָה", "ve-khi tishgu … be-yad ramah",
         "If you err and not do all these mitzvot which YHWH spoke to Moses all that YHWH commanded you by hand of Moses from day YHWH commanded and onward generations: if from eyes of edah done unwittingly whole edah make one bull young of herd olah pleasant scent to YHWH minchah and nesekh by mishpat and one goat of goats chatat; priest atones for all edah Israel forgiven for it was unwitting and they brought their offering isheh to YHWH and their chatat before YHWH for their unwitting; forgiven all edah Israel and ger sojourning among them for all the people in unwitting. If one soul sins unwittingly bring goat yearling female chatat; priest atones the soul erring in sin unwittingly before YHWH to atone for him forgiven; native of Israel and for ger sojourning among them one torah for you for who does unwittingly. But the soul that does with a high hand from native and from ger YHWH he blasphemes; cut off that soul from among its people; for word of YHWH it despised and His commandment it broke; cut off cut off that soul its iniquity in it."),
      ],
      [("S_land_offer_scale", "Minchah/nesekh scales for land"), ("S_challah", "Challah terumah"), ("S_yad_ramah", "High-hand vs shgagah")],
      [("EXPORT_nesekh_scale", "נֶסֶךְ", "nesekh", "Wine libation scale with minchah"),
       ("EXPORT_challah", "חַלָּה", "challah", "First dough terumah"),
       ("EXPORT_yad_ramah", "בְּיָד רָמָה", "be-yad ramah", "High-handed sin — cut off")],
      [("IF isheh vow/freewill/mo'ed in land", "THEN add minchah+nesekh by animal size"),
       ("IF whole edah unwitting", "THEN bull olah + goat chatat"),
       ("IF high hand (blaspheme/despise word)", "THEN cut off")],
      imports_en="Lev minchah/chatat types; land-entry framing after spies."),
    B("num_15_wood_tzitzit", "15:32-41", 15, 32, 15, 41,
      "Wood-gatherer on Shabbat; tzitzit command (15:32–41)",
      "מְקֹשֵׁשׁ עֵצִים — צִיצִת", "mekoshesh etzim — tzitzit", "Gathering wood — tassels",
      ["num_15_offerings_laws", "exo_31_craftsmen_shabbat"], "decision_table", "primary",
      "Man gathering wood on Shabbat; custody because not clarified; YHWH: man die stone him whole edah; stone outside camp. Speak Israel make tzitzit on corners of garments generations; blue cord on tzitzit; look remember all mitzvot not tour after heart eyes; be holy to God; I YHWH God who brought you from Egypt to be your God.",
      [
        ("STEP_N15B_A1", "15:32-36", "WOOD_GATHERER", "וַיִּמְצְאוּ אִישׁ מְקֹשֵׁשׁ עֵצִים", "va-yimtze'u ish mekoshesh etzim",
         "Israel in wilderness find a man gathering wood on day of Shabbat; who find him gathering wood bring him near to Moses Aaron all edah; put him in custody for not clarified what should be done to him; YHWH to Moses: the man die die; stone him with stones all the edah outside the camp; all edah bring him outside the camp stone him with stones he dies as YHWH commanded Moses."),
        ("STEP_N15B_B1", "15:37-41", "TZITZIT", "וְעָשׂוּ לָהֶם צִיצִת", "ve-asu lahem tzitzit",
         "YHWH to Moses: speak Israel say to them make for themselves tzitzit on corners of their garments generations; put on tzitzit of the corner a cord of blue; it shall be for you for tzitzit you shall see it remember all mitzvot of YHWH do them not tour after your heart and after your eyes which you go whoring after them; so that you remember do all My mitzvot be holy to your God; I YHWH your God who brought you out from land of Egypt to be your God I YHWH your God."),
      ],
      [("S_shabbat_wood_case", "Shabbat wood-gatherer capital case"), ("S_tzitzit", "Tzitzit reminder system")],
      [("EXPORT_mekoshesh", "מְקֹשֵׁשׁ עֵצִים", "mekoshesh etzim", "Wood-gatherer Shabbat case"),
       ("EXPORT_tzitzit", "צִיצִת", "tzitzit", "Corner tassels with blue cord")],
      [("IF gather wood on Shabbat (as clarified)", "THEN death by stoning of edah"),
       ("IF wear garments with corners", "THEN tzitzit + blue cord to remember mitzvot")]),
    B("num_16_korach", "16:1-35", 16, 1, 16, 35,
      "Korach Datan Aviram rebellion; fire and earth (16:1–35)",
      "וַיִּקַּח קֹרַח", "va-yikkach korach", "And Korach took",
      ["num_15_wood_tzitzit", "lev_10_nadav_avihu"], "narrative_fsm", "medium",
      "Korach Levite with Datan Aviram On and 250 princes challenge Moses Aaron whole edah holy; Moses: morning YHWH chooses; censers fire incense; Datan Aviram refuse; Moses angry; test: if earth creates mouth swallows; ground opens houses; fire consumes 250 offerers of incense.",
      [
        ("STEP_N16_A1", "16:1-19", "REBEL_CENSERS", "רַב־לָכֶם … כָל־הָעֵדָה", "rav-lakhem … kol-ha-edah",
         "Korach son of Yitzhar Kehat Levi takes Datan Aviram sons of Eliav and On son of Pelet sons of Reuben; rise before Moses men of Israel 250 princes of edah called of assembly men of name; assemble on Moses Aaron: much for you for all edah all of them holy in their midst YHWH; why lift yourselves above assembly of YHWH. Moses hears falls face; to Korach all his edah: morning YHWH makes known who is His and who holy brings near; whom He chooses bring near to Him; this do: take censers Korach all edah; put fire in them put incense before YHWH tomorrow; man whom YHWH chooses he holy much for you sons of Levi. Moses to Korach: hear sons of Levi; is it small God of Israel separated you from edah of Israel to bring near to Him to serve service of mishkan stand before edah to minister; He brought you near and all your brothers sons of Levi with you and you seek also priesthood; therefore you and all your edah are gathered on YHWH; Aaron what is he that you murmur on him. Moses sends to call Datan Aviram; they say we will not go up; is it small you brought us up from land flowing milk honey to kill in wilderness that you make yourself prince also over us; moreover not to land flowing milk honey inheritance field vineyard; will you gouge eyes of these men; we will not go up. Moses very angry to YHWH: do not turn to their minchah; not one donkey I took not evil one of them. Moses to Korach: you and all your edah be before YHWH you they Aaron tomorrow; take each his censer put incense on them bring near before YHWH each his censer 250 censers and you and Aaron each his censer. They take each censer fire incense stand entrance of Tent Moses Aaron; Korach assembles on them all edah to entrance of Tent; glory of YHWH appears to all edah."),
        ("STEP_N16_B1", "16:20-35", "SWALLOW_FIRE", "אִם־בְּרִיאָה יִבְרָא … וָאֵשׁ יָצְאָה", "im-beri'ah yivra … va-esh yatz'ah",
         "YHWH to Moses Aaron: separate from midst of this edah I consume them in a moment; they fall faces: God of spirits of all flesh shall one man sin and on all edah You rage? YHWH: speak to edah saying go up from around dwelling of Korach Datan Aviram. Moses rises goes to Datan Aviram; elders of Israel after him; speak to edah: turn aside from tents of these wicked men not touch anything of theirs lest swept in all their sins; they go up from dwelling of Korach Datan Aviram around; Datan Aviram go out standing entrance of their tents wives children little ones. Moses: in this know YHWH sent me do all these deeds not from my heart; if as all men these die and visitation of all men visited on them YHWH did not send me; but if YHWH creates a creation and ground opens its mouth swallows them and all that is theirs and they go down alive to Sheol then know these men despised YHWH. As he finishes speaking all these words ground under them splits; earth opens mouth swallows them houses all men of Korach all property; they and all that is theirs go down alive to Sheol earth covers over them they perish from midst of assembly; all Israel around them flee at their voice for they said lest earth swallow us. Fire went out from YHWH consumed the 250 men bringers of incense."),
      ],
      [("S_korach_judged", "Korach company swallowed/burned"), ("S_priest_choice", "YHWH chooses who approaches")],
      [("EXPORT_korach", "קֹרַח", "korach", "Korach rebellion judgment"),
       ("EXPORT_machtot", "מַחְתּוֹת", "machtot", "Censers as test of chosenness")]),
    B("num_17_plague_staff", "17:1-28", 17, 1, 17, 28,
      "Censers hammered; plague; Aaron staff buds (17:1–28)",
      "מַטֵּה אַהֲרֹן פָּרַח", "matteh aharon parach", "The staff of Aaron blossomed",
      ["num_16_korach"], "narrative_fsm", "medium",
      "Eleazar hammers censers of sinners covering for altar sign. Next day edah murmurs; plague begins; Aaron runs with incense atones stands between dead and living. Take staffs per tribe write names; Aaron staff for Levi; in Tent before testimony; morning Aaron staff buds blossoms almonds; keep as sign for rebels; Israel fear all approaching mishkan die.",
      [
        ("STEP_N17_A1", "17:1-15", "CENSERS_PLAGUE", "הָרִימוּ … הַמַּחְתֹּת", "harimu … ha-machtot",
         "YHWH to Moses: say to Eleazar son of Aaron take the censers from the burned and fire scatter beyond for they are holy; censers of these sinners in their souls make them beaten plates covering for altar for they brought them near before YHWH they are holy; be for a sign to Israel. Eleazar takes bronze censers brought near by burned ones beats them covering for altar; memorial to Israel so that no stranger who is not of seed of Aaron come near to burn incense before YHWH not be as Korach and his edah as YHWH spoke by hand of Moses to him. Next day all edah of Israel murmur on Moses Aaron saying you killed people of YHWH; when edah assembles on Moses Aaron they turn to Tent behold cloud covered it glory of YHWH appears; Moses Aaron come before Tent; YHWH to Moses: rise from midst of this edah I consume them in a moment; they fall faces. Moses to Aaron: take the censer put fire from on altar put incense go quickly to edah atone for them for wrath has gone out from before YHWH the plague has begun; Aaron takes as Moses spoke runs to midst of assembly and behold plague begun among people; he puts incense atones for the people; stands between the dead and the living plague restrained; dead in the plague 14700 besides dead on matter of Korach; Aaron returns to Moses entrance of Tent plague restrained."),
        ("STEP_N17_B1", "17:16-28", "STAFF_BUDS", "קַח מֵאִתָּם מַטֶּה מַטֶּה", "kach me-ittam matteh matteh",
         "YHWH to Moses: speak to Israel take from them a staff staff for father's house from all their princes by fathers houses twelve staffs each man's name write on his staff; name of Aaron write on staff of Levi for one staff for head of their fathers houses; rest them in Tent of Meeting before the testimony where I meet you; it shall be the man I choose his staff blossoms; I subside from on Me murmurings of Israel which they murmur on you. Moses speaks Israel; all their princes give him a staff for one prince one prince for fathers houses twelve staffs staff of Aaron among their staffs; Moses rests staffs before YHWH in Tent of the testimony; next day Moses comes to Tent of testimony and behold staff of Aaron for house of Levi had budded brought forth bud blossomed brought almonds; Moses brings out all the staffs from before YHWH to all Israel they see take each his staff. YHWH to Moses: return staff of Aaron before the testimony for keeping for a sign for sons of rebellion end their murmurings from on Me not die; Moses does as YHWH commanded. Israel to Moses: behold we perish we are lost all of us lost; all who come near come near to mishkan of YHWH die; are we finished to perish?"),
      ],
      [("S_altar_sign_censers", "Censer covering sign on altar"), ("S_aaron_staff", "Aaron staff buds confirms priesthood"), ("S_plague_stopped", "Incense atonement stops plague")],
      [("EXPORT_matteh_aharon", "מַטֵּה אַהֲרֹן", "matteh aharon", "Aaron's budding staff as sign"),
       ("EXPORT_bein_metim", "בֵּין הַמֵּתִים וּבֵין הַחַיִּים", "bein ha-metim u-vein ha-chayyim", "Aaron stands between dead and living")]),
    # Phase F
    B("num_18_priest_levite_dues", "18:1-32", 18, 1, 18, 32,
      "Priest and Levite charges; terumah ma'aser dues (18:1–32)",
      "אֲנִי חֶלְקְךָ וְנַחֲלָתֶךָ", "ani chelkeha ve-nachalatekha", "I am your portion and your inheritance",
      ["num_17_plague_staff", "lev_07_fat_blood_dues", "lev_22_holy_food"], "decision_table", "primary",
      "Aaron house bear iniquity of sanctuary and priesthood; brothers Levi joined keep charge of Tent not approach vessels of holy and altar; stranger who approaches die. I give charge of terumot; most holy from fire: every minchah chatat asham males eat holy place. Wave gifts; oil wine grain first; firstborn of man redeem; firstborn unclean beast redeem; firstborn ox sheep goat blood altar fat isheh flesh yours. No land inheritance I am portion. To Levites every tithe in Israel inheritance for service of Tent; Israel not approach Tent bear sin die; Levites do service bear their iniquity. Levites raise terumah to YHWH tenth of the tithe to Aaron; remainder as produce; not profane holy of Israel die.",
      [
        ("STEP_N18_A1", "18:1-7", "CHARGES", "אַתָּה וּבָנֶיךָ … תִּשְׂאוּ", "attah u-vanekha … tisu",
         "YHWH to Aaron: you and sons and father's house with you bear iniquity of the sanctuary; you and sons with you bear iniquity of your priesthood; also your brothers tribe of Levi tribe of your father bring near with you joined to you minister you; you and sons before Tent of the testimony; they keep your charge and charge of all the Tent only to vessels of the holy and to the altar they shall not come near not die also they also you; joined to you keep charge of Tent of Meeting for all service of the Tent; stranger shall not come near you; keep charge of the holy and charge of the altar not again be wrath on Israel; I behold take your brothers the Levites from among Israel for you a gift given to YHWH to serve service of Tent of Meeting; you and sons with you keep your priesthood for every matter of the altar and to within the veil you serve; service of gift I give your priesthood; stranger who comes near dies."),
        ("STEP_N18_B1", "18:8-20", "PRIEST_GIFTS", "הִנֵּה נָתַתִּי לְךָ … חֵלֶב", "hinneh natatti lekha … chelev",
         "I give you charge of My terumot of all holy things of Israel to you and sons statute forever; this yours from holy of holies from the fire: every offering of theirs every minchah every chatat every asham they restore to Me holy of holies for you and sons; in most holy eat it every male eats holy it is for you. This yours: terumah of their gift all wave offerings of Israel I give you sons daughters with you statute forever; every pure in your house eats it. All fat of oil all fat of grape and grain their first which they give to YHWH to you I give them; firstfruits of all in their land which they bring to YHWH yours; every pure in your house eats. Every cherem in Israel yours. Every opener of womb of all flesh man beast offered to YHWH yours; only redeem redeem firstborn of man and firstborn of unclean beast redeem; redemption from month old redemption value five sanctuary shekels twenty gerah; but firstborn of ox or firstborn of sheep or firstborn of goat not redeem holy are they; blood sprinkle on altar fat burn as isheh pleasant scent to YHWH; their flesh yours like wave breast like right thigh yours. All terumot of holy things which Israel raise to YHWH I give you sons daughters with you statute forever covenant of salt forever before YHWH for you and seed with you. YHWH to Aaron: in their land not inherit portion not be for you among them; I am your portion and your inheritance among Israel."),
        ("STEP_N18_C1", "18:21-32", "LEVI_TITHE", "וְלִבְנֵי לֵוִי … מַעֲשֵׂר", "ve-li-vene levi … ma'aser",
         "To sons of Levi behold I give every tithe in Israel for inheritance in exchange for their service which they serve service of Tent of Meeting; Israel no more come near Tent of Meeting to bear sin to die; Levite he serves service of Tent of Meeting they bear their iniquity statute forever generations; among Israel not inherit inheritance; for tithe of Israel which they raise to YHWH terumah I give to Levites for inheritance; therefore I said to them among Israel not inherit inheritance. YHWH to Moses: to Levites speak: when you take from Israel the tithe I give you from them for your inheritance raise from it terumah of YHWH tithe from the tithe; counted for you your terumah like grain from threshing floor like fullness from vat; so you raise also you terumah of YHWH from all your tithes which you take from Israel; give from it terumah of YHWH to Aaron the priest; from all your gifts raise every terumah of YHWH from all its fat its holy part from it. Say to them: when you raise its fat from it it is counted for Levites like produce of threshing floor like produce of vat; you eat it in every place you and your house for wage for you in exchange for your service in Tent of Meeting; you bear no sin on it when you raise its fat from it; and holy things of Israel you shall not profane not die."),
      ],
      [("S_priest_dues", "Priest terumah and most-holy dues"), ("S_levi_maaser", "Levite tithe + tenth to priest")],
      [("EXPORT_ani_chelkeha", "אֲנִי חֶלְקְךָ", "ani chelkeha", "YHWH is priest portion/inheritance"),
       ("EXPORT_maaser_levi", "מַעֲשֵׂר לַלֵּוִי", "ma'aser la-levi", "Tithe to Levites for service"),
       ("EXPORT_terumat_maaser", "תְּרוּמַת מַעֲשֵׂר", "terumat ma'aser", "Tenth of tithe to Aaron")],
      [("IF priest house", "THEN bear sanctuary/priesthood iniquity; receive terumot; no land portion"),
       ("IF Levite", "THEN receive Israel's tithe; raise tenth to priest; serve Tent"),
       ("IF stranger approaches altar/inner service", "THEN death")],
      imports_en="Lev 7 priest dues; Lev 22 holy food; Exod Tent."),
    B("num_19_parah", "19:1-22", 19, 1, 19, 22,
      "Red heifer; waters of niddah; corpse impurity seven days (19:1–22)",
      "פָרָה אֲדֻמָּה — מֵי נִדָּה", "parah adummah — mei niddah", "Red heifer — waters of impurity",
      ["num_18_priest_levite_dues", "lev_11_carcass_swarm_close", "num_05_camp_pure_theft"], "decision_table", "primary",
      "Statute: red heifer whole no blemish no yoke; Eleazar take outside camp slaughter; blood finger seven times toward Tent; burn heifer cedar hyssop scarlet; pure man gather ash outside clean place for edah water of niddah. Who burns/gathers wash impure evening. Who touches dead soul of man impure seven days; purify day 3 and 7 with ash water; if not purify cut off defiled mishkan. Tent with dead: all in tent open vessels impure seven; field sword dead bone grave. Recipe: ash in vessel living water; pure man sprinkle on tent vessels persons day 3 and 7; wash clothes bathe evening clean. Who sprinkles wash; who touches mei niddah impure evening; whatever impure touches impure; soul who touches impure until evening.",
      [
        ("STEP_N19_A1", "19:1-10", "RED_HEIFER_ASH", "וְיִקְחוּ אֵלֶיךָ פָרָה אֲדֻמָּה", "ve-yikchu elekha parah adummah",
         "Statute of torah YHWH commanded: speak Israel take to you a red heifer whole in which no blemish which no yoke came on it; give to Eleazar the priest; bring it out outside the camp slaughter it before him; Eleazar priest take of its blood with finger sprinkle toward face of Tent of Meeting of its blood seven times; burn the heifer before his eyes skin flesh blood dung burn; priest take cedar wood hyssop scarlet yarn throw to midst of burning of heifer; priest wash clothes bathe flesh in water after come to camp priest impure until evening; who burns it wash clothes in water bathe flesh impure until evening; man pure gather ash of heifer rest outside camp in clean place; it is for edah of Israel for keeping for water of niddah it is chatat; who gathers ash of heifer wash clothes impure until evening; for Israel and for ger sojourning among them statute forever."),
        ("STEP_N19_B1", "19:11-16", "CORPSE_IMPURE", "הַנֹּגֵעַ בְּמֵת … שִׁבְעַת יָמִים", "ha-noge'a be-met … shiv'at yamim",
         "Who touches the dead of any soul of man is impure seven days; he shall purify with it on third day and on seventh day clean; if not purify on third day then on seventh day not clean; all who touch dead soul of man who dies and not purify — defiled mishkan of YHWH cut off that soul from Israel for water of niddah not thrown on him impure is his impurity still in him. This torah: when a man dies in a tent all who come to the tent and all in the tent impure seven days; every open vessel which has no lid cord impure. All who touch on face of field one slain by sword or dead or bone of man or grave impure seven days."),
        ("STEP_N19_C1", "19:17-22", "SPRINKLE_CLEAN", "וְלָקְחוּ לַטָּמֵא … וְהִזָּה", "ve-lakchu la-tame … ve-hizzah",
         "They take for the impure from dust of burning of the chatat put on it living water in a vessel; pure man take hyssop dip in water sprinkle on the tent and on all vessels and on souls who were there and on who touched the bone or the slain or the dead or the grave; pure sprinkle on impure day three and day seven; day seven purify him wash clothes bathe in water evening clean. Man who is impure and not purify cut off that soul from midst of assembly for mishkan of YHWH he defiled water of niddah not thrown on him impure is. It is statute forever: who sprinkles water of niddah wash clothes; who touches water of niddah impure until evening; all that the impure touches is impure; the soul who touches is impure until evening."),
      ],
      [("S_parah_ash", "Red heifer ash system"), ("S_mei_niddah", "Waters of niddah for corpse impurity")],
      [("EXPORT_parah_adummah", "פָרָה אֲדֻמָּה", "parah adummah", "Red heifer ash for purification water"),
       ("EXPORT_mei_niddah", "מֵי נִדָּה", "mei niddah", "Water of impurity (corpse purification)"),
       ("EXPORT_tumat_met", "טֻמְאַת מֵת", "tumat met", "Seven-day corpse impurity with day 3/7")],
      [("IF touch human dead/bone/grave/slain", "THEN impure 7 days; need mei niddah day 3 and 7"),
       ("IF die in tent", "THEN all in tent + open vessels impure 7 days"),
       ("IF not purify with mei niddah", "THEN cut off; defiled mishkan")],
      imports_en="Lev carcass impurity patterns; camp purity Num 5."),
    # Phase G–L condensed but complete
    B("num_20_meribah_edom_aaron", "20:1-29", 20, 1, 20, 29,
      "Miriam dies; Meribah water; Edom refuses; Aaron dies (20:1–29)",
      "מֵי מְרִיבָה — וַיָּמָת אַהֲרֹן", "mei merivah — va-yamot aharon", "Waters of Meribah — and Aaron died",
      ["num_19_parah"], "narrative_fsm", "thin",
      "First month wilderness Zin Kadesh Miriam dies. No water; people quarrel; Moses Aaron fall; take staff speak to rock; Moses strikes rock twice water comes; YHWH: you did not trust Me to sanctify Me — not bring kahal into land; waters Meribah. Messengers to Edom: let us pass; Edom refuses with force. Journey Hor; Aaron stripped dies Eleazar dressed; house Israel weep 30 days.",
      [
        ("STEP_N20_A1", "20:1-13", "MERIBAH", "וַיַּךְ … הַסֶּלַע", "va-yakh … ha-sela",
         "Israel whole edah come wilderness of Zin first month; people settle Kadesh; Miriam dies buried there. No water for edah; assemble on Moses Aaron; quarrel: if only died with brothers before YHWH; why bring kahal of YHWH to this wilderness die we and our beasts; why bring up from Egypt to this evil place not seed fig vine pomegranate water to drink. Moses Aaron from face of kahal to entrance of Tent fall faces; glory of YHWH appears; YHWH to Moses: take the staff assemble the edah you and Aaron your brother speak to the rock before their eyes give its water; bring out water from rock water the edah and their beasts. Moses takes staff from before YHWH as commanded; Moses Aaron assemble kahal before the rock; he says: hear na rebels from this rock we bring out water for you; Moses lifts hand strikes the rock with his staff twice; much water comes out edah drinks beasts. YHWH to Moses Aaron: because you did not trust in Me to sanctify Me before eyes of Israel therefore you shall not bring this kahal to the land I give them. They are waters of Merivah where Israel quarreled with YHWH and He was sanctified in them."),
        ("STEP_N20_B1", "20:14-21", "EDOM", "נַעְבְּרָה־נָּא בְאַרְצֶךָ", "na'berah-na be-artzekha",
         "Moses sends messengers from Kadesh to king of Edom: thus says your brother Israel… let us pass na in your land not pass field vineyard not drink well water way of the king we go not turn right left until we pass your border. Edom: you shall not pass me lest with sword I go out to meet you. Israel: on the highway we go if we drink your water I or my cattle I give their price only no matter on my feet I pass. He says: you shall not pass; Edom goes out to meet him with heavy people and strong hand; Edom refuses give Israel pass in his border; Israel turns from on him."),
        ("STEP_N20_C1", "20:22-29", "AARON_DEATH", "יֵאָסֵף אַהֲרֹן … וַיָּמָת", "ye'asef aharon … va-yamot",
         "Journey from Kadesh; Israel whole edah come Mount Hor. YHWH to Moses Aaron at Mount Hor border of land of Edom: Aaron gathered to his peoples for not enter land I give Israel because you rebelled My mouth at waters of Merivah; take Aaron and Eleazar his son bring them up Mount Hor; strip Aaron of garments dress Eleazar his son; Aaron gathered dies there. Moses does as YHWH commanded; go up Mount Hor before eyes of all edah; Moses strips Aaron of garments dresses Eleazar; Aaron dies there on head of the mountain; Moses Eleazar come down from the mountain; all edah see Aaron expired; whole house of Israel weep Aaron thirty days."),
      ],
      [("S_meribah", "Meribah strike-rock failure"), ("S_edom_block", "Edom refuses passage"), ("S_aaron_dead", "Aaron dies; Eleazar succeeds")],
      [("EXPORT_mei_merivah", "מֵי מְרִיבָה", "mei merivah", "Waters of quarrel — Moses/Aaron barred from land"),
       ("EXPORT_eleazar_kohen", "אֶלְעָזָר כֹּהֵן", "el'azar kohen", "Eleazar succeeds Aaron as high priest")]),
    B("num_21_snakes_conquest", "21:1-35", 21, 1, 21, 35,
      "Hormah vow; copper snake; journeys; Sihon and Og (21:1–35)",
      "נְחַשׁ נְחֹשֶׁת — סִיחֹן עוֹג", "nechash nechoshet — sichon og", "Copper snake — Sihon Og",
      ["num_20_meribah_edom_aaron"], "narrative_fsm", "thin",
      "Canaanite of Arad fights; Israel vows cherem wins Hormah. From Hor way of Sea of Reeds around Edom people short-souled; speak against God Moses; snakes; copper snake on pole who looks lives. Song of well; Book of Wars. Sihon refuses pass; Israel strikes Heshbon. Og of Bashan struck; take land.",
      [
        ("STEP_N21_A1", "21:1-9", "HORMAH_SNAKE", "אִם־נָתֹן תִּתֵּן … נְחַשׁ נְחֹשֶׁת", "im-naton titten … nechash nechoshet",
         "Canaanite king of Arad dwelling Negev hears Israel comes way of Atarim fights Israel takes captive; Israel vows vow to YHWH: if giving You give this people in my hand I cherem their cities; YHWH hears voice of Israel gives Canaanite; cherem them and their cities; name of place Hormah. Journey from Mount Hor way of Sea of Reeds to go around land of Edom; soul of people short on the way; people speak against God and Moses: why brought us up from Egypt to die in wilderness no bread no water our soul loathes the light bread; YHWH sends in people the snakes the burning ones they bite people much people of Israel die; people come Moses: we sinned we spoke against YHWH and you; pray to YHWH remove from us the snake; Moses prays for the people; YHWH to Moses: make for yourself a burning one put it on a pole; it shall be all who are bitten sees it lives; Moses makes a snake of copper puts it on the pole; if the snake bit a man and he looked to the snake of copper he lived."),
        ("STEP_N21_B1", "21:10-20", "JOURNEYS_SONG", "וַיִּסְעוּ … בְּאֵר", "va-yis'u … be'er",
         "Israel journey camp Ovot; from Ovot Iyei ha-Avarim wilderness facing Moab sunrise; from there journey camp wadi Zered; from there camp beyond Arnon in wilderness coming from border of Amorite for Arnon border Moab between Moab and Amorite; therefore said in Book of Wars of YHWH… from there to Be'er well where YHWH said to Moses gather people I give them water; then Israel sings this song: Rise well sing to it… from wilderness Mattanah Nachaliel Bamot valley in field of Moab head of Pisgah overlooking the yeshimon."),
        ("STEP_N21_C1", "21:21-35", "SIHON_OG", "אֶעְבְּרָה בְאַרְצֶךָ … עוֹג", "e'ebrah be-artzekha … og",
         "Israel sends messengers to Sihon king of Amorites: let me pass your land… Sihon not give Israel pass; gathers people fights Israel Jahaz; Israel strikes him mouth of sword possesses land from Arnon to Yabbok to sons of Ammon for strong border Ammon; Israel takes all these cities dwells in cities of Amorite Heshbon all her daughters; for Heshbon city of Sihon… song of Heshbon. Moses sends to spy Yazer take daughters drive Amorite. Turn go up way of Bashan; Og king of Bashan goes out to Edrei; YHWH to Moses: do not fear him for in your hand I give him all his people land; do to him as Sihon; they strike him sons all people no remnant; possess land."),
      ],
      [("S_nechash", "Copper snake healing sign"), ("S_transjordan_east", "Sihon and Og lands taken")],
      [("EXPORT_nechash_nechoshet", "נְחַשׁ נְחֹשֶׁת", "nechash nechoshet", "Copper snake on pole"),
       ("EXPORT_sichon_og", "סִיחֹן וְעוֹג", "sichon ve-og", "East-bank kings defeated")]),
    B("num_22_balak_bilam_call", "22:1-41", 22, 1, 22, 41,
      "Balak calls Bilʿam; donkey sees malakh (22:1–41)",
      "בִּלְעָם בֶּן־בְּעוֹר", "bil'am ben-be'or", "Bilʿam son of Beor",
      ["num_21_snakes_conquest"], "narrative_fsm", "thin",
      "Israel camps plains of Moab. Balak sees all Israel did to Amorite; sends elders of Moab Midian to Bilʿam Petor: curse this people. God: do not go do not curse for blessed. Second embassy princes more honored; God: if men call go but word I speak do. Anger when he goes; malakh in way; donkey sees three times; Bilʿam's eye opened; go with men but only word I speak. Comes to Balak Kiryat Chutzot; to Bamot Baal sees edge of people.",
      [
        ("STEP_N22_A1", "22:1-14", "FIRST_CALL", "לְכָה אָרָה־לִּי", "lekhah arah-li",
         "Israel journeys camp plains of Moab across Jordan from Jericho. Balak son of Tzippor sees all Israel did to Amorite; Moab very afraid of people for many; Moab sickened before Israel; Moab to elders of Midian: now lick the assembly all around as ox licks green of field; Balak king of Moab at that time; sends messengers to Bilʿam son of Beor Petor on the River land of sons of his people to call him: behold a people came out from Egypt covers eye of the land settles opposite me; go na curse for me this people for stronger than I; perhaps I can strike it drive from land for I know whom you bless blessed whom you curse cursed. Elders of Moab Midian go fees of divination in hand come to Bilʿam speak words of Balak; he: lodge night I return you word as YHWH speaks to me; princes of Moab stay with Bilʿam. God comes to Bilʿam: who these men with you; Bilʿam: Balak sent to me… God to Bilʿam: you shall not go with them you shall not curse the people for it is blessed. Bilʿam rises morning says to princes of Balak: go to your land for YHWH refused to give me to go with you; princes of Moab rise come to Balak: Bilʿam refused to go with us."),
        ("STEP_N22_B1", "22:15-35", "DONKEY", "וַתֵּרֶא הָאָתוֹן", "va-tere ha-aton",
         "Balak adds send princes more and more honored; come to Bilʿam: thus says Balak do not withhold from going to me; for honoring I honor you all you say I do; go na curse for me this people. Bilʿam: if Balak gives me his house full silver gold I cannot pass mouth of YHWH my God to do small or great; now stay na also you this night I know what YHWH adds to speak with me. God comes to Bilʿam night: if to call you the men came rise go with them but the word I speak to you it you do. Bilʿam rises morning saddles donkey goes with princes of Moab; anger of God kindles for he is going; malakh of YHWH stations in way for adversary; he riding donkey two lads with him; donkey sees malakh of YHWH standing in way sword drawn hand; donkey turns from way goes in field; Bilʿam strikes donkey to turn her way; malakh stands in narrow of vineyards fence this fence that; donkey sees malakh presses to wall presses Bilʿam's foot to wall he strikes her again; malakh passes stands in narrow no way to turn right left; donkey sees malakh lies under Bilʿam; anger kindles strikes donkey with staff; YHWH opens mouth of donkey: what did I do to you that you struck me these three times; Bilʿam: because you mocked me if there were a sword in my hand I would kill you; donkey: am I not your donkey you rode on me from then until this day was I ever accustomed to do to you thus; he: no. YHWH opens eyes of Bilʿam he sees malakh of YHWH standing in way sword drawn bows falls face; malakh: for what struck your donkey these three times; I came out for adversary for the way reckless opposite me; donkey saw me turned before me these three times; perhaps turned from me for now also you I would kill and her I would keep alive. Bilʿam to malakh: I sinned for I did not know you standing to meet me in way; now if evil in your eyes I return. Malakh to Bilʿam: go with the men but only the word I speak to you it you speak; Bilʿam goes with princes of Balak."),
        ("STEP_N22_C1", "22:36-41", "MEET_BALAK", "הֲלוֹא שָׁלֹחַ", "ha-lo shaloach",
         "Balak hears Bilʿam comes goes out to meet him to City of Moab which on border of Arnon end of border; Balak to Bilʿam: did I not send earnestly to you to call you; why did you not go to me; am I truly not able to honor you; Bilʿam to Balak: behold I came to you; now am I at all able to speak anything; the word God puts in my mouth it I speak. Bilʿam goes with Balak they come to Kiryat Chutzot; Balak sacrifices cattle and flock sends to Bilʿam and princes with him; in morning Balak takes Bilʿam brings him up Bamot Baal sees from there edge of the people."),
      ],
      [("S_bilam_called", "Bilʿam engaged under word constraint"), ("S_malakh_way", "Malakh blocks reckless way")],
      [("EXPORT_bilam", "בִּלְעָם", "bil'am", "Bilʿam bound to speak only God's word"),
       ("EXPORT_lo_ta'or", "לֹא תָאֹר", "lo ta'or", "Do not curse — people is blessed")]),
    B("num_23_oracles_1_2", "23:1-30", 23, 1, 23, 30,
      "Bilʿam oracles one and two: bless not curse (23:1–30)",
      "מַה־אָקֹּב לֹא קַבֹּה אֵל", "mah-akkov lo kabboh El", "How can I curse whom God has not cursed",
      ["num_22_balak_bilam_call"], "narrative_fsm", "thin",
      "Seven altars bulls rams; oracle 1: from Aram Balak brings; how curse God not cursed; people dwell alone; who counts dust of Jacob; let me die death of upright. Balak: what have you done. Move to field of Tzofim Pisgah; second seven; oracle 2: God not man lie; not behold trouble in Jacob; YHWH his God with him; no enchantment in Jacob; like lion rises. Balak: neither curse nor bless. Move to Peor overlooking yeshimon.",
      [
        ("STEP_N23_A1", "23:1-12", "ORACLE_1", "מַה־אָקֹּב", "mah-akkov",
         "Bilʿam: build me here seven altars prepare seven bulls seven rams; Balak does; bull and ram on altar; Bilʿam: stand by burnt offering I go perhaps YHWH meets me word He shows I tell you; goes bare height; God meets Bilʿam; I arranged seven altars bull ram on altar; put word in mouth of Bilʿam: return to Balak thus speak. Returns: from Aram Balak king of Moab leads me from mountains of east: go curse Jacob go denounce Israel; how I curse God not cursed how denounce YHWH not denounced; from head of rocks I see him from hills I behold him; behold a people dwells alone among nations not reckons itself; who counts dust of Jacob number fourth of Israel; let my soul die death of uprights be my end like his. Balak: what have you done to me; to curse my enemies I took you and behold you blessed bless. He: what YHWH puts in my mouth it I keep to speak."),
        ("STEP_N23_B1", "23:13-30", "ORACLE_2", "לֹא אִישׁ אֵל", "lo ish El",
         "Balak: go with me to another place see him; only his edge see all not see; curse him from there. Takes to field of Tzofim head of Pisgah; builds seven altars bull ram; stand by burnt offering I meet there; YHWH meets puts word in mouth: return to Balak thus speak. Balak: what did YHWH speak; he takes up mashal: rise Balak hear give ear son of Tzippor; God not man that He lie son of man that He repent; He say and not do speak and not establish it; behold to bless I took a blessing He blessed I cannot reverse it; not behold trouble in Jacob not see toil in Israel; YHWH his God with him and shout of a king in him; God brings them out of Egypt like horns of wild ox for him; for no enchantment in Jacob no divination in Israel; in time it is said to Jacob and to Israel what God has done; behold a people like lioness rises like lion lifts himself not lies until eats prey blood of slain drinks. Balak to Bilʿam: also cursing not curse him also blessing not bless him. Bilʿam: did I not speak to you saying all that YHWH speaks it I do. Balak: go I take you to another place perhaps right in eyes of God curse him for me from there; takes Bilʿam head of Peor overlooking face of the yeshimon; Bilʿam: build me here seven altars prepare seven bulls seven rams; Balak does as Bilʿam said offers bull and ram on altar."),
      ],
      [("S_oracle_1_2", "First two mashals bless Israel")],
      [("EXPORT_am_levadad", "עָם לְבָדָד יִשְׁכֹּן", "am levadad yishkon", "A people that dwells alone"),
       ("EXPORT_lo_ish_el", "לֹא אִישׁ אֵל וִיכַזֵּב", "lo ish El vi-khazzeb", "God is not a man that He should lie")]),
    B("num_24_oracles_3_4", "24:1-25", 24, 1, 24, 25,
      "Oracles three and four; star from Jacob; Bilʿam departs (24:1–25)",
      "דָּרַךְ כּוֹכָב מִיַּעֲקֹב", "darakh kokhav mi-ya'akov", "A star has stepped forth from Jacob",
      ["num_23_oracles_1_2"], "narrative_fsm", "thin",
      "Bilʿam sees it is good in eyes of YHWH to bless Israel; spirit of God on him; mashal 3: how good tents of Jacob; like gardens rivers; king higher than Agag; bless who bless curse who curse. Balak angry clap hands. Mashal 4: star from Jacob scepter from Israel smashes Moab; Edom possession; Amalek first of nations end to destruction; Kenite; ships from Kittim. Bilʿam rises returns place; Balak also goes way.",
      [
        ("STEP_N24_A1", "24:1-14", "ORACLE_3", "מַה־טֹּבוּ אֹהָלֶיךָ", "mah-tovu ohalekha",
         "Bilʿam sees it is good in eyes of YHWH to bless Israel; not go as time after time to meet enchantments; sets face toward the wilderness; lifts eyes sees Israel dwelling by tribes; spirit of God on him; takes mashal: utterance of Bilʿam son of Beor utterance of the man opened of eye; utterance of hearer of sayings of God who sees vision of Shaddai falling and eyes uncovered: how good your tents Jacob your dwellings Israel; like wadis stretched like gardens by river like aloes YHWH planted like cedars by water; water drip from his buckets seed in many waters; his king higher than Agag his kingdom lifted; God brings him from Egypt like horns of wild ox for him; he eats nations his foes and their bones gnaws and his arrows strikes; he crouched lay like lion like lioness who raises him; who blesses you blessed who curses you cursed. Balak anger kindles at Bilʿam claps palms; Balak to Bilʿam: to curse my enemies I called you and behold you blessed bless these three times; now flee to your place; I said honor you and behold YHWH withheld you from honor. Bilʿam to Balak: did I not also to your messengers you sent to me speak saying if Balak gives me his house full silver gold I cannot pass mouth of YHWH to do good or evil from my heart; what YHWH speaks it I speak; now behold I go to my people; go I counsel you what this people does to your people in end of days."),
        ("STEP_N24_B1", "24:15-25", "ORACLE_4_STAR", "דָּרַךְ כּוֹכָב מִיַּעֲקֹב", "darakh kokhav mi-ya'akov",
         "Takes mashal: utterance of Bilʿam… who knows knowledge of Most High… I see him but not now behold him but not near; a star steps from Jacob a scepter rises from Israel smashes corners of Moab breaks down all sons of Sheth; Edom is possession Seir possession of his enemies Israel doing valor; from Jacob one rules and destroys remnant from city. Sees Amalek takes mashal: first of nations Amalek and his end to destruction. Sees Kenite: enduring your dwelling set in the rock your nest; but for Kayin be for burning until when Asshur takes you captive. Takes mashal: woe who lives from putting God this; ships from hand of Kittim afflict Asshur afflict Ever also he to destruction. Bilʿam rises goes returns to his place; also Balak goes on his way."),
      ],
      [("S_oracles_done", "Four mashals complete; star oracle"), ("S_bilam_gone", "Bilʿam and Balak depart")],
      [("EXPORT_mah_tovu", "מַה־טֹּבוּ אֹהָלֶיךָ", "mah-tovu ohalekha", "How good your tents Jacob"),
       ("EXPORT_kokhav_yaakov", "כּוֹכָב מִיַּעֲקֹב", "kokhav mi-ya'akov", "Star from Jacob / scepter from Israel")]),
    B("num_25_peor_pinchas", "25:1-19", 25, 1, 25, 19,
      "Baal Peor; Pinchas zeal; Midian foe (25:1–19)",
      "פִּינְחָס … קִנֵּא", "pinchas … kinne", "Pinchas … was zealous",
      ["num_24_oracles_3_4"], "narrative_fsm", "medium",
      "Israel settles Shittim whores with Moab daughters; sacrifices of their gods; joins Baal Peor; anger plague. Moses: leaders of people hang; judges kill men joined Baal Peor. Zimri brings Midianite woman; Pinchas spears both; plague stops 24000. Covenant of peace priesthood forever for zeal. Midianites as foes for Peor matter and Kozbi. (v.19 bridges to census.)",
      [
        ("STEP_N25_A1", "25:1-9", "PEOR_PLAGUE", "וַיָּחֶל הָעָם לִזְנוֹת", "va-yachel ha-am liznot",
         "Israel settles in Shittim; people begin to whore with daughters of Moab; they call the people to sacrifices of their gods; people eat bow to their gods; Israel joins to Baal Peor; anger of YHWH kindles in Israel; YHWH to Moses: take all heads of the people hang them to YHWH opposite the sun turn anger of YHWH from Israel; Moses to judges of Israel: kill each his men joined to Baal Peor. Behold a man of Israel comes brings near to his brothers the Midianite before eyes of Moses and all edah of Israel they weeping at entrance of Tent; Pinchas son of Eleazar son of Aaron the priest sees rises from midst of edah takes spear in hand; comes after the man of Israel to the chamber spears the two of them man of Israel and the woman to her belly; plague restrained from on Israel; dead in the plague 24000."),
        ("STEP_N25_B1", "25:10-19", "PINCHAS_COVENANT", "הִנְנִי נֹתֵן לוֹ … בְּרִית כְּהֻנַּת", "hineni noten lo … berit kehunnat",
         "YHWH to Moses: Pinchas son of Eleazar son of Aaron turned My wrath from on Israel in his being zealous My zeal in their midst I did not finish Israel in My zeal; therefore say: behold I give him My covenant of peace; it is for him and his seed after him covenant of priesthood forever because he was zealous for his God atoned for Israel. Name of man of Israel struck who was struck with Midianite: Zimri son of Salu prince of father's house of Shimoni; name of woman Midianite struck Kozbi daughter of Tzur head of peoples of father's house in Midian. YHWH to Moses: distress the Midianites strike them for they are foes to you in their wiles which they beguiled you on matter of Peor and on matter of Kozbi daughter of prince of Midian their sister who was struck on day of plague on matter of Peor. It was after the plague…"),
      ],
      [("S_peor", "Baal Peor crisis"), ("S_pinchas_berit", "Pinchas covenant of peace/priesthood")],
      [("EXPORT_baal_peor", "בַּעַל פְּעוֹר", "ba'al pe'or", "Baal Peor attachment crisis"),
       ("EXPORT_berit_shalom_pinchas", "בְּרִית שָׁלוֹם", "berit shalom", "Covenant of peace for Pinchas zeal")]),
    B("num_26_second_census", "26:1-65", 26, 1, 26, 65,
      "Second census after plague; land by lot; none of first census left (26:1–65)",
      "שְׂאוּ אֶת־רֹאשׁ … אַחֲרֵי הַמַּגֵּפָה", "se'u et-rosh … acharei ha-magefah", "Lift the head … after the plague",
      ["num_25_peor_pinchas", "num_01_tribe_counts"], "boot_steps", "thin",
      "After plague: count whole edah from 20+ by fathers houses able war; Moses Eleazar count plains of Moab. Tribe lists and clan names; Reuben Datan Aviram note; Korach sons not die; totals per tribe; all counted 601730. To these land divided by lot by names of tribes; many increase inheritance few decrease; by lot inherit. Levites counted month+ 23000 not among Israel no inheritance. Among these not a man of counted by Moses Aaron Sinai; for YHWH said die die in wilderness; none left except Caleb son of Yephunneh and Joshua bin Nun.",
      [
        ("STEP_N26_A1", "26:1-51", "CENSUS_II", "שְׂאוּ אֶת־רֹאשׁ כָּל־עֲדַת", "se'u et-rosh kol-adat",
         "After the plague YHWH to Moses and Eleazar son of Aaron: count whole edah of Israel from 20 years up by fathers houses all go out to army in Israel; Moses Eleazar speak with them in plains of Moab by Jordan of Jericho saying from 20 years up as YHWH commanded Moses and Israel who went out from land of Egypt. Tribe-by-tribe clan lists and counts (Reuben through Naphtali) with narrative notes on Datan Aviram Korach; these counted of Israel 601730."),
        ("STEP_N26_B1", "26:52-65", "LOT_LAND_LEVI", "לָאֵלֶּה תֵּחָלֵק … בְּגוֹרָל", "la-eleh techalek … be-goral",
         "To these the land is divided in inheritance by number of names; for many increase inheritance for few decrease inheritance each according to his counted ones given inheritance; but by lot land is divided by names of tribes of fathers inherit; by mouth of the lot inheritance divided between many and few. These counted of Levi by their clans… every male month old+ 23000; for not counted among Israel for no inheritance given them among Israel. These counted of Moses and Eleazar the priest who counted Israel in plains of Moab by Jordan of Jericho; among these not was a man of counted of Moses and Aaron the priest who counted Israel in wilderness of Sinai; for YHWH said to them die die in the wilderness; not left of them a man except Caleb son of Yephunneh and Joshua bin Nun."),
      ],
      [("S_census_ii", "Second census 601730"), ("S_lot_inheritance", "Land by lot scaled to counts"), ("S_gen_dead", "Sinai census generation gone except two")],
      [("EXPORT_pekudei_ii", "פְּקוּדִים בְּעַרְבוֹת מוֹאָב", "pekudim be-arvot mo'av", "Second census plains of Moab"),
       ("EXPORT_goral_aretz", "בְּגוֹרָל תֵּחָלֵק", "be-goral techalek", "Land divided by lot")]),
    B("num_27_zelophehad_joshua", "27:1-23", 27, 1, 27, 23,
      "Daughters of Zelophehad; Moses view land; Joshua appointed (27:1–23)",
      "בְּנוֹת צְלָפְחָד — יְהוֹשֻׁעַ", "benot tzelofchad — yehoshua", "Daughters of Zelophehad — Joshua",
      ["num_26_second_census"], "decision_table", "primary",
      "Daughters of Zelophehad Menasheh: father died in wilderness not in Korach edah; no sons; give possession among uncles. YHWH: right they speak; transfer father inheritance to them. Inheritance order: son; if no son daughter; if no daughter brothers; if no brothers brothers of father; nearest kin. Moses up Avarim mountain see land; gathered as Aaron for Meribah. Appoint Joshua man of spirit lean hand; stand before Eleazar whole edah; give from your majesty; ask Urim before YHWH go out come in. Moses does.",
      [
        ("STEP_N27_A1", "27:1-11", "HEIRESSES", "כֵּן בְּנוֹת צְלָפְחָד דֹּבְרֹת", "ken benot tzelofchad dovrot",
         "Daughters of Zelophehad son of Chefer Gilead Makhir Menasheh of families of Menasheh son of Joseph draw near: Machlah Noah Choglah Milkah Tirzah; stand before Moses Eleazar princes all edah entrance of Tent: our father died in wilderness he was not in edah gathered on YHWH in edah of Korach for in his sin he died sons he had not; why name of our father withdrawn from midst of his family for no son; give us possession among brothers of our father. Moses brings their mishpat near before YHWH. YHWH to Moses: right daughters of Zelophehad speak; give give them possession of inheritance among brothers of their father transfer inheritance of their father to them. To Israel speak: when a man dies son he has not transfer his inheritance to his daughter; if no daughter give inheritance to his brothers; if no brothers give to brothers of his father; if no brothers of father give to relative nearest to him from his family possess it; be for Israel statute of mishpat as YHWH commanded Moses."),
        ("STEP_N27_B1", "27:12-23", "JOSHUA", "קַח לְךָ אֶת־יְהוֹשֻׁעַ", "kach lekha et-yehoshua",
         "YHWH to Moses: go up to this mountain of Avarim see the land I give Israel; see it be gathered to your peoples also you as Aaron your brother was gathered; as you rebelled My mouth in wilderness of Zin in quarrel of edah to sanctify Me at water before their eyes; they are waters of Merivat Kadesh wilderness of Zin. Moses: let YHWH God of spirits of all flesh appoint a man over the edah who goes out before them comes in before them who leads them out brings them in not be edah of YHWH like flock no shepherd. YHWH: take to you Joshua bin Nun a man in whom is spirit lean your hand on him; stand him before Eleazar the priest before all edah command him before their eyes; give from your majesty on him so that all edah of Israel hear; before Eleazar the priest he stands asks for him mishpat of the Urim before YHWH; at his mouth they go out at his mouth they come in he and all Israel with him all the edah. Moses does as YHWH commanded; takes Joshua stands him before Eleazar the priest before all edah; leans hands on him commands him as YHWH spoke by hand of Moses."),
      ],
      [("S_heiress_order", "Inheritance order with daughters"), ("S_joshua_appointed", "Joshua commissioned with Urim")],
      [("EXPORT_benot_tzelofchad", "בְּנוֹת צְלָפְחָד", "benot tzelofchad", "Daughters inherit when no son"),
       ("EXPORT_seder_nachalah", "סֵדֶר נַחֲלָה", "seder nachalah", "Inheritance cascade: son daughter brothers…"),
       ("EXPORT_yehoshua_samakh", "סְמִיכַת יְהוֹשֻׁעַ", "semikhat yehoshua", "Joshua lean-hand succession")],
      [("IF man dies with no son", "THEN inheritance to daughter then brothers then…"),
       ("IF Moses exit", "THEN Joshua with spirit; lean hand; Eleazar Urim for go out/in")]),
    B("num_28_daily_shabbat_rosh", "28:1-15", 28, 1, 28, 15,
      "Tamid daily; Shabbat musaf; Rosh Chodesh (28:1–15)",
      "עֹלַת תָּמִיד — רָאשֵׁי חָדְשֵׁיכֶם", "olat tamid — rashei chodesheikhem", "Continual burnt offering — heads of your months",
      ["num_27_zelophehad_joshua", "lev_23_spring_festivals", "exo_29_investiture"], "decision_table", "primary",
      "My offering food of my fires: two lambs yearling day continual olah; morning one evening one; tenth ephah fine flour quarter hin beaten oil; nesekh quarter hin wine per lamb; sanctuary for nesekh shekhar to YHWH. Shabbat: two lambs + minchah nesekh besides continual. Heads of months: two bulls one ram seven lambs; minchah scales; nesekh; one goat chatat besides continual.",
      [
        ("STEP_N28A_A1", "28:1-8", "TAMID", "שְׁנַיִם לַיּוֹם עֹלָה תָמִיד", "shenayim la-yom olah tamid",
         "Command Israel My offering My food for My fires My pleasant scent keep to bring near to Me in its appointed time; say to them: this is the isheh you bring near to YHWH: lambs yearling whole two a day olah continual; the one lamb make in morning and the second lamb make between the evenings; tenth of ephah fine flour for minchah mixed in quarter hin of beaten oil; olah continual made at Mount Sinai for pleasant scent isheh to YHWH; its nesekh quarter hin for the one lamb in the sanctuary nesekh of shekhar pour to YHWH; the second lamb between the evenings like minchah of morning and like its nesekh make isheh pleasant scent to YHWH."),
        ("STEP_N28A_B1", "28:9-15", "SHABBAT_ROSH", "וּבְיוֹם הַשַּׁבָּת … וּבְרָאשֵׁי חָדְשֵׁיכֶם", "u-ve-yom ha-shabbat … u-ve-rashei chodesheikhem",
         "On day of Shabbat two lambs yearling whole and two tenths fine flour minchah mixed in oil and its nesekh; olah of Shabbat on its Shabbat besides olah of continual and its nesekh. Heads of your months bring near olah to YHWH: bulls of herd two ram one lambs yearling whole seven; three tenths fine flour minchah mixed oil for the one bull; two tenths for the one ram; tenth tenth for each lamb of seven lambs; one goat of goats for chatat to YHWH besides olah of continual made and its nesekh."),
      ],
      [("S_tamid", "Daily tamid schedule"), ("S_shabbat_musaf", "Shabbat additional"), ("S_rosh_chodesh", "New moon offerings")],
      [("EXPORT_olat_tamid", "עֹלַת תָּמִיד", "olat tamid", "Twice-daily continual burnt offering"),
       ("EXPORT_musaf_shabbat", "עֹלַת שַׁבָּת", "olat shabbat", "Shabbat musaf two lambs"),
       ("EXPORT_rosh_chodesh", "רָאשֵׁי חֳדָשִׁים", "rashei chodashim", "New-month bull/ram/lambs + goat")],
      [("IF every day", "THEN two lambs tamid morning and evening + minchah nesekh"),
       ("IF Shabbat", "THEN + two lambs musaf besides tamid"),
       ("IF Rosh Chodesh", "THEN two bulls ram seven lambs + goat chatat besides tamid")],
      imports_en="Exod 29 tamid seed; Lev 23 mo'adim background."),
    B("num_28_pesach_shavuot", "28:16-31", 28, 16, 28, 31,
      "Pesach/matzot musaf; Shavuot firstfruits (28:16–31)",
      "בַּחֹדֶשׁ הָרִאשׁוֹן — בְּיוֹם הַבִּכּוּרִים", "ba-chodesh ha-rishon — be-yom ha-bikkurim", "In the first month — on the day of firstfruits",
      ["num_28_daily_shabbat_rosh", "lev_23_spring_festivals"], "decision_table", "primary",
      "14th first month pesach; 15th feast seven days matzot; day 1 mikra kodesh no work of service; offerings seven days: two bulls one ram seven lambs + goat chatat besides tamid. Day of firstfruits new minchah weeks: same animal set + goat; be whole for you and nesekh.",
      [
        ("STEP_N28B_A1", "28:16-25", "PESACH_MATZOT", "וּבַחֹדֶשׁ הָרִאשׁוֹן … מַצּוֹת", "u-va-chodesh ha-rishon … matzot",
         "In first month 14th day pesach to YHWH; 15th day of this month feast seven days matzot eaten; day first mikra kodesh all work of service not do; bring near isheh olah to YHWH bulls of herd two ram one lambs yearling seven whole they are for you; their minchah fine flour mixed oil three tenths for bull two tenths for ram; tenth tenth for each lamb of seven lambs; one goat chatat to atone for you; besides olah of morning which is olah of continual make these; like these make for the day seven days bread of isheh pleasant scent to YHWH besides olah of continual made and its nesekh; day seventh mikra kodesh all work of service not do."),
        ("STEP_N28B_B1", "28:26-31", "SHAVUOT", "וּבְיוֹם הַבִּכּוּרִים", "u-ve-yom ha-bikkurim",
         "On day of firstfruits when you bring near new minchah to YHWH in your weeks mikra kodesh all work of service not do; bring near olah for pleasant scent to YHWH bulls of herd two ram one lambs yearling seven; their minchah fine flour mixed oil three tenths for one bull two tenths for one ram; tenth tenth for each lamb of seven lambs; one goat to atone for you; besides continual olah and its minchah make be whole for you and their nesekh."),
      ],
      [("S_pesach_musaf", "Pesach week musafim"), ("S_shavuot_musaf", "Shavuot firstfruits musaf")],
      [("EXPORT_musaf_pesach", "מוּסַף פֶּסַח", "musaf pesach", "Seven-day matzot musaf set"),
       ("EXPORT_yom_bikkurim", "יוֹם הַבִּכּוּרִים", "yom ha-bikkurim", "Day of firstfruits / weeks offering")]),
    B("num_29_fall_festivals", "29:1-39", 29, 1, 29, 39,
      "Tishri: teruah; kippurim; Sukkot day-by-day; atzeret (29:1–39)",
      "יוֹם תְּרוּעָה — חַג — עֲצֶרֶת", "yom teru'ah — chag — atzeret", "Day of blast — feast — assembly",
      ["num_28_pesach_shavuot", "lev_23_fall_festivals"], "decision_table", "primary",
      "Month 7 day 1: teruah mikra kodesh; one bull one ram seven lambs + goat. Day 10: afflict; same set + goat of kippurim besides chatat ha-kippurim. Day 15 feast seven days: day1 thirteen bulls two rams fourteen lambs + goat; days 2–7 bulls decrease by one; day 8 atzeret one bull one ram seven lambs + goat. These besides vows freewill olot minchot nesakhim shelamim.",
      [
        ("STEP_N29_A1", "29:1-11", "TERUAH_KIPPUR", "וּבַחֹדֶשׁ הַשְּׁבִיעִי … בֶּעָשׂוֹר", "u-va-chodesh ha-shevi'i … be-asor",
         "Month seventh day one mikra kodesh all work of service not do; day of teruah it is for you; make olah pleasant scent: bull one ram one lambs yearling whole seven; minchah scales; one goat chatat to atone besides olah of continual. On tenth of this seventh month mikra kodesh afflict your souls all work not do; bring near olah pleasant scent bull one ram one lambs seven; minchah; one goat chatat besides chatat of the kippurim and olah of continual."),
        ("STEP_N29_B1", "29:12-34", "SUKKOT_DAYS", "וּבַחֲמִשָּׁה עָשָׂר … פָּרִים", "u-va-chamishah asar … parim",
         "15th of seventh month mikra kodesh no work of service; feast to YHWH seven days; day 1: thirteen bulls two rams fourteen lambs + goat + minchah scales besides tamid; day 2: twelve bulls … through day 7: seven bulls two rams fourteen lambs each day with goat chatat and minchah/nesekh scales; pattern decreases bulls by one each day."),
        ("STEP_N29_C1", "29:35-39", "ATZERET", "בַּיּוֹם הַשְּׁמִינִי עֲצֶרֶת", "ba-yom ha-shemini atzeret",
         "Day eighth atzeret for you all work of service not do; bring near olah pleasant scent bull one ram one lambs seven; minchah nesekh; one goat chatat besides olah of continual. These you make to YHWH in your mo'adim besides your vows and freewill your olot minchot nesakhim and shelamim."),
      ],
      [("S_tishri_musafim", "Full Tishri musaf calendar loaded")],
      [("EXPORT_yom_teruah", "יוֹם תְּרוּעָה", "yom teru'ah", "Day of blast offerings"),
       ("EXPORT_sukkot_parim", "פָּרֵי הֶחָג", "parei he-chag", "Sukkot bulls decreasing 13→7"),
       ("EXPORT_shemini_atzeret", "עֲצֶרֶת", "atzeret", "Eighth-day assembly offerings")]),
    B("num_30_vows", "30:1-17", 30, 1, 30, 17,
      "Vows: man binds; father/husband silence or annul (30:1–17)",
      "אִישׁ כִּי־יִדֹּר — הֵפֵר יָפֵר", "ish ki-yiddor — hefer yafer", "When a man vows — he may annul",
      ["num_29_fall_festivals", "lev_27_vows_valuations"], "decision_table", "primary",
      "Heads of tribes: man vows vow or oath bind on soul not profane word do all from mouth. Woman youth in father house: if father hears silence stands; if father restrains day he hears not stand YHWH forgives. Married: husband silence stands; husband restrains day hears voids YHWH forgives. Widow divorcee: all binds on soul stands. If husband voids after day he hears bears her iniquity. These chukkim husband wife father daughter youth father house.",
      [
        ("STEP_N30_A1", "30:1-9", "MAN_YOUTH_WIFE", "אִישׁ כִּי־יִדֹּר נֶדֶר", "ish ki-yiddor neder",
         "Moses to heads of tribes of Israel: this is the word YHWH commanded. When a man vows a vow to YHWH or swears an oath to bind a bond on his soul not profane his word; as all that goes from his mouth he does. Also a woman when she vows a vow to YHWH binds a bond in house of her father in her youth; hears her father her vow and her bond which she bound on her soul and her father is silent to her all her vows stand all bond she bound on her soul stands; but if her father restrains her on day of his hearing all her vows and bonds which she bound on her soul not stand; YHWH forgives her for her father restrained her. If being she is to a man her vows on her or utterance of her lips which she bound on her soul; hears her husband on day of his hearing is silent to her her vows stand her bonds stand; if on day of her husband's hearing he restrains her he voids her vow which is on her and utterance of her lips which she bound on her soul YHWH forgives her."),
        ("STEP_N30_B1", "30:10-17", "WIDOW_HUSBAND", "וְנֵדֶר אַלְמָנָה וּגְרוּשָׁה", "ve-neder almanah u-gerushah",
         "Vow of a widow and a divorcee all which she bound on her soul stands on her. If house of her husband she vowed or bound bond on her soul by oath; husband heard silent to her not restrained her all her vows stand all bond she bound on her soul stands; if voiding her husband voids them on day of his hearing all going from her lips to her vows to bond of her soul not stand; her husband voided them YHWH forgives her. Every vow every oath of bond to afflict soul her husband establishes it her husband voids it; if silent silent her husband day to day establishes all her vows or all her bonds which on her; he established them for he was silent to her on day of his hearing; if voiding he voids them after his hearing he bears her iniquity. These the chukkim which YHWH commanded Moses between a man and his wife between a father and his daughter in her youth house of her father."),
      ],
      [("S_vow_authority", "Vow establishment/annulment matrix")],
      [("EXPORT_neder_ish", "לֹא יַחֵל דְּבָרוֹ", "lo yachel devaro", "Man must not profane his vow word"),
       ("EXPORT_hefer_av_baal", "הֵפֵר אָב / בַּעַל", "hefer av / ba'al", "Father/husband same-day annulment")],
      [("IF adult man vows", "THEN must do; not profane word"),
       ("IF daughter in youth father hears and silences", "THEN vow stands; if restrains same day THEN voided forgiven"),
       ("IF wife husband silences", "THEN stands; if restrains day of hearing THEN voided"),
       ("IF widow or divorcee", "THEN her bonds stand")]),
    B("num_31_midian", "31:1-54", 31, 1, 31, 54,
      "War on Midian; purify spoil; divide; officer gifts (31:1–54)",
      "נְקֹם נִקְמַת … מִדְיָן", "nekom nikmat … midyan", "Avenge the vengeance … Midian",
      ["num_30_vows", "num_25_peor_pinchas", "num_19_parah"], "narrative_fsm", "medium",
      "Avenge Israel of Midian then gathered. Thousand per tribe with Pinchas vessels holy trumpets. Kill males kings Bilʿam; take women children cattle. Moses angry: keep alive women who caused Peor? Kill every male child every woman known man; keep girls. Camp outside seven days purify. Eleazar: statute of war — fire items through fire + mei niddah; else water. Divide spoil half warriors half edah; tax YHWH 1/500 from warriors to Eleazar; 1/50 from edah half to Levites. Count: no missing; officers bring gold atonement; 16750 shekels to Tent.",
      [
        ("STEP_N31_A1", "31:1-18", "WAR_CAPTIVES", "הֵחָלְצוּ … אֶלֶף לַמַּטֶּה", "hechaltzu … elef la-matteh",
         "YHWH to Moses: avenge vengeance of Israel from Midian after be gathered to your peoples; Moses to people: arm from yourselves men for army be on Midian give vengeance of YHWH on Midian; thousand per tribe all tribes of Israel send to army; from thousands of Israel thousand per tribe 12000 armed for army; Moses sends them thousand per tribe to army them and Pinchas son of Eleazar the priest to army vessels of holy and trumpets of teruah in his hand. They array on Midian as YHWH commanded Moses kill every male; kings of Midian kill on their slain Evi Rekem Tzur Chur Reva five kings of Midian; Bilʿam son of Beor kill by sword; Israel take captive women of Midian children all their beasts flock wealth plunder; all their cities settlements castles burn fire; take all spoil all booty man beast; bring to Moses Eleazar edah to camp plains of Moab. Moses Eleazar princes go out to meet them outside camp; Moses angry at officers: have you kept alive every female; behold they were to Israel by word of Bilʿam to trespass against YHWH on matter of Peor plague on edah of YHWH; now kill every male among the children and every woman who has known man by lying with male kill; all children among women who have not known lying with male keep alive for yourselves."),
        ("STEP_N31_B1", "31:19-47", "PURIFY_DIVIDE", "וְאַתֶּם חֲנוּ מִחוּץ … מֵי נִדָּה", "ve-attem chanu mi-chutz … mei niddah",
         "You camp outside camp seven days; all who killed a soul all who touched slain purify day three and day seven you and your captives; every garment skin work goats wood purify. Eleazar to men of army: statute of torah YHWH commanded Moses: only gold silver copper iron tin lead every thing that comes in fire pass in fire clean only with water of niddah it purifies; all that not come in fire pass in water; wash clothes day seven clean after come to camp. YHWH to Moses: count heads of booty captive man beast you Eleazar heads of fathers of edah; divide booty half takers of army who went out half all edah; raise tax to YHWH from men of war who went out to army one soul from five hundred from man cattle donkeys flock; take from their half give to Eleazar the priest terumah of YHWH; from half of Israel take one drawn from fifty from man cattle donkeys flock all beasts give them to Levites keepers of charge of mishkan of YHWH. Moses Eleazar do as commanded; booty totals listed; half of army and tax to Eleazar; half of Israel and draw to Levites."),
        ("STEP_N31_C1", "31:48-54", "OFFICER_ATONEMENT", "וַיִּקְרְבוּ … כְּלֵי זָהָב", "va-yikrevu … kelei zahav",
         "Officers of thousands of army captains of thousands captains of hundreds draw near Moses; your servants lifted heads of men of war who are in our hand not missed from us a man; we bring near offering of YHWH what each found vessels of gold armlet bracelet ring earring torus to atone for our souls before YHWH; Moses Eleazar take gold from them all work of vessel; all gold of terumah 16750 shekels from captains of thousands hundreds; men of army plundered each for himself; Moses Eleazar take gold from captains bring to Tent of Meeting memorial for Israel before YHWH."),
      ],
      [("S_midian_war", "Midian vengeance war done"), ("S_spoil_rules", "Fire/water purify; half tax rules")],
      [("EXPORT_nikmat_midyan", "נִקְמַת מִדְיָן", "nikmat midyan", "Vengeance war on Midian"),
       ("EXPORT_spoil_half_tax", "מֶחֱצָה וּמֶכֶס", "mechetzah u-mekhes", "Spoil halves + 1/500 and 1/50 taxes")]),
    B("num_32_gad_reuben", "32:1-42", 32, 1, 32, 42,
      "Gad Reuben (half Menasheh) take east; condition of arms (32:1–42)",
      "נַעְבִירֵם לִפְנֵי … הֶחָלוּץ", "na'avirem lifnei … he-chalutz", "We will cross them before … armed",
      ["num_31_midian", "num_21_snakes_conquest"], "decision_table", "medium",
      "Gad Reuben many cattle see land Yazer Gilead; ask not cross Jordan. Moses recalls spies sin. They: build pens cities; we arm before Israel until each inherits; not return until… Moses: if you do this armed before YHWH — hold; if not sin finds you. Build Dibon etc; half Menasheh also takes Gilead; cities renamed.",
      [
        ("STEP_N32_A1", "32:1-15", "REQUEST_WARNING", "הָאָרֶץ אֲשֶׁר הִכָּה … אַל־תַּעֲבִרֵנוּ", "ha-aretz asher hikkah … al-ta'avirenu",
         "Much cattle to sons of Reuben Gad very mighty; see land of Yazer land of Gilead place place for cattle; come Moses Eleazar princes: Atarot Dibon Yazer Nimrah Heshbon Elealeh Sevam Nevo Beon — land YHWH struck before edah of Israel is land of cattle; your servants have cattle; if we find favor give this land to your servants for possession; do not make us cross the Jordan. Moses to sons of Gad Reuben: shall your brothers come to war and you sit here; why restrain heart of Israel from passing to land YHWH gives them; thus your fathers when I sent from Kadesh Barnea to see land… and YHWH anger kindled… behold you rise in place of your fathers culture of sinful men to add again to anger of YHWH at Israel; if you turn from after Him He again leave them in wilderness you destroy all this people."),
        ("STEP_N32_B1", "32:16-32", "CONDITION", "אֲנַחְנוּ נַחֲלֹץ … לִפְנֵי יְהוָה", "anachnu nachaletz … lifnei YHWH",
         "They draw near: pens of flock we build for our cattle here cities for our children; we arm hurry before Israel until we bring them to their place; our children dwell in cities of fortification from face of dwellers of land; not return to our houses until Israel inherits each his inheritance; for not inherit with them across the Jordan and beyond for our inheritance comes to us across the Jordan east. Moses: if you do this thing if you arm before YHWH for the war; every armed of you crosses the Jordan before YHWH until He dispossesses His enemies from before Him; land subdued before YHWH after you return be clean from YHWH and from Israel this land for possession before YHWH; if not do so behold you sinned to YHWH know your sin which finds you; build for you cities for your children pens for your flock what goes from your mouth do. Sons of Gad Reuben to Moses: your servants do as my lord commands; our children wives flocks all cattle there in cities of Gilead; your servants cross every armed for army before YHWH to the war as my lord speaks. Moses commands Eleazar Joshua heads of fathers of tribes of Israel; if sons of Gad Reuben cross with you the Jordan every armed for war before YHWH land subdued before you give them land of Gilead for possession; if not armed they cross with you they have possession in your midst in land of Canaan. Sons of Gad Reuben answer: what YHWH spoke to your servants so we do; we cross armed before YHWH land of Canaan our possession of inheritance across the Jordan."),
        ("STEP_N32_C1", "32:33-42", "GRANT_CITIES", "וַיִּתֵּן לָהֶם מֹשֶׁה … מְנַשֶּׁה", "va-yitten lahem moshe … menasheh",
         "Moses gives to them sons of Gad sons of Reuben half tribe of Menasheh son of Joseph kingdom of Sihon king of Amorites kingdom of Og king of Bashan land by its cities borders cities of the land around. Sons of Gad build Dibon Atarot Aroer… rename. Sons of Reuben build Heshbon Elealeh… Nebo becomes other names. Sons of Makhir son of Menasheh go Gilead take it drive Amorite; Moses gives Gilead to Makhir settles; Yair son of Menasheh takes their villages calls them Chavvot Yair; Novach takes Kenat daughters calls Novach his name."),
      ],
      [("S_east_settlement", "Transjordan tribes settled under war condition")],
      [("EXPORT_gad_reuben_menasheh", "גָּד רְאוּבֵן חֲצִי מְנַשֶּׁה", "gad re'uven chatzi menasheh", "East-bank inheritance under arms condition"),
       ("EXPORT_chalutz_lifnei", "חָלוּץ לִפְנֵי יְהוָה", "chalutz lifnei YHWH", "Armed before YHWH until land subdued")]),
    B("num_33_journeys", "33:1-56", 33, 1, 33, 56,
      "Itinerary Egypt to plains of Moab; drive out command (33:1–56)",
      "אֵלֶּה מַסְעֵי — הוֹרַשְׁתֶּם", "eleh mas'ei — horashtem", "These are the journeys — you shall dispossess",
      ["num_32_gad_reuben"], "boot_steps", "thin",
      "Moses writes their goings out by journeys at mouth of YHWH; full station list from Rameses to plains of Moab by Jordan Jericho. Command: cross Jordan to Canaan drive all dwellers destroy figures molten high places; possess settle land by lot by families; if not drive remaining be thorns in eyes pricks in sides trouble you on land; as I thought to do to them I do to you.",
      [
        ("STEP_N33_A1", "33:1-49", "ITINERARY", "אֵלֶּה מַסְעֵי בְנֵי־יִשְׂרָאֵל", "eleh mas'ei benei-yisrael",
         "These journeys of Israel who went out from land of Egypt by their armies by hand of Moses Aaron; Moses writes their goings out by their journeys at mouth of YHWH; these their journeys by their goings out. Station list: Rameses Sukkot… wilderness Sinai… Kadesh… Mount Hor Aaron dies year 40 month 5 day 1… plains of Moab by Jordan of Jericho from Beit ha-Yeshimot to Avel Shittim."),
        ("STEP_N33_B1", "33:50-56", "DRIVE_OUT", "הוֹרֵשׁ תּוֹרִישׁוּ … וְאִם־לֹא", "horesh torishu … ve-im-lo",
         "YHWH to Moses plains of Moab by Jordan of Jericho: speak Israel: when you cross the Jordan to land of Canaan: drive out all dwellers of the land from before you; destroy all their figured stones all their molten images destroy; all their high places devastate; possess the land settle in it for to you I give the land to possess it; inherit the land by lot by your families; many increase inheritance few decrease inheritance; to where lot goes for him there his; by tribes of your fathers inherit. If you do not drive out dwellers of the land from before you: it shall be those you leave of them be as thorns in your eyes as pricks in your sides they shall trouble you on the land which you settle in; it shall be as I thought to do to them I do to you."),
      ],
      [("S_mas'ei_list", "Full journey registry written"), ("S_drive_out_command", "Dispossess command with thorn warning")],
      [("EXPORT_mas'ei", "מַסְעֵי", "mas'ei", "Recorded wilderness itinerary"),
       ("EXPORT_horish", "הוֹרֵשׁ תּוֹרִישׁוּ", "horesh torishu", "Drive out inhabitants or face thorns")]),
    B("num_34_borders", "34:1-29", 34, 1, 34, 29,
      "Land borders; princes for allotment (34:1–29)",
      "זֹאת הָאָרֶץ … לִגְבֻלֹתֶיהָ", "zot ha-aretz … li-gevuloteha", "This is the land … by its borders",
      ["num_33_journeys"], "boot_steps", "thin",
      "Land of Canaan by borders: south from Zin along Edom to Sea of Reeds… west Great Sea; north mountain Hor Lebo-Hamat Zedad… east Jordan Sea of Salt. Moses commands Israel: this land inherit by lot which YHWH commanded give nine tribes half Menasheh; for tribe of Reuben Gad half Menasheh took inheritance across Jordan east. These names of men who inherit for you: Eleazar Joshua; one prince per tribe listed.",
      [
        ("STEP_N34_A1", "34:1-15", "BORDERS", "זֹאת הָאָרֶץ אֲשֶׁר תִּפֹּל", "zot ha-aretz asher tippol",
         "YHWH to Moses: command Israel: when you come to land of Canaan this the land that falls to you inheritance land of Canaan by its borders; south corner from wilderness of Zin on hands of Edom; south border from end of Salt Sea east… outlet to Sea. West border Great Sea and border; this west border. North border from Great Sea mark for you Mount Hor; from Mount Hor mark to Lebo-Hamat end of border Zedad… east border from Chatzar Einan Shefam… down to Jordan outlets at Salt Sea; this is land for you by its borders around. Moses commands Israel: this the land which you inherit by lot which YHWH commanded to give to nine tribes and half tribe; for tribe of sons of Reuben by fathers houses and tribe of sons of Gad by fathers houses half tribe of Menasheh took their inheritance; two tribes half tribe took inheritance across from Jordan of Jericho east toward sunrise."),
        ("STEP_N34_B1", "34:16-29", "ALLOTMENT_PRINCES", "אֵלֶּה שְׁמוֹת הָאֲנָשִׁים", "eleh shemot ha-anashim",
         "YHWH to Moses: these names of men who inherit for you the land: Eleazar the priest and Joshua bin Nun; one prince one prince from a tribe take to inherit the land; these names of the men: for Yehudah Caleb son of Yephunneh; for Shimon… (list through Naphtali); these whom YHWH commanded to inherit Israel in land of Canaan."),
      ],
      [("S_borders_set", "Canaan border definition"), ("S_allotment_team", "Eleazar Joshua + tribal princes")],
      [("EXPORT_gevul_kena'an", "גְּבוּל כְּנַעַן", "gevul kena'an", "Canonical land borders"),
       ("EXPORT_nasi_nachalah", "נָשִׂיא לַנַּחֲלָה", "nasi la-nachalah", "Prince per tribe for allotment")]),
    B("num_35_refuge_cities", "35:1-34", 35, 1, 35, 34,
      "Levite cities; cities of refuge; murder vs manslaughter (35:1–34)",
      "עָרֵי מִקְלָט — רֹצֵחַ", "arei miklat — rotzeach", "Cities of refuge — killer",
      ["num_34_borders", "num_18_priest_levite_dues", "exo_21_ox_pit"], "decision_table", "primary",
      "Give Levites cities to dwell from inheritance + migrash; 48 cities; 6 of them refuge. Refuge for unintentional killer from goel ha-dam until stands before edah mishpat. Three west three east Jordan. Distinction: iron wood stone hand murder die; if sudden without enmity then edah judge between killer and goel; restore to refuge until death of high priest; if goes out goel may kill no blood. Not take ransom for soul of murderer to die; not ransom to return from refuge before high priest death. Not pollute land; blood pollutes; land only atoned by blood of who shed; not defile land I dwell in midst of Israel.",
      [
        ("STEP_N35_A1", "35:1-8", "LEVITE_CITIES", "תְּנוּ לַלְוִיִּם … עָרִים", "tenu la-leviyyim … arim",
         "YHWH plains of Moab: command Israel give to Levites from inheritance of their possession cities to dwell and migrash for cities around them give to Levites; cities to dwell migrash for cattle property all beasts; migrash of cities you give Levites from wall of city outward thousand cubit around; measure outside city east side two thousand… city in middle this is for them migrash of cities. Cities give Levites six cities of refuge to flee there the killer; upon them give forty-two city; all cities give Levites forty-eight city them and their migrash; cities which give from possession of Israel from many many from few few each according to his inheritance which inherits give from his cities to Levites."),
        ("STEP_N35_B1", "35:9-28", "MIKLAT_RULES", "וְהִקְרִיתֶם לָכֶם עָרִים", "ve-hikritem lakhem arim",
         "Speak Israel: when cross Jordan to land of Canaan; select for you cities cities of refuge they are for you; flee there killer who strikes a soul by error; cities be for you for refuge from goel not die the killer until he stands before the edah for mishpat; cities which give six cities of refuge; three cities give across the Jordan three cities give in land of Canaan; cities of refuge they are; for Israel for ger for toshav among them these six cities for refuge for fleeing there all who strike a soul by error. If with iron instrument strikes dies murderer he; death die the murderer; if with stone hand by which one dies strikes dies murderer; if with wood hand instrument of death strikes dies murderer; goel of the blood he kills the murderer when he meets him he kills him. If in hatred pushes or throws on him in lying in wait dies; or in enmity strikes with hand dies death die the striker murderer; goel of blood kills the murderer when meets. If in an instant without enmity pushes or throws on him any instrument without lying in wait; or any stone by which dies without seeing drops on him dies he not enemy not seeking his harm; edah judges between striker and goel of blood by these mishpatim; edah rescues the killer from hand of goel of blood; edah returns him to city of his refuge which he fled; dwell in it until death of the high priest who was anointed with holy oil; if going out the killer goes out border of city of his refuge which he flees; goel of blood finds him outside border of city of his refuge; goel of blood kills the killer no blood for him; for in city of his refuge he dwells until death of the high priest; after death of high priest returns the killer to land of his possession."),
        ("STEP_N35_C1", "35:29-34", "NO_RANSOM_BLOOD", "וְלֹא־תִקְחוּ כֹפֶר … דָּם", "ve-lo-tikchu kofer … dam",
         "These for you statute of mishpat generations dwellings; all who strike a soul by mouth of witnesses he kills the killer; one witness not answer in a soul to die. Not take ransom for soul of a murderer who is wicked to die for death he dies; not take ransom to flee to city of his refuge to return to dwell in land until death of the priest. Not pollute the land which you are in for the blood it pollutes the land; for the land not atoned for blood which is shed in it except by blood of who shed it; not defile the land which you settle in whose midst I dwell; for I YHWH dwell in midst of Israel."),
      ],
      [("S_arei_miklat", "Six refuge cities + 42 Levite"), ("S_rotzeach_matrix", "Murder vs error + high-priest gate")],
      [("EXPORT_arei_miklat", "עָרֵי מִקְלָט", "arei miklat", "Cities of refuge for unwitting killer"),
       ("EXPORT_goel_ha-dam", "גֹּאֵל הַדָּם", "go'el ha-dam", "Blood redeemer"),
       ("EXPORT_until_kohen_gadol", "עַד־מוֹת הַכֹּהֵן הַגָּדֹל", "ad-mot ha-kohen ha-gadol", "Stay in refuge until high priest dies")],
      [("IF kill with iron/stone/wood hand intentionally", "THEN murderer dies; goel may kill"),
       ("IF kill by error without enmity", "THEN flee miklat; edah judges; stay until high priest dies"),
       ("IF leave miklat early", "THEN goel may kill without bloodguilt"),
       ("IF murder", "THEN no ransom instead of death")],
      imports_en="Exod 21 homicide seeds; Lev blood pollution themes; Num 18 Levite no land → cities."),
    B("num_36_heiresses", "36:1-13", 36, 1, 36, 13,
      "Heiresses marry within tribe; close of Numbers commands (36:1–13)",
      "לְטוֹב בְּעֵינֵיהֶם תִּהְיֶינָה לְנָשִׁים", "le-tov be-eineihem tihyenah le-nashim", "As is good in their eyes they shall be wives",
      ["num_35_refuge_cities", "num_27_zelophehad_joshua"], "decision_table", "primary",
      "Heads of Gilead Menasheh: if daughters of Zelophehad marry sons of other tribe inheritance moves; jubilee transfers. Moses at YHWH mouth: right tribe of Joseph; every daughter possessing inheritance marry to one of family of tribe of her father; so inheritance not turn tribe to tribe. Daughters of Zelophehad do so marry cousins sons of uncles of Menasheh; inheritance on tribe of family of father. These mitzvot mishpatim YHWH commanded by Moses to Israel plains of Moab by Jordan of Jericho.",
      [
        ("STEP_N36_A1", "36:1-4", "PROBLEM", "וְהָיוּ … יוֹבֵל", "ve-hayu … yovel",
         "Heads of fathers of family of sons of Gilead son of Makhir son of Menasheh of families of sons of Joseph draw near speak before Moses princes heads of fathers of Israel; my lord commanded by YHWH to give the land inheritance by lot to Israel; my lord commanded by YHWH to give inheritance of Zelophehad our brother to his daughters; if they are to one of sons of tribes of Israel for wives their inheritance is taken from inheritance of our fathers added on inheritance of tribe which they are to; from lot of our inheritance taken; when the jubilee is for Israel their inheritance added on inheritance of tribe which they are to; from inheritance of tribe of our fathers their inheritance taken."),
        ("STEP_N36_B1", "36:5-13", "RULE_CLOSE", "כֵּן מַטֵּה בְנֵי־יוֹסֵף דֹּבְרִים", "ken matteh venei-yosef dovrim",
         "Moses commands Israel at mouth of YHWH saying: right tribe of sons of Joseph speak; this the word YHWH commanded for daughters of Zelophehad saying to the good in their eyes be for wives only to family of tribe of their father be for wives; not turn inheritance of Israel tribe to tribe; for each of Israel cleave to inheritance of tribe of his fathers; every daughter possessing an inheritance from tribes of Israel to one of family of tribe of her father be for wife so that Israel possess each inheritance of his fathers; not turn inheritance tribe to another tribe; for each of tribes of Israel cleave to his inheritance. As YHWH commanded Moses so daughters of Zelophehad do; Machlah Tirzah Choglah Milkah Noah daughters of Zelophehad are to sons of their uncles for wives; of families of sons of Menasheh son of Joseph they are for wives; their inheritance is on tribe of family of their father. These the mitzvot and the mishpatim which YHWH commanded by hand of Moses to Israel in plains of Moab by Jordan of Jericho."),
      ],
      [("S_heiress_tribe_lock", "Heiress marriage within tribe"), ("S_numbers_closed", "Numbers command block closed plains of Moab")],
      [("EXPORT_heiress_same_tribe", "מִמִּשְׁפַּחַת מַטֵּה אָבִיהָ", "mi-mishpachat matteh aviha", "Heiress marries within father's tribe"),
       ("EXPORT_num_complete", None, None, "Numbers thorough-block draft map complete")],
      [("IF daughter inherits", "THEN marry within father's tribe family so inheritance stays"),
       ("IF jubilee", "THEN still inheritance must not migrate tribes via heiress marriage")]),
]


def yaml_quote(s: str) -> str:
    if s is None:
        return '""'
    if any(c in s for c in ':"\'\n#{}[]|&*>!%@`') or s == "" or s.strip() != s:
        return json.dumps(s, ensure_ascii=False)
    return s


def verse_list(ch_s: int, v_s: int, ch_e: int, v_e: int) -> list[tuple[int, int]]:
    out = []
    for ch in range(ch_s, ch_e + 1):
        lo = v_s if ch == ch_s else 1
        hi = v_e if ch == ch_e else COUNTS[ch]
        for v in range(lo, hi + 1):
            out.append((ch, v))
    return out


def map_step_for_verse(block: dict, ch: int, v: int) -> str:
    for sid, ref, *_ in block["steps"]:
        m = re.match(r"(\d+):(\d+)-(\d+)", ref)
        if m:
            c, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if ch == c and a <= v <= b:
                return sid
        m2 = re.match(r"(\d+):(\d+)$", ref)
        if m2:
            c, a = int(m2.group(1)), int(m2.group(2))
            if ch == c and v == a:
                return sid
    return block["steps"][0][0]


def role_for_plain(he_plain: str) -> tuple[str, str]:
    p = he_plain.replace("/", "").replace("־", "")
    if p in ("את", "אל", "על", "מן", "עם", "או", "אם", "כי", "גם", "אשר", "לא", "כל", "זה", "זו", "זאת", "בן", "בין"):
        return "glue", "glue"
    people = ("משה", "אהרן", "ישראל", "אלעזר", "איתמר", "יהושע", "כלב", "קרח", "בלעם", "בלק", "פנחס", "מרים")
    if any(x in p for x in people):
        return "agent_or_person", "logic_bearing"
    return "logic_bearing_leaf", "logic_bearing"


def top_split_fields(tree: dict, words: list[dict]) -> dict:
    children = tree.get("children") or []
    if len(children) >= 2:
        left, right = children[0], children[1]
    elif len(children) == 1:
        left, right = children[0], {"he_span": "", "word_indices": []}
    else:
        left = right = {"he_span": tree.get("he_span", ""), "word_indices": tree.get("word_indices", [])}

    def arm(node: dict) -> dict:
        idxs = node.get("word_indices") or []
        he_span = node.get("he_span") or ""
        head_he, head_mark, head_i = "", "", idxs[-1] if idxs else 0
        if idxs:
            for i in idxs:
                w = words[i]
                if "etnachta" in (w.get("mark_en") or ""):
                    head_i = i
                    break
            else:
                head_i = idxs[-1]
            head_he = words[head_i]["he"]
            head_mark = words[head_i].get("mark_en") or ""
        return {"head_he": head_he, "head_i": head_i, "head_mark": head_mark, "he_span": he_span}

    return {"left": arm(left), "right": arm(right)}


_SIFREI_CACHE: Optional[list] = None


def sifrei_samples(max_paras: int = 4) -> list[dict]:
    """Sample flat Sifrei Bamidbar paragraphs (list of lists of strings)."""
    global _SIFREI_CACHE
    if not SIFREI_HE.exists():
        return []
    if _SIFREI_CACHE is None:
        with open(SIFREI_HE, encoding="utf-8") as f:
            data = json.load(f)
        _SIFREI_CACHE = data.get("text") or []
    out: list[dict] = []
    # Spread samples across dump rather than only first paras
    n = len(_SIFREI_CACHE)
    if n == 0:
        return []
    step = max(1, n // max(max_paras, 1))
    for i in range(0, n, step):
        if len(out) >= max_paras:
            break
        para = _SIFREI_CACHE[i]
        if isinstance(para, list) and para:
            he = para[0] if isinstance(para[0], str) else str(para[0])
        elif isinstance(para, str):
            he = para
        else:
            continue
        he = he.strip()
        if he:
            out.append({"section": f"Sifrei Bamidbar §{i+1}", "he": he[:280]})
    return out


def emit_block(block: dict) -> Path:
    bid = block["id"]
    verses = verse_list(block["ch_start"], block["v_start"], block["ch_end"], block["v_end"])
    step_ids = [s[0] for s in block["steps"]]
    sifrei = block.get("sifrei", "thin")
    lines: list[str] = []
    lines.append("# =============================================================================")
    lines.append(f"# LOGIC UNIT: Numbers {block['refs']} — {block['title_en']}")
    lines.append(f"# Numbers 47-block schedule (Sifrei Bamidbar lean: {sifrei})")
    lines.append("# =============================================================================")
    lines.append("# Experimental model — not binding religious law.")
    lines.append("")
    lines.append("meta:")
    lines.append(f'  id: "{bid}"')
    lines.append(f'  title_en: {yaml_quote(block["title_en"])}')
    lines.append(f'  title_he: {yaml_quote(block["title_he"])}')
    lines.append(f'  title_he_translit: {yaml_quote(block["title_he_translit"])}')
    lines.append(f'  title_he_en: {yaml_quote(block["title_he_en"])}')
    lines.append('  book_he: "בְּמִדְבַּר"')
    lines.append('  book_he_translit: "Be-midbar"')
    lines.append('  book_en: "Numbers"')
    lines.append(f'  refs: "{block["refs"]}"')
    lines.append("  data_paths_he:")
    lines.append('    - "Data/Num.xml"')
    lines.append('  status: draft')
    lines.append("  confidence_overall: hypothesis")
    lines.append(f'  genre: "{block["genre"]}"')
    lines.append('  build_track: numbers_ops')
    lines.append("  depends_on:")
    for d in block["depends_on"]:
        lines.append(f'    - "{d}"')
    lines.append("  owner_language_note: >")
    lines.append("    English for reading only. Hebrew is the derivation source.")
    lines.append("  oral_policy_note_en: >")
    lines.append("    Written first. Prefer Sifrei Bamidbar dual-track on law densification;")
    lines.append("    MH endpoints possible Oral; never silent-merge. Free names import Gen/Exod/Lev.")
    lines.append(f"  imports_note_en: {yaml_quote(block.get('imports_en', ''))}")
    lines.append("")
    lines.append("derivation_log:")
    lines.append("  - step: A")
    lines.append('    name_en: "Block choice"')
    lines.append("    comment: >")
    lines.append(f"      Thorough Num block {block['refs']} ({len(verses)} verses). {block['learn']}")
    lines.append("    confidence: established")
    lines.append("  - step: B")
    lines.append('    name_en: "Trees"')
    lines.append("    comment: >")
    lines.append(f"      All verses Num.{block['refs']} via taamim_tree_parse.py v1; full tree_ascii.")
    lines.append("    confidence: tested")
    lines.append('    tags: ["[HE-STRUCT]"]')
    lines.append("  - step: C")
    lines.append('    name_en: "Learnings"')
    lines.append("    comment: >")
    for chunk in re.findall(r".{1,100}(?:\s|$)", block["learn"]):
        lines.append(f"      {chunk.rstrip()}")
    lines.append("    confidence: tested")
    lines.append("  - step: D")
    lines.append('    name_en: "Sifrei dual-track"')
    lines.append("    comment: >")
    lines.append("      Sampled Sifrei Bamidbar from local Data/sifrei_bamidbar_he.json;")
    lines.append("      dual-track only; not merged into Written rules.")
    lines.append("    confidence: hypothesis")
    lines.append('    tags: ["[ORAL]"]')
    lines.append("")
    lines.append("boot_steps:")
    for i, (sid, ref, op, he, tr, en) in enumerate(block["steps"], 1):
        lines.append(f"  - id: {sid}")
        lines.append(f"    order: {i}")
        lines.append(f'    ref: "Num.{ref}"')
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
        lines.append("    Hypothesis IF/THEN from Written Hebrew; not binding law. Refine with Sifrei dual-track.")
        lines.append("  rows:")
        for j, (ifr, thenr) in enumerate(block["decision_hints"], 1):
            lines.append(f"    - id: ROW_{j}")
            lines.append(f"      if_en: {yaml_quote(ifr)}")
            lines.append(f"      then_en: {yaml_quote(thenr)}")
            lines.append("      confidence: hypothesis")
            lines.append('      source: "[HE-WRITTEN]"')
        lines.append("")
    lines.append("state_machine:")
    lines.append(f'  comment_en: "States for {bid}."')
    lines.append("  states:")
    for sid, en in block["states"]:
        lines.append(f"    - id: {sid}")
        lines.append(f"      en: {yaml_quote(en)}")
    lines.append("  transitions:")
    for i in range(len(block["states"]) - 1):
        lines.append(f"    - from: {block['states'][i][0]}")
        lines.append(f"      to: {block['states'][i+1][0]}")
        lines.append(f"      via: {step_ids[min(i, len(step_ids)-1)]}")
    lines.append("")
    lines.append("state_after:")
    for sid, en in (block["states"][-2:] if len(block["states"]) >= 2 else block["states"]):
        lines.append(f"  - id: AFTER_{sid}")
        lines.append(f"    en: {yaml_quote(en)}")
    lines.append("")
    lines.append("exports:")
    for item in block["exports"]:
        lines.append(f"  - id: {item[0]}")
        if len(item) > 1 and item[1]:
            lines.append(f"    he: {yaml_quote(item[1])}")
        if len(item) > 2 and item[2]:
            lines.append(f"    he_translit: {yaml_quote(item[2])}")
        lines.append(f"    en: {yaml_quote(item[3] if len(item) > 3 else '')}")
    lines.append("")
    lines.append("oral_notes:")
    lines.append("  - id: ORAL_policy")
    lines.append("    status: observation")
    lines.append(f'    work_en: "Block oral policy (Sifrei {sifrei})"')
    lines.append("    comment_en: >")
    lines.append("      Prefer Sifrei Bamidbar among Oral for Num law densification; then MH + Bavli.")
    lines.append("      Dual-track only. MH never ruled out. Narrative blocks: Written first.")
    lines.append('    source: "[PROJECT]"')
    if sifrei in ("primary", "strong", "medium"):
        samples = sifrei_samples(max_paras=6 if sifrei == "primary" else 3)
        for i, s in enumerate(samples, 1):
            lines.append(f"  - id: ORAL_sifrei_{i}")
            lines.append("    status: dual_track")
            lines.append('    work_en: "Sifrei Bamidbar"')
            lines.append(f'    locus_en: {yaml_quote(s["section"])}')
            lines.append(f"    he_sample: {yaml_quote(s['he'][:240])}")
            lines.append('    he_translit: "see Hebrew sample; full midrash in Data/sifrei_bamidbar_he.json"')
            lines.append('    en_sample: "[EN-AID] Hebrew Sifrei sample only in local dump; gloss not derivation source."')
            lines.append("    comment_en: >")
            lines.append("      Dual-track sample — does not rewrite Written boot_steps/decision rows.")
            lines.append('    source: "[ORAL][SIFREI]"')
            lines.append("    confidence: hypothesis")
    else:
        lines.append("  - id: ORAL_possible")
        lines.append("    status: possible_oral")
        lines.append('    work_en: "Midrash / Bavli / MH (named when quoted)"')
        lines.append("    comment_en: Dual-track only; Sifrei lean thin for this narrative/registry block.")
        lines.append('    source: "[ORAL]"')
    lines.append("")
    lines.append("scenarios:")
    for i, (sid, ref, op, *_) in enumerate(block["steps"], 1):
        lines.append(f"  - id: S{i}")
        lines.append(f'    title_en: "After {ref} ({op})"')
        lines.append(f'    expect_en: "Advances via {sid}; see boot_steps."')
    lines.append("")
    lines.append("binary_trees:")
    lines.append("  display_policy_en: >")
    lines.append("    Always he + he_translit + en. Full tree_ascii per verse.")
    lines.append("  method_note_en: >")
    lines.append("    taamim_tree_parse.py v1 on Data/Num.xml.")
    lines.append('  data_source: "Data/Num.xml"')
    lines.append('  parser: "taamim_tree_parse.py"')
    lines.append('  rule_set_version: "v1"')
    lines.append('  tags: ["[HE-STRUCT]"]')
    lines.append("  verse_trees:")
    coverage_blocks: list[str] = []
    word_total = 0
    for ch, v in verses:
        osis = f"Num.{ch}.{v}"
        try:
            parsed = parse_verse(osis)
        except Exception as e:
            lines.append(f"    Num_{ch}_{v}:")
            lines.append(f'      verse: "{ch}:{v}"')
            lines.append(f'      osis_id: "{osis}"')
            lines.append("      parser_status: error")
            lines.append(f"      error: {yaml_quote(str(e))}")
            continue
        words = parsed["words"]
        tree = parsed["tree"]
        ascii_t = tree_ascii_string(tree)
        plain_words = [w["he_plain"].replace("/", "") for w in words]
        linear_he = " ".join(plain_words)
        wc = len(words)
        word_total += wc
        pure = "false" if ("3-ary" in ascii_t or "n-ary" in ascii_t) else "true"
        step = map_step_for_verse(block, ch, v)
        ts = top_split_fields(tree, words)
        lines.append(f"    Num_{ch}_{v}:")
        lines.append(f'      verse: "{ch}:{v}"')
        lines.append(f'      osis_id: "{osis}"')
        lines.append(f'      parser_status: {parsed.get("status", "unique")}')
        lines.append(f"      pure_binary: {pure}")
        lines.append(f"      word_count: {wc}")
        lines.append("      linear:")
        lines.append(f"        he: {yaml_quote(linear_he)}")
        lines.append(f'        he_translit: {" ".join(f"w{i}" for i in range(wc))!r}')
        lines.append(
            f'        en: "Free gloss [EN-AID] — derive structure from Hebrew tree. Verse {ch}:{v}."'
        )
        lines.append('        en_note: "Free gloss [EN-AID]. Translit leaf-indexed w0.."')
        lines.append("      top_binary_split:")
        lines.append("        comment: >")
        lines.append(f"          Top split ta'amim v1; maps_to ['{step}'].")
        lines.append("        left_half:")
        lines.append('          side_en: "Left of top split"')
        lines.append("          head:")
        head_plain = strip_taamim_and_points(ts["left"]["head_he"]) if ts["left"]["head_he"] else ""
        lines.append(f"            he: {yaml_quote(head_plain)}")
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
    lines.append("  Draft thorough-block unit for Numbers ops track. Not binding religious law.")
    lines.append("  Trees tested via taamim_tree_parse v1; logic hypothesis/tested per comments.")
    out_path = UNITS / f"{bid}.yaml"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    # Validate verse coverage
    total = sum(len(verse_list(b["ch_start"], b["v_start"], b["ch_end"], b["v_end"])) for b in ALL_BLOCKS)
    expected = sum(COUNTS.values())
    if total != expected:
        print(f"WARNING: block verse sum {total} != book {expected}", file=sys.stderr)

    if args.list:
        for i, b in enumerate(ALL_BLOCKS, 1):
            n = len(verse_list(b["ch_start"], b["v_start"], b["ch_end"], b["v_end"]))
            print(f"{i:02d} {b['id']:40s} {b['refs']:12s} {n:3d}vv  {b['sifrei']}")
        print(f"TOTAL blocks={len(ALL_BLOCKS)} verses={total}")
        return

    written = 0
    for b in ALL_BLOCKS:
        if args.only and b["id"] != args.only and args.only not in b["id"]:
            continue
        if b["id"] in SKIP_IDS and not args.force:
            print(f"skip {b['id']}")
            continue
        path = emit_block(b)
        n = len(verse_list(b["ch_start"], b["v_start"], b["ch_end"], b["v_end"]))
        print(f"wrote {path.name} ({n} vv)")
        written += 1
    print(f"done wrote={written} schedule={len(ALL_BLOCKS)} verses={total}")


if __name__ == "__main__":
    main()
