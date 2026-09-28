import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import os, sys, io, contextlib, subprocess, inspect, traceback, sqlite3
ROOT = _ROOT; sys.path.insert(0, ROOT + '/World/step9')
def load(n):
    with contextlib.redirect_stdout(io.StringIO()): return __import__('cold_run_' + n)
HO = load('holiness'); SA = load('sanctions'); JO = load('joseph'); OS = load('opening_speech'); GL = load('good_land')
for f in (lambda: HO.conduct('stumbling'), lambda: HO.conduct(q='stumbling'), lambda: HO.gifts('kinds'), lambda: SA.grade('fathers_wife'), lambda: SA.grade('sister'), lambda: SA.grade('mother_in_law'), lambda: SA.grade('beast'), lambda: JO.seventy('seventy'), lambda: JO.seventy('exodus_seventy'), lambda: OS.the_frame({'ask': 'the_frame'}, getattr(OS, 'DATA', {})), lambda: GL.narrative()):
    try: v = f(); print('FACT', inspect.getsource(f).strip()[:70], '=', repr(v)[:420])
    except Exception:
        print('FAIL', inspect.getsource(f).strip()[:70]); traceback.print_exc(limit=2)
print('OS.the_frame asks:', __import__('re').findall(r"if ask == '([a-z_0-9]+)':", inspect.getsource(OS.the_frame))[:12])
print('HO.conduct source head:', inspect.getsource(HO.conduct)[:600].replace('\n', ' | '))
db = sqlite3.connect('file:%s/Data/tanakh.sqlite?mode=ro' % ROOT, uri=True)
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
print('the token BAER (explain) in the Torah:', [(b, c, v) for b, c, v, he in db.execute("SELECT v.book, v.chapter, v.verse, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut')") if pl(he) == 'באר'])
