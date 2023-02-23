#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
leagueSet = set()


with open(leaguePath) as f:
    line = f.readline().strip()
    while line:
        leagueSet.add(line)
        line = f.readline().strip()


for line in sys.stdin:
    line = line.strip()
    if line:
        mem, numStr = line.strip().split('\t')
        if mem in leagueSet:
            print(line.strip())

