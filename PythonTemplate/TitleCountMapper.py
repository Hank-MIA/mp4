#!/usr/bin/env python3

import sys
import re

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
stopWords = set()
delimiters = []
delimiterReg = ''

with open(stopWordsPath) as f:
    line = f.readline()
    while line:
        stopWords.add(line.strip())
        line = f.readline()


with open(delimitersPath) as f:
    line = f.readline()
    while line:
        delimiters.extend([*(line.strip())])
        line = f.readline()
for d in delimiters:
    delimiterReg += '\\' + d + '|'
delimiterReg = delimiterReg[:-1]


for line in sys.stdin:
    words = re.split(delimiterReg, line)
    for key in words:
        token = key.strip().lower()
        if token != '' and token not in stopWords:
            print('%s\t%s' % (token, 1))


# print('%s\t%s' % (  ,  )) pass this output to reducer


