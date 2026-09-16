import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 2b (2026-09-16): the register seat Deut 4:5 NONE -> ACT, declared from the tape (the gate's class predicted from its code and
# read at the first tape run): the exhortation's write (adding_barred on Israel, source Deut 4:1-8) contains the verse — the receipt in Moses' own
# voice is the teaching's run (R5). The entry rewritten in place (a registry is rewritable with the gates green); the yaml parsed before it is trusted.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/register_dispositions.yaml'
s = open(P, encoding='utf-8').read()
old = "  Deut 4:5:\n    class: NONE\n    why: Deuteronomy is not on the tape (the book not read) — the seat waits for its reading and compile\n"
assert s.count(old) == 1, s.count(old)
new = ("  Deut 4:5:\n    class: ACT\n    why: 'THE DEUTERONOMY WALK 2b (2026-09-16) | \"behold, I have taught you statutes and judgments AS THE LORD MY GOD COMMANDED ME\" — THE RECEIPT IN MOSES'' OWN VOICE (10:5 the pair): the teaching''s run of Exodus 24:12''s \"the torah and the commandment which I have written to teach them\" (4:14 \"the LORD commanded me at that time to teach you\"; the erection''s ascent cell by CALL); the exhortation''s line (Deut 4:1-8 — add_nothing_commanded, adding_barred on israel_people at (40, 11, 1), the chapter''s one law) carries the verse inside its source: the ACT class, predicted from the gate''s code at the design and read at the first tape run; no debit paid — a run citation of a command with no ledger entry of its own (Bekhorot 29a:7-8 the receipt''s own reading: as I learned for free, you learned for free)'\n")
s = s.replace(old, new)
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert d['receipts']['Deut 4:5']['class'] == 'ACT' and 'THE DEUTERONOMY WALK 2b' in d['receipts']['Deut 4:5']['why']
print('declared Deut 4:5 ACT; the yaml parses')
