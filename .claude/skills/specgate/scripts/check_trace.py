"""SpecGate audit helper: two-way OQ trace check and Section 9 counts.

Usage: python check_trace.py spec/<slug> vN
Reads SRS_<slug>_vN.md and REGISTER_<slug>_vN.md. Prints mismatches and counts.
Exit code 1 if any mismatch or count disagreement is found.
"""
import re, sys, os, collections

folder, ver = sys.argv[1], sys.argv[2]
slug = os.path.basename(os.path.normpath(folder))
srs = open(os.path.join(folder, f'SRS_{slug}_{ver}.md'), encoding='utf-8').read()
reg = open(os.path.join(folder, f'REGISTER_{slug}_{ver}.md'), encoding='utf-8').read()

ROW = re.compile(r'^\| ((?:ACT|FR|NFR|CON|GLO|DEP|ASM|RSK|AC)-\d+) \|(.*)$', re.M)
OQROW = re.compile(r'^\| (OQ-\d+) \| (\w+) \|(.*)$', re.M)
OQID = re.compile(r'OQ-\d+')
ID = re.compile(r'\b(?:ACT|FR|NFR|CON|GLO|DEP|ASM|RSK)-\d+\b')


def expand(text):
    """Expand ranges like 'FR-001 to FR-005'."""
    out = set(ID.findall(text))
    for p, a, b in re.findall(r'\b([A-Z]+)-(\d+) to \1-(\d+)', text):
        out |= {f'{p}-{i:03d}' for i in range(int(a), int(b) + 1)}
    return out


cites = collections.defaultdict(set)   # row id -> OQs it cites
for rid, rest in ROW.findall(srs + '\n' + reg):
    cites[rid] |= set(OQID.findall(rest))

header = [h.strip() for h in re.search(r'^\| ID \| Severity \|(.*)$', reg, re.M).group(0).strip('|').split('|')]
aff_col = header.index('Affects')
answer_col = header.index('Answer') if 'Answer' in header else None
affects, sev, answered = {}, {}, {}
for line in reg.splitlines():
    m = OQROW.match(line)
    if not m:
        continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    affects[m.group(1)] = expand(cells[aff_col])
    sev[m.group(1)] = m.group(2)
    answered[m.group(1)] = bool(answer_col is not None and cells[answer_col])

bad = []
for oq, ids in affects.items():
    for i in ids:
        if i not in cites:
            bad.append(f'{oq} affects {i}, but {i} has no row')
        elif oq not in cites[i]:
            bad.append(f'{oq} affects {i}, but {i} does not cite {oq}')
for rid, oqs in cites.items():
    for oq in oqs:
        if oq in affects and rid not in affects[oq]:
            bad.append(f'{rid} cites {oq}, but {oq} does not list {rid}')

req = re.findall(r'^\| ((?:FR|NFR|CON)-\d+) \|(.*)$', srs, re.M)
status = collections.Counter()
ready = collections.Counter()
for rid, rest in req:
    cells = [c.strip() for c in rest.split('|')]
    st = next((c for c in cells if c in {'STATED', 'INFERRED', 'EXTERNALLY_SUPPORTED', 'SLOT', 'UNRESOLVED', 'CONFIRMED'}), None)
    rd = next((c for c in cells if c in {'READY', 'NEEDS_CLARIFICATION'}), None)
    if st is None or rd is None:
        bad.append(f'{rid} has no status or readiness cell')
        continue
    status[st] += 1
    ready[rd] += 1

ids_all = [r for r, _ in ROW.findall(srs + '\n' + reg)]
dups = [i for i, n in collections.Counter(ids_all).items() if n > 1 and not i.startswith(('ASM', 'RSK'))]

print(f'Requirement rows: {len(req)}')
print('By status:', dict(status), '=', sum(status.values()))
print('By readiness:', dict(ready), '=', sum(ready.values()))
openq = collections.Counter(sev[q] for q in sev if not answered[q])
print(f'OQ rows: {len(sev)}; answered {sum(answered.values())}; open by severity: {dict(openq)}')
print('Duplicate IDs:', dups or 'none')
print('Trace mismatches:', bad or 'none')
ok = not bad and not dups and sum(status.values()) == sum(ready.values()) == len(req)
sys.exit(0 if ok else 1)
