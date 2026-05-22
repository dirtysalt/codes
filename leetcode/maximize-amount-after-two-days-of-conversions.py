#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import defaultdict
from typing import List


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]],
                  rates2: List[float]) -> float:
        dist = defaultdict(float)
        dist[initialCurrency] = 1.0

        def convert(dist, pairs, rates):
            changed = True
            while changed:
                changed = False
                update = dist.copy()
                for (a, b), r in zip(pairs, rates):
                    v = dist[a]
                    v2 = v * r
                    if v2 > update[b]:
                        changed = True
                        update[b] = v2
                    v = dist[b]
                    v2 = v / r
                    if v2 > update[a]:
                        changed = True
                        update[a] = v2
                dist = update
            return dist

        A = convert(dist, pairs1, rates1)
        B = convert(A, pairs2, rates2)
        return B[initialCurrency]


if __name__ == '__main__':
    pass
