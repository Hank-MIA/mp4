#!/usr/bin/env python3
import sys


for line in sys.stdin:
    word, num = line.split('\t')
    if word != '' and num != '':
        print('%s\t%s' % (num, word))


