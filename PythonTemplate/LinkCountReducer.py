#!/usr/bin/env python3
import sys

linkCount = dict()

# input comes from STDIN
for line in sys.stdin:
    if line.strip():
        link, _ = line.split('\t')
        linkCount[link] = linkCount.get(link, 0) + 1

for k, v in linkCount.items():
    print('%s\t%s' % (k, v))

