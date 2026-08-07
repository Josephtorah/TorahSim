# -*- coding: utf-8 -*-
"""Shared transliteration-cleanup dictionary for the solo-era builder.

DB translit uses morpheme hyphens and a literal ה for suffix/paragogic he;
unit pages use polished forms. GLOBAL entries must be UNAMBIGUOUS across
the whole corpus — one DB form, one polished form, always. Anything
context-dependent (e.g. "et-y" = oti at Gen 30:20 but iti at 30:29) goes
in the content module's EXTRA_SUBS instead. Append-only: never repurpose
an existing key.
"""

GLOBAL_SUBS = {
    # names
    "lea": "leah", "vilha": "vilhah", "bilha": "bilhah", "zilpa": "zilpah",
    # suffixed-he (3fs possessive / directional / paragogic)
    "rachma-ה": "rachmah", "ba-achota-ה": "ba-achotah", "hava-ה": "hava",
    "shifchata-ה": "shifchatah", "et-ה": "otah", "la-ה": "lah",
    "ima-ה": "imah", "shema-ה": "shemah", "tena-ה": "tena",
    "naqva-ה": "naqva", "artza-ה": "artzah",
    # 1cs suffixes written -y
    "li-y": "li", "ishi-y": "ishi", "beni-y": "beni", "achoti-y": "achoti",
    "be-anyi-y": "be-onyi", "birka-y": "birkay", "el-y": "elay",
    "be-qoli-y": "be-qoli", "shifchati-y": "shifchati",
    "sekhari-y": "sekhari", "le-ishi-y": "le-ishi", "cherpati-y": "cherpati",
    "amati-y": "amati", "kochi-y": "kochi", "avi-y": "avi",
    "imadi-y": "imadi", "maskurti-y": "maskurti", "tzidqati-y": "tzidqati",
    "avodati-y": "avodati", "meqomi-y": "meqomi", "u-le-artzi-y": "u-le-artzi",
    "le-fana-y": "le-fanay", "le-ragli-y": "le-ragli", "le-veti-y": "le-veti",
    "ena-y": "enay", "bi-y": "bi", "nasha-y": "nashai", "yelada-y": "yeladai",
    "ala-y": "alay", "hineni-y": "hineni",
    # object/person suffixes
    "yeehava-ni": "yeehavani", "dana-ni": "danani", "zevada-ni": "zevadani",
    "yizble-ni": "yizbeleni", "ishru-ni": "ishruni", "be-ashri-y": "be-oshri",
    "et-m": "otam", "li-qerat-o": "liqrato", "la-khen": "lakhen",
    "shem-o": "shemo", "l-o": "lo", "ima-khe": "imakh",
    "bene-khe": "benekh", "vene-khe": "venekh", "sekharti-kha": "sekharticha",
    "qachte-khe": "qachtekh", "ele-ha": "eleha", "mime-khe": "mimekh",
    "mime-na": "mimena", "elay-v": "elav", "la-khe": "lakh",
    "et-kha": "otkha", "le-fane-kha": "le-fanekha", "sekhar-kha": "sekharkha",
    "miqn-kha": "miqnekha", "tzon-kha": "tzonkha", "be-ene-kha": "be-enekha",
    "bi-gelale-kha": "biglalekha", "va-yevarakhe-ni": "va-yevarakheni",
    "shalche-ni": "shalcheni", "khi-devare-kha": "khi-devarekha",
    "ene-nu": "enenu", "banay-v": "banav", "ben-o": "beno", "b-o": "bo",
    "le-kha": "lekha", "be-voa-n": "be-voan", "shata-m": "shatam",
    "le-vad-o": "levado", "raglay-v": "raglav", "le-avi-nu": "le-avinu",
    "im-o": "imo", "avote-kha": "avotekha",
    "u-le-moladte-kha": "u-le-moladtekha", "avi-khen": "avikhen",
    "va-avi-khen": "va-avikhen", "netan-o": "netano", "avi-khem": "avikhem",
    "ene-kha": "enekha", "moladte-kha": "moladtekha", "avi-nu": "avinu",
    "mekhara-nu": "mekharanu", "kaspe-nu": "kaspenu", "me-avi-nu": "me-avinu",
    "la-nu": "lanu", "u-le-vane-nu": "u-le-vanenu", "ele-kha": "elekha",
    "nashay-v": "nashav", "miqne-hu": "miqnehu", "rekhush-o": "rekhusho",
    "qinyan-o": "qinyano", "avi-v": "aviv", "le-avi-ha": "le-aviha",
    "panay-v": "panav", "la-hen": "lahen",
    "avadti-kha": "avadticha", "sekhare-kha": "sekharekha",
    "tzon-o": "tzono",
}
# NOTE (2026-08-07, filed with the maqqef observation): frozen gen_51
# keeps "im-o" raw and frozen gen_52 keeps "bi-y" raw where later units
# polish them (imo / bi). Their content modules pin the historical forms
# via identity EXTRA_SUBS so rebuilds stay byte-exact; new units get the
# polished global forms. Harmonizing the two frozen files = owner-gated
# amendment, not done.
