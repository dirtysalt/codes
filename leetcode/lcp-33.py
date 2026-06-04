#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        hp = []
        adj = 0

        def times(v, b):
            return (v + b - 1) // b

        for i in range(n):
            b, v = bucket[i], vat[i]
            if v == 0: continue
            if b == 0:
                hp.append((-v // 1, 1, v))
                adj += 1
            else:
                hp.append((-times(v, b), b, v))
        if not hp: return 0

        import heapq
        heapq.heapify(hp)
        ans = 1 << 30

        while True:
            step, b, v = heapq.heappop(hp)
            step = -step
            if (step + adj) < ans:
                ans = (step + adj)
            if step == 1:
                break

            adj += 1
            b += 1
            heapq.heappush(hp, (-times(v, b), b, v))

        return ans

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)

        maxvat = max(vat)
        if maxvat == 0: return 0

        ans = 1 << 30
        for t in range(1, maxvat+1):
            adj = 0
            for i in range(n):
                b, v= bucket[i], vat[i]
                minb = (v + t - 1)// t
                adj += max(0, minb - b)
            res = adj + t
            ans = min(ans, res)
        return ans


cases = [
    ([1,3],  [6,8], 4),
    ([9,0,1], [0,2,2], 3),
    ([0], [0], 0),
    ([0], [1], 2),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().storeWater, cases)


if __name__ == '__main__':
    pass
