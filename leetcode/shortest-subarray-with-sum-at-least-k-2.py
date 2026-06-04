#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        hp = []
        hp.append((0, -1))
        import heapq

        acc = 0
        n = len(A)
        ans = n + 1
        for i in range(n):
            x = A[i]
            acc += x

            while hp and (acc - hp[0][0]) >= K:
                (_, j) = heapq.heappop(hp)
                ans = min(ans, i - j)
            heapq.heappush(hp, (acc, i))

        if ans == (n + 1):
            ans = -1
        return ans


cases = [
    ([17, 85, 93, -45, -21], 150, 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().shortestSubarray, cases)
