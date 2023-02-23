#!/usr/bin/env python3
import sys
import heapq

minHeap = []

# input comes from STDIN
for line in sys.stdin:
    link, numStr = line.strip().split('\t')
    num = int(numStr)
    heapq.heappush(minHeap, (num, link))
    if len(minHeap) > 5:
        heapq.heappop(minHeap)

while heapq:
    num, link = heapq.heappop(minHeap)
    print('%s\t%s' % (link, num))

