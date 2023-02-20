#!/usr/bin/env python3
from operator import itemgetter
import sys

wordCounts = dict()

# input comes from STDIN
for line in sys.stdin:
    word = line.split('\t')[0]
    if word != '':
        wordCounts[word] = wordCounts.get(word, 0) + 1

for k, v in wordCounts.items():
    print('%s\t%s' % (k, v))
