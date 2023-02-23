#!/usr/bin/env python3
import sys
import heapq

minHeap = []
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    if line:
        link, numStr = line.split('\t')
        heapq.heappush(minHeap, (int(numStr), link))

indexedLinks = []
index = 0
valueSameIndex = 0
preVal, link = heapq.heappop(minHeap)
heapq.heappush((link, index))

while minHeap:
    val, link = heapq.heappop(minHeap)
    index += 1
    if val == preVal:
        heapq.heappush(indexedLinks, (link, valueSameIndex))
    else:
        heapq.heappush(indexedLinks, (link, index))
        valueSameIndex = index
        preVal = val

while indexedLinks:
    link, index = heapq.heappop(indexedLinks)
    print('%s\t%s' % (link, index))
