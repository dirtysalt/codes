#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        # print(packages)
        n = len(boxes)
        lastPack = [-1] * n
        cost = [0] * n

        NP = len(packages)
        acc = [0] * (NP+1)
        for i in range(NP):
            acc[i+1] = packages[i] + acc[i]


        def searchMaxPack(size, s):
            s = s + 1
            e = len(packages) - 1
            while s <= e:
                m = (s + e) // 2
                if packages[m] > size:
                    e = m - 1
                else:
                    s = m + 1
            return e

        ev = []
        for i in range(n):
            for b in boxes[i]:
                ev.append((b, i))
        ev.sort()

        for sz, idx in ev:
            last = lastPack[idx]
            if last == (NP-1): continue
            now = searchMaxPack(sz, last)
            accSize = acc[now + 1] - acc[last + 1]
            # print(idx, sz, last, now, accSize)
            cost[idx] += (now - last) * sz - accSize
            lastPack[idx] = now

        inf = 1 << 63
        ans = inf
        MOD = 10 ** 9 + 7
        for i in range(n):
            if lastPack[i] != (NP-1):
                continue
            ans = min(ans, cost[i])
        if ans == inf:
            return -1
        return ans % MOD

cases = [
    ([2,3,5],[[4,8],[2,8]],6),
         ([2,3,5],[[1,4],[2,3],[3,4]],-1),
([3,5,8,10,11,12],[[12],[11,9],[10,5,14]],9),
([1,1,1,1],[[4]], 12),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minWastedSpace, cases)



if __name__ == '__main__':
    pass
