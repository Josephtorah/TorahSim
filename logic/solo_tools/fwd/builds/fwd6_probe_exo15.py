#!/usr/bin/env python3
"""exo_15 claim probes — run from repo root."""
import sqlite3
db = sqlite3.connect("torah_grok.SNAPSHOT-main-51801ca.sqlite")
DAGESH = "ּ"
PASEQ = "׀"

def census(sp):
    return db.execute("""SELECT v.book, v.chapter, v.verse FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE replace(w.he_plain,'/','')=? ORDER BY v.book,v.chapter,v.verse""", (sp,)).fetchall()

def tok(book, ch, vs, idx, col="he"):
    return db.execute(f"SELECT w.{col} FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? AND w.idx=?", (book, ch, vs, idx)).fetchone()[0]

def adjacency(first, second_set):
    hits = []
    for b, c, v, i in db.execute("""SELECT v.book, v.chapter, v.verse, w.idx FROM words w
            JOIN verses v ON w.verse_id=v.id WHERE replace(w.he_plain,'/','')=?""", (first,)):
        nxt = db.execute("SELECT w.he_plain FROM words w JOIN verses vv ON w.verse_id=vv.id "
                         "WHERE vv.book=? AND vv.chapter=? AND vv.verse=? AND w.idx=?", (b, c, v, i + 1)).fetchone()
        if nxt and nxt[0].replace("/", "") in second_set:
            hits.append((b, c, v))
    return sorted(hits)

print("== az yashir pair");  print("   ", adjacency("אז", {"ישיר"}))
print("== am zu");  print("   ", adjacency("עם", {"זו"}))
print("== be-lev yam");  print("   ", adjacency("בלב", {"ים"}))
print("== choq u-mishpat");  print("   ", adjacency("חק", {"ומשפט"}))
print("== kamokha-with-he / ba-elim")
print("   כמכה", census("כמכה"), " כמוך count:", len(census("כמוך")), " באלם", census("באלם"))
r = db.execute("SELECT w.idx, w.he_plain, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=11 ORDER BY w.idx").fetchall()
print("   15:11:", [(i, hp.replace('/',''), repr(he)) for i, hp, he in r])
print("== 15:1 gaoh gaah")
r = db.execute("SELECT w.idx, w.he_plain, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=1 ORDER BY w.idx").fetchall()
print("   ", [(i, hp.replace('/','')) for i, hp, he in r])
print("   gaah tokens:", [repr(he) for i, hp, he in r if "גא" in hp.replace('/','')])
print("== 15:16 ka-even")
r = db.execute("SELECT w.idx, w.he_plain, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=16 ORDER BY w.idx").fetchall()
print("   ", [(i, hp.replace('/','')) for i, hp, he in r])
print("   kaeven:", [repr(he) for i, hp, he in r if hp.replace('/','') == "כאבן"])
print("== 15:13 gaalta")
print("   ", repr(tok("Exod", 15, 13, 3)))
r = db.execute("SELECT w.idx, w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=13 ORDER BY w.idx").fetchall()
print("   15:13:", [(i, hp.replace('/','')) for i, hp in r])
print("== 15:18 the paseq")
r = db.execute("SELECT w.idx, w.he_plain, w.he, w.mark_id FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=18 ORDER BY w.idx").fetchall()
print("   ", [(i, hp.replace('/',''), repr(he), m) for i, hp, he, m in r])
print("== afekha / teshalach / vayisa / markevot / u-mivchar / qamekha / le-shivtekha / uzi / be-khoach / achaz / tzalalu / marata / nachita / kaoferet / zeroakha / geonkha / bimtzolot / yekhasyumu")
for sp in ["אפיך", "תשלח", "ויסע", "מרכבות", "ומבחר", "קמיך", "לשבתך", "עזי", "בכח", "אחז", "צללו", "מרתה", "נחית", "כעפרת", "העפרת", "זרועך", "זרעך", "גאונך", "במצולת", "יכסימו"]:
    c = census(sp)
    print("   ", sp, c if len(c) < 7 else str(len(c)) + " stations")
print("== 15:5 yekhasyumu token:", repr(tok("Exod", 15, 5, 1)))
r = db.execute("SELECT w.idx, w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=5 ORDER BY w.idx").fetchall()
print("   15:5:", [(i, hp.replace('/','')) for i, hp in r])
print("== the healer's pe: 15:26 rofekha / 21:19 yerape")
r = db.execute("SELECT w.idx, w.he_plain, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=26 ORDER BY w.idx").fetchall()
print("   15:26:", [(i, hp.replace('/','')) for i, hp, he in r])
print("   rofekha:", [repr(he) for i, hp, he in r if "רפא" in hp.replace('/','')])
r = db.execute("SELECT w.idx, w.he_plain, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=21 AND v.verse=19 ORDER BY w.idx").fetchall()
print("   21:19 rape-tokens:", [(i, hp.replace('/',''), repr(he)) for i, hp, he in r if "רפ" in hp.replace('/','')])
print("== 15:20 miriam")
r = db.execute("SELECT w.idx, w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Exod' AND v.chapter=15 AND v.verse=20 ORDER BY w.idx").fetchall()
print("   ", [(i, hp.replace('/','')) for i, hp in r])
G = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"כ":20,"ך":20,"ל":30,"מ":40,"ם":40,"נ":50,"ן":50,"ס":60,"ע":70,"פ":80,"ף":80,"צ":90,"ץ":90,"ק":100,"ר":200,"ש":300,"ת":400}
g = lambda s: sum(G[c] for c in s if c in G)
print("== gematria: leshivtekha", g("לשבתך"), " yerushalayim+tziyon", g("ירושלים") + g("ציון"))
print("   machala", g("מחלה"), " anagram bread/salt:", sorted("מחלה") == sorted("הלחם") == sorted("המלח"))
print("   sham", g("שם"), " para aduma", g("פרהאדומה"))
