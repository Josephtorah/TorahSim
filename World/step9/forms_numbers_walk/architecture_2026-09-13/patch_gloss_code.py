#!/usr/bin/env python3
# THE PROJECT REVIEW, finding 13's code side (2026-09-13; the owner: "Yes don't skip"): the ninety-character window of the gloss lint
# stops at a PERIOD (GLOSS_NEAR = ^[^.]{0,90}?(marker)), so a "..." inside a Hebrew quotation strands every word before it. Each long
# quotation is cut into short glossed pieces with the ellipsis character; four English notes get their marker; the circumcision regex
# is built from a list whose every form carries its gloss in a comment. Every replacement asserted once; the regex asserted equal.
import re
R = '<repo-old>/'
def patch(path, pairs):
    t = open(R + path, encoding='utf-8').read()
    for old, new in pairs:
        n = t.count(old); assert n == 1, (path, n, old[:60]); t = t.replace(old, new)
    open(R + path, 'w', encoding='utf-8').write(t); print('patched', path, len(pairs))
patch('World/step9/cold_run_temurah.py', [
 ("'ואם כל בהמה טמאה אשר לא יקריבו ממנה קרבן... והעמיד... והעריך '",
  "'ואם כל בהמה טמאה (and if any impure beast) אשר לא יקריבו ממנה קרבן (of which no offering is brought) … והעמיד (he shall stand it) … והעריך '"),
 ("'ואיש כי יקדש את ביתו... והעריכו הכהן (a man sanctifies his house — the '",
  "'ואיש כי יקדש את ביתו (a man sanctifies his house) … והעריכו הכהן (and the '"),
 ("'אך בכור... לא יקדיש איש אתו... ליהוה הוא (a firstborn '",
  "'אך בכור (but a firstborn) … לא יקדיש איש אתו (no man shall sanctify it) … ליהוה הוא (a firstborn '"),
 ("'לא יחליפנו ולא ימיר אתו... ואם המר ימיר בהמה בבהמה והיה הוא ותמורתו יהיה קדש '",
  "'לא יחליפנו ולא ימיר אתו (he shall not exchange it nor substitute it) … ואם המר ימיר בהמה בבהמה (and if he does substitute beast for beast) והיה הוא ותמורתו יהיה קדש '"),
 ("'וכל מעשר הארץ... ליהוה הוא קדש ליהוה (all the tithe of the land... it is '",
  "'וכל מעשר הארץ (all the tithe of the land) … ליהוה הוא קדש ליהוה (all the tithe of the land... it is '"),
])
patch('World/step9/cold_run_moadim.py', [
 ("'והניף הכהן אתם על לחם הבכורים תנופה... על שני כבשים (the priest shall wave them on the bread of '",
  "'והניף הכהן אתם (the priest shall wave them) על לחם הבכורים תנופה (on the bread of the first fruits, a wave offering) … על שני כבשים (on the two lambs — the priest shall wave them on the bread of '"),
])
patch('World/step9/cold_run_minchah.py', [
 ("'כל המנחה... לא תעשה חמץ (ALL the meal offering... shall not be made '",
  "'כל המנחה (all the meal offering) … לא תעשה חמץ (ALL the meal offering... shall not be made '"),
 ("'והבאת את המנחה אשר יעשה מאלה... והגישה אל המזבח (the meal offering made OF '",
  "'והבאת את המנחה (you shall bring the meal offering) אשר יעשה מאלה (made of these) … והגישה אל המזבח (the meal offering made OF '"),
])
patch('World/step9/cold_run_yovel.py', [
 ("'אל תקח מאתו נשך ותרבית... וחי אחיך עמך (25:36) — your BROTHER'",
  "'אל תקח מאתו נשך ותרבית (take no interest or increase from him) … וחי אחיך עמך (25:36, that your brother may live with you) — your BROTHER'"),
])
patch('World/step9/cold_run_tzav.py', [
 ("'shall NOT BE ACCEPTED (לא ירצה)... REJECTED (פגול) shall '", "'shall NOT BE ACCEPTED (לא ירצה \"it shall not be accepted\")... REJECTED (פגול \"rejected\") shall '"),
 ("# law-midrash spine read the same sitting)", "# law-midrash (the rabbinic reading) spine read the same sitting)"),
])
patch('World/step9/cold_run_pesach_sheni.py', [("(the first tanna against R. Yehuda)", "(the first tanna, the anonymous Mishnah voice, against R. Yehuda)")])
patch('World/step9/cold_run_mekoshesh.py', [("the first tanna, who derives forewarning from the wood-gatherer", "the first tanna (the anonymous Mishnah voice), who derives forewarning from the wood-gatherer")])
patch('World/step9/daemon_census.py', [("why names a wrap-worklist line of COMPILE_DEBT.md", "why names a wrap worklist line of COMPILE_DEBT.md")])
OLD = "('circumcision', r'^ו?(המול|ימול|נמול|נמלו|וימל|ימל|מלתם|ומלתם|ומלתה|למול|מלה|נמלים|המלות|ערל|ערלה|ערלת|ערלתו|ערלתם|ערלים|ערלכם|הערל|וערל|וערלתם|לערל|ערלי)$', {'pre_sinai'}),"
NEW = """('circumcision', r'^ו?(' + '|'.join([
        'המול', 'ימול', 'נמול', 'נמלו', 'וימל', 'ימל',                    # 'circumcise' — the verb's forms
        'מלתם', 'ומלתם', 'ומלתה', 'למול', 'מלה', 'נמלים', 'המלות',        # 'circumcise' — with suffixes and prefixes
        'ערל', 'ערלה', 'ערלת', 'ערלתו', 'ערלתם', 'ערלים', 'ערלכם',        # 'foreskin', 'uncircumcised'
        'הערל', 'וערל', 'וערלתם', 'לערל', 'ערלי',                         # 'foreskin' — with prefixes
    ]) + ')$', {'pre_sinai'}),"""
old_re = re.search(r"r'(\^.*?\$)'", OLD).group(1)
new_re = '^ו?(' + '|'.join(['המול', 'ימול', 'נמול', 'נמלו', 'וימל', 'ימל', 'מלתם', 'ומלתם', 'ומלתה', 'למול', 'מלה', 'נמלים', 'המלות', 'ערל', 'ערלה', 'ערלת', 'ערלתו', 'ערלתם', 'ערלים', 'ערלכם', 'הערל', 'וערל', 'וערלתם', 'לערל', 'ערלי']) + ')$'
assert old_re == new_re, 'the regex must be identical'
patch('World/step9/dependency_census.py', [(OLD, NEW)])
patch('World/step9/dependency_dispositions.yaml', [
 ("token (שְׁלָמִים): a HOMOGRAPH", "token (שְׁלָמִים 'peace offerings'): a HOMOGRAPH"),
 ("1 Kings 8:65's נַחַל the same brook)", "1 Kings 8:65's נַחַל 'brook', the same brook)"),
 ("the token's shape (עברי) is the homograph", "the token's shape (עברי 'Hebrew') is the homograph"),
 ("HEBREW man' (עברי) — the people's name", "HEBREW man' (עברי 'Hebrew') — the people's name"),
 ("(עברי, עבד) — Joseph", "(עברי 'Hebrew', עבד 'slave') — Joseph"),
 ("(עלה — go up the mountain)", "(עלה 'go up' — the mountain)"),
 ("Num 32:33 סִיחֹן מֶלֶךְ הָאֱמֹרִי ... עוֹג מֶלֶךְ הַבָּשָׁן ('Sihon KING of the Amorite, Og KING of Bashan')",
  "Num 32:33 סִיחֹן מֶלֶךְ הָאֱמֹרִי ('Sihon KING of the Amorite') … עוֹג מֶלֶךְ הַבָּשָׁן ('Og KING of Bashan')"),
 ("(qamats under the resh against the sheva), FALSE", "(qamats under the resh against the sheva, the vowel point), FALSE"),
])
import yaml; yaml.safe_load(open(R + 'World/step9/dependency_dispositions.yaml', encoding='utf-8')); print('yaml parses')
