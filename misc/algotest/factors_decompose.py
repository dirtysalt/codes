#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

def makeprimes(n):
    p = [0] * (n + 1)
    sz = len(p)
    for i in range(2, sz):
        if i * i >= sz: break
        if p[i] == 1: break
        for j in range(i, sz):
            if i * j >= sz: break
            p[i*j]=1
    return [x for x in range(2, sz) if p[x] == 0]

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def findfactors(x, primes):
    factors = [1]
    for p in primes:
        if x < p: break
        if x % p == 0:
            rep = 0
            while x % p == 0:
                rep += 1
                x = x // p

            b = 1
            up = []
            for i in range(rep):
                b = b * p
                for ft in factors:
                    up.append(b * ft)
            factors.extend(up)

    maxf = max(factors)
    rem = []
    for f in factors:
        f2 = x // f
        if f2 > maxf:
            rem.append(f2)
    factors.extend(rem)
    return factors

class FactorsDecomposer:
    def __init__(self, n):
        self.n = n
        self.primes = makeprimes(int(n** 0.5) + 1)

    def decompose(self, x):
        return findfactors(x, self.primes)

fd = FactorsDecomposer(200000)
factors = fd.decompose(166320)
print(factors, len(factors))
