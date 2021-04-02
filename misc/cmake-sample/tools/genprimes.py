#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

def genprimes(n):
    mark = [0] * (n+1)
    mark[0] = mark[1] = 1
    for i in range(2, n):
        if i * i > n: break
        if mark[i] == 1: break
        for j in range(i, n):
            if i * j > n: break
            mark[i * j] = 1
    return mark

def main(argv):
    fileOutput = argv[1]
    n= 100000
    mark = genprimes(n);
    with open(fileOutput, 'w') as fh:
        fh.write('static int _primes[] = {\n')
        for i in range(len(mark)):
            if i % 20 == 0:
                fh.write('\n')
            fh.write(str(1-mark[i]) + ',')
        fh.write('};')

if __name__ == '__main__':
    import sys
    main(sys.argv)
