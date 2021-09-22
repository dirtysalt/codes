#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rs = [tuple(x) for x in rides]
        import heapq
        heapq.heapify(rs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1], dp[i])
            while rs and rs[0][0] == i:
                (s, e, t) = heapq.heappop(rs)
                dp[e] = max(dp[e], dp[s] + (e - s + t))

        ans = dp[-1]
        return ans


true, false, null = True, False, None
cases = [
    (5, [[2, 5, 4], [1, 5, 1]], 7),
    (20, [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]], 20),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxTaxiEarnings, cases)

if __name__ == '__main__':
    pass
