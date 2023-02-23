#!/usr/bin/env python3
import sys


for line in sys.stdin:
    if line.strip():
        _, links = line.split(':')
        links = links.strip()
        for link in links.split(' '):
            print('%s\t%s' % (link, 1))

