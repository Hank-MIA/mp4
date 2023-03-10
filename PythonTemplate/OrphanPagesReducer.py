#!/usr/bin/env python3
import sys


pp = dict()

for line in sys.stdin:
    line = line.strip()
    if line:
        name, isOrphan = line.split('\t')
        if pp.get(name, 'P') == 'N':
            continue
        pp[name] = isOrphan.strip()

orphanList = []
for k, v in pp.items():
    if v == 'P':
        orphanList.append(int(k))

orphanList.sort()
for orphan in orphanList:
    print(orphan)

