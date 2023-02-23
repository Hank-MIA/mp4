#!/usr/bin/env python3
import sys


for line in sys.stdin:
    parent, kids = line.split(':')
    parent = parent.strip()
    print('%s\t%s' % (parent, 'P'))  # possibly orphan

    children = kids.strip().split(' ')
    for child in children:
        if child != '':
            print('%s\t%s' % (child, 'N'))  # definitely not orphan
