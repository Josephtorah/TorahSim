SP = '<scratch>'
p = f'{SP}/derive_ch11_docket_writer.py'; t = open(p, encoding='utf-8').read()
anchor = '''sub_in_line("NWHOLE = sum(1 for vd, note in V.values() if '[whole:' in note)", "assert NWHOLE == TOT['corrected'] == 0, (NWHOLE, TOT)"'''
assert t.count(anchor) == 1, t.count(anchor)
add = '''sub_in_line("NWHOLE = sum(1 for vd, note in V.values() if '[whole:' in note)", "if '[whole:' in note)", "if '[whole:' in note and '; carried) — ' not in note[:200])")   # a carried note may hold its own docket's [whole:] mark
'''
t = t.replace(anchor, add + anchor); open(p, 'w', encoding='utf-8').write(t); print("derivation patched (NWHOLE over this docket's own notes)")
