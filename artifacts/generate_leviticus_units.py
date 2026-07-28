#!/usr/bin/env python3
"""
Generate Leviticus Pre-Code logic units (50-block schedule).
Trees via taamim_tree_parse; Sifra dual-track samples from Data/sifra_he.json.
Does not invent binding law. Skip hand-done 01–02 unless --force.
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
SIFRA_HE = ROOT / "Data" / "sifra_he.json"

# Hebrew/OSIS Lev chapter lengths (Data/Lev.xml)
COUNTS = {
    1: 17, 2: 16, 3: 17, 4: 35, 5: 26, 6: 23, 7: 38, 8: 36, 9: 24, 10: 20,
    11: 47, 12: 8, 13: 59, 14: 57, 15: 33, 16: 34, 17: 16, 18: 30, 19: 37,
    20: 27, 21: 24, 22: 33, 23: 44, 24: 23, 25: 55, 26: 46, 27: 34,
}

# Chapter → preferred Sifra section key(s)
SIFRA_BY_CH = {
    1: ["Vayikra Dibbura d'Nedavah"],
    2: ["Vayikra Dibbura d'Nedavah"],
    3: ["Vayikra Dibbura d'Nedavah"],
    4: ["Vayikra Dibbura d'Chovah"],
    5: ["Vayikra Dibbura d'Chovah"],
    6: ["Tzav"],
    7: ["Tzav"],
    8: ["Tzav", "Shemini"],
    9: ["Shemini"],
    10: ["Shemini"],
    11: ["Shemini"],
    12: ["Tazria Parashat Yoledet"],
    13: ["Tazria Parashat Nega'im"],
    14: ["Metzora", "Tazria Parashat Nega'im"],
    15: ["Metzora Parashat Zavim"],
    16: ["Acharei Mot"],
    17: ["Acharei Mot"],
    18: ["Kedoshim", "Acharei Mot"],
    19: ["Kedoshim"],
    20: ["Kedoshim"],
    21: ["Emor"],
    22: ["Emor"],
    23: ["Emor"],
    24: ["Emor"],
    25: ["Behar"],
    26: ["Bechukotai"],
    27: ["Bechukotai"],
}

SKIP_IDS = {
    "lev_01_call_and_korban_opening",
    "lev_01_olah_cattle_procedure",
}


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
    sifra: str,
    learn: str,
    steps: list[tuple],
    states: list[tuple],
    exports: list[tuple],
    decisions: Optional[list[tuple]] = None,
    imports_en: str = "Exodus sanctuary free names where used (ohel mo'ed, mizbeach, kohen office).",
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
        "sifra": sifra,
        "learn": learn,
        "steps": steps,
        "states": states,
        "exports": exports,
        "decision_hints": decisions or [],
        "imports_en": imports_en,
    }


ALL_BLOCKS: list[dict[str, Any]] = [
    # 01–02 exist by hand — still listed for map completeness; skipped on write
    B("lev_01_call_and_korban_opening", "1:1-3", 1, 1, 1, 3,
      "Call from Tent; korban from behemah classes (1:1–3)",
      "וַיִּקְרָא — קָרְבָּן", "va-yikra — korban", "And He called — offering",
      ["exo_40_erect_fill"], "decision_table", "primary",
      "Call from ohel mo'ed; speak to Israel; when person offers, from behemah cattle/flock.",
      [("STEP_L01_A1", "1:1-3", "CALL_OPEN", "וַיִּקְרָא … קָרְבַּן", "va-yikra … korban", "Call; when person brings near offering from animals.")],
      [("S_called", "Call from Tent active")],
      [("EXPORT_korban_open", "קָרְבָּן", "korban", "Offering framework open")]),
    B("lev_01_olah_cattle_procedure", "1:4-9", 1, 4, 1, 9,
      "Olah cattle procedure (1:4–9)",
      "עֹלָה — בָּקָר", "olah — bakar", "Burnt offering — cattle",
      ["lev_01_call_and_korban_opening"], "boot_steps", "primary",
      "Cattle olah path: lean, slaughter, blood, flay, arrange, wash, burn sweet savor.",
      [("STEP_L01b_A1", "1:4-9", "OLAH_CATTLE", "וְסָמַךְ … עֹלָה", "ve-samakh … olah", "Cattle olah procedure pipeline.")],
      [("S_cattle_olah", "Cattle olah procedure loaded")],
      [("EXPORT_olah_cattle", "עֹלַת בָּקָר", "olat bakar", "Cattle burnt offering path")]),
    B("lev_01_olah_flock", "1:10-13", 1, 10, 1, 13,
      "Olah flock (sheep/goat) procedure (1:10–13)",
      "עֹלָה — מִן־הַצֹּאן", "olah — min-ha-tzon", "Burnt offering — from the flock",
      ["lev_01_olah_cattle_procedure"], "decision_table", "primary",
      "IF olah from flock (sheep or goat): male whole; north side slaughter; blood; pieces; wash; burn as cattle pattern.",
      [("STEP_L1F_A1", "1:10-13", "OLAH_FLOCK", "וְאִם־מִן־הַצֹּאן … צָפוֹנָה", "ve-im-min-ha-tzon … tzafonah",
        "If olah from flock sheep or goats: male without blemish; slaughter north of altar; blood round; flay section; wash; burn on wood fire.")],
      [("S_flock_olah", "Flock olah path available")],
      [("EXPORT_olah_flock", "עֹלַת צֹאן", "olat tzon", "Flock burnt offering path")],
      [("IF olah from flock (sheep OR goat)", "THEN male whole; slaughter north; blood; burn as olah")]),
    B("lev_01_olah_bird", "1:14-17", 1, 14, 1, 17,
      "Olah bird (turtledove/pigeon) procedure (1:14–17)",
      "עֹלָה — מִן־הָעוֹף", "olah — min-ha-of", "Burnt offering — from the birds",
      ["lev_01_olah_flock"], "decision_table", "primary",
      "IF olah from birds: turtledoves or young pigeons; pinch head; blood drain; crop; tear wings not sever; burn.",
      [("STEP_L1B_A1", "1:14-17", "OLAH_BIRD", "וְאִם מִן־הָעוֹף … תֹרִים אוֹ … יוֹנָה", "ve-im min-ha-of … torim o … yonah",
        "If olah from birds: turtledoves or young pigeons; priest brings to altar; pinch head; blood pressed; remove crop; split by wings not divide; burn.")],
      [("S_bird_olah", "Bird olah path available"), ("S_olah_channels_complete", "Cattle/flock/bird olah channels loaded")],
      [("EXPORT_olah_bird", "עֹלַת עוֹף", "olat of", "Bird burnt offering path")],
      [("IF olah from birds", "THEN turtledove OR young pigeon; pinch-head procedure; burn on altar")]),
    B("lev_02_minchah", "2:1-16", 2, 1, 2, 16,
      "Minchah grain offerings: flour, oven, pan, firstfruits (2:1–16)",
      "מִנְחָה", "minchah", "Grain offering",
      ["lev_01_olah_bird"], "decision_table", "primary",
      "Minchah types: fine flour oil frankincense; oven cakes; griddle; pan; no leaven/honey on altar; salt covenant; first ripe grain.",
      [
        ("STEP_L2_A1", "2:1-3", "MINCHAH_FLOUR", "וְנֶפֶשׁ כִּי־תַקְרִיב … סֹלֶת", "ve-nefesh ki-takriv … solet",
         "When person offers minchah: fine flour, oil, frankincense; fistful memorial burn; rest to Aaron sons most holy."),
        ("STEP_L2_B1", "2:4-10", "MINCHAH_COOKED", "מַאֲפֵה תַנּוּר … מַחֲבַת … מַרְחֶשֶׁת", "ma'afeh tannur … machavat … marcheshet",
         "Oven unleavened cakes/wafers; griddle pieces oil; pan; memorial fistful; rest priests most holy."),
        ("STEP_L2_C1", "2:11-16", "NO_LEAVEN_SALT_BIKKURIM", "כָּל־הַמִּנְחָה … לֹא תֵעָשֶׂה חָמֵץ … מֶלַח", "kol-ha-minchah … lo te'aseh chametz … melach",
         "No leaven or honey as isheh; salt of covenant on all minchah; firstfruits Aviv grain oil frankincense memorial."),
      ],
      [("S_minchah_types", "Minchah type registry loaded"), ("S_salt_covenant", "Salt covenant on offerings")],
      [("EXPORT_minchah", "מִנְחָה", "minchah", "Grain offering system"),
       ("EXPORT_melach_berit", "מֶלַח בְּרִית", "melach berit", "Salt of covenant")],
      [("IF minchah of flour", "THEN oil + frankincense; fistful burned; remainder priests"),
       ("IF minchah cooked", "THEN unleavened; oil; memorial fistful"),
       ("IF any altar minchah", "THEN no chametz/honey as fire offering; salt required")]),
    B("lev_03_shelamim", "3:1-17", 3, 1, 3, 17,
      "Shelamim peace offerings cattle/flock; fat and blood ban (3:1–17)",
      "שְׁלָמִים", "shelamim", "Peace offerings",
      ["lev_02_minchah"], "decision_table", "primary",
      "Shelamim male/female cattle or flock; lean; fat portions to altar; perpetual ban on eating fat and blood.",
      [
        ("STEP_L3_A1", "3:1-5", "SHELAMIM_CATTLE", "וְאִם־זֶבַח שְׁלָמִים … בָּקָר", "ve-im-zevach shelamim … bakar",
         "If shelamim from cattle male or female whole; lean; slaughter; blood; fat cover innards kidneys suet burn as isheh."),
        ("STEP_L3_B1", "3:6-11", "SHELAMIM_SHEEP", "וְאִם־מִן־הַצֹּאן … כֶּבֶשׂ", "ve-im-min-ha-tzon … keves",
         "If from flock sheep: male/female whole; fat tail entire; fat portions burn."),
        ("STEP_L3_C1", "3:12-17", "SHELAMIM_GOAT_BAN", "וְאִם עֵז … חֻקַּת עוֹלָם … חֵלֶב וָדָם", "ve-im ez … chukkat olam … chelev va-dam",
         "If goat path; fat burn; perpetual statute all dwellings: eat neither fat nor blood."),
      ],
      [("S_shelamim_paths", "Shelamim cattle/sheep/goat paths"), ("S_fat_blood_ban", "Fat and blood eating banned forever")],
      [("EXPORT_shelamim", "שְׁלָמִים", "shelamim", "Peace offering system"),
       ("EXPORT_chelev_dam_ban", "חֵלֶב וָדָם", "chelev va-dam", "Fat and blood ban")],
      [("IF shelamim from cattle/flock", "THEN lean; blood on altar; fat portions burned"),
       ("IF eat fat OR blood", "THEN perpetual ban violated (statute all dwellings)")]),
    B("lev_04_chatat_priest", "4:1-12", 4, 1, 4, 12,
      "Chatat: anointed priest errs (4:1–12)",
      "חַטָּאת — הַכֹּהֵן הַמָּשִׁיחַ", "chatat — ha-kohen ha-mashiach", "Sin offering — anointed priest",
      ["lev_03_shelamim"], "decision_table", "primary",
      "IF anointed priest sins bringing guilt on people: bull chatat; blood in Tent; veil; incense altar; rest burn outside.",
      [("STEP_L4P_A1", "4:1-12", "CHATAT_PRIEST", "אִם הַכֹּהֵן הַמָּשִׁיחַ … פַּר", "im ha-kohen ha-mashiach … par",
        "Anointed priest sins: bull without blemish; lean; blood into ohel mo'ed; sprinkle veil; horns incense altar; pour base olah altar; fat burn; hide flesh dung burn outside camp ash place.")],
      [("S_chatat_priest", "Priest chatat path loaded")],
      [("EXPORT_chatat_priest", "חַטַּאת כֹּהֵן", "chatat kohen", "Anointed priest sin offering")],
      [("IF anointed priest sins unwittingly", "THEN bull chatat; blood in Tent; remainder burned outside")]),
    B("lev_04_chatat_congregation", "4:13-21", 4, 13, 4, 21,
      "Chatat: whole congregation errs (4:13–21)",
      "חַטָּאת — כָּל־עֲדַת יִשְׂרָאֵל", "chatat — kol-adat yisrael", "Sin offering — whole congregation",
      ["lev_04_chatat_priest"], "decision_table", "primary",
      "IF whole congregation errs hidden then known: bull; elders lean; blood in Tent like priest; burn outside.",
      [("STEP_L4C_A1", "4:13-21", "CHATAT_EDAH", "וְאִם כָּל־עֲדַת … פַּר", "ve-im kol-adat … par",
        "If whole Israel congregation errs and matter hidden then known: assembly bull; elders lean; slaughter; blood veil and incense altar; fat; burn outside as priest bull.")],
      [("S_chatat_edah", "Congregation chatat path")],
      [("EXPORT_chatat_edah", "חַטַּאת עֵדָה", "chatat edah", "Congregation sin offering")],
      [("IF whole congregation sins unwittingly and becomes known", "THEN bull; elders lean; blood in Tent; burn outside")]),
    B("lev_04_chatat_leader", "4:22-26", 4, 22, 4, 26,
      "Chatat: leader (nasi) errs (4:22–26)",
      "חַטָּאת — נָשִׂיא", "chatat — nasi", "Sin offering — leader",
      ["lev_04_chatat_congregation"], "decision_table", "primary",
      "IF nasi sins unwittingly: male goat; blood on olah altar horns; fat; priest atones forgiven.",
      [("STEP_L4N_A1", "4:22-26", "CHATAT_NASI", "אֲשֶׁר נָשִׂיא יֶחֱטָא … שְׂעִיר עִזִּים", "asher nasi yecheta … se'ir izzim",
        "When leader sins unwittingly: male goat whole; lean; slaughter olah place; blood horns altar olah; pour base; fat burn; atonement forgiveness.")],
      [("S_chatat_nasi", "Leader chatat path")],
      [("EXPORT_chatat_nasi", "חַטַּאת נָשִׂיא", "chatat nasi", "Leader sin offering")],
      [("IF nasi sins unwittingly", "THEN male goat; blood on outer altar; fat; atonement")]),
    B("lev_04_chatat_common", "4:27-35", 4, 27, 4, 35,
      "Chatat: common person goat or sheep (4:27–35)",
      "חַטָּאת — עַם הָאָרֶץ", "chatat — am ha-aretz", "Sin offering — common person",
      ["lev_04_chatat_leader"], "decision_table", "primary",
      "IF one of people sins unwittingly: female goat OR female sheep; blood outer altar; fat; atonement.",
      [
        ("STEP_L4A_A1", "4:27-31", "CHATAT_GOAT_FEMALE", "וְאִם־נֶפֶשׁ … עֵז", "ve-im-nefesh … ez",
         "If common person sins: female goat whole; lean; slaughter; blood horns olah altar; fat; atonement forgiven."),
        ("STEP_L4A_B1", "4:32-35", "CHATAT_SHEEP_FEMALE", "וְאִם־כֶּבֶשׂ … נְקֵבָה", "ve-im-keves … nekevah",
         "If brings sheep female for chatat: same blood/fat pattern; atonement forgiven."),
      ],
      [("S_chatat_common", "Common-person chatat goat/sheep paths"), ("S_chatat_ladder_complete", "Priest/edah/nasi/common chatat ladder loaded")],
      [("EXPORT_chatat_common", "חַטַּאת נֶפֶשׁ", "chatat nefesh", "Common person sin offering")],
      [("IF common person sins unwittingly", "THEN female goat OR female sheep; outer altar blood; atonement")]),
    B("lev_05_asham_graded", "5:1-13", 5, 1, 5, 13,
      "Asham/chatat graded: witness, impurity, oath; sliding scale (5:1–13)",
      "אָשָׁם — קָרְבַּן עוֹלֶה וְיוֹרֵד", "asham — korban oleh ve-yored", "Guilt — sliding-scale offering",
      ["lev_04_chatat_common"], "decision_table", "primary",
      "Cases: withhold testimony; carcass impurity; rash oath; confess; female flock or birds or flour if poor.",
      [
        ("STEP_L5G_A1", "5:1-6", "CASES_CONFESS", "וְנֶפֶשׁ כִּי תֶחֱטָא … וְהִתְוַדָּה", "ve-nefesh ki techeta … ve-hitvaddah",
         "Guilt cases: hears oath/curse and does not tell; touches impure carcass/human impurity; rash oath; feels guilt; confess; bring asham female flock lamb/goat as chatat."),
        ("STEP_L5G_B1", "5:7-13", "SLIDING_SCALE", "וְאִם־לֹא תַגִּיעַ יָדוֹ … סֹלֶת", "ve-im-lo taggia yado … solet",
         "If hand cannot reach flock: two turtledoves/pigeons one chatat one olah; if cannot: tenth ephah flour no oil/frankincense as chatat; fistful burn; rest priest."),
      ],
      [("S_graded_chatat", "Sliding-scale chatat/asham cases")],
      [("EXPORT_oleh_ve_yored", "עוֹלֶה וְיוֹרֵד", "oleh ve-yored", "Sliding-scale offering by means")],
      [("IF cannot afford flock for these guilt cases", "THEN two birds"),
       ("IF cannot afford birds", "THEN flour tenth ephah without oil/frankincense")]),
    B("lev_05_asham_sancta", "5:14-26", 5, 14, 5, 26,
      "Asham: misuse of sancta; fraud and false oath (5:14–26)",
      "אָשָׁם — קָדָשִׁים / מִעִילָה", "asham — kodashim / me'ilah", "Guilt — sancta / trespass",
      ["lev_05_asham_graded"], "decision_table", "primary",
      "Me'ilah in YHWH sancta: ram asham + fifth; fraud neighbor deposit/robbery/oppression/lost+false oath: restore principal+fifth + ram asham.",
      [
        ("STEP_L5S_A1", "5:14-16", "MEILAH_SANCTA", "נֶפֶשׁ כִּי תִמְעֹל … אֵיל", "nefesh ki tim'ol … eil",
         "If sins me'ilah from YHWH holy things unwittingly: ram asham valuation shekels; make good the holy + add fifth; priest atones forgiven."),
        ("STEP_L5S_B1", "5:17-19", "ASHAM_UNKNOWN", "וְאִם־נֶפֶשׁ כִּי תֶחֱטָא … לֹא־יָדַע", "ve-im-nefesh ki techeta … lo-yada",
         "If sins any command unwittingly and did not know: still bears iniquity; ram asham; atonement."),
        ("STEP_L5S_C1", "5:20-26", "FRAUD_FALSE_OATH", "כִּי תֶחֱטָא וּמָעֲלָה … וְשִׁלַּם אֹתוֹ", "ki techeta u-ma'alah … ve-shillam oto",
         "If denies neighbor deposit/pledge/robbery/oppresses/finds lost and swears false: restore item + fifth; ram asham; atonement forgiven."),
      ],
      [("S_asham_sancta", "Sancta me'ilah asham"), ("S_asham_civil", "Civil fraud + false oath asham")],
      [("EXPORT_asham", "אָשָׁם", "asham", "Guilt offering system"),
       ("EXPORT_fifth_restore", "חֲמִישִׁתוֹ", "chamishito", "Add fifth when restoring")],
      [("IF me'ilah in holy things", "THEN ram asham + restore + fifth"),
       ("IF fraud or false oath against neighbor", "THEN restore + fifth + ram asham")]),
    B("lev_06_olah_minchah_torah", "6:1-23", 6, 1, 6, 23,
      "Torat olah, perpetual fire, minchah priest rules, chatat priest (6:1–23)",
      "תּוֹרַת הָעֹלָה — אֵשׁ תָּמִיד", "torat ha-olah — esh tamid", "Law of the burnt offering — continual fire",
      ["lev_05_asham_sancta"], "decision_table", "primary",
      "Command Aaron: olah ash ritual; fire never out; minchah eating rules; priest's own minchah whole; chatat priest eating/vessels; blood-in-Tent chatat not eaten burn.",
      [
        ("STEP_L6_A1", "6:1-6", "OLAH_FIRE", "צַו אֶת־אַהֲרֹן … אֵשׁ תָּמִיד", "tzav et-aharon … esh tamid",
         "Command Aaron sons: torat olah all night; priest linen; take ash; change clothes carry ash outside; fire kept burning; wood each morning; fat shelamim; fire never quenched."),
        ("STEP_L6_B1", "6:7-16", "MINCHAH_PRIEST", "וְזֹאת תּוֹרַת הַמִּנְחָה … כָּל־מִנְחַת כֹּהֵן", "ve-zot torat ha-minchah … kol-minchat kohen",
         "Torat minchah: sons present before YHWH; fistful; rest unleavened holy place; males eat; portion forever; no leaven; priest's anointing minchah whole not eaten."),
        ("STEP_L6_C1", "6:17-23", "CHATAT_PRIEST_RULES", "זֹאת תּוֹרַת הַחַטָּאת … לֹא תֵאָכֵל בָּאֵשׁ תִּשָּׂרֵף", "zot torat ha-chatat … lo te'akhel ba-esh tissaref",
         "Torat chatat: slaughter olah place most holy; priest who offers eats holy place; blood splash sanctifies; earthen pot broken; if blood brought into Tent to atone — not eaten, burned."),
      ],
      [("S_priest_torot", "Priest torot olah/minchah/chatat loaded")],
      [("EXPORT_esh_tamid", "אֵשׁ תָּמִיד", "esh tamid", "Continual altar fire"),
       ("EXPORT_torat_korbanot", "תּוֹרַת הַקָּרְבָּנוֹת", "torat ha-korbanot", "Priest-facing offering torot")],
      [("IF blood of chatat brought into Tent to atone", "THEN do not eat; burn in fire"),
       ("IF altar fire", "THEN must not go out")]),
    B("lev_07_asham_procedure", "7:1-10", 7, 1, 7, 10,
      "Torat asham; priest shares of olah and minchah (7:1–10)",
      "תּוֹרַת הָאָשָׁם", "torat ha-asham", "Law of the guilt offering",
      ["lev_06_olah_minchah_torah"], "decision_table", "primary",
      "Asham most holy; slaughter place; blood; fat; male priests eat; same portion rules as chatat; priest who offers keeps skin of olah; baked minchah shares.",
      [("STEP_L7A_A1", "7:1-10", "ASHAM_SHARES", "וְזֹאת תּוֹרַת הָאָשָׁם … קֹדֶשׁ קָדָשִׁים", "ve-zot torat ha-asham … kodesh kodashim",
        "Torat asham most holy; slaughter where olah; blood round; fat portions burn; every male priest eats holy place; as chatat so asham priest who atones gets it; priest who offers olah gets skin; every minchah oven/pan/griddle to priest who offers; mixed dry to all sons equal.")],
      [("S_asham_torah", "Asham procedure + priest dues")],
      [("EXPORT_asham_torah", "תּוֹרַת הָאָשָׁם", "torat ha-asham", "Guilt offering torah")],
      [("IF asham", "THEN most holy; male priests eat in holy place")]),
    B("lev_07_shelamim_types", "7:11-21", 7, 11, 7, 21,
      "Shelamim: thanksgiving, vow/freewill; impurity bans (7:11–21)",
      "תּוֹדָה — נֶדֶר / נְדָבָה", "todah — neder / nedavah", "Thanksgiving — vow / freewill",
      ["lev_07_asham_procedure"], "decision_table", "primary",
      "Thanksgiving with leavened/unleavened breads same day; vow/freewill until next day morning rules; impurity contact voids eating; cut off.",
      [
        ("STEP_L7S_A1", "7:11-15", "TODAH", "תּוֹרַת זֶבַח הַשְּׁלָמִים … תּוֹדָה", "torat zevach ha-shelamim … todah",
         "If shelamim for thanksgiving: unleavened cakes oil wafers + leavened bread; one of each as terumah to priest who dashes blood; flesh of todah eaten same day none left morning."),
        ("STEP_L7S_B1", "7:16-18", "NEDER_NEDAVAH", "וְאִם־נֶדֶר אוֹ נְדָבָה", "ve-im-neder o nedavah",
         "If vow or freewill: eaten day of offering and next day; day three remainder burned; if eaten day three not accepted abomination bearer iniquity."),
        ("STEP_L7S_C1", "7:19-21", "IMPURE_EAT_BAN", "וְהַבָּשָׂר … טֻמְאָה", "ve-ha-basar … tum'ah",
         "Flesh touching impure not eaten burn; pure may eat flesh; person impure who eats shelamim flesh cut off; touches impure human/animal/any detestable and eats cut off."),
      ],
      [("S_shelamim_subtypes", "Todah vs vow/freewill timing"), ("S_impure_eat_cut_off", "Impure eating sancta cut off")],
      [("EXPORT_todah", "תּוֹדָה", "todah", "Thanksgiving shelamim"),
       ("EXPORT_neder_nedavah", "נֶדֶר וּנְדָבָה", "neder u-nedavah", "Vow and freewill shelamim")],
      [("IF shelamim thanksgiving", "THEN breads included; meat same day only"),
       ("IF vow or freewill shelamim", "THEN may eat day 1–2; day 3 burn"),
       ("IF impure person eats shelamim flesh", "THEN cut off")]),
    B("lev_07_fat_blood_dues", "7:22-38", 7, 22, 7, 38,
      "Fat/blood ban detail; priest breast/thigh; summary of korban torot (7:22–38)",
      "חֵלֶב וָדָם — חָזֶה וְשׁוֹק", "chelev va-dam — chazeh ve-shok", "Fat and blood — breast and thigh",
      ["lev_07_shelamim_types"], "decision_table", "primary",
      "No fat of ox sheep goat eaten; fat of neveilah/terefah for use not eat; no blood birds beasts; wave breast and heave thigh to priests forever; summary of torot on Sinai.",
      [
        ("STEP_L7F_A1", "7:22-27", "FAT_BLOOD_DETAIL", "כָּל־חֵלֶב שׁוֹר … כָּל־דָּם", "kol-chelev shor … kol-dam",
         "Speak Israel: no fat ox/sheep/goat; fat of carcass/torn may be used for any work but not eaten; eater of fat from isheh animals cut off; no blood bird or beast dwellings; eater cut off."),
        ("STEP_L7F_B1", "7:28-38", "BREAST_THIGH_SUMMARY", "הַחָזֶה … הַשּׁוֹק … בְּיוֹם צַוֺּתוֹ", "ha-chazeh … ha-shok … be-yom tzavvoto",
         "Shelamim: bring isheh YHWH; fat with breast wave; breast to Aaron sons; right thigh terumah to priest who offers blood/fat; wave breast + heave thigh taken from Israel shelamim forever; anointing day portion; these torot olah minchah chatat asham milluim shelamim commanded Sinai."),
      ],
      [("S_korban_torot_closed", "Korbanot torot 1–7 summary closed"), ("S_priest_dues", "Breast and thigh dues forever")],
      [("EXPORT_chazeh_shok", "חָזֶה וְשׁוֹק", "chazeh ve-shok", "Priest wave breast and heave thigh"),
       ("EXPORT_korban_block_closed", None, None, "Offering procedure block 1–7 draft complete")],
      [("IF eat fat of ox/sheep/goat from fire offerings", "THEN cut off"),
       ("IF eat any blood of bird or beast", "THEN cut off")]),
    # Phase B
    B("lev_08_milluim", "8:1-36", 8, 1, 8, 36,
      "Seven-day priest investiture (millu'im) (8:1–36)",
      "מִלֻּאִים", "millu'im", "Ordination fillings",
      ["lev_07_fat_blood_dues", "exo_29_investiture"], "boot_steps", "medium",
      "Assemble; wash; dress Aaron; anoint mishkan and Aaron; dress sons; bull chatat; rams olah and milluim; blood ear thumb toe; wave; seven days at entrance.",
      [
        ("STEP_L8_A1", "8:1-13", "DRESS_ANOINT", "קַח אֶת־אַהֲרֹן … וַיִּמְשַׁח", "kach et-aharon … va-yimshach",
         "Command take Aaron sons garments oil bull rams basket; assemble edah; wash; dress Aaron coat sash robe ephod choshen turban; anoint mishkan and all; anoint Aaron head; dress sons."),
        ("STEP_L8_B1", "8:14-30", "OFFER_MILLUIM", "וַיַּגֵּשׁ … אֵיל הַמִּלֻּאִים", "va-yaggash … eil ha-millu'im",
         "Bull chatat lean; blood altar purify; fat burn; hide outside; ram olah; second ram milluim; blood right ear thumb toe Aaron and sons; wave basket; anointing oil blood sprinkle garments."),
        ("STEP_L8_C1", "8:31-36", "SEVEN_DAYS", "בַּשְּׁלּוּ … שִׁבְעַת יָמִים", "bashelu … shiv'at yamim",
         "Boil flesh entrance; eat with basket bread; remainder burn; entrance seven days day night keep charge of YHWH; atonement; Aaron sons do all commanded."),
      ],
      [("S_milluim_done", "Seven-day ordination performed"), ("S_priests_consecrated", "Aaron and sons consecrated")],
      [("EXPORT_milluim_done", "מִלֻּאִים", "millu'im", "Priest ordination executed (cf Exod 29)"),
       ("EXPORT_seven_day_gate", "שִׁבְעַת יָמִים פֶּתַח", "shiv'at yamim petach", "Seven days at Tent entrance")],
      imports_en="Exod 29 investiture specs; garments Exod 28; Tent Exod 40."),
    B("lev_09_eighth_day", "9:1-24", 9, 1, 9, 24,
      "Eighth day service; fire from before YHWH (9:1–24)",
      "בַּיּוֹם הַשְּׁמִינִי — אֵשׁ מִלִּפְנֵי יְהוָה", "ba-yom ha-shemini — esh mi-lifnei YHWH", "On the eighth day — fire from before YHWH",
      ["lev_08_milluim"], "narrative_fsm", "medium",
      "Eighth day: Aaron begins service chatat olah minchah shelamim for self and people; glory appears; fire consumes altar portions; people shout fall.",
      [
        ("STEP_L9_A1", "9:1-14", "AARON_OFFERS", "קַח לְךָ עֵגֶל … וַיַּקְרֵב", "kach lekha egel … va-yakrev",
         "Eighth day Moses calls Aaron sons elders; calf chatat ram olah for Aaron; people goat calf ram shelamim ox ram minchah; approach Tent; Aaron offers own chatat olah."),
        ("STEP_L9_B1", "9:15-24", "PEOPLE_GLORY_FIRE", "וַיַּקְרֵב אֵת קָרְבַּן הָעָם … וַתֵּצֵא אֵשׁ", "va-yakrev et korban ha-am … va-tetze esh",
         "Offers people's chatat olah minchah shelamim; lifts hands blesses; Moses Aaron enter Tent come out bless; glory appears; fire from before YHWH consumes olah fats; people shout fall faces."),
      ],
      [("S_service_live", "Aaronic public service live"), ("S_fire_approved", "Divine fire consumes altar portions")],
      [("EXPORT_esh_lifnei_yhwh", "אֵשׁ מִלִּפְנֵי יְהוָה", "esh mi-lifnei YHWH", "Fire from before YHWH approves altar"),
       ("EXPORT_eighth_day", "יוֹם הַשְּׁמִינִי", "yom ha-shemini", "Eighth-day inauguration complete")]),
    B("lev_10_nadav_avihu", "10:1-20", 10, 1, 10, 20,
      "Nadav and Avihu; mourning limits; drink ban; remaining chatat (10:1–20)",
      "נָדָב וַאֲבִיהוּא — אֵשׁ זָרָה", "nadav va-avihu — esh zarah", "Nadav and Avihu — strange fire",
      ["lev_09_eighth_day"], "narrative_fsm", "medium",
      "Strange fire; die before YHWH; no mourning hair/garments for Aaron sons; kin bury; no wine enter Tent; remaining chatat eat rules; goat chatat burned dispute Moses accepts Aaron.",
      [
        ("STEP_L10_A1", "10:1-7", "STRANGE_FIRE_MOURN", "וַיַּקְרִיבוּ … אֵשׁ זָרָה … וַתֵּצֵא אֵשׁ", "va-yakrivu … esh zarah … va-tetze esh",
         "Nadav Avihu offer strange fire not commanded; fire consumes them die; Moses: among near ones sanctified; Aaron silent; carry cousins outside; Aaron Eleazar Ithamar no loose hair tear clothes lest die wrath on edah; not leave entrance anointing oil."),
        ("STEP_L10_B1", "10:8-11", "WINE_BAN_TEACH", "יַיִן וְשֵׁכָר אַל־תֵּשְׁתְּ … וּלְהוֹרֹת", "yayin ve-shekhar al-tesht … u-lehorot",
         "YHWH to Aaron: no wine/strong drink you or sons when enter ohel mo'ed lest die; statute forever; distinguish holy/common pure/impure; teach Israel all statutes."),
        ("STEP_L10_C1", "10:12-20", "CHATAT_REMAINDER", "קְחוּ … מִנְחָה … שְׂעִיר הַחַטָּאת", "kechu … minchah … se'ir ha-chatat",
         "Eat remaining minchah unleavened beside altar; wave breast thigh eat pure place; goat chatat blood not brought inside burned; Moses angry; Aaron: after such things would YHWH accept eaten chatat; Moses accepts."),
      ],
      [("S_strange_fire_judgment", "Unauthorized fire judged"), ("S_priest_conduct_rules", "Mourning/wine/teaching rules set")],
      [("EXPORT_esh_zarah", "אֵשׁ זָרָה", "esh zarah", "Strange fire ban — only commanded fire"),
       ("EXPORT_yayin_ban_tent", "יַיִן בְּאֹהֶל מוֹעֵד", "yayin be-ohel mo'ed", "No wine when entering Tent to serve")]),
    # Phase C purity
    B("lev_11_animals_water_birds", "11:1-23", 11, 1, 11, 23,
      "Clean/unclean land animals, water creatures, birds, winged swarmers (11:1–23)",
      "טָהוֹר / טָמֵא — בְּהֵמָה", "tahor / tame — behemah", "Clean / unclean — animals",
      ["lev_10_nadav_avihu"], "decision_table", "primary",
      "Split hoof cud land animals; water fins scales; bird ban list; winged swarmers legs joint hop allowed kinds.",
      [
        ("STEP_L11A_A1", "11:1-8", "LAND_ANIMALS", "זֹאת הַחַיָּה … מַפְרֶסֶת פַּרְסָה … מַעֲלַת גֵּרָה", "zot ha-chayah … mafreset parsah … ma'alat gerah",
         "Speak Israel: land animals you may eat: split hoof true + cud; camel hyrax hare swine listed unclean though one sign; not eat carcass not touch."),
        ("STEP_L11A_B1", "11:9-12", "WATER", "מִכֹּל אֲשֶׁר בַּמָּיִם … סְנַפִּיר וְקַשְׂקֶשֶׂת", "mi-kol asher ba-mayim … snapir ve-kaskeset",
         "Water: fins and scales in seas rivers eat; without — detestable not eat."),
        ("STEP_L11A_C1", "11:13-23", "BIRDS_SWARMERS", "וְאֶת־אֵלֶּה תְּשַׁקְּצוּ מִן־הָעוֹף … הַהֹלֵךְ עַל־אַרְבַּע", "ve-et-eleh teshaktzu min-ha-of … ha-holekh al-arba",
         "Birds detestable list (eagle etc.); all winged walking on four detestable except jointed-leg hoppers listed kinds locust types."),
      ],
      [("S_food_animal_registry", "Land/water/bird food purity registry partial")],
      [("EXPORT_behemah_signs", "פַּרְסָה וְגֵרָה", "parsah ve-gerah", "Hoof and cud signs"),
       ("EXPORT_fins_scales", "סְנַפִּיר וְקַשְׂקֶשֶׂת", "snapir ve-kaskeset", "Fins and scales water rule")],
      [("IF land animal has true split hoof AND chews cud", "THEN may eat"),
       ("IF water creature has fins AND scales", "THEN may eat"),
       ("IF bird on detestable list", "THEN do not eat")]),
    B("lev_11_carcass_swarm_close", "11:24-47", 11, 24, 11, 47,
      "Carcass impurity; ground swarmers; holiness close (11:24–47)",
      "נְבֵלָה — שֶׁרֶץ — קְדֹשִׁים", "nevelah — sheretz — kedoshim", "Carcass — swarming thing — holy ones",
      ["lev_11_animals_water_birds"], "decision_table", "primary",
      "Touch carcass impure until evening; vessels; sheretz ground list; cistern exception; pure animals carcass impurity; be holy as I am holy; distinguish.",
      [
        ("STEP_L11B_A1", "11:24-40", "CARCASS_VESSELS", "וּלְאֵלֶּה תִּטַּמָּאוּ … נִבְלָתָם", "u-le'eleh tittamma'u … nivlatam",
         "For these be impure: whoever touches carcass impure evening; carries washes; every beast paw not hoof split unclean; vessels wood garment skin sack wash; earthen oven broken; spring/cistern pure; seed sown pure unless water+carcass; clean animal dies same impurity rules."),
        ("STEP_L11B_B1", "11:41-47", "SHERETZ_HOLY", "וְכָל־הַשֶּׁרֶץ … וְהִתְקַדִּשְׁתֶּם", "ve-khol-ha-sheretz … ve-hitkaddishtem",
         "All ground swarmers detestable not eat belly/four/many feet; not make selves detestable; be holy for I am holy; this is torah of beast bird every living soul water/swarming to distinguish impure/pure edible/not."),
      ],
      [("S_food_torah_complete", "Food purity torah 11 complete"), ("S_holy_people_food", "Holiness linked to diet distinctions")],
      [("EXPORT_torat_behemah", "תּוֹרַת הַבְּהֵמָה", "torat ha-behemah", "Torah of animals clean/unclean"),
       ("EXPORT_be_holy_food", "קְדֹשִׁים תִּהְיוּ", "kedoshim tihyu", "Be holy (food chapter close)")],
      [("IF touch carcass of unclean type", "THEN impure until evening; wash rules apply"),
       ("IF ground sheretz", "THEN not eat; detestable")]),
    B("lev_12_childbirth", "12:1-8", 12, 1, 12, 8,
      "Childbirth purity: male/female durations; birds if poor (12:1–8) v1 schedule rewrite",
      "יּוֹלֶדֶת", "yoledet", "A woman who gives birth",
      ["lev_11_carcass_swarm_close"], "decision_table", "primary",
      "IF bears male: impure 7 days as niddah; day 8 circumcise; 33 days blood purification; no holy enter/touch. IF female: 14 + 66. Then yearling lamb olah + pigeon/turtledove chatat; if poor two birds.",
      [
        ("STEP_L12_A1", "12:1-4", "MALE_CHILD", "אִשָּׁה כִּי תַזְרִיעַ וְיָלְדָה זָכָר", "ishah ki tazria ve-yaledah zakhar",
         "When woman conceives and bears male: impure seven days as in niddah separation; eighth day flesh foreskin circumcised; thirty-three days blood purification; not touch holy thing not come to mikdash until full."),
        ("STEP_L12_B1", "12:5", "FEMALE_CHILD", "וְאִם־נְקֵבָה תֵלֵד", "ve-im-nekevah teled",
         "If bears female: impure two weeks as niddah; sixty-six days blood purification."),
        ("STEP_L12_C1", "12:6-8", "OFFERING_POOR", "וּבִמְלֹאת … כֶּבֶשׂ … וְאִם־לֹא תִמְצָא יָדָהּ", "u-vimlot … keves … ve-im-lo timtza yadah",
         "When days full bring yearling lamb olah and young pigeon or turtledove chatat to Tent entrance priest; atonement pure from blood flow; if hand find not enough lamb: two turtledoves/pigeons one olah one chatat; atonement pure."),
      ],
      [("S_birth_male_path", "Male birth impurity clock"), ("S_birth_female_path", "Female birth impurity clock"), ("S_birth_offering", "Post-birth offerings / poverty branch")],
      [("EXPORT_yoledet", "יּוֹלֶדֶת", "yoledet", "Childbirth purity system"),
       ("EXPORT_dam_tohorah", "דְּמֵי טָהֳרָה", "demei tohorah", "Blood of purification period")],
      [("IF bears male", "THEN impure 7 days + 33 purification; day 8 milah"),
       ("IF bears female", "THEN impure 14 days + 66 purification"),
       ("IF cannot afford lamb", "THEN two birds for olah+chatat")]),
    B("lev_13_skin_initial", "13:1-17", 13, 1, 13, 17,
      "Skin disease initial cases: rising, scab, bright spot (13:1–17)",
      "צָרַעַת — שְׂאֵת סַפַּחַת בַּהֶרֶת", "tzara'at — se'et sappachat baheret", "Scale disease — rising scab bright spot",
      ["lev_12_childbirth"], "decision_table", "primary",
      "Priest inspects skin lesions: white hair deeper; quarantine 7 days; recheck; white all skin = clean turn; raw flesh impure.",
      [
        ("STEP_L13A_A1", "13:1-8", "SEET_BAHERET", "אָדָם כִּי־יִהְיֶה … וְהוּבָא אֶל־אַהֲרֹן", "adam ki-yihyeh … ve-huva el-aharon",
         "Person with rising scab bright spot of tzara'at skin: brought to Aaron/sons; priest sees if hair white and appearance deeper than skin — declare impure tzara'at; if not white hair not deeper — shut 7 days; day 7 look; if spread impure."),
        ("STEP_L13A_B1", "13:9-17", "OLD_LESION_RAW", "נֶגַע צָרַעַת … בָּשָׂר חַי", "nega tzara'at … basar chai",
         "When tzara'at lesion: white rising white hair quick raw flesh — old tzara'at impure; if white lesion covers all skin from head foot — all turned white clean; when raw flesh appears impure; raw turns white come to priest clean."),
      ],
      [("S_nega_skin_protocol", "Skin nega inspection protocol open")],
      [("EXPORT_tzaraat_skin", "צָרַעַת עוֹר", "tzara'at or", "Skin scale-disease diagnostics start")],
      [("IF white hair AND deeper than skin", "THEN priest declares tame tzara'at"),
       ("IF lesion covers entire body white", "THEN declare tahor"),
       ("IF raw flesh in lesion", "THEN declare tame")]),
    B("lev_13_boil_burn", "13:18-28", 13, 18, 13, 28,
      "Skin disease after boil or burn (13:18–28)",
      "שְׁחִין — מִכְוַת־אֵשׁ", "shechin — mikhvat-esh", "Boil — burn of fire",
      ["lev_13_skin_initial"], "decision_table", "primary",
      "After healed boil or fire burn: bright white-red spots; white hair deeper = tzara'at; else quarantine rules.",
      [
        ("STEP_L13B_A1", "13:18-23", "AFTER_BOIL", "וּבָשָׂר כִּי־יִהְיֶה בוֹ־שְׁחִין", "u-vasar ki-yihyeh vo-shechin",
         "Flesh with boil healed: white rising or red-white bright; priest: if deeper white hair — tzara'at from boil impure; if no white hair not deeper faded — shut 7; if spreading impure; if stays scar of boil clean."),
        ("STEP_L13B_B1", "13:24-28", "AFTER_BURN", "אוֹ בָשָׂר כִּי־יִהְיֶה בְעֹרוֹ מִכְוַת־אֵשׁ", "o vasar ki-yihyeh be-oro mikhvat-esh",
         "Fire burn raw: red-white or white bright; same white hair deeper = tzara'at from burn; quarantine/spread/scar logic parallel to boil."),
      ],
      [("S_boil_burn_paths", "Post-boil and post-burn nega paths")],
      [("EXPORT_shechin_mikhvah", "שְׁחִין וּמִכְוָה", "shechin u-mikhvah", "Boil and burn lesion paths")],
      [("IF lesion after boil/burn with white hair deeper", "THEN tzara'at impure"),
       ("IF stays put as scar only", "THEN clean")]),
    B("lev_13_head_isolation", "13:29-46", 13, 29, 13, 46,
      "Head/beard nethek; dull white; bald; isolation of metzora (13:29–46)",
      "נֶתֶק — הַצָּרוּעַ", "netek — ha-tzarua", "Scalp break — the one with scale disease",
      ["lev_13_boil_burn"], "decision_table", "primary",
      "Nethek head/beard yellow thin hair; quarantine shave; bohak clean; bald forehead white-red impure; torn clothes hair loose cover lip unclean dwell outside camp alone.",
      [
        ("STEP_L13C_A1", "13:29-37", "NETHEK", "וְאִישׁ אוֹ אִשָּׁה כִּי־יִהְיֶה בוֹ נָגַע בְּרֹאשׁ", "ve-ish o ishah ki-yihyeh vo naga be-rosh",
         "Man or woman lesion head or beard: priest sees deeper thin yellow hair — netek tzara'at impure; if no black/deep — shut 7; day 7 no yellow not deep shave except netek shut another 7; black hair grown clean; spread without yellow still impure."),
        ("STEP_L13C_B1", "13:38-46", "BOHAK_BALD_ISOLATE", "בֶּהָרֹת בֶּהָרֹת … וְהַצָּרוּעַ", "beharot beharot … ve-ha-tzarua",
         "White bright spots bohak faded white clean; man loses head hair bald clean; forehead bald white-red lesion tzara'at; priest declares; the tzarua: clothes torn hair loose mustache cover unclean unclean; all days lesion impure dwell alone outside camp."),
      ],
      [("S_metzora_isolated", "Declared metzora isolation rules active")],
      [("EXPORT_metzora_outside", "מִחוּץ לַמַּחֲנֶה", "mi-chutz la-machaneh", "Metzora dwells outside camp"),
       ("EXPORT_netek", "נֶתֶק", "netek", "Head/beard scale break")],
      [("IF netek with thin yellow hair deeper", "THEN declare tame"),
       ("IF confirmed tzarua", "THEN outside camp; torn clothes; cover lip; call unclean")]),
    B("lev_13_garment", "13:47-59", 13, 47, 13, 59,
      "Garment nega: wool linen leather (13:47–59)",
      "צָרַעַת הַבֶּגֶד", "tzara'at ha-beged", "Scale disease of the garment",
      ["lev_13_head_isolation"], "decision_table", "primary",
      "Green/red lesion in wool linen warp weft leather: shut 7; wash; if spread burn; if fades tear; if returns burn; if dim wash clean.",
      [("STEP_L13G_A1", "13:47-59", "GARMENT_NEGA", "וְהַבֶּגֶד כִּי־יִהְיֶה בוֹ נֶגַע צָרַעַת", "ve-ha-beged ki-yihyeh vo nega tzara'at",
        "Garment wool/linen warp weft or leather work with greenish/reddish nega: show priest; shut 7; if spread — fretting tzara'at burn; if not spread wash shut 7; if still after wash — burn; if faded tear from garment; if reappears fretting burn; if dim after wash wash again clean; this torah of nega tzara'at garment wool linen leather to declare pure/impure.")],
      [("S_garment_nega", "Garment tzara'at protocol complete"), ("S_ch13_skin_garment_closed", "Chapter 13 diagnostics closed")],
      [("EXPORT_tzaraat_beged", "צָרַעַת בֶּגֶד", "tzara'at beged", "Garment scale-disease rules")],
      [("IF garment nega spreads after shut", "THEN burn garment"),
       ("IF fades after wash", "THEN tear out; if returns burn")]),
    B("lev_14_metzora_cleanse", "14:1-32", 14, 1, 14, 32,
      "Cleansing of metzora: birds, shaving, offerings; poverty branch (14:1–32)",
      "תּוֹרַת הַמְּצֹרָע", "torat ha-metzora", "Law of the one to be cleansed from scale disease",
      ["lev_13_garment"], "decision_table", "primary",
      "Outside camp birds cedar scarlet hyssop; shave wash day 1/7/8; lamb asham oil; chatat olah minchah; if poor reduced animals.",
      [
        ("STEP_L14M_A1", "14:1-20", "CLEANSE_FULL", "וְהוּבָא אֶל־הַכֹּהֵן … שְׁתֵּי־צִפֳּרִים", "ve-huva el-ha-kohen … shetei-tzipporim",
         "Torat metzora day of cleansing: priest outside camp look; two live pure birds cedar scarlet hyssop; slaughter one bird earthen over living water; dip live bird; sprinkle seven; release live bird field; wash clothes shave wash camp but tent outside 7; day 7 shave all hair wash; day 8 two male lambs ewe flour oil; asham log oil wave; blood ear thumb toe; oil; chatat olah minchah atonement."),
        ("STEP_L14M_B1", "14:21-32", "CLEANSE_POOR", "וְאִם־דַּל הוּא", "ve-im-dal hu",
         "If poor: one lamb asham; tenth flour oil; two turtledoves/pigeons chatat olah; same blood/oil ear thumb toe rite; this torah in whom nega when hand cannot reach cleansing."),
      ],
      [("S_metzora_reentry", "Metzora cleansing and reentry path")],
      [("EXPORT_torat_metzora", "תּוֹרַת הַמְּצֹרָע", "torat ha-metzora", "Cleansing procedure for metzora"),
       ("EXPORT_metzora_poor", "אִם־דַּל", "im-dal", "Poverty reduction for metzora offerings")],
      [("IF metzora healed", "THEN bird rite outside + 7 days + day-8 offerings"),
       ("IF poor", "THEN one lamb asham + two birds instead of full flock set")]),
    B("lev_14_house_nega", "14:33-57", 14, 33, 14, 57,
      "House nega in land; cleanse or demolish (14:33–57)",
      "צָרַעַת הַבָּיִת", "tzara'at ha-bayit", "Scale disease of the house",
      ["lev_14_metzora_cleanse"], "decision_table", "primary",
      "When in Canaan: green/red wall depressions; empty house; shut 7; scrape stones; if returns demolish; cleanse with birds if healed; torah summary all nega.",
      [
        ("STEP_L14H_A1", "14:33-47", "HOUSE_INSPECT", "כִּי תָבֹאוּ … נֶגַע צָרַעַת בְּבֵית", "ki tavo'u … nega tzara'at be-veit",
         "When come to Canaan land I give: house nega; owner tells priest; empty house before priest enters; greenish reddish wall lower than wall; shut 7; if spread — remove stones cast impure place; scrape house dust; new stones plaster."),
        ("STEP_L14H_B1", "14:48-57", "HOUSE_CLEANSE_OR_FALL", "וְאִם־יָשׁוּב … וְנָתַץ … וְטִהַר", "ve-im-yashuv … ve-natatz … ve-tihar",
         "If nega returns after pullout/plaster: fretting demolish house stones wood plaster; enterer impure evening; who lies/eats wash clothes; if not spread after plaster priest declares clean; bird cedar scarlet hyssop rite like person; this torah every nega tzara'at netek garment house rising scab spot to teach pure day impure day."),
      ],
      [("S_house_nega", "House nega land protocol"), ("S_nega_torah_summary", "Full nega torah summary closed")],
      [("EXPORT_tzaraat_bayit", "צָרַעַת בַּיִת", "tzara'at bayit", "House scale-disease rules"),
       ("EXPORT_torat_nega_all", "תּוֹרַת כָּל־נֶגַע", "torat kol-nega", "Torah of all plague-signs")],
      [("IF house nega spreads after repair", "THEN demolish house"),
       ("IF not spread after plaster", "THEN cleanse with bird rite; declare tahor")]),
    B("lev_15_male_discharge", "15:1-18", 15, 1, 15, 18,
      "Male zav and semen impurity (15:1–18)",
      "זָב — שִׁכְבַת־זֶרַע", "zav — shikhvat-zera", "One with discharge — lying of seed",
      ["lev_14_house_nega"], "decision_table", "primary",
      "Zav running issue impurity transfer vessels bed; count 7 clean; birds day 8; semen bath impurity; with woman both bathe.",
      [
        ("STEP_L15M_A1", "15:1-15", "ZAV", "אִישׁ אִישׁ כִּי יִהְיֶה זָב", "ish ish ki yihyeh zav",
         "Man with discharge from flesh: impure; bedding sitting saddle touched; spit; clay broken; stone washed; when zav cleansed from issue count 7 wash clothes bathe living water; day 8 two turtledoves/pigeons Tent entrance chatat olah atonement."),
        ("STEP_L15M_B1", "15:16-18", "SEMEN", "וְאִישׁ כִּי־תֵצֵא … שִׁכְבַת־זֶרַע", "ve-ish ki-tetze … shikhvat-zera",
         "Emission of seed: bathe whole body impure evening; garment skin seed on it wash impure evening; woman with whom man lies seed — both bathe impure evening."),
      ],
      [("S_zav_male", "Male discharge purity state machine")],
      [("EXPORT_zav", "זָב", "zav", "Male genital discharge impurity"),
       ("EXPORT_shikhvat_zera", "שִׁכְבַת־זֶרַע", "shikhvat-zera", "Semen impurity rules")],
      [("IF zav cleansed", "THEN count 7 clean days; day 8 two birds"),
       ("IF semen emission", "THEN bathe; impure until evening")]),
    B("lev_15_female_discharge", "15:19-33", 15, 19, 15, 33,
      "Niddah and female zavah; summary of discharges (15:19–33)",
      "נִדָּה — זָבָה", "niddah — zavah", "Menstruation — female discharge",
      ["lev_15_male_discharge"], "decision_table", "primary",
      "Niddah 7 days; contacts impure; if issue beyond or not in niddah many days: count 7 after stop; birds day 8; warn Israel separate from uncleanness lest die defiling mishkan.",
      [
        ("STEP_L15F_A1", "15:19-24", "NIDDAH", "וְאִשָּׁה כִּי־תִהְיֶה זָבָה … נִדָּתָהּ", "ve-ishah ki-tihyeh zavah … niddatah",
         "Woman discharge blood flesh: niddah seven days; touchers impure evening; bedding sitting; man who lies with her — niddah impurity seven days bedding impure."),
        ("STEP_L15F_B1", "15:25-33", "ZAVAH_SUMMARY", "וְאִשָּׁה כִּי־יָזוּב … וְהִזַּרְתֶּם", "ve-ishah ki-yazuv … ve-hizzartem",
         "If blood many days not in niddah time or beyond niddah: all days issue like niddah impure; when clean count 7; day 8 two birds chatat olah; separate Israel from their impurity lest die by defiling mishkan; this torah zav zavah semen niddah male female lying with impure."),
      ],
      [("S_niddah_zavah", "Female discharge states"), ("S_purity_spine_15_closed", "Discharge purity 15 closed; mishkan defilement warning")],
      [("EXPORT_niddah", "נִדָּה", "niddah", "Menstrual impurity seven days"),
       ("EXPORT_zavah", "זָבָה", "zavah", "Extended female blood discharge"),
       ("EXPORT_mishkan_defile_warn", "בְּטַמְּאָם אֶת־מִשְׁכָּנִי", "be-tam'am et-mishkani", "Death risk if defile mishkan by impurity")],
      [("IF niddah", "THEN impure 7 days; contacts impure"),
       ("IF zavah then stops", "THEN count 7; day 8 two birds")]),
    # Phase D
    B("lev_16_yk_entry_blood", "16:1-19", 16, 1, 16, 19,
      "Yom Kippur: entry limits; two goats; blood sequence (16:1–19)",
      "יוֹם הַכִּפֻּרִים — שְׁנֵי הַשְּׂעִירִם", "yom ha-kippurim — shenei ha-se'irim", "Day of Atonement — the two goats",
      ["lev_15_female_discharge", "exo_30_incense_shekel"], "boot_steps", "primary",
      "After Nadav death: not enter anytime within veil; bull chatat; two goats lot YHWH/Azazel; incense cloud; blood on kapporet; purify holy.",
      [
        ("STEP_L16A_A1", "16:1-10", "ENTRY_LOTS", "אַל־יָבֹא בְכָל־עֵת … גּוֹרָל", "al-yavo be-khol-et … goral",
         "After death of two sons: speak Aaron not enter anytime holy within veil before kapporet lest die; cloud on kapporet; bull chatat ram olah; holy linen; two goats lots one YHWH one Azazel; present goat YHWH; Azazel live before YHWH atonement send wilderness."),
        ("STEP_L16A_B1", "16:11-19", "BLOOD_INNER", "וְהִקְרִיב … הַקְּטֹרֶת … הַדָּם", "ve-hikriv … ha-ketoret … ha-dam",
         "Slaughter bull; firepan coals incense within veil cloud covers kapporet; sprinkle blood kapporet east seven times; slaughter goat YHWH; blood kapporet; atone holy for impurities Israel; no man in Tent until he exits; blood altar horns purify."),
      ],
      [("S_yk_blood_done", "YK inner blood sequence set")],
      [("EXPORT_yom_kippur", "יוֹם הַכִּפֻּרִים", "yom ha-kippurim", "Day of Atonement core rite"),
       ("EXPORT_azazel", "עֲזָאזֵל", "azazel", "Goat to Azazel"),
       ("EXPORT_kapporet_blood", "דָּם עַל־הַכַּפֹּרֶת", "dam al-ha-kapporet", "Blood on the cover")],
      imports_en="Veil kapporet incense altar from Exodus mishkan install."),
    B("lev_16_yk_goat_statute", "16:20-34", 16, 20, 16, 34,
      "YK: confession on live goat; burnt offerings; eternal statute (16:20–34)",
      "וְהִתְוַדָּה — חֻקַּת עוֹלָם", "ve-hitvaddah — chukkat olam", "And he shall confess — eternal statute",
      ["lev_16_yk_entry_blood"], "decision_table", "primary",
      "Hands on live goat confess iniquities send by ish itti wilderness; change garments burn chatat; bathe; olah; seventh month tenth day afflict souls rest; once yearly eternal.",
      [
        ("STEP_L16B_A1", "16:20-28", "GOAT_AWAY_BURN", "וְסָמַךְ … וְשִׁלַּח … וְאֵת פַּר הַחַטָּאת", "ve-samakh … ve-shillach … ve-et par ha-chatat",
         "Finish atoning holy Tent altar: live goat; two hands confess all iniquities rebellions sins Israel on head; send by designated man wilderness; goat bears iniquities land cut off; Aaron enter strip bathe garments; offer olah; fat chatat burn; sender wash; burners of bull/goat outside wash."),
        ("STEP_L16B_B1", "16:29-34", "STATUTE_FOREVER", "בַּחֹדֶשׁ הַשְּׁבִיעִי בֶּעָשׂוֹר … חֻקַּת עוֹלָם", "ba-chodesh ha-shevi'i be-asor … chukkat olam",
         "Eternal statute seventh month tenth day: afflict souls no work native or ger; atonement purify; for priest forever once yearly as commanded; Moses did."),
      ],
      [("S_yk_complete", "YK full rite + annual statute")],
      [("EXPORT_asor_month7", "בֶּעָשׂוֹר לַחֹדֶשׁ", "be-asor la-chodesh", "Tenth of seventh month statute"),
       ("EXPORT_innui_nefesh", "תְּעַנּוּ אֶת־נַפְשֹׁתֵיכֶם", "te'annu et-nafshoteikhem", "Afflict your souls")],
      [("IF tenth of seventh month", "THEN afflict souls; no work; annual atonement rite")]),
    B("lev_17_blood_center", "17:1-16", 17, 1, 17, 16,
      "Slaughter at Tent; blood is life; no eating blood/neveilah (17:1–16)",
      "כִּי נֶפֶשׁ הַבָּשָׂר בַּדָּם", "ki nefesh ha-basar ba-dam", "For the life of the flesh is in the blood",
      ["lev_16_yk_goat_statute"], "decision_table", "primary",
      "Slaughter ox/sheep/goat in camp or out must bring to Tent shelamim else bloodguilt; no more field goats; blood not eat — life for atonement on altar; cover blood hunt; neveilah/terefah wash impure.",
      [
        ("STEP_L17_A1", "17:1-9", "SHECHITAH_TENT", "אִישׁ אִישׁ … אֲשֶׁר יִשְׁחַט", "ish ish … asher yishchat",
         "Any house Israel who slaughters ox lamb goat camp or outside and does not bring to Tent entrance as offering YHWH — blood imputed; cut off; bring shelamim; priest dash blood burn fat; no more sacrifices to se'irim; ger same; not offer except Tent entrance."),
        ("STEP_L17_B1", "17:10-16", "BLOOD_LIFE", "וְאִישׁ … דָּם … כִּי־נֶפֶשׁ הַבָּשָׂר בַּדָּם הִוא", "ve-ish … dam … ki-nefesh ha-basar ba-dam hi",
         "Anyone eating any blood — set face cut off; life of flesh in blood I gave on altar atone for lives; blood atones by life; cover blood of hunt bird beast with earth; neveilah terefah wash clothes bathe impure evening; if not bear iniquity."),
      ],
      [("S_blood_theology", "Blood = life for altar atonement"), ("S_central_slaughter", "Central slaughter at Tent for herd animals")],
      [("EXPORT_nefesh_ba_dam", "נֶפֶשׁ בַּדָּם", "nefesh ba-dam", "Life is in the blood"),
       ("EXPORT_dam_altar_kipper", "הַדָּם יְכַפֵּר", "ha-dam yekhapper", "Blood atones on the altar")],
      [("IF slaughter ox/sheep/goat and not bring to Tent", "THEN bloodguilt; cut off"),
       ("IF eat blood", "THEN cut off"),
       ("IF eat neveilah/terefah", "THEN wash; impure evening")]),
    # Phase E
    B("lev_18_sexual_land", "18:1-30", 18, 1, 18, 30,
      "Sexual prohibitions; do not copy Egypt/Canaan; land vomits (18:1–30)",
      "עֶרְוָה — חֻקּוֹת הַגּוֹי", "ervah — chukkot ha-goy", "Nakedness — statutes of the nation",
      ["lev_17_blood_center"], "decision_table", "primary",
      "Do not do Egypt/Canaan deeds; walk My mishpatim; list of forbidden ervah relations; molech; male lie; beast; land vomits nations; keep statutes lest vomit you.",
      [
        ("STEP_L18_A1", "18:1-5", "FRAME", "כְּמַעֲשֵׂה אֶרֶץ־מִצְרַיִם … וָחַי בָּהֶם", "ke-ma'aseh eretz-mitzrayim … va-chai bahem",
         "I am YHWH; not do deeds of Egypt where you dwelt nor Canaan land I bring; not walk their statutes; do My mishpatim and chukkim live by them."),
        ("STEP_L18_B1", "18:6-23", "ERVAH_LIST", "אִישׁ אִישׁ … עֶרְוַת", "ish ish … ervat",
         "None approach any near kin uncover nakedness; list: father mother father's wife sister granddaughter aunt uncle daughter-in-law brother's wife woman+daughter etc.; niddah; neighbor wife; molech; male as lie woman; beast."),
        ("STEP_L18_C1", "18:24-30", "LAND_VOMIT", "אַל־תִּטַּמְּאוּ … וַתָּקִא הָאָרֶץ", "al-tittamme'u … va-taki ha-aretz",
         "Do not defile in any of these; nations defiled land vomited; you keep chukkot mishpatim; abominations cut off; keep My charge not do abominable chukkot."),
      ],
      [("S_ervah_registry", "Forbidden sexual relations registry"), ("S_land_ethics", "Land vomit ethics loaded")],
      [("EXPORT_ervah", "עֶרְוָה", "ervah", "Forbidden uncovering of nakedness list"),
       ("EXPORT_land_vomit", "וַתָּקִא הָאָרֶץ", "va-taki ha-aretz", "Land vomits inhabitants for defilement")],
      [("IF approach listed kin ervah", "THEN forbidden (defilement)"),
       ("IF do Canaan abominations", "THEN land will vomit you out")]),
    B("lev_19_holiness_neighbor", "19:1-18", 19, 1, 19, 18,
      "Kedoshim: revere parents; Shabbat; poor edges; love neighbor (19:1–18)",
      "קְדֹשִׁים תִּהְיוּ", "kedoshim tihyu", "You shall be holy",
      ["lev_18_sexual_land"], "decision_table", "primary",
      "Be holy; fear mother father; Shabbat; no idols; shelamim day rules; pe'ah leket for poor ger; no steal lie; no oppress; wages; deaf blind; justice; no hate revenge; love neighbor as self.",
      [
        ("STEP_L19A_A1", "19:1-8", "HOLY_PARENTS_SHABBAT", "קְדֹשִׁים תִּהְיוּ … אִישׁ אִמּוֹ וְאָבִיו תִּירָאוּ", "kedoshim tihyu … ish immo ve-aviv tira'u",
         "Speak edah: be holy for I YHWH holy; revere mother father keep Shabbat; no turn to idols molten gods; shelamim acceptance two days; day three burn; eater day three bear iniquity cut off."),
        ("STEP_L19A_B1", "19:9-18", "POOR_NEIGHBOR", "וּבְקֻצְרְכֶם … וְאָהַבְתָּ לְרֵעֲךָ כָּמוֹךָ", "u-ve-kutzrekhem … ve-ahavta le-re'akha kamokha",
         "Harvest: not finish corner not gather gleaning vineyard; leave poor and ger; no steal deal falsely; no swear My name false; no oppress rob; wages same day; no curse deaf before blind stumble; no injustice judgment; no hate brother; reprove; no revenge grudge; love neighbor as yourself I YHWH."),
      ],
      [("S_kedoshim_open", "Holiness code open"), ("S_love_neighbor", "Love neighbor command loaded")],
      [("EXPORT_kedoshim", "קְדֹשִׁים תִּהְיוּ", "kedoshim tihyu", "Be holy command"),
       ("EXPORT_ahavta_re'akha", "וְאָהַבְתָּ לְרֵעֲךָ כָּמוֹךָ", "ve-ahavta le-re'akha kamokha", "Love your neighbor as yourself"),
       ("EXPORT_peah_leket", "פֵּאָה לֶקֶט", "pe'ah leket", "Corner and gleaning for poor")],
      [("IF harvest", "THEN leave pe'ah and gleanings for poor and ger"),
       ("IF day laborer", "THEN pay wages that day")]),
    B("lev_19_mixtures_weights", "19:19-37", 19, 19, 19, 37,
      "Mixtures; trees; fair dealing; ger; just weights (19:19–37)",
      "כִּלְאַיִם — מֹאזְנֵי צֶדֶק", "kil'ayim — moznei tzedek", "Mixed kinds — scales of righteousness",
      ["lev_19_holiness_neighbor"], "decision_table", "primary",
      "No kilayim animals seed garments; slave woman betrothed case; orlah fruit years; no blood divination; pe'ot beard; tattoos; daughter harlotry; Shabbat mikdash; ov/yidoni; elder honor; ger love; just ephah hin.",
      [
        ("STEP_L19B_A1", "19:19-25", "KILAYIM_ORLAH", "בְּהֶמְתְּךָ לֹא־תַרְבִּיעַ כִּלְאַיִם … עָרְלָה", "behemtekha lo-tarbi'a kil'ayim … orlah",
         "Keep chukkim: no cross animals; no two-seed field; no sha'atnez garment; case of designated slave woman; when enter land fruit trees — three years orlah; year four holy praise; year five eat increase."),
        ("STEP_L19B_B1", "19:26-37", "DIVINATION_GER_WEIGHTS", "לֹא תֹאכְלוּ עַל־הַדָּם … מֹאזְנֵי צֶדֶק", "lo tokhlu al-ha-dam … moznei tzedek",
         "No eat on blood; no divination; no sideburns corner beard; no flesh cuts for dead tattoos; do not profane daughter harlotry; keep Shabbat revere mikdash; no ov yidoni; rise before grey honor elder; not wrong ger love as self for you were gerim; just balances weights ephah hin; keep all chukkim mishpatim."),
      ],
      [("S_holiness_19_complete", "Chapter 19 holiness cluster complete")],
      [("EXPORT_kilayim", "כִּלְאַיִם", "kil'ayim", "Forbidden mixtures"),
       ("EXPORT_orlah", "עָרְלָה", "orlah", "Young tree fruit restriction"),
       ("EXPORT_moznei_tzedek", "מֹאזְנֵי צֶדֶק", "moznei tzedek", "Just scales and measures"),
       ("EXPORT_ger_kamokha", "וַאֲהַבְתָּ לוֹ כָּמוֹךָ", "ve-ahavta lo kamokha", "Love the ger as yourself")],
      [("IF fruit tree first three years in land", "THEN orlah not eat"),
       ("IF commerce measures", "THEN just ephah and hin")]),
    B("lev_20_sanctions", "20:1-27", 20, 1, 20, 27,
      "Sanctions: Molech; ov; sexual penalties; holy people (20:1–27)",
      "מוֹת יוּמָת — עַם קָדוֹשׁ", "mot yumat — am kadosh", "He shall surely be put to death — holy people",
      ["lev_19_mixtures_weights"], "decision_table", "primary",
      "Molech death stone; set face; ov yidoni cut off; sanctify; curse parents death; adultery incest penalties; beast; separate pure impure animals; be holy I separate you; ov yidoni stone.",
      [
        ("STEP_L20_A1", "20:1-9", "MOLECH_OV_PARENTS", "אֲשֶׁר יִתֵּן מִזַּרְעוֹ לַמֹּלֶךְ", "asher yitten mi-zaro la-molekh",
         "Give seed to Molech: death stone people; I set face cut off; if people hide I set face family cut off; turn to ov yidoni set face; sanctify be holy; curse father mother death blood on them."),
        ("STEP_L20_B1", "20:10-21", "SEXUAL_PENALTIES", "וְאִישׁ אֲשֶׁר יִנְאַף … מוֹת יוּמַת", "ve-ish asher yin'af … mot yumat",
         "Adultery both death; father's wife; daughter-in-law; male lie both death; woman+mother fire; beast death; sister cut off; niddah; aunt; uncle's wife; brother wife childless."),
        ("STEP_L20_C1", "20:22-27", "SEPARATE_HOLY", "וּשְׁמַרְתֶּם … וָאַבְדִּל … אִישׁ אוֹ אִשָּׁה כִּי־יִהְיֶה בָהֶם אוֹב", "u-shmartem … va-avdil … ish o ishah ki-yihyeh bahem ov",
         "Keep chukkim mishpatim land not vomit; not walk nation statutes; I separate you; distinguish pure impure animals; be holy to Me I separate you to be Mine; man or woman ov yidoni death stone blood on them."),
      ],
      [("S_sanctions_registry", "Capital/cut-off sanctions registry"), ("S_holy_separate_people", "People separated as holy")],
      [("EXPORT_molekh_ban", "מֹלֶךְ", "molekh", "Molech seed ban death"),
       ("EXPORT_mot_yumat", "מוֹת יוּמָת", "mot yumat", "Death penalty formulas in holiness code")],
      [("IF give seed to Molech", "THEN death by stoning"),
       ("IF ov or yidoni", "THEN death by stoning")]),
    # Phase F
    B("lev_21_priest_family", "21:1-15", 21, 1, 21, 15,
      "Priest mourning and marriage limits; high priest (21:1–15)",
      "כֹּהֲנִים — אִשָּׁה זֹנָה", "kohanim — ishah zonah", "Priests — a harlot woman",
      ["lev_20_sanctions", "exo_28_priest_garments"], "decision_table", "primary",
      "Sons of Aaron not defile dead except close kin; no bald/shave/flesh cuts; not marry zonah chalalah divorcee; daughter harlotry fire; high priest not unkempt not tear not leave mikdash not defile dead even parents; marry virgin of people.",
      [
        ("STEP_L21A_A1", "21:1-9", "PRIEST_MOURN_MARRY", "לְנֶפֶשׁ לֹא־יִטַּמָּא … כִּי אִם־לִשְׁאֵרוֹ", "le-nefesh lo-yittamma … ki im-li-she'ero",
         "Speak priests sons Aaron: none defile among people for dead except mother father son daughter brother virgin sister near him; not bald head edge beard cuts flesh; holy their God; not marry zonah defiled or divorced; sanctify him; priest daughter harlot profanes father burned."),
        ("STEP_L21A_B1", "21:10-15", "HIGH_PRIEST", "וְהַכֹּהֵן הַגָּדוֹל … בְּתוּלָה", "ve-ha-kohen ha-gadol … betulah",
         "High priest anointed garments: not free hair not tear clothes; not in any dead souls not father mother defile; not leave mikdash not profane; marry woman in virginity; not widow divorcee chalalah zonah — virgin from peoples; not profane seed."),
      ],
      [("S_priest_family_rules", "Priest family purity/marriage rules")],
      [("EXPORT_kohen_dead", "לְנֶפֶשׁ לֹא־יִטַּמָּא", "le-nefesh lo-yittamma", "Priest corpse-defilement limits"),
       ("EXPORT_kohen_gadol_virgin", "בְּתוּלָה יִקָּח", "betulah yikkach", "High priest marries virgin")],
      [("IF ordinary priest near kin dies", "THEN may defile for listed relatives only"),
       ("IF high priest", "THEN no corpse defilement even for parents")]),
    B("lev_21_priest_blemish", "21:16-24", 21, 16, 21, 24,
      "Blemished priest: may eat holy; not approach to offer (21:16–24)",
      "מוּם — לֹא יִגַּשׁ", "mum — lo yiggash", "Blemish — he shall not approach",
      ["lev_21_priest_family"], "decision_table", "primary",
      "Any seed with blemish not approach offer isheh; list blind lame etc.; may eat holy most holy; not come to parokhet altar.",
      [("STEP_L21B_A1", "21:16-24", "MUM_LIST", "אִישׁ מִזַּרְעֲךָ … אֲשֶׁר יִהְיֶה בוֹ מוּם", "ish mi-zar'akha … asher yihyeh vo mum",
        "Speak Aaron: man of your seed generations with blemish not approach offer bread of God; no blind lame mutilated limb overgrown; list broken foot hand hunchback dwarf eye growth itch scabs crushed testicles; with blemish not approach; food of God most holy and holy he may eat; not come to veil not approach altar not profane; Moses speaks Aaron sons all Israel.")],
      [("S_priest_blemish", "Blemish bars altar service not eating")],
      [("EXPORT_mum_kohen", "מוּם בַּכֹּהֵן", "mum ba-kohen", "Priest physical blemish bars offering service")],
      [("IF priest has listed mum", "THEN may eat holy food but not approach to offer")]),
    B("lev_22_holy_food", "22:1-16", 22, 1, 22, 16,
      "Who may eat holy things; purity gates (22:1–16)",
      "קָדָשִׁים — תּוֹשָׁב כֹּהֵן", "kodashim — toshav kohen", "Holy things — priest's resident",
      ["lev_21_priest_blemish"], "decision_table", "primary",
      "Priests separate from holy when impure; zav etc until evening bathe; outsider not eat; toshav hireling not; slave bought may; daughter married out not; widow return may; accidental eater add fifth.",
      [
        ("STEP_L22A_A1", "22:1-9", "IMPURE_PRIEST", "וְיִנָּזְרוּ … בְּטֻמְאָתָם", "ve-yinnazeru … be-tum'atam",
         "Aaron sons separate from holy of Israel not profane; any with tzara'at or zav not eat holy until clean; touches corpse sheretz emission — bathe impure until evening then eat; torn/neveilah not eat; keep charge not die."),
        ("STEP_L22A_B1", "22:10-16", "WHO_EATS", "וְכָל־זָר לֹא־יֹאכַל קֹדֶשׁ", "ve-khol-zar lo-yokhal kodesh",
         "No outsider eat holy; priest's toshav and hireling not; slave bought money or house born may eat; daughter married to zar not; widow/divorcee without child returns father's house as youth may eat; if man eats holy in error add fifth give priest; not profane holy of Israel."),
      ],
      [("S_holy_food_eligibility", "Holy food who-may-eat registry")],
      [("EXPORT_zar_lo_yokhal", "זָר לֹא־יֹאכַל קֹדֶשׁ", "zar lo-yokhal kodesh", "Outsider may not eat holy food"),
       ("EXPORT_fifth_mistaken_holy", "וְיָסַף חֲמִישִׁתוֹ", "ve-yasaf chamishito", "Add fifth if eats holy in error")],
      [("IF priest impure (zav/tzara'at/contact)", "THEN not eat holy until clean process"),
       ("IF zar (outsider)", "THEN not eat kodesh")]),
    B("lev_22_acceptable_offerings", "22:17-33", 22, 17, 22, 33,
      "Acceptable offerings: no blemish; freewill vs vow; desecration ban (22:17–33)",
      "תָּמִים — מוּם לֹא תַקְרִיבוּ", "tamim — mum lo takrivu", "Whole — do not bring a blemish",
      ["lev_22_holy_food"], "decision_table", "primary",
      "Nedavah/neder olah shelamim must be whole male cattle sheep goats; blemish list rejected; freewill may allow some defects for freewill not vow; no castrated; newborn day 8; mother young same day ban; thanksgiving same day; not profane; I sanctify.",
      [
        ("STEP_L22B_A1", "22:17-25", "NO_BLEMISH", "לְרָצֹן … תָּמִים זָכָר", "le-ratzon … tamim zakhar",
         "Anyone Israel or ger who brings olah vow or freewill: cattle sheep goats whole male for acceptance; anything with mum not accept; blind broken maimed warts itch scabs not offer isheh; ox sheep extended/contracted freewill ok not vow; bruised crushed torn cut not offer; from foreigner hand any of these not offer corruption mum not accepted."),
        ("STEP_L22B_B1", "22:26-33", "AGE_THANKS_HOLY", "שׁוֹר אוֹ־כֶשֶׂב … וִהְיִיתֶם קְדֹשִׁים", "shor o-kesev … vihyitem kedoshim",
         "Ox sheep goat seven days under mother; day eight onward accepted isheh; not slaughter ox/sheep and young one day; thanksgiving eaten same day; keep mitzvot; not profane holy name I be hallowed in Israel I sanctify you who brought you Egypt to be your God."),
      ],
      [("S_acceptable_korban", "Acceptable animal offering constraints closed")],
      [("EXPORT_tamim_korban", "תָּמִים", "tamim", "Unblemished requirement for vow/freewill altar animals"),
       ("EXPORT_day8_animal", "וּמִיּוֹם הַשְּׁמִינִי", "u-mi-yom ha-shemini", "Animal accepted from eighth day")],
      [("IF vow or freewill altar animal with mum", "THEN not accepted"),
       ("IF thanksgiving offering", "THEN eat same day")]),
    # Phase G
    B("lev_23_spring_festivals", "23:1-22", 23, 1, 23, 22,
      "Mo'adim: Shabbat; Pesach; matzot; omer; seven weeks; firstfruits; pe'ah (23:1–22)",
      "מוֹעֲדֵי יְהוָה — עֹמֶר", "mo'adei YHWH — omer", "Appointed times of YHWH — sheaf",
      ["lev_22_acceptable_offerings", "exo_23_justice_calendar"], "decision_table", "primary",
      "Speak mo'adim: Shabbat; 14th Nisan pesach; 15th matzot seven days; omer wave day after Shabbat; count fifty; new minchah two loaves; pe'ah for poor.",
      [
        ("STEP_L23A_A1", "23:1-8", "SHABBAT_PESACH_MATZOT", "מוֹעֲדֵי יְהוָה … בַּחֹדֶשׁ הָרִאשׁוֹן", "mo'adei YHWH … ba-chodesh ha-rishon",
         "Mo'adim holy proclamations: six days work seventh Shabbat shabbaton; 14th first month twilight pesach; 15th feast matzot seven days; day 1 and 7 mikra kodesh no work of service."),
        ("STEP_L23A_B1", "23:9-22", "OMER_SHAVUOT_PEAH", "וַהֲבֵאתֶם … עֹמֶר … שֶׁבַע שַׁבָּתוֹת", "va-haveitem … omer … sheva shabbatot",
         "When reap land bring omer first sheaf wave day after Shabbat; lamb minchah wine; bread/parched/carmel not until that day; count seven full weeks from day after Shabbat day you brought omer; day fifty new minchah two loaves seven lambs bull two rams; goat chatat two lambs shelamim wave; mikra kodesh; when reap leave pe'ah leket for poor ger."),
      ],
      [("S_spring_moadim", "Spring festival registry loaded")],
      [("EXPORT_moadim", "מוֹעֲדֵי יְהוָה", "mo'adei YHWH", "Appointed times calendar open"),
       ("EXPORT_omer", "עֹמֶר", "omer", "Wave-sheaf first barley"),
       ("EXPORT_count_fifty", "תִּסְפְּרוּ חֲמִשִּׁים", "tisperu chamishim", "Count fifty days to new minchah")],
      [("IF 14 Nisan twilight", "THEN pesach to YHWH"),
       ("IF day after Shabbat of omer week cycle", "THEN wave omer; start count to fifty")]),
    B("lev_23_fall_festivals", "23:23-44", 23, 23, 23, 44,
      "Mo'adim fall: shofar; affliction day; Sukkot (23:23–44)",
      "שַׁבָּתוֹן זִכְרוֹן תְּרוּעָה — סֻכּוֹת", "shabbaton zikhron teru'ah — sukkot", "Rest memorial blast — booths",
      ["lev_23_spring_festivals"], "decision_table", "primary",
      "7th month 1st shofar rest; 10th afflict souls atonement; 15th Sukkot seven days + eighth; take fruit branches rejoice; dwell booths; native Israel in sukkot.",
      [
        ("STEP_L23B_A1", "23:23-32", "SHOFAR_KIPPUR", "בַּחֹדֶשׁ הַשְּׁבִיעִי בְּאֶחָד … בֶּעָשׂוֹר", "ba-chodesh ha-shevi'i be-echad … be-asor",
         "Seventh month day one: shabbaton memorial teruah mikra kodesh no work of service isheh; tenth day: day ha-kippurim mikra kodesh afflict souls isheh; no work same day; any not afflicted cut off; any work destroy; shabbaton afflict ninth evening to evening."),
        ("STEP_L23B_B1", "23:33-44", "SUKKOT", "בַּחֲמִשָּׁה עָשָׂר יוֹם … חַג הַסֻּכּוֹת", "ba-chamishah asar yom … chag ha-sukkot",
         "15th seventh month feast sukkot seven days; day 1 mikra kodesh; seven days isheh; day 8 mikra kodesh atzeret; take day 1 fruit hadar palms brook willows rejoice before YHWH seven days; feast seven days year; booths seven days all native in Israel dwell booths so generations know I sat Israel in booths leaving Egypt; Moses declares mo'adim."),
      ],
      [("S_fall_moadim", "Fall festival registry loaded"), ("S_moadim_year_complete", "Full mo'adim year map complete")],
      [("EXPORT_teruah", "זִכְרוֹן תְּרוּעָה", "zikhron teru'ah", "Memorial of blast / shofar day"),
       ("EXPORT_sukkot", "חַג הַסֻּכּוֹת", "chag ha-sukkot", "Feast of booths"),
       ("EXPORT_atzeret_day8", "עֲצֶרֶת", "atzeret", "Eighth-day assembly")],
      [("IF 1 Tishri", "THEN shabbaton; teruah; no work of service"),
       ("IF 10 Tishri", "THEN afflict souls; no work; kippurim"),
       ("IF 15–21 Tishri", "THEN sukkot; day 8 atzeret")]),
    B("lev_24_lamp_bread", "24:1-9", 24, 1, 24, 9,
      "Pure oil for ner tamid; lechem ha-panim each Shabbat (24:1–9)",
      "שֶׁמֶן זַיִת — לֶחֶם הַפָּנִים", "shemen zayit — lechem ha-panim", "Olive oil — bread of the Presence",
      ["lev_23_fall_festivals", "exo_27_altar_court", "exo_25_ark_table_menorah"], "boot_steps", "medium",
      "Command pure beaten olive oil continual lamp outside veil Aharon arrange evening to morning; twelve loaves two rows frankincense; each Shabbat arrange everlasting covenant; Aaron sons eat holy place.",
      [
        ("STEP_L24A_A1", "24:1-4", "NER_TAMID", "שֶׁמֶן זַיִת זָךְ … נֵר תָּמִיד", "shemen zayit zakh … ner tamid",
         "Command Israel bring pure beaten olive oil for light to raise continual lamp; outside veil of testimony ohel mo'ed Aaron arranges evening to morning before YHWH statute forever; on pure menorah arrange lamps continually."),
        ("STEP_L24A_B1", "24:5-9", "LECHEM_PANIM", "וְלָקַחְתָּ סֹלֶת … שְׁתֵּים מַעֲרָכוֹת", "ve-lakachta solet … sheteim ma'arakhot",
         "Take fine flour bake twelve cakes two tenths each; set two rows six row on pure table before YHWH; pure frankincense on each row memorial isheh; each Shabbat day arrange before YHWH continually from Israel everlasting covenant; for Aaron sons eat holy place most holy from isheh everlasting statute."),
      ],
      [("S_lamp_bread_service", "Continual lamp and weekly bread service")],
      [("EXPORT_ner_tamid_lev", "נֵר תָּמִיד", "ner tamid", "Continual lamp (Lev restates Exod)"),
       ("EXPORT_lechem_panim", "לֶחֶם הַפָּנִים", "lechem ha-panim", "Bread of the Presence twelve loaves")],
      imports_en="Menorah table from Exod 25; oil lamp Exod 27; Tent Exod 40."),
    B("lev_24_blasphemer_talion", "24:10-23", 24, 10, 24, 23,
      "Blasphemer narrative; lex talionis; one law (24:10–23)",
      "נֹקֵב שֵׁם — עַיִן תַּחַת עַיִן", "nokev shem — ayin tachat ayin", "One who pierces the Name — eye for eye",
      ["lev_24_lamp_bread"], "narrative_fsm", "medium",
      "Mixed son blasphemes Name; custody until word; stone outside; murderer death; beast death; injury as did so done; ger and ezrach one mishpat.",
      [
        ("STEP_L24B_A1", "24:10-16", "BLASPHEMER", "וַיִּקֹּב … אֶת־הַשֵּׁם", "va-yikkov … et-ha-shem",
         "Son of Israelite woman and Egyptian man fights; blasphemes the Name and curses; bring to Moses; mother Shelomith Dibri Dan; custody until mouth of YHWH; bring blasphemer outside camp all hearers hands on head whole edah stone; speak Israel: man curses his God bears sin; pierces Name YHWH death stone ger ezrach."),
        ("STEP_L24B_B1", "24:17-23", "TALION", "וְאִישׁ כִּי יַכֶּה … עַיִן תַּחַת עַיִן", "ve-ish ki yakkeh … ayin tachat ayin",
         "Man kills any human death; kills beast pays life for life; injury to neighbor as he did so done to him: break for break eye for eye tooth for tooth; beast killer pays; human killer death; one mishpat ger and citizen; Moses speaks; bring blasphemer outside stone; Israel does as YHWH commanded."),
      ],
      [("S_name_sanctity", "Name blasphemy capital"), ("S_one_mishpat", "One law for ger and native")],
      [("EXPORT_nokev_shem", "נֹקֵב שֵׁם־יְהוָה", "nokev shem-YHWH", "Blaspheming the Name — death"),
       ("EXPORT_ayin_tachat_ayin_lev", "עַיִן תַּחַת עַיִן", "ayin tachat ayin", "Measure-for-measure injury (Lev 24)"),
       ("EXPORT_mishpat_echad", "מִשְׁפַּט אֶחָד", "mishpat echad", "One judgment for ger and ezrach")]),
    # Phase H
    B("lev_25_shemittah", "25:1-22", 25, 1, 25, 22,
      "Shemittah land rest; six years sow; seventh Sabbath (25:1–22)",
      "שַׁבַּת הָאָרֶץ", "shabbat ha-aretz", "Sabbath of the land",
      ["lev_24_blasphemer_talion", "exo_23_justice_calendar"], "decision_table", "primary",
      "When enter land: six years sow prune gather; seventh shabbaton for land; spontaneous growth for you slave hireling ger beast; ask what eat year 7 — blessing year 6 for three years.",
      [
        ("STEP_L25S_A1", "25:1-7", "YEAR7_REST", "כִּי תָבֹאוּ … וּבַשָּׁנָה הַשְּׁבִיעִת", "ki tavo'u … u-va-shanah ha-shevi'it",
         "When come to land I give: land keep Shabbat YHWH; six years sow field prune vineyard gather produce; seventh year shabbat shabbaton for land Shabbat to YHWH; field not sow vineyard not prune; spontaneous harvest not reap undressed grapes not gather; shabbaton for land; Sabbath yield food for you male female slave hireling sojourner; cattle beast in land all produce to eat."),
        ("STEP_L25S_B1", "25:8-22", "COUNT_JUBILEE_INTRO", "וְסָפַרְתָּ … תֵּשַׁע וְאַרְבָּעִים", "ve-safarta … tesh'a ve-arba'im",
         "Count seven shabbats of years 49; seventh month 10th pass shofar; hallow year 50 proclaim liberty; each return possession family; not sow year 50; if say what eat year 7 — command blessing year 6 produce three years; sow year 8 eat old until year 9 produce comes."),
      ],
      [("S_shemittah", "Land sabbath cycle"), ("S_yovel_announced", "Jubilee count introduced")],
      [("EXPORT_shemittah", "שְׁמִטָּה / שַׁבַּת הָאָרֶץ", "shemittah / shabbat ha-aretz", "Seventh-year land rest"),
       ("EXPORT_yovel", "יוֹבֵל", "yovel", "Jubilee year fifty")],
      [("IF year 7 in land", "THEN do not sow/prune; land rest; eat spontaneous with household and beasts"),
       ("IF year 50", "THEN liberty; return to holding; no sow")]),
    B("lev_25_redeem_poor", "25:23-38", 25, 23, 25, 38,
      "Land not sold forever; redeem; poor brother interest ban (25:23–38)",
      "הָאָרֶץ לֹא תִמָּכֵר לִצְמִתֻת", "ha-aretz lo timmakher li-tzemitut", "The land shall not be sold in perpetuity",
      ["lev_25_shemittah"], "decision_table", "primary",
      "Land Mine you sojourners; redeem land; house walled city one year redeem else forever until yovel; levite houses always redeem; poor strengthen; no interest increase; fear God.",
      [
        ("STEP_L25R_A1", "25:23-28", "LAND_REDEEM", "וְהָאָרֶץ לֹא תִמָּכֵר … גְּאֻלָּה", "ve-ha-aretz lo timmakher … ge'ullah",
         "Land not sold permanently for land is Mine you gerim residents with Me; all your holding grant redemption; if brother poor sells holding: goel near come redeem; if no goel but hand finds enough redeem self; compute years since sale refund balance return holding; if not able — in buyer hand until yovel go out return."),
        ("STEP_L25R_B1", "25:29-38", "HOUSE_POOR_INTEREST", "וְאִישׁ כִּי־יִמְכֹּר בֵּית־מוֹשַׁב עִיר חוֹמָה", "ve-ish ki-yimkor beit-moshav ir chomah",
         "House walled city: redeem year of sale full year; if not redeemed full year — forever buyer generations not out yovel; houses villages no wall as field redeem yovel; Levite cities houses perpetual redeem; field open pasture not sell; if brother poor support ger sojourner live; no interest or increase fear God; I YHWH brought Egypt give Canaan."),
      ],
      [("S_geullah_land", "Land and house redemption rules")],
      [("EXPORT_geullah", "גְּאֻלָּה", "ge'ullah", "Redemption of land/holding"),
       ("EXPORT_no_interest_brother", "אַל־תִּקַּח מֵאִתּוֹ נֶשֶׁךְ", "al-tikkach me-itto neshekh", "No interest from poor brother")],
      [("IF ancestral field sold", "THEN redeem by goel or self; else return at yovel"),
       ("IF lend to poor brother", "THEN no interest or increase")]),
    B("lev_25_slave_jubilee", "25:39-55", 25, 39, 25, 55,
      "Hebrew slave not as bondman; foreign slaves; redeem; yovel free (25:39–55)",
      "עֶבֶד עִבְרִי — בַּשְּׁנַת הַיּוֹבֵל", "eved ivri — ba-shenat ha-yovel", "Hebrew slave — in the jubilee year",
      ["lev_25_redeem_poor", "exo_21_slave_person"], "decision_table", "primary",
      "Poor brother sold: not slave work — as hireling until yovel free children; not rule rigor; foreign slaves permanent property; brother sold to ger: redeem calculation; not rule rigor; Israel servants to Me.",
      [
        ("STEP_L25J_A1", "25:39-46", "HEBREW_HIRELING", "וְכִי־יָמוּךְ … לֹא־תַעֲבֹד בּוֹ עֲבֹדַת עָבֶד", "ve-khi-yamukh … lo-ta'avod bo avodat aved",
         "If brother poor sold to you: not work him as slave; as hireling sojourner with you until yovel; then go out children return family holding; for they My servants out Egypt not sold as slave; not rule rigor fear God; your male female slaves from nations around — buy; permanent possession children inherit; brothers Israel not rule rigor."),
        ("STEP_L25J_B1", "25:47-55", "SOLD_TO_GER", "וְכִי תַשִּׂיג יַד גֵּר … וְנִגְאַל", "ve-khi tassig yad ger … ve-nig'al",
         "If ger resident gains and brother poor sells to ger or stock: after sold redemption; one of brothers or uncle or cousin or his hand redeems; compute years to yovel price by hireling years; if not redeemed go out yovel children; for Israel servants to Me I brought Egypt I YHWH."),
      ],
      [("S_yovel_freedom", "Jubilee slave freedom rules"), ("S_land_economy_closed", "Land economy block 25 closed")],
      [("EXPORT_ivri_not_rigor", "לֹא תִרְדֶּה בוֹ בְּפָרֶךְ", "lo tirdeh bo be-farekh", "Do not rule over Hebrew brother with rigor"),
       ("EXPORT_yovel_free", "יָצָא בַּיּוֹבֵל", "yatza ba-yovel", "Goes out free in the jubilee")],
      [("IF Hebrew sold to you from poverty", "THEN treat as hireling until yovel; not rigor"),
       ("IF not redeemed before yovel", "THEN goes out free in yovel")]),
    B("lev_26_bless_curse", "26:1-46", 26, 1, 26, 46,
      "If walk in chukkim: blessing; if refuse: cascading curse; remember berit (26:1–46)",
      "אִם־בְּחֻקֹּתַי תֵּלֵכוּ — וְאִם־לֹא", "im-be-chukkotai telekhu — ve-im-lo", "If in My statutes you walk — and if not",
      ["lev_25_slave_jubilee"], "narrative_fsm", "medium",
      "No idols; keep Shabbat revere mikdash; IF walk: rains peace sword remove; IF refuse: terror fever enemies; sevenfold cascade siege exile land rest; then confess remember Jacob Isaac Abraham land; not reject utterly; these chukkim on Sinai.",
      [
        ("STEP_L26_A1", "26:1-13", "BLESSING", "אִם־בְּחֻקֹּתַי תֵּלֵכוּ … וּנְתַתִּי גִשְׁמֵיכֶם", "im-be-chukkotai telekhu … u-netatti gishmeikhem",
         "No idols pillars images; keep Shabbat revere mikdash; IF walk chukkim mitzvot: rains in season earth yield peace lie down no terror; chase enemies; five chase hundred; turn to you fruitful multiply berit; eat old long; mishkan among you My soul not abhor; walk among you God you people; I broke yoke bars made you upright."),
        ("STEP_L26_B1", "26:14-39", "CURSE_CASCADE", "וְאִם־לֹא תִשְׁמְעוּ … וְהָלַכְתִּי עִמָּכֶם בַּחֲמַת־קֶרִי", "ve-im-lo tishme'u … ve-halakhti immakhem ba-chamat-keri",
         "If not listen and do: panic consumption fever sow empty; struck before enemies; if still not — sevenfold for sins; break staff bread; if walk contrary — sevenfold plague beasts sword pestilence; siege eat children's flesh high places ashes cities waste; land desolate enemies stunned; scatter nations; land enjoy shabbats; remaining faint heart exile."),
        ("STEP_L26_C1", "26:40-46", "REMEMBER_BERIT", "וְהִתְוַדּוּ … וְזָכַרְתִּי אֶת־בְּרִיתִי", "ve-hitvaddu … ve-zakharti et-beriti",
         "If confess iniquity and walk contrary heart humbled accept punishment; I remember berit Jacob Isaac Abraham and land; land abandoned by them enjoy shabbats; even then when in enemy land not reject destroy break berit I am YHWH; remember first berit Egypt nations to be God; these chukkim mishpatim torot YHWH Israel Sinai Moses."),
      ],
      [("S_blessing_branch", "Obedience blessing branch"), ("S_curse_branch", "Refusal curse cascade"), ("S_berit_memory", "Covenant memory after exile")],
      [("EXPORT_im_bechukkotai", "אִם־בְּחֻקֹּתַי", "im-be-chukkotai", "If you walk in My statutes — blessing gate"),
       ("EXPORT_sevenfold", "שֶׁבַע", "sheva", "Sevenfold intensification in curse cascade"),
       ("EXPORT_remember_berit_lev", "וְזָכַרְתִּי אֶת־בְּרִיתִי", "ve-zakharti et-beriti", "I will remember My covenant")]),
    B("lev_27_vows_valuations", "27:1-34", 27, 1, 27, 34,
      "Vow valuations by age/sex; animal field herem tithe (27:1–34)",
      "עֶרְכְּךָ — חֵרֶם — מַעֲשֵׂר", "erkekha — cherem — ma'aser", "Your valuation — devoted ban — tithe",
      ["lev_26_bless_curse"], "decision_table", "primary",
      "When vows persons valuation shekel ages male female; animal exchange holy; house field valuation yovel; firstborn not vow; cherem most holy not sell redeem; tithe herd tenth rod holy; these mitzvot Sinai.",
      [
        ("STEP_L27_A1", "27:1-13", "PERSON_ANIMAL", "אִישׁ כִּי יַפְלִא נֶדֶר … בְּעֶרְכְּךָ", "ish ki yafli neder … be-erkekha",
         "When man makes difficult vow of persons by your valuation: male 20–60 fifty shekels; female thirty; ages 5–20 / 1mo–5 / 60+ graded; if poor priest values; animal that may offer — holy no exchange; if exchange both holy; impure animal priest values; if redeem add fifth."),
        ("STEP_L27_B1", "27:14-27", "HOUSE_FIELD_FIRSTBORN", "וְאִישׁ כִּי־יַקְדִּישׁ … שָׂדֵהוּ", "ve-ish ki-yakdish … sadehu",
         "Dedicate house: priest values; redeem add fifth; field family holding: valuation by seed homer barley fifty shekels per yovel cycle years; if dedicate after yovel compute; redeem add fifth; if not redeem or sold — at yovel holy to priest holding; bought field at yovel returns original; shekel twenty gerah; firstborn animal already YHWH not dedicate; impure firstborn redeem add fifth else sell valuation."),
        ("STEP_L27_C1", "27:28-34", "CHEREM_TITHE", "אַךְ־כָּל־חֵרֶם … כָּל־מַעְשַׂר", "akh-kol-cherem … kol-ma'asar",
         "But anything cherem man bans for YHWH from man animal field — not sell not redeem most holy; any banned of men not redeemed death; all tithe land seed fruit YHWH holy; if redeem tithe add fifth; tithe herd flock all under rod tenth holy; not search good bad not exchange; if exchange both holy not redeem; these mitzvot YHWH commanded Moses to Israel Mount Sinai."),
      ],
      [("S_vow_registry", "Vow valuation registry"), ("S_lev_book_closed", "Leviticus 50-block draft complete")],
      [("EXPORT_erekh", "עֶרְכְּךָ", "erkekha", "Valuation scale for vowed persons"),
       ("EXPORT_cherem", "חֵרֶם", "cherem", "Devoted ban — most holy irrevocable"),
       ("EXPORT_maaser", "מַעֲשֵׂר", "ma'aser", "Tithe holy to YHWH"),
       ("EXPORT_lev_complete", None, None, "Leviticus thorough-block draft map complete")],
      [("IF vow person by valuation", "THEN pay age/sex shekel scale (or priest if poor)"),
       ("IF cherem to YHWH", "THEN not sell not redeem"),
       ("IF tithe herd under rod", "THEN every tenth holy")]),
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
    return block["steps"][0][0]


def role_for_plain(he_plain: str) -> tuple[str, str]:
    p = he_plain.replace("/", "").replace("־", "")
    if p in ("את", "אל", "על", "מן", "עם", "או", "אם", "כי", "גם", "אשר", "לא", "כל", "זה", "זו", "זאת", "בן", "בין"):
        return "glue", "glue"
    people = ("משה", "אהרן", "ישראל", "פרעה", "אלעזר", "איתמר", "נדב", "אביהוא")
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


_SIFRA_CACHE: Optional[dict] = None


def sifra_samples(ch_start: int, max_paras: int = 6) -> list[dict]:
    global _SIFRA_CACHE
    if not SIFRA_HE.exists():
        return []
    if _SIFRA_CACHE is None:
        with open(SIFRA_HE, encoding="utf-8") as f:
            _SIFRA_CACHE = json.load(f)
    text = _SIFRA_CACHE.get("text") or {}
    keys = SIFRA_BY_CH.get(ch_start) or list(text.keys())[:1]
    out: list[dict] = []

    def walk(o, section: str):
        if len(out) >= max_paras:
            return
        if isinstance(o, str) and o.strip():
            out.append({"section": section, "he": o.strip()[:280]})
            return
        if isinstance(o, list):
            for x in o:
                walk(x, section)
                if len(out) >= max_paras:
                    return
        elif isinstance(o, dict):
            for v in o.values():
                walk(v, section)
                if len(out) >= max_paras:
                    return

    for k in keys:
        if k in text:
            walk(text[k], k)
        if len(out) >= max_paras:
            break
    return out


def emit_block(block: dict) -> Path:
    bid = block["id"]
    verses = verse_list(block["ch_start"], block["v_start"], block["ch_end"], block["v_end"])
    step_ids = [s[0] for s in block["steps"]]
    sifra = block.get("sifra", "primary")
    lines: list[str] = []
    lines.append("# =============================================================================")
    lines.append(f"# LOGIC UNIT: Leviticus {block['refs']} — {block['title_en']}")
    lines.append(f"# Leviticus 50-block schedule (Sifra {sifra})")
    lines.append("# =============================================================================")
    lines.append("# Experimental model — not binding religious law.")
    lines.append("")
    lines.append("meta:")
    lines.append(f'  id: "{bid}"')
    lines.append(f'  title_en: {yaml_quote(block["title_en"])}')
    lines.append(f'  title_he: {yaml_quote(block["title_he"])}')
    lines.append(f'  title_he_translit: {yaml_quote(block["title_he_translit"])}')
    lines.append(f'  title_he_en: {yaml_quote(block["title_he_en"])}')
    lines.append('  book_he: "וַיִּקְרָא"')
    lines.append('  book_he_translit: "Vayikra"')
    lines.append('  book_en: "Leviticus"')
    lines.append(f'  refs: "{block["refs"]}"')
    lines.append("  data_paths_he:")
    lines.append('    - "Data/Lev.xml"')
    lines.append('  status: draft')
    lines.append("  confidence_overall: hypothesis")
    lines.append(f'  genre: "{block["genre"]}"')
    lines.append('  build_track: leviticus_apps')
    lines.append("  depends_on:")
    for d in block["depends_on"]:
        lines.append(f'    - "{d}"')
    lines.append("  owner_language_note: >")
    lines.append("    English for reading only. Hebrew is the derivation source.")
    lines.append("  oral_policy_note_en: >")
    lines.append("    Written first. Prefer Sifra dual-track on law; MH endpoints possible Oral;")
    lines.append("    never silent-merge. Exodus free names import stage, not rebuilt here.")
    lines.append(f"  imports_note_en: {yaml_quote(block.get('imports_en', ''))}")
    lines.append("")
    lines.append("derivation_log:")
    lines.append("  - step: A")
    lines.append('    name_en: "Block choice"')
    lines.append("    comment: >")
    lines.append(f"      Thorough Lev block {block['refs']} ({len(verses)} verses). {block['learn']}")
    lines.append("    confidence: established")
    lines.append("  - step: B")
    lines.append('    name_en: "Trees"')
    lines.append("    comment: >")
    lines.append(f"      All verses Lev.{block['refs']} via taamim_tree_parse.py v1; full tree_ascii.")
    lines.append("    confidence: tested")
    lines.append('    tags: ["[HE-STRUCT]"]')
    lines.append("  - step: C")
    lines.append('    name_en: "Learnings"')
    lines.append("    comment: >")
    for chunk in re.findall(r".{1,100}(?:\s|$)", block["learn"]):
        lines.append(f"      {chunk.rstrip()}")
    lines.append("    confidence: tested")
    lines.append("  - step: D")
    lines.append('    name_en: "Sifra dual-track"')
    lines.append("    comment: >")
    lines.append("      Sampled Sifra from local Data/sifra_he.json for related parasha section;")
    lines.append("      dual-track only; not merged into Written rules.")
    lines.append("    confidence: hypothesis")
    lines.append('    tags: ["[ORAL]"]')
    lines.append("")
    lines.append("boot_steps:")
    for i, (sid, ref, op, he, tr, en) in enumerate(block["steps"], 1):
        lines.append(f"  - id: {sid}")
        lines.append(f"    order: {i}")
        lines.append(f'    ref: "Lev.{ref}"')
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
        lines.append("    Hypothesis IF/THEN from Written Hebrew; not binding law. Refine with Sifra dual-track.")
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
    lines.append(f'    work_en: "Block oral policy (Sifra {sifra})"')
    lines.append("    comment_en: >")
    lines.append("      Prefer Sifra first among Oral for Lev law decode; then MH + Bavli.")
    lines.append("      Dual-track only. MH never ruled out.")
    lines.append('    source: "[PROJECT]"')
    if sifra in ("primary", "strong", "medium"):
        samples = sifra_samples(block["ch_start"], max_paras=6 if sifra == "primary" else 3)
        for i, s in enumerate(samples, 1):
            lines.append(f"  - id: ORAL_sifra_{i}")
            lines.append("    status: dual_track")
            lines.append('    work_en: "Sifra"')
            lines.append(f'    locus_en: {yaml_quote("Sifra section: " + s["section"])}')
            lines.append(f"    he_sample: {yaml_quote(s['he'][:240])}")
            lines.append('    he_translit: "see Hebrew sample; full midrash in Data/sifra_he.json"')
            lines.append('    en_sample: "[EN-AID] Hebrew Sifra sample only in local dump; gloss not derivation source."')
            lines.append("    comment_en: >")
            lines.append("      Dual-track sample — does not rewrite Written boot_steps/decision rows.")
            lines.append('    source: "[ORAL][SIFRA]"')
            lines.append("    confidence: hypothesis")
    else:
        lines.append("  - id: ORAL_possible")
        lines.append("    status: possible_oral")
        lines.append('    work_en: "Midrash / Bavli / MH (named when quoted)"')
        lines.append("    comment_en: Dual-track only.")
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
    lines.append("    taamim_tree_parse.py v1 on Data/Lev.xml.")
    lines.append('  data_source: "Data/Lev.xml"')
    lines.append('  parser: "taamim_tree_parse.py"')
    lines.append('  rule_set_version: "v1"')
    lines.append('  tags: ["[HE-STRUCT]"]')
    lines.append("  verse_trees:")
    coverage_blocks: list[str] = []
    word_total = 0
    for ch, v in verses:
        osis = f"Lev.{ch}.{v}"
        try:
            parsed = parse_verse(osis)
        except Exception as e:
            lines.append(f"    Lev_{ch}_{v}:")
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
        lines.append(f"    Lev_{ch}_{v}:")
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
    lines.append("  Draft thorough-block unit for Leviticus apps track. Not binding religious law.")
    lines.append("  Trees tested via taamim_tree_parse v1; logic hypothesis/tested per comments.")
    out_path = UNITS / f"{bid}.yaml"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--from-id")
    ap.add_argument("--force", action="store_true", help="Also rewrite hand-done 01–02")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    print(f"BLOCKS defined: {len(ALL_BLOCKS)}", flush=True)
    if args.list:
        for b in ALL_BLOCKS:
            print(b["id"], b["refs"], b.get("sifra"))
        return
    started = args.from_id is None
    n = 0
    for b in ALL_BLOCKS:
        if args.only and b["id"] != args.only:
            continue
        if args.from_id and not started:
            if b["id"] == args.from_id:
                started = True
            else:
                continue
        if b["id"] in SKIP_IDS and not args.force and not args.only:
            print(f"SKIP (hand-done): {b['id']}", flush=True)
            continue
        print(f"NEXT: {b['id']} ({b['refs']}) sifra={b.get('sifra')} …", flush=True)
        path = emit_block(b)
        print(f"  wrote {path.relative_to(ROOT)}", flush=True)
        n += 1
        if args.only:
            break
    print(f"DONE schedule pass. wrote {n} units.", flush=True)


if __name__ == "__main__":
    main()
