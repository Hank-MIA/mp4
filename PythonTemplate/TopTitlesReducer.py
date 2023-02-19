#!/usr/bin/env python3
import sys
import heapq

minHeap = []
# input comes from STDIN
for line in sys.stdin:
    numStr, word = line.split('\t')
    word = word.strip()
    if numStr != '' and word != '':
        num = int(numStr)
        heapq.heappush(minHeap, (num, word))
        if len(minHeap) > 5:
            heapq.heappop(minHeap)

while minHeap:
    num, word = heapq.heappop(minHeap)
    print('%s\t%s' % (word, num))
