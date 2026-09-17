import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 3b (2026-09-16): the pointers the dependency gate demanded after the runner existed (dependency_gate_ch5_2.out — the three
# AS_WHEN receipts and nothing else: the token census found no uncited edge past the eleven CALL imports) — Deut 5:12, 5:16, 5:32 RUN_CITATION with
# (L3)'s why: the receipt inside the code cites its first giving (the tape's ten_words_declared), the teacher reading it as Marah; no ledger write
# pays it. Inserted after 2b's pointer rows; the yaml parsed before it is trusted. Idempotent.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
if 'runner: covenant_at_horeb, disposition: RUN_CITATION' not in s:
    a = '  - {verse: "Deut 4:33", form: AS_WHEN, runner: obey_horeb, disposition: RUN_CITATION'
    i = s.index(a); j = s.index('\n', i) + 1
    W = 'THE DEUTERONOMY WALK 3b (2026-09-16) | '
    rows = ('  - {verse: "Deut 5:12", form: AS_WHEN, runner: covenant_at_horeb, disposition: RUN_CITATION, link: reference, why: "' + W + "'keep the sabbath day to sanctify it, AS THE LORD YOUR GOD COMMANDED YOU' (כַּאֲשֶׁר צִוְּךָ יְהוָה אֱלֹהֶיךָ) — THE RECEIPT INSIDE THE CODE: the fourth word's second copy citing its first giving — a run citation of the tape's ten_words_declared (Exodus 20:8 the first telling; 2b's supplied line at Deut 4:10-13, dated (1, 3, 7)); the teacher's referent MARAH (Rav Yehuda — Sanhedrin 56b:16, Shabbat 87b:1: the exodus story's marah cell 'statute_list' CALLED by the runner's cell the_first_tablet); keep and remember in one utterance (Shevuot 20b:9) the row's reading; the second copy is NO line (the laws' readback, R1) — no ledger write pays a receipt (R5); the register seat Deut 5:12 declared CHAPTER (the chapter holds the closed charge to teach)\"}\n"
            '  - {verse: "Deut 5:16", form: AS_WHEN, runner: covenant_at_horeb, disposition: RUN_CITATION, link: reference, why: "' + W + "'honor your father and your mother, AS THE LORD YOUR GOD COMMANDED YOU' (כַּאֲשֶׁר צִוְּךָ יְהוָה אֱלֹהֶיךָ) — THE RECEIPT INSIDE THE CODE: the fifth word's second copy citing its first giving — a run citation of the tape's ten_words_declared (Exodus 20:12 the first telling); the teacher's referent MARAH (Sanhedrin 56b:16 — honoring parents among Marah's statutes); the fifth word compiled at its kin's seat Leviticus 19:3 (the holiness runner's frame cell CALLED by the_second_tablet); 'and that it may go well with you' the expansion's own Talmud row (Bava Kamma 55a:1); no ledger write pays a receipt (R5); the register seat Deut 5:16 declared CHAPTER\"}\n"
            '  - {verse: "Deut 5:32", form: AS_WHEN, runner: covenant_at_horeb, disposition: RUN_CITATION, link: reference, why: "' + W + "'you shall observe to do AS THE LORD YOUR GOD COMMANDED YOU; you shall not turn aside right or left' (כַּאֲשֶׁר צִוָּה יְהוָה אֱלֹהֵיכֶם אֶתְכֶם) — the plural receipt closing the chapter: the charge's citation of the giving as a whole — a run citation of the tape's ten_words_declared (Exodus 20:1-17) and the covenant's lines (Exodus 19:5-8, 24:3-8 — the erection's blood_covenant cell CALLED by the_assembly_called); the charge 5:32-33 writes nothing (the frame's close, R6), the forward marker at 5:32 ends the retrograde stretch of 5:23; no ledger write pays a receipt (R5); the register seat Deut 5:32 declared CHAPTER\"}\n")
    s = s[:j] + rows + s[j:]
    open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
mine = [p for p in d['pointers'] if p.get('runner') == 'covenant_at_horeb']
assert [(p['verse'], p['form'], p['disposition']) for p in mine] == [('Deut 5:12', 'AS_WHEN', 'RUN_CITATION'), ('Deut 5:16', 'AS_WHEN', 'RUN_CITATION'), ('Deut 5:32', 'AS_WHEN', 'RUN_CITATION')], mine
print('pointers: %d for covenant_at_horeb (the three receipts RUN_CITATION); the yaml parses; pointers on file %d' % (len(mine), len(d['pointers'])))
