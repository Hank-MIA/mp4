#!/usr/bin/env python3
import sys
import heapq

minHeap = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    if line:
        link, numStr = line.split('\t')
        num = int(numStr)
        heapq.heappush(minHeap, (num, link))
        if len(minHeap) > 10:
            heapq.heappop(minHeap)

while minHeap:
    num, link = heapq.heappop(minHeap)
    print('%s\t%s' % (link, num))

