import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 22 — CHAPTER 34's READING IN THE LEAN FORM (2026-09-30; the owner: "Reread and go" after the compaction that followed sitting 21b's tail —
# the tree UNCOMMITTED with 21 and 21b since 472d2a3, no commit word said; THE LEAN PASS's seventeenth sitting, its ninth reading, THE DEATH OF MOSES: the Sifrei's spine
# in force at 357 on 34:1 — the export's LAST piska; DEUTERONOMY'S LAST CHAPTER): ch34_dump0.py DERIVED from the forms' ch33_dump0.py by asserted substitutions (sitting 21's
# form derive_ch33_dump0.py, one chapter): the chapter number, the file names, the register and prior-read greps, the drafts by glob (deu_34_moses_death the one draft on
# file), the claim prefixes, the heads window kept (335-357 — the export's end; 356 on 33:27 before, 357 on 34:1, NOTHING after), the kin chapters (the commission Numbers
# 27:12-23; Aaron's death Numbers 20; the mountains of Abarim Numbers 33; Moses' plea 3:23-29; go up to Nebo 32:48-52; the hundred and twenty years and Joshua's charge 31;
# the land sworn Genesis 12, 13, 15; Jacob's and Joseph's deaths and the mourning Genesis 50; face to face Exodus 33:11 and mouth to mouth Numbers 12; the prophet like
# Moses 18:15; Joshua the minister Exodus 24:13 and Numbers 11:28; the signs and wonders Exodus 4-7 and 4:34, 7:19, 29:2; the man of God 33:1 and the lawgiver's portion
# 33:21); THE HEADS-AFTER PRINT GUARDED (no piska after 357 — the export ends); THE SPINE GUARDED as before. THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — chapter 34
# the unit, CHAPTER NUMBERS, the book's last. RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch33_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "import subprocess; ROOT = _ROOT"
PROPHETS = "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"
CH = 34
ORD = "a twenty-sixth time — THE DEATH OF MOSES: 357 on 34:1, the last piska of the export, nothing after it"   # no apostrophe inside the single-quoted print
KIN = ("print('  ledgers with an Onkelos Gen 12 / Gen 13 / Gen 15 / Gen 50 / Exod 4 / Exod 7 / Exod 24 / Exod 33 / Num 11 / Num 12 / Num 20 / Num 27 / Num 33 / Deut 1 / Deut 3 / Deut 18 / Deut 31 / Deut 32 / Deut 33 row (the kin\\'s reading — the commission Numbers 27:12-23 for 34:1-4 and 34:9; Aaron\\'s death Numbers 20 for 34:5-8; the mountains of Abarim Numbers 33:47-48 for Nebo and the plains of Moab; Moses\\' plea 3:23-29 and Pisgah for 34:1; go up to Nebo 32:48-52 for 34:1 and 34:5; the hundred and twenty years and Joshua\\'s charge 31 for 34:7 and 34:9; the land sworn to the fathers Genesis 12:7, 13:15, 15:18 for 34:4; Jacob\\'s and Joseph\\'s deaths and the thirty days Genesis 50 for 34:8; face to face Exodus 33:11 and mouth to mouth Numbers 12:6-8 for 34:10; the prophet like Moses 18:15; Joshua the minister Exodus 24:13 and Numbers 11:28; the signs and wonders Exodus 4-7 and 4:34, 7:19, 29:2 for 34:11-12; the man of God and the lawgiver\\'s portion 33:1 and 33:21 for the grave):', "
       "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Gen (?:12|13|15|50)|Exod (?:4|7|24|33)|Num (?:11|12|20|27|33)|Deut (?:1|3|18|31|32|33)):', t, re.M)), " + PROPHETS)
EDGE = "print('  THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — chapter 34 the unit, CHAPTER NUMBERS, THE LAST CHAPTER OF THE BOOK (357 on 34:1 its piska, the export\\'s last; no piska after it) — THE SPINE IN FORCE: the Sifrei\\'s heads on chapter 34 by verse, and the verses without a head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])"
s = s0
def sub(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
sub("import subprocess; ROOT = _ROOT", GIT)   # the copier's portable line (the forms' copy) back to the scratch form
i = s.index('# DEUTERONOMY CHAPTER 33 — THE BLESSING'); j = s.index('import json, re, html')
HDR = (f"# DEUTERONOMY CHAPTER {CH} — THE DEATH OF MOSES, THE ONE CHAPTER OF SITTING 22, THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 22, 2026-09-30; the owner:\n"
       f"# \"Reread and go\" after the compaction that followed sitting 21b's tail — THE LEAN PASS's seventeenth sitting, its ninth reading; the Sifrei's spine in force at 357 on 34:1,\n"
       f"# the export's last piska; DEUTERONOMY'S LAST CHAPTER) — THE FIRST MEASUREMENT PASS for chapter {CH}, nothing typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to\n"
       f"# the DB's by the monotone alignment over token and negation counts, never by a typed table; (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 335-357, the export's\n"
       f"# end; the whole export scanned in both files for rows citing chapter {CH}; THE HEAD REGEX TOLERATES A COMMA after the chapter's letters — sitting 21's widening kept); (B) the\n"
       f"# Onkelos dump per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts (one\n"
       f"# on file — deu_34_moses_death, 34:1-12); (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the heads (guarded as sitting 19 left it; THE HEADS-AFTER PRINT\n"
       f"# GUARDED — no piska after 357). Sitting 21's form (the forms' ch33_dump0.py) derived by asserted substitutions (derive_ch34_dump0.py); the portion edge: Vezot Habrachah is\n"
       f"# 33:1-34:12 — chapter 34 the unit, CHAPTER NUMBERS, the book's last; the verse count in the DB's numbering measured at A0, never typed.\n")
s = s[:i] + HDR + s[j:]
sub("CH = 33\n", f"CH = {CH}\n")
sub("chapters 1-33:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 34)", "chapters 1-34:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 35)")
sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(33):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
sub("the English citations of chapter 33 are read as they print", f"the English citations of chapter {CH} are read as they print")
sub(r"""re.finditer(r'\((?:Ibid|ibid)\.? ?33:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?%d:(\d+)\)', clean(row))]""" % CH)
sub("print('  EN \"ibid 33:n\" candidates:'", f"print('  EN \"ibid {CH}:n\" candidates:'")
for fn in ('ch33_sifrei_outside.txt', 'ch33_onkelos.txt', 'ch33_store_glosses.txt', 'ch33_sifrei_spine.txt'): sub(fn, fn.replace('ch33_', f'ch{CH}_'), 2)
sub("Deut 33:", f"Deut {CH}:", 6)
sub("Deut(?:eronomy)? 33:", f"Deut(?:eronomy)? {CH}:", 3)
sub("Onkelos Deut 33 row", f"Onkelos Deut {CH} row")
sub("glob.glob(f'{ROOT}/logic/units/deu_32*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_33*.yaml')", f"glob.glob(f'{{ROOT}}/logic/units/deu_{CH - 1}*.yaml') + glob.glob(f'{{ROOT}}/logic/units/deu_{CH}*.yaml')")
sub("    if uid.startswith('deu_33'): print(", f"    if uid.startswith('deu_{CH}'): print(")
sub("for p in ('DV33', 'DV33A', 'DV33B', 'DV32', 'DV34')})", f"for p in ('DV{CH}', 'DV{CH}A', 'DV{CH}B', 'DV{CH - 1}', 'DV{CH + 1}')}})")
sub("existing manifests deu_33*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_33*'))", f"existing manifests deu_{CH}*:', sorted(os.path.basename(f) for f in glob.glob(f'{{ROOT}}/logic/oral_audit/manifests/deu_{CH}*'))")
sub("overrides already for Deut.33:", f"overrides already for Deut.{CH}:"); sub('Deut\\.33\\.', f'Deut\\.{CH}\\.'); sub("by_ref last Deut.32 line:", f"by_ref last Deut.{CH - 1} line:"); sub("l.startswith('  \"Deut.32.')", f"l.startswith('  \"Deut.{CH - 1}.')")
sub("(the spine on the chapter a twenty-fifth time — THE BLESSING: 342 on 33:1 onward, the comma in the head of 342 tolerated), whole')", f"(the spine on the chapter {ORD}), whole')")
# THE HEADS-AFTER PRINT GUARDED: 357 is the export's last piska — heads[358] does not exist
sub("'| the heads before and after:', {p: heads[p] for p in ((SPINE[0] - 1, SPINE[-1] + 1) if SPINE else ())})",
    "'| the heads before and after (a missing neighbour is the export\\'s end):', {p: heads.get(p, 'NO PISKA — the export ends') for p in ((SPINE[0] - 1, SPINE[-1] + 1) if SPINE else ())})")
i = s.index("print('  THE PORTION EDGE: Vezot Habrachah is 33:1-34:12"); j = s.index('\n', i); s = s[:i] + EDGE + s[j:]
i = s.index("print('  ledgers with an Onkelos Gen 27 / Gen 35"); j = s.index('\n', i); s = s[:i] + KIN + s[j:]
chk = s.replace("the forms' ch33_dump0.py", '').replace("342's head (Deuteronomy 33:1) is printed with one — the export's one comma head, headless to sitting 20's instrument", '').replace("Sitting 21's form", '').replace(f"'DV{CH - 1}'", '').replace(f'deu_{CH - 1}*', '').replace(f'Deut.{CH - 1}', '').replace(f'Deut\\.{CH - 1}', '').replace(KIN, '').replace(HDR, '').replace('33:1-34:12', '')
left = re.findall(r'.{40}(?:ch33_|Deut 33|chapter 33|Deut\\\.33|deu_33|DV33|33:1-29|THE BLESSING|a twenty-fifth|342|356).{40}', chk)
assert not left, left
assert "Moses'" not in re.sub(r'#[^\n]*', '', s).replace("\\'", ''), 'an apostrophe inside a single-quoted print'
ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
