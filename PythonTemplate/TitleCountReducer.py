#!/usr/bin/env python3
from operator import itemgetter
import sys

"""
class KeyValue(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __lt__(self, other):
        return self.val < other.val or (self.val == other.val and self.key < other.key)
"""

wordCounts = dict()

# input comes from STDIN
for line in sys.stdin:
    word = line.split('\t')[0]
    wordCounts[word] = wordCounts.get(word, 0) + 1

for k, v in wordCounts.items():
    print('%s\t%s' % (k, v))

"""
minheap = []
for k, v in wordCounts.items():
    heapq.heappush(minheap, KeyValue(k, v))
    if len(minheap) > 5:
        heapq.heappop(minheap)


while minheap:
    kv = heapq.heappop(minheap)
    print('%s\t%s' % (kv.key, kv.val))
"""