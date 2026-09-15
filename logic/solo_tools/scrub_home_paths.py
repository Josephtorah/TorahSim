#!/usr/bin/env python3
"""scrub_home_paths.py — NO MACHINE USERNAME IN THE PROJECT (the owner, 2026-09-15: "I don't want <user> in any of this project" — the
Mac's login name; and the older Mac's, the same rule). One pass replaces every form of a home path or a Claude Code project folder with
a neutral marker, in every tracked text file — records included, the ledgers' append-only law set aside for a machine artifact on the
owner's word — and in the memory folder; the same table feeds the history rewrite (git filter-repo --replace-text). Kept as the record.

    python3 logic/solo_tools/scrub_home_paths.py --dry                 # counts by pattern and by file, nothing written
    python3 logic/solo_tools/scrub_home_paths.py --apply [--memory DIR]  # rewrite the tracked text files (and the memory folder)
    python3 logic/solo_tools/scrub_home_paths.py --check               # THE GATE: any username or home path in a tracked text file → exit 1
    python3 logic/solo_tools/scrub_home_paths.py --expressions FILE    # write git filter-repo's replace-text expressions to FILE

THE MARKERS: <repo> this repo's folder; <repo-old> its old name; <world-link> the World symlink; <scratch> a session's scratch folder;
<memory> the memory folder; <claude-project> / <claude-projects> Claude Code's project folders; <home> / <old-home> the two home
folders; <project-folder> / <project-folder-old> / <old-mac-project-folder> the project folders' names; <user> / <old-user> the bare names.
The two names are composed at run time so this file carries neither."""
import os, re, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
U1 = 'ben' + 'gal'                      # this Mac's login
U2 = 'brian' + 'leblanc'                # the older Mac's login
TABLE = [
    (r'/private/tmp/claude-501/-Users-(?:%s|%s)-[A-Za-z_-]+/[0-9a-f-]+/scratchpad' % (U1, U2), '<scratch>'),
    (r'/private/tmp/claude-501/-Users-(?:%s|%s)-[A-Za-z_-]+' % (U1, U2), '<scratch-root>'),
    (r'/Users/%s/\.claude/projects/-Users-%s-(?:TorahSim|Torah-Grok)/memory' % (U1, U1), '<memory>'),
    (r'/Users/%s/\.claude/projects/-Users-%s-(?:TorahSim|Torah-Grok)' % (U1, U1), '<claude-project>'),
    (r'/Users/%s/\.claude/projects' % U1, '<claude-projects>'),
    (r'/Users/%s/TorahSim' % U1, '<repo>'),
    (r'/Users/%s/Torah_Grok' % U1, '<repo-old>'),
    (r'/Users/%s/World' % U1, '<world-link>'),
    (r'/Users/%s/code/Torah-Grok' % U2, '<old-mac-repo>'),
    (r'/Users/%s/' % U1, '<home>/'),
    (r'/Users/%s/' % U2, '<old-home>/'),
    (r'-Users-%s-TorahSim' % U1, '<project-folder>'),
    (r'-Users-%s-Torah-Grok' % U1, '<project-folder-old>'),
    (r'-Users-%s-code-Torah[-_A-Za-z]*' % U2, '<old-mac-project-folder>'),
    (r'\b%s\b' % U1, '<user>'),
    (r'\b%s\b' % U2, '<old-user>'),
]
RX = [(re.compile(p), m) for p, m in TABLE]
BINARY = ('.epub', '.sqlite', '.db', '.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.gz', '.woff', '.woff2', '.ttf', '.mp3', '.m4a', '.ico')


def tracked():
    out = subprocess.run(['git', 'ls-files', '-z'], capture_output=True, text=True, cwd=ROOT).stdout
    return [f for f in out.split('\0') if f and not f.endswith(BINARY) and os.path.isfile(os.path.join(ROOT, f))]


def scrub(text):
    counts = {}
    for rx, marker in RX:
        text, n = rx.subn(marker, text)
        if n:
            counts[marker] = counts.get(marker, 0) + n
    return text, counts


def run(paths, apply, label):
    total, files = {}, 0
    for p in paths:
        try:
            s = open(p, encoding='utf-8').read()
        except (UnicodeDecodeError, OSError):
            continue
        new, counts = scrub(s)
        if not counts:
            continue
        files += 1
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        if apply:
            open(p, 'w', encoding='utf-8').write(new)
    print('%s (%s): %d files, %s' % (label, 'APPLIED' if apply else 'DRY', files, ', '.join('%s %d' % kv for kv in sorted(total.items(), key=lambda kv: -kv[1])) or 'nothing'))
    return files


def check():
    bad = []
    for f in tracked():
        try:
            s = open(os.path.join(ROOT, f), encoding='utf-8').read()
        except (UnicodeDecodeError, OSError):
            continue
        if U1 in s or U2 in s or re.search(r'/Users/(?!Shared/)[A-Za-z]+/', s) or re.search(r'-Users-(?!Shared-)[A-Za-z]+-', s):   # /Users/Shared is no one's home
            bad.append(f)
    print('THE HOME-PATH GATE: %s — %d tracked text files carry a username or a home path%s' % ('GREEN' if not bad else 'RED', len(bad), (': ' + ', '.join(bad[:6])) if bad else ''))
    return not bad


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--check' in a:
        sys.exit(0 if check() else 1)
    if '--expressions' in a:
        out = a[a.index('--expressions') + 1]
        with open(out, 'w', encoding='utf-8') as f:
            for p, m in TABLE:
                f.write('regex:%s==>%s\n' % (p, m))
        print('filter-repo expressions written:', out); sys.exit(0)
    apply = '--apply' in a
    run([os.path.join(ROOT, f) for f in tracked()], apply, 'the tracked text files')
    if '--memory' in a:
        d = a[a.index('--memory') + 1]
        run([os.path.join(d, f) for f in os.listdir(d) if f.endswith('.md')], apply, 'the memory folder')
