SP = '<scratch>'
p = f'{SP}/derive_ch11_docket_writer.py'; t = open(p, encoding='utf-8').read()
old = '''sub_in_line("NWHOLE = sum(1 for vd, note in V.values() if '[whole:' in note)", "assert NWHOLE == TOT['corrected'] == 0, (NWHOLE, TOT)"'''
new = '''sub_in_line("NWHOLE = sum(1 for vd, note in V.values()", "assert NWHOLE == TOT['corrected'] == 0, (NWHOLE, TOT)"'''
assert t.count(old) == 1; t = t.replace(old, new); open(p, 'w', encoding='utf-8').write(t); print('prefix shortened')
