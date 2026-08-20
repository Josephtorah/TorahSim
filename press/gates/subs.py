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
    # gen_54 span (31:22-54), appended 2026-08-07 — all unambiguous
    "echay-v": "echav", "acharay-v": "acharav", "levavi-y": "levavi",
    "benota-y": "benotay", "adoni-y": "adoni", "chatati-y": "chatati",
    "pishi-y": "pishi", "anyi-y": "onyi", "kela-y": "kelay",
    "acha-y": "achay", "achara-y": "acharay", "kapa-y": "kapay",
    "yadi-y": "yadi", "mi-yadi-y": "mi-yadi", "tzoni-y": "tzoni",
    "bana-y": "banay", "shenati-y": "shenati", "eloha-y": "elohay",
    "me-imi-y": "me-imi", "me-ena-y": "me-enay", "le-vana-y": "le-vanay",
    "ve-li-venota-y": "ve-li-venotay", "ache-nu": "achenu",
    "shene-nu": "shenenu", "vene-nu": "venenu", "ima-nu": "imanu",
    "avi-kha": "avikha", "ve-ache-kha": "ve-achekha",
    "benote-kha": "benotekha", "venote-kha": "venotekha",
    "be-vete-kha": "be-vetekha", "vete-kha": "vetekha",
    "be-tzone-kha": "be-tzonekha", "rechele-kha": "rechelekha",
    "ve-ize-kha": "ve-izekha", "elohe-kha": "elohekha",
    "mi-pane-kha": "mi-panekha", "va-ashalecha-kha": "va-ashalechakha",
    "u-vene-kha": "u-venekha", "u-ven-kha": "u-venkha",
    "avi-hem": "avihem", "ale-hem": "alehem", "li-vene-hen": "li-venehen",
    "akhala-ni": "akhalani", "netashta-ni": "netashtani",
    "shilachta-ni": "shilachtani", "genavata-m": "genavatam",
    "va-tesime-m": "va-tesimem", "va-yerime-ha": "va-yerimeha",
    "avi-ha": "aviha", "achate-na": "achatena",
    "tevaqshe-na": "tevaqshena", "me-ree-hu": "me-reehu",
    "ima-khem": "imakhem",
    # gen_55 span (32:1-33), appended 2026-08-07 — all unambiguous
    "va-eshlcha-ה": "va-eshlecha", "hagida-ה": "hagida",
    "et-hem": "othem", "le-vanay-v": "le-vanav",
    "ve-li-venotay-v": "ve-li-venotav", "li-meqom-o": "li-meqomo",
    "le-dark-o": "le-darko", "raa-m": "raam", "tomru-n": "tomrun",
    "avd-kha": "avdekha", "li-qerat-kha": "liqratkha",
    "achi-kha": "achikha", "ve-hika-hu": "ve-hikahu",
    "ve-hika-ni": "ve-hikani", "avde-kha": "avdekha",
    "ve-maqli-y": "ve-maqli", "le-artz-kha": "le-artzekha",
    "u-le-moladt-kha": "u-le-moladtekha", "zara-kha": "zarakha",
    "ve-yad-o": "ve-yado", "avaday-v": "avadav",
    "yifgash-kha": "yifgashkha", "vi-sheel-kha": "vi-sheelkha",
    "le-avd-kha": "le-avdekha", "achare-nu": "acharenu",
    "fanay-v": "fanav", "fana-y": "fanay",
    "be-motzaa-khem": "be-motzaakhem", "u-vene-hem": "u-venehem",
    "shifchotay-v": "shifchotav", "yeladay-v": "yeladav",
    "va-yiqache-m": "va-yiqachem", "va-yaavire-m": "va-yaavirem",
    "yerekh-o": "yerekho", "be-heavq-o": "be-heavqo",
    "berakhta-ni": "berakhtani", "ashalecha-kha": "ashalechakha",
    "sheme-kha": "shemekha", "shim-kha": "shimkha",
    "li-shemi-y": "li-shemi", "nafshi-y": "nafshi",
    "tedabru-n": "tedabrun", "hatzile-ni": "hatzileni",
    # gen_56 span (33:1-20), appended 2026-08-07 — all unambiguous.
    # NOTE: "ahol-o" is NOT here — frozen gen_54 (31:25 et-ahol-o)
    # keeps the raw form; gen_56 polishes it via module EXTRA_SUBS.
    "sukota-ה": "sukotah", "seira-ה": "seirah",
    "yalde-hen": "yaldehen", "vi-ylade-ha": "vi-yladeha",
    "gisht-o": "gishto", "va-yechabqe-hu": "va-yechabqehu",
    "tzavara-v": "tzavarav", "va-yishaqe-hu": "va-yishaqehu",
    "chana-ni": "chanani", "va-tirtze-ni": "va-tirtzeni",
    "birkhati-y": "birkhati", "minchati-y": "minchati",
    "le-negde-kha": "le-negdekha", "u-defaqu-m": "u-defaqum",
    "le-iti-y": "le-iti", "avd-o": "avdo",
    "u-le-miqne-hu": "u-le-miqnehu", "be-vo-o": "be-voo",
    # gen_57 span (34:1-31), appended 2026-08-07 — all unambiguous.
    # NOTE: "li-fene-hem" and "ir-o" are NOT here — both appear raw inside
    # frozen gen_56 / gen_54 files (substring scan); gen_57 polishes them
    # via module EXTRA_SUBS, same class as the ahol-o carve-out above.
    # The et-* object/with pronouns ("him/them/us/you-plural/me") stay
    # module-local too: object-marker vs with-preposition is context-
    # dependent (oto/ito class — see header).
    "nafsh-o": "nafsho", "vit-o": "vito", "u-vanay-v": "u-vanav",
    "va-yeane-ha": "va-yeaneha", "be-vit-khem": "be-vitkhem",
    "benote-khem": "benotekhem", "benote-nu": "benotenu",
    "la-khem": "lakhem", "la-hem": "lahem", "li-fene-khem": "li-fenekhem",
    "u-secharu-ha": "u-secharuha", "ba-ה": "bah", "avi-ה": "aviha",
    "ache-ha": "acheha", "be-ene-khem": "be-enekhem",
    "achota-m": "achotam", "achote-nu": "achotenu",
    "khamo-nu": "khamonu", "ele-nu": "elenu", "bite-nu": "bitenu",
    "divre-hem": "divrehem", "ira-m": "iram", "benota-m": "benotam",
    "miqne-hem": "miqnehem", "ve-qinyana-m": "ve-qinyanam",
    "behemta-m": "behemtam", "bi-heota-m": "bi-heotam",
    "charb-o": "charbo", "tzona-m": "tzonam", "beqara-m": "beqaram",
    "chamore-hem": "chamorehem", "chela-m": "chelam", "tapa-m": "tapam",
    "neshe-hem": "neshehem", "le-havishe-ni": "le-havisheni",
    "ve-hiku-ni": "ve-hikuni", "u-veti-y": "u-veti",
    "boa-m": "boam", "ke-shama-m": "ke-shamam",
    # gen_58 span (35:1-29), appended 2026-08-07 — all unambiguous.
    # NOTE: "et-o" is NOT here and stays RAW in gen_58 — the span mixes
    # object-marker et-o (oto: 35:9,29) with with-preposition et-o
    # (ito: 35:13,14,15); one key cannot carry both (im-o/bi-y class).
    # "aholo-ה" (his-tent spelled with final he, 9:21/35:21) is distinct
    # from frozen gen_54's raw "ahol-o" (see NOTE above).
    "be-varcha-kha": "be-varchakha", "be-varch-o": "be-varcho",
    "be-tokh-khem": "be-tokhkhem", "tzarati-y": "tzarati",
    "be-yada-m": "be-yadam", "be-azne-hem": "be-aznehem",
    "sevivote-hem": "sevivotehem", "luza-ה": "luzah",
    "mime-ka": "mimeka", "me-chalatze-kha": "me-chalatzekha",
    "etne-na": "etnena", "u-le-zara-kha": "u-le-zarakha",
    "achare-kha": "acharekha", "me-alay-v": "me-alav",
    "ale-ha": "aleha", "be-lidta-ה": "be-lidtah",
    "ve-haqshota-ה": "ve-haqshotah", "nafsha-ה": "nafshah",
    "amay-v": "amav", "qevurata-ה": "qevuratah",
    "aholo-ה": "aholo", "bet-o": "beto",
    # gen_59 span (36:1-43), appended 2026-08-07 — all unambiguous.
    "benotay-v": "benotav", "behemt-o": "behemto",
    "rekhusha-m": "rekhusham", "megure-hem": "megurehem",
    "tachtay-v": "tachtav", "isht-o": "ishto",
    "alufe-hem": "alufehem", "le-mishpchota-m": "le-mishpchotam",
    "li-meqomota-m": "li-meqomotam", "bi-shemota-m": "bi-shemotam",
    "le-moshvota-m": "le-moshvotam", "achuzata-m": "achuzatam",
    "bi-reot-o": "bi-reoto",
    # lev_19 span (19:1-37), appended 2026-08-07 (probe wave block 1) —
    # all unambiguous, collision-scanned against solo frozen yamls
    # (zero raw hits). et-khem ("you-plural") deliberately ABSENT: mixed
    # lemma in-span
    # (854 itkhem 19:34 / 853 etkhem 19:36) — stays raw, gen_58 et-o
    # precedent. el-hem -> alehem shares its value with ale-hem (both
    # surface alehem; the he line keeps the letter distinction).
    # "ve-avi-v" is NOT here — frozen gen_58 (35:18) keeps the raw form
    # (the ahol-o carve-out class); lev_19 polishes via module EXTRA_SUBS.
    "le-haznota-ה": "le-haznotah",
    "alay-v": "alav", "ale-kha": "alekha", "ame-kha": "amekha",
    "amite-kha": "amitekha", "arlat-o": "arlato", "artz-khem": "artzkhem",
    "asham-o": "ashamo", "avon-o": "avono", "ba-amit-o": "ba-amito",
    "ba-khem": "bakhem", "be-ame-kha": "be-amekha",
    "be-artz-khem": "be-artzkhem", "behemt-kha": "behemtekha",
    "bi-levave-kha": "bi-levavekha", "bi-vesar-khem": "bi-vesarkhem",
    "bit-kha": "bitkha", "chatat-o": "chatato", "chuqota-y": "chuqotay",
    "el-hem": "alehem", "elohe-khem": "elohekhem",
    "kamo-kha": "kamokha", "karm-kha": "karmkha",
    "le-rea-kha": "le-reakha", "li-retzon-khem": "li-retzonkhem",
    "me-chatat-o": "me-chatato", "me-elohe-kha": "me-elohekha",
    "mishpata-y": "mishpatay", "piry-o": "piryo",
    "qetzir-kha": "qetzirkha", "rea-kha": "reakha", "ree-kha": "reekha",
    "rosh-khem": "roshkhem", "sad-kha": "sadkha",
    "shabtota-y": "shabtotay", "tevuat-o": "tevuato",
    "tizbachu-hu": "tizbachuhu", "u-miqdashi-y": "u-miqdashi",
    "u-ve-qutzr-khem": "u-ve-qutzrkhem", "va-hem": "vahem",
    "ve-kharm-kha": "ve-kharmkha",
    "ve-okhlay-v": "ve-okhlav", "vi-shemi-y": "vi-shemi",
    "zeqane-kha": "zeqanekha", "zivcha-khem": "zivchakhem",
    # lev_04 span (4:1-35), appended 2026-08-07 (probe wave block 2) —
    # all unambiguous, collision-scanned (zero raw hits in solo frozen).
    "ale-hen": "alehen", "ba-asota-ה": "ba-asotah",
    "be-etzba-o": "be-etzbao", "besar-o": "besaro", "chelb-o": "chelbo",
    "chelba-ה": "chelbah", "dam-o": "damo", "dama-ה": "damah",
    "elohay-v": "elohav", "etzba-o": "etzbao",
    "ha-mizbecha-ה": "ha-mizbechah", "keraay-v": "keraav",
    "mi-dama-ה": "mi-damah", "mime-nu": "mimenu", "qarban-o": "qarbano",
    "rosh-o": "rosho", "u-firsh-o": "u-firsho",
    "ve-hiqtira-m": "ve-hiqtiram", "ve-qirb-o": "ve-qirbo",
    "yad-o": "yado", "yede-hem": "yedehem", "yesire-na": "yesirena",
    "yevie-na": "yeviena",
}
# NOTE (2026-08-07, filed with the maqqef observation): frozen gen_51
# keeps "im-o" raw and frozen gen_52 keeps "bi-y" raw where later units
# polish them (imo / bi). Their content modules pin the historical forms
# via identity EXTRA_SUBS so rebuilds stay byte-exact; new units get the
# polished global forms. Harmonizing the two frozen files = owner-gated
# amendment, not done.
