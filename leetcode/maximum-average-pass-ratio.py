#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        import heapq
        hp = []
        S = 10 ** 6
        base = 0
        for p, t in classes:
            d = (p+1) * S / (t+1) - p * S / t
            hp.append((-d, p+1, t+1))
            base += p * S / t
        heapq.heapify(hp)

        ans = 0
        for _ in range(extraStudents):
            d, p, t = heapq.heappop(hp)
            ans += -d
            d2 = (p+1) *S / (t+1) - p * S /t
            heapq.heappush(hp, (-d2, p+1, t+1))

        ans += base
        ans = (ans / S) / len(classes)
        ans = round(ans, 5)
        return ans

cases = [
    ([[1,2],[3,5],[2,2]], 2, 0.78333),
    ([[2,4],[3,9],[4,5],[2,10]],  4, 0.53485)
]

import aatest_helper
aatest_helper.run_test_cases(Solution().maxAverageRatio, cases)


if __name__ == '__main__':
    pass
