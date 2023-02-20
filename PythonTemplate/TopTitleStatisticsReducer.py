#!/usr/bin/env python3
import sys
import math


total = 0
count = 0
inputs = []
for line in sys.stdin:
    _, numStr = line.split('\t')
    numStr = numStr.strip()
    if numStr != '':
        num = int(numStr)
        total += num
        count += 1
        inputs.append(num)

average = math.floor(total / count)
print('Mean\t%s' % average)
print('Sum\t%s' % total)
print('Min\t%s' % min(inputs))
print('Max\t%s' % max(inputs))

variance = sum([(i-average)**2 for i in inputs]) / count
print('Var\t%s' % math.floor(variance))
