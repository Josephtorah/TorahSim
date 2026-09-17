import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 3b (2026-09-16): the register seats Deut 5:12, 5:16, 5:32 NONE -> CHAPTER, declared from the design (the gate's class predicted
# from its code — no write's source contains the verses, the second copy being no line (R1); the chapter holds a closed entry, the charge to teach
# closed inside the daemon by the prior run) and read at the fast checkpoint check: THE RECEIPT INSIDE THE CODE is a RUN CITATION of the code's first
# giving (the tape's ten_words_declared — Exodus 20:8, 20:12, 20:1-17 the first tellings), no ledger write pays it (R5); the teacher reads the receipt
# as Marah (Sanhedrin 56b:16; Shabbat 87b:1). The entries rewritten in place (a registry is rewritable with the gates green); the yaml parsed before it
# is trusted. declare_ch4_seat.py's form.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/register_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 3b (2026-09-16) | '
NEW = {
    'Deut 5:12': W + '"KEEP the sabbath day to sanctify it, AS THE LORD YOUR GOD COMMANDED YOU" — THE RECEIPT INSIDE THE CODE (5:16 and 20:17 its other seats): the fourth word\'s second copy citing its first giving — a RUN CITATION of the tape\'s ten_words_declared (Exodus 20:8 the first telling, the line at Deut 4:10-13 dated (1, 3, 7)); the teacher\'s referent MARAH (Rav Yehuda, Sanhedrin 56b:16; Shabbat 87b:1 — the exodus story\'s marah cell by CALL); the second copy is NO line on the tape (a retelling is a reference row, never a second act — the laws\' readback, R1), so no write\'s source contains the verse; the chapter holds a closed entry (the charge to teach, commanded on Moses at Deut 5:28-31, closed inside the daemon by the prior run Deut 1:1-5): the CHAPTER class, predicted from the gate\'s code at the design and read at the fast checkpoint check; no debit paid — keep and remember in one utterance (Shevuot 20b:9; Rosh Hashanah 27a:2) the row\'s own reading',
    'Deut 5:16': W + '"honor your father and your mother, AS THE LORD YOUR GOD COMMANDED YOU" — THE RECEIPT INSIDE THE CODE (5:12 the pair): the fifth word\'s second copy citing its first giving — a RUN CITATION of the tape\'s ten_words_declared (Exodus 20:12 the first telling); the teacher\'s referent MARAH (Sanhedrin 56b:16 — honoring father and mother among Marah\'s statutes); the fifth word compiled at its kin\'s seat, Leviticus 19:3 (the holiness runner\'s frame cell by CALL — Kiddushin 30b-31b); no write\'s source contains the verse, the chapter holds the closed charge: the CHAPTER class, predicted from the gate\'s code at the design and read at the fast checkpoint check; no debit paid — the expansion "and that it may go well with you" the row\'s own Talmud seat (Bava Kamma 55a:1)',
    'Deut 5:32': W + '"you shall observe to do AS THE LORD YOUR GOD COMMANDED YOU; you shall not turn aside right or left" — the plural receipt closing the chapter (the singular pair at 5:12, 5:16 inside the code): the CHARGE\'s citation of the giving as a whole — a RUN CITATION of the tape\'s ten_words_declared (Exodus 20:1-17 the first telling) and of the covenant\'s lines (Exodus 19:5-8, 24:3-8); the charge 5:32-33 writes nothing (the frame\'s close, R6) and the forward marker at 5:32 ends the retrograde stretch of 5:23; no write\'s source contains the verse, the chapter holds the closed charge (5:28-31): the CHAPTER class, predicted from the gate\'s code at the design and read at the fast checkpoint check; no debit paid',
}
for k, why in NEW.items():
    old = "  %s:\n    class: NONE\n    why: Deuteronomy is not on the tape (the book not read) — the seat waits for its reading and compile\n" % k
    assert s.count(old) == 1, (k, s.count(old))
    s = s.replace(old, "  %s:\n    class: CHAPTER\n    why: '%s'\n" % (k, why.replace("'", "''")))
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert all(d['receipts'][k]['class'] == 'CHAPTER' and 'THE DEUTERONOMY WALK 3b' in d['receipts'][k]['why'] for k in NEW)
print('declared Deut 5:12, 5:16, 5:32 CHAPTER; the yaml parses')
