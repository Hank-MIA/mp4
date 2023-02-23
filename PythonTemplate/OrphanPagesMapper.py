#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    if line:
        parent, kids = line.split(':')
        parent = parent.strip()
        print('%s\t%s' % (parent, 'P'))  # possibly orphan

        children = kids.strip().split(' ')
        for child in children:
            if child != '' and child != parent:
                print('%s\t%s' % (child, 'N'))  # definitely not orphan
